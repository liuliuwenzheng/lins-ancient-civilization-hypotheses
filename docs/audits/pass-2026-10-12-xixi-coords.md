# 嘻嘻 coordinate ingest — D-2026-10-12-20

[中文](pass-2026-10-12-xixi-coords.zh.md) | English

Ingested [`docs/handoffs/2026-10-12-xixi-coords-P-grade.csv`](../handoffs/2026-10-12-xixi-coords-P-grade.csv) with integrity rules from 嘻嘻 P-grade notes.

## Yufu / 鱼凫
**Not ingested.** `site-yufu` coordinates remain **null**. False hit `en:Yufu` = Yufu-shi, Ōita, Japan. Editorial note stamped.

## Counts
| Action | N |
|--------|--:|
| New fills (mostly S) | 27 |
| P-upgrades (UNESCO official poi) | 7 |
| S-matched kept existing coords (stamped) | 21 |
| Skipped | 17 |

Machine log: [`pass-2026-10-12-xixi-coords.json`](pass-2026-10-12-xixi-coords.json).

## P upgrades
- `china-bronze/site-anyang-yinxu` → 36.121978, 114.325162
- `andes/site-chavin-de-huantar` → -9.5927725444, -77.1784535027
- `indus/site-mohenjo-daro` → 27.32916667, 68.13888889
- `indus/site-dholavira` → 23.8884083333, 70.2133027778
- `mesopotamia/site-assur` → 35.4566666667, 43.2611111111
- `aegean/site-tiryns` → 37.6, 22.8
- `aegean/site-troy-hissarlik` → 39.95644, 26.239

## New fills (sample)
- `sanxingdui/site-baodun` grade=S 30.4502,103.7508
- `china-bronze/site-erlitou` grade=S 34.693,112.689
- `china-bronze/site-panlongcheng` grade=S 30.694444444,114.265555555
- `china-bronze/site-taosi` grade=S 35.89060278,111.49717222
- `china-bronze/site-zhengzhou-erligang` grade=S 34.75222222,113.69027778
- `china-bronze/site-tianma-qucun` grade=S 35.7357,111.56281
- `china-bronze/site-liulihe` grade=S 39.61111111,116.02916667
- `andes/site-aspero` grade=S -10.8156,-77.741
- `andes/site-huaca-prieta` grade=S -7.924,-79.307
- `andes/site-el-paraiso` grade=S -11.95393,-77.11838
- `andes/site-cerro-sechin` grade=S -9.47633333,-78.25666667
- `andes/site-kotosh` grade=S -9.93083333,-76.27944444
- `andes/site-la-galgada` grade=S -8.467,-78.15
- `andes/site-caballo-muerto` grade=S -8.0712,-78.9104
- `indus/site-kalibangan` grade=S 29.47416667,74.13027778
- … +12 more (see JSON)

## Notable skips
- sanxingdui Yufu: SKIP_YUFU
- sanxingdui Qingguanshan: SKIP_EMPTY
- china-bronze Wucheng: SKIP_EMPTY
- china-bronze Tonglushan: SKIP_EMPTY
- china-bronze Houma: SKIP_EMPTY
- andes Bandurria: SKIP_EMPTY
- andes Vichama: SKIP_NO_SITE
- indus Chanhudaro: SKIP_NO_SITE
- indus Ganweriwala: SKIP_EMPTY
- olmec Cascajal Block: SKIP_AMBIGUOUS
- early-maya San Bartolo: SKIP_EMPTY
- early-maya Aguada Fénix: empty lat/lon in CSV
- early-maya Kaminaljuyú: SKIP_FRAME
- early-maya Mundo Perdido: SKIP_AMBIGUOUS
- egypt Tarkhan (Egypt): SKIP_EMPTY
- mesopotamia Ishchali: SKIP_EMPTY
- aegean Ayia Irini: SKIP_EMPTY

Provenance copies under `docs/handoffs/`. No invented archaeology beyond coordinates.
