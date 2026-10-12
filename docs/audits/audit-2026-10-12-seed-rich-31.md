# Quality audit — 31 `library-seed-rich` packs (2026-10-12)

English | [中文](audit-2026-10-12-seed-rich-31.zh.md)

> Same FAIL/WARN criteria as [`audit-2026-10-12-seven-packs.md`](audit-2026-10-12-seven-packs.md) and [`audit-2026-10-12-mesopotamia-egypt.md`](audit-2026-10-12-mesopotamia-egypt.md). Integrity over speed. Does **not** invent archaeology to close gaps.

**Decision:** [D-2026-10-12-18](../decisions.md#d-2026-10-12-18--quality-audit-31-library-seed-rich-packs)

**Scope:** All **31** packs with `civilization.status = library-seed-rich` (Wave-1 + Wave-2 + Wave-3 densified shells). The original nine `fact-library` packs (`mesopotamia`, `egypt`, `andes`, `indus`, `china-bronze`, `sanxingdui`, `aegean`, `olmec`, `early-maya`) are **out of scope** except as criteria reference (already audited).

**Method:** Automated referential integrity + ranking-language scan + hypothesis disclaimer check + object inventory-field scan + biblio-meta pattern scan; human review of clear FAILs only.

**Gate:** `export_check` OK after remediations (**40** packs; citation gate green).

---

## Summary counts

| Pack | Sources | Sites | Periods | Objects | Claims (fact / hyp) | Media | FAIL | WARN |
|------|--------:|------:|--------:|--------:|---------------------:|------:|-----:|------|
| `aksum` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 2 | **0** | see WARN |
| `anatolia-hittite` | 15 | 7 | 4 | 3 | 11 (10 / 1) | 3 | **0** | see WARN |
| `ancestral-pueblo` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 3 | **0** | see WARN |
| `angkor` | 15 | 8 | 4 | 3 | 11 (11 / 0) | 3 | **0** | see WARN |
| `aztec` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 2 | **0** | see WARN |
| `ban-chiang` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 2 | **0** | see WARN |
| `bmac-oxus` | 15 | 7 | 4 | 3 | 11 (10 / 1) | 2 | **0** | see WARN |
| `cahokia` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 3 | **0** | see WARN |
| `chavin-andes` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 3 | **0** | see WARN |
| `classic-maya` | 15 | 8 | 4 | 3 | 11 (11 / 0) | 3 | **0** | see WARN |
| `dong-son` | 15 | 7 | 4 | 3 | 11 (10 / 1) | 1 | **0** | see WARN |
| `early-korea` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 2 | **0** | see WARN |
| `elam-iran` | 15 | 8 | 4 | 3 | 11 (10 / 1) | 3 | **0** | see WARN |
| `great-zimbabwe` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 2 | **0** | see WARN |
| `hallstatt-celtic` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 2 | **0** | see WARN |
| `inca` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 3 | **0** | see WARN |
| `jomon-yayoi` | 15 | 6 | 4 | 3 | 11 (10 / 1) | 3 | **0** | see WARN |
| `lapita-pacific` | 15 | 7 | 4 | 3 | 11 (10 / 1) | 2 | **0** | see WARN |
| `levant-ugarit` | 15 | 7 | 4 | 3 | 11 (10 / 1) | 2 | **0** | see WARN |
| `mitanni` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 1 | **0** | see WARN |
| `moche` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 1 | **0** | see WARN |
| `nok-west-africa` | 15 | 7 | 4 | 3 | 11 (10 / 1) | 3 | **0** | see WARN |
| `nubia-kush` | 15 | 9 | 4 | 3 | 11 (10 / 1) | 3 | **0** | see WARN |
| `nuragic-sardinia` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 2 | **0** | see WARN |
| `phoenician` | 15 | 8 | 4 | 3 | 11 (11 / 0) | 3 | **0** | see WARN |
| `rapa-nui` | 15 | 7 | 4 | 3 | 11 (9 / 2) | 2 | **0** | see WARN |
| `teotihuacan` | 15 | 6 | 4 | 3 | 11 (10 / 1) | 3 | **0** | see WARN |
| `tiwanaku` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 2 | **0** | see WARN |
| `wari` | 15 | 7 | 4 | 3 | 11 (11 / 0) | 1 | **0** | see WARN |
| `west-africa-medieval` | 15 | 8 | 4 | 3 | 11 (11 / 0) | 2 | **0** | see WARN |
| `zapotec` | 15 | 6 | 4 | 3 | 11 (10 / 1) | 3 | **0** | see WARN |

**Clear FAIL remediations this pass:** **3 issue classes → 0 FAIL** (see below). Open WARNs documented; no vanity fills; no invented coordinates, page numbers, inventory numbers, or media art.

---

## Criteria (same as Mesopotamia/Egypt / seven-packs)

1. Claim `sources[]` non-empty; IDs resolve in-pack **and** in `sources/*.md` registry; site/period/object refs resolve.
2. Contested “first / earliest / only / America’s first” ranking language must not sit unlabeled in `kind=fact`.
3. `kind=hypothesis` requires non-empty `disclaimer`.
4. Sites: no invented coordinates (null OK); orientation/survey frames flagged as ontology WARN.
5. Objects: no `inventory_number` / `accession` / `museum_number` fields filled.
6. Pure bibliographic-only fact statements (“Author YEAR provides a synthesis…”) rewritten toward report-level orientation **or** left as honest WARN when already substantive — **no invented finds**.

---

## FAIL remediations (fixed)

| Id | Pack | Issue | Fix |
|----|------|-------|-----|
| `asm-mitanni-amarna-letters-frame` | mitanni | `sources[]` cited missing `src-mitanni-letterman-diplomatic-texts` (in-pack + registry) | Typo fix: → already-registered `src-mitanni-beckman-diplomatic-texts` |
| `claim-rapanui-transport-hypothesis` | rapa-nui | Contested experimental transport model sat as `kind=fact` (id/statement say hypothesis) | Relabeled `fact` → `hypothesis` + non-empty `disclaimer` |
| `claim-rapanui-hunt-lipo` | rapa-nui | Contested colonization/rat/“ecocide” competing models sat as `kind=fact` | Relabeled `fact` → `hypothesis` + `disclaimer` |
| 28 biblio-meta claims | 22 packs | Pure “Author provides a synthesis…” fact lines | Rewritten toward report-level orientation phrasing; **no new archaeology** |

**No inventing** of page numbers, coordinates, inventory numbers, or new finds.

---

## Soft ranking language (dismissed — not FAIL)

| Claim | Pack | Hit | Verdict |
|-------|------|-----|---------|
| `claim-chavin-nesbitt-reconsider` | chavin-andes | “twenty-**first**-century” | **Dismissed** — century ordinal, not primacy ranking |
| `claim-nok-archaeology-magazine-public` | nok-west-africa | “orientation-**only**” | **Dismissed** — tier disclaimer |
| `claim-rapanui-ethics` | rapa-nui | “links **only**” | **Dismissed** — ethics/media policy |

No unlabeled contested primacy ranking found in `kind=fact` after remediations.

---

## Per-pack WARN notes

### `aksum`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; biblio-meta≈2/11; media=2; ontology=4 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-beta-gaba-orientation`, `site-matara-orientation`, `site-aksum-cathedral-orientation`, `site-adulis-orientation`

**Residual biblio-orientation facts:** `claim-aksum-munro-hay`, `claim-aksum-coinage`

### `anatolia-hittite`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=2; ontology=2 |

**Hypotheses (1):** `claim-hittite-empire-collapse-frame`

**Ontology / orientation sites:** `site-hattusa-lower-city-frame`, `site-hattusa-temple-district-frame`

**Residual biblio-orientation facts:** —

### `ancestral-pueblo`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=5; biblio-meta≈3/11; ontology=4 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-pueblo-cliff-palace-orientation`, `site-pueblo-chetro-ketl-orientation`, `site-pueblo-aztec-ruins-orientation`, `site-pueblo-salmon-ruins-orientation`

**Residual biblio-orientation facts:** `claim-pueblo-plog-overview`, `claim-pueblo-lekson-synthesis`, `claim-pueblo-vivian-chacoan`

### `angkor`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; ontology=6 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-angkor-baphuon-orientation`, `site-angkor-hariharalaya-orientation`, `site-angkor-west-baray-orientation`, `site-angkor-ta-prohm-orientation`, `site-angkor-bayon-orientation`, `site-angkor-hydraulic-orientation`

**Residual biblio-orientation facts:** —

### `aztec`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; biblio-meta≈1/11; media=2; ontology=6 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-tlatelolco-orientation`, `site-aztec-texcoco-orientation`, `site-aztec-tlacopan-orientation`, `site-aztec-chapultepec-orientation`, `site-aztec-tenochtitlan-island-orientation`, `site-aztec-tlatelolco-market-orientation`

**Residual biblio-orientation facts:** `claim-aztec-smith-aztecs`

### `ban-chiang`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; biblio-meta≈1/11; media=2; ontology=3 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-ban-non-wat-orientation`, `site-lopburi-metal-orientation`, `site-ban-chiang-museum-orientation`

**Residual biblio-orientation facts:** `claim-ban-chiang-glover`

### `bmac-oxus`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=5; media=2; ontology=4 |

**Hypotheses (1):** `claim-bmac-state-level-hypothesis`

**Ontology / orientation sites:** `site-shortughai-orientation`, `site-murghab-delta-survey-frame`, `site-bactria-oasis-frame`, `site-gonur-north-south-frame`

**Residual biblio-orientation facts:** —

### `cahokia`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; biblio-meta≈1/11; ontology=6 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-cahokia-mitchell-orientation`, `site-cahokia-st-louis-mound-group-orientation`, `site-cahokia-powell-mound-orientation`, `site-cahokia-mound-72-orientation`, `site-cahokia-woodhenge-orientation`, `site-cahokia-east-st-louis-orientation`

**Residual biblio-orientation facts:** `claim-cahokia-fowler-atlas`

### `chavin-andes`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; biblio-meta≈2/11; ontology=5 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-chavin-pochoc-orientation`, `site-chavin-pacopampa-orientation`, `site-chavin-old-temple-orientation`, `site-chavin-interaction-orientation`, `site-chavin-kuntur-wasi-orientation`

**Residual biblio-orientation facts:** `claim-chavin-burger-synthesis`, `claim-chavin-excavation-monograph`

### `classic-maya`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; biblio-meta≈1/11; ontology=3 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-ceibal-orientation`, `site-calakmul-biosphere-orientation`, `site-yaxchilan-orientation`

**Residual biblio-orientation facts:** `claim-classic-maya-coe-houston`

### `dong-son`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=7; media=1; ontology=6 |

**Hypotheses (1):** `claim-dong-son-china-interaction-hypothesis`

**Ontology / orientation sites:** `site-chau-can-orientation`, `site-viet-khe-orientation`, `site-co-loa-orientation`, `site-lang-vac-orientation`, `site-drum-exchange-sphere-frame`, `site-red-river-delta-frame`

**Residual biblio-orientation facts:** —

### `early-korea`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=7; biblio-meta≈1/11; media=2; ontology=5 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-gochang-dolmen-orientation`, `site-mumun-songguk-ri-orientation`, `site-mumun-settlement-orientation`, `site-baekje-historic-orientation`, `site-buyeo-baekje-orientation`

**Residual biblio-orientation facts:** `claim-early-korea-nelson`

### `elam-iran`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=2; ontology=2 |

**Hypotheses (1):** `claim-elam-proto-elamite-writing-frame`

**Ontology / orientation sites:** `site-elam-susiana-survey-frame`, `site-elam-fars-highland-frame`

**Residual biblio-orientation facts:** —

### `great-zimbabwe`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; biblio-meta≈2/11; media=2; ontology=4 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-zimbabwe-culture-orientation`, `site-zimbabwe-mapungubwe-orientation`, `site-zimbabwe-khami-orientation`, `site-zimbabwe-valley-ruins-orientation`

**Residual biblio-orientation facts:** `claim-zimbabwe-huffman-handbook`, `claim-zimbabwe-garlake`

### `hallstatt-celtic`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; biblio-meta≈1/11; media=2; ontology=6 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-hallstatt-vix-orientation`, `site-hallstatt-heuneburg-orientation`, `site-hallstatt-salt-mines-orientation`, `site-hallstatt-cemetery-orientation`, `site-hallstatt-hochdorf-orientation`, `site-hallstatt-princely-orientation`

**Residual biblio-orientation facts:** `claim-hallstatt-cunliffe`

### `inca`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=5; biblio-meta≈1/11; ontology=5 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-inca-ollantaytambo-orientation`, `site-inca-sacsayhuaman-orientation`, `site-inca-huanuco-pampa-orientation`, `site-inca-pisac-orientation`, `site-inca-vilcashuaman-orientation`

**Residual biblio-orientation facts:** `claim-inca-mcewan-overview`

### `jomon-yayoi`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=2; ontology=2 |

**Hypotheses (1):** `claim-jomon-yayoi-transition-hypothesis`

**Ontology / orientation sites:** `site-itazuke-orientation`, `site-yoshinogari-orientation`

**Residual biblio-orientation facts:** —

### `lapita-pacific`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=7; biblio-meta≈1/10; media=2; ontology=4 |

**Hypotheses (1):** `claim-lapita-single-migration-hypothesis`

**Ontology / orientation sites:** `site-nukuleka-orientation`, `site-bismarck-early-lapita-frame`, `site-bourewa-or-fiji-frame`, `site-reef-santa-cruz-orientation`

**Residual biblio-orientation facts:** `claim-lapita-oceanic-ancestors-frame`

### `levant-ugarit`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=7; biblio-meta≈1/10; media=2; ontology=5 |

**Hypotheses (1):** `claim-ugarit-sea-peoples-hypothesis`

**Ontology / orientation sites:** `site-ras-ibn-hani-orientation`, `site-ugarit-acropolis-temples-frame`, `site-ugarit-kingdom-territory-frame`, `site-ugarit-royal-palace-frame`, `site-ugarit-south-palace-archives-frame`

**Residual biblio-orientation facts:** `claim-ugarit-handbook-studies`

### `mitanni`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=7; media=1; ontology=3 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-mitanni-upper-khabur-orientation`, `site-mitanni-washukanni-orientation`, `site-tell-fekheriye-orientation`

**Residual biblio-orientation facts:** —

### `moche`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; biblio-meta≈1/11; media=1; ontology=5 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-moche-san-jose-moro-orientation`, `site-moche-galindo-orientation`, `site-moche-el-brujo-orientation`, `site-sipan-orientation`, `site-moche-pacatnamu-orientation`

**Residual biblio-orientation facts:** `claim-moche-quilter-synthesis`

### `nok-west-africa`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=7; biblio-meta≈1/10; ontology=2 |

**Hypotheses (1):** `claim-nok-state-complexity-hypothesis`

**Ontology / orientation sites:** `site-nok-anama-orientation`, `site-jos-museum-frame`

**Residual biblio-orientation facts:** `claim-nok-west-africa-ironization`

### `nubia-kush`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=2; biblio-meta≈2/10; ontology=1 |

**Hypotheses (1):** `claim-nubia-twenty-fifth-dynasty-frame`

**Ontology / orientation sites:** `site-kerma-eastern-cemetery-frame`

**Residual biblio-orientation facts:** `claim-nubia-handbook-2021-orientation`, `claim-nubia-long-sequence-edwards`

### `nuragic-sardinia`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; biblio-meta≈1/11; media=2; ontology=6 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-nuragic-santa-vittoria-orientation`, `site-nuragic-arrubiu-orientation`, `site-nuragic-lena-orientation`, `site-nuragic-landscape-orientation`, `site-nuragic-santimbru-orientation`, `site-nuragic-su-tempiesu-orientation`

**Residual biblio-orientation facts:** `claim-nuragic-webster`

### `phoenician`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=5; ontology=3 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-gadir-cadiz-orientation`, `site-sarepta-orientation`, `site-kition-orientation`

**Residual biblio-orientation facts:** —

### `rapa-nui`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=5; media=2; ontology=6 |

**Hypotheses (2):** `claim-rapanui-hunt-lipo`, `claim-rapanui-transport-hypothesis`

**Ontology / orientation sites:** `site-rapanui-puna-pau-orientation`, `site-rapanui-anakena-orientation`, `site-rapanui-ahu-tongariki-orientation`, `site-rapanui-rano-raraku-orientation`, `site-rapanui-orongo-orientation`, `site-rapanui-ahu-akivi-orientation`

**Residual biblio-orientation facts:** —

### `teotihuacan`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=5; ontology=4 |

**Hypotheses (1):** `claim-teotihuacan-decline-hypothesis`

**Ontology / orientation sites:** `site-teotihuacan-pyramid-sun-frame`, `site-teotihuacan-apartment-compounds-frame`, `site-teotihuacan-obsidian-workshops-frame`, `site-teotihuacan-pyramid-moon-frame`

**Residual biblio-orientation facts:** —

### `tiwanaku`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=6; biblio-meta≈1/11; media=2; ontology=3 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-tiwanaku-lukurmata-orientation`, `site-tiwanaku-omo-orientation`, `site-tiwanaku-katari-orientation`

**Residual biblio-orientation facts:** `claim-tiwanaku-kolata`

### `wari`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=7; biblio-meta≈1/11; media=1; ontology=3 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-jincamocco-orientation`, `site-wari-azangaro-orientation`, `site-viracochapampa-orientation`

**Residual biblio-orientation facts:** `claim-wari-schreiber-empire`

### `west-africa-medieval`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=5; biblio-meta≈1/11; media=2; ontology=6 |

**Hypotheses (0):** *(none in pack)*

**Ontology / orientation sites:** `site-koumbi-saleh-orientation`, `site-waf-niani-orientation`, `site-waf-gao-orientation`, `site-waf-jenne-jeno-orientation`, `site-waf-aoudaghost-orientation`, `site-waf-walata-orientation`

**Residual biblio-orientation facts:** `claim-waf-gomez-dominion`

### `zapotec`

| Result | Count | Notes |
|--------|------:|-------|
| **FAIL** | **0** | After remediations |
| **WARN** | open | null coords=5; ontology=4 |

**Hypotheses (1):** `claim-zapotec-state-formation-debate`

**Ontology / orientation sites:** `site-monte-alban-danzantes-frame`, `site-monte-alban-main-plaza-frame`, `site-oaxaca-valley-survey-frame`, `site-mitla-orientation`

**Residual biblio-orientation facts:** —


### Shared open WARNs

| WARN class | Meaning | Action |
|------------|---------|--------|
| **null coords** | Site `coordinates: null` where no clean published WGS84 was cited this wave | Keep null; fill only with cited Pleiades/UNESCO/museum WGS84 |
| **biblio-meta** | Claim still reads as synthesis/handbook orientation after light rewrite | Honest for `library-seed-rich`; thicken with report-level substance later **without inventing** |
| **thin media** | `< 3` outbound media items | Add outbound-link-only landings when rights-clear |
| **ontology / orientation sites** | `*-orientation`, `*-survey-frame`, `*-pointer` site ids | Keep labeled; not excavated “sites” with forged coords |

---

## Spot-check (dense nine)

Not re-audited end-to-end. Quick integrity spot-check via `export_check` (all 40 packs) — **green**. Prior audits remain authoritative: meso/egypt, seven-packs.

---

## Verdict

| Metric | Result |
|--------|--------|
| Packs audited | **31** / 31 `library-seed-rich` |
| FAIL after fix | **0** |
| Invented archaeology | **0** |
| `export_check` | **OK** (40 packs) |
