# Methodology / 方法说明

**Language / 语言:** [English](#english) | [中文](#中文)

---

## English

### Four stages

1. **Collect** — Register references in `sources/` before (or alongside) using them. Prefer excavation reports, corpora, museum catalogs, and peer-reviewed work.
2. **Build library** — Maintain civilization entries under `data/civilizations/` as a **fact library**: dates, geography, material culture summaries that can be tied to sources. Do **not** put speculative claims in fact fields.
3. **Discover associations (hypothesis board)** — Put cross-links, analogies, and tentative patterns in `hypotheses/`. Every file must be labeled **HYPOTHESIS**. Status may be `open`, `challenged`, or `retired`.
4. **Reconstruct & archive causality** — In `reconstructions/`, combine cited facts with linked hypotheses. State causal claims carefully, list caveats, and mark uncertainty. Retire or revise when better evidence appears.

### Fact vs hypothesis separation

| Column / area | Allowed | Not allowed |
|---------------|---------|-------------|
| Fact library (`data/civilizations/`) | Sourced summaries, consensus descriptions, dated finds | Speculation, “maybe related to…”, unverified diffusion stories |
| Hypothesis board (`hypotheses/`) | Labeled claims, supporting & conflicting sources, caveats | Presenting claims as proven fact |
| Reconstructions | Explicit links to fact IDs + hypothesis IDs; uncertainty notes | Blending fact and guess without labels |

If a sentence cannot be sourced, it does not belong in a fact field. If it is a guess, it belongs on the hypothesis board (or in a clearly marked reconstruction section).

### What we refuse

- Fabricated fantasy narratives framed as research
- Forged or mislabeled artifact images
- Client / cost / private business data
- Entries without sources

---

## 中文

### 四阶段

1. **收集** — 在使用文献前（或同时）于 `sources/` 登记来源。优先发掘报告、语料/铭文、博物馆图录、同行评议成果。
2. **建库** — 在 `data/civilizations/` 维护文明条目，作为**事实库**：年代、地理、可溯源的物质文化摘要。事实字段**禁止**写入臆测。
3. **发现联想（假说板）** — 跨文明关联、类比、待检验模式写入 `hypotheses/`。每份文件必须标注 **HYPOTHESIS / 假说**。状态可为 `open`（开放）、`challenged`（受质疑）、`retired`（已退役）。
4. **还原与归档因果** — 在 `reconstructions/` 中把已引事实与相关假说连起来。谨慎写因果、列出保留意见、标明不确定。有更好证据时修订或退役。

### 事实与假说分栏

| 区域 | 允许 | 禁止 |
|------|------|------|
| 事实库 (`data/civilizations/`) | 有出处的摘要、学界共识描述、有年代的发现 | 臆测、「也许与…有关」、无核验的传播故事 |
| 假说板 (`hypotheses/`) | 标注清楚的主张、支持与冲突来源、保留意见 | 把主张写成已证实事实 |
| 还原稿 | 明确链接事实 ID + 假说 ID；不确定性说明 | 不加标注地混写事实与猜测 |

一句话若找不到来源，就不应进事实栏；若是猜测，应上假说板（或写入还原稿中明确标注的部分）。

### 红线

- 以研究名义编造幻想故事
- 伪造或错标文物图
- 客户 / 成本 / 私密商务数据
- 无出处条目
