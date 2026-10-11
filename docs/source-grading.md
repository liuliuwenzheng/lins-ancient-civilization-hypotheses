# Source grading / 来源分级

**Language / 语言:** [English](#english) | [中文](#中文)

---

## English

### Tiers

| Code | Tier | Use for | Caution |
|------|------|---------|---------|
| **P** | Primary | Excavation reports, corpora/inscriptions editions, curated museum catalogs | Still check edition, dating, and find context |
| **S** | Secondary | Peer-reviewed articles, academic handbooks, research monographs | Prefer recent consensus over outdated surveys |
| **T** | Tertiary | Encyclopedias, textbooks, high-quality popular overviews | Good for orientation; not enough alone for strong claims |
| **U** | Uncertain | Incomplete citation, abstract-only, contested authorship/attribution | Flag clearly; do not treat as decisive |

### How to cite

1. Create a file under `sources/` from `_template.md` (or a stable ID naming scheme).
2. Fill: `id`, `type`, `citation` (author/editor, year, title, publisher or journal), `url` (if any), `access_date`, `reliability_tier`, `notes`.
3. In civilization / hypothesis / reconstruction entries, refer to sources by **`sources/<id>`** (or the registry `id`), not by bare URLs alone.
4. For web pages, always record **access_date** (ISO date, e.g. `2026-10-11`).
5. Prefer persistent identifiers (DOI, ISBN, museum object numbers) when available.

### Example citation shapes (templates only — not real case data)

```
Author, A. A. (Year). Title of report. Series/Publisher. DOI or URL.
Editor, E. (Ed.). (Year). Handbook title. Publisher.
Museum Name. Object catalog entry: inventory no. XXX. URL (accessed YYYY-MM-DD).
```

### Conflicts

When sources disagree, register both, note the conflict in `notes` or in the hypothesis `conflicting_sources` field, and do not silently pick a favorite in the fact library.

---

## 中文

### 档次

| 代码 | 档次 | 用途 | 注意 |
|------|------|------|------|
| **P** | 一手 | 发掘报告、铭文/语料整理本、经策展的博物馆图录 | 仍需核对版本、断代与出土语境 |
| **S** | 二手 | 同行评议论文、学术手册、研究专著 | 优先较新共识，慎用过时通论 |
| **T** | 三手 | 百科、教材、高质量普及概述 | 适合入门定向；不足以单独支撑强主张 |
| **U** | 存疑 | 出处不全、仅摘要、作者/归属有争议 | 必须标明；不可当作决定性证据 |

### 如何引用

1. 在 `sources/` 按 `_template.md` 新建来源文件（或沿用稳定 ID 命名）。
2. 填写：`id`、`type`、`citation`（作者/编者、年、题名、出版社或期刊）、`url`（如有）、`access_date`、`reliability_tier`、`notes`。
3. 文明 / 假说 / 还原条目中用 **`sources/<id>`**（或登记 `id`）引用，不要只贴裸 URL。
4. 网页务必写 **access_date**（ISO 日期，如 `2026-10-11`）。
5. 尽量使用持久标识（DOI、ISBN、馆藏号等）。

### 冲突处理

来源互相矛盾时，两侧都登记，在 `notes` 或假说的 `conflicting_sources` 中写明冲突；事实库中不要悄悄只留一方。
