---
id: delib-2026-10-12-global-coverage
title: "Deliberation: Global coverage — Wave-1 shells now vs wait for density"
status: synthesized
created: 2026-10-12
updated: 2026-10-12
targets:
  civilizations:
    - civ-elam-iran
    - civ-nubia-kush
    - civ-anatolia-hittite
    - civ-levant-ugarit
    - civ-bmac-oxus
    - civ-nok-west-africa
    - civ-teotihuacan
    - civ-zapotec
    - civ-lapita-pacific
    - civ-dong-son
    - civ-jomon-yayoi
  hypotheses: []
  reconstructions: []
  sources: []
seats:
  - deming-perspective
  - steve-jobs-perspective
  - elon-musk-perspective
  - darwin-perspective
  - descartes-perspective
  - qianxuesen-perspective
  - mozi-perspective
facilitator: "cloud-orchestrator"
question: "User asks for more complete world coverage and earlier usability. Should we open Wave-1 shells across geographic gaps now while continuing to thicken the existing nine dense packs — or wait until each new civ reaches fact-library density before listing in API/UI?"
perspective: true
person_endorsement: false
lens_catalog: "https://github.com/liuliuwenzheng/FHLS-perspectives"
---

# Deliberation: Global coverage — Wave-1 shells now vs wait for density

> **Perspective lenses only.** AI-generated thinking aids from [FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives).  
> `perspective: true` · `person_endorsement: false` — named persons do **not** endorse this project or this session.

## Intake

- **Question:** Open geographic Wave-1 shells now for API/UI discoverability, while thickening the nine dense packs — or gate listing on perfect density?
- **Target ids:** eleven Wave-1 `civ-*` shells + coverage map; existing nine dense packs remain untouched in depth.
- **Cited sources (must resolve to `src-*` when claiming fact):** project-meta (export_check pack discovery, coverage-map scope). Archaeological facts belong only inside registered pack sources.

## Parallel lens notes

### deming-perspective

- `perspective: true` · `person_endorsement: false`
- Quality is a **system**: citation gate + status ladder (`library-seed` vs `fact-library`) already encode variation. Opening shells without inventing archaeology **reduces** special-cause risk of silent geographic holes.
- Measure: export_check green; shell packs must keep `status: library-seed` until density passes; never demote dense packs to “match” shells.
- Continual improvement: Wave-1 list → thicken by WARN/coord/media playbooks already used on the nine.

### steve-jobs-perspective

- `perspective: true` · `person_endorsement: false`
- Product is a **careful archive you can query**, not a finished encyclopedia. Users cannot use what they cannot see.
- Listing shells in API/UI with honest thinness is better than a beautiful nine-civ silo that pretends the rest of the world does not exist.
- Cut Wikipedia vanity. Say “shell” in status and README. Typography and badges already carry craft — empty media stays empty.

### elon-musk-perspective

- `perspective: true` · `person_endorsement: false`
- First principles: atoms (Source/Site/Period/Object/Claim) + auto-discovery loader + fail-closed gate. Physics of coverage = **more valid pack directories**, not longer essays.
- Delete the requirement “perfect density before list.” That is a process fetish, not a physics constraint.
- Parallelize: shells land now; density passes continue on the nine and then on shells by regional priority.

### darwin-perspective

- `perspective: true` · `person_endorsement: false`
- Selection pressure favors packs that close real geographic niches (Africa, Oceania, SEA, Central Asia, Anatolia/Levant, highland Mesoamerica) without duplicating existing niches.
- Wave-1 choice set is an adaptive radiation into empty niches; Wave-2/3 are further speciation (Tiwanaku, Classic Maya, Aksum…), not a single leap to “all civilizations.”

### descartes-perspective

- `perspective: true` · `person_endorsement: false`
- Doubt Wikipedia-breadth. Clear and distinct: only claims with registered `src-*` enter fact columns; shells may have empty geography sections.
- Method: open shell → register 3–8 real sources → one sourced fact claim minimum → thicken only with evidence.
- Reject invented coordinates and forged media as method errors, not schedule tradeoffs.

### qianxuesen-perspective

- `perspective: true` · `person_endorsement: false`
- Systems engineering: coverage map is the **top-level WBS**; Wave-1 is the first increment; dense packs are the high-maturity subsystems that keep shipping improvements.
- Interfaces: API discovery is already pack-directory-based — no hardcoded nine-civ limit. UI inherits the same list.
- Risk control: decision record + deliberation outputs; do not thin dense packs.

### mozi-perspective

- `perspective: true` · `person_endorsement: false`
- Impartial care: a West African or Pacific pack deserves the same citation honesty as Mesopotamia — not an encyclopedia paragraph without sources.
- Benefit the users who need a **map of what exists** in the archive; benefit future deepeners with honest shells.
- Against waste: do not spend craft on fake media to hide thinness.

## Cross-examination

| Challenge | From seat | Toward | Notes |
|-----------|-----------|--------|-------|
| Shells will look “fake complete” | Descartes / Deming | Jobs / Musk | Mitigate with `library-seed` status + coverage map labels + README poetry tree |
| Opening 11 shells distracts from dense quality | Deming | Musk | Parallel tracks; D-2026-10-12-12 forbids thinning dense packs |
| Too many Wave-1 ids | Darwin | Coverage map | Eleven chosen to close continents; Wave-2/3 absorb the rest |
| Andes later phases missing in Wave-1 | Qian / Darwin | Map | Explicit Wave-2 (Chavín/Tiwanaku/Wari) — cleaner than stuffing into Caral pack |

## Facilitator synthesis

Consensus: **open Wave-1 shells now and keep thickening the existing nine.** Do not wait for perfect density before API/UI listing. Status honesty + citation gate + coverage map are the quality system. Geographic gap-closing beats vanity article count.

---

## Outputs

### FACT_NOTES

- Loader and UI already auto-discover `data/structured/*/civilization.json`; no hardcoded nine-pack ceiling.
- Nine existing packs remain `fact-library` density tracks; Wave-1 shells are `library-seed` with real registered sources only.
- Coverage scope is complex societies with archaeological archives, not modern nations or Wikipedia stubs.
- `export_check` is the fail-closed gate for all packs (20 after Wave-1).

### HYPOTHESIS_CHALLENGES

- Challenge: “Wait for fact-library density before listing.” Rejected — delays usability without improving citation integrity.
- Challenge: “Merge Tiwanaku/Wari into Andes pack now.” Deferred — separate Wave-2 packs (or explicit sub-notes) cleaner than scope creep in Caral–Norte Chico.
- Challenge: “Ban Chiang instead of Đông Sơn.” Đông Sơn chosen for clearer complex-society bronze-drum archive; Ban Chiang may open as Wave-2 if distinct.

### OPEN_QUESTIONS

- Exact Wave-2 ordering after Andes later phases vs Classic Maya vs Aksum?
- When do shells promote `library-seed` → `library-seed-rich` → `fact-library` (source-count + section-cite thresholds already in entry-depth)?
- Hermes/嘻嘻 local bibliography handoff for Chinese/Andean/Indus coords — still pending human transfer.

### FUTURE_WINDOW

- Users see 20 civilizations in API/UI immediately (9 dense + 11 shells).
- Next engineering: density passes on shells by WARN playbook; Wave-2 pack openings; optional UI badge for `library-seed`.
- Do not fabricate media art; do not invent archaeology to “complete” the map.
