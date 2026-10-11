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

### D-2026-10-11-14 — 印度河加厚至 fact-library（对齐两河/埃及/安第斯）

**决定：** 在两河、古埃及与安第斯加厚之后，按完整加厚模板重写 `civ-indus-valley`，状态升为 **`fact-library`**。

**说明：** 保留原有六条来源（Kenoyer 1991；Wright 2010；Kenoyer 2014 剑桥专章；Possehl 2002；Marshall 1931 P；Meadow 编 1991 P），并新登记九条已核验来源（Kenoyer 1998 通论；Mackay 1938 摩亨佐-达罗续掘 P；Vats 1940 哈拉帕 P；Parpola 1994 文字语料——破译方案不采纳为事实；Giosan 等 *PNAS* 2012 河流地貌；Rao 1979 洛塔尔 ASI 专报 P；Ratnagar 2004 贸易；教科文摩亨佐-达罗名录 1980 T；Wheeler 1968 研究史对照）——合计 **15** 条 `src-*`。深度焦点：大印度河区地理（印度河 / 加加尔–哈克拉；季风补给 vs 冰川大河争议）；Kenoyer Table I 年表；摩亨佐-达罗、哈拉帕、甘韦里瓦拉、拉希加里及层级遗址；城市网状平面 / 井排水 / 大浴场标签谨慎书写；文字未破译 + 砝码封泥；生计与手工业；Meluhha / 海湾接触；研究史。文字未破译、帝国 vs 城市网络、洛塔尔「船坞」、气候—去城市化一律留在 Notes。不编造页码；不伪造文物图。正直优先于速度。

### D-2026-10-11-15 — 中国青铜总览 + 三星堆加厚至 fact-library（对齐两河/埃及/安第斯/印度河）

**决定：** 在印度河加厚之后，按完整加厚模板重写 `civ-china-bronze` 与 `civ-sanxingdui`，状态均升为 **`fact-library`**。

**说明（中国青铜总览）：** 保留原有四条来源（Thorp 1991；Liu & Chen 2003；Flad & Chen 2013；Bagley 1987），并新登记十条已核验来源（Liu & Chen 2012 剑桥《中国考古学》；Campbell 2014 Cotsen 二里头→安阳；Keightley 1978 甲骨；Chang 1980 商文明；Thorp 2006 早期青铜时代；Li Chi 1977 安阳；Loewe & Shaughnessy 1999 / Bagley 商考古学专章；Underhill 2013 / Xu Hong 二里头文化专章；夏商周断代工程 2000 简本——作有争议年表方案；Rawson 编 1996 大英展览目录）——合计 **14** 条 `src-*`。深度焦点：中原地理与资源获取；二里头/二里岗/小双桥–洹北/安阳分期表；关键遗址；都会与制度；甲骨文；生计与块范铸造；礼器青铜；长江/北疆互动；研究史。**夏史实性与 XSZCP 绝对年一律留在 Notes**。不编造页码；不伪造文物图。

**说明（三星堆）：** 保留原有四条来源（四川 1999 P；Ge & Linduff 1990；Bagley 1988；Li et al. 2022），并新登记十条已核验来源（Bagley 编 2001《古代四川》；Xu 2001 青铜专章；Flad 2018 城市作为技术；Flad 2012 贵重物品；Sun Hua 2003 考古文化界定；Wu/Ran/Lei 2021 四号坑碳十四；教科文预备名单 5816 T；Zhao 2021 NSR 亮点；并交叉引用 Flad & Chen 2013、Rawson 1996）——合计 **14** 条 `src-*`。深度焦点：成都平原地理；遗址跨度/文化分期/坑年代分表；一–八号坑与金沙对照；礼仪中心与 Flad 城市模型；无甲骨级文字档案；礼仪经济与铸造；面具/神树/金器；与中原接触≠同一王国；研究史。**三星堆–商政体认同与坑绝对年代争议一律留在 Notes**。正直优先于速度。

### D-2026-10-11-16 — 爱琴 + 奥尔梅克 + 早期玛雅加厚至 fact-library（第一批加厚完成）

**决定：** 在中国青铜 / 三星堆加厚之后，按完整加厚模板重写 `civ-aegean`、`civ-olmec`、`civ-early-maya`，状态均升为 **`fact-library`**。本提交起，**全部九条**首批文明条目均为 `fact-library` 深度。

