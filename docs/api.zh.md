# 开放接口设计（v0）

[English](api.md) | 中文

> 留下可复用的审慎轨迹。资料库只读优先。出处失败即关闭。假说始终标注。审议会话云端优先，且永不把假说升为事实。

OpenAPI 草稿：[`openapi.v0.yaml`](openapi.v0.yaml) · 架构：[`architecture.zh.md`](architecture.zh.md)

**状态：** 仅设计。本文档不要求同时上线服务。一旦实现，行为须符合下列原则。

---

## 1. 先讲原则，再讲接口

### 1.1 出处失败即关闭（citation fail-closed）

**没有已登记来源 → 不以事实形态对外暴露该主张。**

借鉴诗文树的授权闸门，改用于**出处**：

1. **构建 / 导出期：** 从 Markdown 生成 SQLite/JSON 时，若文明（事实）记录的 `sources[]` 为空或指向缺失的 `src-*` 文件，一律拒绝入库。
2. **服务期（有 API 之后）：** 启动审计——任何要对外提供的「事实」项若未通过出处检查，**拒绝启动**（或剔除该项并告警）。接口绝不能成为绕过 Markdown 规矩的后门。

假说与还原可以证据更薄，但**必须**保持标注与免责；绝不以 `kind: "fact"` 返回。

### 1.2 正交的筛选轴

**不要**把地区 + 时代 + 认识角色压成一个假标签（「唐诗」式陷阱）。

| 轴 | 回答的问题 | 例值 |
|----|------------|------|
| `region` | **何处** | `West Asia`、`East Asia`、`Mesoamerica`…（人可读；精确词表随种子条目敲定） |
| `time_span` / 时间筛选 | **何时** | `time_from`、`time_to`（日后规范化 BCE/CE）；v0 可对 `time_span` 文本做尽力匹配 |
| `kind` | **认识角色** | `fact` \| `hypothesis` \| `reconstruction` \| `source` |
| `source_tier` | **所引来源强度** | `P` \| `S` \| `T` \| `U` |
| `status` | **生命周期** | 文明：`draft`\|`fact-library`；假说：`open`\|`challenged`\|`retired`；还原：`draft`\|`review`\|`archived` |

调用方可自由组合，例如「东亚 × 事实」「与某 civ 相关的开放假说」「tier=P 的来源」。

### 1.3 每条记录都带 `sources` 块

下游不必翻 README 才知道主张从哪来。列表/详情响应包含来源引用（id + 档次 + 短书目，若有）。假说另暴露支持与冲突列表。

### 1.4 资料库只读；写入走 git/PR（审议会话除外）

**资料库**端点（文明、来源、假说、还原、检索、元数据）**仅 GET**。资料库记录的创建与修改通过针对 Markdown 模板的 PR 完成——出处闸门留在人工审阅 + CI。

**例外：** 审议圆桌会话可使用会话作用域的 POST（创建会话、追加消息）。这些写入**不得**改写事实库记录，也不得悄悄把假说升为事实。要把审议写入 `deliberations/*.md` 成为 git 轨迹，仍须导出/PR。

### 1.5 诚实的分页与错误

- **游标分页**（`limit` + `after` / `next_cursor`），不用脆弱的深 `offset`。
- 区分 **未知筛选值**（客户端错误）与 **筛选项合法但交集为空**（200 + 空 `items`）。
- 任何响应中的假说都必须带 `kind: "hypothesis"` 与 `disclaimer` 字符串。

### 1.6 正直的语气

本接口存在的意义，是让他人能审慎复用事实库与假说板——为生命与求知留下轨迹，而不是输出教条。

---

## 2. 基址与版本

建议基址（主机待定——见项目讨论中的拍板项）：

```
https://{host}/api/v1
```

下列资源均相对 `/api/v1`。

---

## 3. 通用响应形状

### 3.1 列表信封

```json
{
  "items": [ /* Entity */ ],
  "total": 0,
  "count": 0,
  "next_cursor": null,
  "has_more": false
}
```

把 `next_cursor` 原样作为下一页的 `after` 传回。

### 3.2 实体骨架

每条至少包含：

