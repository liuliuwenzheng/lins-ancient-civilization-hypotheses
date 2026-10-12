# Quality audit — Mesopotamia + Egypt (2026-10-12)

English | [中文](audit-2026-10-12-mesopotamia-egypt.zh.md)

> Implements priority **#1** of [D-2026-10-12-7](../decisions.md#d-2026-10-12-7--postpass-5-priority-ranking-deliberation-council): claim/site quality audit for the densest packs. Integrity over speed. This report does **not** invent archaeology to “fix” gaps.

**Scope:** `data/structured/mesopotamia/` and `data/structured/egypt/` (claims, sites, sources, objects; periods/media spot-checked). Cross-checked against `sources/*.md` registry and, where needed, `data/civilizations/civ-mesopotamia.md` / `civ-ancient-egypt.md`.

**Method:** Automated referential integrity + pattern scan, then human review of every `kind=hypothesis` claim, assertive fact statements, famous-object metadata, and site coordinate policy.

**Gate:** `export_check` re-run after audit — **OK** (9 packs; citation gate green).

---

## Summary counts

| Pack | Sources | Sites | Periods | Objects | Claims (fact / hyp) | Media |
|------|--------:|------:|--------:|--------:|---------------------:|------:|
| Mesopotamia | 76 | 43 | 10 | 58 | 70 (63 / 7) | 1 |
| Egypt | 70 | 43 | 6 | 57 | 69 (63 / 6) | 2 |
| **Audit total** | **146** | **86** | **16** | **115** | **139 (126 / 13)** | **3** |

| Result | Mesopotamia | Egypt | Notes |
|--------|------------:|------:|-------|
| **FAIL** | **0** | **0** | No hard integrity failures found |
| **WARN** | **44** | **46** | Mostly intentional null coordinates; see lists |
| **PASS (claims ref/kind)** | 70/70 | 69/69 | All claim `sources[]` non-empty and resolve in-pack + registry |

**JSON remediations this pass:** **none** (no clear FAILs to relabel/trim/drop). Open WARNs remain documented below.

---

## Criteria results

### 1. Claim `sources[]` non-empty and IDs resolve

| Check | Result |
|-------|--------|
| Empty `sources[]` on any claim | **PASS** (0) |
| Source id missing from pack JSON | **PASS** (0) |
| Source id missing from `sources/*.md` registry | **PASS** (0) — meso 76/76, egypt 70/70 |
| Claim → `site_ids` / `period_ids` / `object_ids` dangling | **PASS** (0) |
| Site/object → `sources[]` dangling | **PASS** (0) |

### 2. Overreach / “first–only–earliest” ranking language

Ranking / primacy language for contested comparisons is **already in the hypothesis column** for both packs. Automated “First Dynasty / first season” hits on facts are **false positives** (period name / excavation-season ordinal) — dismissed.

| Claim id | Kind | Verdict |
|----------|------|---------|
| `claim-meso-first-city-ranking` | hypothesis | **PASS** — world’s-first-city ranking rejected as fact |
| `claim-meso-hassuna-first-village` | hypothesis | **PASS** |
| `claim-meso-jerwan-first-aqueduct` | hypothesis | **PASS** |
| `claim-egypt-uj-earliest-writing` | hypothesis | **PASS** |
| `claim-egypt-amarna-unique-planned-capital` | hypothesis | **PASS** |
| `claim-meso-hansen-alhiba-1970` | fact | **WARN dismissed** — “first (1968–1969) season” = campaign ordinal |
| `claim-egypt-abydos-royal-tombs` | fact | **WARN dismissed** — “First Dynasty” = period name |
| `claim-egypt-emery-great-tombs-ii` | fact | **WARN dismissed** — same |
| `claim-egypt-emery-saqqara-tombs` | fact | **WARN dismissed** — same |

**No FAIL** for unlabeled ranking-as-fact.

### 3. `kind=fact` vs `kind=hypothesis`

All 13 hypotheses carry a non-empty `disclaimer` and cite sources. Contested models reviewed:

**Mesopotamia hypotheses (7):** `claim-meso-brak-uruk-colony`, `claim-meso-first-city-ranking`, `claim-meso-hassuna-first-village`, `claim-meso-jerwan-first-aqueduct`, `claim-meso-leilan-climate-collapse`, `claim-meso-nuzi-as-early-urban`, `claim-meso-uruk-expansion-model`.