**说明（爱琴）：** 保留原有八条来源，并新登记六条已核验来源（Renfrew 1972；Warren & Hankey 1989；Chadwick 1976；Doumas 1983 阿克罗蒂里；Wace 1949 迈锡尼 P；Cline 编 2010 牛津手册）——合计 **14** 条 `src-*`。深度焦点：基克拉泽斯 / 克里特米诺斯 / 大陆迈锡尼地理；分期表（高/低年代分栏标注）；克诺索斯、迈锡尼、皮洛斯、阿克罗蒂里、早期基克拉泽斯遗址群；宫室城市；线性 A 未破译 / 线性 B 迈锡尼希腊语；经济与手工业；经埃及同步争议的对外接触；研究史。海上霸权与绝对年代一律留在 Notes。不编造页码；不伪造文物图。

**说明（奥尔梅克）：** 保留原有六条来源，并新登记七条已核验来源（Drucker 1952 拉文塔 P；Drucker/Heizer/Squier 1959 拉文塔 P；Cyphers 2004 雕塑编目；Clark & Pye 2000 国家美术馆文集；Benson & de la Fuente 1996 / González Lauck；Blomster 等 2005 *Science* 陶器 INAA；Taube 2004 Dumbarton Oaks）——合计 **13** 条 `src-*`。深度焦点：海湾心脏地带地理；形成期年表；圣洛伦佐、拉文塔、查尔卡钦戈；纪念性城市；不宣称已破译文字；生计/手工业与陶器外销模型；对外接触；研究史。母文化 vs 姊妹文化与 Diehl 书名「最早」一律留在 Notes。正直优先于速度。

**说明（早期玛雅）：** 保留原有五条来源，并新登记七条已核验来源（Saturno/Stuart/Beltrán 2006 圣巴托洛 *Science*；Clark & Hansen 2001 早期王权/MFC；Demarest 2004；Inomata 等 2019 塞瓦尔高原 *PLOS ONE*；Coe & Houston 2015；Hansen 1998 纳克贝；Willey 等塞瓦尔皮博迪系列 P）——合计 **12** 条 `src-*`。深度焦点：低地地理；前古典–早古典年表；塞瓦尔、纳克贝、埃尔米拉多尔、西瓦尔、圣巴托洛；E 组与人造高原；晚前古典文字；生计；与奥尔梅克互动作争议；研究史。古典崩溃不在范围。正直优先于速度。

### D-2026-10-11-17 — 产品核心 = 档案 + 只读 API（百科散文是呈现层）

**决定：** 经圆桌会话 [`delib-2026-10-11-archive-api-direction`](../deliberations/delib-2026-10-11-archive-api-direction.md) 审议后，产品核心定为**数字档案 + 只读 API**，而非仅博客/百科页面。双语文明 Markdown 仍是有价值的**编辑 / 呈现**层，可以继续加厚，但加厚必须**喂入结构化档案记录**（来源 Source、遗址 Site、分期 Period、组合/器物 Assemblage/Object 含权利、主张 Claim 事实 vs 假说、媒体 Media 仅权利清晰、审议 Deliberation）。API 对这些实体做 list/filter/get；每条带 `sources[]`；假说绝不自动升格。

**可检验的下一步：** JSON Schema 和/或 SQLite DDL；从 MD + 附属结构化文件导出并作出处失败即关闭；OpenAPI 档案路径（`/sites`、`/periods`、`/objects`、`/claims`、`/media`）；选一条文明做完整结构化试点（优先 `civ-mesopotamia`）。云端审议仍先规范后实现（D-2026-10-11-2 不变）。不上伪造文物图。

**说明：** 细化 D-2026-10-11-4 —— git Markdown 仍是已发布编辑权威；经闸门的 `export/` 作为 API 服务形态（禁止静默双写）。架构：档案层专节。接口：§4.6。OpenAPI 已增档案集合草图。

### D-2026-10-11-18 — Schema 草稿 + 两河结构化试点启动

**决定：** 落实审议 [`delib-2026-10-11-archive-api-direction`](../deliberations/delib-2026-10-11-archive-api-direction.md) / D-2026-10-11-17 的 FUTURE_WINDOW：在 [`schemas/`](../schemas/) 落地 JSON Schema 草稿；双语数据模型文档 [`archive-data-model.zh.md`](archive-data-model.zh.md)；结构化试点 [`data/structured/mesopotamia/`](../data/structured/mesopotamia/)；出处失败即关闭校验 [`tools/export_check.py`](../tools/export_check.py)。

