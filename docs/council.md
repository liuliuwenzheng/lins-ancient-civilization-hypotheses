# Deliberation Council

English | [中文](council.zh.md)

> Multi-lens audit before entries harden. Perspectives are AI-generated thinking lenses — **not** endorsements by historical or living persons.

Related: [Architecture](architecture.md) · [API](api.md) · Session template: [`../deliberations/_template.md`](../deliberations/_template.md)

**Lens catalog (by reference only):** [liuliuwenzheng/FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives) — do **not** copy the full perspective pack into this repo; select seats by folder slug.

---

## 1. Purpose

The **Deliberation Council** is a conversational, future-facing review layer. Before a civilization fact, hypothesis, or reconstruction hardens (or before a PR merges material that could blur fact and speculation), a Facilitator seats several **perspective lenses** to:

1. Check citations and the fact ≠ hypothesis split  
2. Stress-test claims from diverse epistemic angles  
3. Surface open questions and **testable** next steps (not prophecy)  
4. Leave a durable Markdown trail under `deliberations/`

The Council **audits**; it does not invent civilizations, forge images, or promote hypotheses to facts.

---

## 2. Roles

| Role | Who | Duty |
|------|-----|------|
| **Facilitator** | Neutral process role (human editor and/or cloud orchestration) | Enforce fact/hypothesis separation; require citations; bar silent promotion of hyps → facts; synthesize outputs into the four columns below; never speak *as* a named historical person. |
| **Seat lenses** | Selected skills from FHLS-perspectives | Each seat is an **AI-generated thinking lens** keyed by folder slug (e.g. `deming-perspective`). Lenses critique structure, evidence, clarity, systems, utility — they do **not** speak with the authority or endorsement of the real person. |

### Integrity labels (mandatory on every lens turn)

| Field | Value | Meaning |
|-------|-------|---------|
| `perspective` | `true` | Output is a perspective lens, not a primary source |
| `person_endorsement` | `false` | The named person did **not** endorse this project or this session |
| `lens_slug` | e.g. `deming-perspective` | Exact FHLS-perspectives folder slug |

Tone aligned with FHLS-perspectives: AI-generated; for reference only; not biography, not academic final word; do not use for impersonation or commercial false endorsement.

---

## 3. Default seats (v0)

Seven diverse lenses that **already exist** in FHLS-perspectives. Adjust per session; keep Facilitator + at least three seats for a minimal audit.

| # | Folder slug (use this in API / front matter) | Lens focus in this project |
|---|----------------------------------------------|----------------------------|
| 1 | `deming-perspective` | Quality of evidence, process, variation vs special causes |
| 2 | `steve-jobs-perspective` | Clarity, what to cut, whether the claim is sayable in one breath |
| 3 | `elon-musk-perspective` | First principles; strip inherited assumptions |
| 4 | `darwin-perspective` | Evidence trails, selection among competing explanations |
| 5 | `descartes-perspective` | Methodical doubt; what must be doubted first |
| 6 | `qianxuesen-perspective` | Systems structure; feedback and open loops |
| 7 | `mozi-perspective` | Utility and consequential check — what good does this claim do if wrong? |

**v0 seats confirmed (2026-10-11):** the seven seats above are the default Council lineup; see [`decisions.md`](decisions.md). **Cloud deliberation implementation is deferred** until after the API/OpenAPI spec is settled (spec-first) — design only in [`api.md` §9](api.md#9-deliberation-council-cloud-first).

**Not in catalog yet:** Aristotle (`aristotle-perspective` or similar). Optional later via Nuwa distillation into FHLS-perspectives — **do not invent** a full perspective file in this repo.

Browse all available slugs: [FHLS-perspectives CATALOG](https://github.com/liuliuwenzheng/FHLS-perspectives/blob/main/CATALOG.md).

---

## 4. Discussion flow

```
Intake → Parallel lens notes → Cross-examination → Facilitator synthesis → Four-column outputs
```

| Step | Name | What happens |
|------|------|----------------|
| 1 | **Intake** | Name target ids (`civ-*` / `hyp-*` / `rec-*` / `src-*`), paste or link cited sources, state the question. No undocumented claims. |
| 2 | **Parallel lens notes** | Each seat writes short notes under its slug; every note carries `perspective: true`, `person_endorsement: false`. |
| 3 | **Cross-examination** | Seats challenge each other on evidence gaps, category errors (fact vs hyp), and overclaiming. Facilitator blocks ad-hominem and “because the famous person would say…”. |
| 4 | **Facilitator synthesis** | Merge into four output columns; mark unresolved items; never rewrite fact-library fields from a lens opinion alone. |
| 5 | **Persist** | Save session Markdown under `deliberations/` (see template). Published sessions remain git-backed; cloud API sessions are ephemeral until exported/PR’d. |

### Four output columns

| Column | Id | Content |
|--------|-----|---------|
| **FACT_NOTES** | `FACT_NOTES` | Notes that strengthen, correct, or demand better citations for **fact** claims — still require `src-*` before any fact edit |
| **HYPOTHESIS_CHALLENGES** | `HYPOTHESIS_CHALLENGES` | Challenges to labeled hypotheses; never auto-retire or auto-promote |
| **OPEN_QUESTIONS** | `OPEN_QUESTIONS` | Unresolved epistemic questions |
| **FUTURE_WINDOW** | `FUTURE_WINDOW` | Forward-looking **research questions** and **testable next steps** (excavation checklists, comparative corpora, dating tests) — **not** prophecy or destiny talk |

---

## 5. Persistence

- Directory: `deliberations/`
- Template: [`deliberations/_template.md`](../deliberations/_template.md)
- Id pattern: `delib-YYYY-short-slug`
- Status: `open` \| `synthesized` \| `archived`
- Link targets via registry ids only (`civ-*`, `hyp-*`, `rec-*`, `src-*`)

Cloud deliberation compute may run elsewhere for speed; **git Markdown is still the source of truth** for any session we publish as part of the project trail.

---

## 6. Hard rules (Council-specific)

1. Facts ≠ hypotheses; every claim needs sources.  
2. No forged artifact images; no client/cost/private business data.  
3. Lenses are audit tools — never presented as the historical person speaking with endorsement authority.  
4. Reuse FHLS-perspectives **by reference** (repo link + slug list); do not vendor the entire pack here.  
5. Council output must not silently promote a hypothesis into the fact library. Fact changes still go through PR + citation gate.  
6. Do not invent civilization case studies in templates or examples.

---

## 7. Cloud API (preview)

Conversational sessions prefer a **cloud** host for latency (SSE or WebSocket streaming; sync JSON fallback). Sketch: [api.md § Deliberations](api.md#9-deliberation-council-cloud-first) · [openapi.v0.yaml](openapi.v0.yaml).

Library endpoints stay **read-only**. Deliberation writes are **session-scoped** and must not mutate fact records by side effect.
