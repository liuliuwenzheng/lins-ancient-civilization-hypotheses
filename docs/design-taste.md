# Design taste

English | [中文](design-taste.zh.md)

> Adapted from Paul Graham’s [*Taste for Makers*](http://www.paulgraham.com/taste.html) and Jobs-style craft: quality in what is seen *and* unseen. Product core remains **archive + read-only API**; prose and `/ui` are presentation layers — never a substitute for citable structure.

Inspired in part by a public compilation of Graham’s essay ([Jaden_riku / X](https://x.com/Jaden_riku/status/2108876904002670873)). Credit the essay; do not copy copyrighted text wholesale.

## What we are designing

| Layer | Role | Beauty means |
|-------|------|----------------|
| **Archive** | JSON packs + schemas + citation gate | Honest IDs, fail-closed facts, no decorative fields |
| **API** | Read-only `/api/v1/…` | Clear envelopes, stable shape, hypothesis labels unavoidable |
| **Presentation** | README, docs, `/ui` | Typography, restraint, bilingual clarity — **no forged artifact imagery** |

Wikipedia wins coverage. We win **inspectable archive craft**: fact ≠ hypothesis in the data *and* on the screen.

## Principles (makers’ taste → this project)

1. **Simple** — Prefer fewer surfaces that tell the truth over ornament that hides thin structure.
2. **Solves the right problem** — The product is a citable archive + API, not a prettier encyclopedia essay.
3. **Hard work that looks easy** — Dense sourcing and gates stay behind calm UI and short README paths.
4. **Consistency** — Same bilingual names, same `kind` vocabulary (`fact` / `hypothesis`), same pagination fields everywhere.
5. **Restraint** — One accent color; generous whitespace; no stock “relic” photos; no fake parchment textures.
6. **Honesty** — Facts and hypotheses must be **visually and structurally obvious**. A hypothesis badge is not optional chrome.
7. **No decorative lies** — Do not invent coordinates, page numbers, museum photos, or “secret archives” to fill space.
8. **Redesign** — Iterate when denser packs or clearer API envelopes make the old presentation wrong.
9. **Seen and unseen** — Jobs: the back of the cabinet matters. Schemas, `export_check.py`, and load errors are craft too.

## Checklist

### README (EN + ZH)

- [ ] Language switcher first line: `English | [中文](…)` / `[English](…) | 中文`
- [ ] One-line mission before method tables
- [ ] Short **Why not Wikipedia** (honest: narrower coverage, stronger machine-readable integrity)
- [ ] Short **Try the API / UI** with exact local commands — not marketing fluff
- [ ] Link design taste, architecture, archive model
- [ ] No forged images; disclaimer still present

### API JSON envelopes

- [ ] List responses keep `{ items, total, count, limit, offset, has_more }`
- [ ] Claims always expose `kind`; hypotheses keep disclaimer when present
- [ ] `sources` on claims expand to refs with `id`, `reliability_tier`, `citation`, `url`
- [ ] Strip internal `_pack` / private keys from public payloads
- [ ] Root `/api/v1/` is principle-first and points to `/ui` and health

### `/ui` archive browse

- [ ] Museum-grade restraint: excellent type, whitespace, **one** accent
- [ ] Bilingual CN/EN toggle (persist preference if practical)
- [ ] Dark / light via `prefers-color-scheme` (optional manual override OK)
- [ ] Flow: civilization → **archive report (columns)** / sites / periods / claims (report is default)
- [ ] Claim **kind badge** visually obvious (`fact` vs `hypothesis`)
- [ ] Sources expandable under each claim
- [ ] Light search / filter; mobile-friendly
- [ ] Research history + registered source lineage visible (no invented fieldwork prose)
- [ ] **Zero** stock or forged artifact photos — structure and type carry beauty
- [ ] Self-contained under `api/static/`; served by the same process as the API

### Docs

- [ ] DeepSeek-Bot style language switcher on bilingual pairs
- [ ] Decisions dated; architecture links design taste briefly
- [ ] Prefer linking sources over pasting copyrighted prose

## Non-goals

- Competing with Wikipedia page count
- Illustrated “museum gallery” of unverified object photos
- Marketing copy that overclaims coverage or certainty

## Related

- [Architecture](architecture.md) · [Archive data model](archive-data-model.md) · [API](api.md) · [Decisions](decisions.md)
