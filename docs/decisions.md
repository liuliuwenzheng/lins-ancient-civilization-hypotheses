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

### D-2026-10-11-27 — Aegean + Olmec + Early Maya archive density deepen (completes first pass across 9 packs)

**Decision:** Per owner priority (aligned with Mesopotamia D-21 / Egypt D-22 / Indus D-23 / Andes D-24 / China-bronze+Sanxingdui D-25), deepen aegean, olmec, and early-maya packs: register verified site-level excavation reports (P) and strong secondary (S), expand structured sites/objects/claims, sync corresponding `civ-*.md`. This completes the **first** density pass across all nine civilization packs.

**This round (bibliographic identity verified via WebSearch/catalogs/journal pages; access_date 2026-10-11; no invented pages/coords/forged images):**

**Aegean major P:** Lang Pylos frescoes 1969; Blegen et al. Vol. III 1973; Shaw Kommos I 1995; Betancourt II 1990; Watrous III 1992; Platon Zakros 1971; Iakovidis Gla II 1998.

**Olmec major P:** Stirling BAE 138; Weiant 139; Drucker 140; Pool Tres Zapotes 2003; Ortiz & Rodríguez El Manatí; Symonds/Cyphers San Lorenzo settlement; Rust & Sharer 1988 Science.

**Early Maya major P:** Inomata et al. Nature 2020 Aguada Fénix; PNAS 2015 Ceibal; Hammond Cuello 1991; Laporte & Fialko 1995 Mundo Perdido; Ricketson/Smith Uaxactún; Matheny NWAF Tigre; Hansen basin reports; Healy Cahal Pech; Garber Blackman Eddy.

**Structured results:**
- **aegean:** sources 14→28; sites 4→14; objects 3→16; claims 6→24; periods 5→7; media 1→4
- **olmec:** sources 13→28; sites 3→12; objects 3→16; claims 5→24; periods 3→4; media 1→4
- **early-maya:** sources 12→28; sites 5→14; objects 3→16; claims 6→26; periods 4→5; media 1→4
- `tools/export_check.py` passes all packs.

**Note:** Contested models stay hypotheses. Integrity over speed. First density pass across all nine packs complete.


### D-2026-10-11-28 — Mesopotamia + Egypt second archive density pass

**Decision:** After the first density pass (D-21 / D-22), deepen Mesopotamia and Egypt packs again with **site-level primary / strong secondary** publications only: verified reports and stable URLs; more sites, assemblages, and fact claims; contested readings stay hypotheses; sync Key sites + Sources in `civ-mesopotamia.md` / `civ-ancient-egypt.md`; full-repo `export_check` must pass. Integrity over speed.

**Major new P (and needed S):**

**Mesopotamia:** Speiser Gawra I 1935; Tobler Gawra II 1950; Lloyd & Safar Tell Uqair JNES 1943; Wilson Adab OIP 138 2012 (+ Banks 1912 S); Delougaz & Lloyd OIP 58 (Tell Agrab); Oates Choga Mami 1969; Andrae Assur Ishtar 1922; Mallowan Brak 1947; Hrouda Isin I 1977.

**Egypt:** Brunton & Caton-Thompson Badarian 1928; Brunton Qau and Badari I 1927; Petrie Gerzeh 1912; Petrie Diospolis Parva 1901; Mond & Myers Armant 1937; Brunton Mostagedda 1937; de Morgan Dahchour 1895; Borchardt Sahure plates 1913; Tell el-Farkha I 2012; Rizkana & Seeher Maadi 1987–1990.

**Structured results (`export_check`):**
- **mesopotamia:** sources 31→41; sites 17→25; objects 16→24; claims 23→32
- **egypt:** sources 28→38; sites 13→24; objects 16→26; claims 24→35
- Other seven packs unchanged; citation gate green.

**Notes:** Brak-as-Uruk-colony and simple Tasian-before-Badarian stay hypotheses; no invented coordinates/museum numbers/forged images; READMEs avoid hardcoded live counts (trust `export_check`).

### D-2026-10-11-29 — Indus + Andes second archive density pass

**Decision:** After the first density passes (D-23 / D-24), deepen the Indus and Andes structured packs again with **site-level primary / strong secondary** sources only: verified excavation reports and stable URLs; expand sites, assemblages, and claims; contested items → hypothesis column; sync `civ-indus-valley.md` / `civ-andes.md` Key sites & Sources; full-repo `export_check` must pass. Integrity over speed.

**Major new P (and necessary S) this round:**

**Indus:**
- Majumdar *Explorations in Sind* ASI Memoir 48 (1934) (Archive)
- Hargreaves *Excavations in Baluchistan* ASI Memoir 35 (1929) — Nāl / Mastung
- Francfort & Pottier Shortughaï preliminary, *Arts asiatiques* 34 (1978) (Persée); Francfort *Fouilles de Shortughaï* 1989
- Durrani Rehman Dheri, *Ancient Pakistan* 6 (1988)
- Jarrige Nausharo, *Pakistan Archaeology* 24 (1989); CRAI 1996 synthesis (S)
- Wheeler Harappa 1946, *Ancient India* 3 (1947) (historical P; url null if no stable open PDF)
- Dales Balakot, *JFA* 1 (1974), DOI 10.1179/jfa.1974.1.1-2.3
- Stein Ghaggar–Hakra / ‘Sarasvati’ survey, *Geographical Journal* 99 (1942), DOI 10.2307/1788862

**Andes:**
- Bird *Huaca Prieta* AMNH Anthropological Papers 62(1) (1985)
- Grieder et al. *La Galgada* (1988) UT Press
- Pozorski & Pozorski *Early Settlement… Casma Valley* (1987); Sechín Alto chapter (2002, S)
- Fuchs et al. Sechín Bajo, *Boletín de Arqueología PUCP* 13 (2009)
- Vega-Centeno Cerro Lampay, *Latin American Antiquity* 21 (2010); PUCP 2006 (S)
- Engel Asia Unit I, APS *Transactions* 53(3) (1963)
- Benfer Paloma, *Latin American Antiquity* 1 (1990) (S); Moseley maritime retrospect, *Andean Past* 3 (1992) (S, hypothesis)

**Structured results (`export_check`):**
- **indus:** sources 28→38; sites 12→20; objects 16→24; claims 23→33
- **andes:** sources 28→38; sites 14→22; objects 16→24; claims 27→36
- Other seven packs unchanged; full-repo gate passes.

**Notes:** Shortughaï “colony,” Balakot Gulf-trade node, Casma/Norte Chico “earliest” rankings, and maritime-foundations stay in the hypothesis column; Casma and Chicama/Asia sites are **comparative baselines**, not merged into one Norte Chico polity; no invented coordinates/catalog numbers/forged images; README counts defer to `export_check`.

### D-2026-10-11-30 — China Bronze + Sanxingdui + Aegean + Olmec + Early Maya second archive density pass

**Decision:** After the first density passes (D-25 / D-27), deepen the remaining five structured packs again with **site-level primary / strong secondary** sources only: verified excavation reports and stable URLs; expand sites, assemblages, and claims; contested items → hypothesis column; sync each `civ-*.md` Key sites & Sources; full-repo `export_check` must pass. Integrity over speed. This completes density pass 2 across all nine packs.

**Major new P (and necessary S) this round:**

**China Bronze:** Fu Hao tomb 1980; Taosi 1978–1985 (2015) + 1999–2001 (2025); Xingan Dayangzhou 1997; Wucheng 2005; Fengxi 1962; Huayuanzhuang East oracle bones 2003; Tonglüshan 1999; Houma foundry 1993; Shaughnessy 1991 (S).

**Sanxingdui:** Baodun 2009–2010 brief; Jiang Zhanghua 2022 (S); Shi’erqiao / Renshengcun / Qingguanshan / Cangbaobao / Jinsha Lanyuan field-literature pointers; Flad & Chen 2013 Chengdu Plain framing (pack-local).

**Aegean:** Pendlebury 1939; Cadogan 1976; Driessen & Macdonald 1997; Hawes Gournia 1908; Cummer & Schofield Keos III 1984; Palaikastro BSA series; Marinatos Thera seasons; Taylour 1983; Hope Simpson 1981; Wiener chronology pointer (S).

**Olmec:** Cascajal Science 2006 + Mora-Marín 2020; Teopantecuanitlán; Manatí 1988 prelim; San Andrés / Llano del Jícaro / Arroyo Pesquero (provenience caveat) / El Remolino / Ojochi.

**Early Maya:** Forsyth Nakbe 1993; Estrada-Belli Cival 2006; Willey Belize Valley 1965; Kosakowsky Cuello 2003; Cerros / Lamanai / Yaxuná FAMSI 1988 / Holmul; Hansen et al. Mirador–Calakmul LiDAR 2022.

**Structured results (`export_check`):**
- **china-bronze:** sources 28→38; sites 12→20; objects 16→24; claims 24→34
- **sanxingdui:** sources 28→38; sites 10→18; objects 16→23; claims 23→31
- **aegean:** sources 28→38; sites 14→23; objects 16→24; claims 24→32
- **olmec:** sources 28→38; sites 12→19; objects 16→24; claims 24→31
- **early-maya:** sources 28→38; sites 14→22; objects 16→24; claims 26→33
- Full-repo gate passes.

