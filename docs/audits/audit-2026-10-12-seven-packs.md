# Quality audit — seven packs (2026-10-12)

English | [中文](audit-2026-10-12-seven-packs.zh.md)

> Same FAIL/WARN criteria as [`audit-2026-10-12-mesopotamia-egypt.md`](audit-2026-10-12-mesopotamia-egypt.md). Integrity over speed. Does **not** invent archaeology to close gaps.

**Scope:** `andes`, `indus`, `china-bronze`, `sanxingdui`, `aegean`, `olmec`, `early-maya`.

**Method:** Automated referential integrity + ranking-language scan + hypothesis disclaimer check + object inventory-field scan; human review of clear FAILs only.

**Gate:** `export_check` OK after remediations (9 packs; citation gate green). early-maya sources 68→70 after copying two already-registered comparative `src-olmec-*` into-pack.

---

## Summary counts

| Pack | Sources | Sites | Periods | Objects | Claims (fact / hyp) | Media | FAIL | WARN |
|------|--------:|------:|--------:|--------:|---------------------:|------:|-----:|------|
| andes | 68 | 41 | 7 | 48 | 65 (48 / 17) | 6 | **0** | see WARN |
| indus | 68 | 38 | 5 | 46 | 61 (48 / 13) | 5 | **0** | see WARN |
| china-bronze | 68 | 39 | 7 | 47 | 62 (47 / 15) | 1 | **0** | see WARN |
| sanxingdui | 68 | 36 | 7 | 46 | 59 (43 / 16) | 1 | **0** | see WARN |
| aegean | 68 | 40 | 7 | 46 | 60 (44 / 16) | 4 | **0** | see WARN |
| olmec | 68 | 37 | 4 | 47 | 55 (39 / 16) | 4 | **0** | see WARN |
| early-maya | 70 | 40 | 5 | 47 | 60 (43 / 17) | 4 | **0** | see WARN |

**Clear FAIL remediations this pass:** **4 → 0** (see below). Open WARNs documented; no vanity fills.

---

## Criteria (same as Mesopotamia/Egypt)

1. Claim `sources[]` non-empty; IDs resolve in-pack **and** in `sources/*.md` registry; site/period/object refs resolve.
2. Contested “first / earliest / only / America’s first” ranking language must not sit unlabeled in `kind=fact`.
3. `kind=hypothesis` requires non-empty `disclaimer`.
4. Sites: no invented coordinates (null OK); names match cited literature on review.
5. Objects: no `inventory_number` / `accession` / `museum_number` fields filled.

---

## FAIL remediations (fixed)

| Id | Pack | Issue | Fix |
|----|------|-------|-----|
| `claim-olmec-diehl-synthesis` | olmec | Fact statement echoed book-title ranking (“America’s First Civilization”) | Reworded: secondary synthesis; title ranking **not adopted as fact** |
| `claim-maya-olmec-to-maya-unilinear` | early-maya | `sources[]` cited `src-olmec-flannery-marcus-olmec-oaxaca` missing from early-maya pack JSON | Copied registered source JSON from olmec pack into early-maya (comparative cite; no new archaeology) |
| `site-izapa-comparative` | early-maya | Cited `src-olmec-stirling-bae-138-1943` missing in-pack | Same — copied registered Stirling BAE 138 into early-maya |
| `asm-maya-izapa-stelae-comparative` | early-maya | Same dangling Stirling source | Same copy |

**No inventing** of page numbers, coordinates, inventory numbers, or new finds.

---

## Per-pack WARN notes

### andes

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations below (if any) |
| **WARN** | open | null coords=41; biblio-meta≈3/48; media=6; ontology=— |

**Hypotheses (17):** `claim-andes-aspero-chiefdom-label`, `claim-andes-bandurria-challenges-chiefdom-state`, `claim-andes-casma-earliest-state`, `claim-andes-casma-state-1987-hypothesis`, `claim-andes-casma-vs-norte-chico-priority`, `claim-andes-chao-pristine-center`, `claim-andes-city-vs-ceremonial-center`, `claim-andes-gavilanes-maize-priority`, `claim-andes-maize-staple-intensity`, `claim-andes-maritime-foundations-model`, `claim-andes-maritime-model-settled`, `claim-andes-moseley-maritime-reappraised`, `claim-andes-oldest-civilization-marketing`, `claim-andes-pristine-state-label`, `claim-andes-sandweiss-environmental-demise`, `claim-andes-square-room-emblem`, `claim-andes-tello-matriz-hypothesis`

