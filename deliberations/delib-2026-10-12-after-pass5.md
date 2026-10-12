---
id: delib-2026-10-12-after-pass5
title: "Deliberation: After density pass 5 — archive quality vs thin intro; next priorities"
status: synthesized
created: 2026-10-12
updated: 2026-10-12
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
  sources: []   # project-meta intake — export_check totals, not archaeological P/S claims
seats:
  - deming-perspective
  - steve-jobs-perspective
  - elon-musk-perspective
  - darwin-perspective
  - descartes-perspective
  - qianxuesen-perspective
  - mozi-perspective
facilitator: "cloud-orchestrator + human editor trail"
question: "第五轮深挖已完成。审议：当前档案是否仍「薄简介」、相对维基/学术档案的优势是否站得住、下一优先是什么（继续密度 / 新文明 / 云端只读 / UI 工艺 / 一手 PDF 权利清晰媒体 / 主张粒度细化）。"
perspective: true
person_endorsement: false
lens_catalog: "https://github.com/liuliuwenzheng/FHLS-perspectives"
related_docs:
  - docs/architecture.md
  - docs/api.md
  - docs/archive-data-model.md
  - docs/design-taste.md
  - docs/entry-depth.md
  - docs/decisions.md
  - docs/council.md
  - deliberations/delib-2026-10-11-archive-api-direction.md
---

# Deliberation: After density pass 5 — archive quality vs thin intro; next priorities

> **Perspective lenses only.** AI-generated thinking aids from [FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives).  
> `perspective: true` · `person_endorsement: false` — named persons do **not** endorse this project or this session.

## Intake

- **Question (owner 林):** 第五轮深挖已完成。审议：当前档案是否仍「薄简介」、相对维基/学术档案的优势是否站得住、下一优先是什么（继续密度 / 新文明 / 云端只读 / UI 工艺 / 一手 PDF 权利清晰媒体 / 主张粒度细化）。

- **Target ids:** all nine first-batch `civ-*` with structured packs under `data/structured/*` (pass 5 complete per D-2026-10-12-5 / D-2026-10-12-6).

- **Cited materials for this session (PROJECT META — not archaeological P/S/T/U):**
  - `tools/export_check.py` run 2026-10-12 — **OK**; citation gate: fact claims require non-empty resolvable `sources[]`
  - Prior deliberation [`delib-2026-10-11-archive-api-direction`](delib-2026-10-11-archive-api-direction.md) (product = archive + read API)
  - `docs/design-taste.md` / `/ui`; `docs/api.md`; D-2026-10-11-2 cloud deliberation still **spec-first**
  - Density decisions D-2026-10-11-21…27 (pass 1), D-28…30 (pass 2), D-2026-10-12-1…2 (pass 3), D-3…4 (pass 4), D-5…6 (pass 5)

- **Observed `export_check` totals (2026-10-12, post pass 5):**

| Pack | sources | sites | periods | objects | claims | media |
|------|--------:|------:|--------:|--------:|-------:|------:|
| mesopotamia | 76 | 43 | 10 | 58 | 70 | 1 |
| egypt | 70 | 43 | 6 | 57 | 69 | 2 |
| andes | 68 | 41 | 7 | 48 | 65 | 6 |
| indus | 68 | 38 | 5 | 46 | 61 | 5 |
| china-bronze | 68 | 39 | 7 | 47 | 62 | 1 |
| sanxingdui | 68 | 36 | 7 | 46 | 59 | 1 |
| aegean | 68 | 40 | 7 | 46 | 60 | 4 |
| olmec | 68 | 37 | 4 | 47 | 55 | 4 |
| early-maya | 68 | 40 | 5 | 47 | 60 | 4 |
| **TOTAL** | **622** | **357** | **58** | **442** | **561** | **28** |

  Claim kind split (structured claims): **fact 438** · **hypothesis 123** · other 0.

- **Out of scope:** inventing archaeological content for coverage vanity; forging artifact images; promoting hyp → fact; implementing live cloud hosts in this session; wholesale copyright PDF dumps.

## Parallel lens notes

### deming-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: deming-perspective`
- **Process quality:** Five density passes + fail-closed `export_check` is a measurable system, not anecdotal “we wrote more.” Common-cause quality is now the citation gate and schema conformance; special-cause risk is **row vanity** (more sources that are thin stubs) vs **row integrity** (resolvable P/S, honest hyp labels).
- **Still thin vs exhaustive site reports?** Yes relative to full excavation corpora — but **no longer a thin intro page**. The defect to watch next is uneven claim grain and duplicate/near-duplicate sources across packs, not absence of structure.
- **Next control chart:** audit densest packs (mesopotamia, egypt) for claim→source resolvability depth and site-record completeness before another volume pass.

