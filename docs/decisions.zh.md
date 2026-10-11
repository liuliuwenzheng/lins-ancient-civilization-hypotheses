# 项目决策记录

[English](decisions.md) | 中文

> 有日期的范围约束。在已实现且通过出处闸门的 API 出现之前，本仓 Markdown 仍为真源。

相关：[圆桌](council.zh.md) · [接口](api.zh.md) · [架构](architecture.zh.md)

---

## 2026-10-11

### D-2026-10-11-1 — 默认圆桌席位（v0）确认

**决定：** 维持 [`council.zh.md`](council.zh.md) 已列的七席 FHLS-perspectives：

1. `deming-perspective`
2. `steve-jobs-perspective`
3. `elon-musk-perspective`
4. `darwin-perspective`
5. `descartes-perspective`
6. `qianxuesen-perspective`
7. `mozi-perspective`

**说明：** 透镜是 AI 思维工具（`perspective: true`，`person_endorsement: false`）。亚里士多德在 FHLS 目录有真实条目之前**不入席**——勿在本仓捏造视角文件。

### D-2026-10-11-2 — 云端审议：先只规范，后实现

**决定：** 云端审议主机 = **先规范、后实现（spec-first）**。继续完善 [`api.zh.md` §9](api.zh.md#9-审议圆桌云端优先) / [`openapi.v0.yaml`](openapi.v0.yaml) 设计；**暂不**上线实时云端服务。

**说明：** 将来实现时优先云端（SSE/WebSocket、席位并行）。已发布会话仍以 `deliberations/` 下 git Markdown 落盘。

### D-2026-10-11-3 — 第一批事实库种子区域（仅空壳）

**决定：** 在 `data/civilizations/` 为下列 id 开脚手架文件——**仅结构与占位**。不编造事实、不伪造来源、不上假文物图。

| Id | 名称（中 / 英） |
|----|-----------------|
| `civ-mesopotamia` | 两河 / Mesopotamia |
| `civ-ancient-egypt` | 古埃及 / Ancient Egypt |
| `civ-indus-valley` | 印度河 / Indus Valley |
| `civ-china-bronze` | 中国青铜时代（总览壳） / China Bronze Age (overview shell) |
| `civ-sanxingdui` | 三星堆 / Sanxingdui |
| `civ-olmec` | 奥尔梅克 / Olmec |
| `civ-early-maya` | 早期玛雅 / Early Maya |
| `civ-andes` | 安第斯早期文明（总览壳） / Andean early civilizations (overview shell) |
| `civ-aegean` | 爱琴 / Aegean |

**说明：** 空壳上的 `time_span` 为学界常用近似区间，并标明「发布前须引用」。在真实 `src-*` 登记前 `sources: []`。在出处到位前状态保持 `draft`。

### D-2026-10-11-4 — 现阶段以 Markdown 为真源

**决定：** 在实现带出处失败即关闭的导出/API 之前，git 中的 Markdown 模板与条目是**唯一**对外资料库接口。禁止静默双写。

### D-2026-10-11-5 — 填充顺序：先两河 + 古埃及

**决定：** 事实库内容填充从时间上最早的近东 / 尼罗河条目开始：`civ-mesopotamia`（苏美尔/乌鲁克中心概述）与 `civ-ancient-egypt`（前王朝→早王朝概述），再及其他种子区。

**说明：** 出处闸门不变：每条事实主张须挂已登记的 `src-*`。安第斯仅在有扎实出处时加可选的 Caral 年代指针；本轮不做安第斯全文扩展。仅当 ≥2 条扎实来源且摘要全部可引用时，状态才可由 `draft` 改为 `library-seed`。

### D-2026-10-11-6 — 安第斯/卡拉尔补全为 library-seed

**决定：** 在两河 + 古埃及之后，先将 `civ-andes`（卡拉尔–北奇科）由 draft 升为 `library-seed`，再进入下一批种子区。

**说明：** 登记并引用 Science 2001、Nature 2004（95 年代；~3000–1800 cal BCE）、Shady 1997、Shady & Leyva 2003。不宣称世界最早文明排序；「城市 vs 礼仪中心 / 国家 vs 复杂社会」留在 Notes 作开放争议。

### D-2026-10-11-7 — 印度河作为下一批时间序 library-seed 填实

**决定：** 安第斯/卡拉尔补全之后，将 `civ-indus-valley` 由 draft 空壳升为 `library-seed`，作为下一批时间序旧大陆条目（印度河传统 / Mature Harappan 繁荣期约公元前 2600–1900 年，与第三千纪晚期诸文明并存）。

**说明：** 登记 Kenoyer 1991（年代表）、Wright 2010（繁荣期 2600–1900 BCE；印度河/加加尔–哈克拉）、Kenoyer 2014 剑桥专章、Possehl 2002、Marshall 1931（摩亨佐-达罗 P）、Meadow 编 1991（哈拉帕 1986–1990 P）。文字未破译 = 研究现况事实。「帝国 vs 城市网络 / 国家形态」留在 Notes 作开放争议。不伪造文物图、不编造页码。

### D-2026-10-11-8 — 中国青铜总览 + 三星堆为下一批时间序 library-seed

**决定：** 印度河填实之后，将 `civ-china-bronze`（中原二里头/商–周青铜总览）与 `civ-sanxingdui`（四川广汉三星堆）由 draft 空壳升为 `library-seed`，作为下一批时间序东亚条目。

**说明：** 登记 Thorp 1991（二里头「最小」定义；不预设夏史实）、Liu & Chen 2003（约公元前 1800–1400 年国家形成；金属与盐）、Flad & Chen 2013（长江流域晚新石器→青铜时代末）、Bagley 1987（商代礼器青铜）；三星堆登记四川 1999《三星堆祭祀坑》（P）、Ge & Linduff 1990、Bagley 1988、Li et al. 2022 Antiquity（约 12 km²；约公元前 2700–1000 年；1986 一/二号坑；新坑与四号坑碳十四）。夏王朝历史真实性、三星堆与商是否同一政体，以及祭祀坑绝对年代争议，一律留在 Notes。不伪造文物图、不编造页码。

### D-2026-10-11-9 — 爱琴青铜时代为下一批时间序 library-seed

**决定：** 中国青铜总览 + 三星堆填实之后，将 `civ-aegean` 由 draft 空壳升为 `library-seed`，作为下一批时间序东地中海 / 欧洲条目（早–晚青铜时代爱琴总览：基克拉泽斯 / 克里特米诺斯 / 大陆迈锡尼）。

**说明：** 登记 Dickinson 1994（剑桥通论；约公元前 3000–1000 年）、Shelmerdine 编 2008（剑桥指南；约公元前 3000–1100 年；克里特/大陆/群岛）、Broodbank 2000（早期基克拉泽斯）、Manning 等 2006 *Science*（圣托里尼公元前 17 世纪晚期；LM IA–II 高年代方案——争议开放）、Evans《米诺斯宫》1921–1935（历史一手；修复须标注）、Blegen & Rawson 1966（涅斯托尔宫 / Englianos P）、Ventris & Chadwick 1956（线性 B = 迈锡尼希腊语）、Salgarella 2022 OCD（线性 A 未破译；仅 T 档定向）。海上霸权（thalassocracy）与高/低绝对年代一律留在 Notes。非单宫专条。不伪造文物图、不编造页码。

### D-2026-10-11-10 — 奥尔梅克 + 早期玛雅为末批中美洲 library-seed（第一批九壳填实完成）

**决定：** 爱琴填实之后，将 `civ-olmec` 与 `civ-early-maya` 由 draft 空壳升为 `library-seed`，作为第一批九个文明空壳的末对中美洲条目。本提交起，**全部九条**首批种子（`civ-mesopotamia`、`civ-ancient-egypt`、`civ-indus-valley`、`civ-china-bronze`、`civ-sanxingdui`、`civ-andes`、`civ-aegean`、`civ-olmec`、`civ-early-maya`）均为 `library-seed`。

**说明：** 奥尔梅克——登记 Pool 2007（剑桥；南韦拉克鲁斯–塔巴斯科形成期；约 3500 年前兴起 / 约千年繁荣；纪念性石雕框架）、Diehl 2004（泰晤士与哈德逊通论；圣洛伦佐 / 拉文塔 / 域外 / 后奥尔梅克目录；书名「最早」仅为出版定位）、Coe & Diehl 1980（圣洛伦佐发掘报告，P 档）、Grove 编 1987（《古代查尔卡钦戈》，高地奥尔梅克风格中心，P 档）、Nichols & Pool 2012（牛津中美洲考古手册取向）。早期玛雅——登记 Sharer & Traxler 2006（第 6 版长时段手册；本条止于早古典）、Estrada-Belli 2011（前古典仪式与权力；纳克贝 / 埃尔米拉多尔 / 西瓦尔；古典期约公元 3 世纪开启）、Inomata 等 2013 *Science*（塞瓦尔约公元前 1000–700 年广场–金字塔 / E 组；区域互动 vs 拉文塔单向扩散）。「母文化 vs 姊妹文化 / 奥尔梅克→玛雅扩散」留在 Notes。古典玛雅「崩溃」明确不在 `civ-early-maya` 范围。`related_ids` 交叉保留并加争议标注。不伪造文物图、不编造页码。

### D-2026-10-11-11 — 将现有种子加厚为丰富事实条目

**决定：** 升级文明事实库的**深度**。过薄的一段式种子没有意义。采用 [`data/civilizations/_template.md`](../data/civilizations/_template.md) 加厚栏目，以及双语深度标准 [`entry-depth.zh.md`](entry-depth.zh.md) / [`entry-depth.md`](entry-depth.md)。

**说明：** 大型文明总览向可持久库状态加厚时，目标约 8–15+ 条已登记来源；每一主要栏目须引用；正文优先中英双语；禁止注水与不可核验「色彩」。状态阶梯：`draft` → `library-seed` → `library-seed-rich` → `fact-library`。试点：按新模板重写 `civ-mesopotamia` 并大幅增加真实来源（2026-10-11）。其他种子在同等加厚前仍为 `library-seed`。正直优先于速度。

### D-2026-10-11-12 — 古埃及加厚至 fact-library（对齐两河试点）

**决定：** 在两河试点加厚之后，按完整加厚模板重写 `civ-ancient-egypt`，状态升为 **`fact-library`**。

**说明：** 保留原有三条来源（Shaw 2000；Wilkinson 1999；Midant-Reynes 2000），并新登记十二条已核验来源（Kemp 2006；Bard 2015；Trigger 等 1983；Lehner 1997；Wengrow 2006；Butzer 1976；Allen 2014；Petrie《王陵》1900–1901 P；Quibell《希拉孔波利斯》1900 P；Quibell & Green 1902 P；Hoffman 1979；Edwards 1993）——合计 **15** 条 `src-*`。深度焦点：前王朝→早王朝→古王国（地理/尼罗河；年表；阿拜多斯、希拉孔波利斯、孟斐斯、萨卡拉、吉萨谨慎书写；国家形成；象形文字；经济；物质文化；对外接触；研究史）。纳尔迈/「统一」在 Notes 中作过程 + 有争议图像解读——不作单次事件定论。不编造页码；不伪造文物图。正直优先于速度。

### D-2026-10-11-13 — 安第斯（卡拉尔–北奇科）加厚至 fact-library

**决定：** 在两河与古埃及加厚之后，按完整加厚模板重写 `civ-andes`，状态升为 **`fact-library`**。

**说明：** 保留原有四条来源（Shady/Haas/Creamer *Science* 2001；Haas/Creamer/Ruiz *Nature* 2004；Shady & Leyva 2003；Shady 1997），并新登记十一条已核验来源（Creamer/Ruiz/Haas 帕蒂维尔卡 *Fieldiana* 2007 P；Creamer 等福塔莱萨 *Fieldiana* 2013 P；Haas 等 *PNAS* 玉米 2013；Moseley & Willey 阿斯佩罗 1973；Moseley 海洋生计基础 1975；Raymond 再检讨 1981；Haas & Creamer in Silverman 2004；Feldman in Haas/Pozorski/Pozorski 1987；Quilter 帕洛马 1989 比较；Burger 查文 1995 后续取向；教科文卡拉尔–苏佩名录 2009 T）——合计 **15** 条 `src-*`。深度焦点：北奇科晚古风地理；年表；卡拉尔、阿斯佩罗、卡瓦列特、瓦里坎加及邻谷试掘；纪念性建筑（平台丘、沉陷圆形广场、shicra、huancas）；无陶/未证实文字；灌溉 + 有争议的海洋模型 + 玉米多证据；仅区域内海岸—河谷互动；研究史。城市 vs 礼仪中心 / 国家 vs 复杂社会 / 海洋生计基础 / 玉米主粮程度一律留在 Notes。范围不含更晚安第斯帝国。不编造页码；不伪造文物图。正直优先于速度。