**说明：** 试点 JSON **仅**派生自 `civ-mesopotamia.md` + 已登记 `src-mesopotamia-*`。不新增考古主张；不上伪造图；假说主张保持标注。OpenAPI 档案路径已有草图（§4.6）；文档现指向 schemas + 试点。运行：`.venv/bin/python tools/export_check.py`。

### D-2026-10-11-19 — 只读档案 API 落地 + 埃及结构化包

**决定：** 落实 D-2026-10-11-17 / FUTURE_WINDOW：落地本地**只读** HTTP API（FastAPI），服务 `data/structured/*` 全部包；新增埃及结构化包 [`data/structured/egypt/`](../data/structured/egypt/)；[`tools/export_check.py`](../tools/export_check.py) 校验**全部**包。

**说明：**
- API：`python -m api.serve`（默认绑定 `127.0.0.1:8080`）。路径：`/api/v1/healthz`、`/civilizations`、`/sources`、`/sites`、`/periods`、`/objects`、`/claims`、`/media`。分页 v0：`limit`+`offset`。无写路由。主张响应展开 `sources` 引用；假说 `kind: hypothesis`。
- 埃及包**仅**派生自 `civ-ancient-egypt.md` + `src-egypt-*`（15 来源 · 6 遗址 · 6 分期 · 4 器物组合 · 10 主张含纳尔迈「单次统一」假说 · 2 外链媒体）。不新增考古发明；不上伪造图。
- Markdown 仍是编辑真源；结构化 JSON 是经闸门的服务形态（禁止静默双写）。


### D-2026-10-11-20 — 其余七个文明结构化档案包进 API

**决定：** 在两河 / 埃及试点之后，为其余七个 `fact-library` 文明落地结构化包，使只读 API 可列出全部九个文明：`andes`、`indus`、`china-bronze`、`sanxingdui`、`aegean`、`olmec`、`early-maya`（外加既有 `mesopotamia`、`egypt`）。

**说明：**
- 各包 JSON **仅**派生自对应 `civ-*.md` + 已登记 `src-*`；争议项进 `kind: hypothesis`；不上伪造文物图；媒体仅外链元数据。
- 种子定义：`tools/pack_seeds/*.json`；写入器：`tools/write_packs_from_seeds.py`。
- `tools/export_check.py` 对全部 9 包通过出处闸门。API 冒烟：`GET /api/v1/civilizations` 返回 9 条。
- Markdown 仍是编辑真源；结构化 JSON 是经闸门的服务形态。

### D-2026-10-11-21 — 两河档案密度加深（遗址 + 一手来源）

**决定：** 按主人优先项，先加深两河试点档案密度：登记可核验的遗址级发掘/调查报告（P）与强二手（S），扩展结构化遗址/器物组合/主张，并同步 `civ-mesopotamia.md` 关键遗址与来源栏。

**本轮新增（均经 WebSearch/目录页核验书目；access_date 2026-10-11；不编造页码/坐标/伪造图）：**

主要 **P** 档：
- Nippur OIP 78（McCown & Haines 1967）、OIP 97（McCown, Haines & Biggs 1978）
- Tell Asmar OIP 43（Frankfort, Lloyd & Jacobsen 1940）；Khafajah OIP 53（Delougaz 1940）；OIC 13 首季初步报告（1932）
- Jemdet Nasr Matthews 2002；Kish Mackay 1925；Eridu Safar, Mustafa & Lloyd 1981；al-‘Ubaid Hall & Woolley 1927；Mari Ishtar Parrot 1956；Abu Salabikh ASE 1 Postgate 1983

主要 **S** 档：Parrot Tello 1948；Moorey Kish 1978；Martin Fara 1988；Adams Diyala 1965；Strommenger Habuba Kabira 1980

**结构化结果（mesopotamia 包）：** 来源 15→31；遗址 7→17；器物组合 4→16；主张 10→23；`tools/export_check.py` 全仓通过。

**说明：** 吉尔苏（特罗）与希巴丘（拉格什本城）分列；Habuba 记为已发掘的乌鲁克相关城镇事实，Algaze 扩张模型仍为假说。完整性优先于速度。

### D-2026-10-11-22 — 埃及档案密度加深（遗址 + 一手来源）

**决定：** 按主人优先项（对齐两河 D-21），加深埃及结构化包：登记可核验的前王朝–古王国遗址级发掘报告（P），并同步 `civ-ancient-egypt.md` 关键遗址与来源栏。

