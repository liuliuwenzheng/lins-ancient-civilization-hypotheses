# 审议圆桌（Deliberation Council）

[English](council.md) | 中文

> 条目固化前的多视角审核。视角是 AI 生成的思维透镜——**不代表**历史人物或在世名人背书。

相关：[架构](architecture.zh.md) · [接口](api.zh.md) · 会话模板：[`../deliberations/_template.md`](../deliberations/_template.md)

**视角目录（仅引用，不整包拷贝）：** [liuliuwenzheng/FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives) — 按文件夹 slug 选席，勿把整套 perspective 打进本仓。

---

## 1. 目的

**审议圆桌**是对话式、面向未来的审核层。在文明事实、假说或还原稿固化之前（或在可能模糊「事实 / 假说」边界的 PR 合并前），由**主持（Facilitator）**安排若干**视角透镜**席位，用于：

1. 检查出处与「事实 ≠ 假说」分栏  
2. 从多元认识角度压力测试主张  
3. 浮现开放问题与**可检验**的下一步（不是预言）  
4. 在 `deliberations/` 留下可持久的 Markdown 轨迹  

圆桌**只审核**；不发明文明、不伪造影像、不把假说抬升为事实。

---

## 2. 角色

| 角色 | 是谁 | 职责 |
|------|------|------|
| **主持 Facilitator** | 中立流程角色（人工编辑和/或云端编排） | 强制事实/假说分栏；要求出处；禁止假说悄悄升格为事实；汇总为下方四栏输出；不以某历史人物口吻发言。 |
| **席位透镜 Seat lenses** | 选自 FHLS-perspectives 的技能 | 每个席位是按文件夹 slug 标识的 **AI 生成思维透镜**（如 `deming-perspective`）。透镜批评结构、证据、清晰度、系统、功用——**不以**真人背书权威发言。 |

### 正直标签（每一轮透镜输出必带）

| 字段 | 取值 | 含义 |
|------|------|------|
| `perspective` | `true` | 输出为视角透镜，非一手史料 |
| `person_endorsement` | `false` | 具名人物**并未**背书本项目或本场审议 |
| `lens_slug` | 如 `deming-perspective` | 精确对应 FHLS-perspectives 文件夹 slug |

语气对齐 FHLS-perspectives：AI 生成、仅供参考；非传记、非学术定论；勿用于冒充或商业虚假背书。

---

## 3. 默认席位（v0）

以下七席均**已存在于** FHLS-perspectives。可按场次调整；最小审核建议：主持 + 至少三席。

| # | 文件夹 slug（API / front matter 用此名） | 在本项目中的透镜焦点 |
|---|------------------------------------------|----------------------|
| 1 | `deming-perspective` | 证据质量、过程、变异与特殊原因 |
| 2 | `steve-jobs-perspective` | 清晰度、该砍什么、主张能否一句话说清 |
| 3 | `elon-musk-perspective` | 第一性原理；剥掉继承来的假设 |
| 4 | `darwin-perspective` | 证据轨迹、竞争解释的筛选 |
| 5 | `descartes-perspective` | 方法性怀疑；先怀疑什么 |
| 6 | `qianxuesen-perspective` | 系统结构、反馈与开环 |
| 7 | `mozi-perspective` | 功用与后果检验——若判错，这主张带来什么 |

**目录中尚无：** 亚里士多德（如 `aristotle-perspective`）。日后可用女娲（Nuwa）蒸馏进 FHLS-perspectives——**不要**在本仓捏造完整视角文件。

全部可用 slug 见：[FHLS-perspectives CATALOG](https://github.com/liuliuwenzheng/FHLS-perspectives/blob/main/CATALOG.md)。

---

## 4. 讨论流程

```
接入 → 并行透镜笔记 → 交叉诘问 → 主持综合 → 四栏输出
```

| 步 | 名称 | 做什么 |
|----|------|--------|
| 1 | **接入 Intake** | 点名目标 id（`civ-*` / `hyp-*` / `rec-*` / `src-*`），粘贴或链接已引来源，写清问题。无出处主张不得进场。 |
| 2 | **并行透镜笔记** | 各席以自身 slug 写短注；每条笔记带 `perspective: true`、`person_endorsement: false`。 |
| 3 | **交叉诘问** | 就证据缺口、范畴错误（事实 vs 假说）、过度宣称互相挑战。主持禁止人身攻击与「因为那位名人会这么说…」。 |
| 4 | **主持综合** | 汇入四栏输出；标未决项；**不得**仅凭透镜意见改写事实库字段。 |
| 5 | **落盘** | 按模板存入 `deliberations/`。已发布会话以 git 为准；云端 API 会话在导出/PR 前可视为临时态。 |

### 四栏输出

| 栏 | Id | 内容 |
|----|-----|------|
| **事实注记** | `FACT_NOTES` | 加强、纠正或要求更好出处的**事实**侧注记——任何事实修改仍须先有 `src-*` |
| **假说挑战** | `HYPOTHESIS_CHALLENGES` | 对已标注假说的挑战；不自动退休、不自动升格 |
| **开放问题** | `OPEN_QUESTIONS` | 尚未解决的认识问题 |
| **面向未来窗口** | `FUTURE_WINDOW` | 前瞻的**研究问题**与**可检验下一步**（发掘核对清单、比较语料、测年试验等）——**不是**预言或宿命话 |

---

## 5. 持久化

- 目录：`deliberations/`
- 模板：[`deliberations/_template.md`](../deliberations/_template.md)
- Id 模式：`delib-YYYY-short-slug`
- 状态：`open` \| `synthesized` \| `archived`
- 仅通过登记 id 链接目标（`civ-*`、`hyp-*`、`rec-*`、`src-*`）

审议算力可放云端求速度；**凡要作为项目轨迹发布的会话，仍以 git Markdown 为真源。**

---

## 6. 硬规矩（圆桌专用）

1. 事实 ≠ 假说；每条主张必有出处。  
2. 无伪造文物图；客户/成本/私密商务数据不上仓。  
3. 视角是审核工具——绝不以「真人背书权威」口吻呈现。  
4. FHLS-perspectives **仅引用**（仓链接 + slug 列表）；不整包搬进本仓。  
5. 圆桌输出不得悄悄把假说写入事实库。事实变更仍走 PR + 出处闸门。  
6. 模板与示例中不发明文明案例。

---

## 7. 云端接口（预览）

对话式会话优先走**云端**主机以降延迟（SSE 或 WebSocket 流式；同步 JSON 兜底）。草图：[api.zh.md § 审议圆桌](api.zh.md#9-审议圆桌云端优先) · [openapi.v0.yaml](openapi.v0.yaml)。

资料库端点保持**只读**。审议写入为**会话作用域**，不得副作用改写事实记录。
