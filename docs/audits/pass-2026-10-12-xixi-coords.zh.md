# 嘻嘻坐标入仓 — D-2026-10-12-20

[English](pass-2026-10-12-xixi-coords.md) | 中文

依据 [`docs/handoffs/2026-10-12-xixi-coords-P-grade.csv`](../handoffs/2026-10-12-xixi-coords-P-grade.csv) 与嘻嘻 P 级说明入仓。

## 鱼凫
**未写入。** `site-yufu` 坐标保持 **空**。假命中 `en:Yufu` = 日本大分县由布市。已盖编辑备注。

## 计数
| 动作 | 数量 |
|------|-----:|
| 新填（多为 S） | 27 |
| P 级升级（UNESCO 官方 poi） | 7 |
| S 命中但保留原坐标（盖章） | 21 |
| 跳过 | 17 |

机器日志：[`pass-2026-10-12-xixi-coords.json`](pass-2026-10-12-xixi-coords.json)。

## P 级升级
- `china-bronze/site-anyang-yinxu` → 36.121978, 114.325162
- `andes/site-chavin-de-huantar` → -9.5927725444, -77.1784535027
- `indus/site-mohenjo-daro` → 27.32916667, 68.13888889
- `indus/site-dholavira` → 23.8884083333, 70.2133027778
- `mesopotamia/site-assur` → 35.4566666667, 43.2611111111
- `aegean/site-tiryns` → 37.6, 22.8
- `aegean/site-troy-hissarlik` → 39.95644, 26.239

## 新填（摘录）
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
- … 另有 12 条见 JSON

## 主要跳过
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

出处副本在 `docs/handoffs/`。除坐标外未编造考古内容。
