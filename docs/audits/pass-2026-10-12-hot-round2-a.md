# Hot densify Round-2 Batch A — D-2026-10-12-22

[中文](pass-2026-10-12-hot-round2-a.zh.md) | English

Five hot packs densified a second round toward `fact-library` band; **status kept `library-seed-rich`** (still below Egypt-level density).

Machine counts: [`pass-2026-10-12-hot-round2-a.json`](pass-2026-10-12-hot-round2-a.json).

## Before → after

| Pack | sources | sites | periods | objects | claims | media | coords filled |
|------|--------:|------:|--------:|--------:|-------:|------:|---------------|
| `teotihuacan` | 30→48 | 14→22 | 8→10 | 7→19 | 26→43 | 6→9 | [] |
| `classic-maya` | 30→48 | 16→24 | 8→10 | 7→19 | 26→43 | 6→9 | ['site-quirigua-orientation', 'site-uxmal-classic-orientation'] |
| `inca` | 30→48 | 15→23 | 8→10 | 7→19 | 26→43 | 6→9 | [] |
| `angkor` | 30→48 | 16→24 | 8→10 | 7→19 | 26→43 | 6→9 | [] |
| `aksum` | 30→48 | 15→23 | 8→10 | 7→19 | 25→42 | 5→8 | [] |

**Delta totals:** +90 sources · +40 sites · +10 periods · +60 objects · +85 claims · +15 media.

**Coords:** Quiriguá and Uxmal filled from UNESCO WHC published coordinates (grade=P). Other new sites left null.

Integrity: no invented pages/coords/finds/media art. Tooling: `tools/hot_densify/densify_hot_round2_a.py` + `payloads_round2_a.py`.