**Notes:** Taosi=Yao capital, Xingan=Shang vassal capital, Qingguanshan=royal palace, Baodun linear ancestor-state, Theran eruption as sole LM IB cause, single high/low calendar year, Cascajal “oldest writing” without caveat, Arroyo Pesquero as closed excavated assemblage, Mirador “first state,” and full Middle Preclassic divine kingship stay hypotheses. No invented coordinates/catalog numbers/forged images; README counts defer to `export_check`.


### D-2026-10-12-1 — Mesopotamia + Egypt third archive density pass

**Decision:** Continue owner priority to deepen archive density. Add a **third** verified density pass for Mesopotamia and Egypt: primary (P) and strong secondary (S) excavation reports / corpora not already registered; expand structured sites, assemblages, and claims; sync Key sites + Sources in `civ-mesopotamia.md` / `civ-ancient-egypt.md`; full-repo `export_check` must pass. Integrity over speed.

**Major new P (and needed S):**

**Mesopotamia:**
- Woolley *Ur Excavations* II *The Royal Cemetery* (1934); *UE* V *The Ziggurat and Its Surroundings* (1939)
- Gibson et al. *Excavations at Nippur: Twelfth Season* OIC 23 (1978)
- Loud *Khorsabad* Part 1 OIP 38 (1936); Loud & Altman *Khorsabad* Part 2 OIP 40 (1938)
- Green & Nissen ZATU / ATU 2 (1987); Legrain *UE* III archaic seal-impressions (1936)
- Mallowan *Nimrud and Its Remains* (1966); Oates & Oates *Nimrud* (2001, S)
- Hansen “Al-Hiba, 1968–1969,” *Artibus Asiae* 32/4 (1970)
- Koldewey *The Excavations at Babylon* (1914 Eng.); Layard *Discoveries… Nineveh and Babylon* (1853, historical P)
- Weiss et al. Tell Leilan 1985 season, *AJA* 94/4 (1990); de Genouillac *Fouilles de Telloh* I (1934)

**Egypt:**
- Petrie *Abydos* Part II (1903); Reisner *Naga-ed-Dêr* Part I (1908)
- Emery *Great Tombs of the First Dynasty* II (1954); Emery *Archaic Egypt* (1961, S)
- Dreyer *Umm el-Qaab* I tomb U-j (1998); Quibell *El Kab* (1898)
- Garstang *Mahâsna and Bêt Khallâf* (1903); Petrie *Pyramids and Temples of Gizeh* (1883)
- Junker *Gîza* I (1929); Naville *Temple of Deir el Bahari* Part I (1895)
- Petrie *Illahun, Kahun and Gurob* (1891)

**Structured results (`export_check`):**
- **mesopotamia:** sources 41→55; sites 25→31; objects 24→37; claims 32→46
- **egypt:** sources 38→49; sites 24→31; objects 26→36; claims 35→46
- Other seven packs unchanged; citation gate green.

**Notes:** Tell Leilan climate-collapse and U-j “earliest writing” rankings stay hypotheses; Layard/Koldewey are historical P (not modern stratigraphy); no invented coordinates/museum numbers/forged images; README counts defer to `export_check`.

### D-2026-10-12-2 — Third archive density pass for remaining seven packs

**Decision:** After Mesopotamia + Egypt pass 3 (D-2026-10-12-1), apply the **same third** verified density pass to the other seven packs: verified P/S only; expand sites/assemblages/claims; contested → hypothesis; sync each `civ-*.md` Key sites + Sources; full-repo `export_check` must pass. Integrity over speed.

**Major new P (and needed S):**

**Andes:** Samaniego et al. Cerro Sechín (1985); Pozorski Antiquity 1992 / square-room 2011; Burger & Salazar-Burger Huaricoto; Izumi Kotosh Andes 2/4; Sandweiss Jaguay / Keefer Tacahuay Science 1998; Dillehay Monte Verde II; Donnan 1985 volume (S)

**Indus:** Bisht Banawali 1982/1984; Possehl & Raval Rojdi 1989; Rao Lothal vol. 2 1985; Jansen/Urban Mohenjo-Daro interim; Kenoyer bead/trade 1997; Fairservis 1961; Allchin 1968; Possehl Ancient Cities 1979; Shaffer 1992

**China Bronze:** Zhouyuan CHAR 2017 / Fengchu No. 3 brief; Liulihe Yan cemetery 1995; Tianma–Qucun; Sufutun; Xiaomintun foundry; Guicheng; Qianzhangda

**Sanxingdui:** Yufu/Jiangzhang Baodun; pits 3–8 official briefs; Fangchijie; Meiyuan/Shi'erqiao deepened; CPAS; Lin 2019 Jinsha craft

**Aegean:** Caskey Hesperia Lerna; Wiencke Lerna IV; Banks Lerna VII; Blegen Troy I; Popham Lefkandi I/II; Atkinson Phylakopi 1904; Furumark; Manning PLOS 2022

**Olmec:** Stirling BAE 157; Cyphers El Azuzul; Etlatongo; Tres Zapotes/Chalcatzingo deepened; Bernal 1969; Coe Mexico 8th ed.

**Early Maya:** Matheny NWAF 45; Culbert TR 25A/25B; Coe decipherment history; Martin & Grube; Mirador/San Bartolo/Holmul/Aguada Fénix deepened

**Structured results (`export_check`):**
- **andes:** sources 38→48; sites 22→29; objects 24→32; claims 36→45
- **indus:** sources 38→48; sites 20→26; objects 24→30; claims 33→41
- **china-bronze:** sources 38→48; sites 20→27; objects 24→31; claims 34→42
- **sanxingdui:** sources 38→48; sites 18→24; objects 23→30; claims 31→39
- **aegean:** sources 38→48; sites 23→28; objects 24→30; claims 32→40
- **olmec:** sources 38→48; sites 19→25; objects 24→31; claims 31→37
- **early-maya:** sources 38→48; sites 22→28; objects 24→31; claims 33→40
- Full-repo gate passes (including Mesopotamia/Egypt pass 3 already on main).

**Notes:** Casma “earliest state,” Indus “empire,” Fengchu “she palace,” Sanxingdui=Shang / Baodun ancestor-state, Thera=sole LM IB cause and single calendar year, Olmec mother-culture and Cascajal “oldest writing,” Mirador “first state,” and Middle Preclassic full divine kingship stay hypotheses. No invented coordinates/museum numbers/forged images; README counts defer to `export_check`.


### D-2026-10-12-3 — Fourth archive density pass for Mesopotamia + Egypt

**Decision:** Continue owner priority on archive density. Apply a **fourth** verified density pass to Mesopotamia and Egypt: register only not-yet-ingested primary (P) and needed strong secondary (S) reports; expand structured sites, assemblages, and claims; sync `civ-mesopotamia.md` / `civ-ancient-egypt.md`; contested → hypothesis; full-repo `export_check` must pass. Integrity over speed.

**Major new P (and needed S):**

**Mesopotamia:**
- Delougaz *Pottery from the Diyala Region* OIP 63 (1952); Frankfort Diyala sculpture OIP 44 (1939)
- Mallowan & Rose Arpachiyah *Iraq* 1935; Mallowan Chagar Bazar second campaign *Iraq* 1937
- Woolley *UE* VI Third Dynasty buildings (1974); *UE* VII Old Babylonian (1976)
- Parrot *Mari* II.1 Palace Architecture (1958); Starr *Nuzi* 1937/1939
- Reuther Babylon Merkes WVDOG 47 (1926); Englund ATU 5 (1994); Zettler Nippur Inanna temple BBVO 11 (1992)

**Egypt:**
- Reisner *Giza Necropolis* I (1942); Caton-Thompson & Gardner *The Desert Fayum* (1934)
- Lauer *La pyramide à degrés* architecture (1936); Petrie *Dendereh, 1898* (1900)
- Borchardt Niuserre funerary complex (1907); Jéquier Pepi II royal tomb I (1936)
- Brunton *Qau and Badari* II (1928); Peet *Cemeteries of Abydos* II (1914)
- Arnold *Pyramid of Senwosret I* (1988); Frankfort Cenotaph of Seti I (1933); Winlock Deir el-Bahri 1911–1931 (1942)

**Structured results (`export_check`):**
- **mesopotamia:** sources 55→66; sites 31→37; objects 37→48; claims 46→58
- **egypt:** sources 49→60; sites 31→37; objects 36→47; claims 46→58
- Other seven packs unchanged; citation gate green.

**Notes:** Nuzi is not a third-millennium southern city; Fayum Neolithic ≠ sole Nile-state cradle; Osireion is New Kingdom. No invented coordinates/museum numbers/forged images; README counts defer to `export_check`.

### D-2026-10-12-4 — Fourth archive density pass for remaining seven packs

**Decision:** After Mesopotamia + Egypt pass 4 (D-2026-10-12-3), apply the **same fourth** verified density pass to the other seven packs: verified P/S only; expand sites/assemblages/claims; contested → hypothesis; sync each `civ-*.md` Key sites + Sources + Research history; full-repo `export_check` must pass. Integrity over speed. Completes density pass 4 across all nine packs.

**Major new P (and needed S):**

