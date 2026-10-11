# Public API (design v0)

English | [中文](api.zh.md)

> Leave a careful trail others can reuse. Read-only first. Citation fail-closed. Hypotheses always labeled.

OpenAPI stub: [`openapi.v0.yaml`](openapi.v0.yaml) · Architecture: [`architecture.md`](architecture.md)

**Status:** design only. No server is required to ship with this document. When implemented, behavior must match these principles.

---

## 1. Principles before endpoints

### 1.1 Citation fail-closed

**No registered source → do not expose the claim as fact.**

Adapted from poetry-tree’s rights gate, applied to **citations**:

1. **Build / export time:** a generator that builds SQLite/JSON from Markdown must reject civilization (fact) records whose `sources[]` are empty or point at missing `src-*` files.
2. **Serve time (when an API exists):** startup audit — if any served “fact” item fails the citation check, **refuse to start** (or exclude that item and surface an ops alert). The API must never become a backdoor around the Markdown rules.

Hypotheses and reconstructions may exist with thinner evidence, but they **must** stay labeled and carry disclaimers; they are never returned as `kind: "fact"`.

### 1.2 Orthogonal filter axes

Do **not** smash region + era + epistemic kind into one fake label (the “唐诗”-style trap).

| Axis | Answers | Example values |
|------|---------|----------------|
| `region` | **Where** | `West Asia`, `East Asia`, `Mesoamerica`, … (human-readable; exact vocabulary TBD with seeds) |
| `time_span` / time filters | **When** | query params such as `time_from`, `time_to` (BCE/CE normalized later) or substring match on `time_span` in v0 |
| `kind` | **Epistemic role** | `fact` \| `hypothesis` \| `reconstruction` \| `source` |
| `source_tier` | **Evidence strength of linked sources** | `P` \| `S` \| `T` \| `U` |
| `status` | **Lifecycle** | civ: `fact-library`; hyp: `open`\|`challenged`\|`retired`; rec: `draft`\|`review`\|`archived` |

Callers combine axes freely, e.g. “East Asia × fact”, “open hypotheses mentioning civ-…”, “sources tier=P”.

### 1.3 Every item carries a `sources` block

Downstream must not hunt the README to know where a claim came from. List/detail responses include source refs (ids + tier + short citation when available). Hypotheses additionally expose supporting vs conflicting lists.

### 1.4 Read-only API; writes via git/PR

v0 is **GET-only**. Creating or editing records happens through pull requests against Markdown templates. That keeps the citation gate in human review + CI, not in an unauthenticated POST.

### 1.5 Honest pagination and errors

- **Cursor pagination** (`limit` + `after` / `next_cursor`), not fragile deep `offset`.
- Distinguish **unknown filter value** (client error) from **valid filters, empty intersection** (200 + empty `items`).
- Hypotheses in any response always include `kind: "hypothesis"` and a `disclaimer` string.

### 1.6 Integrity of tone

This API exists so others can reuse the library and hypothesis board carefully — a trail for life and inquiry, not a dogma feed.

---

## 2. Base URL and versioning

Suggested base (host TBD — see decision points in the project conversation):

```
https://{host}/api/v1
```

All resources below are relative to `/api/v1`.

---

## 3. Common response shapes

### 3.1 List envelope

```json
{
  "items": [ /* Entity */ ],
  "total": 0,
  "count": 0,
  "next_cursor": null,
  "has_more": false
}
```

Pass `next_cursor` back as `after` unchanged.

### 3.2 Entity skeleton

Every item includes at least:

| Field | Notes |
|-------|--------|
| `id` | Registry id (`civ-…`, `src-…`, `hyp-…`, `rec-…`) |
| `kind` | `fact` \| `source` \| `hypothesis` \| `reconstruction` |
| `status` | Per-entity lifecycle |
| `sources` | Array of source ref objects (may be empty only for non-fact kinds under documented rules) |
| `links` | Related registry ids |

**Hypothesis extras (mandatory):**

```json
{
  "kind": "hypothesis",
  "disclaimer": "This record is a HYPOTHESIS, not an established historical or archaeological conclusion."
}
```

**Source ref object:**

```json
{
  "id": "src-2020-example",
  "reliability_tier": "S",
  "citation": "Author (Year). Title…",
  "url": "https://doi.org/…"
}
```

