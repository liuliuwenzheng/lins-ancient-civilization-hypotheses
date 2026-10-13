# 热门包加厚 Round-4 Batch A — D-2026-10-12-30

[English](pass-2026-10-12-hot-round4-a.md) | 中文

五包以**遗址/对象为重点**朝埃及/爱琴/两河档加厚；再按诚实数值 + 质量门槛评估是否升格 `fact-library`。

机器计数：[`pass-2026-10-12-hot-round4-a.json`](pass-2026-10-12-hot-round4-a.json)。

## 加厚前后

| 包 | 来源 | 遗址 | 时段 | 对象 | 主张 | 媒体 | 坐标已填 |
|----|-----:|-----:|-----:|-----:|-----:|-----:|---------:|
| `teotihuacan` | 66→71 | 31→41 | 12→13 | 33→51 | 61→69 | 11→12 | 1/41 |
| `classic-maya` | 66→71 | 33→43 | 12→13 | 33→51 | 61→69 | 11→12 | 6/43 |
| `inca` | 66→71 | 32→42 | 12→13 | 33→51 | 61→69 | 11→12 | 4/42 |
| `angkor` | 66→71 | 33→43 | 12→13 | 33→51 | 61→69 | 11→12 | 4/43 |
| `aksum` | 66→71 | 32→42 | 12→13 | 33→51 | 60→68 | 10→11 | 3/42 |

**增量合计：** +25 来源 · +50 遗址 · +5 时段 · +90 对象 · +40 主张 · +5 媒体。

**坐标：** 本轮无新填（空值保持空；无伪造坐标）。

## 升格评估

**数值门槛：** 来源 ≥ 65 · 遗址 ≥ 38 · 对象 ≥ 45 · 主张 ≥ 58。

**质量/诚信：** 主要章节有引用；主张达报告级；坐标不能几乎全空且关键遗址无 P/S；orientation 指针比例不能占主导。

| 包 | 升格？ | 状态 | 数值 | 质量 | 坐标 | 指针遗址 | 理由 |
|----|:------:|------|:----:|:----:|-----:|---------:|------|
| `teotihuacan` | N | `library-seed-rich` | PASS | FAIL | 1/41 | 20 | Numeric OK but quality/honesty fail: coords mostly null (1/41 filled, 2%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (20/41, 49%); depth still seed-like vs Egypt report-level sites |
| `classic-maya` | N | `library-seed-rich` | PASS | FAIL | 6/43 | 19 | Numeric OK but quality/honesty fail: coords mostly null (6/43 filled, 14%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (19/43, 44%); depth still seed-like vs Egypt report-level sites |
| `inca` | N | `library-seed-rich` | PASS | FAIL | 4/42 | 21 | Numeric OK but quality/honesty fail: coords mostly null (4/42 filled, 10%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (21/42, 50%); depth still seed-like vs Egypt report-level sites |
| `angkor` | N | `library-seed-rich` | PASS | FAIL | 4/43 | 22 | Numeric OK but quality/honesty fail: coords mostly null (4/43 filled, 9%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (22/43, 51%); depth still seed-like vs Egypt report-level sites |
| `aksum` | N | `library-seed-rich` | PASS | FAIL | 3/42 | 21 | Numeric OK but quality/honesty fail: coords mostly null (3/42 filled, 7%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (21/42, 50%); depth still seed-like vs Egypt report-level sites |

**已升格：** *（无）*.

**仍为 `library-seed-rich`：** `teotihuacan`, `classic-maya`, `inca`, `angkor`, `aksum`.

诚信：无伪造页码/坐标/发现/配图。工具：`tools/hot_densify/densify_hot_round4_a.py`。