**Andes:** Dillehay Huaca Prieta 2017; Bonavia Los Gavilanes 1982; Pozorski Huaynuná 1990; Alva Salinas de Chao 1986; Izumi Shillacoto 1972; Lanning 1967; Moseley Ancestors 2001; Quilter Central Andes 2014; Dillehay Foraging–Farming 2011; Sandweiss 2008 maritime critique

**Indus:** Dales & Kenoyer Mohenjo-daro pottery 1986; Flam Ghazi Shah 1996; Law RIHN provenience 2011; Possehl Indus Age Beginnings 1999; Lal 1997; Fairservis 1971; Allchin Rise 1982; Chakrabarti 1995; Miller technology methods 2007; Kenoyer trade/technology 1997 WA

**China Bronze:** Xiaotunnan oracle bones 1980–83; Yinxu Discoveries and Research 1994; Keightley Ancestral Landscape 2000; Li Feng Landscape and Power 2006; Zhengzhou bronze hoards 1999; Yinxu Bronzes 1985; Guojiazhuang 1998; Rawson Sackler Western Zhou; Bagley CHAC Shang chapter; Underhill craft 2002

**Sanxingdui:** Wenwu Pit 1/2 briefs; pits 3–8 2021 pointer; Jinsha 2006 synthesis / ziliaoji deepen; Bagley Ancient Sichuan Princeton path; Zhao 2006; Flad ARA 2018; Ge & Linduff Antiquity path; UNESCO tentative deepen

**Aegean:** Schliemann Tiryns 1885 / Mycenae 1878; Mylonas Grave Circle B 1972–73; Wace chamber tombs 1932; Seager Pseira 1910; INSTAP Pseira series pointer; Mountjoy Regional Mycenaean 1999; Hood/PRAP secondary pointers

**Olmec:** Coe Jaguar’s Children 1965; Rosenswig 2010; Grove regional perspectives; Cyphers sculpture corpus deepen; Pool settlement pointer; Diehl/Stirling/Drucker/Blomster/Taube deepen paths

**Early Maya:** Willey/Adams Altar de Sacrificios Peabody trilogy; Powis Pacbitun 2019; Awe Cahal Pech E-Group; Coe Tikal handbook; Shook/Carnegie Uaxactun pointer; Rice political geography; Maya Cosmos; Cival/Holmul deepen

**Structured results (`export_check`):**
- **andes:** sources 48→58; sites 29→35; objects 32→38; claims 45→54
- **indus:** sources 48→58; sites 26→32; objects 30→36; claims 41→50
- **china-bronze:** sources 48→58; sites 27→33; objects 31→37; claims 42→51
- **sanxingdui:** sources 48→58; sites 24→30; objects 30→36; claims 39→48
- **aegean:** sources 48→58; sites 28→34; objects 30→36; claims 40→49
- **olmec:** sources 48→58; sites 25→31; objects 31→37; claims 37→44
- **early-maya:** sources 48→58; sites 28→34; objects 31→37; claims 40→49
- Mesopotamia/Egypt unchanged in this commit (already pass-4 on main). Citation gate green.

**Notes:** Contested items (Gavilanes maize priority; Indus empire/decipherment; Xia=Erlitou; Sanxingdui=Shang colony; Homer-as-history / single-year Thera; Olmec mother-culture / Cascajal deciphered; Middle Preclassic full divine kingship / Mirador first state) stay hypotheses. No invented coordinates/museum numbers/forged images; README counts defer to `export_check`.

### D-2026-10-12-5 — Fifth archive density pass for Mesopotamia and Egypt

**Decision:** Continue archive density deepening per owner priority. Apply a **fifth** verified density pass to Mesopotamia and Egypt only: register P (and needed S) not already in the archive; expand structured sites/assemblages/claims; sync `civ-mesopotamia.md` / `civ-ancient-egypt.md`; contested → hypothesis; full-repo `export_check` must pass. Integrity over speed. Remaining seven packs and deliberation are scheduled separately.

**Major new P (and needed S):**

**Mesopotamia:**
- Delougaz, Hill & Lloyd *Private Houses and Graves in the Diyala Region* OIP 88 (1967)
- Frankfort *Stratified Cylinder Seals from the Diyala Region* OIP 72 (1955)
- Adams & Nissen *The Uruk Countryside* (1972)
- Andrae *Die Festungswerke von Assur* WVDOG 23 (1913); *Der Anu-Adad-Tempel in Assur* WVDOG 10 (1909)
- Jacobsen & Lloyd *Sennacherib’s Aqueduct at Jerwan* OIP 24 (1935)
- Lloyd & Safar Tell Hassuna JNES 1945; Gibson *The City and Area of Kish* (1972)
- Frankfort OIC 16 (1933) / OIC 17 (1934) preliminary reports

**Egypt:**
- Peet & Woolley *City of Akhenaten* I (1923); Frankfort & Pendlebury II (1933); Pendlebury III (1951)
- Petrie *Tell el Amarna* (1894); Petrie *Memphis I* (1909)
- Naville *Bubastis* (1891); Naville *Temple of Deir el Bahari* II (1896)
- Brunton *Matmar* (1948); Quibell *Archaic Mastabas* (1923); Mond & Myers *Temples of Armant* (1940)

**Structured results (`export_check`):**
- **mesopotamia:** sources 66→76; sites 37→43; objects/claims expanded accordingly
- **egypt:** sources 60→70; sites 37→43; objects/claims expanded accordingly
- Other seven packs unchanged in this commit; citation gate green.

**Notes:** Jerwan “first aqueduct before Rome,” Hassuna “earliest village,” and Amarna “unique planned capital without precursors” stay hypotheses. No invented coordinates/museum numbers/forged images; README counts defer to `export_check`.

### D-2026-10-12-6 — Fifth archive density pass for remaining seven packs

**Decision:** After Mesopotamia + Egypt pass 5 (D-2026-10-12-5), apply the **same fifth** verified density pass to the other seven packs: verified P/S only; expand sites/assemblages/claims; contested → hypothesis; sync each `civ-*.md` Key sites + Sources + Research history; full-repo `export_check` must pass. Integrity over speed. Completes density pass 5 across all nine packs. Parent will run deliberation next.

**Major new P (and needed S):**

**Andes:** Pozorski Pampa de las Llamas–Moxeke JFA 1986; Pozorski ventilated hearths LAA 1996; Engel El Paraíso 1966; Quilter El Paraíso JFA 1985; Burger Excavaciones Chavín 1998; Rick–Kembel Chavín architecture 1998; Haas–Pozorski Andean State 1987; Tello Chavín 1960; Proulx Nepeña 1985; Nesbitt Caballo Muerto 2012

**Indus:** Fairservis Allahdino 1979/1976; Shaffer Allahdino 1974; Sonawane Bagasra 2003; Bhan Gola Dhoro Antiquity 2005; Meadow & Kenoyer Harappa city wall 1994; Jansen Mohenjo-daro water 1993; Lahiri Finding Forgotten Cities 2005; Vidale Indus crafts 2000; Thapar Kalibangan Expedition 1975

**China Bronze:** Shih Xiaotun architecture 1959; Liang & Gao Houjiazhuang HPKM 1001/1002; YH127 publication path; Luoyang Beiyiao 1999; Chang Archaeology of Ancient China 1986; Allan Shape of the Turtle 1991; CASS Zhou volume 2004; Zou Heng 1980; Xibeigang CASS continuation

**Sanxingdui:** Kaogu 2022 sacrificial area / CHAR 2023; Mangcheng & Pimadu Baodun briefs; museum catalogue paths; Sun Hua Shu syntheses; Flad & Chen Yangzi; UNESCO Tentative List update; 2022 progress overview

**Aegean:** Hood & Taylor Knossos plans 1981; Popham Unexplored Mansion 1984; Blegen Troy III–IV; Wace postwar Mycenae; Shaw Kommos IV; Cadogan BSA Studies 12; Davis–Bennet PRAP deepen; Warren stone vases 1969; Higgins terracottas

**Olmec:** Stirling Tres Zapotes path; González Lauck Complex A; Cyphers sculpture deepen; Pool Formative deepen; Grove Chalcatzingo reliefs; Rust/Sharer San Andrés; Blomster Etlatongo deepen; Cheetham pottery; Diehl revisit; Taube iconography deepen

**Early Maya:** Willey Seibal Peabody memoirs; Hansen Mirador conservation 2016; Freidel Cerros deepen; Laporte Mundo Perdido deepen; Hammond Cuello deepen; Saturno San Bartolo deepen; Inomata Aguada Fénix follow-on; Powis Pacbitun deepen; Ricketson Group E deepen; Estrada-Belli Holmul–Cival deepen

**Structured results (`export_check`):**
- **andes:** sources 58→68; sites 35→41; objects 38→48; claims 54→65
- **indus:** sources 58→68; sites 32→38; objects 36→46; claims 50→61
- **china-bronze:** sources 58→68; sites 33→39; objects 37→47; claims 51→62
- **sanxingdui:** sources 58→68; sites 30→36; objects 36→46; claims 48→59
- **aegean:** sources 58→68; sites 34→40; objects 36→46; claims 49→60
- **olmec:** sources 58→68; sites 31→37; objects 37→47; claims 44→55
- **early-maya:** sources 58→68; sites 34→40; objects 37→47; claims 49→60
- Mesopotamia/Egypt unchanged in this commit (already pass-5 on main). Citation gate green.

