# Project decisions

English | [中文](decisions.zh.md)

> Dated choices that constrain scope. Markdown in this repo remains the source of truth until an implemented API proves otherwise.

Related: [Council](council.md) · [API](api.md) · [Architecture](architecture.md)

---

## 2026-10-11

### D-2026-10-11-1 — Default Council seats (v0) confirmed

**Decision:** Keep the seven FHLS-perspectives seats already listed in [`council.md`](council.md):

1. `deming-perspective`
2. `steve-jobs-perspective`
3. `elon-musk-perspective`
4. `darwin-perspective`
5. `descartes-perspective`
6. `qianxuesen-perspective`
7. `mozi-perspective`

**Notes:** Lenses are AI thinking tools (`perspective: true`, `person_endorsement: false`). Aristotle is **not** seated until a real FHLS catalog entry exists — do not invent a perspective file in this repo.

### D-2026-10-11-2 — Cloud deliberation: spec first, implement later

**Decision:** Cloud deliberation host = **spec-first**. Ship and refine the design in [`api.md` §9](api.md#9-deliberation-council-cloud-first) / [`openapi.v0.yaml`](openapi.v0.yaml); **do not** implement a live cloud service yet.

**Notes:** Prefer cloud (SSE/WebSocket, parallel seats) when implementation begins. Published sessions still land as git Markdown under `deliberations/`.

### D-2026-10-11-3 — First fact-library seed regions (shells only)

**Decision:** Open scaffold files under `data/civilizations/` for these seed ids — **structure and placeholders only**. No invented facts, no fake sources, no forged images.

| Id | Names (zh / en) |
|----|-----------------|
| `civ-mesopotamia` | 两河 / Mesopotamia |
| `civ-ancient-egypt` | 古埃及 / Ancient Egypt |
| `civ-indus-valley` | 印度河 / Indus Valley |
| `civ-china-bronze` | 中国青铜时代（总览壳） / China Bronze Age (overview shell) |
| `civ-sanxingdui` | 三星堆 / Sanxingdui |
| `civ-olmec` | 奥尔梅克 / Olmec |
| `civ-early-maya` | 早期玛雅 / Early Maya |
| `civ-andes` | 安第斯早期文明（总览壳） / Andean early civilizations (overview shell) |
| `civ-aegean` | 爱琴 / Aegean |

**Notes:** `time_span` values on shells are approximate scholarly conventional ranges labeled for citation before any “publish as fact-library” step. `sources: []` until real `src-*` registry entries exist. Status remains `draft` until citations land.

### D-2026-10-11-4 — Markdown remains source of truth (for now)

**Decision:** Git-backed Markdown templates and entries are the **only** public library interface until a citation-fail-closed export/API is implemented. No silent dual store.

### D-2026-10-11-5 — Fill order starts with Mesopotamia + Egypt

**Decision:** Fact-library filling begins with the earliest Near Eastern / Nile shells: `civ-mesopotamia` (Sumer/Uruk-centered overview) and `civ-ancient-egypt` (Predynastic → Early Dynastic overview), before other seed regions.

**Notes:** Integrity gate remains: every factual claim needs a registered `src-*`. Andes receives only an optional Caral chronologic pointer when solidly cited; no full Andes expansion in this pass. Status may move from `draft` to `library-seed` only with ≥2 solid sources and a fully cited summary.

### D-2026-10-11-6 — Andes/Caral completed to library-seed

**Decision:** After Mesopotamia + Egypt, complete `civ-andes` (Caral–Norte Chico) from draft to `library-seed` before the next seed batch.

**Notes:** Registered Science 2001, Nature 2004 (95 dates; ~3000–1800 cal BCE), Shady 1997, and Shady & Leyva 2003. No world-earliest ranking claim; “city vs ceremonial center / state vs complex society” kept in Notes as open debate.

### D-2026-10-11-7 — Indus Valley filled as next chronological library-seed

**Decision:** After Andes/Caral completion, fill `civ-indus-valley` from draft shell to `library-seed` as the next chronological Old World batch (Indus Tradition / Mature Harappan florescence ~2600–1900 BCE, overlapping late 3rd-millennium peers).

**Notes:** Registered Kenoyer 1991 (era table), Wright 2010 (florescence 2600–1900 BCE; Indus/Ghaggar-Hakra), Kenoyer 2014 Cambridge chapter, Possehl 2002, Marshall 1931 (Mohenjo-daro P), Meadow ed. 1991 (Harappa 1986–1990 P). Script undeciphered = research-status fact. “Empire” vs city-network / state form kept in Notes as open debate. No forged images or invented page numbers.

### D-2026-10-11-8 — China Bronze overview + Sanxingdui filled as next chronological library-seed

**Decision:** After Indus Valley, fill `civ-china-bronze` (Central Plains Erlitou / Shang–Zhou bronze overview) and `civ-sanxingdui` (Guanghan, Sichuan) from draft shells to `library-seed` as the next chronological East Asian batch.

**Notes:** Registered Thorp 1991 (Erlitou “minimal” definition; Xia historicity not assumed), Liu & Chen 2003 (state formation ~1800–1400 BCE; metal and salt), Flad & Chen 2013 (Yangzi Late Neolithic → end of Bronze Age), Bagley 1987 (Shang ritual bronzes); for Sanxingdui, Sichuan 1999 pit report (P), Ge & Linduff 1990, Bagley 1988, Li et al. 2022 Antiquity (~12 km²; c. 2700–1000 BC; 1986 Pits 1–2; new pits and Pit 4 radiocarbon). Xia historicity, Sanxingdui–Shang polity identity, and disputed pit chronologies kept in Notes. No forged images or invented page numbers.

### D-2026-10-11-9 — Aegean Bronze Age filled as next chronological library-seed

**Decision:** After China Bronze overview + Sanxingdui, fill `civ-aegean` from draft shell to `library-seed` as the next chronological East Mediterranean / European batch (Early–Late Bronze Age Aegean overview: Cyclades / Minoan Crete / Mycenaean mainland).

**Notes:** Registered Dickinson 1994 (CUP synthesis; ~3000–1000 BC), Shelmerdine ed. 2008 (Companion; c. 3000–1100 BCE; Crete / mainland / islands), Broodbank 2000 (Early Cyclades), Manning et al. 2006 *Science* (Thera late 17th c. BCE; LM IA–II high-chronology case — debate open), Evans *Palace of Minos* 1921–1935 (historical P; restoration caveats), Blegen & Rawson 1966 (Palace of Nestor / Englianos P), Ventris & Chadwick 1956 (Linear B = Mycenaean Greek), Salgarella 2022 OCD (Linear A undeciphered; tier T orientation only). Thalassocracy and high vs low absolute chronology kept in Notes as open debate. Not a single-palace entry. No forged images or invented page numbers.

### D-2026-10-11-10 — Olmec + Early Maya filled as final Mesoamerica library-seeds (first seed batch complete)

**Decision:** After Aegean, fill `civ-olmec` and `civ-early-maya` from draft shells to `library-seed` as the final Mesoamerican pair in the first nine-shell seed batch. With this commit, **all nine** first-batch civilization shells (`civ-mesopotamia`, `civ-ancient-egypt`, `civ-indus-valley`, `civ-china-bronze`, `civ-sanxingdui`, `civ-andes`, `civ-aegean`, `civ-olmec`, `civ-early-maya`) are at `library-seed`.

**Notes:** Olmec — registered Pool 2007 (CUP; Veracruz–Tabasco Formative; ~3500 ya / ~1000-year floruit; monumental stone art framing), Diehl 2004 (Thames & Hudson survey; San Lorenzo / La Venta / abroad / Epi-Olmec TOC; title primacy = framing only), Coe & Diehl 1980 (San Lorenzo Tenochtitlán excavation report, tier P), Grove ed. 1987 (*Ancient Chalcatzingo*, highland Olmec-style center, tier P), Nichols & Pool 2012 (Oxford Mesoamerica handbook orientation). Early Maya — registered Sharer & Traxler 2006 (6th ed. long-view handbook; seed stops at Early Classic), Estrada-Belli 2011 (Preclassic ritual/power; Nakbe / El Mirador / Cival; Classic onset ~3rd c. CE), Inomata et al. 2013 *Science* (Ceibal ~1000–700 BCE plaza-pyramid / E-Group; interregional interaction vs one-way La Venta). Mother culture vs sister cultures / Olmec→Maya diffusion kept in Notes. Classic Maya collapse explicitly out of scope for `civ-early-maya`. Cross-link `related_ids` retained with debate caveats. No forged images or invented page numbers.

### D-2026-10-11-11 — Deepen existing seeds to rich fact entries

**Decision:** Upgrade civilization fact-library **depth**. Thin one-paragraph seeds are not meaningful. Adopt the enriched template sections in [`data/civilizations/_template.md`](../data/civilizations/_template.md) and the bilingual depth standard in [`entry-depth.md`](entry-depth.md) / [`entry-depth.zh.md`](entry-depth.zh.md).

**Notes:** Major-civilization overviews expanding toward durable library status aim for ~8–15+ registered sources; every major section must cite; bilingual CN+EN preferred; no filler or unverifiable color. Status ladder: `draft` → `library-seed` → `library-seed-rich` → `fact-library`. Pilot enrichment: rewrite `civ-mesopotamia` to the new template with substantially more real sources (2026-10-11). Other seeds remain `library-seed` until similarly deepened. Integrity > speed.

### D-2026-10-11-12 — Ancient Egypt deepened to fact-library (Mesopotamia-matched)

**Decision:** After the Mesopotamia pilot enrichment, rewrite `civ-ancient-egypt` to the full enriched template and promote status to **`fact-library`**.

**Notes:** Kept prior three sources (Shaw 2000; Wilkinson 1999; Midant-Reynes 2000) and registered twelve additional verified sources (Kemp 2006; Bard 2015; Trigger et al. 1983; Lehner 1997; Wengrow 2006; Butzer 1976; Allen 2014; Petrie Royal Tombs 1900–1901 P; Quibell Hierakonpolis 1900 P; Quibell & Green 1902 P; Hoffman 1979; Edwards 1993) — **15** `src-*` total. Depth focus: Predynastic → Early Dynastic → Old Kingdom (geography/Nile; chronology table; Abydos, Hierakonpolis, Memphis, Saqqara, Giza carefully; state formation; hieroglyphs; economy; material culture; contacts; research history). Narmer / unification kept as process + contested iconography in Notes — not a single-event fact. No invented page numbers; no forged images. Integrity > speed.

### D-2026-10-11-13 — Andes (Caral–Norte Chico) deepened to fact-library

**Decision:** After Mesopotamia and Egypt enrichments, rewrite `civ-andes` to the full enriched template and promote status to **`fact-library`**.

**Notes:** Kept prior four sources (Shady/Haas/Creamer *Science* 2001; Haas/Creamer/Ruiz *Nature* 2004; Shady & Leyva 2003; Shady 1997) and registered eleven additional verified sources (Creamer/Ruiz/Haas Pativilca *Fieldiana* 2007 P; Creamer et al. Fortaleza *Fieldiana* 2013 P; Haas et al. *PNAS* maize 2013; Moseley & Willey Aspero 1973; Moseley maritime foundations 1975; Raymond reconsideration 1981; Haas & Creamer in Silverman 2004; Feldman in Haas/Pozorski/Pozorski 1987; Quilter Paloma 1989 comparative; Burger Chavín 1995 later orientation; UNESCO Caral-Supe listing 2009 T) — **15** `src-*` total. Depth focus: Norte Chico Late Archaic geography; chronology table; Caral, Aspero, Caballete, Huaricanga and valley testing; monumental architecture (platform mounds, sunken circular plazas, *shicra*, *huancas*); aceramic / no attested writing; irrigation + contested maritime model + maize multi-proxy evidence; intra-regional coast–valley interaction only; research history. City vs ceremonial center / state vs complex society / maritime foundations / maize staple intensity kept in Notes. Scope excludes later Andean empires. No invented page numbers; no forged images. Integrity > speed.

### D-2026-10-11-14 — Indus Valley deepened to fact-library (Mesopotamia/Egypt/Andes-matched)

**Decision:** After Mesopotamia, Egypt, and Andes enrichments, rewrite `civ-indus-valley` to the full enriched template and promote status to **`fact-library`**.

**Notes:** Kept prior six sources (Kenoyer 1991; Wright 2010; Kenoyer 2014 Cambridge chapter; Possehl 2002; Marshall 1931 P; Meadow ed. 1991 P) and registered nine additional verified sources (Kenoyer 1998 synthesis; Mackay 1938 Mohenjo-daro continuation P; Vats 1940 Harappa P; Parpola 1994 script corpus — decipherment proposal not adopted as fact; Giosan et al. *PNAS* 2012 fluvial landscapes; Rao 1979 Lothal ASI memoir P; Ratnagar 2004 trade; UNESCO Moenjodaro listing 1980 T; Wheeler 1968 research-history foil) — **15** `src-*` total. Depth focus: Greater Indus geography (Indus / Ghaggar-Hakra; monsoon-fed vs glacier-fed debate); Kenoyer Table I chronology; Mohenjo-daro, Harappa, Ganweriwala, Rakhigarhi and settlement tiers; irregular net plan / wells-drains / speculative Great Bath labels; undeciphered script + weights/sealings; subsistence and crafts; Meluhha / Gulf contacts; research history. Script undeciphered, empire vs city-network, Lothal “dock,” and climate–deurbanization kept in Notes. No invented page numbers; no forged images. Integrity > speed.

### D-2026-10-11-15 — China Bronze overview + Sanxingdui deepened to fact-library (Mesopotamia/Egypt/Andes/Indus-matched)

**Decision:** After the Indus enrichment, rewrite both `civ-china-bronze` and `civ-sanxingdui` to the full enriched template and promote both to **`fact-library`**.

**Notes (China Bronze overview):** Kept prior four sources (Thorp 1991; Liu & Chen 2003; Flad & Chen 2013; Bagley 1987) and registered ten additional verified sources (Liu & Chen 2012 Cambridge *Archaeology of China*; Campbell 2014 Cotsen Erlitou→Anyang; Keightley 1978 oracle bones; Chang 1980 *Shang Civilization*; Thorp 2006 Early Bronze Age; Li Chi 1977 *Anyang*; Loewe & Shaughnessy 1999 / Bagley Shang Archaeology chapter; Underhill 2013 / Xu Hong Erlitou Culture chapter; XSZCP 2000 brief — contested chronology scheme; Rawson ed. 1996 BM catalogue) — **14** `src-*` total. Depth focus: Central Plains geography and resource procurement; Erlitou/Erligang/Xiaoshuangqiao–Huanbei/Anyang period table; key sites; urbanism and institutions; oracle-bone writing; subsistence and piece-mold casting; ritual bronzes; Yangzi/northern-frontier interaction; research history. **Xia historicity and XSZCP absolute bands kept in Notes only.** No invented page numbers; no forged images.

**Notes (Sanxingdui):** Kept prior four sources (Sichuan 1999 P; Ge & Linduff 1990; Bagley 1988; Li et al. 2022) and registered ten additional verified sources (Bagley ed. 2001 *Ancient Sichuan*; Xu 2001 bronze chapter; Flad 2018 urbanism-as-technology; Flad 2012 valuable objects; Sun Hua 2003 culture definition; Wu/Ran/Lei 2021 Pit 4 radiocarbon; UNESCO Tentative List 5816 T; Zhao 2021 NSR highlight; plus cross-cites of Flad & Chen 2013 and Rawson 1996) — **14** `src-*` total. Depth focus: Chengdu Plain geography; site span / culture phases / pit chronology table; Pits 1–8 and Jinsha comparative; ritual center and Flad urbanism model; no oracle-bone-scale local archive; ritual economy and casting; masks/trees/gold; Central Plains contact ≠ same kingdom; research history. **Sanxingdui–Shang polity identity and pit absolute chronology debates kept in Notes only.** Integrity > speed.

### D-2026-10-11-16 — Aegean + Olmec + Early Maya deepened to fact-library (first-batch enrichment complete)

**Decision:** After China Bronze / Sanxingdui enrichments, rewrite `civ-aegean`, `civ-olmec`, and `civ-early-maya` to the full enriched template and promote all three to **`fact-library`**. With this commit, **all nine** first-batch civilization entries are at `fact-library` depth.

**Notes (Aegean):** Kept prior eight sources and registered six additional verified sources (Renfrew 1972; Warren & Hankey 1989; Chadwick 1976; Doumas 1983 Akrotiri; Wace 1949 Mycenae P; Cline ed. 2010 Oxford Handbook) — **14** `src-*` total. Depth focus: Cyclades / Minoan Crete / Mycenaean mainland geography; period table (high vs low chronology labeled); Knossos, Mycenae, Pylos, Akrotiri, Early Cycladic groups; palatial urbanism; Linear A undeciphered / Linear B Mycenaean Greek; economy and crafts; contacts via Egypt synchronism debate; research history. Thalassocracy and absolute chronology kept in Notes. No invented page numbers; no forged images.

**Notes (Olmec):** Kept prior six sources and registered seven additional verified sources (Drucker 1952 La Venta P; Drucker/Heizer/Squier 1959 La Venta P; Cyphers 2004 sculpture catalog; Clark & Pye 2000 NGA volume; Benson & de la Fuente 1996 / González Lauck; Blomster et al. 2005 *Science* pottery INAA; Taube 2004 Dumbarton Oaks) — **13** `src-*` total. Depth focus: Gulf heartland geography; Formative chronology table; San Lorenzo, La Venta, Chalcatzingo; monumental urbanism; no asserted deciphered script; subsistence/craft and export-pottery model; external contacts; research history. Mother vs sister cultures and Diehl title primacy kept in Notes. Integrity > speed.

**Notes (Early Maya):** Kept prior five sources and registered seven additional verified sources (Saturno/Stuart/Beltrán 2006 San Bartolo *Science*; Clark & Hansen 2001 early kingship/MFC; Demarest 2004; Inomata et al. 2019 Ceibal plateaus *PLOS ONE*; Coe & Houston 2015; Hansen 1998 Nakbe; Willey et al. Seibal Peabody series P) — **12** `src-*` total. Depth focus: lowland geography; Preclassic–Early Classic period table; Ceibal, Nakbe, El Mirador, Cival, San Bartolo; E-Groups and artificial plateaus; Late Preclassic writing; subsistence; Olmec interaction as debate; research history. Classic collapse out of scope. Integrity > speed.

### D-2026-10-11-17 — Product core = archive + read API (encyclopedia prose is presentation)

**Decision:** After Council session [`delib-2026-10-11-archive-api-direction`](../deliberations/delib-2026-10-11-archive-api-direction.md), the product core is a **digital archive + read API**, not blog/encyclopedia pages alone. Bilingual civilization Markdown remains a valuable **editorial / presentation** layer and may continue to thicken, but enrichment must **feed structured archive records** (Source, Site, Period, Assemblage/Object with rights, Claim fact-vs-hypothesis, Media rights-cleared only, Deliberation). API list/filter/get those entities; every item carries `sources[]`; hypotheses never auto-promote.

**Immediate next (testable):** JSON Schema and/or SQLite DDL; export pipeline from MD + sidecars with citation fail-closed; OpenAPI archive paths (`/sites`, `/periods`, `/objects`, `/claims`, `/media`); one pilot civilization fully structured (prefer `civ-mesopotamia`). Cloud deliberation stays spec-first (D-2026-10-11-2 unchanged). No forged artifact images.

**Notes:** Refines D-2026-10-11-4 — git Markdown remains published editorial authority; gated `export/` becomes the API serving form (no silent dual-write). Architecture: Archive layer section. API: §4.6. OpenAPI bumped for archive collections.

### D-2026-10-11-18 — Schema drafts + Mesopotamia structured pilot started

**Decision:** Implement FUTURE_WINDOW items from [`delib-2026-10-11-archive-api-direction`](../deliberations/delib-2026-10-11-archive-api-direction.md) / D-2026-10-11-17: land JSON Schema drafts under [`schemas/`](../schemas/), bilingual data-model docs [`archive-data-model.md`](archive-data-model.md), structured pilot at [`data/structured/mesopotamia/`](../data/structured/mesopotamia/), and citation fail-closed checker [`tools/export_check.py`](../tools/export_check.py).

**Notes:** Pilot JSON is derived **only** from `civ-mesopotamia.md` + registered `src-mesopotamia-*`. No new archaeological claims; no forged images; hypothesis claims labeled. OpenAPI archive paths already sketched (§4.6); docs now point at schemas + pilot. Run: `.venv/bin/python tools/export_check.py`.

### D-2026-10-11-19 — Read-only archive API + Egypt structured pack

**Decision:** Implement D-2026-10-11-17 / FUTURE_WINDOW: ship a local **read-only** HTTP API (FastAPI) serving all packs under `data/structured/*`; add Egypt structured pack [`data/structured/egypt/`](../data/structured/egypt/); extend [`tools/export_check.py`](../tools/export_check.py) to validate **all** packs.

**Notes:**
- API: `python -m api.serve` (default bind `127.0.0.1:8080`). Routes: `/api/v1/healthz`, `/civilizations`, `/sources`, `/sites`, `/periods`, `/objects`, `/claims`, `/media`. Pagination v0: `limit`+`offset`. No write routes. Claim responses expand `sources` refs; hypotheses stay `kind: hypothesis`.
- Egypt pack derived **only** from `civ-ancient-egypt.md` + `src-egypt-*` (15 sources · 6 sites · 6 periods · 4 assemblages · 10 claims incl. Narmer single-unification hypothesis · 2 outbound media). No new archaeological inventions; no forged images.
- Markdown remains editorial source of truth; structured JSON is the gated serveable form (no silent dual-write).


### D-2026-10-11-20 — Remaining seven civilizations structured into archive packs for API

**Decision:** After the Mesopotamia / Egypt pilots, land structured packs for the other seven `fact-library` civilizations so the read-only API lists all nine: `andes`, `indus`, `china-bronze`, `sanxingdui`, `aegean`, `olmec`, `early-maya` (plus existing `mesopotamia`, `egypt`).

**Notes:**
- Each pack’s JSON is derived **only** from the matching `civ-*.md` + registered `src-*`; contested items are `kind: hypothesis`; no forged artifact images; media is outbound-link metadata only.
- Seed definitions: `tools/pack_seeds/*.json`; writer: `tools/write_packs_from_seeds.py`.
- `tools/export_check.py` passes citation fail-closed for all 9 packs. API smoke: `GET /api/v1/civilizations` returns 9.
- Markdown remains editorial source of truth; structured JSON is the gated serveable form.

### D-2026-10-11-21 — Mesopotamia archive density (sites + primary sources)

**Decision:** Per owner priority, deepen the Mesopotamia pilot: register verifiable site-level excavation/survey reports (P) and strong secondaries (S); expand structured sites/assemblages/claims; sync `civ-mesopotamia.md` Key sites and Sources.

**This pass (bibliographic details verified via WebSearch/catalog pages; access_date 2026-10-11; no invented page numbers/coordinates/forged images):**

Major **P**: Nippur OIP 78/97; Tell Asmar OIP 43; Khafajah OIP 53; OIC 13; Matthews Jemdet Nasr 2002; Mackay Kish 1925; Safar et al. Eridu 1981; Hall & Woolley al-‘Ubaid 1927; Parrot Mari Ishtar 1956; Postgate Abu Salabikh ASE 1 1983.

Major **S**: Parrot Tello 1948; Moorey Kish 1978; Martin Fara 1988; Adams Diyala 1965; Strommenger Habuba Kabira 1980.

**Structured pack:** sources 15→31; sites 7→17; objects 4→16; claims 10→23; `tools/export_check.py` passes all packs.

**Notes:** Girsu/Tello vs Tell al-Hiba kept distinct; Habuba recorded as excavated Uruk-related town fact; Algaze expansion remains hypothesis. Integrity over speed.

### D-2026-10-11-22 — Egypt archive density (sites + primary sources)

**Decision:** Per owner priority (Mesopotamia-style D-21), deepen the Egypt structured pack: register verifiable Predynastic–Old Kingdom site-level excavation reports (P) and sync `civ-ancient-egypt.md` Key sites / Sources.

**This pass (bibliographic details verified via WebSearch/catalog pages; access_date 2026-10-11; no invented page numbers/coordinates/forged images):**

Major **P**: Petrie & Quibell *Naqada and Ballas* 1896; Petrie *Abydos* I 1902; Randall-MacIver & Mace *El Amrah and Abydos* 1902; Petrie *Tarkhan I and Memphis V* 1913; Petrie *Tarkhan II* 1914; Petrie *Medum* 1892; Reisner *Mycerinus* 1931; Firth & Quibell *Step Pyramid* 1935; Emery *Great Tombs* III 1958; Kaiser et al. Elephantine MDAIK 26 1970; von der Way *Buto I* AV 83 1997; Adams HK6 BAR S903 2000; Saad *Excavations at Helwan* 1969 (excavator synthesis).

**Structured pack:** sources 15→28; sites 6→13; objects 4→16; claims 10→24; `tools/export_check.py` passes all packs.

**Notes:** Memphis remains handbook-level political-center orientation (precision pinpoint = hypothesis); Ballas Predynastic cemeteries not conflated with later Deir el-Ballas palace; Giza workforce counts not invented; Saqqara First Dynasty tombs kept distinct from Abydos royal tombs. Integrity over speed.

### D-2026-10-11-23 — Indus Valley archive density (sites + primary sources)

**Decision:** Per owner priority (Mesopotamia D-21 / Egypt D-22 pattern), deepen the Indus structured pack: register verifiable site-level excavation/survey reports (P/S) and sync `civ-indus-valley.md` Key sites / Sources.

**This pass (bibliographic details verified via WebSearch/catalog pages; access_date 2026-10-11; no invented page numbers/coordinates/forged images):**

Major **P**:
- Bisht *Excavations at Dholavira* 2015 (ASI **draft**/website release; under publication)
- Lal et al. Kalibangan Early Harappans MASI 98 (2003); Lal et al. Kalibangan Harappans MASI 110 (2015/2020)
- Mackay *Chanhu-daro Excavations, 1935–36* 1943 (AOS)
- Khan “Excavations at Kot Diji,” *Pakistan Archaeology* 2 (1965)
- Casal *Fouilles d’Amri* 1964
- Joshi *Excavations at Surkotada* MASI 87 (1990)
- Nath *Excavations at Rakhigarhi* (1997–2000 seasons; ASI **draft**)
- Shinde et al. Rakhigarhi cemetery *PLoS ONE* 2018 (DOI 10.1371/journal.pone.0192299)
- Jarrige et al., eds., *Mehrgarh: Field Reports 1974–1985* 1995

Major **S**: Mughal “Recent Archaeological Research in the Cholistan Desert” in Possehl 1982; Mughal *Ancient Cholistan* 1997 (Ganweriwala / Hakra survey).

**T**: UNESCO Dholavira listing 2021 (WHC 1645).

**Structured pack:** sources 15→28; sites 6→12; objects 4→16; claims 8→23; media 2→5; `tools/export_check.py` passes all packs.

**Notes:** Bisht/Nath cited as drafts; Ganweriwala remains survey-only (no invented trench inventory); Rakhigarhi “eastern capital,” Kot Diji conquest/conflagration, Lothal dock, climate single-cause, empire-vs-network kept as hypotheses. Integrity over speed.

### D-2026-10-11-24 — Andes / Caral–Norte Chico archive density (sites + primary sources)

**Decision:** Per owner priority (Mesopotamia D-21 / Egypt D-22 / Indus D-23 pattern), deepen the Andes structured pack: register verifiable site-level excavation/survey literature (P/S) for Caral, Aspero, and other Supe/Pativilca/Fortaleza/Huaura sites when citeable, and sync `civ-andes.md` Key sites / Sources.

**This pass (bibliographic details verified via WebSearch/catalog/journal pages; access_date 2026-10-11; no invented page numbers/coordinates/forged images):**

Major **P**:
- Willey & Corbett *Early Ancón and Early Supe Culture* 1954 (incl. Aspero; historical dating outdated)
- Feldman *Aspero…* Harvard Ph.D. 1980
- Existing Creamer et al. Fieldiana Pativilca 2007 / Fortaleza 2013 (this pass splits Porvenir, Shaura, Cerro Blanco into site records)
- Chu Barrera *Household Organization… Bandurria* Pittsburgh Ph.D. 2011
- Zechenter *Subsistence Strategies in the Supe Valley…* UCLA Ph.D. 1988

Major **S**: Feldman 1985 (Donnan ed.); Fung 1988 (Keatinge ed.); Chu 2006 *Boletín de Arqueología PUCP* 10; Quilter et al. 1991 *Science* (El Paraíso, comparative); Sandweiss et al. 2009 *PNAS* (environmental demise = hypothesis); Kosok 1965; Engel 1987; Haas & Creamer 2006 *Current Anthropology*; Shady 2008 PEACS synthesis PDF (“oldest” = marketing, not ranking).

**Structured pack (andes):** sources 15→28; sites 6→14; objects 3→16; claims 7→27; media 1→6; periods 5→7; `tools/export_check.py` passes all packs.

**Notes:** Chupacigarro (West) kept separate from Caral; Vichama only as PEACS list pointer (often Early Formative, after Caral monumental window); environmental abrupt demise, Aspero chiefdom, Bandurria challenge to chiefdom/state, maize staple intensity, and “oldest civilization” kept as hypotheses. Integrity over speed.

### D-2026-10-11-26 — Design taste (seen and unseen)

**Decision:** Adopt an explicit craft standard for this repository: product = **archive + read-only API**; prose and `/ui` are presentation. Principles adapted from Paul Graham’s *Taste for Makers* and Jobs-style “quality in what is seen and unseen”: simple, solves the right problem, hard work that looks easy, consistency, restraint, honesty (fact ≠ hypothesis must be obvious in UI), no decorative lies, no forged artifact imagery.

**Ship with this decision:**
- [`design-taste.md`](design-taste.md) / [`design-taste.zh.md`](design-taste.zh.md) — principles + checklists for README, API envelopes, `/ui`, docs
- Browse UI at **`/ui`** (`api/static/ui.html`) — bilingual, dark/light via `prefers-color-scheme`, claim kind badges, expandable sources, no artifact stock photos
- API root `/api/v1/` principle-first message + `browse_ui: /ui`
- README “Why not Wikipedia” + “Try the API / UI” (honest, not fluff)

**Notes:** Inspiration pointer (public compilation): https://x.com/Jaden_riku/status/2108876904002670873 — credit Graham’s essay; do not paste copyrighted text wholesale. Parallel densify work may continue on `data/structured/*`; this decision does not invent archaeology.

### D-2026-10-11-25 — China Bronze + Sanxingdui archive density (sites + primary sources)

**Decision:** Per owner priority (Mesopotamia D-21 / Egypt D-22 / Indus D-23 / Andes D-24 pattern), deepen **both** china-bronze and sanxingdui structured packs: register verifiable site-level excavation reports/briefs (P) and strong secondaries (S), expand sites/objects/claims, and sync `civ-china-bronze.md` / `civ-sanxingdui.md`.

**This pass (bibliographic details verified via WebSearch/catalog pages; access_date 2026-10-11; no invented page numbers/coordinates/forged images):**

Major **P** (China Bronze): Erlitou 1959–1978 (1999); Erlitou 1999–2006 (2014, 5 vols.); Yanshi Shang City Vol. 1 (2013); Zhengzhou Erligang (1959); Zhengzhou Shang City 1953–1985 (2001); Xiaoshuangqiao 1990–2000 (2012); Huanbei Palace Foundations 1–2 briefs (*Kaogu* 2003/2010); Yinxu 1958–1961 (1987); Panlongcheng 1963–1994 (2001); Yuanqu Shang City (1) 1996 / (2) 2014.

**S/T** (China Bronze): CASS *Chinese Archaeology: Xia–Shang Volume* 2003; UNESCO Yin Xu 2006 (WHC 1114).

Major **P** (Sanxingdui/Jinsha): Pit 1–2 *Wenwu* briefs 1987/1989 (+ existing 1999 monograph); Graham 1934 Hanchow/Yueliangwan preliminary report; East City Wall 2016 brief (*Sichuan Cultural Relics* 2024); Jinsha Meiyuan 2004 brief; Jinsha Materials Vol. 1 2013; Jinsha sacrificial-zone report 2022 (5 vols.).

**S** (Sanxingdui): Chen Xiandan 1990; Ma Jixian 1993 Yueliangwan memoir; Jinsha 2006 popular synthesis (orientation only).

**Structured packs:**
- **china-bronze:** sources 14→28; sites 4→12; objects 3→16; claims 6→24; periods 5→7; media 0→1
- **sanxingdui:** sources 14→28; sites 4→10; objects 3→16; claims 6→23; periods 5→7; media 1→1
- `tools/export_check.py` passes all packs.

**Notes:** Xia historicity, Erlitou=Xia capital, Zhengzhou/Yanshi/Huanbei textual royal-seat IDs, Panlongcheng as Shang outpost, Sanxingdui=Shang polity, Sanxingdui→Jinsha simple relocation, and fully formed “Ancient Shu State” kept as hypotheses. Integrity over speed.

