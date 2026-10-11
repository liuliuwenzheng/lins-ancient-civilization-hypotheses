# Contributing / 贡献指南

**Language / 语言:** [English](contributing.md#english) | [中文](contributing.md#中文)

English | [中文](#中文)

---

## English

### Before you start

- Read [`methodology.md`](methodology.md) and [`source-grading.md`](source-grading.md).
- Facts and hypotheses stay in **separate** files/fields.
- No client/cost data, no forged images, no fabricated stories.

### Add a civilization (fact library)

1. Copy `data/civilizations/_template.md` → `data/civilizations/<id>.md`.
2. Fill `id`, names (CN / EN / native), `region`, `time_span`, `status` (fact-library), `summary`, `sources[]`, `related_ids[]`, `notes`.
3. Every non-trivial sentence in `summary` should be backed by at least one registered source.
4. Do **not** invent placeholder “example civilizations” with fake details; leave unused fields empty or `TBD` with a note.

### Add a source

1. Copy `sources/_template.md` → `sources/<id>.md`.
2. Set `reliability_tier` to P / S / T / U honestly.
3. Include `access_date` for URLs.

### Add a hypothesis

1. Copy `hypotheses/_template.md` → `hypotheses/<id>.md`.
2. Keep the **HYPOTHESIS** label in the title/header.
3. Fill `claims[]`, `supporting_sources[]`, `conflicting_sources[]`, `related_civilizations[]`, `caveats`, and `status` (`open` | `challenged` | `retired`).

### Add a reconstruction

1. Copy `reconstructions/_template.md` → `reconstructions/<id>.md`.
2. Link both fact-library IDs and hypothesis IDs.
3. Write causality notes with **explicit uncertainty**; never present a reconstruction as settled truth.

### Pull requests

- One logical change per PR when possible (e.g. one civilization + its new sources).
- Describe what is fact vs what is hypothesis in the PR body.
- Publishing or deleting the GitHub repository itself requires owner approval (not a normal PR).

---

## 中文

### 开始之前

- 先读 [`methodology.md`](methodology.md) 与 [`source-grading.md`](source-grading.md)。
- 事实与假说必须分文件 / 分栏。
- 不上客户/成本数据、不上伪造图、不编造故事。

### 添加文明条目（事实库）

1. 复制 `data/civilizations/_template.md` → `data/civilizations/<id>.md`。
2. 填写 `id`、名称（中/英/本地）、`region`、`time_span`、`status`（事实库）、`summary`、`sources[]`、`related_ids[]`、`notes`。
3. `summary` 中非常识性陈述都应能指向至少一条已登记来源。
4. **不要**虚构「示例文明」细节；暂空字段可留空或写 `TBD` 并说明。

### 添加来源

1. 复制 `sources/_template.md` → `sources/<id>.md`。
2. 如实填写 `reliability_tier`（P / S / T / U）。
3. URL 必须写 `access_date`。

### 添加假说

1. 复制 `hypotheses/_template.md` → `hypotheses/<id>.md`。
2. 标题/页眉保留 **HYPOTHESIS / 假说** 标注。
3. 填写 `claims[]`、`supporting_sources[]`、`conflicting_sources[]`、`related_civilizations[]`、`caveats`、`status`（`open` | `challenged` | `retired`）。

### 添加还原稿

1. 复制 `reconstructions/_template.md` → `reconstructions/<id>.md`。
2. 同时链接事实库 ID 与假说 ID。
3. 因果说明须带**显式不确定性**；不得写成已成定论。

### 提交 PR

- 尽量一事一 PR（例如：一个文明 + 其新来源）。
- 在 PR 说明里分清哪些是事实、哪些是假说。
- **发布或删除** GitHub 仓库本身须所有者批准（不属于普通 PR 流程）。
