---
id: delib-2026-10-11-archive-api-direction
title: "Deliberation: Archive + API product direction (not encyclopedia-only)"
status: synthesized
created: 2026-10-11
updated: 2026-10-11
targets:
  civilizations:
    - civ-mesopotamia
    - civ-ancient-egypt
    - civ-indus-valley
    - civ-china-bronze
    - civ-sanxingdui
    - civ-olmec
    - civ-early-maya
    - civ-andes
    - civ-aegean
  hypotheses: []
  reconstructions: []
  sources: []   # project-meta intake only — see Intake (not archaeological P/S)
seats:
  - deming-perspective
  - steve-jobs-perspective
  - elon-musk-perspective
  - darwin-perspective
  - descartes-perspective
  - qianxuesen-perspective
  - mozi-perspective
facilitator: "cloud-orchestrator + human editor trail"
question: "咱们想做的内容是涵盖丰富资料的档案接口一样的项目，不是简简单单的文字介绍哦，先去审议一下 — We want an archive+API project covering rich materials, NOT simple textual introductions. Deliberate first."
perspective: true
person_endorsement: false
lens_catalog: "https://github.com/liuliuwenzheng/FHLS-perspectives"
related_docs:
  - docs/architecture.md
  - docs/api.md
  - docs/openapi.v0.yaml
  - docs/entry-depth.md
  - docs/decisions.md
  - docs/council.md
---

# Deliberation: Archive + API product direction (not encyclopedia-only)

> **Perspective lenses only.** AI-generated thinking aids from [FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives).  
> `perspective: true` · `person_endorsement: false` — named persons do **not** endorse this project or this session.

## Intake

- **Question (owner 林):** 「咱们想做的内容是涵盖丰富资料的档案接口一样的项目，不是简简单单的文字介绍哦，先去审议一下」  
  Translation: We want an **archive + API** project covering rich materials — **not** simple textual introductions. Deliberate first.

- **Target ids (as examples of current shape):** all nine first-batch `civ-*` at `fact-library` depth — `civ-mesopotamia`, `civ-ancient-egypt`, `civ-indus-valley`, `civ-china-bronze`, `civ-sanxingdui`, `civ-olmec`, `civ-early-maya`, `civ-andes`, `civ-aegean`.

- **Cited materials for this session (PROJECT META — not archaeological P/S/T/U):**
  - `docs/architecture.md` / `architecture.zh.md` — layers, entity model, “Markdown + git is source of truth,” optional later SQLite/JSON export
  - `docs/api.md` / `api.zh.md` + `docs/openapi.v0.yaml` — read-only REST for civ/src/hyp/rec/search; deliberation cloud sketch; **no** Site/Period/Object/Claim/Media archive paths yet
  - `docs/entry-depth.md` / `entry-depth.zh.md` — thick bilingual encyclopedia-style sections for civ pages
  - `docs/decisions.md` — D-2026-10-11-1…16 (seats, seed fill, deepen-to-fact-library); D-2026-10-11-2 cloud deliberation spec-first; D-2026-10-11-4 Markdown-only public interface for now
  - `docs/council.md` — this session’s process

- **Observed project state (facilitator inventory — still project meta):**
  - Public bilingual README, architecture, OpenAPI v0, council design, entry-depth standard: **present**.
  - Nine `civ-*` upgraded to rich bilingual encyclopedia-style sections + many `src-*` registries: **present**.
  - Still primarily **Markdown narrative pages + bibliography IDs** — **not yet** a machine-readable archive (no normalized JSON/SQLite export pipeline, no IIIF/media-rights packages, no queryable Site/Period/Assemblage/Object/Claim datasets, library API **unimplemented**).
  - Cloud deliberation: **spec-first, implement later** (already decided).

- **Out of scope for this session:** inventing archaeological facts; forging artifact images; promoting any hyp → fact; implementing live cloud hosts.

## Parallel lens notes

### deming-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: deming-perspective`
- **Process quality:** Thick MD + `src-*` improved *content* quality, but the **production system** still lacks a measurable export/citation gate that runs on every change. Encyclopedia prose is a special cause of “looks done” while the archive API remains common-cause unfinished.
- **Missing primitives for stable process:** Site, Period, Assemblage/Object, Claim (fact vs hypothesis), Media (rights-cleared), plus Source and Deliberation already sketched — each with stable IDs and `sources[]`.
- **Useful API:** list/filter/get those entities; serve-time citation audit; never auto-promote claims. MD can stay an *inspection* view, not the only measurable product.

