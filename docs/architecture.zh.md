# 架构说明

[English](architecture.md) | 中文

> 正直优先：事实 ≠ 假说；每条主张必有出处；留下可复用的审慎轨迹——不是教条。

## 使命语气（简短）

| 原则 | 在本仓库中的含义 |
|------|------------------|
| **正直** | 事实栏永不写臆测；假说始终标注；不编造故事、不上伪造文物图。 |
| **开放复用** | 今天：任何人可读 git 中的 Markdown。明天：同一批实体经只读 API 提供。 |
| **谦逊** | 假说是工作想法；更好来源的纠正优先。我们留下轨迹，不立教义。 |

## 分层

数据单向经过资料库诸阶段。后层可**链接**前层，但不得悄悄改写事实字段。**审议圆桌**位于假说与还原旁侧，作固化前的审核层——只审不抬，绝不把假说悄悄升为事实。

```
sources/                  (1) 来源登记 — 分级 P/S/T/U
    ↓ 被引用
data/civilizations/       (2) 事实库 — 仅有出处的摘要
    ↓ 被关联
hypotheses/               (3) 假说板 — 始终标注 HYPOTHESIS
    ↓ 被审核            ──── deliberations/  (3b) 审议圆桌
    ↓ 组合进                  （多透镜审核；面向未来窗口）
reconstructions/          (4) 还原稿 — 事实 + 假说 + 不确定性
```

| 层 | 目录 | 职责 | 状态取值 |
|----|------|------|----------|
| 来源 | `sources/` | 书目登记 + 可信度档 | 档：`P` \| `S` \| `T` \| `U` |
| 事实库 | `data/civilizations/` | 有年代、有出处的文明条目 | `fact-library` |
| 假说板 | `hypotheses/` | 已标注的关联 / 模式 | `open` \| `challenged` \| `retired` |
| 审议圆桌 | `deliberations/` | 多透镜审核会话（席位来自 FHLS-perspectives） | `open` \| `synthesized` \| `archived` |
| 还原 | `reconstructions/` | 带显式不确定性的因果说明 | `draft` \| `review` \| `archived` |

方法细节见 [`methodology.md`](methodology.md)。来源档次见 [`source-grading.md`](source-grading.md)。圆桌设计：[`council.zh.md`](council.zh.md) · [English](council.md)。视角目录（仅引用）：[FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives)。

## 实体模型

ID 为稳定字符串。前缀让链接与 API 响应中的类型一目了然。

| 实体 | ID 模式 | Front-matter（来自模板） | 正文 |
|------|---------|--------------------------|------|
| **来源 Source** | `src-YYYY-short-slug` | `id`, `type`, `citation`, `url`, `access_date`, `reliability_tier`, `notes` | 引用表 + 备注 |
| **文明 Civilization** | `civ-YYYY-slug` | `id`, `names`（zh/en/native）, `region`, `time_span`, `status`, `summary`, `sources[]`, `related_ids[]`, `notes` | 摘要、来源、相关文明 |
| **假说 Hypothesis** | `hyp-YYYY-short-slug` | `id`, `title`, `status`, `claims[]`, `supporting_sources[]`, `conflicting_sources[]`, `related_civilizations[]`, `caveats` | **HYPOTHESIS** 页眉 + 分节 |
| **还原 Reconstruction** | `rec-YYYY-short-slug` | `id`, `title`, `linked_facts[]`, `linked_hypotheses[]`, `status`, `uncertainty_summary` | 链接 ID、叙述、不确定性 |
| **审议 Deliberation** | `delib-YYYY-short-slug` | `id`, `title`, `status`, `targets`, `seats[]`（FHLS slug）, `question`, `perspective`, `person_endorsement` | 接入、透镜笔记、四栏输出 |

### 关系（`related_ids` 及其同类字段）

```
Source.src-*  ←被引用←  Civilization.sources[]
Source.src-*  ←被引用←  Hypothesis.supporting_sources[] / conflicting_sources[]
Civilization.civ-*  ←→  Civilization.related_ids[]          （仅事实性的地理/年代关联）
Civilization.civ-*  ←被关联←  Hypothesis.related_civilizations[]
Civilization.civ-*  ←被关联←  Reconstruction.linked_facts[]
Hypothesis.hyp-*    ←被关联←  Reconstruction.linked_hypotheses[]
Deliberation.delib-*  →targets→  civ-* / hyp-* / rec-* / src-*
Deliberation.seats[]  →引用→  FHLS-perspectives 文件夹 slug（外部）
```

规则：

- 跨链接一律用**登记 ID**，不用裸 URL。
- 文明的 `related_ids` 只写地理/年代等**事实**关系。投机的「也许因为…有关」进假说。
- 还原稿若主张某条因果猜测，**必须**为该猜测引用至少一个 `hyp-*`。

## 不变量（失败即关闭 / fail-closed）

这些不是文风建议，而是闸门（精神同诗文树的授权闸门，此处改成**出处**）：

