# Hot densify Round-4 Batch B — D-2026-10-12-31

[中文](pass-2026-10-12-hot-round4-b.zh.md) | English

Five hot packs densified with **sites/objects focus** toward Egypt/Aegean/Mesopotamia band; then evaluated for `fact-library` promotion under honest numeric + quality gates.

Machine counts: [`pass-2026-10-12-hot-round4-b.json`](pass-2026-10-12-hot-round4-b.json).

## Before → after

| Pack | sources | sites | periods | objects | claims | media | coords filled |
|------|--------:|------:|--------:|--------:|-------:|------:|---------------|
| `aztec` | 66→71 | 32→42 | 12→13 | 33→51 | 61→69 | 10→11 | 3/42 |
| `phoenician` | 66→71 | 33→43 | 12→13 | 33→51 | 61→69 | 11→12 | 5/43 |
| `anatolia-hittite` | 66→71 | 32→42 | 12→13 | 33→51 | 61→69 | 11→12 | 5/42 |
| `nubia-kush` | 66→71 | 34→44 | 12→13 | 33→51 | 61→69 | 11→12 | 8/44 |
| `elam-iran` | 66→71 | 33→43 | 12→13 | 33→51 | 61→69 | 11→12 | 6/43 |

**Delta totals:** +25 sources · +50 sites · +5 periods · +90 objects · +40 claims · +5 media.

**Coords:** none newly filled this pass (null left null; no invented coordinates).

## Promotion evaluation

**Numeric gates:** sources ≥ 65 · sites ≥ 38 · objects ≥ 45 · claims ≥ 58.

**Quality/honesty:** major sections cited; report-level claims; coord fill not almost-all-null without P/S on key sites; orientation-stub ratio not dominant.

| Pack | Promote? | Status | Numeric | Quality | Coords | Orient. stubs | Reason |
|------|:--------:|--------|:-------:|:-------:|-------:|-------------:|--------|
| `aztec` | N | `library-seed-rich` | PASS | FAIL | 3/42 | 16 | Numeric OK but quality/honesty fail: coords mostly null (3/42 filled, 7%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (16/42, 38%); depth still seed-like vs Egypt report-level sites |
| `phoenician` | N | `library-seed-rich` | PASS | FAIL | 5/43 | 13 | Numeric OK but quality/honesty fail: coords mostly null (5/43 filled, 12%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites) |
| `anatolia-hittite` | N | `library-seed-rich` | PASS | FAIL | 5/42 | 11 | Numeric OK but quality/honesty fail: coords mostly null (5/42 filled, 12%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites) |
| `nubia-kush` | N | `library-seed-rich` | PASS | FAIL | 8/44 | 9 | Numeric OK but quality/honesty fail: coords mostly null (8/44 filled, 18%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites) |
| `elam-iran` | N | `library-seed-rich` | PASS | FAIL | 6/43 | 11 | Numeric OK but quality/honesty fail: coords mostly null (6/43 filled, 14%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites) |

**Promoted:** *(none)*.

**Kept `library-seed-rich`:** `aztec`, `phoenician`, `anatolia-hittite`, `nubia-kush`, `elam-iran`.

Integrity: no invented pages/coords/finds/media art. Tooling: `tools/hot_densify/densify_hot_round4_b.py` + `payloads_round4_b.py`.
