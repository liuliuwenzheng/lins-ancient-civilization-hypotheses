# Architecture

English | [中文](architecture.zh.md)

> Integrity first: facts ≠ hypotheses; every claim cites sources; leave a careful trail others can reuse — not a dogma.

## Mission tone (short)

| Principle | Meaning in this repo |
|-----------|----------------------|
| **Integrity** | Fact columns never hold speculation. Hypotheses are always labeled. No fabricated stories or forged artifact images. |
| **Open reuse** | Today: anyone can read Markdown in git. Tomorrow: the same entities via a read-only API. |
| **Humility** | Hypotheses are working ideas. Corrections with better sources win. We leave a trail, not a creed. |
| **Craft** | Seen and unseen quality — schemas, citation gates, calm `/ui`. See [`design-taste.md`](design-taste.md). |

## Layers

Data flows one way through the library stages. Later layers may **link** earlier ones; they must not rewrite fact fields silently. The **Deliberation Council** sits beside hypotheses and reconstructions as an audit layer — it reviews before hardening, and never silently promotes hypotheses to facts.

```
sources/                  (1) Source registry — graded P/S/T/U
    ↓ cited by
data/civilizations/       (2) Fact library — sourced summaries only
    ↓ linked by
hypotheses/               (3) Hypothesis board — always HYPOTHESIS
    ↓ audited by          ──── deliberations/  (3b) Deliberation Council
    ↓ combined in              (multi-lens audit; FUTURE_WINDOW)
reconstructions/          (4) Reconstructions — facts + hyps + uncertainty
```

| Layer | Directory | Role | Status values |
|-------|-----------|------|----------------|
| Sources | `sources/` | Bibliographic registry + reliability tier | tier: `P` \| `S` \| `T` \| `U` |
| Fact library | `data/civilizations/` | Dated, cited civilization entries | `fact-library` |
| Hypothesis board | `hypotheses/` | Labeled associations / patterns | `open` \| `challenged` \| `retired` |
| Deliberation Council | `deliberations/` | Multi-lens audit sessions (FHLS-perspectives seats) | `open` \| `synthesized` \| `archived` |
| Reconstructions | `reconstructions/` | Causality notes with explicit uncertainty | `draft` \| `review` \| `archived` |

Details of the method: [`methodology.md`](methodology.md). Source tiers: [`source-grading.md`](source-grading.md). Council design: [`council.md`](council.md) · [中文](council.zh.md). Lens catalog (by reference): [FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives).

## Entity model

IDs are stable strings. Prefixes make type obvious in links and API responses.

| Entity | ID pattern | Front-matter (from templates) | Body |
|--------|------------|-------------------------------|------|
| **Source** | `src-YYYY-short-slug` | `id`, `type`, `citation`, `url`, `access_date`, `reliability_tier`, `notes` | Citation table + notes |
| **Civilization** | `civ-YYYY-slug` | `id`, `names` (zh/en/native), `region`, `time_span`, `status`, `summary`, `sources[]`, `related_ids[]`, `notes` | Summary, sources, related civs |
| **Hypothesis** | `hyp-YYYY-short-slug` | `id`, `title`, `status`, `claims[]`, `supporting_sources[]`, `conflicting_sources[]`, `related_civilizations[]`, `caveats` | **HYPOTHESIS** header + sections |
| **Reconstruction** | `rec-YYYY-short-slug` | `id`, `title`, `linked_facts[]`, `linked_hypotheses[]`, `status`, `uncertainty_summary` | Linked IDs, narrative, uncertainty |
| **Deliberation** | `delib-YYYY-short-slug` | `id`, `title`, `status`, `targets`, `seats[]` (FHLS slugs), `question`, `perspective`, `person_endorsement` | Intake, lens notes, four output columns |

### Relationships (`related_ids` and cousins)

```
Source.src-*  ←cited by←  Civilization.sources[]
Source.src-*  ←cited by←  Hypothesis.supporting_sources[] / conflicting_sources[]
Civilization.civ-*  ←→  Civilization.related_ids[]          (factual geo/chrono links only)
Civilization.civ-*  ←linked by←  Hypothesis.related_civilizations[]
Civilization.civ-*  ←linked by←  Reconstruction.linked_facts[]
Hypothesis.hyp-*    ←linked by←  Reconstruction.linked_hypotheses[]
Deliberation.delib-*  →targets→  civ-* / hyp-* / rec-* / src-*
Deliberation.seats[]  →references→  FHLS-perspectives folder slugs (external)
```

Rules:

- Cross-links always use **registry IDs**, not bare URLs.
- Civilization `related_ids` describe geography/chronology in **fact** terms only. Speculative “maybe related because …” goes in a hypothesis.
- A reconstruction that asserts a causal guess **must** cite at least one `hyp-*` for that guess.

## Invariants (fail-closed)

These are not style tips. Treat them as gates (same spirit as poetry-tree’s rights gate, adapted to **citations**):