### steve-jobs-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: steve-jobs-perspective`
- **One-line product:** still “a careful digital archive you can query” — and after pass 5 the structured layer finally **looks like** that product, not nine essays pretending.
- Cut the temptation to chase Wikipedia breadth. Our edge is **honest labels + queryable atoms**, not article count. UI `/ui` already shows fact vs hypothesis badges — keep polish **iterative**, not a redesign distraction from archive quality.
- Do not ship decorative media; empty media tables with clear rights later beat fake museum photos now.

### elon-musk-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: elon-musk-perspective`
- **First principles check:** Atoms exist (Source/Site/Period/Object/Claim/Media) + read API + gate. Physics of next gain: improve **signal per row** (quality audit) before adding new civ shells or cloud host complexity.
- Strip assumption “more rows = better archive.” Exhaustive site reports are a different product (museum/excavation pubs). We need **machine-readable cited claims**, not a mirror of every trench notebook.
- Cloud read-only host: useful when local API is stable and packs audited — not before quality baseline on densest packs.

### darwin-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: darwin-perspective`
- **Selection:** Variants of “what we are” after pass 5: (A) thick bilingual wiki clone; (B) growing structured archive with epistemic labels; (C) academic site-report repository. Fitness evidence favors **B**. A loses on structure; C loses on rights/hosting/exhaustiveness.
- Advantage vs Wikipedia stands **if** we keep selection pressure on citation gate + hypothesis labeling; it collapses if we invent content for coverage vanity.
- New civ shells: careful speciation only — empty shells OK; filled vanity shells fail.

### descartes-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: descartes-perspective`
- **Doubt:** Doubt that “622 sources” equals scholarly archive depth — many may be bibliographic pointers without page-level anchors. Doubt that media count 28 means visual archive (mostly outbound metadata). Doubt that cloud deliberation readiness follows from density passes (still D-2026-10-11-2 spec-first).
- What survives doubt: structured packs for 9 civs; API serving them; fact≠hypothesis enforced at export; no forged images policy held; `/ui` + design-taste present.
- Withhold assent that “advantage over Wikipedia” is coverage; assent only to **methodological** advantage until claim/site audits pass.

### qianxuesen-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: qianxuesen-perspective`
- **Systems loop now:** MD editorial → structured JSON → export_check → API → `/ui` → (gaps back to editorial). Open loops remaining: **quality audit feedback**, **cloud read-only deployment**, **rights-cleared media intake**, claim-grain standards.
- Do not open a new civ-shell subsystem before closing the audit loop on existing packs — otherwise system complexity grows without feedback.
- Ranked control: (1) audit densest packs (2) optional careful new shells (3) cloud read-only when ready (4) UI polish iteration (5) media only with clear rights.

### mozi-perspective

- `perspective: true` · `person_endorsement: false` · `lens_slug: mozi-perspective`
- **Utility if wrong:** If we call the project “still a thin intro,” we undervalue the archive+API work and misallocate to prose. If we claim Wikipedia-beating coverage, we overclaim and erode trust. If we invent rows for vanity, we fail the integrity promise.
- Benefit of ranked next steps: audit first maximizes truthfulness per hour; new civs without audit dilutes; cloud host without quality baseline ships brittle service; media without rights creates legal/ethical cost.
- Consequential check: **do not invent content for coverage vanity.**

## Cross-examination

| Challenge | From seat | Toward | Notes |
|-----------|-----------|--------|-------|
| “Still just thin intros” | (steelman owner fear) | All seats | **Partially outdated:** prose alone was thin; structured 622/357/561 with gate is archive-*ish*. Still thin vs exhaustive excavation corpora — say that honestly. |
| “We now beat Wikipedia” | (temptation) | descartes / mozi | **Reject coverage claim.** Advantage = machine-readable + citation gate + hyp labels, not breadth. |
| “Keep pass 6 immediately on all nine” | volume habit | deming / elon | Defer blanket volume; prefer **quality audit** on densest packs first, then selective deepen where audit finds gaps. |
| “Open many new civs now for show” | coverage vanity | darwin / mozi | **Reject.** Optional careful shells only; no invented fills. |
| “Ship cloud deliberation + media hosting now” | feature itch | jobs / qian | Keep deliberation **spec-first** (D-2). Cloud **read-only archive** host is separate and ranked after audit. Media only rights-cleared. |
| “LLM-auto thicken claims to look dense” | speed temptation | deming / descartes | Reject silent fact promotion; any extraction → hypothesis/draft until human+citation gate. |

