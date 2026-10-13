# Global coverage map — callable archive packs

[中文](coverage-map.zh.md) | English

**Decision:** [D-2026-10-12-12](decisions.md#d-2026-10-12-12--global-coverage-map--wave-1-shells) (Wave-1 opened) · [D-2026-10-12-13](decisions.md#d-2026-10-12-13--wave-1-densify-to-library-seed-rich) (Wave-1 densified) · [D-2026-10-12-14](decisions.md#d-2026-10-12-14--wave-2-shells) (Wave-2 opened) · [D-2026-10-12-15](decisions.md#d-2026-10-12-15--wave-3-shells) (Wave-3 opened) · [D-2026-10-12-16](decisions.md#d-2026-10-12-16--wave-2-densify-to-library-seed-rich) (Wave-2 densified) · [D-2026-10-12-17](decisions.md#d-2026-10-12-17--wave-3-densify-to-library-seed-rich) (Wave-3 densified)  
**Deliberation:** [`deliberations/delib-2026-10-12-global-coverage.md`](../deliberations/delib-2026-10-12-global-coverage.md)

## Scope

This project catalogs **complex societies / early civilizations with archaeological archives** — not modern nations, not every culture name on Wikipedia.

**In scope:** societies with excavated sites, published reports or durable syntheses, and enough structure (settlement, institutions, craft specialization, writing *or* other administrative media) that a **callable** Source / Site / Period / Object / Claim pack is meaningful.

**Out of scope (for now):** purely ethnographic labels without archaeological archive depth; modern nation histories; mythic “lost continents”; decorative encyclopedia stubs.

**Integrity rule:** Wikipedia-breadth is **not** the goal. Callable, sourced packs (including honest `library-seed` shells) are. Prefer an empty section labeled empty over fake density.

## Status legend

| Label | Meaning |
|-------|---------|
| **Dense** | `fact-library` structured pack with substantial Sources/Sites/Claims |
| **Shell** | `library-seed` undensified pack — real Sources, minimal Sites/Claims, sections may be empty (none remaining after D-2026-10-12-17) |
| **Expanding** | `library-seed-rich` — densified Wave-1/Wave-2 pack (usable archive density; not yet `fact-library`) |
| **Missing** | Not opened yet; listed for later waves |

## Matrix by world region

| Region | HAVE (dense) | HAVE (expanding) | MISSING (priority) | Wave |
|--------|--------------|------------------|--------------------|------|
| **Mesopotamia / SW Iran** | Mesopotamia | Elam (`library-seed-rich`) | Later Iranian empires (Achaemenid+) as separate packs | 1 densified; 2 later |
| **Nile / NE Africa** | Egypt | Nubia–Kush; Aksum (`library-seed-rich`) | Later Christian Nubia split if needed | 1–2 densified |
| **Anatolia / Levant / E Med** | Aegean | Hittite; Ugarit; Mitanni; Phoenician (`library-seed-rich`) | Cyprus Late Bronze further densify | 1–2 densified |
| **Central / South Asia** | Indus | BMAC/Oxus (`library-seed-rich`) | Vedic/early Historic Ganga; Gandhara; Sri Lanka early | 1 densified; 2–3 |
| **East Asia** | China Bronze; Sanxingdui | Jōmon/Yayoi; Early Korea (`library-seed-rich`) | Later Zhou–Han overview split | 1–2 densified |
| **Southeast Asia** | — | Đông Sơn; Ban Chiang; Angkor (`library-seed-rich`) | Funan split if needed | 1–2 densified; 3 opened |
| **West / Sahel Africa** | — | Nok; West Africa medieval; Great Zimbabwe (`library-seed-rich`) | Ife/Benin later | 1 densified; 3 opened |
| **Mesoamerica** | Olmec; Early Maya | Teotihuacan; Zapotec; Classic Maya; Aztec (`library-seed-rich`) | Mixtec later | 1–2 densified; 3 opened |
| **Andes / South America** | Andes (Caral–Norte Chico) | Chavín; Tiwanaku; Wari; Moche; Inca (`library-seed-rich`) | — | 2 densified; 3 opened |
| **Oceania / Pacific** | — | Lapita; Rapa Nui (`library-seed-rich`) | Broader Polynesian chiefdoms | 1 densified; 3 opened |
| **Europe (beyond Aegean)** | — | Hallstatt; Nuragic (`library-seed-rich`) | Iberia Copper/Bronze; fuller La Tène | 3 opened |
| **North America** | — | Cahokia; Ancestral Puebloan (`library-seed-rich`) | Broader Mississippian peers | 3 opened |

## Wave-1 packs (opened D-2026-10-12-12; densified D-2026-10-12-13)

Status upgraded to **`library-seed-rich`**. Typical density after densify: **~15 Sources**, **6–9 Sites**, **4 Periods**, **~11 Claims**, **1–3 outbound media**. Coords only from UNESCO WHC DMS or Pleiades CSV; otherwise null. **No invented finds, page numbers, or media art.** Still below Egypt/Mesopotamia `fact-library` density.

| Pack id | Civilization id | Status | Region gap closed |
|---------|-----------------|--------|-------------------|
| `elam-iran` | `civ-elam-iran` | library-seed-rich | SW Iran beside Mesopotamia |
| `nubia-kush` | `civ-nubia-kush` | library-seed-rich | Nile south of Egypt |
| `anatolia-hittite` | `civ-anatolia-hittite` | library-seed-rich | Anatolian plateau |
| `levant-ugarit` | `civ-levant-ugarit` | library-seed-rich | Northern Levant LBA |
| `bmac-oxus` | `civ-bmac-oxus` | library-seed-rich | Central Asian oases |
| `nok-west-africa` | `civ-nok-west-africa` | library-seed-rich | West Africa Iron Age |
| `teotihuacan` | `civ-teotihuacan` | library-seed-rich | Central Mexican Classic |
| `zapotec` | `civ-zapotec` | library-seed-rich | Oaxaca / Monte Albán |
| `lapita-pacific` | `civ-lapita-pacific` | library-seed-rich | Pacific Austronesian dispersal |
| `dong-son` | `civ-dong-son` | library-seed-rich | Mainland SEA bronze drums |
| `jomon-yayoi` | `civ-jomon-yayoi` | library-seed-rich | Japanese archipelago |

## Pre-existing dense packs (unchanged this decision)

`mesopotamia`, `egypt`, `andes`, `indus`, `china-bronze`, `sanxingdui`, `aegean`, `olmec`, `early-maya` — continue thickening; **do not thin** to “match” shells.

## Wave-2 packs (opened D-2026-10-12-14; densified D-2026-10-12-16)

Status upgraded to **`library-seed-rich`**. Typical density after densify: **~15 Sources**, **7–8 Sites**, **4 Periods**, **~11 Claims**, **1–3 outbound media**. Coords only from UNESCO WHC published DMS (or left null). **No invented finds, page numbers, or media art.** Tooling: `tools/wave2_shells/densify_wave2.py`.

| Pack id | Civilization id | Status | Region gap closed |
|---------|-----------------|--------|-------------------|
| `chavin-andes` | `civ-chavin` | library-seed-rich | Early Horizon Andes (beside Caral pack) |
| `tiwanaku` | `civ-tiwanaku` | library-seed-rich | Titicaca highland Middle Horizon |
| `wari` | `civ-wari` | library-seed-rich | Ayacucho / Middle Horizon expansion |
| `classic-maya` | `civ-classic-maya` | library-seed-rich | Classic lowland Maya (beside early-maya) |
| `aksum` | `civ-aksum` | library-seed-rich | Ethiopian highland / Red Sea kingdom |
| `ban-chiang` | `civ-ban-chiang` | library-seed-rich | NE Thailand prehistoric (beside Đông Sơn) |
| `early-korea` | `civ-early-korea` | library-seed-rich | Mumun–early states peninsula |
| `mitanni` | `civ-mitanni` | library-seed-rich | LBA Hurrian / Upper Mesopotamia |
| `phoenician` | `civ-phoenician` | library-seed-rich | Levantine coast + western Punic nodes |

## Wave-3 packs (opened D-2026-10-12-15; densified D-2026-10-12-17)

Status upgraded to **`library-seed-rich`**. Typical density after densify: **~15 Sources**, **7–8 Sites**, **4 Periods**, **~11 Claims**, **1–3 outbound media**. Coords from English Wikipedia primary points where UNESCO WHC was unreachable this pass (honest precision notes); otherwise null. **No invented finds, page numbers, or media art.** Tooling: `tools/wave3_shells/densify_wave3.py`.

| Pack id | Civilization id | Status | Region gap closed |
|---------|-----------------|--------|-------------------|
| `cahokia` | `civ-cahokia` | library-seed-rich | Mississippian / American Bottom |
| `ancestral-pueblo` | `civ-ancestral-pueblo` | library-seed-rich | Colorado Plateau / Chaco–Mesa Verde |
| `great-zimbabwe` | `civ-great-zimbabwe` | library-seed-rich | Southern African Iron Age capital |
| `west-africa-medieval` | `civ-west-africa-medieval` | library-seed-rich | Ghana–Mali–Songhai Sahelian empires |
| `hallstatt-celtic` | `civ-hallstatt-celtic` | library-seed-rich | Alpine Early Iron Age / Hallstatt |
| `nuragic-sardinia` | `civ-nuragic-sardinia` | library-seed-rich | Sardinian Nuragic towers |
| `rapa-nui` | `civ-rapa-nui` | library-seed-rich | Polynesian Rapa Nui (ethics-first) |
| `inca` | `civ-inca` | library-seed-rich | Tawantinsuyu Late Horizon |
| `moche` | `civ-moche` | library-seed-rich | North-coast Peru EIP |
| `aztec` | `civ-aztec` | library-seed-rich | Mexica / Triple Alliance |
| `angkor` | `civ-angkor` | library-seed-rich | Khmer Angkorian capital landscape |

**Still Missing (later):** Iberian Copper/Bronze; fuller La Tène; Mixtec; Funan split; Cyprus LBA densify; Ife/Benin; broader Polynesian chiefdoms; later Christian Nubia split if needed.

## How users see packs now

- **API:** `GET /api/v1/civilizations` auto-discovers every `data/structured/*/civilization.json` — Wave-1/2/3 densified packs appear with `status: library-seed-rich`; nine pre-existing packs remain `fact-library`.
- **UI:** `/ui` loads the same list; filter by name.
- **Gate:** `tools/export_check.py` — citation fail-closed for all packs (**40**).

## Product stance

**40 packs callable: 9 dense (`fact-library`) + 31 expanding (`library-seed-rich`); all 10 hot packs at Round-4 (~71 / 41–44 / 51 / 68–69) but **none promoted**; **all 21 non-hot Seed packs now ~48 (Batches G–J complete).** Honesty of status beats vanity of count. Next: cited UNESCO/P coord fills on hot packs before any promotion review; open remaining Missing where archives allow.

> **2026-10-12 update (Hot Round-3 A):** Hot densify Round-3 Batch A (D-2026-10-12-28) raised teotihuacan / classic-maya / inca / angkor / aksum to ~66 sources / 31–33 sites / 33 objects / 60–61 claims; status remains `library-seed-rich` (not promoted). No new coords.

> **2026-10-12 update (Hot Round-3 B):** Hot densify Round-3 Batch B (D-2026-10-12-29) raised aztec / phoenician / anatolia-hittite / nubia-kush / elam-iran to ~66 sources / 32–34 sites / 33 objects / 61 claims; status remains `library-seed-rich` (not promoted). **All 10 hot packs now Round-3 band.** No new coords this pass.

> **2026-10-12 update (Hot Round-4 A):** Hot densify Round-4 Batch A (D-2026-10-12-30) raised teotihuacan / classic-maya / inca / angkor / aksum to ~71 sources / 41–43 sites / 51 objects / 68–69 claims (sites/objects focus). **Numeric gates passed; quality/honesty failed (coords 2–14% filled, orientation stubs remain) → none promoted; all stay `library-seed-rich`.** No new coords this pass.

> **2026-10-12 update (Hot Round-4 B):** Hot densify Round-4 Batch B (D-2026-10-12-31) raised aztec / phoenician / anatolia-hittite / nubia-kush / elam-iran to ~71 sources / 42–44 sites / 51 objects / 69 claims. **Numeric OK; quality/honesty fail (coords 7–18%) → none promoted.** **All 10 hot packs now Round-4 band numerically; still 0 hot fact-library promotions.** No new coords this pass.

> **2026-10-13 update (Seed J milestone):** Seed densify Batch J (D-2026-10-13-04) raised ancestral-pueblo / great-zimbabwe / west-africa-medieval / hallstatt-celtic / nuragic-sardinia / rapa-nui to ~48 sources / 23–24 sites / 19 objects / 43 claims; status remains `library-seed-rich`. **All 21 former ~30-source seeds now ~48.** Rapa Nui: outbound UNESCO media only; no hosted moai. No new coords this pass.

> **2026-10-13 update (Seed I):** Seed densify Batch I (D-2026-10-13-03) raised wari / ban-chiang / early-korea / moche / cahokia to ~48 sources / 23 sites / 19 objects / 43 claims; status remains `library-seed-rich`. **15 of 21 former ~30-source seeds now ~48.** Remaining 6 for Batch J. No new coords this pass.

> **2026-10-13 update (Seed H):** Seed densify Batch H (D-2026-10-13-02) raised nok-west-africa / lapita-pacific / chavin-andes / tiwanaku / mitanni to ~48 sources / 23 sites / 19 objects / 42–43 claims; status remains `library-seed-rich`. **10 of 21 former ~30-source seeds now ~48.** Remaining 11 for Batches I/J. No new coords this pass.

> **2026-10-13 update (Seed G):** Seed densify Batch G (D-2026-10-13-01) raised levant-ugarit / bmac-oxus / zapotec / jomon-yayoi / dong-son to ~48–49 sources / 22–23 sites / 19 objects / 43 claims; status remains `library-seed-rich`. **5 of 21 former ~30-source seeds now ~48.** Remaining 16 for Batches H/I/J. No new coords this pass.

> **2026-10-12 update (Seed F):** Seed densify Batch F (D-2026-10-12-27) raised ancestral-pueblo / great-zimbabwe / west-africa-medieval / hallstatt-celtic / nuragic-sardinia / rapa-nui to ~30 sources / 15 sites / 26 claims; status remains `library-seed-rich`. **All 21 former ~15-source packs now ~30.** Rapa Nui: outbound UNESCO media only; no hosted moai imagery. No new coords this pass.

> **2026-10-12 update (Seed E):** Seed densify Batch E (D-2026-10-12-26) raised wari / ban-chiang / early-korea / moche / cahokia to ~30 sources / 15 sites / 26 claims; status remains `library-seed-rich`. No new coords this pass.

> **2026-10-12 update (Seed D):** Seed densify Batch D (D-2026-10-12-25) raised nok-west-africa / lapita-pacific / chavin-andes / tiwanaku / mitanni to ~30 sources / 14–15 sites / 26 claims; status remains `library-seed-rich`. No new coords this pass.

> **2026-10-12 update (Seed C):** Seed densify Batch C (D-2026-10-12-24) raised levant-ugarit / bmac-oxus / zapotec / jomon-yayoi / dong-son to ~30 sources / 14–15 sites / 26 claims; status remains `library-seed-rich`. Jōmon UNESCO 1632 component coords (P) on four new sites.

> **2026-10-12 update (Round-2 B):** Hot Round-2 Batch B densify (D-2026-10-12-23) raised aztec / phoenician / anatolia-hittite / nubia-kush / elam-iran to ~48 sources / 23–25 sites / 19 objects / 43 claims; status remains `library-seed-rich` (not fact-library). No new coords this pass.

> **2026-10-12 update (Round-2 A):** Hot Round-2 Batch A densify (D-2026-10-12-22) further raised teotihuacan / classic-maya / inca / angkor / aksum to ~48 sources / 22–24 sites / 19 objects / 42–43 claims; status remains `library-seed-rich` (not fact-library). Quiriguá + Uxmal coords filled (UNESCO P).

> **2026-10-12 update:** Hot Batch A densify (D-2026-10-12-19) raised teotihuacan / classic-maya / inca / angkor / aksum toward denser `library-seed-rich` (~30 sources each). 嘻嘻 coords ingest (D-2026-10-12-20): +27 fills, 7 P-upgrades; Yufu left empty. Hot Batch B densify (D-2026-10-12-21) raised aztec / phoenician / anatolia-hittite / nubia-kush / elam-iran to the same denser band (~30 sources / 15–17 sites / ~26 claims each); status remains `library-seed-rich`.

