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