**Notes:** Contested items (Tello matriz / Casma early state; Indus script deciphered; Xia=Erlitou / Allan cosmos; Sanxingdui Shang colony; Troy=Homeric war; Olmec mother culture; Mirador first state) stay hypotheses. No invented coordinates/museum numbers/forged images; README counts defer to `export_check`.

### D-2026-10-12-7 — Post–pass-5 priority ranking (Deliberation Council)

**Decision:** After council session [`delib-2026-10-12-after-pass5`](../deliberations/delib-2026-10-12-after-pass5.md):

1. **State of product:** After density pass 5 on all nine packs, this is **no longer a thin textual introduction**. It is a **real but incomplete** machine-readable archive + local read-only API + `/ui`, with a fail-closed citation gate and explicit hypothesis labels. Versus Wikipedia / exhaustive excavation corpora: **coverage advantage does not hold**; **methodological advantage does** (queryable entities, resolvable `sources[]` on facts, explicit hypotheses, no forged artifact images).
2. **Explicit non-goals:** Do **not** invent content for coverage vanity; do **not** treat another unaudited all-pack volume pass as the default next step; cloud deliberation remains **spec-first** (D-2026-10-11-2 unchanged).
3. **Ranked next priorities:**
   1. **Claim/site quality audit** — start with densest packs Mesopotamia and Egypt (claim→source links, hyp labeling, site completeness), then selective deepen where gaps appear  
   2. **Optional new civilization shells** — scaffolding only; no vanity fills  
   3. **Cloud read-only host** — after an acceptable audit baseline; no write routes  
   4. **UI craft iteration** — taste polish, not a product-definition pivot  
   5. **Media** — rights-cleared metadata/outbound links only; no forged images; no wholesale copyrighted PDF/image dumps

**Verified counts (`export_check` 2026-10-12, post pass 5):** packs=9; sources **622**; sites **357**; periods **58**; objects **442**; claims **561** (fact 438 / hypothesis 123); media **28**.

**Notes:** Lenses are AI thinking aids (`perspective: true`, `person_endorsement: false`), not person endorsements. Integrity over vanity coverage.


### D-2026-10-12-8 — Mesopotamia + Egypt quality audit complete

**Decision:** Complete the claim/site quality audit for `data/structured/mesopotamia/` and `data/structured/egypt/` per D-2026-10-12-7 priority #1. Full report: [`docs/audits/audit-2026-10-12-mesopotamia-egypt.md`](audits/audit-2026-10-12-mesopotamia-egypt.md) ([中文](audits/audit-2026-10-12-mesopotamia-egypt.zh.md)).

**Findings:**
- **FAIL: 0 / 0** (Mesopotamia / Egypt). No empty or dangling claim `sources[]`; contested primacy rankings already `kind=hypothesis` with disclaimers; no invented site coordinates; objects are assemblage/artifact-class metadata only (no fake inventory numbers).
- **WARN (open):** (1) all 86 audited sites have `coordinates: null` — intentional, do not invent; (2) bibliographic-meta facts dominate substance facts (~40/63 meso, ~46/63 egypt) — deepen with *sourced* substance next, not vanity prose; (3) a few soft interpretive framings on handbook facts — watchlist only; (4) media still thin (outbound links only).
- **JSON remediations this pass:** none (no clear FAILs to relabel/trim/drop). Inventing archaeology to close WARNs is forbidden.

**Verified:** `export_check` OK after audit (9 packs; citation gate green).

**Notes:** Integrity over speed. Open WARNs are documented for the next ranked work (cited coordinates + substance claims), not swept under a fake FAIL fix.


### D-2026-10-12-9 — Substance tighten (Mesopotamia/Egypt) + seven-pack quality audit

**Decision:** (A) Address W2 from D-2026-10-12-8 by rewriting Mesopotamia + Egypt `kind=fact` claims toward **report-level substance** (site finds / strata / assemblages first; reports as documentation). (B) Run the same FAIL/WARN quality audit on the other seven structured packs; fix clear FAILs only.

**Job A:**
- Mesopotamia: **57** fact claims rewritten; Egypt: **59**; **116** total.
- No invented page numbers, coordinates, inventory numbers, or archaeology.
- Author-publish-lead facts reduced to **0/63** (each pack) by the audit classifier; residual W2 = report-scoped depth still thinner than ideal.
- Updated [`docs/audits/audit-2026-10-12-mesopotamia-egypt.md`](audits/audit-2026-10-12-mesopotamia-egypt.md).

**Job B:**
- Report: [`docs/audits/audit-2026-10-12-seven-packs.md`](audits/audit-2026-10-12-seven-packs.md) ([中文](audits/audit-2026-10-12-seven-packs.zh.md)).
- **FAIL before fix: 4** (1 olmec ranking-as-fact book title; 3 early-maya dangling cross-pack `src-olmec-*`). **FAIL after: 0**.
- Remediations: reword Diehl claim; copy two already-registered olmec source JSON files into early-maya for citation integrity.
- Open WARNs: null coordinates; biblio-meta residue (esp. china-bronze); survey-as-site ontology; thin media.

**Verified:** `export_check` OK (9 packs; early-maya sources 70 after copy).

**Notes:** Integrity over speed. Unaffected packs not vanity-rewritten in this pass.


### D-2026-10-12-10 — Cited coordinates + outbound media thicken (nine packs)

**Decision:** Address open W1 (null coordinates) and W4 (thin media) from D-2026-10-12-8/9 with an **honest partial fill** across all nine structured packs. Integrity over completeness.

**Coordinates (84 sites filled; rest left null):**
| Pack | Filled | Still null |
|------|-------:|----------:|
| mesopotamia | 29 | 14 |
| egypt | 22 | 21 |
| aegean | 20 | 20 |
| early-maya | 6 | 34 |
| indus | 3 | 35 |
| olmec | 2 | 35 |
| andes | 1 | 40 |
| china-bronze | 1 | 38 |
| sanxingdui | 0 | 36 |

**Sources used:** Pleiades places CSV dump (representative points + place id in `precision_note`); UNESCO WHC published DMS (Caral 1269, Moenjodaro 138, Dholavira 1645, Yinxu 1114-001, San Bartolo Tentative 5738); GeoNames `S.ANS` archaeological sites (El Mirador, La Venta, Chalcatzingo, Harappa, Cuello, Ceibal, Uaxactún, Tikal). Ambiguous title matches and survey/locus/pointer records were **not** filled.

**Media (+30 outbound records; total 28→58):** Rights status `outbound-link-only` (Archive.org / Heidelberg / ISAC / Met Publications / Field Museum / UNESCO / registered DOI landings / PLOS CC-BY). No forged artifact images; `local_path` remains null.

**Audits updated:** [`audit-2026-10-12-mesopotamia-egypt.md`](audits/audit-2026-10-12-mesopotamia-egypt.md), [`audit-2026-10-12-seven-packs.md`](audits/audit-2026-10-12-seven-packs.md) (+ zh).

**Verified:** `export_check` OK (9 packs; citation gate green).

**Notes:** Honest partial fill > fake completeness. Sanxingdui coordinates intentionally remain all-null this pass.


### D-2026-10-12-11 — Open-web gazetteer thicken (coords + sources + media)

**Decision:** Continue W1/W4 remediation with a second **honest** open-web pass after D-2026-10-12-10. Priority: sanxingdui → china-bronze → andes → indus → olmec → early-maya → remaining egypt/aegean empties. No invented archaeology.

**Coordinates:** **+26** sites (cumulative filled **84 → 110**). Sanxingdui/Jinsha from UNESCO Tentative **5816**; Chavín from UNESCO **330**; others from Pleiades CSV or GeoNames `S.ANS`/`S.RUIN` with country lock. Fuzzy / PPL-town / survey-frame hits left null.

**Sources:** New `src-andes-unesco-chavin-1985`, `src-sanxingdui-npj-jade-2023`; filled open PDF URLs on Qingguanshan + Pit 4 briefs.

**Media:** **+11** outbound records (**58 → 69**). Rights `outbound-link-only`; no forged images.

**Report:** [`docs/audits/pass-2026-10-12-web-sources.md`](audits/pass-2026-10-12-web-sources.md) ([中文](audits/pass-2026-10-12-web-sources.zh.md)).

**Verified:** `export_check` OK (9 packs; citation gate green).

**Notes:** Slack search found no Hermes/嘻嘻 contact in this workspace. Paywalled titles listed in the audit as title-only (not fake-cited).


### D-2026-10-12-12 — Global coverage map + Wave-1 shells

**Decision:** Publish a bilingual **coverage map** defining archive scope (complex societies with archaeological archives, not Wikipedia-breadth). Open **eleven Wave-1 `library-seed` shells** that close major geographic gaps while **continuing to thicken** the existing nine dense packs. **Do not wait** for perfect density before listing in API/UI. **Do not thin** dense packs. **Do not invent** finds, coordinates, or media art.

**Coverage map:** [`docs/coverage-map.md`](coverage-map.md) · [中文](coverage-map.zh.md)