**本轮新增（均经 WebSearch/目录页核验书目；access_date 2026-10-11；不编造页码/坐标/伪造图）：**

主要 **P** 档：
- Petrie & Quibell《Naqada and Ballas》1896；Petrie《Abydos》I 1902；Randall-MacIver & Mace《El Amrah and Abydos》1902
- Petrie《Tarkhan I and Memphis V》1913、《Tarkhan II》1914；Petrie《Medum》1892
- Reisner《Mycerinus》1931；Firth & Quibell《Step Pyramid》1935；Emery《Great Tombs》III 1958
- Kaiser 等象岛 MDAIK 26（1970）；von der Way《Buto I》AV 83（1997）；Adams HK6 BAR S903（2000）；Saad《Excavations at Helwan》1969（发掘者综合）

**结构化结果（egypt 包）：** 来源 15→28；遗址 6→13；器物组合 4→16；主张 10→24；`tools/export_check.py` 全仓通过。

**说明：** 孟斐斯仍为通论级政治中心取向（精确落点=假说）；巴拉斯前王朝墓地不与晚期 Deir el-Ballas 宫殿混同；不编造吉萨劳工人数；萨卡拉第一王朝大墓与阿拜多斯王陵分列。完整性优先于速度。

### D-2026-10-11-23 — 印度河档案密度加深（遗址 + 一手来源）

**决定：** 按主人优先项（对齐两河 D-21 / 埃及 D-22），加深印度河结构化包：登记可核验的遗址级发掘/调查报告（P/S），并同步 `civ-indus-valley.md` 关键遗址与来源栏。

**本轮新增（均经 WebSearch/目录页核验书目；access_date 2026-10-11；不编造页码/坐标/伪造图）：**

主要 **P** 档：
- Bisht《Excavations at Dholavira》2015（ASI **草稿**/网站发布；注明在出版中）
- Lal 等卡利班甘早期 MASI 98（2003）；Lal 等成熟期 MASI 110（2015/2020）
- Mackay《Chanhu-daro Excavations, 1935–36》1943（美国东方学会）
- Khan「Excavations at Kot Diji」，《巴基斯坦考古学》第 2 期（1965）
- Casal《Fouilles d’Amri》1964
- Joshi《Excavations at Surkotada》MASI 87（1990）
- Nath《Excavations at Rakhigarhi》（1997–2000 季；ASI **草稿**）
- Shinde 等拉希加里墓地 *PLoS ONE* 2018（DOI 10.1371/journal.pone.0192299）
- Jarrige 等编《Mehrgarh: Field Reports 1974–1985》1995

主要 **S** 档：Mughal 1982 乔利斯坦专章（Possehl 编）；Mughal《Ancient Cholistan》1997（甘韦里瓦拉 / 哈克拉调查）。

**T** 档：教科文陀罗维拉名录 2021（WHC 1645）。

**结构化结果（indus 包）：** 来源 15→28；遗址 6→12；器物组合 4→16；主张 8→23；媒体 2→5；`tools/export_check.py` 全仓通过。

**说明：** Bisht/Nath 按草稿引用；甘韦里瓦拉仍为调查遗址（不编造探方清单）；拉希加里「东部都城」、科特迪吉征服/大火、洛塔尔船坞、气候单因、帝国 vs 网络一律留在假说栏。完整性优先于速度。

### D-2026-10-11-24 — 安第斯/卡拉尔–北奇科档案密度加深（遗址 + 一手来源）

**决定：** 按主人优先项（对齐两河 D-21 / 埃及 D-22 / 印度河 D-23），加深安第斯结构化包：登记可核验的卡拉尔、阿斯佩罗及其他苏佩/帕蒂维尔卡/福塔莱萨/华乌拉遗址级发掘与调查文献（P/S），并同步 `civ-andes.md` 关键遗址与来源栏。

**本轮新增（均经 WebSearch/目录页/期刊页核验书目；access_date 2026-10-11；不编造页码/坐标/伪造图）：**

主要 **P** 档：
- Willey & Corbett《Early Ancón and Early Supe Culture》1954（含阿斯佩罗；历史年代框架过时）
- Feldman《Aspero…》哈佛博士论文 1980
- Creamer 等已有 Fieldiana 帕蒂维尔卡 2007 / 福塔莱萨 2013（本轮把波韦尼尔、绍拉、塞罗布兰科等分列进遗址）
- Chu Barrera《Household Organization… Bandurria》匹兹堡博士论文 2011
- Zechenter《Subsistence Strategies in the Supe Valley…》UCLA 博士论文 1988

