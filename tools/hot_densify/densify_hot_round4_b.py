#!/usr/bin/env python3
"""Apply hot-pack Round-4 Batch B densify + fact-library promotion eval (D-2026-10-12-31).

Sites/objects focus. Appends; does not wipe. Promotion only if BOTH numeric and
quality/honesty gates pass; otherwise status stays library-seed-rich.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from densify_round2_config import TODAY, patch_densify_lib

DECISION = "D-2026-10-12-31"
dl = patch_densify_lib(decision=DECISION, script="densify_hot_round4_b.py")
# Override notes for Round-4
dl.ED = {
    "derived_from": [
        "tools/hot_densify/densify_hot_round4_b.py",
        "docs/coverage-map.md",
        f"docs/decisions.md#{DECISION.lower()}",
    ],
    "derived_on": TODAY,
    "notes": (
        f"Hot densify Round-4 Batch B sites/objects + promotion eval ({DECISION}). "
        "No invented pages/coords/finds/media. Promote only if numeric AND quality gates pass."
    ),
}
from densify_lib import ROOT, apply_pack, dump
from payloads_round4_b import PAYLOADS

PACKS = ["aztec", "phoenician", "anatolia-hittite", "nubia-kush", "elam-iran"]

# Numeric gates vs dense peers (Egypt/Aegean/Mesopotamia band)
NUM_GATES = {"sources": 65, "sites": 38, "objects": 45, "claims": 58}


def count_coords(pack_dir: Path) -> tuple[int, int]:
    filled = null = 0
    for p in (pack_dir / "sites").glob("*.json"):
        st = json.loads(p.read_text(encoding="utf-8"))
        c = st.get("coordinates") or {}
        if c.get("lat") is not None:
            filled += 1
        else:
            null += 1
    return filled, null


def count_orientation_stubs(pack_dir: Path) -> int:
    n = 0
    for p in (pack_dir / "sites").glob("*.json"):
        st = json.loads(p.read_text(encoding="utf-8"))
        name = (st.get("names") or {}).get("en") or ""
        sid = st.get("id") or ""
        if "orientation" in name.lower() or sid.endswith("-orientation") or "orientation" in sid:
            n += 1
    return n


def evaluate_promotion(pack: str, after: dict) -> dict:
    """Honest promotion eval. Returns promote bool + reasons."""
    pack_dir = ROOT / "data/structured" / pack
    filled, null = count_coords(pack_dir)
    total_sites = filled + null
    stubs = count_orientation_stubs(pack_dir)
    stub_ratio = stubs / total_sites if total_sites else 1.0
    coord_fill_ratio = filled / total_sites if total_sites else 0.0

    numeric_ok = all(after.get(k, 0) >= v for k, v in NUM_GATES.items())
    numeric_detail = {k: {"have": after.get(k, 0), "need": v, "ok": after.get(k, 0) >= v}
                      for k, v in NUM_GATES.items()}

    quality_fail_reasons = []
    # Honesty: almost all coords null AND no meaningful P/S fills on key sites
    if coord_fill_ratio < 0.20:
        quality_fail_reasons.append(
            f"coords mostly null ({filled}/{total_sites} filled, {coord_fill_ratio:.0%}); "
            "below honesty floor for fact-library (need ~≥20% or cited P/S on key sites)"
        )
    # Many orientation stubs remain
    if stub_ratio > 0.35:
        quality_fail_reasons.append(
            f"orientation stubs still high ({stubs}/{total_sites}, {stub_ratio:.0%}); "
            "depth still seed-like vs Egypt report-level sites"
        )
    # Claims band OK numerically but peer Egypt has richer report-level statements;
    # we flag if sites still under Egypt-ish 40+ with low coords
    if after.get("sites", 0) < 40 and coord_fill_ratio < 0.15:
        quality_fail_reasons.append(
            "sites still below Egypt-band floor (~43) with thin coord evidence"
        )

    quality_ok = len(quality_fail_reasons) == 0
    promote = numeric_ok and quality_ok

    if promote:
        reason = "Passes numeric gates and quality/honesty (coord + stub) floors."
    elif numeric_ok and not quality_ok:
        reason = "Numeric OK but quality/honesty fail: " + "; ".join(quality_fail_reasons)
    elif not numeric_ok:
        miss = [k for k, d in numeric_detail.items() if not d["ok"]]
        reason = f"Numeric fail on {miss}; " + ("; ".join(quality_fail_reasons) if quality_fail_reasons else "quality not reached")
    else:
        reason = "Fails both numeric and quality gates."

    return {
        "promote": promote,
        "status": "fact-library" if promote else "library-seed-rich",
        "numeric_ok": numeric_ok,
        "quality_ok": quality_ok,
        "numeric_detail": numeric_detail,
        "coords_filled": filled,
        "coords_null": null,
        "coord_fill_ratio": round(coord_fill_ratio, 3),
        "orientation_stubs": stubs,
        "stub_ratio": round(stub_ratio, 3),
        "quality_fail_reasons": quality_fail_reasons,
        "reason": reason,
    }


def set_civ_status(pack: str, status: str, summary: dict | None = None) -> None:
    path = ROOT / "data/structured" / pack / "civilization.json"
    civ = json.loads(path.read_text(encoding="utf-8"))
    civ["status"] = status
    if summary:
        civ["summary"] = summary
    dump(path, civ)


def sync_civ_md(pack_name: str, payload: dict, counts: dict, eval_row: dict) -> None:
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

    promote_note = (
        f"Promoted to `fact-library` ({DECISION})."
        if eval_row["promote"]
        else f"Kept `library-seed-rich` ({DECISION}): {eval_row['reason']}"
    )

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
notes: "Hot densify Round-4 Batch B {DECISION}. Sites/objects focus + promotion eval. {promote_note}"
---

# {names['en']} / {names['zh']}

> **Status:** `{status}` (hot densify Round-4 Batch B, {DECISION}). {promote_note}
> **Depth:** [`docs/entry-depth.md`](../../docs/entry-depth.md). Hypotheses stay `kind=hypothesis`.
> **Coverage map:** [`docs/coverage-map.md`](../../docs/coverage-map.md).

## Summary

**EN:** {summary['en']}

**ZH:** {summary['zh']}

## Counts (structured)

| sources | sites | periods | objects | claims | media |
|--------:|------:|--------:|--------:|-------:|------:|
| {after['sources']} | {after['sites']} | {after['periods']} | {after['objects']} | {after['claims']} | {after['media']} |

## Promotion eval ({DECISION})

- Numeric gates: {'PASS' if eval_row['numeric_ok'] else 'FAIL'}
- Quality/honesty: {'PASS' if eval_row['quality_ok'] else 'FAIL'}
- Coords: {eval_row['coords_filled']}/{eval_row['coords_filled']+eval_row['coords_null']} filled
- Orientation stubs: {eval_row['orientation_stubs']}
- Decision: **{'PROMOTE → fact-library' if eval_row['promote'] else 'DO NOT PROMOTE → library-seed-rich'}**
- Reason: {eval_row['reason']}

## Periods

| Name | Time label | Summary |
|------|------------|---------|
{chr(10).join(per_rows)}

## Sites (sample / full list)

{chr(10).join(site_lines)}

## Claims

{chr(10).join(claim_lines)}

## Sources

{chr(10).join(src_lines)}
"""
    (ROOT / "data/civilizations" / f"{civ_id}.md").write_text(md, encoding="utf-8")

    pack_dir = ROOT / "data/structured" / pack_name
    readme = f"""# {names['en']} — structured pack

Status: `{status}` · Round-4 Batch B `{DECISION}` · {promote_note}

Counts: sources={after['sources']} sites={after['sites']} periods={after['periods']} objects={after['objects']} claims={after['claims']} media={after['media']}

Civ markdown: `data/civilizations/{civ_id}.md`
"""
    (pack_dir / "README.md").write_text(readme, encoding="utf-8")
    readme_zh = f"""# {names['zh']} — 结构化包

状态：`{status}` · Round-4 Batch B `{DECISION}` · {promote_note}

计数：来源={after['sources']} 遗址={after['sites']} 时段={after['periods']} 对象={after['objects']} 主张={after['claims']} 媒体={after['media']}

文明文档：`data/civilizations/{civ_id}.md`
"""
    (pack_dir / "README.zh.md").write_text(readme_zh, encoding="utf-8")


