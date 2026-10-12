#!/usr/bin/env python3
"""Apply Wave-2 densify payloads → library-seed-rich (D-2026-10-12-16)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# allow importing sibling module
sys.path.insert(0, str(Path(__file__).resolve().parent))
from densify_lib import ROOT, TODAY, ED, apply_pack, dump  # noqa: E402

PAYLOAD_DIR = Path(__file__).resolve().parent / "densify_payloads"
PACKS = [
    "chavin-andes",
    "tiwanaku",
    "wari",
    "classic-maya",
    "aksum",
    "ban-chiang",
    "early-korea",
    "mitanni",
    "phoenician",
]


def sync_civ_md(pack_name: str, payload: dict, counts: dict) -> None:
    civ_id = payload["civ_id"]
    civ = json.loads((ROOT / "data" / "structured" / pack_name / "civilization.json").read_text(encoding="utf-8"))
    names = civ["names"]
    summary = civ["summary"]
    status = civ["status"]
    after = counts["after"]

    # rebuild a compact but useful markdown shell
    src_dir = ROOT / "data" / "structured" / pack_name / "sources"
    site_dir = ROOT / "data" / "structured" / pack_name / "sites"
    per_dir = ROOT / "data" / "structured" / pack_name / "periods"
    claim_dir = ROOT / "data" / "structured" / pack_name / "claims"

    src_lines = []
    for p in sorted(src_dir.glob("*.json")):
        s = json.loads(p.read_text(encoding="utf-8"))
        src_lines.append(f"- `{s['id']}` — {s['type']} (tier {s['reliability_tier']})")

    site_lines = []
    for p in sorted(site_dir.glob("*.json")):
        st = json.loads(p.read_text(encoding="utf-8"))
        coord = "coords filled" if st.get("coordinates") else "coords null"
        site_lines.append(
            f"- **{st['names']['en']}** (`{st['id']}`): {st['summary']['en']} [{coord}]"
        )

    per_rows = []
    for p in sorted(per_dir.glob("*.json")):
        per = json.loads(p.read_text(encoding="utf-8"))
        t = per.get("time") or {}
        per_rows.append(
            f"| {per['names']['en']} | {t.get('label') or '—'} | {per['summary']['en']} |"
        )

    claim_lines = []
    for p in sorted(claim_dir.glob("*.json")):
        cl = json.loads(p.read_text(encoding="utf-8"))
        claim_lines.append(f"- ({cl['kind']}) {cl['statement']['en']}")

    md = f"""---
id: {civ_id}
names:
  zh: {json.dumps(names.get('zh'), ensure_ascii=False)}
  en: {json.dumps(names.get('en'), ensure_ascii=False)}
  native: {json.dumps(names.get('native'), ensure_ascii=False)}
region: {json.dumps(civ.get('region'), ensure_ascii=False)}
time_span: {json.dumps(civ.get('time_span'), ensure_ascii=False)}
status: {status}
summary: |
  {summary['en']}
sources: {json.dumps(civ.get('sources'), ensure_ascii=False)}
related_ids: {json.dumps(civ.get('related_ids') or [], ensure_ascii=False)}
notes: "Densified to library-seed-rich D-2026-10-12-16. Honest thin > fake dense."
---

# {names['en']} / {names['zh']}

> **Status:** `{status}` (Wave-2 densify, D-2026-10-12-16). Not yet `fact-library` / Egypt-level density.
> **Depth:** follow [`docs/entry-depth.md`](../../docs/entry-depth.md). Hypotheses stay in `kind=hypothesis`.
> **Coverage map:** [`docs/coverage-map.md`](../../docs/coverage-map.md).

## Summary

**EN:** {summary['en']}

**ZH:** {summary['zh']}

## Counts (structured)

| Entity | Count |
|--------|------:|
| sources | {after['sources']} |
| sites | {after['sites']} |
| periods | {after['periods']} |
| objects | {after['objects']} |
| claims | {after['claims']} |
| media | {after['media']} |

## Geography & environment

Region (editorial label): {civ.get('region')}.

Site coordinates are filled only from UNESCO WHC published DMS or Pleiades CSV place ids; otherwise left null.

## Chronology / periodization

| Period / phase | Approx. range (as in cited scheme) | Notes |
|----------------|-------------------------------------|-------|
{chr(10).join(per_rows)}

## Key sites

{chr(10).join(site_lines)}

## Registered sources

{chr(10).join(src_lines)}

## Claims (EN)

{chr(10).join(claim_lines)}

## Integrity

No invented archaeology, page numbers, coordinates, or media art in this densify pass.
"""
    (ROOT / "data" / "civilizations" / f"{civ_id}.md").write_text(md, encoding="utf-8")

    # pack README
    readme = f"""# Structured pack — {names['en']}

[中文](README.zh.md) | English

Read-only archive entities for `{civ_id}`.

**Status:** `{status}` (Wave-2 densify, D-2026-10-12-16). Toward usable archive density; not fact-library.

Counts (`export_check` is authoritative):
- sources: {after['sources']}
- sites: {after['sites']}
- periods: {after['periods']}
- objects: {after['objects']}
- claims: {after['claims']}
- media: {after['media']}

Markdown editorial source: `data/civilizations/{civ_id}.md`.
Run `tools/export_check.py` before serving.
"""
    pack_dir = ROOT / "data" / "structured" / pack_name
    (pack_dir / "README.md").write_text(readme, encoding="utf-8")
    (pack_dir / "README.zh.md").write_text(
        f"""# 结构化包 — {names['zh']}

[English](README.md) | 中文

`{civ_id}` 的只读档案实体。

**状态：** `{status}`（第二波加厚，D-2026-10-12-16）。朝可调用密度推进，非 fact-library。

| 实体 | 数量 |
|------|-----:|
| sources | {after['sources']} |
| sites | {after['sites']} |
| periods | {after['periods']} |
| objects | {after['objects']} |
| claims | {after['claims']} |
| media | {after['media']} |

编辑稿：`data/civilizations/{civ_id}.md`。
""",
        encoding="utf-8",
    )


def main() -> int:
    results = []
    for pack in PACKS:
        path = PAYLOAD_DIR / f"{pack}.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        # validate source ids
        for s in payload.get("sources") or []:
            if not re.match(r"^src-[a-z0-9-]+$", s["id"]):
                raise SystemExit(f"bad source id: {s['id']}")
        counts = apply_pack(pack, payload)
        sync_civ_md(pack, payload, counts)
        delta = {k: counts["after"][k] - counts["before"][k] for k in counts["after"]}
        results.append({"pack": pack, **counts, "delta": delta})
        print(
            f"{pack}: src {counts['before']['sources']}→{counts['after']['sources']} "
            f"site {counts['before']['sites']}→{counts['after']['sites']} "
            f"claim {counts['before']['claims']}→{counts['after']['claims']} "
            f"per {counts['before']['periods']}→{counts['after']['periods']} "
            f"media {counts['before']['media']}→{counts['after']['media']} "
            f"[{counts['status']}]"
        )

    summary_path = ROOT / "docs" / "audits" / "pass-2026-10-12-wave2-densify.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    dump(summary_path, {"decision": "D-2026-10-12-16", "date": TODAY, "packs": results})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
