#!/usr/bin/env python3
"""Validate structured archive pilot JSON against schemas + citation fail-closed gate.

Usage:
  .venv/bin/python tools/export_check.py
  python3 tools/export_check.py   # requires jsonschema

Exit 0 on success; non-zero on schema or citation failures.
Integrity rule: Claim kind=fact must have non-empty sources[] with resolvable src-* ids.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
    from jsonschema.validators import RefResolver
except ImportError:
    print(
        "ERROR: jsonschema not installed. Use:\n"
        "  python3 -m venv .venv && .venv/bin/pip install jsonschema\n"
        "  .venv/bin/python tools/export_check.py",
        file=sys.stderr,
    )
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
PILOT = ROOT / "data" / "structured" / "mesopotamia"
SOURCES_MD = ROOT / "sources"

ENTITY_DIRS = {
    "source": PILOT / "sources",
    "site": PILOT / "sites",
    "period": PILOT / "periods",
    "object": PILOT / "objects",
    "claim": PILOT / "claims",
    "media": PILOT / "media",
}

SCHEMA_FILES = {
    "source": "source.schema.json",
    "site": "site.schema.json",
    "period": "period.schema.json",
    "object": "object.schema.json",
    "claim": "claim.schema.json",
    "media": "media.schema.json",
    "civilization": "civilization.schema.json",
    "deliberation": "deliberation.schema.json",
}


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_schemas():
    store = {}
    for path in SCHEMAS.glob("*.json"):
        data = load_json(path)
        sid = data.get("$id")
        if sid:
            store[sid] = data
        # also key by filename for local $ref like "common.defs.json#/..."
        store[path.name] = data
        store[str(path)] = data
    return store


def validator_for(entity: str, store: dict) -> Draft202012Validator:
    schema_path = SCHEMAS / SCHEMA_FILES[entity]
    schema = load_json(schema_path)
    resolver = RefResolver(
        base_uri=schema_path.as_uri(),
        referrer=schema,
        store=store,
    )
    return Draft202012Validator(schema, resolver=resolver)


def registered_source_ids() -> set[str]:
    ids = set()
    for p in SOURCES_MD.glob("src-*.md"):
        ids.add(p.stem)
    return ids


def main() -> int:
    errors: list[str] = []
    store = load_schemas()
    registry = registered_source_ids()
    seen_source_ids: set[str] = set()

    # Per-entity instance files
    for entity, directory in ENTITY_DIRS.items():
        if not directory.is_dir():
            errors.append(f"missing directory: {directory.relative_to(ROOT)}")
            continue
        v = validator_for(entity, store)
        paths = sorted(directory.glob("*.json"))
        if entity != "media" and not paths:
            errors.append(f"no JSON instances under {directory.relative_to(ROOT)}")
        for path in paths:
            data = load_json(path)
            for err in sorted(v.iter_errors(data), key=lambda e: list(e.path)):
                loc = "/".join(str(x) for x in err.path) or "(root)"
                errors.append(f"{path.relative_to(ROOT)} @ {loc}: {err.message}")

            # Citation fail-closed for claims
            if entity == "claim":
                kind = data.get("kind")
                sources = data.get("sources") or []
                if kind == "fact":
                    if not sources:
                        errors.append(
                            f"{path.relative_to(ROOT)}: citation gate FAIL — "
                            "kind=fact requires non-empty sources[]"
                        )
                    for sid in sources:
                        if sid not in registry:
                            errors.append(
                                f"{path.relative_to(ROOT)}: citation gate FAIL — "
                                f"unknown source id {sid!r} (no sources/{sid}.md)"
                            )
                        if not (PILOT / "sources" / f"{sid}.json").exists():
                            errors.append(
                                f"{path.relative_to(ROOT)}: citation gate FAIL — "
                                f"fact claim cites {sid!r} but pilot sources/{sid}.json missing"
                            )
                if kind == "hypothesis":
                    if not (data.get("disclaimer") or "").strip():
                        errors.append(
                            f"{path.relative_to(ROOT)}: hypothesis claim missing disclaimer"
                        )

            if entity == "source":
                seen_source_ids.add(data.get("id"))
                # Media must not claim local binaries
            if entity == "media":
                if data.get("local_path") is not None:
                    errors.append(
                        f"{path.relative_to(ROOT)}: local_path must be null "
                        "(unverified uploads forbidden)"
                    )
                rights = data.get("rights") or {}
                if rights.get("status") == "forbidden-unverified-upload":
                    errors.append(
                        f"{path.relative_to(ROOT)}: rights.status forbidden-unverified-upload"
                    )

    # Civilization aggregate
    civ_path = PILOT / "civilization.json"
    if civ_path.exists():
        v = validator_for("civilization", store)
        data = load_json(civ_path)
        for err in sorted(v.iter_errors(data), key=lambda e: list(e.path)):
            loc = "/".join(str(x) for x in err.path) or "(root)"
            errors.append(f"{civ_path.relative_to(ROOT)} @ {loc}: {err.message}")
        for sid in data.get("sources") or []:
            if sid not in registry:
                errors.append(
                    f"{civ_path.relative_to(ROOT)}: unknown source id {sid!r}"
                )
            if not (PILOT / "sources" / f"{sid}.json").exists():
                errors.append(
                    f"{civ_path.relative_to(ROOT)}: missing structured source {sid}.json"
                )
    else:
        errors.append("missing data/structured/mesopotamia/civilization.json")

    # Optional deliberation stub
    delib_path = PILOT / "deliberation.json"
    if delib_path.exists():
        v = validator_for("deliberation", store)
        data = load_json(delib_path)
        for err in sorted(v.iter_errors(data), key=lambda e: list(e.path)):
            loc = "/".join(str(x) for x in err.path) or "(root)"
            errors.append(f"{delib_path.relative_to(ROOT)} @ {loc}: {err.message}")

    if errors:
        print(f"export_check FAILED ({len(errors)} issue(s)):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    n_src = len(list((PILOT / "sources").glob("*.json")))
    n_sites = len(list((PILOT / "sites").glob("*.json")))
    n_periods = len(list((PILOT / "periods").glob("*.json")))
    n_obj = len(list((PILOT / "objects").glob("*.json")))
    n_claims = len(list((PILOT / "claims").glob("*.json")))
    n_media = len(list((PILOT / "media").glob("*.json")))
    print("export_check OK")
    print(
        f"  pilot mesopotamia: sources={n_src} sites={n_sites} periods={n_periods} "
        f"objects={n_obj} claims={n_claims} media={n_media}"
    )
    print("  citation gate: fact claims require non-empty resolvable sources[]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
