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


### D-2026-10-12-1 — 两河 + 埃及第三轮档案密度加深

**决定：** 继续按老大优先级加深档案密度。对两河与埃及做**第三轮**可核验密度加深：登记尚未入库的一手（P）与强二手（S）发掘报告/语料；扩展结构化遗址、组合与主张；同步 `civ-mesopotamia.md` / `civ-ancient-egypt.md` 的关键遗址与来源列表；全仓 `export_check` 必须通过。诚信优于速度。

**本轮主要新 P（及必要 S）：**

**两河：**
- Woolley《乌尔发掘》II 皇家墓地（1934）；UE V 塔庙及周边（1939）
- Gibson 等《尼普尔发掘：第十二季》OIC 23（1978）
- Loud《霍尔萨巴德》I OIP 38（1936）；Loud & Altman《霍尔萨巴德》II OIP 40（1938）
- Green & Nissen ZATU / ATU 2（1987）；Legrain UE III 古朴印章印痕（1936）
- Mallowan《尼姆鲁德及其遗存》（1966）；Oates & Oates《尼姆鲁德》（2001，S）
- Hansen「Al-Hiba, 1968–1969」*Artibus Asiae* 32/4（1970）
- Koldewey《巴比伦发掘》（1914 英译）；Layard《尼尼微与巴比伦废墟中的发现》（1853，历史性 P）
- Weiss 等莱兰丘 1985 季 *AJA* 94/4（1990）；de Genouillac《特罗发掘》I（1934）

**埃及：**
- Petrie《阿拜多斯》II（1903）；Reisner《纳加埃德戴尔》I（1908）
- Emery《第一王朝大墓》II（1954）；Emery《古朴埃及》（1961，S）
- Dreyer《Umm el-Qaab》I U-j 墓（1998）；Quibell《El Kab》（1898）
- Garstang《马哈斯纳与贝特哈拉夫》（1903）；Petrie《吉萨的金字塔与神庙》（1883）
- Junker《Gîza》I（1929）；Naville《德尔拜赫里神庙》I（1895）
- Petrie《伊拉洪、卡洪与古罗布》（1891）

**结构化结果（以 `export_check` 为准）：**
- **mesopotamia：** 来源 41→55；遗址 25→31；器物组合 24→37；主张 32→46
- **egypt：** 来源 38→49；遗址 24→31；器物组合 26→36；主张 35→46
- 其余七包不变；出处闸门通过。

**说明：** 莱兰丘气候崩溃与 U-j「最早文字」排序留假说栏；Layard/Koldewey 为历史性 P（非现代地层报告）；不编造坐标/馆藏号/伪造图；README 计数以 `export_check` 为准。

### D-2026-10-12-2 — 其余七包第三轮档案密度加深

**决定：** 在两河 + 埃及第三轮（D-2026-10-12-1）之后，对其余七包做**同标准第三轮**可核验密度加深：仅登记可核验 P/S；扩展遗址/组合/主张；争议进假说栏；同步各 `civ-*.md` 关键遗址与来源列表；全仓 `export_check` 必须通过。诚信优于速度。

**本轮主要新 P（及必要 S）：**

**安第斯：** Samaniego 等塞钦山（1985）；Pozorski Antiquity 1992 / 方房间 2011；Burger & Salazar-Burger 瓦里科托；Izumi Kotosh Andes 2/4；Sandweiss Jaguay / Keefer Tacahuay Science 1998；Dillehay Monte Verde II；Donnan 1985 文集（S）

**印度河：** Bisht 巴纳瓦利 1982/1984；Possehl & Raval 罗杰迪 1989；Rao 洛塔尔卷二 1985；Jansen/Urban 摩亨佐-达罗临时报告；Kenoyer 珠作贸易 1997；Fairservis 1961；Allchin 1968；Possehl Ancient Cities 1979；Shaffer 1992

**中国青铜：** 周原 CHAR 2017 / 凤雏三号简报；琉璃河燕国墓地 1995；天马—曲村；苏埠屯；孝民屯铸铜；归城；前掌大

**三星堆：** 鱼凫/江章宝墩城址；坑 3–8 官方简报；方池街；梅苑/十二桥加深；CPAS；Lin 2019 金沙工艺

**爱琴：** Caskey Hesperia 勒尔纳；Wiencke Lerna IV；Banks Lerna VII；Blegen Troy I；Popham Lefkandi I/II；Atkinson 菲拉科皮 1904；Furumark；Manning PLOS 2022

**奥尔梅克：** Stirling BAE 157；Cyphers 阿苏苏尔；Etlatongo；Tres Zapotes/Chalcatzingo 加深；Bernal 1969；Coe《墨西哥》第 8 版

**早期玛雅：** Matheny NWAF 45；Culbert TR 25A/25B；Coe 破译史；Martin & Grube；米拉多尔/圣巴托洛/霍尔穆尔/阿瓜达菲尼克斯加深

**结构化结果（以 `export_check` 为准）：**
- **andes：** 来源 38→48；遗址 22→29；器物组合 24→32；主张 36→45
- **indus：** 来源 38→48；遗址 20→26；器物组合 24→30；主张 33→41
- **china-bronze：** 来源 38→48；遗址 20→27；器物组合 24→31；主张 34→42
- **sanxingdui：** 来源 38→48；遗址 18→24；器物组合 23→30；主张 31→39
- **aegean：** 来源 38→48；遗址 23→28；器物组合 24→30；主张 32→40
- **olmec：** 来源 38→48；遗址 19→25；器物组合 24→31；主张 31→37
- **early-maya：** 来源 38→48；遗址 22→28；器物组合 24→31；主张 33→40
- 全仓闸门通过（含两河/埃及既有第三轮）。

**说明：** 卡斯马「最早国家」、印度河「帝国」、凤雏「社宫」、三星堆＝商/宝墩直线前身、锡拉＝LM IB 唯一主因与单一日历年、奥尔梅克母文化与 Cascajal「最早文字」、米拉多尔「首个国家」与中前古典完备神王等一律假说栏。不编造坐标/馆藏号/伪造图；README 计数以 `export_check` 为准。