**Deliberation:** [`deliberations/delib-2026-10-12-global-coverage.md`](../deliberations/delib-2026-10-12-global-coverage.md) — council endorses shells-now + thicken-nine.

**Wave-1 pack ids:** `elam-iran`, `nubia-kush`, `anatolia-hittite`, `levant-ugarit`, `bmac-oxus`, `nok-west-africa`, `teotihuacan`, `zapotec`, `lapita-pacific`, `dong-son`, `jomon-yayoi` (each `civ-*` + structured pack; ≥5 Sources; 1–3 Sites; 1 Period; 1 Object; 1 sourced Claim).

**Wave-2/3 (not opened):** Andes later phases (Chavín / Tiwanaku / Wari), Classic Maya, Aksum, Ban Chiang, Korean early states, Mitanni, Phoenician; later Mississippian, Great Zimbabwe, Inca, etc. — see map.

**Verified:** `export_check` OK (**20** packs; citation gate green). API/UI auto-discover new packs via `data/structured/*/civilization.json`.

**Notes:** Integrity > speed. Honest shells beat fake density. Generator: `tools/wave1_shells/generate_wave1.py`.


### D-2026-10-12-13 — Wave-1 densify to `library-seed-rich`

**Decision:** Densify all eleven Wave-1 packs opened in D-2026-10-12-12 from `library-seed` toward usable archive density. Schema status ladder uses **`library-seed-rich`** (not a free-text “expanding” label). Integrity over completeness: no invented archaeology, page numbers, coordinates, or media art.

**Per-pack deltas (structured JSON counts):**

| Pack | +sources | +sites | +periods | +objects | +claims | +media | After (src/site/claim/per/media) |
|------|--------:|-------:|---------:|---------:|--------:|-------:|----------------------------------|
| elam-iran | 10 | 5 | 3 | 2 | 10 | 3 | 15/8/11/4/3 |
| nubia-kush | 10 | 6 | 3 | 2 | 10 | 3 | 15/9/11/4/3 |
| anatolia-hittite | 10 | 5 | 3 | 2 | 10 | 3 | 15/7/11/4/3 |
| levant-ugarit | 10 | 5 | 3 | 2 | 10 | 2 | 15/7/11/4/2 |
| bmac-oxus | 10 | 5 | 3 | 2 | 10 | 2 | 15/7/11/4/2 |
| nok-west-africa | 10 | 5 | 3 | 2 | 10 | 3 | 15/7/11/4/3 |
| teotihuacan | 10 | 5 | 3 | 2 | 10 | 3 | 15/6/11/4/3 |
| zapotec | 10 | 5 | 3 | 2 | 10 | 3 | 15/6/11/4/3 |
| lapita-pacific | 10 | 5 | 3 | 2 | 10 | 2 | 15/7/11/4/2 |
| dong-son | 10 | 5 | 3 | 2 | 10 | 1 | 15/7/11/4/1 |
| jomon-yayoi | 10 | 5 | 3 | 2 | 10 | 3 | 15/6/11/4/3 |
| **Totals** | **110** | **56** | **33** | **22** | **110** | **28** | — |

**Coordinates:** UNESCO WHC published DMS (Susa 1455, Tchogha Zanbil 113, Hattusa/Yazılıkaya 377, Meroe island 1336, Gebel Barkal region 1073, Teotihuacan 414, Monte Albán 415, Jōmon serial 1632) and Pleiades CSV representative points (Malyan, Chogha Mish/Bonut, Kabnak, Alaca, Sapinuwa, Kaneš, Gonur, Altyn-Depe, etc.). Ambiguous or non-gazetteer sites left **null**.

**Media:** Outbound-link-only landings (UNESCO / Pleiades / Persée / JAA Brill / ANU / Archive.org / institutional portals). `local_path` remains null.

**Docs:** Coverage map updated; `civ-*.md` + pack READMEs synced. Machine summary: [`docs/audits/pass-2026-10-12-wave1-densify.json`](audits/pass-2026-10-12-wave1-densify.json).

**Verified:** `export_check` OK (**20** packs; citation gate green).

**Notes:** Still far from Egypt/Mesopotamia `fact-library` density. Prefer honest thin over fake dense. Tooling: `tools/wave1_shells/densify_wave1.py` + `densify_payloads/*.json`.


### D-2026-10-12-14 — Wave-2 shells

**Decision:** Open **nine Wave-2 `library-seed` shells** from the coverage-map priority list (D-2026-10-12-12), without thinning existing dense or Wave-1 packs. Same integrity rules as Wave-1: real P/S/T sources only; abstract/TOC-level claims; no invented finds, coordinates, page numbers, or media art.

**Wave-2 pack ids:** `chavin-andes`, `tiwanaku`, `wari`, `classic-maya`, `aksum`, `ban-chiang`, `early-korea`, `mitanni`, `phoenician` (each `civ-*` + structured pack; 5 Sources; 2–3 Sites; 1 Period; 1 Object; 1 sourced Claim; 0 media).

**Not opened (remain Wave-3 / Missing):** Cahokia/Mississippian; Ancestral Puebloan; Great Zimbabwe; West African medieval empires; Iberian Bronze; Hallstatt; Nuragic; Rapa Nui; full Inca; Moche; Aztec/Mexica; Mixtec; Angkor/Funan; Cyprus LBA — see [`coverage-map.md`](coverage-map.md).

**Docs:** Coverage map + README listings updated. Generator: `tools/wave2_shells/generate_wave2.py`.

**Verified:** `export_check` OK (**29** packs; citation gate green). API/UI auto-discover via `data/structured/*/civilization.json`.

**Notes:** Chavín pack uses distinct site id `site-chavin-huantar-type` so it does not collide with Andes comparative `site-chavin-de-huantar`. Honesty of thin shells beats fake density.

### D-2026-10-12-15 — Wave-3 shells

**Decision:** Open **eleven Wave-3 `library-seed` shells** that close major remaining geographic gaps from the coverage map (North America, southern/West Africa medieval, Europe beyond Aegean, Pacific Rapa Nui ethics-first, Andes Moche/Inca, Mesoamerica Aztec, SEA Angkor), without thinning existing packs. Same integrity rules: real P/S/T sources only; abstract/TOC-level claims; no invented finds, coordinates, page numbers, or media art.

**Wave-3 pack ids:** `cahokia`, `ancestral-pueblo`, `great-zimbabwe`, `west-africa-medieval`, `hallstatt-celtic`, `nuragic-sardinia`, `rapa-nui`, `inca`, `moche`, `aztec`, `angkor` (each `civ-*` + structured pack; 5 Sources; 2–3 Sites; 1 Period; 1 Object; 1 sourced Claim; 0 media).

**Not opened (remain Missing):** Iberian Copper/Bronze; fuller La Tène; Mixtec; Funan split; Cyprus LBA densify; Ife/Benin; broader Polynesian chiefdoms; later Christian Nubia split if needed.

**Docs:** Coverage map + README listings updated. Generator: `tools/wave3_shells/generate_wave3.py`.

**Verified:** `export_check` OK (**40** packs after Wave-3 open + Wave-2 densify in D-2026-10-12-16; citation gate green when both land).

**Notes:** West African medieval kept as one Ghana–Mali–Songhai pack for cleaner Sahel coverage. Rapa Nui packed ethics-first (no forged moai imagery).


### D-2026-10-12-16 — Wave-2 densify to `library-seed-rich`

**Decision:** Densify all nine Wave-2 packs opened in D-2026-10-12-14 from `library-seed` toward usable archive density (`library-seed-rich`). Same recipe as Wave-1 densify: ~+10 Sources, +5 Sites, +3 Periods, +2 Objects, +10 Claims, +1–3 outbound media. Integrity over completeness: no invented archaeology, page numbers, coordinates, or media art.

**Per-pack after counts (structured JSON):**

| Pack | sources | sites | periods | objects | claims | media |
|------|--------:|------:|--------:|--------:|-------:|------:|
| chavin-andes | 15 | 7 | 4 | 3 | 11 | 3 |
| tiwanaku | 15 | 7 | 4 | 3 | 11 | 2 |
| wari | 15 | 7 | 4 | 3 | 11 | 1 |
| classic-maya | 15 | 8 | 4 | 3 | 11 | 3 |
| aksum | 15 | 7 | 4 | 3 | 11 | 2 |
| ban-chiang | 15 | 7 | 4 | 3 | 11 | 2 |
| early-korea | 15 | 7 | 4 | 3 | 11 | 2 |
| mitanni | 15 | 7 | 4 | 3 | 11 | 1 |
| phoenician | 15 | 8 | 4 | 3 | 11 | 3 |
| **Delta totals** | **+90** | **+45** | **+27** | **+18** | **+90** | **+19** |

**Coordinates:** UNESCO WHC published points filled where available (Chavín 330, Tiwanaku 567, Tikal/Palenque, Aksum 15, Ban Chiang 575, Byblos/Tyre/Carthage, etc.). Ambiguous sites left **null**.

**Media:** Outbound-link-only landings (UNESCO / institutional portals). `local_path` remains null.

**Docs:** Coverage map updated; `civ-*.md` + pack READMEs synced. Machine summary: [`docs/audits/pass-2026-10-12-wave2-densify.json`](audits/pass-2026-10-12-wave2-densify.json).