主要 **S** 档：Feldman 1985（Donnan 编）；Fung 1988（Keatinge 编）；Chu 2006《Boletín de Arqueología PUCP》10；Quilter 等 1991 *Science*（埃尔帕莱索，比较）；Sandweiss 等 2009 *PNAS*（环境废弃=假说）；Kosok 1965；Engel 1987；Haas & Creamer 2006 *Current Anthropology*；Shady 2008 PEACS 综述 PDF（「最古老」=营销语，不定论）。

**结构化结果（andes 包）：** 来源 15→28；遗址 6→14；器物组合 3→16；主张 7→27；媒体 1→6；分期 5→7；`tools/export_check.py` 全仓通过。

**说明：** 丘帕西加罗（西）与卡拉尔分列；Vichama 仅作 PEACS 名录指针（常偏早期成型、晚于卡拉尔纪念性窗）；环境突变废弃、阿斯佩罗酋邦、班杜里亚挑战酋邦/国家、玉米主粮强度、「最古老文明」一律假说栏。完整性优先于速度。

### D-2026-10-11-26 — 设计品味（表里如一）

**决定：** 为本仓库采纳明确的工艺标准：产品 = **档案 + 只读 API**；文案与 `/ui` 是呈现层。原则取自 Paul Graham《Taste for Makers》与乔布斯式「看见的与看不见的都要过关」：简单、解决对的问题、辛苦却显得轻松、一致、克制、诚实（UI 上事实 ≠ 假说必须醒目）、不做装饰性谎言、不上伪造文物图。

**随本决定交付：**
- [`design-taste.zh.md`](design-taste.zh.md) / [`design-taste.md`](design-taste.md) — 原则 + README / API 信封 / `/ui` / 文档检查清单
- 浏览 UI：**`/ui`**（`api/static/ui.html`）— 双语、`prefers-color-scheme` 深浅色、主张 kind 徽章、来源可展开、无库存文物图
- API 根 `/api/v1/` 原则优先文案 + `browse_ui: /ui`
- README「为何不是维基百科」+「试用 API / UI」（诚实，非空话）

**说明：** 灵感指针（公开编译帖）：https://x.com/Jaden_riku/status/2108876904002670873 — 致敬 Graham 原文；勿整篇粘贴受版权保护文字。并行的档案加厚可能继续改 `data/structured/*`；本决定不编造考古内容。

### D-2026-10-11-25 — 中国青铜 + 三星堆档案密度加深（遗址 + 一手来源）

**决定：** 按主人优先项（对齐两河 D-21 / 埃及 D-22 / 印度河 D-23 / 安第斯 D-24），同时加深中国青铜（中原）与三星堆结构化包：登记可核验的遗址级发掘报告/简报（P）与强二手（S），扩展结构化遗址/器物组合/主张，并同步 `civ-china-bronze.md` 与 `civ-sanxingdui.md`。

**本轮新增（均经 WebSearch/目录页核验书目；access_date 2026-10-11；不编造页码/坐标/伪造图）：**

**中国青铜主要 P：**
- 《偃师二里头：1959–1978》（社科院考古所，中国大百科全书出版社 1999）
- 《二里头：1999–2006》五卷（文物出版社 2014，ISBN 9787501041077）
- 《偃师商城》第1卷（科学出版社 2013，ISBN 9787030386991）
- 《郑州二里岗》（1959）；《郑州商城：1953–1985》三卷（文物出版社 2001）
- 《郑州小双桥：1990–2000》（科学出版社 2012）
- 洹北宫殿区一、二号基址简报（《考古》2003.5、2010.1）
- 《殷墟发掘报告 1958–1961》（文物出版社 1987）
- 《盘龙城：1963–1994》（文物出版社 2001）
- 《垣曲商城（一）》1996；《垣曲商城（二）》2014

**中国青铜 S/T：** 《中国考古学·夏商卷》2003；教科文殷墟世界遗产 2006（WHC 1114）。

**三星堆/金沙主要 P：**
- 一、二号坑《文物》1987.10 / 1989.5 简报；1999《三星堆祭祀坑》已有
- Graham 1934 Hanchow/月亮湾初步报告（JWCBRS 6）
- 东城墙 2016 年度简报（《四川文物》2024.2）
- 金沙梅苑 2004《文物》简报；《资料集（一）》2013；《祭祀区发掘报告》2022 五卷（ISBN 9787501077786）