### D-2026-10-12-3 — 两河 + 埃及第四轮档案密度加深

**决定：** 继续按老大优先级加深档案密度。对两河与埃及做**第四轮**可核验密度加深：仅登记尚未入库的一手（P）与必要强二手（S）；扩展结构化遗址、组合与主张；同步 `civ-mesopotamia.md` / `civ-ancient-egypt.md`；争议进假说栏；全仓 `export_check` 必须通过。诚信优于速度。

**本轮主要新 P（及必要 S）：**

**两河：**
- Delougaz《迪亚拉陶器》OIP 63（1952）；Frankfort 迪亚拉雕像 OIP 44（1939）
- Mallowan & Rose 阿尔帕契亚《Iraq》1935；Mallowan 查加尔巴扎尔第二季《Iraq》1937
- Woolley《乌尔发掘》VI 乌尔三朝建筑（1974）；UE VII 古巴比伦（1976）
- Parrot《马里》II.1 宫殿建筑（1958）；Starr《努兹》1937/1939
- Reuther 巴比伦 Merkes WVDOG 47（1926）；Englund ATU 5（1994）；Zettler 尼普尔伊南娜神庙 BBVO 11（1992）

**埃及：**
- Reisner《吉萨墓地史》I（1942）；Caton-Thompson & Gardner《Desert Fayum》（1934）
- Lauer《阶梯金字塔：建筑》（1936）；Petrie《Dendereh, 1898》（1900）
- Borchardt 尼乌塞尔拉陵庙（1907）；Jéquier 佩皮二世陵 I（1936）
- Brunton《Qau and Badari》II（1928）；Peet《阿拜多斯墓地》II（1914）
- Arnold《塞索斯特里斯一世金字塔》（1988）；Frankfort 塞提一世衣冠冢（1933）；Winlock 德尔拜赫里 1911–1931（1942）

**结构化结果（以 `export_check` 为准）：**
- **mesopotamia：** 来源 55→66；遗址 31→37；器物组合与主张相应增加
- **egypt：** 来源 49→60；遗址 31→37；器物组合与主张相应增加
- 其余七包不变；出处闸门通过。

**说明：** 努兹不作第三千纪南部城市；法尤姆新石器≠尼罗河国家唯一摇篮；奥西睿昂为新王国纪念建筑。不编造坐标/馆藏号/伪造图；README 计数以 `export_check` 为准。

### D-2026-10-12-4 — 其余七包第四轮档案密度加深

**决定：** 在两河 + 埃及第四轮（D-2026-10-12-3）之后，对其余七包做**同标准第四轮**可核验密度加深：仅登记可核验 P/S；扩展遗址/组合/主张；争议进假说栏；同步各 `civ-*.md` 关键遗址、来源列表与研究史；全仓 `export_check` 必须通过。诚信优于速度。至此九包第四轮密度加深完成。

**本轮主要新 P（及必要 S）：**

**安第斯：** Dillehay 瓦卡普列塔 2017；Bonavia 洛斯加维拉内斯 1982；Pozorski 瓦伊努纳 1990；Alva 查奥盐沼 1986；Izumi 希利亚科托 1972；Lanning 1967；Moseley 祖先综论 2001；Quilter 中央安第斯 2014；Dillehay 采集—农耕 2011；Sandweiss 2008 海洋模型评论

**印度河：** Dales & Kenoyer 陶器 1986；Flam 加齐沙阿 1996；Law 溯源 2011；Possehl 开端 1999；Lal 1997；Fairservis 1971；Allchin 兴起 1982；Chakrabarti 1995；Miller 技术方法 2007；Kenoyer 贸易技术 1997 WA

**中国青铜：** 小屯南地甲骨；殷墟发现与研究 1994；Keightley 祖先景观 2000；Li Feng 西周景观 2006；郑州铜器窖藏 1999；殷墟青铜器 1985；郭家庄 1998；Rawson Sackler 西周；Bagley CHAC 章；Underhill 手工业 2002

**三星堆：** 文物一/二号坑简报；3–8 号坑 2021 指针；金沙 2006 综合/资料集加深；Bagley Ancient Sichuan；赵殿增 2006；Flad ARA 2018；Ge & Linduff；UNESCO 预备清单加深

**爱琴：** Schliemann 梯林斯 1885 / 迈锡尼 1878；Mylonas B 圆圈墓；Wace 室墓 1932；Seager 普塞拉 1910；INSTAP 普塞拉指针；Mountjoy 1999；Hood/PRAP 指针

**奥尔梅克：** Coe Jaguar’s Children 1965；Rosenswig 2010；Grove 区域视角；Cyphers 雕塑语料加深；Pool 聚落指针；Diehl/Stirling/Drucker/Blomster/Taube 加深

**早期玛雅：** Altar Peabody 三卷；Pacbitun 2019；Cahal Pech E 组；Coe 蒂卡尔手册；Shook/Carnegie 指针；Rice；Maya Cosmos；Cival/Holmul 加深

**结构化结果（以 `export_check` 为准）：**
- **andes：** 来源 48→58；遗址 29→35；器物组合 32→38；主张 45→54
- **indus：** 来源 48→58；遗址 26→32；器物组合 30→36；主张 41→50
- **china-bronze：** 来源 48→58；遗址 27→33；器物组合 31→37；主张 42→51
- **sanxingdui：** 来源 48→58；遗址 24→30；器物组合 30→36；主张 39→48
- **aegean：** 来源 48→58；遗址 28→34；器物组合 30→36；主张 40→49
- **olmec：** 来源 48→58；遗址 25→31；器物组合 31→37；主张 37→44
- **early-maya：** 来源 48→58；遗址 28→34；器物组合 31→37；主张 40→49
- 两河/埃及本提交不变（已在 main 完成第四轮）。出处闸门通过。