**Verified:** `export_check` OK (**40** packs; citation gate green).

**Notes:** Still far from Egypt/Mesopotamia `fact-library` density. Prefer honest thin over fake dense. Tooling: `tools/wave2_shells/densify_wave2.py` + `densify_payloads/*.json`.



### D-2026-10-12-17 — Wave-3 densify to `library-seed-rich`

**Decision:** Densify all eleven Wave-3 packs opened in D-2026-10-12-15 from `library-seed` toward usable archive density (`library-seed-rich`). Same recipe as Wave-1/Wave-2 densify: ~+10 Sources, +5 Sites, +3 Periods, +2 Objects, +10 Claims, +1–3 outbound media. Integrity over completeness: no invented archaeology, page numbers, coordinates, or media art.

**Per-pack after counts (structured JSON):**

| Pack | sources | sites | periods | objects | claims | media |
|------|--------:|------:|--------:|--------:|-------:|------:|
| cahokia | 15 | 7 | 4 | 3 | 11 | 3 |
| ancestral-pueblo | 15 | 7 | 4 | 3 | 11 | 3 |
| great-zimbabwe | 15 | 7 | 4 | 3 | 11 | 2 |
| west-africa-medieval | 15 | 8 | 4 | 3 | 11 | 2 |
| hallstatt-celtic | 15 | 7 | 4 | 3 | 11 | 2 |
| nuragic-sardinia | 15 | 7 | 4 | 3 | 11 | 2 |
| rapa-nui | 15 | 7 | 4 | 3 | 11 | 2 |
| inca | 15 | 7 | 4 | 3 | 11 | 3 |
| moche | 15 | 7 | 4 | 3 | 11 | 1 |
| aztec | 15 | 7 | 4 | 3 | 11 | 2 |
| angkor | 15 | 8 | 4 | 3 | 11 | 3 |
| **Delta totals** | **+110** | **+55** | **+33** | **+22** | **+110** | **+25** |

**Coordinates:** English Wikipedia primary coordinates filled for major UNESCO-orientation sites (Cahokia, Chaco, Mesa Verde, Great Zimbabwe, Djenné, Timbuktu, Hallstatt, Su Nuraxi, Rapa Nui, Cusco, Machu Picchu, Templo Mayor, Angkor Wat, Huaca del Sol, etc.) with honest precision notes — UNESCO WHC pages were Cloudflare-blocked this pass. Ambiguous sites left **null**.

**Media:** Outbound-link-only landings (UNESCO / NPS / INAH / APSARA / project portals). `local_path` remains null. Rapa Nui remains ethics-first (no hosted moai imagery).

**Docs:** Coverage map updated; `civ-*.md` + pack READMEs synced. Machine summary: [`docs/audits/pass-2026-10-12-wave3-densify.json`](audits/pass-2026-10-12-wave3-densify.json).

**Verified:** `export_check` OK (**40** packs; citation gate green).

**Notes:** Still far from Egypt/Mesopotamia `fact-library` density (those nine remain the dense tier). Prefer honest thin over fake dense. Tooling: `tools/wave3_shells/densify_wave3.py` + `densify_payloads/*.json`.


### D-2026-10-12-18 — Quality audit 31 `library-seed-rich` packs

**Decision:** Run the same FAIL/WARN quality audit used for Mesopotamia/Egypt and the seven dense packs against all **31** `library-seed-rich` packs (Wave-1/2/3). Fix clear FAILs only; document honest WARNs; do not invent archaeology.

**Clear FAIL remediations:**
- `mitanni` / `asm-mitanni-amarna-letters-frame`: dangling `src-mitanni-letterman-diplomatic-texts` → `src-mitanni-beckman-diplomatic-texts`
- `rapa-nui`: `claim-rapanui-transport-hypothesis`, `claim-rapanui-hunt-lipo` relabeled `fact` → `hypothesis` + disclaimer
- 28 bibliographic-only fact statements rewritten toward report-level orientation (no new finds)

**Reports:** [`docs/audits/audit-2026-10-12-seed-rich-31.md`](audits/audit-2026-10-12-seed-rich-31.md) · [中文](audits/audit-2026-10-12-seed-rich-31.zh.md)

**Verified:** `export_check` OK (**40** packs; citation gate green). **FAIL = 0** across all 31 seed-rich packs after remediations.

**Notes:** Open WARNs (null coords, residual biblio orientation, thin media, `*-orientation` ontology sites) stay intentional. Dense nine not re-audited end-to-end this pass.

### D-2026-10-12-19 — Hot-pack Batch A densify toward fact-library

**Decision:** Densify user-priority packs `teotihuacan`, `classic-maya`, `inca`, `angkor`, `aksum` toward the `fact-library` band; **do not promote status to `fact-library` yet** (depth still below Egypt/Mesopotamia). Integrity over completeness: no invented pages/finds/media art.

**Approx. per-pack delta:** +15 sources · +8 sites · +4 periods · +4 objects · +15 claims · +3 media (totals ~ +75/+40/+20/+20/+74/+15).

**Reports:** [`docs/audits/pass-2026-10-12-hot-batch-a.md`](audits/pass-2026-10-12-hot-batch-a.md) · [中文](audits/pass-2026-10-12-hot-batch-a.zh.md)

**Verified:** `export_check` OK (40 packs).


### D-2026-10-12-20 — Ingest 嘻嘻 P-grade coordinate reply

**Decision:** Ingest 嘻嘻 P-grade coordinate CSV with integrity rules: **never ingest 鱼凫/Yufu** (false hit = Yufu-shi, Japan); prefer P(UNESCO); S only when carefully matched to existing site ids by pack+name; skip empty/frame/ambiguous rows; record grade + URL in `precision_note`.

**Results:** 27 new fills · 7 P-upgrades · Yufu left null. Reports: [`docs/audits/pass-2026-10-12-xixi-coords.md`](audits/pass-2026-10-12-xixi-coords.md) · [中文](audits/pass-2026-10-12-xixi-coords.zh.md)

**Verified:** `export_check` OK.

### D-2026-10-12-21 — Hot-pack Batch B densify toward fact-library

**Decision:** Densify user-priority packs `aztec`, `phoenician`, `anatolia-hittite`, `nubia-kush`, `elam-iran` toward the `fact-library` band (same recipe as Batch A / D-2026-10-12-19); **do not promote status to `fact-library` yet** (depth still below Egypt/Mesopotamia). Integrity over completeness: no invented pages/finds/media art.

**Approx. per-pack delta:** +15 sources · +8 sites · +4 periods · +4 objects · +15 claims · +3 media (totals +75/+40/+20/+20/+75/+15).

**Coord fills (grounded only):** Tlatelolco, Texcoco (S/Wikipedia); Motya, Sidon (S/Wikipedia); Kerma (S/Wikipedia). Orientation frames left null.

**Reports:** [`docs/audits/pass-2026-10-12-hot-batch-b.md`](audits/pass-2026-10-12-hot-batch-b.md) · [中文](audits/pass-2026-10-12-hot-batch-b.zh.md)

**Verified:** `export_check` OK (40 packs).

### D-2026-10-12-22 — Hot-pack Round-2 Batch A densify toward denser archive

**Decision:** Second densify pass on `teotihuacan`, `classic-maya`, `inca`, `angkor`, `aksum` toward Egypt/Mesopotamia `fact-library` density; **do not promote status to `fact-library` yet** (still below Egypt). Integrity over completeness: no invented pages/finds/media art/coords.

**Approx. per-pack delta:** +18 sources · +8 sites · +2 periods · +12 objects · +17 claims · +3 media (landing ≈45–50 / 22–24 / 10 / 19 / 42–43 / 8–9).

**Coord fills (grounded only):** Quiriguá (UNESCO WHC 149 DMS, grade=P); Uxmal (UNESCO WHC periodic reporting / list 791, grade=P).

