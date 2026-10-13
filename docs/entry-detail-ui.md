# Entry detail presentation (v1)

[中文](entry-detail-ui.zh.md) | English

> Unlock **existing** archive depth in `/ui`. Prefer surfacing registered markdown report columns over generating new prose. Related: [`entry-depth.md`](entry-depth.md) · [`design-taste.md`](design-taste.md) · [`council.md`](council.md) · decision **D-2026-10-13-09**.

---

## Problem

Opening a civilization in `/ui` previously defaulted to **claim one-liners** plus site/period **name + short summary**. Rich bilingual markdown under `data/civilizations/civ-*.md` (Summary, Geography, Chronology, Key sites, Urbanism…, Writing…, Economy…, Material culture, External contacts, Research history, Sources) was linked via `markdown_path` but **not served** to the browse UI. That made the product look thin even when the fact-library entry was thick.

## Goal

When a reader opens a civilization, the **primary surface** is the **report columns** already written for entry-depth — not a claim list. Claims, sites, and periods remain available as secondary archive tabs.

## Primary view: 分栏报告 / Report columns

| Rule | Detail |
|------|--------|
| Source of truth | `civilization.json` → `markdown_path` → parse `##` sections from that file |
| Section set | Whatever `##` headings exist; map known titles to entry-depth ids; **do not invent** missing columns |
| Empty | Omit empty sections honestly — no padding copy |
| Language | Prefer `zh` body when UI is Chinese and a zh block was parsed; else show full `body_md` (often bilingual paragraphs already). EN UI prefers `body_en` when present |
| Rendering | Light markdown: paragraphs, lists, simple tables as readable blocks; highlight `` `src-*` `` ids. No forged images |
| Research history | Must appear when present in markdown — this is the honest home for discovery lineage |

Known title → id map (non-exhaustive; unknown `##` titles still appear with a slug id):

| id | en | zh |
|----|----|----|
| `summary` | Summary | 摘要 |
| `geography-environment` | Geography & environment | 地理与环境 |
| `chronology-periodization` | Chronology / periodization | 年代与分期 |
| `key-sites` | Key sites | 关键遗址 |
| `urbanism-architecture-institutions` | Urbanism, architecture & institutions | 城市、建筑与制度 |
| `writing-language-administration` | Writing, language & administration | 文字、语言与行政 |
| `economy-subsistence-craft` | Economy, subsistence & craft | 经济、生计与手工业 |
| `material-culture` | Material culture | 物质文化 |
| `external-contacts` | External contacts | 对外接触 |
| `research-history` | Research history | 研究史 |
| `sources` | Sources | 来源 |
| `related-civilizations` | Related civilizations | 相关文明 |
| `notes` | Notes | 备注 |

## 考察办法 / 发现脉络 (methods & lineage)

| Do | Do not |
|----|--------|
| Surface **Research history** section text as written | Invent excavation narratives |
| Label curated lists of **registered** `src-*` (especially tier **P** excavation reports) as **已登记来源脉络 / Registered source lineage** | Claim those lists are a complete fieldwork history |
| On site cards, show expanded sources + linked claims when already in the pack | Fabricate methods notes, coordinates, or page numbers |

Copy for the lineage strip (UI): short notice that the strip is **registered sources only**, not a substitute for reading the reports.

## Secondary tabs

1. **Sites** — name, summary, region, coordinates **only if** present and verified in JSON, expandable sources, linked claims (same civ bundle) that cite the site.
2. **Periods** — name, time_span, summary (omit empty).
3. **Claims** — demoted from default; keep kind badges, source expansion, fact/hypothesis filter.
4. **Objects / Media** — optional later if useful; v1 may omit if empty to avoid chrome.

## API shape (v1)

**Preferred:** dedicated read-only endpoint so list/detail stay light:

```
GET /api/v1/civilizations/{id}/report
```

Response sketch:

```json
{
  "civilization_id": "civ-ancient-egypt",
  "markdown_path": "data/civilizations/civ-ancient-egypt.md",
  "available": true,
  "sections": [
    {
      "id": "geography-environment",
      "title_en": "Geography & environment",
      "title_zh": "地理与环境",
      "body_md": "…",
      "body_zh": "…",
      "body_en": "…"
    }
  ]
}
```

- `available: false` + empty `sections` when `markdown_path` missing or file absent — **no invented body**.
- Best-effort `body_zh` / `body_en` split from bilingual paragraphs; always keep `body_md`.
- Optionally `GET /civilizations/{id}` may expose `markdown_path` / `report_available` only; full sections stay on `/report`.

## UI defaults

- Language: Chinese (`zh`) unless user toggled EN.
- Default tab on open: **档案报告 / Report**.
- Claim-kind filter applies when Claims tab is active (does not hide the report).
- Taste: one accent, typography, honest empty states — see [`design-taste.md`](design-taste.md).

## Non-goals (v1)

- Generating new encyclopedia prose in the API
- Auto-translating missing zh/en halves
- Decorative “museum” imagery
- Promoting hypotheses into report columns

## Verification

- `export_check` still passes (report parse is read-only presentation).
- Curl Egypt + Mesopotamia `/report` → nonempty sections including Research history when present in markdown.