**说明：** 争议项（加维拉内斯玉米优先；印度河帝国/破译；夏＝二里头；三星堆＝商殖民；荷马信史/锡拉单年；奥尔梅克母文化/Cascajal 已释读；中前古典完整神王/米拉多第一国家）留假说栏。不编造坐标/馆藏号/伪造图；README 计数以 `export_check` 为准。

### D-2026-10-12-5 — 两河 + 埃及第五轮档案密度加深

**决定：** 继续按老大优先级加深档案密度。对两河与埃及做**第五轮**可核验密度加深：仅登记尚未入库的一手（P）与必要强二手（S）；扩展结构化遗址、组合与主张；同步 `civ-mesopotamia.md` / `civ-ancient-egypt.md`；争议进假说栏；全仓 `export_check` 必须通过。诚信优于速度。其余七包与审议圆桌由后续任务安排。

**本轮主要新 P（及必要 S）：**

**两河：**
- Delougaz、Hill & Lloyd《迪亚拉私宅与墓葬》OIP 88（1967）
- Frankfort《迪亚拉层位圆柱印章》OIP 72（1955）
- Adams & Nissen《乌鲁克乡村》(1972)
- Andrae《亚述城防御工事》WVDOG 23（1913）；《安努—阿达德神庙》WVDOG 10（1909）
- Jacobsen & Lloyd《杰尔万的辛那赫里布渡槽》OIP 24（1935）
- Lloyd & Safar 哈苏纳 JNES 1945；Gibson《基什城与地区》(1972)
- Frankfort OIC 16（1933）/ OIC 17（1934）初步季报

**埃及：**
- Peet & Woolley《阿肯那顿之城》I（1923）；Frankfort & Pendlebury II（1933）；Pendlebury III（1951）
- Petrie《Tell el Amarna》(1894)；Petrie《Memphis I》(1909)
- Naville《Bubastis》(1891)；Naville《德尔拜赫里神庙》II（1896）
- Brunton《Matmar》(1948)；Quibell《Archaic Mastabas》(1923)；Mond & Myers《Temples of Armant》(1940)

**结构化结果（以 `export_check` 为准）：**
- **mesopotamia：** 来源 66→76；遗址 37→43；器物组合与主张相应增加
- **egypt：** 来源 60→70；遗址 37→43；器物组合与主张相应增加
- 其余七包本提交不变；出处闸门通过。

**说明：** 杰尔万「罗马前最早渡槽」、哈苏纳「最早村落」、阿马尔那「无前身纯规划唯一首都」一律假说栏。不编造坐标/馆藏号/伪造图；README 计数以 `export_check` 为准。

### D-2026-10-12-6 — 其余七包第五轮档案密度加深

**决定：** 在两河 + 埃及第五轮（D-2026-10-12-5）之后，对其余七包做**同标准第五轮**可核验密度加深：仅登记可核验 P/S；扩展遗址/组合/主张；争议进假说栏；同步各 `civ-*.md` 关键遗址、来源列表与研究史；全仓 `export_check` 必须通过。诚信优于速度。至此九包第五轮密度加深完成；下一步由父代理开审议。

**本轮主要新 P（及必要 S）：**

**安第斯：** Pozorski 拉马平原 JFA 1986；通风火塘 LAA 1996；Engel / Quilter 埃尔帕拉伊索；Burger / Rick–Kembel 查文；Haas–Pozorski 1987；Tello 1960；Proulx 内佩尼亚；Nesbitt 死马

**印度河：** Fairservis/Shaffer 阿拉赫迪诺；Sonawane/Bhan 戈拉多罗；Meadow & Kenoyer 城墙 1993；Jansen 水利；Lahiri 发现史；Vidale 手工业；Thapar 卡里班甘概述

**中国青铜：** 石璋如小屯建筑；侯家庄 1001/1002；YH127；洛阳北窑；Chang 1986；Allan 1991；社科院两周卷；邹衡 1980；西北冈社科院后续

**三星堆：** 《考古》2022 祭祀区 / CHAR 2023；芒城/郫县古城；博物馆图录；孙华；Flad–Chen；预备清单更新；2022 进展通报

**爱琴：** Hood 测绘图；Popham 未勘探邸宅；Blegen Troy III–IV；Wace 战后；Kommos IV；Cadogan Studies；PRAP 加深；Warren 石瓶；Higgins 陶俑

**奥尔梅克：** Stirling 路径；González Lauck A 组；Cyphers/Pool 加深；Grove 浮雕；Rust/Sharer 圣安德烈斯；Blomster；Cheetham；Diehl；Taube

**早期玛雅：** Seibal Peabody 多卷；Hansen 米拉多保护；Freidel 塞罗斯加深；失落世界/奎略/圣巴托洛加深；阿瓜达菲尼克斯后续；帕克比通；瓦哈克通 E 组；霍尔穆尔—西瓦尔

**结构化结果（以 `export_check` 为准）：**
- **andes：** 来源 58→68；遗址 35→41；器物组合 38→48；主张 54→65
- **indus：** 来源 58→68；遗址 32→38；器物组合 36→46；主张 50→61
- **china-bronze：** 来源 58→68；遗址 33→39；器物组合 37→47；主张 51→62
- **sanxingdui：** 来源 58→68；遗址 30→36；器物组合 36→46；主张 48→59
- **aegean：** 来源 58→68；遗址 34→40；器物组合 36→46；主张 49→60
- **olmec：** 来源 58→68；遗址 31→37；器物组合 37→47；主张 44→55
- **early-maya：** 来源 58→68；遗址 34→40；器物组合 37→47；主张 49→60
- 两河/埃及本提交不变（已在 main 完成第五轮）。出处闸门通过。

**说明：** 争议项（Tello 母体/卡斯马早期国家；印度河文字已破译；夏＝二里头/Allan 宇宙论；三星堆商殖民；特洛伊＝荷马战争；奥尔梅克母文化；米拉多第一国家）留假说栏。不编造坐标/馆藏号/伪造图；README 计数以 `export_check` 为准。

