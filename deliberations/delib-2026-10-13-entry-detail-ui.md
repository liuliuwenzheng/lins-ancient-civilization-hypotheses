---
id: delib-2026-10-13-entry-detail-ui
title: "Deliberation: Entry detail UI — markdown report columns as primary surface"
status: synthesized
created: 2026-10-13
updated: 2026-10-13
targets:
  civilizations:
    - civ-ancient-egypt
    - civ-mesopotamia
  hypotheses: []
  reconstructions: []
  sources: []   # project-meta intake — see Intake
seats:
  - deming-perspective
  - steve-jobs-perspective
  - elon-musk-perspective
  - darwin-perspective
  - descartes-perspective
  - qianxuesen-perspective
  - mozi-perspective
facilitator: "cloud-orchestrator"
question: "Should /ui prioritize parsed markdown report columns as the primary civilization surface? How to present 考察办法/发现脉络 without inventing? Demote claim list? Site drill-down? API: sections endpoint vs markdown blob?"
perspective: true
person_endorsement: false
lens_catalog: "https://github.com/liuliuwenzheng/FHLS-perspectives"
related_docs:
  - docs/entry-detail-ui.md
  - docs/entry-detail-ui.zh.md
  - docs/entry-depth.md
  - docs/design-taste.md
  - docs/council.md
  - docs/api.md
---

# Deliberation: Entry detail UI — markdown report columns as primary surface

> **Perspective lenses only.** AI-generated thinking aids from [FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives).  
> `perspective: true` · `person_endorsement: false` — named persons do **not** endorse this project or this session.

## Intake

- **Question (owner 老大林 / 林):** UI at `/ui` only shows names + short summaries / claim one-liners. He wants real detailed entry content: analysis, report columns, excavation/investigation methods, discovery research lineage. Design it, run council, then implement.

- **Target examples:** `civ-ancient-egypt`, `civ-mesopotamia` (thick `fact-library` markdown with Research history + P-level site reports already registered).

- **Cited materials (PROJECT META — not archaeological invention):**
  - `docs/entry-depth.md` / `.zh.md` — required report columns
  - `docs/design-taste.md` — restraint; unlock archive depth, not chrome
  - `api/loader.py` + `api/static/ui.html` — markdown_path unused by API/UI; tabs = claims/sites/periods
  - `data/civilizations/civ-ancient-egypt.md`, `civ-mesopotamia.md` — existing bilingual `##` sections
  - `data/structured/*/civilization.json` → `markdown_path`

- **Observed gap:** Structured claims/sites are real archive atoms, but the **human-depth** product promise lives in markdown columns that never reach the screen.

- **Out of scope:** Inventing excavation methods; forging coordinates/images; rewriting fact-library prose in this session; promoting hyp → fact.

## Parallel lens notes

### deming-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: deming-perspective`
- **Process:** The special cause of “UI looks empty” is a **missing handoff** from `markdown_path` → API → UI, not missing archaeology. Fix the process: parse sections once, serve stably, omit empties.
- **Quality metric:** For fact-library civs, `/report` section count ≥ entry-depth core columns present in file; Research history visible when heading exists.
- **Variation:** Seed packs have thinner/different headings — system must tolerate missing columns without padding (common-cause honesty).

### steve-jobs-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: steve-jobs-perspective`
- **One breath:** Open a civilization → **read the report**. Claims are the index cards in the drawer, not the cover.
- Cut: defaulting to claim one-liners. That taught the wrong story (“we only have slogans”).
- Say no to decorative chrome, fake parchment, and invented “methods essays.” Typography + real columns is enough.

### elon-musk-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: elon-musk-perspective`
- **First principles:** Bytes already on disk (`civ-*.md`). Shortest path: parse `##` → JSON sections → render. Do not rebuild encyclopedia text in the model.
- API: **sections endpoint** beats dumping a raw blob into the civ GET (keeps list/detail light; UI can lazy-load). Raw blob alone forces every client to re-parse.
- Demote claims to secondary; keep them machine-sharp for filters.