### steve-jobs-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: steve-jobs-perspective`
- **Clarity cut:** The product in one breath should be: **“a careful digital archive you can query.”** Not “nine long wiki pages.”
- Encyclopedia sections are welcome as **presentation**, but shipping only prose is the wrong shape if the promise is archive+API.
- Cut dual pretend-truths: do not let beautiful bilingual essays pretend to be the queryable archive. One product story: structured records out; human-readable layers derived or linked.

### elon-musk-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: elon-musk-perspective`
- **First principles:** An archive API needs addressable atoms (site, period, object/assemblage, claim, source, media). Civilization overview essays are *aggregations*, not atoms.
- Strip the inherited assumption “GitHub README + long MD = library.” That assumption fails machine reuse.
- Physics of the build: define schema → pilot one civ fully structured (e.g. Mesopotamia) → export → OpenAPI paths that hit those tables. Spec already started; finish the archive half.

### darwin-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: darwin-perspective`
- **Selection among product shapes:** Competing explanations of “what we are”: (A) bilingual encyclopedia site; (B) research notebook; (C) digital archive + read API. Owner question selects **C**. Evidence of current fitness: A is well-fed; C is larval.
- Fitness pressure: reuse by others favors filterable entities with sources, not only narrative. Traits that help C: normalized IDs, rights-aware media, claim-level citation, fail-closed export.
- Do not “evolve” encyclopedia thickness alone and call it archive speciation.

### descartes-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: descartes-perspective`
- **Doubt first:** Doubt that `status: fact-library` on a Markdown file equals “archive ready.” Doubt that front-matter `sources[]` alone yields queryable Site/Object graphs. Doubt that OpenAPI paths for `/civilizations` fulfill “档案接口.”
- What remains clear: directional docs exist; API unimplemented; structured archive entities underspecified.
- Method: withhold assent that the product is done until schema + pilot export + archive endpoints exist as testable artifacts.

### qianxuesen-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: qianxuesen-perspective`
- **Systems structure:** Today the open loop is Enrich MD → commit → (hope API later). Missing feedback: MD/frontmatter → structured records → export gate → API → consumer queries → gaps back into editorial MD.
- Layers should distinguish: **editorial presentation** (MD) vs **archive system of record for API** (JSON Schema / SQLite tables for Source, Site, Period, Assemblage/Object, Claim, Media, Deliberation).
- Civilization pages remain a useful *view* composing claims/sites/periods; they must not be the only store the API can see.

### mozi-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: mozi-perspective`
- **Utility if wrong:** If we keep thickening essays and call it an archive API, others cannot filter sites/objects/claims, rights packages stay empty, and the project fails its stated benefit (careful reuse by others). Cost of that error is high relative to writing one more section of prose.
- Benefit of correcting now: one pilot structured civilization + schema + OpenAPI archive paths unlocks real third-party use without forging images or loosening citation gates.
- Consequential check favors **structure-feeding enrichment** over prose-only enrichment.

## Cross-examination

| Challenge | From seat | Toward | Notes |
|-----------|-----------|--------|-------|
| “Thick fact-library MD already *is* the archive” | (steelman) | All seats | Rejected as product definition: MD is necessary editorial/human layer, insufficient as machine-readable archive. |
| Depth standard contradicts archive pivot | darwin → entry-depth | entry-depth | No: keep depth, but every new section should **feed** structured Site/Period/Claim/Source records, not only paragraphs. |
| Markdown-as-SoT (D-2026-10-11-4) blocks structured SoT | descartes → decisions | D-4 | Refine, don’t scrap: git remains authoritative; structured export becomes the **API serving form**; avoid silent dual write by making export derived + gated. |
| Implement cloud deliberation before archive API | (temptation) | elon / deming | Keep D-2026-10-11-2: deliberation stays spec-first; archive schema + pilot has higher utility for “档案接口.” |
| Add IIIF/media immediately with scraped images | (temptation) | mozi / integrity | Reject: media only rights-cleared; no forged artifacts; link/cite upstream; empty Media table OK until cleared packages exist. |
| Auto-extract claims from prose with LLM into fact kind | jobs / deming | pipeline idea | Dangerous: claim extraction may seed **hypothesis** or draft Claim records requiring human+citation gate — never silent `kind: fact`. |

## Facilitator synthesis

Neutral merge of the seven lenses:

