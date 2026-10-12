# 质量审计 — 其余七包（2026-10-12）

[English](audit-2026-10-12-seven-packs.md) | 中文

> 标准与 [`audit-2026-10-12-mesopotamia-egypt.zh.md`](audit-2026-10-12-mesopotamia-egypt.zh.md) 相同。诚信优于速度。**不为补洞而编造考古内容**。

**范围：** `andes`、`indus`、`china-bronze`、`sanxingdui`、`aegean`、`olmec`、`early-maya`。

**方法：** 自动引用完整性 + 排名用语扫描 + 假说免责检查 + 器物馆藏号字段扫描；仅人工处理清晰 FAIL。

**闸门：** 修复后 `export_check` 通过。early-maya 来源 68→70（将两份已登记的比较用 `src-olmec-*` 拷入包内）。

---

## 摘要计数

| 包 | 来源 | 遗址 | 分期 | 器物 | 主张（事实 / 假说） | 媒体 | FAIL | WARN |
|------|--------:|------:|--------:|--------:|---------------------:|------:|-----:|------|
| 安第斯 (`andes`) | 68 | 41 | 7 | 48 | 65（48 / 17） | 6 | **0** | 见 WARN |
| 印度河 (`indus`) | 68 | 38 | 5 | 46 | 61（48 / 13） | 5 | **0** | 见 WARN |
| 中国青铜 (`china-bronze`) | 68 | 39 | 7 | 47 | 62（47 / 15） | 1 | **0** | 见 WARN |
| 三星堆 (`sanxingdui`) | 68 | 36 | 7 | 46 | 59（43 / 16） | 1 | **0** | 见 WARN |
| 爱琴 (`aegean`) | 68 | 40 | 7 | 46 | 60（44 / 16） | 4 | **0** | 见 WARN |
| 奥尔梅克 (`olmec`) | 68 | 37 | 4 | 47 | 55（39 / 16） | 4 | **0** | 见 WARN |
| 早期玛雅 (`early-maya`) | 70 | 40 | 5 | 47 | 60（43 / 17） | 4 | **0** | 见 WARN |

**本轮清晰 FAIL 修复：** **4 → 0**（见下）。开放 WARN 如实记录；无虚荣填充。

---

## 标准（同两河/埃及）

1. 主张 `sources[]` 非空；ID 在包内 **且** `sources/*.md` 可解析；遗址/分期/器物引用可解析。
2. 争议性「最早 / 第一 / 唯一 / America’s first」排名用语不得未标注落在 `kind=fact`。
3. `kind=hypothesis` 须有非空 `disclaimer`。
4. 遗址：无编造坐标（null 可）；名称与文献一致。
5. 器物：无填 `inventory_number` / `accession` / `museum_number`。

---

## FAIL 修复（已处理）

| Id | 包 | 问题 | 处理 |
|----|------|------|------|
| `claim-olmec-diehl-synthesis` | olmec | 事实句复述书名排名用语 | 改写：二手综合；书名排名**不采为定论** |
| `claim-maya-olmec-to-maya-unilinear` | early-maya | 引用 `src-olmec-flannery-marcus-olmec-oaxaca` 不在 early-maya 包内 | 自 olmec 包拷入已登记来源 JSON（比较引用；无新考古） |
| `site-izapa-comparative` | early-maya | 引用 `src-olmec-stirling-bae-138-1943` 悬空 | 同上，拷入 Stirling BAE 138 |
| `asm-maya-izapa-stelae-comparative` | early-maya | 同上 | 同上 |

**未编造**页码、坐标、馆藏号或新发现。

---

## 分包 WARN

### 安第斯（`andes`）

| 结果 | 计数 | 说明 |
|------|-----:|------|
| **FAIL** | **0** | 下方修复后 |
| **WARN** | 开放 | 空坐标=41；书目元≈3/48；媒体=6；本体=— |

**假说（17）：** `claim-andes-aspero-chiefdom-label`、`claim-andes-bandurria-challenges-chiefdom-state`、`claim-andes-casma-earliest-state`、`claim-andes-casma-state-1987-hypothesis`、`claim-andes-casma-vs-norte-chico-priority`、`claim-andes-chao-pristine-center`、`claim-andes-city-vs-ceremonial-center`、`claim-andes-gavilanes-maize-priority`、`claim-andes-maize-staple-intensity`、`claim-andes-maritime-foundations-model`、`claim-andes-maritime-model-settled`、`claim-andes-moseley-maritime-reappraised`、`claim-andes-oldest-civilization-marketing`、`claim-andes-pristine-state-label`、`claim-andes-sandweiss-environmental-demise`、`claim-andes-square-room-emblem`、`claim-andes-tello-matriz-hypothesis`