### darwin-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: darwin-perspective`
- **Selection:** Competing UI fitness: (A) claim-first index, (B) report-first archive reader, (C) generate new summaries at runtime. Owner need + entry-depth select **B**. A survives as secondary tab; C is unfit (hallucination risk).
- Lineage presentation that **only cites registered `src-*`** survives scrutiny; invented method narratives get selected against.

### descartes-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: descartes-perspective`
- **Doubt first:** Doubt any UI copy that implies fieldwork happened if it is not in Research history or a registered P source. Doubt coordinates unless present on the site record.
- Method: show Research history verbatim; separately list registered P-tier sources labeled **已登记来源脉络** — never merge into a fake continuous narrative.
- Clear and distinct: fact report columns ≠ hypothesis claims tab.

### qianxuesen-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: qianxuesen-perspective`
- **System:** Layers — Markdown (editorial depth) → structured packs (atoms) → API → UI. Feedback: empty section omitted; missing file → `available: false`.
- Open loop to avoid: UI inventing filler when markdown thin. Closed loop: parse → serve → display or omit.
- Site drill-down feeds back into claims/sources already in the pack (graph view light: linked claims only).

### mozi-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: mozi-perspective`
- **Utility:** Does this help readers? Yes — report columns + research history + registered source lineage. Claim lists alone fail the usefulness test the owner stated.
- Consequence if wrong: shipping invented methods would harm trust worse than a thin tab. Prefer omission.
- Standards: bilingual default zh; honest empty; gate (`export_check`) unchanged.

## Cross-examination

| Challenge | From seat | Toward | Notes |
|-----------|-----------|--------|-------|
| Claim atoms are the “real” archive — why elevate prose? | elon-musk / deming | steve-jobs report-first | Both needed: prose = human depth already curated; claims = filterable atoms. Primary **presentation** = report; archive atoms stay API-first. |
| Parsed zh/en split may mis-fire | descartes | elon parser | Keep `body_md` always; zh/en best-effort only; UI falls back to full md. |
| P-tier list ≠ excavation method | darwin / descartes | lineage strip | Label explicitly 已登记来源脉络; Research history carries narrative; no new prose. |
| Thin seed packs will look empty | deming | mozi | Omit empty; do not pad; status pill already signals library-seed vs fact-library. |

## Facilitator synthesis

Neutral merge for implementers:

1. **Primary UI tab** = 档案报告 / Report, fed by parsed markdown sections.
2. **API** = `GET /api/v1/civilizations/{id}/report` returning structured `sections[]` (`id`, titles, `body_md`, optional `body_zh`/`body_en`). Do not invent sections. Civ GET may expose `markdown_path` / `report_available` only.
3. **Lineage** = Research history section + optional registered P-source strip with honest label — never generated fieldwork essays.
4. **Claims demoted** to secondary tab; sites gain summary/coords/sources/linked claims when present.
5. **Taste** = restrain; unlock existing depth.
6. Record as **D-2026-10-13-09**; implement in same change set.

---

## Outputs

### FACT_NOTES

- Egypt/Mesopotamia markdown already contain entry-depth columns including Research history; surfacing them is presentation, not a new fact claim.
- Site coordinates only when already on site JSON (e.g. verified Pleiades notes) — do not add new coords in this UI work.
- Any lineage list must use existing `src-*` registrations only.

### HYPOTHESIS_CHALLENGES

- None raised against archaeological hypotheses in this meta session. UI must keep hypothesis claims visually labeled and out of report columns.

### OPEN_QUESTIONS

- Should Objects/Media become v1.1 tabs when nonempty?
- Longer-term: store pre-parsed sections in pack JSON at export time vs parse-at-read (v1 = parse-at-read is enough)?

### FUTURE_WINDOW

- Testable next steps: curl `/report` for egypt + mesopotamia (expect nonempty sections + research-history); open `/ui` default tab = report; `export_check` green; thin seed civ shows fewer sections without filler.
- Later: optional client-side section TOC; linkify `src-*` to source expand panels.
