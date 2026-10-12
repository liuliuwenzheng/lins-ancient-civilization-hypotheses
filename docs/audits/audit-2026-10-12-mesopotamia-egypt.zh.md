# 质量审计 — 两河 + 埃及（2026-10-12）

[English](audit-2026-10-12-mesopotamia-egypt.md) | 中文

> 落实 [D-2026-10-12-7](../decisions.zh.md#d-2026-10-12-7--第五轮后优先序审议圆桌) 优先项 **#1**：对最密包做主张/遗址质量审计。诚信优于速度。本报告**不为「补洞」而编造考古内容**。

**范围：** `data/structured/mesopotamia/` 与 `data/structured/egypt/`（claims、sites、sources、objects；periods/media 抽查）。并对照 `sources/*.md` 登记簿，必要时对照 `data/civilizations/civ-mesopotamia.md` / `civ-ancient-egypt.md`。

**方法：** 自动引用完整性 + 模式扫描，再人工审阅全部 `kind=hypothesis`、断言式事实主张、著名器物元数据、遗址坐标策略。

**闸门：** 审计后重跑 `export_check` — **通过**（9 包；出处闸门绿）。

---

## 摘要计数

| 包 | 来源 | 遗址 | 分期 | 器物 | 主张（事实 / 假说） | 媒体 |
|------|--------:|------:|--------:|--------:|---------------------:|------:|
| 两河 | 76 | 43 | 10 | 58 | 70（63 / 7） | 1 |
| 埃及 | 70 | 43 | 6 | 57 | 69（63 / 6） | 2 |
| **审计合计** | **146** | **86** | **16** | **115** | **139（126 / 13）** | **3** |

| 结果 | 两河 | 埃及 | 说明 |
|------|-----:|-----:|------|
| **FAIL** | **0** | **0** | 未发现硬性诚信失败 |
| **WARN** | **44** | **46** | 多为有意留空的坐标；见列表 |
| **PASS（主张引用/分栏）** | 70/70 | 69/69 | 全部主张 `sources[]` 非空且包内+登记簿可解析 |

**初审 JSON 修复：** **无**（无清晰 FAIL）。**后续 Job A：** 116 条事实主张压贴为报告级实质（见下）。

---

## 标准结果

### 1. 主张 `sources[]` 非空且 ID 可解析

| 检查 | 结果 |
|------|------|
| 任何主张空 `sources[]` | **PASS**（0） |
| 来源 id 不在包 JSON | **PASS**（0） |
| 来源 id 不在 `sources/*.md` | **PASS**（0）— 两河 76/76，埃及 70/70 |
| 主张 → 遗址/分期/器物悬空引用 | **PASS**（0） |
| 遗址/器物 → 来源悬空 | **PASS**（0） |

### 2. 过度表述 / 「最早–唯一–第一」排名用语

比较史争排名用语在两包中**已落在假说栏**。自动扫描命中的「First Dynasty / first season」属**假阳性**（期名 / 发掘季序数）— 已驳回。

| 主张 id | 分栏 | 裁决 |
|----------|------|------|
| `claim-meso-first-city-ranking` | hypothesis | **PASS** — 「世界第一城」不作定论 |
| `claim-meso-hassuna-first-village` | hypothesis | **PASS** |
| `claim-meso-jerwan-first-aqueduct` | hypothesis | **PASS** |
| `claim-egypt-uj-earliest-writing` | hypothesis | **PASS** |
| `claim-egypt-amarna-unique-planned-capital` | hypothesis | **PASS** |
| `claim-meso-hansen-alhiba-1970` 等 | fact | **WARN 驳回** — 「第一季 / 第一王朝」非全球排名 |

**无 FAIL**（未标注排名当事实）。

### 3. `kind=fact` vs `kind=hypothesis`

13 条假说均有非空 `disclaimer` 且挂来源。争议模型已核：

**两河假说（7）：** `claim-meso-brak-uruk-colony`、`claim-meso-first-city-ranking`、`claim-meso-hassuna-first-village`、`claim-meso-jerwan-first-aqueduct`、`claim-meso-leilan-climate-collapse`、`claim-meso-nuzi-as-early-urban`、`claim-meso-uruk-expansion-model`。

**埃及假说（6）：** `claim-egypt-amarna-unique-planned-capital`、`claim-egypt-fayum-as-nile-state-cradle`、`claim-egypt-memphis-capital-precision`、`claim-egypt-narmer-single-unification`、`claim-egypt-tasian-before-badarian`、`claim-egypt-uj-earliest-writing`。

Leilan：发掘季报告事实与干旱崩溃模型假说已正确分栏。纳尔迈「一战统一」留假说；过程框架留事实。

**无 FAIL**（无分栏错误）。

### 4. 遗址 — 坐标与名称

| 检查 | 结果 |
|------|------|
| 编造坐标 | **PASS** — **86** 处遗址均为 `coordinates: null` |
| 名称与文献一致 | **PASS**（抽查：乌鲁克/瓦尔卡、Hiba≠特罗、阿拜多斯/Umm el-Qaab、希拉孔波利斯等） |
| 遗址无 `sources[]` | **PASS**（0） |

**WARN（开放、有意）：** 全部遗址暂无坐标。编辑注已写明「不断言/不编造坐标」。这是**诚信延后**，不是用假 lat/lon「修掉」的缺陷。补救 = **仅在出处给出时**再填。

（遗址 id 全表见英文版同节。）

**WARN（本体、开放）：** 部分记录实为**子地点**或**调查区**却以 `entity: site` 入库（如 `site-assur-anu-adad`、`site-diyala-plains-survey`）。v0 可查询可接受；日后可加 `site_kind`。

### 5. 器物 — 仅元数据、无假馆藏号

| 检查 | 结果 |
|------|------|
| `inventory_number` / `accession` / `museum_number` | **PASS** — 115 条均**无**这些字段 |
| 类型 | 两河：57 assemblage + 1 artifact-class；埃及：57 assemblage |
| 权利 | 全部 `outbound-link-only`；注明禁止伪造二进制/编造馆藏号 |
| 纳尔迈调色板等 | **组合级**元数据 + 发掘出处；统一解读留假说栏 |

**无 FAIL。**

---

## FAIL 列表

*无。*

本轮未对结构化 JSON 做改标、删改或削句。

---

## WARN 列表（仍开放）

### W1 — 全部审计遗址坐标为空（86）

**级别：** WARN（保全诚信）  
**补救：** 仅用有出处的地名词典/正式报告补坐标；绝不编造。

### W2 — 书目元主张远多于实质考古主张

**级别：** WARN（档案深度 / 产品诚实）  
粗分：两河事实约 40/63、埃及约 46/63 主要为「文献 X 报告/出版了 Y」，而非考古实质陈述。

这是**诚实的出处脊梁**，但主张层相对遗址/来源数量仍偏「薄」。

**补救（不编造）：** 下一轮优先从**已登记**发掘报告提炼有出处的实质主张；或把书目主张中的考古内容拆成独立事实主张并挂同一 `sources[]`。禁止无出处叙事填充。

### W3 — 少数事实表述略带解释性框架（继续盯）

非 FAIL（有手册出处、无排名定论），但措辞略解释性：`claim-meso-core-region-early-cities`、`claim-meso-uruk-key-horizon`、`claim-egypt-old-kingdom-monuments`、`claim-egypt-nile-flood-ecology`、`claim-egypt-delta-upper-interaction`。

**补救：** 可选日后文案再明确「某通论框架为…」；本轮不强行改标。

### W4 — 媒体仍薄

两河 1 + 埃及 2 条外链目录/文献；符合不上伪造图政策；仅为覆盖面 WARN。

---

## 建议补救顺序

1. **保持 FAIL = 0** — 不为显得密而编造坐标、馆藏号或无出处实质。  
2. **有出处坐标轮**：乌鲁克、乌尔、尼普尔、吉萨、萨卡拉、阿拜多斯、希拉孔波利斯等。  
3. **实质主张轮**：先两河后埃及，从已登记 P 档提炼。  
4. **可选 `site_kind`**（locus / survey-zone / settlement）。  
5. 然后再考虑全仓堆量（按 D-2026-10-12-7：无审计堆量不作默认下一步）。

---


---

## 后续 — 实质压贴（Job A，同日）

**决策链接：** 亦记入 **D-2026-10-12-9**。

**动作：** 将所选 `kind=fact` 主张改写为以**遗址出土 / 地层 / 组合**为主语，发掘或调查报告仅作著录依据——不再以「文献 X 出版了 Y」本身当主张。

| 包 | 改写事实主张数 | 方法 |
|------|----------------:|------|
| 两河 | **57** | 书目元 → 报告级实质；W3 通论框架改为先写归属 |
| 埃及 | **59** | 同上 |
| **合计** | **116** | 未编造页码、坐标、馆藏号或新考古内容 |

**W2 压贴后：** 以「作者/书名 + publishes」起句的事实主张 **0/63**（两河）与 **0/63**（埃及）。出处仍在 `sources[]`，文中常作「见……著录」。

**仍开放的 WARN（诚实保留）：**
- **W1** — 86 处遗址仍为 `coordinates: null`（有意）。
- **W2 残留** — 许多事实仍是*报告范围*（某季记录了什么），而非页级地层深描；再加深须*有出处*阅读，禁虚荣散文。
- **W3** — 解释性事实已改为通论归属起句；继续盯。
- **W4** — 媒体仍薄。

**闸门：** Job A 后 `export_check` 通过。

## 决策链接

已记为 **D-2026-10-12-8**，见 [`docs/decisions.zh.md`](../decisions.zh.md) / [`docs/decisions.md`](../decisions.md)。

---

## 附录 — 假说 id（全）

- 两河：`claim-meso-brak-uruk-colony`、`claim-meso-first-city-ranking`、`claim-meso-hassuna-first-village`、`claim-meso-jerwan-first-aqueduct`、`claim-meso-leilan-climate-collapse`、`claim-meso-nuzi-as-early-urban`、`claim-meso-uruk-expansion-model`
- 埃及：`claim-egypt-amarna-unique-planned-capital`、`claim-egypt-fayum-as-nile-state-cradle`、`claim-egypt-memphis-capital-precision`、`claim-egypt-narmer-single-unification`、`claim-egypt-tasian-before-badarian`、`claim-egypt-uj-earliest-writing`


---

## 后续 — 有出处坐标 + 媒体加厚（Job C，同日）

**决策链接：** **D-2026-10-12-10**。

**原则：** 坐标仅来自 Pleiades CSV 代表点、UNESCO WHC 公布 DMS，或 GeoNames `S.ANS` 考古遗址。媒体仅为带权利元数据的 outbound `document-link` / `external-catalog`。**禁止编造经纬度、馆藏号或伪造器物图。**

### 两河 + 埃及坐标

| 包 | 已填 | 仍空 | 说明 |
|------|-----:|-----:|------|
| 两河 | **29** / 43 | **14** | 空值含调查区、locus，以及无干净地名词典命中者 |
| 埃及 | **22** / 43 | **21** | 空值含子点与未匹配的前王朝墓地等 |

每条已填遗址的 `coordinates.precision_note` 记录地名词典 id。

### 两河 + 埃及媒体

| 包 | 之前 | 之后 | 新增示例 |
|------|-----:|-----:|----------|
| 两河 | 1 | **6** | ISAC Adams PDF；Woolley UE IV；Layard；菲尔德博物馆基什目录；ZATU 海德堡 |
| 埃及 | 2 | **7** | Petrie 阿拜多斯/纳卡达 Archive；Naville 海德堡；Arnold 大都会出版；Petrie 阿玛尔纳海德堡 |

### W1 / W4 状态

- **W1：** 部分处理 — 诚实半填，非虚荣补全。
- **W4：** 有改善，仍仅为 outbound（设计如此）。

**闸门：** Job C 后 `export_check` 通过。