## Facilitator synthesis

Neutral merge of the seven lenses:

1. After density **pass 5**, the project is **no longer a thin textual introduction**. It is a **real, still incomplete, machine-readable archive** with a fail-closed citation gate, fact≠hypothesis labeling, local read API, `/ui`, and design-taste doctrine.
2. Relative to Wikipedia / full academic site-report corpora: **coverage advantage does not hold**; **methodological advantage holds** (queryable atoms, resolvable `sources[]` on facts, explicit hypotheses, no forged images).
3. Cloud deliberation remains **spec-first** (unchanged). Cloud **read-only** hosting of the archive API is desirable later, not the immediate bottleneck.
4. Ranked next priorities (see FUTURE_WINDOW / D-2026-10-12-7):
   1. Claim/site **quality audit** on densest packs (mesopotamia, egypt first)
   2. Optional **new civilization shells** carefully (structure only; no vanity fills)
   3. **Cloud read-only** host when audit baseline is acceptable
   4. **UI polish** iteration (taste, not redesign-as-escape)
   5. **Media** only with clear rights (metadata/links first; no forged artifacts)
5. Explicit non-recommendation: **do not invent content for coverage vanity**; do not treat another blind volume pass as the default without audit.

This synthesis does **not** rewrite archaeological fact fields.

---

## Outputs

### FACT_NOTES

*(Project meta — verified 2026-10-12.)*

- `export_check` **OK** on **9** packs; citation gate active (fact claims need non-empty resolvable `sources[]`).
- Structured totals: **sources 622** · **sites 357** · **periods 58** · **objects 442** · **claims 561** (fact **438** / hypothesis **123**) · **media 28**.
- Densest packs by sources/sites: **mesopotamia** (76 / 43), **egypt** (70 / 43); other seven packs at sources **68** each after pass 5.
- Product stack present: structured archive + local read-only API + `/ui` + `docs/design-taste.*`; encyclopedia Markdown remains presentation/editorial layer.
- Integrity held: no forged artifact images policy; media mostly outbound metadata; cloud deliberation still **spec-first** (D-2026-10-11-2).
- Prior directional deliberation [`delib-2026-10-11-archive-api-direction`](delib-2026-10-11-archive-api-direction.md) goals (schema, pilot, API, gate) are **substantially landed**; remaining gap is depth/quality vs exhaustive corpora, not “missing archive shape.”

### HYPOTHESIS_CHALLENGES

- **HYPOTHESIS H1:** Calling the current state a “thin intro” **understates** the structured archive+API work after pass 5 — challenge that framing.
- **HYPOTHESIS H2:** Claiming superiority to Wikipedia on **coverage** is false; superiority claim should be limited to **epistemic/machine-readable method**.
- **HYPOTHESIS H3:** Another blind all-pack volume pass yields less integrity per hour than a **claim/site quality audit** on mesopotamia/egypt first.
- **HYPOTHESIS H4:** Opening many new filled civilizations now optimizes for vanity, not reuse — shells only if careful.
- **HYPOTHESIS H5:** Hosting rights-unclear PDFs/images would trade short-term “richness” for long-term integrity failure.

### OPEN_QUESTIONS

- Audit checklist: what minimum fields make a Site/Claim “pass” (URL/DOI, page or plate pointer, grade P/S, non-duplicate)?
- When is claim grain too coarse (civilization-level slogans) vs too fine (unmaintainable micro-claims)?
- Threshold to greenlight cloud read-only deploy (uptime, auth none, rate limits, which packs)?
- Vocabulary freeze timing for region/period labels across packs?
- Aristotle (or other) lens distillation into FHLS — still out of band until catalog exists?

### FUTURE_WINDOW

*(Testable next steps — not prophecy.)*

1. Record **D-2026-10-12-7**: post–pass-5 priority ranking as synthesized below.  
2. **(1) Quality audit** — start with `data/structured/mesopotamia/` and `egypt/`: spot-check claim→source links, hyp labeling, site completeness; open fix PRs; only then selective deepen.  
3. **(2) Optional new civ shells** — scaffolding + empty structured packs allowed; **no** invented fills for coverage vanity.  
4. **(3) Cloud read-only host** — when audit baseline acceptable; serve existing API; no write routes; deliberation cloud remains spec-first.  
5. **(4) UI polish iteration** — taste checklist passes on `/ui` (contrast, bilingual, badges), not a product pivot.  
6. **(5) Media** — rights-cleared metadata/links only; no forged artifacts; no wholesale copyright dumps.  
7. Do **not** default to undifferentiated pass 6 across all nine without audit findings.