### 印度河（`indus`）

| 结果 | 计数 | 说明 |
|------|-----:|------|
| **FAIL** | **0** | 下方修复后 |
| **WARN** | 开放 | 空坐标=38；书目元≈7/48；媒体=5；本体=site-ghaggar-hakra-stein-survey、site-sind-majumdar-survey |

**假说（13）：** `claim-indus-allahdino-script-deciphered`、`claim-indus-balakot-gulf-trade`、`claim-indus-climate-deurbanization`、`claim-indus-empire-model`、`claim-indus-empire-unified`、`claim-indus-empire-vs-network`、`claim-indus-kot-diji-conquest`、`claim-indus-law-proves-harappa-capital`、`claim-indus-lothal-dock`、`claim-indus-parpola-decipherment`、`claim-indus-rakhigarhi-eastern-capital`、`claim-indus-script-fully-deciphered`、`claim-indus-shortughai-colony`

### 中国青铜（`china-bronze`）

| 结果 | 计数 | 说明 |
|------|-----:|------|
| **FAIL** | **0** | 下方修复后 |
| **WARN** | 开放 | 空坐标=39；书目元≈14/47；媒体=1；本体=— |

**假说（15）：** `claim-china-allan-cosmos-hypothesis`、`claim-china-anyange-sole-capital-always`、`claim-china-erlitou-equals-xia-capital`、`claim-china-fengchu-she-palace`、`claim-china-hoards-are-emergency-only`、`claim-china-huanbei-as-hedanjia-capital`、`claim-china-panlongcheng-as-shang-outpost`、`claim-china-taosi-yao-capital`、`claim-china-xia-equals-erlitou`、`claim-china-xia-historicity`、`claim-china-xingan-as-shang-kingdom`、`claim-china-xszcp-bands`、`claim-china-yanshi-as-western-bo`、`claim-china-zhengzhou-as-ao-or-bo`、`claim-china-zou-heng-xia-equation`

### 三星堆（`sanxingdui`）

| 结果 | 计数 | 说明 |
|------|-----:|------|
| **FAIL** | **0** | 下方修复后 |
| **WARN** | 开放 | 空坐标=36；书目元≈5/43；媒体=1；本体=site-cpas-survey-region |

**假说（16）：** `claim-sxd-ancient-shu-title`、`claim-sxd-baodun-ancestor-state`、`claim-sxd-baodun-direct-ancestor-state`、`claim-sxd-capital-moved-to-jinsha`、`claim-sxd-east-wall-date-equals-erlitou`、`claim-sxd-is-ancient-shu-state`、`claim-sxd-is-shang-colony`、`claim-sxd-maritime-cowrie-trade-route`、`claim-sxd-not-same-shang-polity`、`claim-sxd-pit-chronology-debated`、`claim-sxd-pits-only-sacrifice`、`claim-sxd-qingguanshan-palace`、`claim-sxd-same-polity-shang`、`claim-sxd-shang-colony-still-hypothesis`、`claim-sxd-single-ceremony-all-pits`、`claim-sxd-unesco-equals-verdict`

### 爱琴（`aegean`）

| 结果 | 计数 | 说明 |
|------|-----:|------|
| **FAIL** | **0** | 下方修复后 |
| **WARN** | 开放 | 空坐标=40；书目元≈7/44；媒体=4；本体=site-thera-chronology-pointer |

**假说（16）：** `claim-aegean-agamemnon-historic-mycenae-king`、`claim-aegean-circle-b-equals-circle-a-dynasty`、`claim-aegean-eruption-caused-lm-ib-collapse`、`claim-aegean-high-low-chronology`、`claim-aegean-high-vs-low-chronology`、`claim-aegean-homer-equals-excavation`、`claim-aegean-homer-nestor-equals-englianos`、`claim-aegean-linear-a-is-greek`、`claim-aegean-minoan-thalassocracy`、`claim-aegean-sea-peoples-pylos-destruction`、`claim-aegean-single-calendar-year`、`claim-aegean-single-knossos-thalassocracy`、`claim-aegean-single-thera-calendar`、`claim-aegean-thera-caused-minoan-collapse`、`claim-aegean-thera-sole-lmib`、`claim-aegean-troy-war-hypothesis`

### 奥尔梅克（`olmec`）

| 结果 | 计数 | 说明 |
|------|-----:|------|
| **FAIL** | **0** | 下方修复后 |
| **WARN** | 开放 | 空坐标=37；书目元≈2/39；媒体=4；本体=site-olmec-heartland-survey-pointer |

