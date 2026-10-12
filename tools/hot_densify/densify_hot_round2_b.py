#!/usr/bin/env python3
"""Apply hot-pack Round-2 Batch B densify payloads (D-2026-10-12-23). Appends; does not wipe prior content."""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from densify_round2_config import TODAY, patch_densify_lib

DECISION = "D-2026-10-12-23"
dl = patch_densify_lib(decision=DECISION, script="densify_hot_round2_b.py")
from densify_lib import ROOT, apply_pack, dump
from payloads_round2_b import PAYLOADS

PACKS = ["aztec", "phoenician", "anatolia-hittite", "nubia-kush", "elam-iran"]


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

    src_lines = []
    for p in sorted(src_dir.glob("*.json")):
        s = json.loads(p.read_text(encoding="utf-8"))
        src_lines.append(f"- `{s['id']}` — {s['type']} (tier {s['reliability_tier']})")
    site_lines = []
    for p in sorted(site_dir.glob("*.json")):
        st = json.loads(p.read_text(encoding="utf-8"))
        coord = "coords filled" if st.get("coordinates") and st["coordinates"].get("lat") is not None else "coords null"
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
notes: "Hot densify Round-2 Batch B {DECISION}. Toward fact-library; status remains library-seed-rich."
---

# {names['en']} / {names['zh']}

> **Status:** `{status}` (hot densify Round-2 Batch B, {DECISION}). Not yet Egypt-level `fact-library`.
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
    pack_dir = ROOT / "data/structured" / pack_name
    readme = f"""# Structured pack — {names['en']}

[中文](README.zh.md) | English

**Status:** `{status}` (hot densify Round-2 Batch B, {DECISION}). Toward fact-library; not yet Egypt-level density.

Counts: sources {after['sources']} · sites {after['sites']} · periods {after['periods']} · objects {after['objects']} · claims {after['claims']} · media {after['media']}

Markdown: `data/civilizations/{civ_id}.md`. Run `tools/export_check.py`.
"""
    (pack_dir / "README.md").write_text(readme, encoding="utf-8")
    readme_zh = f"""# 结构化包 — {names['zh']}

[English](README.md) | 中文

**状态：** `{status}`（热门加厚 Round-2 Batch B，{DECISION}）。朝向 fact-library，尚未达埃及级密度。

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
        "status_note": "All five packs remain library-seed-rich (not promoted to fact-library).",
    }
    dump(ROOT / "docs/audits/pass-2026-10-12-hot-round2-b.json", out)

    # per-pack table for markdown
    rows = []
    for r in results:
        b, a = r["before"], r["after"]
        rows.append(
            f"| `{r['pack']}` | {b['sources']}→{a['sources']} | {b['sites']}→{a['sites']} | "
            f"{b['periods']}→{a['periods']} | {b['objects']}→{a['objects']} | "
            f"{b['claims']}→{a['claims']} | {b['media']}→{a['media']} | {r.get('coords_filled') or []} |"
        )
    dt = out["delta_totals"]
    md = f"""# Hot densify Round-2 Batch B — {DECISION}

[中文](pass-2026-10-12-hot-round2-b.zh.md) | English

Five hot packs densified a second round toward `fact-library` band; **status kept `library-seed-rich`** (still below Egypt-level density).

Machine counts: [`pass-2026-10-12-hot-round2-b.json`](pass-2026-10-12-hot-round2-b.json).

## Before → after

| Pack | sources | sites | periods | objects | claims | media | coords filled |
|------|--------:|------:|--------:|--------:|-------:|------:|---------------|
{chr(10).join(rows)}

**Delta totals:** +{dt['sources']} sources · +{dt['sites']} sites · +{dt['periods']} periods · +{dt['objects']} objects · +{dt['claims']} claims · +{dt['media']} media.

**Coords:** No new coord fills this pass (orientation sites left null; prior P/S fills retained).

Integrity: no invented pages/coords/finds/media art. Tooling: `tools/hot_densify/densify_hot_round2_b.py` + `payloads_round2_b.py`.
"""
    (ROOT / "docs/audits/pass-2026-10-12-hot-round2-b.md").write_text(md, encoding="utf-8")
    zh = f"""# 热门包加厚 Round-2 Batch B — {DECISION}

[English](pass-2026-10-12-hot-round2-b.md) | 中文

五包第二轮朝 `fact-library` 加厚；**状态仍为 `library-seed-rich`**（未达埃及级）。

机器计数：[`pass-2026-10-12-hot-round2-b.json`](pass-2026-10-12-hot-round2-b.json)。

## 加厚前后

| 包 | 来源 | 遗址 | 时段 | 对象 | 主张 | 媒体 | 坐标补填 |
|----|-----:|-----:|-----:|-----:|-----:|-----:|----------|
{chr(10).join(rows)}

**增量合计：** +{dt['sources']} 来源 · +{dt['sites']} 遗址 · +{dt['periods']} 时段 · +{dt['objects']} 对象 · +{dt['claims']} 主张 · +{dt['media']} 媒体。

**坐标：** 本轮无新坐标补填（指针遗址留空；既有 P/S 坐标保留）。

诚信：无伪造页码/坐标/发现/配图。工具：`tools/hot_densify/densify_hot_round2_b.py`。
"""
    (ROOT / "docs/audits/pass-2026-10-12-hot-round2-b.zh.md").write_text(zh, encoding="utf-8")
    print("delta", out["delta_totals"])


if __name__ == "__main__":
    main()
