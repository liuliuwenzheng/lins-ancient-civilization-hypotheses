# Project decisions

English | [中文](decisions.zh.md)

> Dated choices that constrain scope. Markdown in this repo remains the source of truth until an implemented API proves otherwise.

Related: [Council](council.md) · [API](api.md) · [Architecture](architecture.md)

---

## 2026-10-11

### D-2026-10-11-1 — Default Council seats (v0) confirmed

**Decision:** Keep the seven FHLS-perspectives seats already listed in [`council.md`](council.md):

1. `deming-perspective`
2. `steve-jobs-perspective`
3. `elon-musk-perspective`
4. `darwin-perspective`
5. `descartes-perspective`
6. `qianxuesen-perspective`
7. `mozi-perspective`

**Notes:** Lenses are AI thinking tools (`perspective: true`, `person_endorsement: false`). Aristotle is **not** seated until a real FHLS catalog entry exists — do not invent a perspective file in this repo.

### D-2026-10-11-2 — Cloud deliberation: spec first, implement later

**Decision:** Cloud deliberation host = **spec-first**. Ship and refine the design in [`api.md` §9](api.md#9-deliberation-council-cloud-first) / [`openapi.v0.yaml`](openapi.v0.yaml); **do not** implement a live cloud service yet.

**Notes:** Prefer cloud (SSE/WebSocket, parallel seats) when implementation begins. Published sessions still land as git Markdown under `deliberations/`.

### D-2026-10-11-3 — First fact-library seed regions (shells only)

**Decision:** Open scaffold files under `data/civilizations/` for these seed ids — **structure and placeholders only**. No invented facts, no fake sources, no forged images.

| Id | Names (zh / en) |
|----|-----------------|
| `civ-mesopotamia` | 两河 / Mesopotamia |
| `civ-ancient-egypt` | 古埃及 / Ancient Egypt |
| `civ-indus-valley` | 印度河 / Indus Valley |
| `civ-china-bronze` | 中国青铜时代（总览壳） / China Bronze Age (overview shell) |
| `civ-sanxingdui` | 三星堆 / Sanxingdui |
| `civ-olmec` | 奥尔梅克 / Olmec |
| `civ-early-maya` | 早期玛雅 / Early Maya |
| `civ-andes` | 安第斯早期文明（总览壳） / Andean early civilizations (overview shell) |
| `civ-aegean` | 爱琴 / Aegean |

**Notes:** `time_span` values on shells are approximate scholarly conventional ranges labeled for citation before any “publish as fact-library” step. `sources: []` until real `src-*` registry entries exist. Status remains `draft` until citations land.

### D-2026-10-11-4 — Markdown remains source of truth (for now)

**Decision:** Git-backed Markdown templates and entries are the **only** public library interface until a citation-fail-closed export/API is implemented. No silent dual store.

### D-2026-10-11-5 — Fill order starts with Mesopotamia + Egypt

**Decision:** Fact-library filling begins with the earliest Near Eastern / Nile shells: `civ-mesopotamia` (Sumer/Uruk-centered overview) and `civ-ancient-egypt` (Predynastic → Early Dynastic overview), before other seed regions.

**Notes:** Integrity gate remains: every factual claim needs a registered `src-*`. Andes receives only an optional Caral chronologic pointer when solidly cited; no full Andes expansion in this pass. Status may move from `draft` to `library-seed` only with ≥2 solid sources and a fully cited summary.