**假说（16）：** `claim-olmec-arroyo-pesquero-controlled`、`claim-olmec-cascajal-oldest-script`、`claim-olmec-cascajal-oldest-writing-settled`、`claim-olmec-cascajal-oldest-writing`、`claim-olmec-colossal-heads-portraits-only`、`claim-olmec-el-manati-state-ritual`、`claim-olmec-empire-political`、`claim-olmec-mother-culture-model`、`claim-olmec-mother-culture-still`、`claim-olmec-mother-culture`、`claim-olmec-pottery-export-model`、`claim-olmec-pottery-unidirectional-export`、`claim-olmec-san-lorenzo-capital-of-all`、`claim-olmec-tres-zapotes-stela-c-long-count-origin`、`claim-olmec-were-jaguar-religion-unitary`、`claim-olmec-writing-fully-deciphered`

### 早期玛雅（`early-maya`）

| 结果 | 计数 | 说明 |
|------|-----:|------|
| **FAIL** | **0** | 下方修复后 |
| **WARN** | 开放 | 空坐标=40；书目元≈6/43；媒体=4；本体=site-calakmul-preclassic-pointer |

**假说（17）：** `claim-maya-aguada-fenix-egalitarian`、`claim-maya-altar-is-only-classic`、`claim-maya-calakmul-preclassic-capital`、`claim-maya-cuello-oldest-maya`、`claim-maya-e-group-astronomical-only`、`claim-maya-estrada-belli-first-title`、`claim-maya-estrada-belli-primacy-title`、`claim-maya-full-middle-preclassic-divine-kingship`、`claim-maya-kinship-kingship-model`、`claim-maya-middle-preclassic-divine-kingship-settled`、`claim-maya-middle-preclassic-divine-kingship`、`claim-maya-mirador-first-state-hypothesis`、`claim-maya-mirador-first-state-settled`、`claim-maya-mirador-first-state`、`claim-maya-olmec-influence-direction`、`claim-maya-olmec-to-maya-unilinear`、`claim-maya-preclassic-divine-kingship-full`


### 共同开放 WARN

- **W1 — 坐标为空**（有意延后；仅在出处给出时补）。
- **W2 — 书目元残留** — 部分包仍有「作者出版」起句事实（中国青铜约 14/47）。宜日后做两河/埃及式实质压贴；禁无出处叙事。
- **W3 — 遗址本体** — 调查区/指针以 `site` 入库（印度河、三星堆、奥尔梅克）。v0 可接受；可选日后 `site_kind`。
- **W4 — 媒体薄** — 仅外链/元数据；符合不上伪造图政策。

---

## 决策链接

已记为 **D-2026-10-12-9**，见 [`docs/decisions.zh.md`](../decisions.zh.md) / [`docs/decisions.md`](../decisions.md)。


---

## 后续 — 有出处坐标 + 媒体加厚（Job C，同日）

**决策链接：** **D-2026-10-12-10**。规则同两河/埃及 Job C。

### 七包坐标

| 包 | 已填 | 仍空 | 地名词典依据（例） |
|------|-----:|-----:|----------------------|
| andes | **1** / 41 | **40** | 仅 UNESCO 1269 卡拉尔 |
| indus | **3** / 38 | **35** | UNESCO 摩亨佐达罗/多拉维拉；GeoNames 哈拉帕 S.ANS |
| china-bronze | **1** / 39 | **38** | UNESCO 1114-001 殷墟宫殿区 |
| sanxingdui | **0** / 36 | **36** | 本轮无干净命中 — **诚实跳过** |
| aegean | **20** / 40 | **20** | Pleiades 克诺索斯宫/迈锡尼/涅斯托尔宫等 |
| olmec | **2** / 37 | **35** | GeoNames 拉文塔/查尔卡钦戈 S.ANS |
| early-maya | **6** / 40 | **34** | GeoNames 埃尔米拉多尔等；UNESCO 预备清单圣巴托洛 |

### 七包媒体

| 包 | 之前 | 之后 |
|------|-----:|-----:|
| andes | 6 | **8** |
| indus | 5 | **8** |
| china-bronze | 1 | **4** |
| sanxingdui | 1 | **4** |
| aegean | 4 | **7** |
| olmec | 4 | **7** |
| early-maya | 4 | **7** |

### Job C 后共享 WARN

- **W1：** 各包部分处理；剩余空值保留。
- **W2 / W3：** 本轮未动。
- **W4：** 有改善；仍仅为 outbound。

**闸门：** `export_check` 通过。九包媒体合计 **58**（D-2026-10-12-7 基线为 28）。