**Egypt hypotheses (6):** `claim-egypt-amarna-unique-planned-capital`, `claim-egypt-fayum-as-nile-state-cradle`, `claim-egypt-memphis-capital-precision`, `claim-egypt-narmer-single-unification`, `claim-egypt-tasian-before-badarian`, `claim-egypt-uj-earliest-writing`.

Climate collapse at Leilan is correctly split: excavation-report fact (`claim-meso-weiss-leilan-1990`) vs drought-collapse model hypothesis (`claim-meso-leilan-climate-collapse`). Narmer “single battle unification” stays hypothesis; process framing stays fact.

**No FAIL** for misclassification.

### 4. Sites — coordinates and names

| Check | Result |
|-------|--------|
| Invented coordinates | **PASS** — all **86** sites have `coordinates: null` |
| Names match cited literature | **PASS** on review (Uruk/Warka, Tell al-Hiba/Lagash vs Girsu/Tello kept distinct, Umm el-Qaab/Abydos, Hierakonpolis/Kom el-Ahmar, etc.) |
| Sites lack `sources[]` | **PASS** (0) |

**WARN (open, intentional):** every site omits coordinates. Editorial notes already say “coordinates not asserted / not invented.” This is **honest deferral**, not a defect to “fix” by fabricating lat/lon. Remediation = add coords **only** when a cited gazetteer / excavation report supplies them.

Mesopotamia site ids (43):  
`site-abu-salabikh`, `site-adab-bismaya`, `site-arpachiyah`, `site-assur`, `site-assur-anu-adad`, `site-babylon`, `site-babylon-merkes`, `site-bavian-gomel`, `site-chagar-bazar`, `site-choga-mami`, `site-diyala-plains-survey`, `site-eridu`, `site-euphrates-central-floodplain-survey`, `site-habuba-kabira`, `site-hassuna`, `site-ishchali`, `site-isin`, `site-jemdet-nasr`, `site-jerwan`, `site-khafajah`, `site-khorsabad`, `site-kish`, `site-lagash-girsu`, `site-mari`, `site-nimrud`, `site-nineveh`, `site-nippur`, `site-nuzi`, `site-shuruppak-fara`, `site-tell-agrab`, `site-tell-al-hiba-lagash`, `site-tell-al-ubaid`, `site-tell-asmar`, `site-tell-brak`, `site-tell-leilan`, `site-tell-uqair`, `site-tepe-gawra`, `site-uhaimir-kish`, `site-ur`, `site-ur-royal-cemetery`, `site-ur-ur-iii-buildings`, `site-uruk`, `site-uruk-countryside-survey`.

Egypt site ids (43):  
`site-abusir`, `site-abydos`, `site-abydos-osireion`, `site-amarna`, `site-amarna-north-suburb`, `site-amarna-workmens-village`, `site-armant`, `site-armant-temples`, `site-badari`, `site-ballas`, `site-bet-khallaf`, `site-bubastis`, `site-buto`, `site-dahshur`, `site-deir-el-bahari`, `site-dendereh`, `site-el-amrah`, `site-el-kab`, `site-elephantine`, `site-fayum-kom-k`, `site-fayum-kom-w`, `site-gerzeh`, `site-giza`, `site-helwan`, `site-hemamieh`, `site-hierakonpolis`, `site-hu-abadiyeh`, `site-illahun`, `site-kahun`, `site-lisht`, `site-maadi`, `site-mahasna`, `site-matmar`, `site-meidum`, `site-memphis`, `site-mostagedda`, `site-naga-ed-der`, `site-naqada`, `site-qau`, `site-saqqara`, `site-saqqara-pepi-ii`, `site-tarkhan`, `site-tell-el-farkha`.

**WARN (ontology, open):** some records are **sub-loci** or **survey zones** filed as `entity: site` (e.g. `site-assur-anu-adad`, `site-babylon-merkes`, `site-diyala-plains-survey`, `site-amarna-workmens-village`). Acceptable for v0 queryability; later schema may add `site_kind: locus|survey-zone|settlement`.

