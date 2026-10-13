# 热门包加厚 Round-4 Batch B — D-2026-10-12-31

[English](pass-2026-10-12-hot-round4-b.md) | 中文

五包以**遗址/对象为重点**朝埃及/爱琴/两河档加厚；再按诚实数值 + 质量门槛评估是否升格 `fact-library`。

机器计数：[`pass-2026-10-12-hot-round4-b.json`](pass-2026-10-12-hot-round4-b.json)。

## 加厚前后

| 包 | 来源 | 遗址 | 时段 | 对象 | 主张 | 媒体 | 坐标已填 |
|----|-----:|-----:|-----:|-----:|-----:|-----:|---------:|
| `aztec` | 66→71 | 32→42 | 12→13 | 33→51 | 61→69 | 10→11 | 3/42 |
| `phoenician` | 66→71 | 33→43 | 12→13 | 33→51 | 61→69 | 11→12 | 5/43 |
| `anatolia-hittite` | 66→71 | 32→42 | 12→13 | 33→51 | 61→69 | 11→12 | 5/42 |
| `nubia-kush` | 66→71 | 34→44 | 12→13 | 33→51 | 61→69 | 11→12 | 8/44 |
| `elam-iran` | 66→71 | 33→43 | 12→13 | 33→51 | 61→69 | 11→12 | 6/43 |

**增量合计：** +25 来源 · +50 遗址 · +5 时段 · +90 对象 · +40 主张 · +5 媒体。

**坐标：** 本轮无新填（空值保持空；无伪造坐标）。

## 升格评估

**数值门槛：** 来源 ≥ 65 · 遗址 ≥ 38 · 对象 ≥ 45 · 主张 ≥ 58。

**质量/诚信：** 主要章节有引用；主张达报告级；坐标不能几乎全空且关键遗址无 P/S；orientation 指针比例不能占主导。

| 包 | 升格？ | 状态 | 数值 | 质量 | 坐标 | 指针遗址 | 理由 |
|----|:------:|------|:----:|:----:|-----:|---------:|------|
| `aztec` | N | `library-seed-rich` | PASS | FAIL | 3/42 | 16 | Numeric OK but quality/honesty fail: coords mostly null (3/42 filled, 7%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites); orientation stubs still high (16/42, 38%); depth still seed-like vs Egypt report-level sites |
| `phoenician` | N | `library-seed-rich` | PASS | FAIL | 5/43 | 13 | Numeric OK but quality/honesty fail: coords mostly null (5/43 filled, 12%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites) |
| `anatolia-hittite` | N | `library-seed-rich` | PASS | FAIL | 5/42 | 11 | Numeric OK but quality/honesty fail: coords mostly null (5/42 filled, 12%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites) |
| `nubia-kush` | N | `library-seed-rich` | PASS | FAIL | 8/44 | 9 | Numeric OK but quality/honesty fail: coords mostly null (8/44 filled, 18%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites) |
| `elam-iran` | N | `library-seed-rich` | PASS | FAIL | 6/43 | 11 | Numeric OK but quality/honesty fail: coords mostly null (6/43 filled, 14%); below honesty floor for fact-library (need ~≥20% or cited P/S on key sites) |

**已升格：** *（无）*.

**仍为 `library-seed-rich`：** `aztec`, `phoenician`, `anatolia-hittite`, `nubia-kush`, `elam-iran`.

诚信：无伪造页码/坐标/发现/配图。工具：`tools/hot_densify/densify_hot_round4_b.py`。