**三星堆 S：** 陈显丹 1990；马继贤 1993 月亮湾追记；金沙 2006 通俗综合（仅取向）。

**结构化结果：**
- **china-bronze：** 来源 14→28；遗址 4→12；器物组合 3→16；主张 6→24；分期 5→7；媒体 0→1
- **sanxingdui：** 来源 14→28；遗址 4→10；器物组合 3→16；主张 6→23；分期 5→7；媒体 1→1
- `tools/export_check.py` 全仓通过。

**说明：** 夏史实性、二里头=夏都、郑州/偃师/洹北文献王都指认、盘龙城=商前哨、三星堆=商同一政体、三星堆→金沙简单迁都、「古蜀国」完备国家实体一律留在假说栏。完整性优先于速度。

### D-2026-10-11-27 — 爱琴 + 奥尔梅克 + 早期玛雅档案密度加深（完成九包第一轮）

**决定：** 按主人优先项（对齐两河 D-21 / 埃及 D-22 / 印度河 D-23 / 安第斯 D-24 / 中国青铜+三星堆 D-25），加深爱琴、奥尔梅克、早期玛雅三包：登记可核验遗址级发掘报告/简报（P）与强二手（S），扩展结构化遗址/器物组合/主张，并同步对应 `civ-*.md`。本决定完成九个文明包的**第一轮**档案密度加深。

**本轮新增（均经 WebSearch/目录页/期刊页核验书目；access_date 2026-10-11；不编造页码/坐标/伪造图）：**

**爱琴主要 P：**
- Lang《Palace of Nestor》Vol. II 壁画 1969；Blegen 等 Vol. III 1973
- Shaw & Shaw《Kommos》Vol. I 1995；Betancourt Vol. II 1990；Watrous Vol. III 1992
- Platon《Zakros》1971（发掘者英文专书）
- Iakovidis《Γλας II》1998

主要 **S：** French《Mycenae》2002；Mountjoy 迈锡尼彩陶手册 1986；Barber 基克拉泽斯 1987；Macdonald/Hood 克诺索斯交叉；Davis《Sandy Pylos》1998；Palaima Linear B 行政指针。

**奥尔梅克主要 P：**
- Stirling BAE Bulletin 138（1943）；Weiant BAE 139；Drucker BAE 140
- Pool 编 Tres Zapotes Cotsen 专书 2003
- Ortiz & Rodríguez 埃尔马纳蒂圣泉献祭项目叙述
- Symonds/Cyphers《Asentamiento… San Lorenzo》UNAM；Rust & Sharer 1988 *Science* 拉文塔聚落

主要 **S：** Flannery & Marcus 母文化批判；Clewlow 等巨石头像目录；Benson 1981 邻境文集；Milbrath 雕塑年代；Cyphers《Las bellas teorías…》。

**早期玛雅主要 P：**
- Inomata 等 2020 *Nature* 阿瓜达费尼克斯；Inomata 等 2015 *PNAS* 塞瓦尔
- Hammond《Cuello》1991
- Laporte & Fialko 1995 *Ancient Mesoamerica* 失落世界
- Ricketson 1937 / Smith 1950 瓦哈克通卡内基报告
- Matheny NWAF 米拉多尔老虎群；Hansen 盆地报告指针
- Healy 卡哈尔佩奇；Garber 布莱克曼艾迪

主要 **S：** McAnany《Living with the Ancestors》；Ashmore 低地聚落；Schele & Freidel（假说卫生用）。

**结构化结果：**
- **aegean：** 来源 14→28；遗址 4→14；器物组合 3→16；主张 6→24；分期 5→7；媒体 1→4
- **olmec：** 来源 13→28；遗址 3→12；器物组合 3→16；主张 5→24；分期 3→4；媒体 1→4
- **early-maya：** 来源 12→28；遗址 5→14；器物组合 3→16；主张 6→26；分期 4→5；媒体 1→4
- `tools/export_check.py` 全仓通过。

**说明：** 爱琴高/低年代、海上霸权、荷马等同；奥尔梅克母文化/帝国/单向陶器出口；玛雅单向奥尔梅克起源、米拉多尔「首个国家」、中前古典完备神王等一律假说栏。完整性优先于速度。九包第一轮密度加深至此完成。


### D-2026-10-11-28 — 两河 + 埃及第二轮档案密度加深