| 字段 | 说明 |
|------|------|
| `id` | 登记 id（`civ-…`、`src-…`、`hyp-…`、`rec-…`） |
| `kind` | `fact` \| `source` \| `hypothesis` \| `reconstruction` |
| `status` | 各实体生命周期 |
| `sources` | 来源引用对象数组（非事实类在文档约定下可为空） |
| `links` | 相关登记 id |

**假说必填附加字段：**

```json
{
  "kind": "hypothesis",
  "disclaimer": "This record is a HYPOTHESIS, not an established historical or archaeological conclusion."
}
```

**来源引用对象：**

```json
{
  "id": "src-2020-example",
  "reliability_tier": "S",
  "citation": "Author (Year). Title…",
  "url": "https://doi.org/…"
}
```

### 3.3 错误信封

```json
{
  "error": {
    "code": "unknown_filter_value",
    "message": "Unknown region: Atlantis",
    "details": { "param": "region", "value": "Atlantis" }
  }
}
```

| 代码 | HTTP | 时机 |
|------|------|------|
| `unknown_filter_value` | 400 | 筛选值不在词表 |
| `invalid_cursor` | 400 | `after` 非法 |
| `not_found` | 404 | 未知 id |
| `citation_gate_failed` | 503 | 服务期审计失败（运维） |
| `internal_error` | 500 | 未预期错误 |

**合法**组合下的空结果 → **200** 且 `items: []`，不是 404。

---

## 4. 端点（REST，只读）

| 方法 | 路径 | 用途 |
|------|------|------|
| GET | `/` | 服务信息：原则、能力、端点索引 |
| GET | `/healthz` | 存活检查；可选出处审计摘要 |
| GET | `/meta/regions` | 地区轴词表 |
| GET | `/meta/source-tiers` | P/S/T/U |
| GET | `/meta/stats` | 按 kind / region / tier / status 计数 |
| GET | `/civilizations` | 事实库列表（筛选 + 游标） |
| GET | `/civilizations/{id}` | 单条文明 |
| GET | `/sources` | 来源登记列表 |
| GET | `/sources/{id}` | 单条来源 |
| GET | `/hypotheses` | 假说板列表 |
| GET | `/hypotheses/{id}` | 单条假说（始终标注） |
| GET | `/reconstructions` | 还原列表 |
| GET | `/reconstructions/{id}` | 单条还原 |
| GET | `/search` | 跨类型检索（`q` + 可选 `kind`、各轴） |

### 4.1 共用查询参数

| 参数 | 默认 | 说明 |
|------|------|------|
| `limit` | `20` | 建议上限 100 |
| `after` | — | 上一页 `next_cursor` |
| `region` | — | 正交「何处」轴 |
| `time_from` / `time_to` | — | 粗粒度时间界（v0 可对 `time_span` 文本尽力匹配） |
| `status` | — | 生命周期筛选 |
| `source_tier` | — | 筛选至少引用该档来源的条目（各端点语义另述） |
| `q` | — | 标题/摘要子串；日后可换 FTS |

### 4.2 `/civilizations`

附加筛选：可有 `related_to={civ-id}`。

响应项：`kind: "fact"`。通过出处闸门后 **必须** 带非空 `sources`；未过闸的草稿只留在 git。

### 4.3 `/hypotheses`

始终 `kind: "hypothesis"` + `disclaimer`。筛选：`status`、`related_civilization={civ-id}`、对支持来源的 `source_tier`。

### 4.4 `/reconstructions`

项含 `linked_facts`、`linked_hypotheses`、`uncertainty_summary`。推测性叙述永不提升为 `kind: "fact"`。

### 4.5 `/search`

```
GET /search?q=...&kind=fact&region=...&limit=20
```

有 FTS 时可带 `snippet` 与 `score`；否则如实走子串并标注 `engine: "like-fallback"`（同诗文树：路径降级时绝不假装「零结果」骗人）。

---

## 5. 鉴权

- 资料库全部 GET：**公开读**。
- **资料库写：** 不在 v0 范围内。用 git/PR + 模板。
- **审议写：** 会话作用域 POST 上线后可要求 API key / 限流；仍不得绕过事实出处闸门。主机待定（见 §9）。

---

## 6. GraphQL（可选，日后）

日后可增加镜像同一实体与正交筛选的 GraphQL，方便灵活客户端。一句话：**不进 v0**；先把 REST 合约落地。

