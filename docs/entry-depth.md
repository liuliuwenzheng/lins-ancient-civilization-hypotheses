# Fact-library entry depth

English | [中文](entry-depth.zh.md)

> Rich, comprehensive, and real. Thin stubs are not meaningful library entries.
> Related: [`_template.md`](../data/civilizations/_template.md) · [`source-grading.md`](source-grading.md) · [`methodology.md`](methodology.md)

---

## Why depth matters

A civilization entry that only restates a one-paragraph summary does not help readers, contributors, or downstream APIs. The fact library exists to **accumulate verifiable knowledge** — geography, chronology, sites, institutions, writing, economy, material culture, contacts, and research history — with every non-trivial claim tied to a registered `src-*`.

Integrity beats speed. Prefer fewer well-cited sections over many decorative sentences.

## Required sections (template v1)

Copy [`data/civilizations/_template.md`](../data/civilizations/_template.md). All body sections are **FACT only**. Hypotheses belong in `hypotheses/`.

1. **Summary**
2. **Geography & environment**
3. **Chronology / periodization** (table preferred; cite the scheme used)
4. **Key sites**
5. **Urbanism, architecture & institutions**
6. **Writing, language & administration** (omit if not applicable)
7. **Economy, subsistence & craft**
8. **Material culture** (highlights with cites)
9. **External contacts** (only when sourced; otherwise omit the heading)
10. **Research history** (brief)
11. **Sources**
12. **Related civilizations**
13. **Notes** (open scholarly debates — not project hypotheses)

## Minimums for a major-civilization overview

When expanding a **major** overview (e.g. Mesopotamia, Egypt, Indus, China Bronze, Andes) toward a durable library entry:

| Gate | Expectation |
|------|-------------|
| Registered sources | Aim **~8–15+** distinct `src-*` entries (mix of P and S; T only for orientation) |
| Section cites | **Every major section** above must cite at least one registered source |
| No filler | Do not pad with vague adjectives, invented atmosphere, or unsourced “color” |
| Language | **Bilingual CN + EN** preferred for body text (parallel paragraphs OK) |
| Page numbers | Cite pages only when you have inspected the edition; otherwise omit |
| Images | No forged or mislabeled artifact images |

Smaller site-focused entries (e.g. a single mound) may use fewer sources, but must still fill applicable sections and cite every claim.

## Status ladder

| Status | Meaning |
|--------|---------|
| `draft` | Scaffold / placeholder; `sources: []` allowed |
| `library-seed` | Cited short overview; structure may still be thin |
| `library-seed-rich` | New template sections substantially filled; sources growing toward the major-civ minimum |
| `fact-library` | Sections genuinely filled, major claims cited, source count meets the major-civ target (or justified for a site entry) |

Promote to `fact-library` only when depth is solid — not as a cosmetic label.

## What belongs in Notes (not Hypotheses)

- Open scholarly debates (e.g. ranking “first city,” absolute chronology disputes, primacy titles in book marketing)
- Limits of this entry’s chronological scope
- Conflicts between older excavation reports and modern secondary syntheses

Do **not** use Notes for speculative cross-civilization storytelling. Those go to `hypotheses/` with an explicit **HYPOTHESIS** label.

## Refusal rules

- Refuse unverifiable color (mood, fictional scenes, anonymous “experts say”)
- Refuse invented page numbers, fake excavation IDs, or forged images
- Refuse mixing fact paragraphs with unlabeled speculation