**决定：** 在第一轮（D-21 / D-22）之后，对两河与埃及结构化包再做一轮**遗址级一手/强二手**加深：只登记可核验发掘报告与稳定 URL；扩展遗址、器物组合、事实主张；争议进假说栏；同步 `civ-mesopotamia.md` / `civ-ancient-egypt.md` 的 Key sites 与 Sources；全仓 `export_check` 必须通过。完整性优先于速度。

**本轮主要新增 P（及必要 S）：**

**两河：**
- Speiser《Tepe Gawra》I 1935；Tobler《Tepe Gawra》II 1950（Archive）
- Lloyd & Safar Tell Uqair，JNES 2 (1943)，DOI 10.1086/370671
- Wilson《Bismaya / Adab》OIP 138 (2012) PDF；Banks《Bismya》1912（S，通俗）
- Delougaz & Lloyd《Pre-Sargonid Temples》OIP 58 (1942) — Tell Agrab 沙拉神庙
- Oates Choga Mami 1967–68，*Iraq* 31 (1969)
- Andrae《Die archaischen Ischtar-Tempel in Assur》1922（Archive / Heidelberg Digi）
- Mallowan Brak & Chagar Bazar，*Iraq* 9 (1947)
- Hrouda 编《Isin–Išān Baḥrīyāt》I 1977（LMU 项目页）

**埃及：**
- Brunton & Caton-Thompson《Badarian Civilisation》1928；Brunton《Qau and Badari》I 1927
- Petrie 等《Labyrinth, Gerzeh and Mazghuneh》1912；Petrie《Diospolis Parva》1901
- Mond & Myers《Cemeteries of Armant》I 1937；Brunton《Mostagedda》1937
- de Morgan《Fouilles à Dahchour》1895；Borchardt 萨胡拉图版卷 1913
- Chłodnicki 等《Tell el-Farkha I》2012（UJ / PCMA）
- Rizkana & Seeher《Maadi》四卷 1987–1990（DAI 项目页）

**结构化结果（export_check）：**
- **mesopotamia：** 来源 31→41；遗址 17→25；器物组合 16→24；主张 23→32
- **egypt：** 来源 28→38；遗址 13→24；器物组合 16→26；主张 24→35
- 其余七包不变；全仓闸门通过。

**说明：** 布拉克=乌鲁克殖民地、塔西安简单早于巴达里等留在假说栏；不编造坐标/馆藏号/伪造图；README 不写死实时计数（以 `export_check` 为准）。

### D-2026-10-11-29 — 印度河 + 安第斯第二轮档案密度加深

**决定：** 在第一轮（D-23 / D-24）之后，对印度河与安第斯结构化包再做一轮**遗址级一手/强二手**加深：只登记可核验发掘报告与稳定 URL；扩展遗址、器物组合、事实主张；争议进假说栏；同步 `civ-indus-valley.md` / `civ-andes.md` 的 Key sites 与 Sources；全仓 `export_check` 必须通过。完整性优先于速度。

**本轮主要新增 P（及必要 S）：**

**印度河：**
- Majumdar《Explorations in Sind》ASI Memoir 48（1934）（Archive）
- Hargreaves《Excavations in Baluchistan》ASI Memoir 35（1929）— Nāl / Mastung
- Francfort & Pottier Shortughaï 初报，*Arts asiatiques* 34（1978）（Persée）；Francfort《Fouilles de Shortughaï》1989
- Durrani Rehman Dheri，*Ancient Pakistan* 6（1988）
- Jarrige Nausharo，*Pakistan Archaeology* 24（1989）；CRAI 1996 综述（S）
- Wheeler Harappa 1946，*Ancient India* 3（1947）（历史 P；无稳定开源 PDF 则 url 留空）
- Dales Balakot，*JFA* 1（1974），DOI 10.1179/jfa.1974.1.1-2.3
- Stein Ghaggar–Hakra / ‘Sarasvati’ 调查，*Geographical Journal* 99（1942），DOI 10.2307/1788862

**安第斯：**
- Bird《Huaca Prieta》AMNH Anthropological Papers 62(1)（1985）
- Grieder 等《La Galgada》(1988) UT Press
- Pozorski & Pozorski《Early Settlement… Casma Valley》(1987)；Sechín Alto 章（2002，S）
- Fuchs 等 Sechín Bajo，*Boletín de Arqueología PUCP* 13（2009）
- Vega-Centeno Cerro Lampay，*Latin American Antiquity* 21（2010）；PUCP 2006（S）
- Engel Asia Unit I，APS *Transactions* 53(3)（1963）
- Benfer Paloma，*Latin American Antiquity* 1（1990）（S）；Moseley maritime retrospect，*Andean Past* 3（1992）（S，假说）