### D-2026-10-12-7 — 第五轮后优先序（审议圆桌）

**决定：** 经圆桌会话 [`delib-2026-10-12-after-pass5`](../deliberations/delib-2026-10-12-after-pass5.md) 审议后确认：

1. **现状定性：** 九包第五轮完成后，项目**已不再是「薄简介」**；已是可机读、带出处闸门与假说标签的**真实但仍不完备**的档案 + 本地只读 API + `/ui`。相对维基/穷尽性遗址报告：**覆盖面优势不成立**；**方法优势成立**（可查询实体、事实主张须可解析 `sources[]`、假说显式标注、不上伪造文物图）。
2. **明确不做：** 不为「看起来覆盖广」而编造内容；不把又一轮无审计的全仓堆量当作默认下一步；云端审议仍先规范后实现（D-2026-10-11-2 不变）。
3. **排序后的下一优先：**
   1. **主张/遗址质量审计** — 先从最密包两河、埃及开始（claim→source、假说标签、遗址完整度），再按缺口选择性加深  
   2. **可选新文明空壳** — 仅脚手架；禁止虚荣填充  
   3. **云端只读托管** — 审计基线可接受后再上；无写路由  
   4. **UI 工艺迭代** — 品味打磨，非改产品定义  
   5. **媒体** — 仅权利清晰的元数据/外链；不上伪造图；不整包倾销受版权保护 PDF/影像

**核实计数（`export_check` 2026-10-12，第五轮后）：** packs=9；sources **622**；sites **357**；periods **58**；objects **442**；claims **561**（fact 438 / hypothesis 123）；media **28**。

**说明：** 透镜为 AI 思维工具（`perspective: true`，`person_endorsement: false`），非人物背书。完整性优先于虚荣覆盖。


### D-2026-10-12-8 — 两河 + 埃及质量审计完成

**决定：** 按 D-2026-10-12-7 优先项 #1，完成 `data/structured/mesopotamia/` 与 `data/structured/egypt/` 的主张/遗址质量审计。全文见 [`docs/audits/audit-2026-10-12-mesopotamia-egypt.zh.md`](audits/audit-2026-10-12-mesopotamia-egypt.zh.md)（[English](audits/audit-2026-10-12-mesopotamia-egypt.md)）。

**结论：**
- **FAIL：0 / 0**（两河 / 埃及）。主张 `sources[]` 无空、无悬空；争议性「最早/唯一」排名已在假说栏并带免责；遗址无编造坐标；器物仅为组合/器类元数据（无假馆藏号）。
- **WARN（仍开放）：**（1）审计范围内 86 处遗址 `coordinates: null` — 有意为之，禁止编造；（2）书目元事实远多于实质考古事实（两河约 40/63，埃及约 46/63）— 下一步用*有出处*实质主张加深，禁虚荣散文；（3）少数手册式解释性措辞 — 仅观察清单；（4）媒体仍薄（仅外链）。
- **本轮 JSON 修复：** 无（无清晰 FAIL 可改标/删改）。禁止为消掉 WARN 而编造考古内容。

**核实：** 审计后 `export_check` 通过（9 包；出处闸门绿）。

**说明：** 诚信优于速度。开放 WARN 记入下一优先工作（有出处坐标 + 实质主张），不用假 FAIL 修复粉饰。


### D-2026-10-12-9 — 两河/埃及实质压贴 + 其余七包质量审计

**决定：**（A）落实 D-2026-10-12-8 的 W2：将两河 + 埃及 `kind=fact` 主张压贴为**报告级实质**（遗址出土/地层/组合为主语；报告作著录）。（B）对其余七个结构化包跑同一 FAIL/WARN 审计；仅修清晰 FAIL。

**Job A：**
- 两河改写 **57** 条事实主张；埃及 **59** 条；合计 **116**。
- 未编造页码、坐标、馆藏号或考古内容。
- 「作者出版」起句事实降至各包 **0/63**；W2 残留 = 报告范围深度仍非理想页级。
- 已更新 [`docs/audits/audit-2026-10-12-mesopotamia-egypt.zh.md`](audits/audit-2026-10-12-mesopotamia-egypt.zh.md)。

**Job B：**
- 报告：[`docs/audits/audit-2026-10-12-seven-packs.zh.md`](audits/audit-2026-10-12-seven-packs.zh.md)（[English](audits/audit-2026-10-12-seven-packs.md)）。
- **修复前 FAIL：4**（奥尔梅克书名排名作事实 1；早期玛雅跨包来源悬空 3）。**修复后：0**。
- 处理：改写 Diehl 主张；将两份已登记 olmec 来源 JSON 拷入 early-maya 以保包内引用完整。
- 开放 WARN：空坐标；书目元残留（中国青铜尤甚）；调查区当 site；媒体薄。

**核实：** `export_check` 通过（9 包；early-maya 来源拷入后为 70）。

**说明：** 诚信优于速度。本轮未对其余包做虚荣式全量改写。


### D-2026-10-12-10 — 有出处坐标 + outbound 媒体加厚（九包）

**决策：** 按 D-2026-10-12-8/9 开放的 W1（空坐标）与 W4（媒体薄），对全部九个结构化包做**诚实半填**。完整性服从出处诚实。

**坐标（已填 84；其余仍空）：**
| 包 | 已填 | 仍空 |
|------|-----:|-----:|
| 两河 | 29 | 14 |
| 埃及 | 22 | 21 |
| 爱琴 | 20 | 20 |
| 早期玛雅 | 6 | 34 |
| 印度河 | 3 | 35 |
| 奥尔梅克 | 2 | 35 |
| 安第斯 | 1 | 40 |
| 中国青铜 | 1 | 38 |
| 三星堆 | 0 | 36 |

**所用出处：** Pleiades CSV 代表点（`precision_note` 记 place id）；UNESCO WHC 公布 DMS；GeoNames `S.ANS` 考古遗址。模糊名称命中与调查区/locus/指针记录**不填**。

