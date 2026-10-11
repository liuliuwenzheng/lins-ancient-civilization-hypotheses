# 事实库条目深度标准

[English](entry-depth.md) | 中文

> 资料要丰富、全面、真实。过薄的条目没有意义。
> 相关：[`_template.md`](../data/civilizations/_template.md) · [`source-grading.md`](source-grading.md) · [`methodology.md`](methodology.md)

---

## 为什么要有深度

若文明条目只剩一段摘要复述，对读者、贡献者与下游接口都帮助有限。事实库的目的是**积累可核验知识**——地理环境、分期、关键遗址、城市与制度、文字与行政、生计与手工业、物质文化、对外接触与研究史——且每条非琐碎主张都挂已登记的 `src-*`。

**正直优先于速度。** 宁可少写几段有出处的内容，也不堆装饰性空话。

## 必填栏目（模板 v1）

复制 [`data/civilizations/_template.md`](../data/civilizations/_template.md)。正文栏目一律为**事实**。假说放入 `hypotheses/`。

1. **Summary（摘要）**
2. **Geography & environment（地理与环境）**
3. **Chronology / periodization（年代与分期）**（优先表格；写明所依据的方案并引用）
4. **Key sites（关键遗址）**
5. **Urbanism, architecture & institutions（城市、建筑与制度）**
6. **Writing, language & administration（文字、语言与行政）**（不适用则整节省略）
7. **Economy, subsistence & craft（经济、生计与手工业）**
8. **Material culture（物质文化）**（要点须有出处）
9. **External contacts（对外接触）**（仅在有出处时写；否则省略该标题）
10. **Research history（研究史）**（简要）
11. **Sources（来源）**
12. **Related civilizations（相关文明）**
13. **Notes（备注）**（学界开放争议——不是本项目假说）

## 大型文明总览的最低要求

将**大型**总览（如两河、埃及、印度河、中国青铜、安第斯）往可持久库条目加厚时：

| 门槛 | 期望 |
|------|------|
| 已登记来源 | 目标约 **8–15+** 条不同的 `src-*`（P/S 为主；T 仅作定向） |
| 分栏引用 | **每一个主要栏目**至少引用一条已登记来源 |
| 拒绝注水 | 不用空泛形容词、虚构氛围或无出处「色彩」凑字数 |
| 语言 | 正文**优先中英双语**（可并行段落） |
| 页码 | 仅在核对过该版后才写页码；否则不写 |
| 图像 | 不上伪造或错标的文物图 |

较小的单遗址条目可用更少来源，但仍须填适用栏目并逐条引用。

## 状态阶梯

| 状态 | 含义 |
|------|------|
| `draft` | 脚手架 / 占位；允许 `sources: []` |
| `library-seed` | 有出处的短概述；结构仍可能偏薄 |
| `library-seed-rich` | 新模板栏目已大体填实；来源数向大型文明最低线靠近 |
| `fact-library` | 栏目切实填满、主张有出处、来源数达到大型文明目标（或单遗址已说明合理例外） |

仅在深度扎实后升为 `fact-library`——勿作装饰性标签。

## Notes 放什么（不是 Hypotheses）

- 学界开放争议（如「第一座城市」排序、绝对年代分歧、书名营销式「最早」表述）
- 本条年代范围的边界
- 早期发掘报告与现代二手综合之间的冲突

**不要**在 Notes 里写跨文明臆测故事。那些放入 `hypotheses/`，并明确标注 **HYPOTHESIS**。

## 拒绝规则

- 拒绝不可核验的「色彩」（情绪描写、虚构场景、匿名「专家说」）
- 拒绝编造页码、假发掘编号或伪造图像
- 拒绝把事实段落与未标注的臆测混写
