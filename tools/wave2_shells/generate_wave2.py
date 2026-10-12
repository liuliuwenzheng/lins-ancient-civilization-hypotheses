#!/usr/bin/env python3
"""Generate Wave-2 civilization shells (D-2026-10-12-14). Integrity > speed; no invented archaeology."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TODAY = "2026-10-12"
ED = {
    "derived_from": ["tools/wave2_shells/generate_wave2.py", "docs/coverage-map.md", "docs/decisions.md#d-2026-10-12-14"],
    "derived_on": TODAY,
    "notes": "Wave-2 library-seed shell (D-2026-10-12-14). Abstract/TOC-level claims only; no invented pages, coords, or finds.",
}

def dump(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def write_source_md(s: dict) -> None:
    sid = s["id"]
    url = s.get("url") or ""
    access = TODAY if url else ""
    body = f"""---
id: {sid}
type: {s["type"]}
citation: {json.dumps(s["citation"], ensure_ascii=False)}
url: {json.dumps(url or None)}
access_date: {json.dumps(access or None)}
reliability_tier: {s["tier"]}
notes: {json.dumps(s.get("notes") or "", ensure_ascii=False)}
---

# Source: `{sid}`

| Field | Value |
|-------|--------|
| Type | {s["type"]} |
| Tier | {s["tier"]} |
| Citation | {s["citation"]} |
| URL | {url or "—"} |
| Accessed | {access or "—"} |

## Notes

{s.get("notes") or ""}
"""
    (ROOT / "sources" / f"{sid}.md").write_text(body, encoding="utf-8")

def write_source_json(pack_dir: Path, s: dict) -> None:
    dump(pack_dir / "sources" / f"{s["id"]}.json", {
        "id": s["id"],
        "entity": "source",
        "type": s["type"],
        "citation": s["citation"],
        "url": s.get("url"),
        "access_date": TODAY if s.get("url") else None,
        "reliability_tier": s["tier"],
        "notes": s.get("notes"),
        "editorial": ED,
    })

def write_pack(pack: dict) -> None:
    pack_name = pack["pack"]
    civ_id = pack["civ_id"]
    pack_dir = ROOT / "data" / "structured" / pack_name
    if pack_dir.exists():
        raise SystemExit(f"Refusing to overwrite existing pack: {pack_dir}")
    pack_dir.mkdir(parents=True)
    for sub in ("sources", "sites", "periods", "objects", "claims", "media"):
        (pack_dir / sub).mkdir()

    for s in pack["sources"]:
        write_source_md(s)
        write_source_json(pack_dir, s)

    site_ids = []
    for st in pack["sites"]:
        site_ids.append(st["id"])
        dump(pack_dir / "sites" / f"{st["id"]}.json", {
            "id": st["id"],
            "entity": "site",
            "names": st["names"],
            "kind_note": st["kind_note"],
            "region": st["region"],
            "civilization_ids": [civ_id],
            "summary": st["summary"],
            "sources": st["sources"],
            "coordinates": st.get("coords"),
            "editorial": ED,
        })

    per = pack["period"]
    dump(pack_dir / "periods" / f"{per["id"]}.json", {
        "id": per["id"],
        "entity": "period",
        "names": per["names"],
        "civilization_ids": [civ_id],
        "time": per["time"],
        "summary": per["summary"],
        "sources": per["sources"],
        "editorial": ED,
    })

    obj = pack["object"]
    dump(pack_dir / "objects" / f"{obj["id"]}.json", {
        "id": obj["id"],
        "entity": "object",
        "object_kind": "assemblage",
        "names": obj["names"],
        "civilization_ids": [civ_id],
        "site_ids": obj.get("site_ids") or [],
        "period_ids": [per["id"]],
        "summary": obj["summary"],
        "sources": obj["sources"],
        "rights": {
            "status": "outbound-link-only",
            "license": None,
            "attribution": None,
            "upstream_url": None,
            "notes": "Metadata-only shell assemblage; no forged plates or museum numbers.",
        },
        "media_ids": [],
        "editorial": ED,
    })

    cl = pack["claim"]
    dump(pack_dir / "claims" / f"{cl["id"]}.json", {
        "id": cl["id"],
        "entity": "claim",
        "kind": "fact",
        "statement": cl["statement"],
        "civilization_ids": [civ_id],
        "site_ids": cl.get("site_ids") or [],
        "period_ids": [per["id"]],
        "object_ids": [obj["id"]],
        "sources": cl["sources"],
        "disclaimer": None,
        "editorial": ED,
    })

    # empty media dir is OK
    civ = {
        "id": civ_id,
        "entity": "civilization",
        "kind": "fact",
        "status": "library-seed",
        "names": pack["names"],
        "region": pack["region"],
        "time_span": pack["time_span"],
        "summary": pack["summary"],
        "sources": [s["id"] for s in pack["sources"]],
        "site_ids": site_ids,
        "period_ids": [per["id"]],
        "claim_ids": [cl["id"]],
        "object_ids": [obj["id"]],
        "related_ids": pack.get("related_ids") or [],
        "markdown_path": f"data/civilizations/{civ_id}.md",
        "editorial": ED,
    }
    dump(pack_dir / "civilization.json", civ)

    readme = f"""# Structured pack — {pack["names"]["en"]}

