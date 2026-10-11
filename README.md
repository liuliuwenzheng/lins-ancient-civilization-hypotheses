# Lin's Ancient Civilization Hypotheses

English | [中文](README.zh.md)

> Collect widely, separate fact from hypothesis, cite every claim — never invent a story.

## Mission

**Lin's Ancient Civilization Hypotheses** (Chinese name: 林的古文明猜想) is an open library and hypothesis board for ancient civilizations worldwide.

Scope is intentionally **broad**: continents, regions, and cultures across the planet — not limited to any single site or river valley. We collect published evidence, register sources, surface associations as **labeled hypotheses**, and archive reconstructions with explicit uncertainty.

This project is **not** a place for fantasy narratives, forged artifact images, or unverifiable “lost civilization” fiction. Every entry must carry sources. Hypotheses are hypotheses — never presented as established conclusions.

## Four-stage method

| Stage | Name | What happens |
|-------|------|----------------|
| 1 | **Collect** | Gather references (excavation reports, corpora, museum catalogs, peer-reviewed surveys) into `sources/` |
| 2 | **Build library** | Create / update civilization entries in `data/civilizations/` as a **fact library** (dated, cited, no speculation in the fact columns) |
| 3 | **Discover associations** | Record cross-links and tentative patterns on the **hypothesis board** in `hypotheses/` — each item must be labeled **HYPOTHESIS** |
| 4 | **Reconstruct & archive causality** | Write reconstructions in `reconstructions/` that link facts + hypotheses, state causal claims carefully, and mark uncertainty |

**Hard rule:** fact columns and hypothesis columns stay separate. Do not mix them in one undifferentiated paragraph.

**Deliberation Council:** before material hardens, an optional multi-lens audit (Facilitator + seats from [FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives)) produces FACT_NOTES / HYPOTHESIS_CHALLENGES / OPEN_QUESTIONS / FUTURE_WINDOW. Lenses are AI perspectives (`perspective: true`, `person_endorsement: false`) — not endorsements by named persons. Prefer a cloud API for live conversational review; published sessions live in `deliberations/`.

Details: [`docs/methodology.md`](docs/methodology.md) · Council: [`docs/council.md`](docs/council.md)

## Source grading

Every source is registered and graded. Rough tiers:

| Tier | Label | Typical examples |
|------|--------|------------------|
| **P** | Primary | Excavation reports, inscriptions, curated museum catalogs of objects |
| **S** | Secondary | Peer-reviewed syntheses, handbooks, academic monographs |
| **T** | Tertiary | Encyclopedias, textbooks, reputable overviews |
| **U** | Uncertain | Incomplete citations, paywalled-only abstracts, contested attributions |

How to cite and grade: [`docs/source-grading.md`](docs/source-grading.md)

## Repository map

```
lins-ancient-civilization-hypotheses/
├── README.md                 # English (this file)
├── README.zh.md              # Chinese
├── LICENSE                   # MIT
├── docs/
│   ├── methodology.md        # Four stages + fact/hypothesis separation
│   ├── source-grading.md     # Source tiers & citation practice
│   ├── contributing.md       # How to contribute
│   ├── architecture.md       # System layers & entity model (EN)
│   ├── architecture.zh.md    # 架构说明（中文）
│   ├── council.md            # Deliberation Council (EN)
│   ├── council.zh.md         # 审议圆桌（中文）
│   ├── api.md                # Public API design v0 (EN)
│   ├── api.zh.md             # 开放接口设计 v0（中文）
│   ├── openapi.v0.yaml       # OpenAPI stub (library + deliberations)
│   ├── decisions.md          # Dated project decisions (EN)
│   ├── decisions.zh.md       # 项目决策记录（中文）
│   ├── entry-depth.md        # Fact-library depth standard (EN)
│   └── entry-depth.zh.md     # 事实库条目深度标准（中文）
├── data/civilizations/       # Fact-library entries (+ seed shells, _template.md)
├── sources/                  # Source registry (+ _template.md)
├── hypotheses/               # Hypothesis board (+ _template.md) — labeled HYPOTHESIS
├── deliberations/            # Council sessions (+ _template.md) — perspective lenses
└── reconstructions/          # Reconstructions with causality & uncertainty (+ _template.md)
```

Templates are marked clearly; they are **not** filled with invented case studies.

**Library status (2026-10-11):** nine civilization entries exist under `data/civilizations/`. Mesopotamia (`civ-mesopotamia`) is the depth pilot at **`fact-library`** under the enriched template; the others remain **`library-seed`** pending the same enrichment. Depth rules: [`docs/entry-depth.md`](docs/entry-depth.md). Dated choices: [`docs/decisions.md`](docs/decisions.md).

- **Entry depth** — required sections, source minimums, status ladder: [`docs/entry-depth.md`](docs/entry-depth.md) · [中文](docs/entry-depth.zh.md)
- **Decisions** — dated scope choices (seats, cloud spec-first, seed regions, deepen seeds): [`docs/decisions.md`](docs/decisions.md) · [中文](docs/decisions.zh.md)
- **Architecture** — layers, entities, invariants, storage path: [`docs/architecture.md`](docs/architecture.md) · [中文](docs/architecture.zh.md)
- **Deliberation Council** — multi-lens audit before entries harden; conversational FUTURE_WINDOW: [`docs/council.md`](docs/council.md) · [中文](docs/council.zh.md) · sessions in [`deliberations/`](deliberations/)
- **Perspective lenses (by reference)** — AI thinking skills, not real-person endorsement: [FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives)
- **Public API (design)** — library read-only v0 + cloud-first deliberations: [`docs/api.md`](docs/api.md) · [中文](docs/api.zh.md) · [`openapi.v0.yaml`](docs/openapi.v0.yaml)

## Contribution norms

1. **Cite everything.** No source → do not add the claim.
2. **Separate fact and hypothesis.** Use the templates; keep status fields honest.
3. **No fabricated stories.** No invented dialogues, no forged artifact photos, no “secret archives” without verifiable citation.
4. **No client / cost / private business data** in this repo.
5. **Publish or delete this repository** only with the owner's explicit approval.
6. Prefer open-access or clearly citable references; note access dates for URLs.

Full guide: [`docs/contributing.md`](docs/contributing.md)

## Disclaimer

**Hypotheses in this repository are not established historical or archaeological conclusions.**

Entries under `hypotheses/` and speculative parts of `reconstructions/` are working ideas for discussion and further checking. Readers and contributors must not treat them as proven fact. When evidence conflicts, record both sides; when evidence is thin, say so.

The fact library aims for careful, sourced summaries — it is still a living draft and may contain errors. Corrections with better sources are welcome.

Council seat names refer to **AI-generated thinking lenses** from FHLS-perspectives. They do **not** mean those persons endorse this repository or any deliberation.

## License

Code and documentation: **MIT** — see [`LICENSE`](LICENSE).

Cited third-party texts, images, and data remain under their original rights. Do not paste copyrighted material wholesale; link and cite instead. Do not upload forged or mislabeled artifact imagery.