**媒体（+30 条 outbound；合计 28→58）：** `outbound-link-only`；无伪造器物图；`local_path` 仍为 null。

**审计更新：** [`audit-2026-10-12-mesopotamia-egypt.zh.md`](audits/audit-2026-10-12-mesopotamia-egypt.zh.md)、[`audit-2026-10-12-seven-packs.zh.md`](audits/audit-2026-10-12-seven-packs.zh.md)。

**核实：** `export_check` 通过。

**备注：** 诚实半填优于虚荣补全。三星堆本轮坐标全部有意留空。


### D-2026-10-12-11 — 公开网络地名录加厚（坐标 + 来源 + 媒体）

**决策：** 在 D-2026-10-12-10 之后继续诚实加厚 W1/W4。优先级：三星堆 → 中原青铜 → 安第斯 → 印度河 → 奥尔梅克 → 早期玛雅 → 埃及/爱琴剩余空位。不编造考古。

**坐标：** **+26**（累计 **84 → 110**）。三星堆/金沙用教科文预备名录 **5816**；查文用 **330**；其余用 Pleiades 或 GeoNames `S.ANS`/`S.RUIN`（国家锁定）。模糊命中不填。

**来源 / 媒体：** 新登记教科文查文与 npj 玉器 OA；青关山/四号坑补开放 PDF；新媒体 **+11**（**58 → 69**），仅出站链接。

**报告：** [`docs/audits/pass-2026-10-12-web-sources.zh.md`](audits/pass-2026-10-12-web-sources.zh.md)。

**核实：** `export_check` OK。

**备注：** 本工作区未找到 hermes/嘻嘻；付费书目只记题名、不伪造引用。


### D-2026-10-12-12 — 全球覆盖图 + 第一波壳包

**决策：** 发布双语**覆盖图**（复杂社会/有考古档案的早期文明，非维基式广度）。开设 **11 个第一波 `library-seed` 壳**，填补主要地理空白，同时**继续加厚**原有九个密包。**不等**完美密度再进 API/UI。**不削薄**密包。**不编造**发现、坐标或媒体图。

**覆盖图：** [`docs/coverage-map.zh.md`](coverage-map.zh.md) · [English](coverage-map.md)

**审议：** [`deliberations/delib-2026-10-12-global-coverage.md`](../deliberations/delib-2026-10-12-global-coverage.md) — 圆桌赞成「先开壳 + 继续加厚九包」。

**第一波包 id：** `elam-iran`、`nubia-kush`、`anatolia-hittite`、`levant-ugarit`、`bmac-oxus`、`nok-west-africa`、`teotihuacan`、`zapotec`、`lapita-pacific`、`dong-son`、`jomon-yayoi`（各含 `civ-*` + 结构化包；≥5 来源；1–3 遗址；1 时段；1 对象；1 条有出处主张）。

**第二/三波（未开）：** 安第斯晚期（查文/蒂瓦纳科/瓦里）、经典玛雅、阿克苏姆、班清、朝鲜半岛早期、米坦尼、腓尼基；以及卡霍基亚、大津巴布韦、印加等 — 见覆盖图。

**核实：** `export_check` OK（**20** 包）。API/UI 经目录自动发现新包。

**备注：** 诚信优先于速度。诚实壳优于虚荣密度。生成器：`tools/wave1_shells/generate_wave1.py`。


### D-2026-10-12-13 — 第一波加厚至 `library-seed-rich`

**决策：** 将 D-2026-10-12-12 开设的 11 个第一波包从 `library-seed` 加厚到可调用档案密度。Schema 状态阶梯使用 **`library-seed-rich`**（无自由文本 “expanding”）。诚信优先于完备：不编造考古、页码、坐标或媒体图。

**各包增量（结构化 JSON 计数）：**

| 包 | +来源 | +遗址 | +时段 | +对象 | +主张 | +媒体 | 加厚后（源/址/主张/时段/媒体） |
|----|------:|------:|------:|------:|------:|------:|--------------------------------|
| elam-iran | 10 | 5 | 3 | 2 | 10 | 3 | 15/8/11/4/3 |
| nubia-kush | 10 | 6 | 3 | 2 | 10 | 3 | 15/9/11/4/3 |
| anatolia-hittite | 10 | 5 | 3 | 2 | 10 | 3 | 15/7/11/4/3 |
| levant-ugarit | 10 | 5 | 3 | 2 | 10 | 2 | 15/7/11/4/2 |
| bmac-oxus | 10 | 5 | 3 | 2 | 10 | 2 | 15/7/11/4/2 |
| nok-west-africa | 10 | 5 | 3 | 2 | 10 | 3 | 15/7/11/4/3 |
| teotihuacan | 10 | 5 | 3 | 2 | 10 | 3 | 15/6/11/4/3 |
| zapotec | 10 | 5 | 3 | 2 | 10 | 3 | 15/6/11/4/3 |
| lapita-pacific | 10 | 5 | 3 | 2 | 10 | 2 | 15/7/11/4/2 |
| dong-son | 10 | 5 | 3 | 2 | 10 | 1 | 15/7/11/4/1 |
| jomon-yayoi | 10 | 5 | 3 | 2 | 10 | 3 | 15/6/11/4/3 |
| **合计** | **110** | **56** | **33** | **22** | **110** | **28** | — |

**坐标：** 教科文 WHC 公布 DMS + Pleiades CSV 代表点；其余保持 **null**。

**媒体：** 仅外链落地页；`local_path` 仍为 null。

**文档：** 覆盖图已更新；`civ-*.md` 与包 README 已同步。机器摘要：[`docs/audits/pass-2026-10-12-wave1-densify.json`](audits/pass-2026-10-12-wave1-densify.json)。

**核实：** `export_check` OK（**20** 包）。

**备注：** 仍远未及埃及/两河 `fact-library` 密度。诚实薄包优于虚荣密包。工具：`tools/wave1_shells/densify_wave1.py`。


### D-2026-10-12-14 — 第二波开壳

