# Global coverage map — callable archive packs

[中文](coverage-map.zh.md) | English

**Decision:** [D-2026-10-12-12](decisions.md#d-2026-10-12-12--global-coverage-map--wave-1-shells) (Wave-1 opened) · [D-2026-10-12-13](decisions.md#d-2026-10-12-13--wave-1-densify-to-library-seed-rich) (Wave-1 densified) · [D-2026-10-12-14](decisions.md#d-2026-10-12-14--wave-2-shells) (Wave-2 opened) · [D-2026-10-12-15](decisions.md#d-2026-10-12-15--wave-3-shells) (Wave-3 opened) · [D-2026-10-12-16](decisions.md#d-2026-10-12-16--wave-2-densify-to-library-seed-rich) (Wave-2 densified)  
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
| **Shell** | `library-seed` Wave-3 (and earlier undensified) pack — real Sources, minimal Sites/Claims, sections may be empty |
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
| **Southeast Asia** | — | Đông Sơn; Ban Chiang (`library-seed-rich`); Angkor (`library-seed`) | Funan split if needed | 1–2 densified; 3 opened |
| **West / Sahel Africa** | — | Nok (`library-seed-rich`); West Africa medieval (`library-seed`); Great Zimbabwe (`library-seed`) | Ife/Benin later | 1 densified; 3 opened |
| **Mesoamerica** | Olmec; Early Maya | Teotihuacan; Zapotec; Classic Maya (`library-seed-rich`); Aztec (`library-seed`) | Mixtec later | 1–2 densified; 3 opened |
| **Andes / South America** | Andes (Caral–Norte Chico) | Chavín; Tiwanaku; Wari (`library-seed-rich`); Moche; Inca (`library-seed`) | — | 2 densified; 3 opened |
| **Oceania / Pacific** | — | Lapita (`library-seed-rich`); Rapa Nui (`library-seed`) | Broader Polynesian chiefdoms | 1 densified; 3 opened |
| **Europe (beyond Aegean)** | — | Hallstatt; Nuragic (`library-seed`) | Iberia Copper/Bronze; fuller La Tène | 3 opened |
| **North America** | — | Cahokia; Ancestral Puebloan (`library-seed`) | Broader Mississippian peers | 3 opened |

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

## Wave-3 packs (opened D-2026-10-12-15)

Status: **`library-seed`**. Typical shell density: **5 Sources**, **2–3 Sites**, **1 Period**, **1 Object**, **1 sourced Claim**, **0 media**. Coords null unless a registered source publishes them. **No invented finds, page numbers, or media art.** Generator: `tools/wave3_shells/generate_wave3.py`.

| Pack id | Civilization id | Status | Region gap closed |
|---------|-----------------|--------|-------------------|
| `cahokia` | `civ-cahokia` | library-seed | Mississippian / American Bottom |
| `ancestral-pueblo` | `civ-ancestral-pueblo` | library-seed | Colorado Plateau / Chaco–Mesa Verde |
| `great-zimbabwe` | `civ-great-zimbabwe` | library-seed | Southern African Iron Age capital |
| `west-africa-medieval` | `civ-west-africa-medieval` | library-seed | Ghana–Mali–Songhai Sahelian empires |
| `hallstatt-celtic` | `civ-hallstatt-celtic` | library-seed | Alpine Early Iron Age / Hallstatt |
| `nuragic-sardinia` | `civ-nuragic-sardinia` | library-seed | Sardinian Nuragic towers |
| `rapa-nui` | `civ-rapa-nui` | library-seed | Polynesian Rapa Nui (ethics-first) |
| `inca` | `civ-inca` | library-seed | Tawantinsuyu Late Horizon |
| `moche` | `civ-moche` | library-seed | North-coast Peru EIP |
| `aztec` | `civ-aztec` | library-seed | Mexica / Triple Alliance |
| `angkor` | `civ-angkor` | library-seed | Khmer Angkorian capital landscape |

**Still Missing (later):** Iberian Copper/Bronze; fuller La Tène; Mixtec; Funan split; Cyprus LBA densify; Ife/Benin; broader Polynesian chiefdoms; later Christian Nubia split if needed.

## How users see packs now

- **API:** `GET /api/v1/civilizations` auto-discovers every `data/structured/*/civilization.json` — Wave-3 shells appear with `status: library-seed`; Wave-2 with `library-seed-rich`.
- **UI:** `/ui` loads the same list; filter by name. Shells are intentionally thin.
- **Gate:** `tools/export_check.py` — citation fail-closed for all packs (**40** after Wave-3 + Wave-2 densify).

## Product stance

**40 packs callable: 9 dense + 11 Wave-1 rich + 9 Wave-2 rich + 11 Wave-3 shells.** Honesty of status beats vanity of count. Next: densify Wave-3 toward `library-seed-rich`, continue coord/media fill on earlier packs, open remaining Missing where archives allow.