**结构化结果（export_check）：**
- **indus：** 来源 28→38；遗址 12→20；器物组合 16→24；主张 23→33
- **andes：** 来源 28→38；遗址 14→22；器物组合 16→24；主张 27→36
- 其余七包不变；全仓闸门通过。

**说明：** 肖图盖「殖民点」、巴拉科特湾区贸易节点、卡斯马/北奇科「最早」排名、海洋奠基模型等留在假说栏；卡斯马与奇卡马/亚洲等为**比较基线**，不并入单一北奇科政体；不编造坐标/馆藏号/伪造图；README 计数以 `export_check` 为准。

### D-2026-10-11-30 — 中国青铜 + 三星堆 + 爱琴 + 奥尔梅克 + 早期玛雅第二轮档案密度加深

**决定：** 在第一轮（D-25 / D-27）之后，对剩余五包再做一轮**遗址级一手/强二手**加深：只登记可核验发掘报告与稳定 URL；扩展遗址、器物组合、事实主张；争议进假说栏；同步各 `civ-*.md` 的 Key sites 与 Sources；全仓 `export_check` 必须通过。完整性优先于速度。至此九包第二轮密度加深完成。

**本轮主要新增 P（及必要 S）：**

**中国青铜：**
- 《殷墟妇好墓》1980（文物出版社）
- 《襄汾陶寺——1978～1985年发掘报告》2015；《襄汾陶寺——1999～2001年考古发掘报告》2025
- 《新干商代大墓》1997；《吴城：1973～2002年考古发掘报告》2005
- 《沣西发掘报告》1962；《殷墟花园庄东地甲骨》2003
- 《铜绿山古矿冶遗址》1999；《侯马铸铜遗址》1993
- Shaughnessy《Sources of Western Zhou History》1991（S）

**三星堆：**
- 宝墩 2009–2010 调查试掘简报（成都考古发现 2009）
- 江章华《长江上游先秦考古研究》2022（S）
- 十二桥 / 仁胜村 / 青关山 / 仓包包 / 金沙兰苑田野文献指针
- Flad & Chen 2013 成都平原框架（包内复用）

**爱琴：**
- Pendlebury《Archaeology of Crete》1939（Archive）
- Cadogan《Palaces of Minoan Crete》1976；Driessen & Macdonald《Troubled Island》1997
- Hawes《Gournia…》1908；Cummer & Schofield《Keos》III 1984
- Palaikastro BSA 系列；Marinatos《Excavations at Thera》季报
- Taylour 1983；Hope Simpson 1981；Wiener 年代学指针（S）

**奥尔梅克：**
- Rodríguez et al. Cascajal《Science》2006；Mora-Marín 2020《Ancient Mesoamerica》
- Martínez Donjuán Teopantecuanitlán；Ortiz & Rodríguez Manatí 1988 初报
- San Andrés / Llano del Jícaro / Arroyo Pesquero（语境警示）/ El Remolino / Ojochi

**早期玛雅：**
- Forsyth Nakbe ceramics 1993；Estrada-Belli Cival 2006
- Willey et al. Belize Valley 1965；Kosakowsky Cuello 2003
- Cerros / Lamanai / Yaxuná FAMSI 1988 / Holmul 项目文献
- Hansen et al. Mirador–Calakmul LiDAR 2022

**结构化结果（以 `export_check` 为准）：**
- **china-bronze：** 来源 28→38；遗址 12→20；器物组合 16→24；主张 24→34
- **sanxingdui：** 来源 28→38；遗址 10→18；器物组合 16→23；主张 23→31
- **aegean：** 来源 28→38；遗址 14→23；器物组合 16→24；主张 24→32
- **olmec：** 来源 28→38；遗址 12→19；器物组合 16→24；主张 24→31
- **early-maya：** 来源 28→38；遗址 14→22；器物组合 16→24；主张 26→33
- 全仓闸门通过。

**说明：** 陶寺=尧都、新干=商方国都邑、青关山=王宫、宝墩直线前身国家、锡拉喷发=LM IB 唯一主因、高/低年代单一日历、Cascajal「最早文字」无争议、Arroyo Pesquero 当作层位闭合组合、米拉多尔「首个国家」、中前古典完备神王等一律假说栏。不编造坐标/馆藏号/伪造图；README 计数以 `export_check` 为准。