[中文](README.zh.md) | English

Read-only archive entities for `{civ_id}`.

**Status:** library-seed shell (Wave-2, D-2026-10-12-14). Honest thin pack — not fact-library density.

Counts (`export_check` is authoritative):
- sources: {len(pack["sources"])}
- sites: {len(pack["sites"])}
- periods: 1
- objects: 1
- claims: 1
- media: 0

Markdown editorial source: `data/civilizations/{civ_id}.md`.
Run `tools/export_check.py` before serving.
"""
    (pack_dir / "README.md").write_text(readme, encoding="utf-8")
    (pack_dir / "README.zh.md").write_text(
        f"""# 结构化包 — {pack["names"]["zh"]}

[English](README.md) | 中文

`{civ_id}` 的只读档案实体。

**状态：** library-seed 壳（第二波，D-2026-10-12-14）。诚实薄包，非 fact-library 密度。

计数以 `export_check` 为准。编辑稿：`data/civilizations/{civ_id}.md`。
""",
        encoding="utf-8",
    )

    # civilization markdown shell
    src_lines = "\n".join(f"- `{s["id"]}` — {s["type"]} (tier {s["tier"]})" for s in pack["sources"])
    site_lines = "\n".join(f"- **{st["names"]["en"]}** (`{st["id"]}`): {st["summary"]["en"]}" for st in pack["sites"])
    md = f"""---
id: {civ_id}
names:
  zh: {json.dumps(pack["names"]["zh"], ensure_ascii=False)}
  en: {json.dumps(pack["names"]["en"], ensure_ascii=False)}
  native: {json.dumps(pack["names"].get("native") or "", ensure_ascii=False)}
region: {json.dumps(pack["region"], ensure_ascii=False)}
time_span: {json.dumps(pack["time_span"], ensure_ascii=False)}
status: library-seed
summary: |
  {pack["summary"]["en"]}
sources: {[s["id"] for s in pack["sources"]]}
related_ids: {pack.get("related_ids") or []}
notes: "Wave-2 shell D-2026-10-12-14. Empty sections labeled; no invented archaeology."
---

# {pack["names"]["en"]} / {pack["names"]["zh"]}

> **Status:** library-seed shell (Wave-2). Factual overview only at abstract/TOC level of registered sources.
> **Depth:** follow [`docs/entry-depth.md`](../../docs/entry-depth.md). Hypotheses stay out of fact columns.
> **Coverage map:** [`docs/coverage-map.md`](../../docs/coverage-map.md).

## Summary

**EN:** {pack["summary"]["en"]}

**ZH:** {pack["summary"]["zh"]}

## Geography & environment

<!-- Shell: landscape claims deferred until page-verified in registered sources. Region label: {pack["region"]}. -->

Region (editorial label): {pack["region"]}.

## Chronology / periodization

| Period / phase | Approx. range (as in cited scheme) | Notes |
|----------------|-------------------------------------|-------|
| {per["names"]["en"]} | {per["time"]["label"]} | Shell overview — subdivisions deferred |

Scheme note: {per["time"].get("scheme_note") or "—"}.

## Key sites

{site_lines}

Coordinates left null unless a registered source publishes them.

## Urbanism, architecture & institutions

<!-- Shell placeholder: deepen from excavation reports (P) and syntheses (S) already registered. -->

## Writing, language & administration

<!-- Omit or deepen only with sourced script/admin evidence. -->

## Economy, subsistence & craft

<!-- Shell placeholder. -->

## Material culture

Shell assemblage pointer: `{obj["id"]}`.

## External contacts

<!-- Only when sourced; else leave empty. -->

## Research history

Brief orientation only — see registered sources below.

## Sources

{src_lines}

## Related civilizations

{", ".join(f"`{r}`" for r in (pack.get("related_ids") or [])) or "—"}

## Notes

Wave-2 shell. Integrity over speed: prefer honest empty sections over fake density. Empire / primacy / ethnicity labels stay out of fact claims until sourced.
"""
    (ROOT / "data" / "civilizations" / f"{civ_id}.md").write_text(md, encoding="utf-8")
    print(f"wrote Wave-2 pack {pack_name} ({civ_id})")

def main() -> None:
    from packs_defs import PACKS
    for pack in PACKS:
        write_pack(pack)
    print(f"OK: {len(PACKS)} Wave-2 packs")

if __name__ == "__main__":
    main()