**Reports:** [`docs/audits/pass-2026-10-12-hot-round2-a.md`](audits/pass-2026-10-12-hot-round2-a.md) · [中文](audits/pass-2026-10-12-hot-round2-a.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-12-23 — Hot-pack Round-2 Batch B densify toward denser archive

**Decision:** Second densify pass on `aztec`, `phoenician`, `anatolia-hittite`, `nubia-kush`, `elam-iran` toward Egypt/Mesopotamia `fact-library` density; **do not promote status to `fact-library` yet** (still below Egypt). Integrity over completeness: no invented pages/finds/media art/coords.

**Approx. per-pack delta:** +18 sources · +8 sites · +2 periods · +12 objects · +17 claims · +3 media (landing ≈48 / 23–25 / 10 / 19 / 43 / 8–9).

**Coord fills:** none this pass (orientation sites left null; prior P/S fills retained).

**Reports:** [`docs/audits/pass-2026-10-12-hot-round2-b.md`](audits/pass-2026-10-12-hot-round2-b.md) · [中文](audits/pass-2026-10-12-hot-round2-b.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-12-24 — Seed densify Batch C toward denser archive

**Decision:** Densify Wave-1 leftover packs `levant-ugarit`, `bmac-oxus`, `zapotec`, `jomon-yayoi`, `dong-son` from ~15-source shells toward the first hot-densify band (~30 sources); **do not promote status to `fact-library`** (keep `library-seed-rich`). Integrity over completeness: no invented pages/finds/media art/coords.

**Approx. per-pack delta:** +15 sources · +8 sites · +4 periods · +4 objects · +15 claims · +2–3 media.

**Coord fills (grounded only):** New Jōmon UNESCO 1632 component sites Isedotai, Goshono, Futatsumori, Omori Katsuyama written with WHC maps DMS→decimal (grade=P) on create.

**Reports:** [`docs/audits/pass-2026-10-12-seed-batch-c.md`](audits/pass-2026-10-12-seed-batch-c.md) · [中文](audits/pass-2026-10-12-seed-batch-c.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-12-25 — Seed densify Batch D toward denser archive

**Decision:** Densify packs `nok-west-africa`, `lapita-pacific`, `chavin-andes`, `tiwanaku`, `mitanni` from ~15-source shells toward the first hot-densify band (~30 sources); **keep `library-seed-rich`** (do not promote to fact-library). Integrity over completeness: no invented pages/finds/media art/coords.

**Approx. per-pack delta:** +15 sources · +8 sites · +4 periods · +4 objects · +15 claims · +2–3 media.

**Coord fills:** none this pass (orientation sites left null; prior UNESCO fills on Chavín/Tiwanaku type sites retained).

**Reports:** [`docs/audits/pass-2026-10-12-seed-batch-d.md`](audits/pass-2026-10-12-seed-batch-d.md) · [中文](audits/pass-2026-10-12-seed-batch-d.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-12-26 — Seed densify Batch E toward denser archive

**Decision:** Densify packs `wari`, `ban-chiang`, `early-korea`, `moche`, `cahokia` from ~15-source shells toward the first hot-densify band (~30 sources); **keep `library-seed-rich`** (do not promote to fact-library). Integrity over completeness: no invented pages/finds/media art/coords. Claim IDs use `-seed-e` suffix to avoid seed collisions (lesson from Batch D).

**Approx. per-pack delta:** +15 sources · +8 sites · +4 periods · +4 objects · +15 claims · +3 media.

**Coord fills:** none this pass (orientation sites left null; prior UNESCO fills on Ban Chiang / Cahokia type sites retained).

**Reports:** [`docs/audits/pass-2026-10-12-seed-batch-e.md`](audits/pass-2026-10-12-seed-batch-e.md) · [中文](audits/pass-2026-10-12-seed-batch-e.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-12-27 — Seed densify Batch F toward denser archive (final thin seeds)

**Decision:** Densify packs `ancestral-pueblo`, `great-zimbabwe`, `west-africa-medieval`, `hallstatt-celtic`, `nuragic-sardinia`, `rapa-nui` from ~15-source shells toward the first hot-densify band (~30 sources); **keep `library-seed-rich`**. Claim IDs use `-seed-f` suffix. **Rapa Nui ethics-first:** outbound UNESCO media only; no hosted moai imagery; transport/ecology claims kept as open hypotheses.

**Approx. per-pack delta:** +15 sources · +8 sites · +4 periods · +4 objects · +15 claims · +3 media.

**Coord fills:** none this pass (orientation sites left null; prior UNESCO/Wikipedia fills retained).

**Milestone:** All **21** former ~15-source seed packs (Batches C–F) now sit at ~30 sources / ~15 sites / ~26 claims. Remaining thinner work is only non-seed or already-hot packs.

**Reports:** [`docs/audits/pass-2026-10-12-seed-batch-f.md`](audits/pass-2026-10-12-seed-batch-f.md) · [中文](audits/pass-2026-10-12-seed-batch-f.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-12-28 — Hot densify Round-3 Batch A toward denser archive

**Decision:** Densify hot packs `teotihuacan`, `classic-maya`, `inca`, `angkor`, `aksum` from ~48-source Round-2 band toward Egypt/Mesopotamia-adjacent depth; **keep `library-seed-rich`** (do not promote to fact-library this pass). Claim IDs use `-r3a` suffix.

**Approx. per-pack delta:** +18 sources · +9 sites · +2 periods · +14 objects · +18 claims · +2 media.

**Landed band:** ~66 sources / 31–33 sites / 12 periods / 33 objects / 60–61 claims / 10–11 media (Egypt ref still higher on sites/objects/claims).

**Coord fills:** none this pass.

**Reports:** [`docs/audits/pass-2026-10-12-hot-round3-a.md`](audits/pass-2026-10-12-hot-round3-a.md) · [中文](audits/pass-2026-10-12-hot-round3-a.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-12-29 — Hot densify Round-3 Batch B toward denser archive

**Decision:** Densify hot packs `aztec`, `phoenician`, `anatolia-hittite`, `nubia-kush`, `elam-iran` from ~48-source Round-2 band toward Egypt/Mesopotamia-adjacent depth; **keep `library-seed-rich`** (do not promote to fact-library this pass). Claim IDs use `-r3b` suffix.

**Approx. per-pack delta:** +18 sources · +9 sites · +2 periods · +14 objects · +18 claims · +2 media.

**Landed band:** ~66 sources / 32–34 sites / 12 periods / 33 objects / 61 claims / 10–11 media (Egypt ref still higher on sites/objects/claims).

**Coord fills:** none this pass.

**Reports:** [`docs/audits/pass-2026-10-12-hot-round3-b.md`](audits/pass-2026-10-12-hot-round3-b.md) · [中文](audits/pass-2026-10-12-hot-round3-b.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-12-30 — Hot densify Round-4 Batch A sites/objects + fact-library eval

**Decision:** Densify hot packs `teotihuacan`, `classic-maya`, `inca`, `angkor`, `aksum` with **sites/objects focus** from Round-3 band (~66/32/33/61) toward Egypt/Aegean/Mesopotamia-adjacent depth; then evaluate each pack for `fact-library` promotion under honest numeric + quality gates. Claim IDs use `-r4a` suffix.

**Approx. per-pack delta:** +5 sources · +10 sites · +1 period · +18 objects · +8 claims · +1 media.

**Landed band:** ~71 sources / 41–43 sites / 13 periods / 51 objects / 68–69 claims / 11–12 media.

**Promotion gates:**
1. Numeric: sources ≥ 65 · sites ≥ 38 · objects ≥ 45 · claims ≥ 58
2. Quality/honesty: report-level claims; coord fill not almost-all-null; orientation stubs not dominant

**Promotion outcome:** **None promoted.** All five passed numeric gates but failed quality/honesty (coords still 2–14% filled; orientation stubs remain substantial). Status stays `library-seed-rich` for all five.

**Coord fills:** none this pass (null left null; no invented coordinates).

**Reports:** [`docs/audits/pass-2026-10-12-hot-round4-a.md`](audits/pass-2026-10-12-hot-round4-a.md) · [中文](audits/pass-2026-10-12-hot-round4-a.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-12-31 — Hot densify Round-4 Batch B sites/objects + fact-library eval

**Decision:** Densify hot packs `aztec`, `phoenician`, `anatolia-hittite`, `nubia-kush`, `elam-iran` with **sites/objects focus** from Round-3 band (~66/32–34/33/61) toward Egypt/Aegean/Mesopotamia-adjacent depth; then evaluate each pack for `fact-library` promotion under honest numeric + quality gates. Claim IDs use `-r4b` suffix.

**Approx. per-pack delta:** +5 sources · +10 sites · +1 period · +18 objects · +8 claims · +1 media.

**Landed band:** ~71 sources / 42–44 sites / 13 periods / 51 objects / 69 claims / 11–12 media.

**Promotion gates:** same as D-30 (numeric sources≥65 / sites≥38 / objects≥45 / claims≥58; quality/honesty: coords not almost-all-null; orientation stubs not dominant).

**Promotion outcome:** **None promoted.** All five passed numeric gates but failed quality/honesty (coords still 7–18% filled; orientation stubs remain). Status stays `library-seed-rich` for all five. **All 10 hot packs now Round-4 band numerically; none fact-library.**

**Coord fills:** none this pass.

**Reports:** [`docs/audits/pass-2026-10-12-hot-round4-b.md`](audits/pass-2026-10-12-hot-round4-b.md) · [中文](audits/pass-2026-10-12-hot-round4-b.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-13-01 — Seed densify Batch G toward ~48 sources

**Decision:** Densify seed packs `levant-ugarit`, `bmac-oxus`, `zapotec`, `jomon-yayoi`, `dong-son` from ~30-source Seed C–F band toward hot Round-2 band (~48 sources); **keep `library-seed-rich`**. Claim IDs use `-seed-g` suffix. Remaining 16 thin seeds deferred to Batches H/I/J.

**Approx. per-pack delta:** +18 sources · +8 sites · +2 periods · +12 objects · +17 claims · +3 media.

**Landed band:** ~48–49 sources / 22–23 sites / 10 periods / 19 objects / 43 claims / 7–9 media.

**Coord fills:** none this pass.

**Reports:** [`docs/audits/pass-2026-10-13-seed-batch-g.md`](audits/pass-2026-10-13-seed-batch-g.md) · [中文](audits/pass-2026-10-13-seed-batch-g.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-13-02 — Seed densify Batch H toward ~48 sources

**Decision:** Densify seed packs `nok-west-africa`, `lapita-pacific`, `chavin-andes`, `tiwanaku`, `mitanni` from ~30-source band toward hot Round-2 band (~48 sources); **keep `library-seed-rich`**. Claim IDs use `-seed-h` suffix. Remaining 11 thin seeds deferred to Batches I/J.

**Approx. per-pack delta:** +18 sources · +8 sites · +2 periods · +12 objects · +17 claims · +3 media.

**Landed band:** ~48 sources / 23 sites / 10 periods / 19 objects / 42–43 claims / 7–9 media.

**Coord fills:** none this pass.

**Reports:** [`docs/audits/pass-2026-10-13-seed-batch-h.md`](audits/pass-2026-10-13-seed-batch-h.md) · [中文](audits/pass-2026-10-13-seed-batch-h.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-13-03 — Seed densify Batch I toward ~48 sources

**Decision:** Densify seed packs `wari`, `ban-chiang`, `early-korea`, `moche`, `cahokia` from ~30-source band toward hot Round-2 band (~48 sources); **keep `library-seed-rich`**. Claim IDs use `-seed-i` suffix. Remaining 6 thin seeds deferred to Batch J.

**Approx. per-pack delta:** +18 sources · +8 sites · +2 periods · +12 objects · +17 claims · +3 media.

**Landed band:** ~48 sources / 23 sites / 10 periods / 19 objects / 43 claims / 7–9 media.

**Coord fills:** none this pass.

**Reports:** [`docs/audits/pass-2026-10-13-seed-batch-i.md`](audits/pass-2026-10-13-seed-batch-i.md) · [中文](audits/pass-2026-10-13-seed-batch-i.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-13-04 — Seed densify Batch J toward ~48 sources (milestone)

**Decision:** Densify the last six ~30-source seed packs `ancestral-pueblo`, `great-zimbabwe`, `west-africa-medieval`, `hallstatt-celtic`, `nuragic-sardinia`, `rapa-nui` toward hot Round-2 band (~48 sources); **keep `library-seed-rich`**. Claim IDs use `-seed-j` suffix. **Milestone:** all 21 former ~30-source non-hot seeds are now ~48.

**Rapa Nui ethics:** outbound UNESCO media only; no hosted moai imagery; transport/collapse/colonization claims kept as `hypothesis` with disclaimers.

**Approx. per-pack delta:** +18 sources · +8 sites · +2 periods · +12 objects · +17 claims · +3 media.

**Landed band:** ~48 sources / 23–24 sites / 10 periods / 19 objects / 43 claims / 8–9 media.

**Coord fills:** none this pass.

**Reports:** [`docs/audits/pass-2026-10-13-seed-batch-j.md`](audits/pass-2026-10-13-seed-batch-j.md) · [中文](audits/pass-2026-10-13-seed-batch-j.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-13-05 — Seed densify Batch K toward ~71 sources

**Decision:** Densify seed packs `levant-ugarit`, `bmac-oxus`, `zapotec`, `jomon-yayoi`, `dong-son` from ~48-source Seed G–J band toward hot Round-4 band (~71 sources); **keep `library-seed-rich`** (do not promote). Claim IDs use `-seed-k` suffix. Remaining 16 non-hot seeds deferred to Batches L/M/N.

**Approx. per-pack delta:** +23 sources · +20 sites · +3 periods · +32 objects · +26 claims · +3 media.

**Landed band:** ~71–72 sources / 42–43 sites / 13 periods / 51 objects / 69 claims / 10–12 media.

**Coord fills:** none this pass.

**Reports:** [`docs/audits/pass-2026-10-13-seed-batch-k.md`](audits/pass-2026-10-13-seed-batch-k.md) · [中文](audits/pass-2026-10-13-seed-batch-k.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-13-06 — Seed densify Batch L toward ~71 sources

**Decision:** Densify seed packs `nok-west-africa`, `lapita-pacific`, `chavin-andes`, `tiwanaku`, `mitanni` from ~48-source band toward hot Round-4 band (~71 sources); **keep `library-seed-rich`**. Claim IDs use `-seed-l` suffix. Remaining 11 non-hot seeds deferred to Batches M/N.

**Approx. per-pack delta:** +23 sources · +20 sites · +3 periods · +32 objects · +26 claims · +3 media.

**Landed band:** ~71 sources / 43 sites / 13 periods / 51 objects / 68–69 claims / 10–12 media.

**Coord fills:** none this pass.

**Reports:** [`docs/audits/pass-2026-10-13-seed-batch-l.md`](audits/pass-2026-10-13-seed-batch-l.md) · [中文](audits/pass-2026-10-13-seed-batch-l.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-13-07 — Seed densify Batch M toward ~71 sources

**Decision:** Densify seed packs `wari`, `ban-chiang`, `early-korea`, `moche`, `cahokia` from ~48-source band toward hot Round-4 band (~71 sources); **keep `library-seed-rich`**. Claim IDs use `-seed-m` suffix. Remaining 6 non-hot seeds deferred to Batch N.

**Approx. per-pack delta:** +23 sources · +20 sites · +3 periods · +32 objects · +26 claims · +3 media.

**Landed band:** ~71 sources / 43 sites / 13 periods / 51 objects / 69 claims / 10–12 media.

**Coord fills:** none this pass.

**Reports:** [`docs/audits/pass-2026-10-13-seed-batch-m.md`](audits/pass-2026-10-13-seed-batch-m.md) · [中文](audits/pass-2026-10-13-seed-batch-m.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-13-08 — Seed densify Batch N toward ~71 sources (milestone)

**Decision:** Densify the last six ~48-source seed packs `ancestral-pueblo`, `great-zimbabwe`, `west-africa-medieval`, `hallstatt-celtic`, `nuragic-sardinia`, `rapa-nui` toward hot Round-4 band (~71 sources); **keep `library-seed-rich`**. Claim IDs use `-seed-n` suffix. **Milestone:** all 21 non-hot seeds are now ~71.

**Rapa Nui ethics:** outbound UNESCO media only; no hosted moai imagery; transport/collapse/colonization claims kept as `hypothesis` with disclaimers.

**Approx. per-pack delta:** +23 sources · +20 sites · +3 periods · +32 objects · +26 claims · +3 media.

**Landed band:** ~71 sources / 43–44 sites / 13 periods / 51 objects / 69 claims / 11–12 media.

**Coord fills:** none this pass.

**Reports:** [`docs/audits/pass-2026-10-13-seed-batch-n.md`](audits/pass-2026-10-13-seed-batch-n.md) · [中文](audits/pass-2026-10-13-seed-batch-n.zh.md)

**Verified:** `export_check` OK (40 packs) after this pass.

### D-2026-10-13-09 — Entry detail UI: report columns as primary surface

**Decision:** Opening a civilization in `/ui` defaults to the **archive report** (parse `##` sections from `markdown_path`); claim list becomes a secondary tab. Add read-only `GET /api/v1/civilizations/{id}/report`. Methods / discovery lineage = **Research history** verbatim + registered sources (especially tier P) labeled “registered source lineage” — **do not invent** excavation narratives. Omit empty sections. Chinese UI default.

**Design:** [`docs/entry-detail-ui.md`](entry-detail-ui.md) · [中文](entry-detail-ui.zh.md)

**Deliberation:** [`deliberations/delib-2026-10-13-entry-detail-ui.md`](../deliberations/delib-2026-10-13-entry-detail-ui.md)

**Implement:** Best-effort `body_zh`/`body_en` split; always keep `body_md`; site cards expand sources / linked claims / existing coordinates; `export_check` unchanged.

### D-2026-10-13-10 — Period chronological sort + honest Media tab

**Decision:** `/api/v1/periods` lists chronologically: primary `time.approx_from_bce` **descending** (older / higher BCE first), then `approx_to_bce` descending, then `id`; **nulls last**. Spans are **cited schemes** (`time.label` / `scheme_note`), not a unique calendar. UI `renderPeriods` shows `time.label` (+ optional from–to) and muted `scheme_note`; client-side sort matches as a safety net. Add **媒体 / Media** secondary tab (default remains 档案报告): fetch `/api/v1/media?civilization=…`, expand sources, cards with title / media_type / rights / outbound link — **never** invent thumbnails. `rights.status === outbound-link-only` labeled as 外链资料 / outbound only (document, catalog, or gallery page), not an embeddable photo.

**配图闸门 (image pairing):** Register media only when (a) stable public URL, (b) rights clear for outbound (or open license for any future hotlink/embed), (c) caption + `src-*`, (d) no AI / fake artifacts, (e) prefer site maps, excavation report digitizations, museum open catalogs, UNESCO WHC pages already or newly verified. No copyrighted binaries in-repo; no decorative stock.

**Pilot:** Egypt + Mesopotamia each gained one verified UNESCO WHC outbound `external-catalog` media (+ tier-T source): Memphis WHC 86; Ahwar of Southern Iraq WHC 1481. Existing document-link / catalog media remain the bulk.

**Design:** [`docs/entry-detail-ui.md`](entry-detail-ui.md) · [中文](entry-detail-ui.zh.md)

**Implement:** API `_period_sort_key`; `enrich_media`; UI Media tab; `export_check` unchanged beyond new records.

