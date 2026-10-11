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
