# Hot densify Round-4 Batch A — D-2026-10-12-30

[中文](pass-2026-10-12-hot-round4-a.zh.md) | English

Five hot packs densified with **sites/objects focus** toward Egypt/Aegean/Mesopotamia band; then evaluated for `fact-library` promotion under honest numeric + quality gates.

Machine counts: [`pass-2026-10-12-hot-round4-a.json`](pass-2026-10-12-hot-round4-a.json).

## Before → after

| Pack | sources | sites | periods | objects | claims | media | coords filled |
|------|--------:|------:|--------:|--------:|-------:|------:|---------------|
| `teotihuacan` | 66→71 | 31→41 | 12→13 | 33→51 | 61→69 | 11→12 | 1/41 |
| `classic-maya` | 66→71 | 33→43 | 12→13 | 33→51 | 61→69 | 11→12 | 6/43 |
| `inca` | 66→71 | 32→42 | 12→13 | 33→51 | 61→69 | 11→12 | 4/42 |
| `angkor` | 66→71 | 33→43 | 12→13 | 33→51 | 61→69 | 11→12 | 4/43 |
| `aksum` | 66→71 | 32→42 | 12→13 | 33→51 | 60→68 | 10→11 | 3/42 |

**Delta totals:** +25 sources · +50 sites · +5 periods · +90 objects · +40 claims · +5 media.

**Coords:** none newly filled this pass (null left null; no invented coordinates).

## Promotion evaluation

**Numeric gates:** sources ≥ 65 · sites ≥ 38 · objects ≥ 45 · claims ≥ 58.

**Quality/honesty:** major sections cited; report-level claims; coord fill not almost-all-null without P/S on key sites; orientation-stub ratio not dominant.

| Pack | Promote? | Status | Numeric | Quality | Coords | Orient. stubs | Reason |
|------|:--------:|--------|:-------:|:-------:|-------:|-------------:|--------|
| `teotihuacan` | N | `library-seed-rich` | PASS | FAIL | 1/41 | 20 | Numeric OK but quality/honesty fail: coords mostly null (1/41 filled, 2%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (20/41, 49%); depth still seed-like vs Egypt report-level sites |
| `classic-maya` | N | `library-seed-rich` | PASS | FAIL | 6/43 | 19 | Numeric OK but quality/honesty fail: coords mostly null (6/43 filled, 14%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (19/43, 44%); depth still seed-like vs Egypt report-level sites |
| `inca` | N | `library-seed-rich` | PASS | FAIL | 4/42 | 21 | Numeric OK but quality/honesty fail: coords mostly null (4/42 filled, 10%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (21/42, 50%); depth still seed-like vs Egypt report-level sites |
| `angkor` | N | `library-seed-rich` | PASS | FAIL | 4/43 | 22 | Numeric OK but quality/honesty fail: coords mostly null (4/43 filled, 9%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (22/43, 51%); depth still seed-like vs Egypt report-level sites |
| `aksum` | N | `library-seed-rich` | PASS | FAIL | 3/42 | 21 | Numeric OK but quality/honesty fail: coords mostly null (3/42 filled, 7%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (21/42, 50%); depth still seed-like vs Egypt report-level sites |

**Promoted:** *(none)*.

**Kept `library-seed-rich`:** `teotihuacan`, `classic-maya`, `inca`, `angkor`, `aksum`.

Integrity: no invented pages/coords/finds/media art. Tooling: `tools/hot_densify/densify_hot_round4_a.py` + `payloads_round4_a.py`.
