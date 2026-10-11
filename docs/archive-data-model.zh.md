# 档案数据模型（结构化实体）

[English](archive-data-model.md) | 中文

> 产品核心 = **数字档案 + 只读 API**（D-2026-10-11-17）。  
> 文明 Markdown 仍是编辑 / 人读层。  
> `data/structured/` 下的 JSON 是面向 API 的**试点**形态。  
> 出处**失败即关闭**：`kind: fact` 若无已解析的 `src-*`，不得导出。

相关：[架构](architecture.zh.md) · [接口 §4.6](api.zh.md) · [OpenAPI](openapi.v0.yaml) · [Schemas](../schemas/) · [决策](decisions.zh.md)

---

## 1. 为何需要实体（而不只是散文）

双语百科式 Markdown 是有价值的呈现。**档案 API** 需要可寻址的原子：

| 实体 | Id 前缀 | 作用 |
|------|---------|------|
| **Source（来源）** | `src-*` | 书目登记（P/S/T/U） |
| **Site（遗址）** | `site-*` | 考古遗址 / 调查区 / 仅定向地名 |
| **Period（分期）** | `period-*` | 有出处方案的期段（不是伪造的唯一年表） |
| **Object（器物/组合）** | `obj-*` / `asm-*` | 组合或器物类**元数据**——不上伪造二进制图 |
| **Claim（主张）** | `claim-*` | 原子断言：`kind: fact` \| `hypothesis` |
| **Media（媒体）** | `media-*` | 权利元数据；允许外链；禁止未核验上传 |
| **Civilization（文明）** | `civ-*` | 聚合视图，链接遗址 / 分期 / 主张 / 器物 |
| **Deliberation（审议）** | `delib-*` | 可选桩，指向 `deliberations/*.md` |

JSON Schema 草稿见 [`schemas/`](../schemas/)。

---

## 2. 关系（简化）

```
Source  <—— 被引用 ——  Claim / Site / Period / Object / Civilization / Media
Site    <—— 定位 ——   Object, Claim
Period  <—— 断代 ——   Object, Claim
Object  <—— 是否配图？ —— Media（仅外链 / 权利清晰）
Civilization —— 聚合 —— Site[], Period[], Claim[], Object[], Source[]
Deliberation —— 可指向 —— Civilization[]（不改写事实）
```

信任方向：**来源优先**。主张不得凭空造书目。

---

## 3. Claim 上的认识分栏

| `kind` | 导出规则 |
|--------|----------|
| `fact` | **失败即关闭：** `sources[]` 非空；每个 id 须存在 `sources/{id}.md`，且（试点中）存在 `data/structured/.../sources/{id}.json`。 |
| `hypothesis` | 必须有非空 `disclaimer`。来源可选但建议填写。绝不可自动升为 `fact`。 |

MD 中已标明为学术模型的内容（如乌鲁克扩张；「第一座城市」排名）在试点中存为 **hypothesis** 主张。

---

## 4. 媒体正直性

- 优先 `rights.status: outbound-link-only` + `external_url`。
- v0 中 `local_path` **必须为 null**（禁止未核验上传）。
- **不上伪造文物图。** 媒体表为空是诚实且允许的。

---

## 5. 试点布局 — 两河

```
data/structured/mesopotamia/
  civilization.json
  deliberation.json          # 桩 → archive-api-direction 审议
  sources/*.json             # 15 × src-mesopotamia-*
  sites/*.json
  periods/*.json
  objects/*.json             # 组合 / 器物类元数据
  claims/*.json              # fact + hypothesis
  media/*.json               # CDLI 外链目录指针
  README.md | README.zh.md
```

派生规则：字段只来自 `civ-mesopotamia.md` + 已登记 `src-mesopotamia-*`。原文没有的字段省略或 `null` 并加编辑说明。不编造坐标、P 编号、公顷总数或新考古主张。

---

## 6. 出处失败即关闭（导出闸门）

`tools/export_check.py`：

1. 用 `schemas/` 中对应 schema 校验每条 JSON。
2. 对所有 `kind: fact` 的 Claim，要求 `sources[]` 非空且可解析到登记册 + 试点 source JSON。
3. 拒绝带非 null `local_path` 的 Media。
4. 任一失败则非零退出（可进 CI）。

```bash
.venv/bin/python tools/export_check.py
```

在已实现且通过闸门的托管 API 出现之前，git Markdown 仍是已发布编辑权威（D-2026-10-11-4，经 D-2026-10-11-17/18 细化）。经闸门的结构化 JSON 是将来的服务形态——**禁止静默双写**。

---

## 7. OpenAPI 映射

只读路径（设计）：`/sources`、`/sites`、`/periods`、`/objects`、`/claims`、`/media`、`/civilizations`、`/deliberations` — 见 [`openapi.v0.yaml`](openapi.v0.yaml) 与 [接口 §4.6](api.zh.md)。