1. Owner intent is clear: **digital archive + read API**, not blog/encyclopedia alone.  
2. Current nine `fact-library` pages are valuable **presentation and editorial work**, and evidence that citation discipline can scale — but they are the wrong *sole* product shape for “档案接口.”  
3. Missing archive primitives: **Site**, **Period**, **Assemblage/Object** (with rights), **Claim** (fact vs hypothesis), **Media** (rights-cleared only); plus existing Source / Civilization-overview / Hypothesis / Reconstruction / Deliberation.  
4. API should **list / filter / get** these entities; every item carries `sources[]`; hypotheses never auto-promote.  
5. Enrichment of civ pages **continues**, but must **feed structured data**, not only prose.  
6. Immediate testable path: data schema (JSON Schema and/or SQLite) → export pipeline from MD frontmatter+sections → OpenAPI archive entity paths → **one pilot civilization fully structured** (recommend `civ-mesopotamia`).  
7. This synthesis does **not** rewrite any archaeological fact fields; it proposes product/architecture work and a decision record.

---

## Outputs

### FACT_NOTES

*(About **current repo capabilities** — project meta, not archaeology.)*

- Public repo already has bilingual READMEs, architecture, API design + OpenAPI v0, council design, entry-depth standard, and decisions through D-2026-10-11-16.
- Nine `civ-*` entries are at `status: fact-library` with rich bilingual sections and registered `src-*` bibliographies (example: `civ-mesopotamia` lists 15 source ids in front matter).
- Library HTTP API is **design-only / unimplemented**; no `export/` JSON or SQLite pipeline is shipping yet.
- OpenAPI currently exposes civilizations, sources, hypotheses, reconstructions, search, meta, deliberations — **not** Site / Period / Object / Claim / Media archive collections.
- Cloud deliberation remains **spec-first, implement later** (D-2026-10-11-2).
- No IIIF or rights-cleared media packages are in-repo; integrity rules already forbid forged artifact images.

### HYPOTHESIS_CHALLENGES

*(Product / architecture hypotheses to test — labeled **HYPOTHESIS**.)*

- **HYPOTHESIS H1:** Treating thick encyclopedia Markdown as the *primary* product will fail the owner’s “archive+API” intent even if every section is well cited.
- **HYPOTHESIS H2:** A workable public archive API needs first-class entities **Source, Site, Period, Assemblage/Object, Claim, Media, Deliberation** (Civilization overview may remain an aggregate view).
- **HYPOTHESIS H3:** Git Markdown can remain the **editorial / human-readable layer** while a gated derived JSON/SQLite export is the **API system of record**, without silent dual-write — if CI citation gate owns promotion to export.
- **HYPOTHESIS H4:** Continuing civ-page enrichment is still valuable **iff** each enrichment pass emits or updates structured records (sites, periods, claims) rather than prose alone.
- **HYPOTHESIS H5:** Piloting full structure on **one** civilization (`civ-mesopotamia`) will surface schema gaps cheaper than boiling the ocean across all nine.

### OPEN_QUESTIONS

- Exact directory layout for structured data (`data/sites/`, `data/objects/`, vs single `archive/*.json`, vs SQLite-only under `export/`)?
- Claim grain: paragraph-level vs atomic dated assertions? Who approves claim extraction?
- Media strategy v0: metadata-only + outbound links, or host rights-cleared binaries later?
- How do bilingual editorial sections map to locale fields on structured entities without duplicating conflicting facts?
- Vocabulary for region / period labels (orthogonal axes already sketched) — freeze when?
- Does D-2026-10-11-4 need explicit supersession language once export ships, or only an addendum?

### FUTURE_WINDOW

*(Testable next steps — not prophecy.)*

1. Record decision **D-2026-10-11-17**: product core = **archive + read API**; encyclopedia prose = presentation layer.  
2. Draft **JSON Schema** (and optional SQLite DDL) for Source, Site, Period, Assemblage/Object, Claim, Media, Deliberation; place under `docs/schema/` or `schemas/` (path TBD in follow-up PR).  
3. Extend **OpenAPI** with archive collection paths: `/sites`, `/periods`, `/objects`, `/claims`, `/media` (+ `{id}`), each item carrying `sources[]` and epistemic `kind` where needed.  
4. Sketch **export pipeline**: parse MD frontmatter + structured sidecars → citation fail-closed → `export/`.  
5. **Pilot:** fully structure Mesopotamia (sites, periods, a small set of well-sourced objects/assemblages, claim rows linked to `src-*`) while keeping the human MD page as the readable view.  
6. Keep civ enrichment going **only** in lockstep with structured feeds; do not treat another prose-only thicken pass as archive completion.  
7. Deliberation cloud host: remain spec-first (no change to D-2026-10-11-2).  
8. Media: add rights fields and empty/allow-listed entries only — **no** forged images, no wholesale copyright dumps.