1. **事实 ≠ 臆测。** `data/civilizations/` 字段不写「也许 / 失落文明」类主张；那些进 `hypotheses/` 或还原稿中明确标注的部分。
2. **假说标注。** 每个假说文件页眉，以及任何 API 表示，必须带显式 HYPOTHESIS / `kind: "hypothesis"` 与免责字段。
3. **来源分级。** 每条 `sources/` 条目有 `reliability_tier` ∈ {P, S, T, U}。事实库主张优先 P/S；U 必须标明，不得单独当决定性证据。
4. **必须有出处。** 无已登记来源 → 不以事实形态对外暴露该主张（Markdown 与未来 API 皆然）。失败即关闭。
5. **无私密商务数据。** 客户名、成本、合同 —— 永不进仓。
6. **无伪造影像。** 不上伪造文物图；不整篇倒受版权文本 —— 链接并引用。
7. **视角 ≠ 背书。** 圆桌席位是 FHLS-perspectives 的 AI 透镜（`perspective: true`，`person_endorsement: false`）。不能单独改写事实字段，也不得装成真人背书。


## 档案层（产品澄清 — 2026-10-11）

**产品核心 = 数字档案 + 只读 API**，不是博客/百科简介本身。

| 层 | 职责 |
|----|------|
| **编辑 / 呈现** | git 中的双语文明 Markdown、README、人类可读叙述 |
| **面向 API 的档案真源形态** | 结构化记录：**来源 Source**、**遗址 Site**、**分期 Period**、**组合/器物 Assemblage/Object**（含权利）、**主张 Claim**（事实 vs 假说）、**媒体 Media**（仅权利清晰）、**审议 Deliberation**，以及作为聚合视图的文明 Civilization |

规则：

1. 加厚百科式 Markdown 可作为**呈现层**与编辑工艺——但**不足以**单独充当「档案接口」产品形态。
2. `civ-*` 加厚须**喂入**结构化记录（遗址、分期、主张、来源），不能只堆散文。
3. 已发布轨迹仍以 git 为准；经出处闸门的派生 **JSON / SQLite**（如 `export/`，路径待定）作为 API 服务形态——禁止静默双写。
4. API 对档案实体做 list/filter/get；每条带 `sources[]`；假说绝不自动升格为事实。
5. 不上伪造文物图；Media 须权利清晰（v0 可用元数据 + 外链）。

决定：[`decisions.zh.md` D-2026-10-11-17](decisions.zh.md)。审议轨迹：[`../deliberations/delib-2026-10-11-archive-api-direction.md`](../deliberations/delib-2026-10-11-archive-api-direction.md)。

## 今日存储

**Markdown + git 仍是已发布的编辑真源。** 结构化档案记录 + 经闸门的 `export/` 在实现后作为 API 服务形态（见上方档案层）。

- 人通过 PR，按 `_template.md` 复制填写。
- Front matter 为 YAML；正文为可读 Markdown。
- 各目录下的模板只是脚手架——**不会**预填虚构案例。

## 日后存储（档案导出路径）

档案+API 产品所必需（检索、筛选、托管）：

1. 构建步骤把 Markdown 解析为规范化 **SQLite** 和/或 **JSON**（例如 `export/`，路径待定）。
2. **出处闸门（fail-closed）：** 自称事实却缺少可解析 `sources[]` / 登记文件的条目，**拒绝进入导出**（最好同时让 CI 失败）。同诗文树思路：构建期闸门 + 服务期审计，避免 API 成为绕过规则的后门。
3. git 中的 Markdown 仍权威；DB/JSON 是派生物，不得成为唯一真源。
4. 事实库现已有有出处种子（截至 2026-10-11 九条 `fact-library`）——进入 schema + 试点导出；出处闸门仍失败即关闭。

## 目录地图（对齐现有，不另起炉灶）

```
lins-ancient-civilization-hypotheses/
├── README.md / README.zh.md
├── LICENSE
├── docs/
│   ├── methodology.md
│   ├── source-grading.md
│   ├── contributing.md
│   ├── architecture.md / architecture.zh.md   ← 本文
│   ├── council.md / council.zh.md             ← 审议圆桌
│   ├── api.md / api.zh.md                     ← 开放接口设计
│   └── openapi.v0.yaml                        ← OpenAPI 草稿
├── data/civilizations/     # 事实库（含 _template.md）
├── sources/                # 来源登记（含 _template.md）
├── hypotheses/             # 假说板（含 _template.md）
├── deliberations/          # 圆桌会话（含 _template.md）
└── reconstructions/        # 还原稿（含 _template.md）
```

不要平行发明新的顶层目录树。有真实需要时再扩展（例如生成库用的 `export/`）。

## 开放接口（预览）

现阶段仅设计：资料库资源为 `/api/v1/…` 下的**只读** REST（正交筛选、出处引用、假说始终标注）。审议会话另加**会话作用域**的云端端点（优先流式），且不得把假说悄悄升为事实。完整设计：[`api.zh.md`](api.zh.md) · 圆桌：[`council.zh.md`](council.zh.md) · OpenAPI 草稿：[`openapi.v0.yaml`](openapi.v0.yaml)。