### 3.3 Error envelope

```json
{
  "error": {
    "code": "unknown_filter_value",
    "message": "Unknown region: Atlantis",
    "details": { "param": "region", "value": "Atlantis" }
  }
}
```

| Code | HTTP | When |
|------|------|------|
| `unknown_filter_value` | 400 | Filter value not in vocabulary |
| `invalid_cursor` | 400 | Bad `after` |
| `not_found` | 404 | Unknown id |
| `citation_gate_failed` | 503 | Serve-time audit failed (ops) |
| `internal_error` | 500 | Unexpected |

Empty result for a **valid** combo → **200** with `items: []`, not 404.

---

## 4. Endpoints (REST, read-only)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/` | Service info: principles, capabilities, endpoint index |
| GET | `/healthz` | Liveness; optional citation-audit summary |
| GET | `/meta/regions` | Region axis vocabulary |
| GET | `/meta/source-tiers` | P/S/T/U |
| GET | `/meta/stats` | Counts by kind / region / tier / status |
| GET | `/civilizations` | Fact-library list (filters + cursor) |
| GET | `/civilizations/{id}` | One civilization |
| GET | `/sources` | Source registry list |
| GET | `/sources/{id}` | One source |
| GET | `/hypotheses` | Hypothesis board list |
| GET | `/hypotheses/{id}` | One hypothesis (always labeled) |
| GET | `/reconstructions` | Reconstruction list |
| GET | `/reconstructions/{id}` | One reconstruction |
| GET | `/search` | Cross-kind search (`q` + optional `kind`, axes) |

### 4.1 Shared query parameters

| Param | Default | Notes |
|-------|---------|--------|
| `limit` | `20` | Max 100 (suggested) |
| `after` | — | Cursor from previous `next_cursor` |
| `region` | — | Orthogonal where-axis |
| `time_from` / `time_to` | — | Optional coarse bounds (v0 may be best-effort on `time_span` text) |
| `status` | — | Lifecycle filter |
| `source_tier` | — | Filter items that cite at least one source of this tier (semantics documented per endpoint) |
| `q` | — | Substring / later FTS over titles and summaries |

### 4.2 `/civilizations`

Additional filters: none beyond shared, plus maybe `related_to={civ-id}`.

Response items: `kind: "fact"`. **Must** include non-empty `sources` after citation gate; ungated drafts stay git-only.

### 4.3 `/hypotheses`

Always `kind: "hypothesis"` + `disclaimer`. Filters: `status`, `related_civilization={civ-id}`, `source_tier` on supporting sources.

### 4.4 `/reconstructions`

Items include `linked_facts`, `linked_hypotheses`, `uncertainty_summary`. Speculative narrative is never promoted to `kind: "fact"`.

### 4.5 `/search`

```
GET /search?q=...&kind=fact&region=...&limit=20
```

Each hit may include `snippet` and `score` when FTS exists; otherwise honest substring search with `engine: "like-fallback"` (same honesty lesson as poetry-tree: never fake a zero when the path degraded).

---

## 5. Auth

- **Public read** for all v0 GET endpoints.
- **Write:** out of scope for v0. Use git/PR + templates. Future write APIs (if any) would need auth, audit logs, and the same citation gate — not planned here.

---

## 6. GraphQL (optional, later)

A single GraphQL schema mirroring the same entities and orthogonal filters may be added later for flexible clients. One sentence for now: **not in v0**; REST is the contract to implement first.

---

## 7. License note for API consumers

- **This project’s code and documentation:** MIT ([`LICENSE`](../LICENSE)).
- **Cited third-party texts, images, and data:** remain under upstream rights. The API returns identifiers and bibliographic refs; it must not become a wholesale republication pipe for copyrighted corpora.
- Do not serve forged or mislabeled artifact binaries through this API.

---

## 8. Implementation sketch (non-normative)

When ready to build:

1. Parse YAML front matter from `sources/`, `data/civilizations/`, `hypotheses/`, `reconstructions/`.
2. Run citation gate → write `export/` SQLite or JSON.
3. Serve read-only from the export (DB opened read-only).
4. CI: fail if gate rejects; fail if hypothesis files lack the HYPOTHESIS label / `kind` mapping.

Until then, **git Markdown remains the only public interface** — and that is already enough for careful human reuse.
