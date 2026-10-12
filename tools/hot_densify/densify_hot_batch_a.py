#!/usr/bin/env python3
"""Apply hot-pack Batch A densify payloads (D-2026-10-12-19)."""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from densify_lib import ROOT, TODAY, DECISION, ED, apply_pack, dump
from payloads_batch_a import PAYLOADS

PACKS = ["teotihuacan", "classic-maya", "inca", "angkor", "aksum"]


def sync_civ_md(pack_name: str, payload: dict, counts: dict) -> None:
    civ_id = payload["civ_id"]
    civ = json.loads((ROOT / "data/structured" / pack_name / "civilization.json").read_text(encoding="utf-8"))
    names = civ["names"]
    summary = civ["summary"]
    status = civ["status"]
    after = counts["after"]

    src_dir = ROOT / "data/structured" / pack_name / "sources"
    site_dir = ROOT / "data/structured" / pack_name / "sites"
    per_dir = ROOT / "data/structured" / pack_name / "periods"
    claim_dir = ROOT / "data/structured" / pack_name / "claims"

    src_lines = [f"- `{json.loads(p.read_text(encoding="utf-8"))['id']}` — {json.loads(p.read_text(encoding="utf-8"))['type']} (tier {json.loads(p.read_text(encoding="utf-8"))['reliability_tier']})" for p in sorted(src_dir.glob("*.json"))]
    # simpler rebuild
    src_lines = []
    for p in sorted(src_dir.glob("*.json")):
        s = json.loads(p.read_text(encoding="utf-8"))
        src_lines.append(f"- `{s['id']}` — {s['type']} (tier {s['reliability_tier']})")
    site_lines = []
    for p in sorted(site_dir.glob("*.json")):
        st = json.loads(p.read_text(encoding="utf-8"))
        coord = "coords filled" if st.get("coordinates") else "coords null"
        site_lines.append(f"- **{st['names']['en']}** (`{st['id']}`): {st['summary']['en']} [{coord}]")
    per_rows = []
    for p in sorted(per_dir.glob("*.json")):
        per = json.loads(p.read_text(encoding="utf-8"))
        t = per.get("time") or {}
        per_rows.append(f"| {per['names']['en']} | {t.get('label') or '—'} | {per['summary']['en']} |")
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
notes: "Hot densify Batch A {DECISION}. Toward fact-library; status remains library-seed-rich."
---

# {names['en']} / {names['zh']}

> **Status:** `{status}` (hot densify Batch A, {DECISION}). Not yet Egypt-level `fact-library`.
> **Depth:** [`docs/entry-depth.md`](../../docs/entry-depth.md). Hypotheses stay `kind=hypothesis`.
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

## Chronology / periodization

| Period / phase | Approx. range | Notes |
|----------------|---------------|-------|
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
    (ROOT / "data/civilizations" / f"{civ_id}.md").write_text(md, encoding="utf-8")
    readme = f"""# Structured pack — {names['en']}

[中文](README.zh.md) | English

**Status:** `{status}` (hot densify Batch A, {DECISION}). Toward fact-library; not yet Egypt-level density.

Counts: sources {after['sources']} · sites {after['sites']} · periods {after['periods']} · objects {after['objects']} · claims {after['claims']} · media {after['media']}

Markdown: `data/civilizations/{civ_id}.md`. Run `tools/export_check.py`.
"""
    pack_dir = ROOT / "data/structured" / pack_name
    (pack_dir / "README.md").write_text(readme, encoding="utf-8")
    readme_zh = f"""# 结构化包 — {names['zh']}

[English](README.md) | 中文

**状态：** `{status}`（热门加厚 Batch A，{DECISION}）。朝向 fact-library，尚未达埃及级密度。

计数：来源 {after['sources']} · 遗址 {after['sites']} · 时段 {after['periods']} · 对象 {after['objects']} · 主张 {after['claims']} · 媒体 {after['media']}
"""
    (pack_dir / "README.zh.md").write_text(readme_zh, encoding="utf-8")


def main():
    results = []
    for pack in PACKS:
        payload = PAYLOADS[pack]()
        counts = apply_pack(pack, payload)
        sync_civ_md(pack, payload, counts)
        results.append({"pack": pack, **counts})
        print(pack, counts["before"], "->", counts["after"], "coords+", counts.get("coords_filled"))
    out = {
        "decision": DECISION,
        "date": TODAY,
        "packs": results,
        "delta_totals": {
            k: sum(r["after"][k] - r["before"][k] for r in results)
            for k in ["sources", "sites", "periods", "objects", "claims", "media"]
        },
    }
    dump(ROOT / "docs/audits/pass-2026-10-12-hot-batch-a.json", out)
    md = f"""# Hot densify Batch A — {DECISION}

[中文](pass-2026-10-12-hot-batch-a.zh.md) | English

Five hot packs densified toward `fact-library` band; **status kept `library-seed-rich`** (depth not yet Egypt-level).

Machine counts: [`pass-2026-10-12-hot-batch-a.json`](pass-2026-10-12-hot-batch-a.json).

**Delta totals:** +{out['delta_totals']['sources']} sources · +{out['delta_totals']['sites']} sites · +{out['delta_totals']['periods']} periods · +{out['delta_totals']['objects']} objects · +{out['delta_totals']['claims']} claims · +{out['delta_totals']['media']} media.

Integrity: no invented pages/coords/finds/media art. Tooling: `tools/hot_densify/`.
"""
    (ROOT / "docs/audits/pass-2026-10-12-hot-batch-a.md").write_text(md, encoding="utf-8")
    zh = f"""# 热门包加厚 Batch A — {DECISION}

[English](pass-2026-10-12-hot-batch-a.md) | 中文

五包朝 `fact-library` 加厚；**状态仍为 `library-seed-rich`**（未达埃及级）。

机器计数：[`pass-2026-10-12-hot-batch-a.json`](pass-2026-10-12-hot-batch-a.json)。

**增量合计：** +{out['delta_totals']['sources']} 来源 · +{out['delta_totals']['sites']} 遗址 · +{out['delta_totals']['periods']} 时段 · +{out['delta_totals']['objects']} 对象 · +{out['delta_totals']['claims']} 主张 · +{out['delta_totals']['media']} 媒体。

诚信：无伪造页码/坐标/发现/配图。工具：`tools/hot_densify/`。
"""
    (ROOT / "docs/audits/pass-2026-10-12-hot-batch-a.zh.md").write_text(zh, encoding="utf-8")
    print("delta", out["delta_totals"])


if __name__ == "__main__":
    main()
