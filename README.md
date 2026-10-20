# Lin's Ancient Civilization Hypotheses

English | [中文](README.zh.md)

> Collect widely, separate fact from hypothesis, cite every claim — never invent a story.

## Mission

**Lin's Ancient Civilization Hypotheses** (Chinese name: 林的古文明猜想) is an open **archive + read-only API** for ancient civilizations worldwide — with human-readable prose as a presentation layer, not the product itself.

Scope is intentionally **broad**: continents, regions, and cultures across the planet — not limited to any single site or river valley. We collect published evidence, register sources, surface associations as **labeled hypotheses**, and archive reconstructions with explicit uncertainty.

This project is **not** a place for fantasy narratives, forged artifact images, or unverifiable “lost civilization” fiction. Every entry must carry sources. Hypotheses are hypotheses — never presented as established conclusions.

Craft standard: [Design taste](docs/design-taste.md) · [中文](docs/design-taste.zh.md) — quality in what is seen *and* unseen.

## Why not Wikipedia?

Wikipedia is unsurpassed for **breadth** and public collaboration. This repository aims at a different job:

| | Wikipedia | This project |
|--|-----------|--------------|
| Unit of truth | Narrative article | Structured archive entities (source, site, period, object, claim, media) |
| Fact vs guess | Often woven into one prose voice | **Hard split** — `kind: fact` vs `kind: hypothesis`, visible in API and `/ui` |
| Machine use | Scraping / dumps | First-class **read-only API** + citation fail-closed gate |
| Imagery | Community media | **No forged artifact images**; media is outbound-link metadata when rights are clear |

Coverage here is still narrow. Advantage only holds if density, gates, and honesty keep growing.

## Try the API / UI

```bash
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/export_check.py
.venv/bin/python -m api.serve
```

Then open:

- **Browse UI:** [http://127.0.0.1:8080/ui](http://127.0.0.1:8080/ui) — **Chinese by default**; museum-grade restraint; EN switch; fact/hypothesis badges
- **API root:** [http://127.0.0.1:8080/api/v1/](http://127.0.0.1:8080/api/v1/) — principle-first service card
- **OpenAPI:** [http://127.0.0.1:8080/api/v1/docs](http://127.0.0.1:8080/api/v1/docs)

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

## Structured archive

Product core is **archive + read-only API**. JSON Schema: [`schemas/`](schemas/). Structured packs: [`data/structured/`](data/structured/). Model: [`docs/archive-data-model.md`](docs/archive-data-model.md). Gate: `.venv/bin/python tools/export_check.py`. Design: [`docs/design-taste.md`](docs/design-taste.md).

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
├── README.md / README.zh.md
├── LICENSE
├── api/                      # Read-only FastAPI + /ui (api/static/ui.html)
├── schemas/                  # JSON Schema for archive entities
├── data/
│   ├── civilizations/        # Human-readable fact-library Markdown
│   └── structured/           # Machine-readable packs (JSON)
├── docs/                     # Method, architecture, API, design taste, decisions
├── sources/                  # Source registry
├── hypotheses/               # Hypothesis board — labeled HYPOTHESIS
├── deliberations/            # Council sessions — perspective lenses
├── reconstructions/          # Causality & uncertainty
└── tools/export_check.py     # Citation fail-closed gate
```

Templates are marked clearly; they are **not** filled with invented case studies.

**Library status (2026-10-13):** **40** structured packs under `data/structured/` — **9 dense** (`fact-library`, ~68–76 sources) + **31 expanding** (`library-seed-rich`, ~71-source band). Roughly **2800+** registered sources, **1600+** sites, **2600+** claims (structured counts / `export_check`). Coverage map: [`docs/coverage-map.md`](docs/coverage-map.md) · [中文](docs/coverage-map.zh.md). Depth: [`docs/entry-depth.md`](docs/entry-depth.md). Decisions: [`docs/decisions.md`](docs/decisions.md) (incl. D-2026-10-13-08).

**Dense (9):** mesopotamia · egypt · andes · indus · china-bronze · sanxingdui · aegean · olmec · early-maya

**Expanding (31, ~71 sources):** the hot ten plus the other twenty-one Wave-1/2/3 packs share the same density band; **none promoted to `fact-library` yet** — promotion waits on sourced coordinates and thinning orientation stubs, not vanity labels.

**Browse UI:** `/ui` **defaults to Chinese** (one-click EN). Museum-grade restraint; fact/hypothesis badges; no forged artifact imagery.


- **Design taste** — makers’ principles + UI/API/README checklist: [`docs/design-taste.md`](docs/design-taste.md) · [中文](docs/design-taste.zh.md)
- **Entry depth** — required sections, source minimums, status ladder: [`docs/entry-depth.md`](docs/entry-depth.md) · [中文](docs/entry-depth.zh.md)
- **Entry detail UI** — report columns as primary surface: [`docs/entry-detail-ui.md`](docs/entry-detail-ui.md) · [中文](docs/entry-detail-ui.zh.md)
- **Decisions** — dated scope choices: [`docs/decisions.md`](docs/decisions.md) · [中文](docs/decisions.zh.md)
- **Architecture** — layers, entities, invariants, storage path: [`docs/architecture.md`](docs/architecture.md) · [中文](docs/architecture.zh.md)
- **Deliberation Council** — multi-lens audit; FUTURE_WINDOW: [`docs/council.md`](docs/council.md) · [中文](docs/council.zh.md) · [`deliberations/`](deliberations/)
- **Perspective lenses (by reference)** — AI thinking skills, not real-person endorsement: [FHLS-perspectives](https://github.com/liuliuwenzheng/FHLS-perspectives)
- **Public API** — library read-only v0 + cloud-first deliberations (spec): [`docs/api.md`](docs/api.md) · [中文](docs/api.zh.md) · [`openapi.v0.yaml`](docs/openapi.v0.yaml)

## Contribution norms

1. **Cite everything.** No source → do not add the claim.
2. **Separate fact and hypothesis.** Use the templates; keep status fields honest.
3. **No fabricated stories.** No invented dialogues, no forged artifact photos, no “secret archives” without verifiable citation.
4. **No client / cost / private business data** in this repo.
5. **Publish or delete this repository** only with the owner's explicit approval.
6. Prefer open-access or clearly citable references; note access dates for URLs.
7. **Design craft** — follow [`docs/design-taste.md`](docs/design-taste.md); do not paper over thin archive with decoration.

Full guide: [`docs/contributing.md`](docs/contributing.md)

## Disclaimer

**Hypotheses in this repository are not established historical or archaeological conclusions.**

Entries under `hypotheses/` and speculative parts of `reconstructions/` are working ideas for discussion and further checking. Readers and contributors must not treat them as proven fact. When evidence conflicts, record both sides; when evidence is thin, say so.

The fact library aims for careful, sourced summaries — it is still a living draft and may contain errors. Corrections with better sources are welcome.

Council seat names refer to **AI-generated thinking lenses** from FHLS-perspectives. They do **not** mean those persons endorse this repository or any deliberation.

## License

Code and documentation: **MIT** — see [`LICENSE`](LICENSE).

Cited third-party texts, images, and data remain under their original rights. Do not paste copyrighted material wholesale; link and cite instead. Do not upload forged or mislabeled artifact imagery.

**Image files:** `data/media-files/` holds web-sized copies of openly licensed images (Public Domain / CC0 / CC BY / CC BY-SA). The MIT license does **not** apply to them; each keeps its own license, with author, license URL, and source page listed in `data/media-files/<pack>/ATTRIBUTION.md`. CC BY-SA files are shared alike. See [`data/media-files/README.md`](data/media-files/README.md).
