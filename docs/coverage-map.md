# Global coverage map — callable archive packs

[中文](coverage-map.zh.md) | English

**Decision:** [D-2026-10-12-12](decisions.md#d-2026-10-12-12--global-coverage-map--wave-1-shells)  
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
| **Shell** | `library-seed` Wave-1 pack — real Sources, minimal Sites/Claims, sections may be empty |
| **Missing** | Not opened yet; listed for Wave-2/3 planning |

## Matrix by world region

| Region | HAVE (dense) | HAVE (shell) | MISSING (priority) | Wave |
|--------|--------------|--------------|--------------------|------|
| **Mesopotamia / SW Iran** | Mesopotamia | Elam | Later Iranian empires (Achaemenid+) as separate packs | 1 done; 2 later |
| **Nile / NE Africa** | Egypt | Nubia–Kush | Aksum; later Christian Nubia split if needed | 1 done; 2–3 |
| **Anatolia / Levant / E Med** | Aegean | Hittite Anatolia; Ugarit/Levant | Mitanni; Phoenician city-states; Cyprus Late Bronze | 1 done; 2 |
| **Central / South Asia** | Indus | BMAC/Oxus | Vedic/early Historic Ganga; Gandhara; Sri Lanka early | 1 done; 2–3 |
| **East Asia** | China Bronze; Sanxingdui | Jōmon/Yayoi | Korean Mumun/early states; later Zhou–Han overview split | 1 done; 2 |
| **Southeast Asia** | — | Đông Sơn | Ban Chiang (separate if needed); Angkor/Funan later | 1 done; 2–3 |
| **West / Sahel Africa** | — | Nok | Ghana/Mali empires (medieval); Great Zimbabwe; Ife/Benin | 1 done; 2–3 |
| **Mesoamerica** | Olmec; Early Maya | Teotihuacan; Zapotec | Classic Maya (full); Aztec/Mexica; Mixtec | 1 done; 2 |
| **Andes / South America** | Andes (Caral–Norte Chico) | — | Chavín (sub-note or pack); Tiwanaku; Wari; Moche; Inca | 2–3 |
| **Oceania / Pacific** | — | Lapita | Polynesian chiefdoms; Rapa Nui (careful, thin archive ethics) | 1 done; 3 |
| **Europe (beyond Aegean)** | — | — | Iberia Copper/Bronze; Hallstatt/La Tène; Nuragic | 3 |
| **North America** | — | — | Mississippian / Cahokia; Ancestral Puebloan (complex society bar) | 3 |

## Wave-1 packs opened (2026-10-12)

Shell status `library-seed`. Each has ≥5 registered Sources (P/S/T graded), 1–3 grounded Sites, 1 Period, 1 assemblage Object, 1 sourced fact Claim. **No invented finds, coords, or media art.**

| Pack id | Civilization id | Region gap closed |
|---------|-----------------|-------------------|
| `elam-iran` | `civ-elam-iran` | SW Iran beside Mesopotamia |
| `nubia-kush` | `civ-nubia-kush` | Nile south of Egypt |
| `anatolia-hittite` | `civ-anatolia-hittite` | Anatolian plateau |
| `levant-ugarit` | `civ-levant-ugarit` | Northern Levant LBA |
| `bmac-oxus` | `civ-bmac-oxus` | Central Asian oases |
| `nok-west-africa` | `civ-nok-west-africa` | West Africa Iron Age |
| `teotihuacan` | `civ-teotihuacan` | Central Mexican Classic |
| `zapotec` | `civ-zapotec` | Oaxaca / Monte Albán |
| `lapita-pacific` | `civ-lapita-pacific` | Pacific Austronesian dispersal |
| `dong-son` | `civ-dong-son` | Mainland SEA bronze drums |
| `jomon-yayoi` | `civ-jomon-yayoi` | Japanese archipelago |

## Pre-existing dense packs (unchanged this decision)

`mesopotamia`, `egypt`, `andes`, `indus`, `china-bronze`, `sanxingdui`, `aegean`, `olmec`, `early-maya` — continue thickening; **do not thin** to “match” shells.

## Wave-2 (next)

Priority rationale: fill remaining continental holes and later Andean phases without duplicating Wave-1.

Suggested: **Chavín / Early Horizon Andes** (or Tiwanaku + Wari as separate packs), **Classic Maya** (beyond early-maya scope), **Aksum**, **Ban Chiang** (if distinct from Đông Sơn), **Korean peninsula early states**, **Mitanni / Hurrian**, **Phoenician / Carthaginian**.

## Wave-3 (later)

Mississippian/Cahokia; Ancestral Puebloan; Great Zimbabwe; West African medieval empires; Iberian Bronze; Hallstatt; Nuragic; Rapa Nui (ethics-first); full Inca.

## How users see packs now

- **API:** `GET /api/v1/civilizations` auto-discovers every `data/structured/*/civilization.json` — shells appear alongside dense packs with `status: library-seed`.
- **UI:** `/ui` loads the same list; filter by name. Shells show thin Sites/Claims until density passes.
- **Gate:** `tools/export_check.py` — citation fail-closed for all packs.

## Product stance

**Open shells now + keep thickening the nine dense packs.** Do not wait for perfect density before listing in API/UI. Honesty of status beats vanity of count.