1. **Fact ≠ speculation.** `data/civilizations/` fields never hold “maybe / perhaps / lost civilization” claims. Those belong under `hypotheses/` or a marked section of a reconstruction.
2. **Hypothesis label.** Every hypothesis file header and any API representation must carry an explicit HYPOTHESIS / `kind: "hypothesis"` signal and a disclaimer.
3. **Source grading.** Every `sources/` entry has `reliability_tier` ∈ {P, S, T, U}. Fact-library claims should prefer P/S; U must be flagged, never decisive alone.
4. **Citation required.** No registered source → do not expose the claim as fact (in Markdown or in a future API). Fail closed.
5. **No private business data.** Client names, costs, contracts — never in this repo.
6. **No forged imagery.** No fabricated artifact photos; no wholesale copyrighted dumps — cite and link.
7. **Perspectives ≠ endorsement.** Council seats are AI lenses from FHLS-perspectives (`perspective: true`, `person_endorsement: false`). They never rewrite fact fields by themselves and must not be framed as real-person endorsement.

## Archive layer (product clarification — 2026-10-11)

**Product core = digital archive + read API**, not blog/encyclopedia alone.

| Layer | Role |
|-------|------|
| **Editorial / presentation** | Bilingual Markdown civilization pages, READMEs, human-readable narratives under git |
| **Archive system of record (for API)** | Structured records: **Source**, **Site**, **Period**, **Assemblage/Object** (with rights), **Claim** (fact vs hypothesis), **Media** (rights-cleared only), **Deliberation**, plus Civilization as an aggregate overview |

Rules:

1. Thick encyclopedia MD is welcome as a **view** and editorial craft — it is **not** sufficient as the sole product shape for “档案接口 / archive API.”
2. Enrichment of `civ-*` pages continues **only if** it feeds structured records (sites, periods, claims, sources), not prose alone.
3. Git remains authoritative for published trails; a gated derived **JSON / SQLite** export under `export/` (path TBD) becomes the API serving form — no silent dual-write.
4. API list/filter/get archive entities; every item carries `sources[]`; hypotheses never auto-promote to facts.
5. No forged artifact images; Media entries require clear rights (metadata + outbound links acceptable in v0).

Decision: [`decisions.md` D-2026-10-11-17](decisions.md). Schemas: [`../schemas/`](../schemas/). Pilot: [`../data/structured/mesopotamia/`](../data/structured/mesopotamia/). Model: [`archive-data-model.md`](archive-data-model.md). Gate: `tools/export_check.py`. Decision D-2026-10-11-18. Deliberation trail: [`../deliberations/delib-2026-10-11-archive-api-direction.md`](../deliberations/delib-2026-10-11-archive-api-direction.md).

## Storage today

**Markdown + git remains the published editorial source of truth.** Structured archive records + gated `export/` are the API serving form once implemented (see Archive layer above).

- Humans edit via PR using `_template.md` copies.
- Front matter is YAML; bodies are readable Markdown.
- Templates under each directory are scaffolding only — **not** filled with invented case studies.

## Storage later (archive export path)

Required for the archive+API product (search, filters, hosting):

1. A build step parses Markdown → normalized **SQLite** and/or **JSON** under something like `export/` (exact path TBD).
2. **Citation gate (fail-closed):** entries that claim fact status but lack resolvable `sources[]` / registry files are **rejected from the export** (and ideally fail CI). Same idea as poetry-tree: build-time gate + serve-time audit so the API cannot be a backdoor around the rule.
3. The git Markdown remains authoritative; the DB/JSON is a derived artifact, never the only copy of truth.
4. Fact-library now has cited seeds (nine `fact-library` entries as of 2026-10-11) — proceed to schema + pilot export; still fail-closed on citations.

## Directory map (aligned)

```
lins-ancient-civilization-hypotheses/
├── README.md / README.zh.md
├── LICENSE
├── docs/
│   ├── methodology.md
│   ├── source-grading.md
│   ├── contributing.md
│   ├── architecture.md / architecture.zh.md   ← this document
│   ├── council.md / council.zh.md             ← Deliberation Council
│   ├── api.md / api.zh.md                     ← public API design
│   ├── design-taste.md / design-taste.zh.md   ← craft / UI checklist
│   └── openapi.v0.yaml                        ← OpenAPI stub
├── data/civilizations/     # fact library (+ _template.md)
├── sources/                # source registry (+ _template.md)
├── hypotheses/             # hypothesis board (+ _template.md)
├── deliberations/          # Council sessions (+ _template.md)
└── reconstructions/        # reconstructions (+ _template.md)
```

Do not invent parallel top-level trees. Extend this map only when a real need appears (e.g. `export/` for generated DB).

## Public API (preview)

Design-only for now: library resources are **read-only** REST under `/api/v1/…` (orthogonal filters, source refs, hypotheses always labeled). Deliberation sessions add **session-scoped** cloud endpoints (prefer streaming) that must not silently promote hypotheses to facts. Full design: [`api.md`](api.md) · Council: [`council.md`](council.md) · OpenAPI stub: [`openapi.v0.yaml`](openapi.v0.yaml).
