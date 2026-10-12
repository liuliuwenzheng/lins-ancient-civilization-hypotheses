# Global coverage map — callable archive packs

[中文](coverage-map.zh.md) | English

**Decision:** [D-2026-10-12-12](decisions.md#d-2026-10-12-12--global-coverage-map--wave-1-shells) (Wave-1 opened) · [D-2026-10-12-13](decisions.md#d-2026-10-12-13--wave-1-densify-to-library-seed-rich) (Wave-1 densified) · [D-2026-10-12-14](decisions.md#d-2026-10-12-14--wave-2-shells) (Wave-2 opened)  
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
| **Shell** | `library-seed` Wave-1/Wave-2 pack — real Sources, minimal Sites/Claims, sections may be empty |
| **Expanding** | `library-seed-rich` — densified Wave-1 pack (usable archive density; not yet `fact-library`) |
| **Missing** | Not opened yet; listed for Wave-2/3 planning |

## Matrix by world region

| Region | HAVE (dense) | HAVE (expanding) | MISSING (priority) | Wave |
|--------|--------------|------------------|--------------------|------|
| **Mesopotamia / SW Iran** | Mesopotamia | Elam (`library-seed-rich`) | Later Iranian empires (Achaemenid+) as separate packs | 1 densified; 2 later |
| **Nile / NE Africa** | Egypt | Nubia–Kush (`library-seed-rich`); Aksum (`library-seed`) | Later Christian Nubia split if needed | 1 densified; 2 opened |
| **Anatolia / Levant / E Med** | Aegean | Hittite; Ugarit (`library-seed-rich`); Mitanni; Phoenician (`library-seed`) | Cyprus Late Bronze; Carthage densify | 1 densified; 2 opened |
| **Central / South Asia** | Indus | BMAC/Oxus (`library-seed-rich`) | Vedic/early Historic Ganga; Gandhara; Sri Lanka early | 1 densified; 2–3 |
| **East Asia** | China Bronze; Sanxingdui | Jōmon/Yayoi (`library-seed-rich`); Early Korea (`library-seed`) | Later Zhou–Han overview split | 1 densified; 2 opened |
| **Southeast Asia** | — | Đông Sơn (`library-seed-rich`); Ban Chiang (`library-seed`) | Angkor/Funan later | 1 densified; 2 opened |
| **West / Sahel Africa** | — | Nok (`library-seed-rich`) | Ghana/Mali empires (medieval); Great Zimbabwe; Ife/Benin | 1 densified; 2–3 |
| **Mesoamerica** | Olmec; Early Maya | Teotihuacan; Zapotec (`library-seed-rich`); Classic Maya (`library-seed`) | Aztec/Mexica; Mixtec | 1 densified; 2 opened |
| **Andes / South America** | Andes (Caral–Norte Chico) | Chavín; Tiwanaku; Wari (`library-seed`) | Moche; Inca | 2 opened; 3 later |
| **Oceania / Pacific** | — | Lapita (`library-seed-rich`) | Polynesian chiefdoms; Rapa Nui (careful, thin archive ethics) | 1 densified; 3 |
| **Europe (beyond Aegean)** | — | — | Iberia Copper/Bronze; Hallstatt/La Tène; Nuragic | 3 |
| **North America** | — | — | Mississippian / Cahokia; Ancestral Puebloan (complex society bar) | 3 |

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

## Wave-2 packs (opened D-2026-10-12-14)

Status: **`library-seed`**. Typical shell density: **5 Sources**, **2–3 Sites**, **1 Period**, **1 Object**, **1 sourced Claim**, **0 media**. Coords null unless a registered source publishes them. **No invented finds, page numbers, or media art.** Generator: `tools/wave2_shells/generate_wave2.py`.

| Pack id | Civilization id | Status | Region gap closed |
|---------|-----------------|--------|-------------------|
| `chavin-andes` | `civ-chavin` | library-seed | Early Horizon Andes (beside Caral pack) |
| `tiwanaku` | `civ-tiwanaku` | library-seed | Titicaca highland Middle Horizon |
| `wari` | `civ-wari` | library-seed | Ayacucho / Middle Horizon expansion |
| `classic-maya` | `civ-classic-maya` | library-seed | Classic lowland Maya (beside early-maya) |
| `aksum` | `civ-aksum` | library-seed | Ethiopian highland / Red Sea kingdom |
| `ban-chiang` | `civ-ban-chiang` | library-seed | NE Thailand prehistoric (beside Đông Sơn) |
| `early-korea` | `civ-early-korea` | library-seed | Mumun–early states peninsula |
| `mitanni` | `civ-mitanni` | library-seed | LBA Hurrian / Upper Mesopotamia |
| `phoenician` | `civ-phoenician` | library-seed | Levantine coast + western Punic nodes |

## Wave-3 (later / still Missing)

Mississippian/Cahokia; Ancestral Puebloan; Great Zimbabwe; West African medieval empires (Ghana/Mali); Iberian Bronze; Hallstatt/La Tène; Nuragic; Rapa Nui (ethics-first); full Inca; Moche; Aztec/Mexica; Mixtec; Angkor/Funan; Cyprus Late Bronze; later Christian Nubia split if needed.

## How users see packs now

- **API:** `GET /api/v1/civilizations` auto-discovers every `data/structured/*/civilization.json` — Wave-2 packs appear with `status: library-seed`.
- **UI:** `/ui` loads the same list; filter by name. Shells are intentionally thin.
- **Gate:** `tools/export_check.py` — citation fail-closed for all packs (**29** after Wave-2).

## Product stance

**29 packs callable: 9 dense + 11 Wave-1 rich + 9 Wave-2 shells.** Honesty of status beats vanity of count. Next: densify Wave-2 toward `library-seed-rich`, continue Wave-1/media/coord fill, then Wave-3 openings where archives allow.
