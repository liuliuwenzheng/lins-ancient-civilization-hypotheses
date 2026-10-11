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

Details: [`docs/methodology.md`](docs/methodology.md)

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
│   └── contributing.md       # How to contribute
├── data/civilizations/       # Fact-library entries (+ _template.md)
├── sources/                  # Source registry (+ _template.md)
├── hypotheses/               # Hypothesis board (+ _template.md) — labeled HYPOTHESIS
└── reconstructions/          # Reconstructions with causality & uncertainty (+ _template.md)
```

Templates are marked clearly; they are **not** filled with invented case studies.

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

## License

Code and documentation: **MIT** — see [`LICENSE`](LICENSE).

Cited third-party texts, images, and data remain under their original rights. Do not paste copyrighted material wholesale; link and cite instead. Do not upload forged or mislabeled artifact imagery.