### 5. Objects — metadata only, no fake inventory numbers

| Check | Result |
|-------|--------|
| `inventory_number` / `accession` / `museum_number` fields | **PASS** — **absent** on all 115 objects |
| Object kinds | Mesopotamia: 57 `assemblage` + 1 `artifact-class`; Egypt: 57 `assemblage` |
| Rights | All `outbound-link-only`; notes forbid forged binaries / invented inventory |
| Famous items (e.g. Narmer Palette) | Filed as **assemblage-level** metadata with excavation sources; unification reading deferred to hypothesis claim |

**No FAIL.**

---

## FAIL list

*None.*

No claim was relabeled, trimmed, or dropped in structured JSON this pass.

---

## WARN list (open)

### W1 — Null coordinates on all audited sites (86)

**Severity:** WARN (integrity-preserving)  
**Ids:** all Mesopotamia + Egypt site ids listed above.  
**Remediation:** Add `coordinates` only from cited gazetteers / final reports; never invent. Track as a future density task, not a vanity fill.

### W2 — Bibliographic-meta claims dominate substance claims

**Severity:** WARN (archive depth / product honesty)  
Rough classifier: ~40/63 Mesopotamia facts and ~46/63 Egypt facts are primarily “publication X reports/publishes Y” rather than archaeological substance statements.

This is **honest provenance spine**, but it means the claim layer still under-delivers “rich archive API” substance relative to site/source counts.

**Remediation (do not invent):** Prefer next deepen pass to add **sourced substance claims** (stratigraphy, assemblage classes, administrative practices) tied to already-registered P reports — or promote selected biblio claims’ archaeological content into separate fact claims with the same `sources[]`. Do **not** mint unsourced narrative.

### W3 — Soft interpretive framing on a few facts (keep watching)

Not FAILs (handbook-sourced; no primacy ranking), but wording is slightly interpretive:

| Id | Note |
|----|------|
| `claim-meso-core-region-early-cities` | “core region” framing — 5 handbook sources; OK as orientation fact |
| `claim-meso-uruk-key-horizon` | “key horizon” — handbook framing |
| `claim-egypt-old-kingdom-monuments` | “state capacity and royal ideology” — attributed to Lehner/Edwards/Shaw surveys |
| `claim-egypt-nile-flood-ecology` | Butzer cultural-ecology framing — attributed |
| `claim-egypt-delta-upper-interaction` | Network language carefully hedges against conquest narrative — OK |

**Remediation:** Optional future copy-edit to lead with “Survey X frames…” even more explicitly; no forced relabel this pass.

### W4 — Media still thin

Mesopotamia 1 + Egypt 2 outbound catalog/document links only. Aligns with no-forged-image policy; coverage WARN only.

---

## Recommended remediations (ordered)

1. **Keep FAIL count at zero** — do not invent coords, inventory numbers, or unsourced substance to look denser.  
2. **Cited coordinates pass** for top sites (Uruk, Ur, Nippur, Giza, Saqqara, Abydos, Hierakonpolis, …) when a source states them.  
3. **Substance-claim pass** on Mesopotamia then Egypt: derive archaeologically specific facts from already-registered excavation reports.  
4. **Optional `site_kind`** for locus vs survey-zone.  
5. Only then resume multi-pack volume density (per D-2026-10-12-7: unaudited volume is not the default).

---

## Decision link

Recorded as **D-2026-10-12-8** in [`docs/decisions.md`](../decisions.md) / [`docs/decisions.zh.md`](../decisions.zh.md).

---

## Appendix — hypothesis ids (complete)

- Mesopotamia: `claim-meso-brak-uruk-colony`, `claim-meso-first-city-ranking`, `claim-meso-hassuna-first-village`, `claim-meso-jerwan-first-aqueduct`, `claim-meso-leilan-climate-collapse`, `claim-meso-nuzi-as-early-urban`, `claim-meso-uruk-expansion-model`
- Egypt: `claim-egypt-amarna-unique-planned-capital`, `claim-egypt-fayum-as-nile-state-cradle`, `claim-egypt-memphis-capital-precision`, `claim-egypt-narmer-single-unification`, `claim-egypt-tasian-before-badarian`, `claim-egypt-uj-earliest-writing`