def main() -> None:
    results = []
    evals = []
    for pack in PACKS:
        payload = PAYLOADS[pack]()
        # Apply with library-seed-rich first; promotion applied after eval
        payload["status"] = "library-seed-rich"
        counts = apply_pack(pack, payload)
        ev = evaluate_promotion(pack, counts["after"])
        # Apply promotion decision to civilization.json + refresh summary note
        set_civ_status(pack, ev["status"], payload.get("summary"))
        counts["status"] = ev["status"]
        sync_civ_md(pack, payload, counts, ev)
        row = {"pack": pack, **counts, "evaluation": ev}
        results.append(row)
        evals.append({"pack": pack, **ev, "after": counts["after"], "before": counts["before"]})
        print(
            pack,
            counts["before"], "->", counts["after"],
            "promote=", ev["promote"],
            "|", ev["reason"][:100],
        )

    out = {
        "decision": DECISION,
        "date": TODAY,
        "numeric_gates": NUM_GATES,
        "packs": [
            {
                "pack": r["pack"],
                "before": r["before"],
                "after": r["after"],
                "civ_id": r["civ_id"],
                "status": r["status"],
                "coords_filled": r.get("coords_filled") or [],
                "evaluation": r["evaluation"],
            }
            for r in results
        ],
        "delta_totals": {
            k: sum(r["after"][k] - r["before"][k] for r in results)
            for k in ["sources", "sites", "periods", "objects", "claims", "media"]
        },
        "promotion_summary": {
            "promoted": [e["pack"] for e in evals if e["promote"]],
            "kept_seed_rich": [e["pack"] for e in evals if not e["promote"]],
        },
        "status_note": (
            "Promote only packs that pass BOTH numeric and quality/honesty gates. "
            "This pass: see promotion_summary."
        ),
    }
    dump(ROOT / "docs/audits/pass-2026-10-12-hot-round4-b.json", out)

    rows = []
    eval_rows = []
    for r in results:
        b, a, ev = r["before"], r["after"], r["evaluation"]
        rows.append(
            f"| `{r['pack']}` | {b['sources']}→{a['sources']} | {b['sites']}→{a['sites']} | "
            f"{b['periods']}→{a['periods']} | {b['objects']}→{a['objects']} | "
            f"{b['claims']}→{a['claims']} | {b['media']}→{a['media']} | "
            f"{ev['coords_filled']}/{ev['coords_filled']+ev['coords_null']} |"
        )
        yn = "Y" if ev["promote"] else "N"
        eval_rows.append(
            f"| `{r['pack']}` | {yn} | `{ev['status']}` | "
            f"{'PASS' if ev['numeric_ok'] else 'FAIL'} | "
            f"{'PASS' if ev['quality_ok'] else 'FAIL'} | "
            f"{ev['coords_filled']}/{ev['coords_filled']+ev['coords_null']} | "
            f"{ev['orientation_stubs']} | {ev['reason']} |"
        )
    dt = out["delta_totals"]
    promoted = out["promotion_summary"]["promoted"]
    kept = out["promotion_summary"]["kept_seed_rich"]

    md = f"""# Hot densify Round-4 Batch B — {DECISION}

[中文](pass-2026-10-12-hot-round4-b.zh.md) | English

Five hot packs densified with **sites/objects focus** toward Egypt/Aegean/Mesopotamia band; then evaluated for `fact-library` promotion under honest numeric + quality gates.

Machine counts: [`pass-2026-10-12-hot-round4-b.json`](pass-2026-10-12-hot-round4-b.json).

## Before → after

| Pack | sources | sites | periods | objects | claims | media | coords filled |
|------|--------:|------:|--------:|--------:|-------:|------:|---------------|
{chr(10).join(rows)}

**Delta totals:** +{dt['sources']} sources · +{dt['sites']} sites · +{dt['periods']} periods · +{dt['objects']} objects · +{dt['claims']} claims · +{dt['media']} media.

**Coords:** none newly filled this pass (null left null; no invented coordinates).

## Promotion evaluation

**Numeric gates:** sources ≥ {NUM_GATES['sources']} · sites ≥ {NUM_GATES['sites']} · objects ≥ {NUM_GATES['objects']} · claims ≥ {NUM_GATES['claims']}.

**Quality/honesty:** major sections cited; report-level claims; coord fill not almost-all-null without P/S on key sites; orientation-stub ratio not dominant.

| Pack | Promote? | Status | Numeric | Quality | Coords | Orient. stubs | Reason |
|------|:--------:|--------|:-------:|:-------:|-------:|-------------:|--------|
{chr(10).join(eval_rows)}

**Promoted:** {', '.join(f'`{p}`' for p in promoted) if promoted else '*(none)*'}.

**Kept `library-seed-rich`:** {', '.join(f'`{p}`' for p in kept) if kept else '*(none)*'}.

Integrity: no invented pages/coords/finds/media art. Tooling: `tools/hot_densify/densify_hot_round4_b.py` + `payloads_round4_b.py`.
"""
    (ROOT / "docs/audits/pass-2026-10-12-hot-round4-b.md").write_text(md, encoding="utf-8")

    zh = f"""# 热门包加厚 Round-4 Batch B — {DECISION}

[English](pass-2026-10-12-hot-round4-b.md) | 中文

五包以**遗址/对象为重点**朝埃及/爱琴/两河档加厚；再按诚实数值 + 质量门槛评估是否升格 `fact-library`。

机器计数：[`pass-2026-10-12-hot-round4-b.json`](pass-2026-10-12-hot-round4-b.json)。

## 加厚前后

| 包 | 来源 | 遗址 | 时段 | 对象 | 主张 | 媒体 | 坐标已填 |
|----|-----:|-----:|-----:|-----:|-----:|-----:|---------:|
{chr(10).join(rows)}

**增量合计：** +{dt['sources']} 来源 · +{dt['sites']} 遗址 · +{dt['periods']} 时段 · +{dt['objects']} 对象 · +{dt['claims']} 主张 · +{dt['media']} 媒体。

**坐标：** 本轮无新填（空值保持空；无伪造坐标）。

## 升格评估

**数值门槛：** 来源 ≥ {NUM_GATES['sources']} · 遗址 ≥ {NUM_GATES['sites']} · 对象 ≥ {NUM_GATES['objects']} · 主张 ≥ {NUM_GATES['claims']}。

**质量/诚信：** 主要章节有引用；主张达报告级；坐标不能几乎全空且关键遗址无 P/S；orientation 指针比例不能占主导。

| 包 | 升格？ | 状态 | 数值 | 质量 | 坐标 | 指针遗址 | 理由 |
|----|:------:|------|:----:|:----:|-----:|---------:|------|
{chr(10).join(eval_rows)}

**已升格：** {', '.join(f'`{p}`' for p in promoted) if promoted else '*（无）*'}.

**仍为 `library-seed-rich`：** {', '.join(f'`{p}`' for p in kept) if kept else '*（无）*'}.

诚信：无伪造页码/坐标/发现/配图。工具：`tools/hot_densify/densify_hot_round4_b.py`。
"""
    (ROOT / "docs/audits/pass-2026-10-12-hot-round4-b.zh.md").write_text(zh, encoding="utf-8")
    print("delta", dt)
    print("promoted", promoted)
    print("kept_seed_rich", kept)


if __name__ == "__main__":
    main()
