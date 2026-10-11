#!/usr/bin/env python3
"""Validate all structured archive packs under data/structured/*/ against schemas + citation fail-closed gate.

Usage:
  .venv/bin/python tools/export_check.py
  python3 tools/export_check.py   # requires jsonschema

Exit 0 on success; non-zero on schema or citation failures.
Integrity rule: Claim kind=fact must have non-empty sources[] with resolvable src-* ids
in sources/*.md and in the same pack's sources/{id}.json.
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
        "  python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt\n"
        "  .venv/bin/python tools/export_check.py",
        file=sys.stderr,
    )
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
STRUCTURED = ROOT / "data" / "structured"
SOURCES_MD = ROOT / "sources"

ENTITY_SUBDIRS = ("sources", "sites", "periods", "objects", "claims", "media")

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

ENTITY_FROM_DIR = {
    "sources": "source",
    "sites": "site",
    "periods": "period",
    "objects": "object",
    "claims": "claim",
    "media": "media",
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
    return {p.stem for p in SOURCES_MD.glob("src-*.md")}


def discover_packs() -> list[Path]:
    if not STRUCTURED.is_dir():
        return []
    packs = []
    for p in sorted(STRUCTURED.iterdir()):
        if p.is_dir() and (p / "civilization.json").exists():
            packs.append(p)
    return packs


def check_pack(pack: Path, store: dict, registry: set[str], errors: list[str]) -> dict[str, int]:
    counts = {k: 0 for k in ("sources", "sites", "periods", "objects", "claims", "media")}
    rel_pack = pack.relative_to(ROOT)

    for subdir, entity in ENTITY_FROM_DIR.items():
        directory = pack / subdir
        if not directory.is_dir():
            # media may be empty; others required for a pack
            if subdir == "media":
                continue
            errors.append(f"missing directory: {rel_pack / subdir}")
            continue
        v = validator_for(entity, store)
        paths = sorted(directory.glob("*.json"))
        if entity != "media" and not paths:
            errors.append(f"no JSON instances under {rel_pack / subdir}")
        counts[subdir] = len(paths)
        for path in paths:
            data = load_json(path)
            for err in sorted(v.iter_errors(data), key=lambda e: list(e.path)):
                loc = "/".join(str(x) for x in err.path) or "(root)"
                errors.append(f"{path.relative_to(ROOT)} @ {loc}: {err.message}")

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
                        if not (pack / "sources" / f"{sid}.json").exists():
                            errors.append(
                                f"{path.relative_to(ROOT)}: citation gate FAIL — "
                                f"fact claim cites {sid!r} but pack sources/{sid}.json missing"
                            )
                if kind == "hypothesis":
                    if not (data.get("disclaimer") or "").strip():
                        errors.append(
                            f"{path.relative_to(ROOT)}: hypothesis claim missing disclaimer"
                        )

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

    civ_path = pack / "civilization.json"
    if civ_path.exists():
        v = validator_for("civilization", store)
        data = load_json(civ_path)
        for err in sorted(v.iter_errors(data), key=lambda e: list(e.path)):
            loc = "/".join(str(x) for x in err.path) or "(root)"
            errors.append(f"{civ_path.relative_to(ROOT)} @ {loc}: {err.message}")
        for sid in data.get("sources") or []:
            if sid not in registry:
                errors.append(f"{civ_path.relative_to(ROOT)}: unknown source id {sid!r}")
            if not (pack / "sources" / f"{sid}.json").exists():
                errors.append(
                    f"{civ_path.relative_to(ROOT)}: missing structured source {sid}.json"
                )
    else:
        errors.append(f"missing {rel_pack}/civilization.json")

    delib_path = pack / "deliberation.json"
    if delib_path.exists():
        v = validator_for("deliberation", store)
        data = load_json(delib_path)
        for err in sorted(v.iter_errors(data), key=lambda e: list(e.path)):
            loc = "/".join(str(x) for x in err.path) or "(root)"
            errors.append(f"{delib_path.relative_to(ROOT)} @ {loc}: {err.message}")

    return counts


def main() -> int:
    errors: list[str] = []
    store = load_schemas()
    registry = registered_source_ids()
    packs = discover_packs()

    if not packs:
        errors.append("no packs found under data/structured/*/civilization.json")

    summaries: list[str] = []
    for pack in packs:
        counts = check_pack(pack, store, registry, errors)
        summaries.append(
            f"  pack {pack.name}: sources={counts['sources']} sites={counts['sites']} "
            f"periods={counts['periods']} objects={counts['objects']} "
            f"claims={counts['claims']} media={counts['media']}"
        )

    if errors:
        print(f"export_check FAILED ({len(errors)} issue(s)):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print("export_check OK")
    print(f"  packs={len(packs)}")
    for line in summaries:
        print(line)
    print("  citation gate: fact claims require non-empty resolvable sources[]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