**决策：** 按覆盖图优先清单（D-2026-10-12-12）开设 **九个第二波 `library-seed` 壳**，不削薄既有密包或第一波包。诚信规则同第一波：仅真实 P/S/T 来源；摘要/目录级主张；不编造发现、坐标、页码或媒体图。

**第二波包 id：** `chavin-andes`、`tiwanaku`、`wari`、`classic-maya`、`aksum`、`ban-chiang`、`early-korea`、`mitanni`、`phoenician`（各 `civ-*` + 结构化包；5 来源；2–3 遗址；1 时段；1 对象；1 条有出处主张；0 媒体）。

**未开（仍属第三波 / 缺）：** 卡霍基亚；先祖普韦布洛；大津巴布韦；西非中世纪帝国；伊比利亚青铜；哈尔施塔特；努拉吉；拉帕努伊；印加全文；莫切；阿兹特克；米斯特克；吴哥/扶南；塞浦路斯晚青铜 — 见 [`coverage-map.zh.md`](coverage-map.zh.md)。

**文档：** 覆盖图与 README 列表已更新。生成器：`tools/wave2_shells/generate_wave2.py`。

**核实：** `export_check` OK（**29** 包）。API/UI 自动发现。

**备注：** 查文包使用独立遗址 id `site-chavin-huantar-type`，避免与安第斯包比较条目 `site-chavin-de-huantar` 冲突。诚实薄壳优于虚荣密度。

### D-2026-10-12-15 — 第三波开壳

**决策：** 从覆盖图仍缺项中开出 **十一个第三波 `library-seed` 壳**，填补北美、南部/西非中世纪、爱琴以外欧洲、大洋洲拉帕努伊（伦理优先）、安第斯莫切/印加、中美洲阿兹特克、东南亚吴哥等主要空白；不削薄既有包。诚信规则同前：仅真实 P/S/T 来源；摘要/目录级主张；不编造发现、坐标、页码或媒体图。

**第三波包 id：** `cahokia`、`ancestral-pueblo`、`great-zimbabwe`、`west-africa-medieval`、`hallstatt-celtic`、`nuragic-sardinia`、`rapa-nui`、`inca`、`moche`、`aztec`、`angkor`（各 `civ-*` + 结构化包；5 来源；2–3 遗址；1 时段；1 对象；1 条有出处主张；0 媒体）。

**未开（仍缺）：** 伊比利亚铜石并用/青铜；更完整拉坦诺；米斯特克；扶南拆分；塞浦路斯晚青铜加厚；伊费/贝宁；更广波利尼西亚酋邦；晚期基督教努比亚必要时拆分。

**文档：** 覆盖图与 README 已更新。生成器：`tools/wave3_shells/generate_wave3.py`。

**核验：** `export_check` OK（与 D-2026-10-12-16 一并落地后 **40** 包；出处闸门绿）。

**备注：** 西非中世纪以加纳–马里–桑海一包覆盖萨赫勒更干净。拉帕努伊伦理优先，不伪造摩艾图像。


### D-2026-10-12-16 — 第二波加厚至 `library-seed-rich`

**决策：** 将 D-2026-10-12-14 所开九个第二波包自 `library-seed` 加厚至可调用密度（`library-seed-rich`）。配方同第一波加厚：约 +10 来源、+5 遗址、+3 时段、+2 对象、+10 主张、+1–3 外链媒体。诚信优先：不编造考古、页码、坐标或媒体图。

**各包加厚后计数（结构化 JSON）：**

| 包 | sources | sites | periods | objects | claims | media |
|------|--------:|------:|--------:|--------:|-------:|------:|
| chavin-andes | 15 | 7 | 4 | 3 | 11 | 3 |
| tiwanaku | 15 | 7 | 4 | 3 | 11 | 2 |
| wari | 15 | 7 | 4 | 3 | 11 | 1 |
| classic-maya | 15 | 8 | 4 | 3 | 11 | 3 |
| aksum | 15 | 7 | 4 | 3 | 11 | 2 |
| ban-chiang | 15 | 7 | 4 | 3 | 11 | 2 |
| early-korea | 15 | 7 | 4 | 3 | 11 | 2 |
| mitanni | 15 | 7 | 4 | 3 | 11 | 1 |
| phoenician | 15 | 8 | 4 | 3 | 11 | 3 |
| **增量合计** | **+90** | **+45** | **+27** | **+18** | **+90** | **+19** |

**坐标：** 有教科文 WHC 公布点则填（查文 330、蒂瓦纳科 567、蒂卡尔/帕伦克、阿克苏姆 15、班清 575、比布鲁斯/推罗/迦太基等）；含糊者留空。

**媒体：** 仅外链落地页（教科文/机构门户）。`local_path` 仍为空。

**文档：** 覆盖图已更新；`civ-*.md` 与包 README 已同步。机器摘要：[`docs/audits/pass-2026-10-12-wave2-densify.json`](audits/pass-2026-10-12-wave2-densify.json)。

**核验：** `export_check` OK（**40** 包；出处闸门绿）。

**备注：** 距埃及/两河 `fact-library` 密度仍远。宁薄勿假。工具：`tools/wave2_shells/densify_wave2.py` + `densify_payloads/*.json`。



### D-2026-10-12-17 — 第三波加厚至 `library-seed-rich`

**决策：** 将 D-2026-10-12-15 所开十一个第三波包自 `library-seed` 加厚至可调用密度（`library-seed-rich`）。配方同第一/二波加厚：约 +10 来源、+5 遗址、+3 时段、+2 对象、+10 主张、+1–3 外链媒体。诚信优先：不编造考古、页码、坐标或媒体图。

**各包加厚后计数（结构化 JSON）：**