### indus

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations below (if any) |
| **WARN** | open | null coords=38; biblio-meta≈7/48; media=5; ontology=site-ghaggar-hakra-stein-survey, site-sind-majumdar-survey |

**Hypotheses (13):** `claim-indus-allahdino-script-deciphered`, `claim-indus-balakot-gulf-trade`, `claim-indus-climate-deurbanization`, `claim-indus-empire-model`, `claim-indus-empire-unified`, `claim-indus-empire-vs-network`, `claim-indus-kot-diji-conquest`, `claim-indus-law-proves-harappa-capital`, `claim-indus-lothal-dock`, `claim-indus-parpola-decipherment`, `claim-indus-rakhigarhi-eastern-capital`, `claim-indus-script-fully-deciphered`, `claim-indus-shortughai-colony`

### china-bronze

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations below (if any) |
| **WARN** | open | null coords=39; biblio-meta≈14/47; media=1; ontology=— |

**Hypotheses (15):** `claim-china-allan-cosmos-hypothesis`, `claim-china-anyange-sole-capital-always`, `claim-china-erlitou-equals-xia-capital`, `claim-china-fengchu-she-palace`, `claim-china-hoards-are-emergency-only`, `claim-china-huanbei-as-hedanjia-capital`, `claim-china-panlongcheng-as-shang-outpost`, `claim-china-taosi-yao-capital`, `claim-china-xia-equals-erlitou`, `claim-china-xia-historicity`, `claim-china-xingan-as-shang-kingdom`, `claim-china-xszcp-bands`, `claim-china-yanshi-as-western-bo`, `claim-china-zhengzhou-as-ao-or-bo`, `claim-china-zou-heng-xia-equation`

### sanxingdui

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations below (if any) |
| **WARN** | open | null coords=36; biblio-meta≈5/43; media=1; ontology=site-cpas-survey-region |

**Hypotheses (16):** `claim-sxd-ancient-shu-title`, `claim-sxd-baodun-ancestor-state`, `claim-sxd-baodun-direct-ancestor-state`, `claim-sxd-capital-moved-to-jinsha`, `claim-sxd-east-wall-date-equals-erlitou`, `claim-sxd-is-ancient-shu-state`, `claim-sxd-is-shang-colony`, `claim-sxd-maritime-cowrie-trade-route`, `claim-sxd-not-same-shang-polity`, `claim-sxd-pit-chronology-debated`, `claim-sxd-pits-only-sacrifice`, `claim-sxd-qingguanshan-palace`, `claim-sxd-same-polity-shang`, `claim-sxd-shang-colony-still-hypothesis`, `claim-sxd-single-ceremony-all-pits`, `claim-sxd-unesco-equals-verdict`

### aegean

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations below (if any) |
| **WARN** | open | null coords=40; biblio-meta≈7/44; media=4; ontology=site-thera-chronology-pointer |

**Hypotheses (16):** `claim-aegean-agamemnon-historic-mycenae-king`, `claim-aegean-circle-b-equals-circle-a-dynasty`, `claim-aegean-eruption-caused-lm-ib-collapse`, `claim-aegean-high-low-chronology`, `claim-aegean-high-vs-low-chronology`, `claim-aegean-homer-equals-excavation`, `claim-aegean-homer-nestor-equals-englianos`, `claim-aegean-linear-a-is-greek`, `claim-aegean-minoan-thalassocracy`, `claim-aegean-sea-peoples-pylos-destruction`, `claim-aegean-single-calendar-year`, `claim-aegean-single-knossos-thalassocracy`, `claim-aegean-single-thera-calendar`, `claim-aegean-thera-caused-minoan-collapse`, `claim-aegean-thera-sole-lmib`, `claim-aegean-troy-war-hypothesis`

### olmec

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations below (if any) |
| **WARN** | open | null coords=37; biblio-meta≈2/39; media=4; ontology=site-olmec-heartland-survey-pointer |

**Hypotheses (16):** `claim-olmec-arroyo-pesquero-controlled`, `claim-olmec-cascajal-oldest-script`, `claim-olmec-cascajal-oldest-writing-settled`, `claim-olmec-cascajal-oldest-writing`, `claim-olmec-colossal-heads-portraits-only`, `claim-olmec-el-manati-state-ritual`, `claim-olmec-empire-political`, `claim-olmec-mother-culture-model`, `claim-olmec-mother-culture-still`, `claim-olmec-mother-culture`, `claim-olmec-pottery-export-model`, `claim-olmec-pottery-unidirectional-export`, `claim-olmec-san-lorenzo-capital-of-all`, `claim-olmec-tres-zapotes-stela-c-long-count-origin`, `claim-olmec-were-jaguar-religion-unitary`, `claim-olmec-writing-fully-deciphered`