---

## 7. 对接方许可说明

- **本项目代码与文档：** MIT（[`LICENSE`](../LICENSE)）。
- **所引第三方文本、图像与数据：** 仍属上游权利。接口返回标识与书目引用；不得变成整库再发布受版权语料的管道。
- 不得通过本接口提供伪造或错标的文物二进制文件。

---

## 8. 实现草图（非规范）

准备动手实现**资料库** API 时：

1. 解析 `sources/`、`data/civilizations/`、`hypotheses/`、`reconstructions/` 以及已发布的 `deliberations/` 的 YAML front matter。
2. 跑出处闸门 → 写入 `export/` 下的 SQLite 或 JSON。
3. 资料库 GET 只读服务该导出（数据库以只读方式打开）。
4. CI：闸门拒绝则失败；假说文件缺 HYPOTHESIS 标注 / `kind` 映射则失败。

在此之前，**git Markdown 仍是唯一对外资料库接口**——对审慎的人类复用已经足够。

---

## 9. 审议圆桌（云端优先）

设计见 [`council.zh.md`](council.zh.md)。透镜仅引用：[FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives)。

审议算力优先放**云端**（低延迟、席位并行）。凡要**发布**的会话，仍以 `deliberations/` 下的 git Markdown 为真源。

### 9.1 端点

| 方法 | 路径 | 用途 |
|------|------|------|
| POST | `/deliberations` | 创建会话：目标 id、席位 slug、问题 |
| GET | `/deliberations/{id}` | 取会话状态与输出 |
| POST | `/deliberations/{id}/messages` | 对话轮次（用户或主持提示） |
| GET | `/deliberations/{id}/stream` | 可选 SSE：透镜 token / 事件流 |

WebSocket 等价语义：`WS /deliberations/{id}/ws`，双向低延迟。流式不可用时，POST 上的**同步 JSON**为兜底。

### 9.2 创建体（草图）

```json
{
  "targets": {
    "civilizations": ["civ-…"],
    "hypotheses": ["hyp-…"],
    "reconstructions": [],
    "sources": ["src-…"]
  },
  "seats": [
    "deming-perspective",
    "steve-jobs-perspective",
    "elon-musk-perspective",
    "darwin-perspective",
    "descartes-perspective",
    "qianxuesen-perspective",
    "mozi-perspective"
  ],
  "question": "该假说是否相对已引来源过度宣称？",
  "stream": true
}
```

席位 slug 须存在于 FHLS-perspectives（或已声明的白名单）。未知 slug → `400 unknown_seat_slug`。

### 9.3 透镜消息标注（强制）

每一条透镜生成的消息/笔记**必须**包含：

```json
{
  "role": "lens",
  "lens_slug": "deming-perspective",
  "perspective": true,
  "person_endorsement": false,
  "content": "…"
}
```

不得省略。客户端应展示这些字段，以免读者误认为真人背书。

### 9.4 输出形状

状态变为 `synthesized` 时包含：

```json
{
  "outputs": {
    "FACT_NOTES": [],
    "HYPOTHESIS_CHALLENGES": [],
    "OPEN_QUESTIONS": [],
    "FUTURE_WINDOW": []
  }
}
```

`FUTURE_WINDOW` = 前瞻研究问题与可检验下一步——**不是**预言。

### 9.5 禁止升格

审议 API **不得**：

- 因会话副作用 PATCH/PUT 文明事实字段  
- 在无明确人工/PR 路径时改假说 `status`  
- 以 `kind: "fact"` 返回透镜文本  

### 9.6 效率说明

- 云端尽量**并行**跑各席。  
- 用 SSE/WebSocket 流式推送部分透镜笔记，让对话窗口更跟手。  
- 按 slug 缓存 FHLS 技能正文；勿每轮拉整仓目录。  
- 限制创建会话的速率；资料库 GET 保持便宜、可缓存。

**决定（2026-10-11）：** 云端主机路径为 **先规范、后实现（spec-first）**——继续完善本节与 [`openapi.v0.yaml`](openapi.v0.yaml)；**暂不**上线实时审议服务。见 [`decisions.zh.md`](decisions.zh.md)。v0 默认席位已在 [`council.zh.md`](council.zh.md) 确认。