| 包 | sources | sites | periods | objects | claims | media |
|------|--------:|------:|--------:|--------:|-------:|------:|
| cahokia | 15 | 7 | 4 | 3 | 11 | 3 |
| ancestral-pueblo | 15 | 7 | 4 | 3 | 11 | 3 |
| great-zimbabwe | 15 | 7 | 4 | 3 | 11 | 2 |
| west-africa-medieval | 15 | 8 | 4 | 3 | 11 | 2 |
| hallstatt-celtic | 15 | 7 | 4 | 3 | 11 | 2 |
| nuragic-sardinia | 15 | 7 | 4 | 3 | 11 | 2 |
| rapa-nui | 15 | 7 | 4 | 3 | 11 | 2 |
| inca | 15 | 7 | 4 | 3 | 11 | 3 |
| moche | 15 | 7 | 4 | 3 | 11 | 1 |
| aztec | 15 | 7 | 4 | 3 | 11 | 2 |
| angkor | 15 | 8 | 4 | 3 | 11 | 3 |
| **增量合计** | **+110** | **+55** | **+33** | **+22** | **+110** | **+25** |

**坐标：** 主要教科文取向遗址填维基百科主坐标（卡霍基亚、查科、梅萨维德、大津巴布韦、杰内、廷巴克图、哈尔施塔特、苏努拉希、拉帕努伊、库斯科、马丘比丘、大神庙、吴哥窟、太阳金字塔等），并写明精度说明——本轮教科文 WHC 被 Cloudflare 拦截。含糊者留空。

**媒体：** 仅外链落地页（教科文 / NPS / INAH / APSARA / 项目门户）。`local_path` 仍为空。拉帕努伊仍伦理优先（不托管摩艾图像）。

**文档：** 覆盖图已更新；`civ-*.md` 与包 README 已同步。机器摘要：[`docs/audits/pass-2026-10-12-wave3-densify.json`](audits/pass-2026-10-12-wave3-densify.json)。

**核验：** `export_check` OK（**40** 包；出处闸门绿）。

**备注：** 距埃及/两河 `fact-library` 密度仍远（该九包仍为密档层）。宁薄勿假。工具：`tools/wave3_shells/densify_wave3.py` + `densify_payloads/*.json`。

### D-2026-10-12-19 — 热门包 Batch A 朝 fact-library 加厚

**决定：** 对用户优先的五包 `teotihuacan`、`classic-maya`、`inca`、`angkor`、`aksum` 做朝 `fact-library` 的加厚；**状态暂不升为 fact-library**（深度未达埃及/两河级）。诚信优先：无伪造页码/发现/配图。

**每包大约增量：** +15 来源 · +8 遗址 · +4 时段 · +4 对象 · +15 主张 · +3 媒体（合计约 +75/+40/+20/+20/+74/+15）。

**报告：** [`docs/audits/pass-2026-10-12-hot-batch-a.md`](audits/pass-2026-10-12-hot-batch-a.md) · [中文](audits/pass-2026-10-12-hot-batch-a.zh.md)

**验证：** `export_check` OK（40 包）。


### D-2026-10-12-20 — 嘻嘻 P 级坐标回传入仓

**决定：** 按嘻嘻 P 级补充表入仓坐标；**禁止写入鱼凫**（日本由布市假命中）；优先 P(UNESCO)；S 仅在包+名称仔细匹配现有 site id 时写入；跳过空坐标/框架/歧义遗址；`precision_note` 记录 grade 与 URL。

**结果：** 新填 27 · P 升级 7 · 鱼凫保持空。报告：[`docs/audits/pass-2026-10-12-xixi-coords.md`](audits/pass-2026-10-12-xixi-coords.md) · [中文](audits/pass-2026-10-12-xixi-coords.zh.md)

**验证：** `export_check` OK。

### D-2026-10-12-21 — 热门包 Batch B 朝 fact-library 加厚

**决定：** 对用户优先的五包 `aztec`、`phoenician`、`anatolia-hittite`、`nubia-kush`、`elam-iran` 做朝 `fact-library` 的加厚（配方同 Batch A / D-2026-10-12-19）；**状态暂不升为 fact-library**（深度未达埃及/两河级）。诚信优先：无伪造页码/发现/配图。

**每包大约增量：** +15 来源 · +8 遗址 · +4 时段 · +4 对象 · +15 主张 · +3 媒体（合计 +75/+40/+20/+20/+75/+15）。

**坐标补填（仅有出处）：** 特拉特洛尔科、特斯科科（S/维基）；莫蒂亚、西顿（S/维基）；科尔玛（S/维基）。框架/指针遗址仍空。

**报告：** [`docs/audits/pass-2026-10-12-hot-batch-b.md`](audits/pass-2026-10-12-hot-batch-b.md) · [中文](audits/pass-2026-10-12-hot-batch-b.zh.md)

**验证：** `export_check` OK（40 包）。

### D-2026-10-12-22 — 热门包 Round-2 Batch A 朝更密档案加厚

**决定：** 对 `teotihuacan`、`classic-maya`、`inca`、`angkor`、`aksum` 做第二轮加厚，逼近埃及/两河 `fact-library` 密度；**状态暂不升为 fact-library**（仍低于埃及）。诚信优先：无伪造页码/发现/配图/坐标。

**每包大约增量：** +18 来源 · +8 遗址 · +2 时段 · +12 对象 · +17 主张 · +3 媒体（落地约 45–50 / 22–24 / 10 / 19 / 42–43 / 8–9）。

**坐标补填（仅有出处）：** 基里瓜（教科文 WHC 149 DMS，P 级）；乌斯马尔（教科文周期报告/名录 791，P 级）。

**报告：** [`docs/audits/pass-2026-10-12-hot-round2-a.md`](audits/pass-2026-10-12-hot-round2-a.md) · [中文](audits/pass-2026-10-12-hot-round2-a.zh.md)

**验证：** 本轮后 `export_check` OK（40 包）。

### D-2026-10-12-23 — 热门包 Round-2 Batch B 朝更密档案加厚

**决定：** 对 `aztec`、`phoenician`、`anatolia-hittite`、`nubia-kush`、`elam-iran` 做第二轮加厚，逼近埃及/两河 `fact-library` 密度；**状态暂不升为 fact-library**（仍低于埃及）。诚信优先：无伪造页码/发现/配图/坐标。