### early-maya

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations below (if any) |
| **WARN** | open | null coords=40; biblio-meta≈6/43; media=4; ontology=site-calakmul-preclassic-pointer |

**Hypotheses (17):** `claim-maya-aguada-fenix-egalitarian`, `claim-maya-altar-is-only-classic`, `claim-maya-calakmul-preclassic-capital`, `claim-maya-cuello-oldest-maya`, `claim-maya-e-group-astronomical-only`, `claim-maya-estrada-belli-first-title`, `claim-maya-estrada-belli-primacy-title`, `claim-maya-full-middle-preclassic-divine-kingship`, `claim-maya-kinship-kingship-model`, `claim-maya-middle-preclassic-divine-kingship-settled`, `claim-maya-middle-preclassic-divine-kingship`, `claim-maya-mirador-first-state-hypothesis`, `claim-maya-mirador-first-state-settled`, `claim-maya-mirador-first-state`, `claim-maya-olmec-influence-direction`, `claim-maya-olmec-to-maya-unilinear`, `claim-maya-preclassic-divine-kingship-full`


### Shared open WARNs

- **W1 — Null coordinates** on all sites in these seven packs (intentional deferral; add only from cited gazetteers/reports).
- **W2 — Bibliographic-meta residue** — several packs still have author-publish-lead facts (esp. china-bronze ~14/47). Prefer a future substance-tighten pass like Mesopotamia/Egypt Job A; do not mint unsourced narrative.
- **W3 — Site ontology** — survey zones / pointers filed as `entity: site` (indus, sanxingdui, olmec). Acceptable for v0; optional later `site_kind`.
- **W4 — Media thin** — outbound/metadata only; aligns with no-forged-image policy.

---

## Decision link

Recorded as **D-2026-10-12-9** in [`docs/decisions.md`](../decisions.md) / [`docs/decisions.zh.md`](../decisions.zh.md).


---

## Follow-up — cited coordinates + media thicken (Job C, same day)

**Decision link:** **D-2026-10-12-10**. Same gazetteer/media integrity rules as Mesopotamia/Egypt Job C.

### Coordinates filled (seven packs)

| Pack | Filled | Still null | Gazetteer basis (examples) |
|------|-------:|----------:|------------------------------|
| andes | **1** / 41 | **40** | UNESCO WHC 1269 Caral DMS only — other Norte Chico sites left null pending clear GeoNames/UNESCO hits |
| indus | **3** / 38 | **35** | UNESCO Moenjodaro 138 + Dholavira 1645; GeoNames Harappa S.ANS |
| china-bronze | **1** / 39 | **38** | UNESCO WHC 1114-001 Yinxu Palace area DMS; Erlitou etc. left null (no clean GeoNames S.ANS in this pass) |
| sanxingdui | **0** / 36 | **36** | No clean Pleiades/GeoNames/UNESCO inscribed centroid verified this pass — **honest skip** |
| aegean | **20** / 40 | **20** | Pleiades (Knossos palace, Mycenae, Nestor’s Palace, Phaistos, Tiryns, Troy/Ilium, Akrotiri, Mallia, Zakros, Kommos, …); loci/frames left null |
| olmec | **2** / 37 | **35** | GeoNames La Venta Ruinas S.ANS; Chalcatzingo S.ANS; San Lorenzo left null (no clear S.ANS match this pass) |
| early-maya | **6** / 40 | **34** | GeoNames El Mirador / Ceibal / Uaxactún / Tikal / Cuello S.ANS; UNESCO Tentative 5738 San Bartolo DMS |

### Media added (seven packs)

| Pack | Before | After |
|------|-------:|------:|
| andes | 6 | **8** |
| indus | 5 | **8** |
| china-bronze | 1 | **4** |
| sanxingdui | 1 | **4** |
| aegean | 4 | **7** |
| olmec | 4 | **7** |
| early-maya | 4 | **7** |

Examples: UNESCO Yinxu / Shu tentative listings; Archive.org Schliemann Mycenae / Bagley Ancient Sichuan / Li Chi Anyang; PLOS/Nature/Science DOIs already registered as sources.

### Shared WARN status after Job C

- **W1:** Partially addressed across packs; remaining empties documented — do not invent.
- **W2 / W3:** Unchanged this pass (substance / ontology).
- **W4:** Improved; still outbound-link-only by design.

**Gate:** `export_check` OK (9 packs; citation gate green). Media total **58** (was 28 at D-2026-10-12-7 baseline).