**每包大约增量：** +18 来源 · +8 遗址 · +2 时段 · +12 对象 · +17 主张 · +3 媒体（落地约 48 / 23–25 / 10 / 19 / 43 / 8–9）。

**坐标补填：** 本轮无新填（指针遗址留空；既有 P/S 保留）。

**报告：** [`docs/audits/pass-2026-10-12-hot-round2-b.md`](audits/pass-2026-10-12-hot-round2-b.md) · [中文](audits/pass-2026-10-12-hot-round2-b.zh.md)

**验证：** 本轮后 `export_check` OK（40 包）。

### D-2026-10-12-24 — 种子包 Batch C 朝更密档案加厚

**决定：** 对第一波剩余五包 `levant-ugarit`、`bmac-oxus`、`zapotec`、`jomon-yayoi`、`dong-son` 从约 15 来源壳加厚至热门加厚带（约 30 来源）；**状态不升为 fact-library**（保持 `library-seed-rich`）。诚信优先：无伪造页码/发现/配图/坐标。

**每包大约增量：** +15 来源 · +8 遗址 · +4 时段 · +4 对象 · +15 主张 · +2–3 媒体。

**坐标补填（仅有出处）：** 新绳文教科文 1632 组件伊势堂岱、御所野、二森、大森胜山按 WHC 地图 DMS→小数写入（P 级）。

**报告：** [`docs/audits/pass-2026-10-12-seed-batch-c.md`](audits/pass-2026-10-12-seed-batch-c.md) · [中文](audits/pass-2026-10-12-seed-batch-c.zh.md)

**验证：** 本轮后 `export_check` OK（40 包）。

### D-2026-10-12-25 — 种子包 Batch D 朝更密档案加厚

**决定：** 对 `nok-west-africa`、`lapita-pacific`、`chavin-andes`、`tiwanaku`、`mitanni` 从约 15 来源壳加厚至热门加厚带（约 30 来源）；**保持 `library-seed-rich`**（不升 fact-library）。诚信优先：无伪造页码/发现/配图/坐标。

**每包大约增量：** +15 来源 · +8 遗址 · +4 时段 · +4 对象 · +15 主张 · +2–3 媒体。

**坐标补填：** 本轮无新填（指针遗址留空；查文/蒂瓦纳科既有教科文坐标保留）。

**报告：** [`docs/audits/pass-2026-10-12-seed-batch-d.md`](audits/pass-2026-10-12-seed-batch-d.md) · [中文](audits/pass-2026-10-12-seed-batch-d.zh.md)

**验证：** 本轮后 `export_check` OK（40 包）。

### D-2026-10-12-26 — 种子包 Batch E 朝更密档案加厚

**决定：** 对 `wari`、`ban-chiang`、`early-korea`、`moche`、`cahokia` 从约 15 来源壳加厚至热门加厚带（约 30 来源）；**保持 `library-seed-rich`**（不升 fact-library）。诚信优先：无伪造页码/发现/配图/坐标。主张 ID 使用 `-seed-e` 后缀以避免与种子 ID 碰撞（Batch D 教训）。

**每包大约增量：** +15 来源 · +8 遗址 · +4 时段 · +4 对象 · +15 主张 · +3 媒体。

**坐标补填：** 本轮无新填（指针遗址留空；班清/卡霍基亚既有教科文坐标保留）。

**报告：** [`docs/audits/pass-2026-10-12-seed-batch-e.md`](audits/pass-2026-10-12-seed-batch-e.md) · [中文](audits/pass-2026-10-12-seed-batch-e.zh.md)

**验证：** 本轮后 `export_check` OK（40 包）。

### D-2026-10-12-27 — 种子包 Batch F 朝更密档案加厚（最后一批薄壳）

**决定：** 对 `ancestral-pueblo`、`great-zimbabwe`、`west-africa-medieval`、`hallstatt-celtic`、`nuragic-sardinia`、`rapa-nui` 从约 15 来源壳加厚至热门加厚带（约 30 来源）；**保持 `library-seed-rich`**。主张 ID 使用 `-seed-f` 后缀。**拉帕努伊伦理优先：** 仅教科文外链媒体；不托管摩艾影像；运输/生态主张保持开放假说。

**每包大约增量：** +15 来源 · +8 遗址 · +4 时段 · +4 对象 · +15 主张 · +3 媒体。

**坐标补填：** 本轮无新填（指针遗址留空；既有教科文/维基坐标保留）。

**里程碑：** 全部 **21** 个原约 15 来源种子包（Batch C–F）现均约 30 来源 / 15 遗址 / 26 主张。非热门薄壳已清空。

**报告：** [`docs/audits/pass-2026-10-12-seed-batch-f.md`](audits/pass-2026-10-12-seed-batch-f.md) · [中文](audits/pass-2026-10-12-seed-batch-f.zh.md)

**验证：** 本轮后 `export_check` OK（40 包）。

### D-2026-10-12-28 — 热门包 Round-3 Batch A 朝更密档案加厚

**决定：** 对热门包 `teotihuacan`、`classic-maya`、`inca`、`angkor`、`aksum` 从约 48 来源 Round-2 带朝埃及/两河邻近深度加厚；**保持 `library-seed-rich`**（本轮不升 fact-library）。主张 ID 使用 `-r3a` 后缀。

**每包大约增量：** +18 来源 · +9 遗址 · +2 时段 · +14 对象 · +18 主张 · +2 媒体。

**落地带：** 约 66 来源 / 31–33 遗址 / 12 时段 / 33 对象 / 60–61 主张 / 10–11 媒体（埃及参照在遗址/对象/主张上仍更高）。

**坐标补填：** 本轮无新填。

**报告：** [`docs/audits/pass-2026-10-12-hot-round3-a.md`](audits/pass-2026-10-12-hot-round3-a.md) · [中文](audits/pass-2026-10-12-hot-round3-a.zh.md)

**验证：** 本轮后 `export_check` OK（40 包）。

