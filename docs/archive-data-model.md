# Archive data model (structured entities)

English | [中文](archive-data-model.zh.md)

> Product core = **digital archive + read API** (D-2026-10-11-17).  
> Markdown civilization pages remain the editorial / human-readable layer.  
> Structured JSON under `data/structured/` is the pilot **API-facing** form.  
> Citation **fail-closed**: `kind: fact` without resolvable `src-*` must not export.

Related: [Architecture](architecture.md) · [API §4.6](api.md) · [OpenAPI](openapi.v0.yaml) · [Schemas](../schemas/) · [Decisions](decisions.md)

---

## 1. Why entities (not only prose)

Encyclopedia-style bilingual MD is valuable presentation. An **archive API** needs addressable atoms:

| Entity | Id prefix | Role |
|--------|-----------|------|
| **Source** | `src-*` | Bibliographic registry (P/S/T/U) |
| **Site** | `site-*` | Archaeological site / survey zone / orientation name |
| **Period** | `period-*` | Period / phase with cited scheme (not a fake unique calendar) |
| **Object** | `obj-*` / `asm-*` | Assemblage or artifact-class **metadata** only — no forged binaries |
| **Claim** | `claim-*` | Atomic assertion: `kind: fact` \| `hypothesis` |
| **Media** | `media-*` | Rights metadata; external URL allowed; unverified uploads forbidden |
| **Civilization** | `civ-*` | Aggregate view linking sites / periods / claims / objects |
| **Deliberation** | `delib-*` | Optional stub pointing at `deliberations/*.md` |

JSON Schema drafts live in [`schemas/`](../schemas/).

---

## 2. Relations (simplified)

```
Source  <—— cited by ——  Claim / Site / Period / Object / Civilization / Media
Site    <—— located ——   Object, Claim
Period  <—— dated ——     Object, Claim
Object  <—— illustrated? —— Media (outbound / rights-cleared only)
Civilization —— aggregates —— Site[], Period[], Claim[], Object[], Source[]
Deliberation —— may target —— Civilization[] (does not mutate facts)
```

Direction of trust: **Sources first**. Claims never invent bibliography.

---

## 3. Epistemic split on Claim

| `kind` | Export rule |
|--------|-------------|
| `fact` | **Fail-closed:** `sources[]` non-empty; every id must exist as `sources/{id}.md` and (for pilot) `data/structured/.../sources/{id}.json`. |
| `hypothesis` | Must include non-empty `disclaimer`. Sources optional but recommended. Never auto-promote to `fact`. |

Scholarly models that the MD already labels as models (e.g. Uruk expansion; “first city” ranking) are stored as **hypothesis** claims in the pilot.

---

## 4. Media integrity

- Prefer `rights.status: outbound-link-only` + `external_url`.
- `local_path` **must be null** in v0 (no unverified uploads).
- **No forged artifact images.** Empty media set is honest and allowed.

---

## 5. Pilot layout — Mesopotamia

```
data/structured/mesopotamia/
  civilization.json
  deliberation.json          # stub → archive-api-direction delib
  sources/*.json             # 15 × src-mesopotamia-*
  sites/*.json
  periods/*.json
  objects/*.json             # assemblages / artifact-class metadata
  claims/*.json              # fact + hypothesis
  media/*.json               # CDLI outbound catalog pointer
  README.md | README.zh.md
```

Derivation rule: fields come only from `civ-mesopotamia.md` + registered `src-mesopotamia-*`. If a field is not in those texts, omit it or set `null` with an editorial note. Do not invent coordinates, P-numbers, hectare totals, or new archaeological claims.

---

## 6. Citation fail-closed gate (export)

`tools/export_check.py`:

1. Validate each JSON instance against the matching schema in `schemas/`.
2. For every Claim with `kind: fact`, require non-empty `sources[]` resolvable to registry + pilot source JSON.
3. Reject Media with non-null `local_path`.
4. Exit non-zero on any failure (CI-ready).

```bash
.venv/bin/python tools/export_check.py
```

Until a hosted API exists, git Markdown remains the published editorial source of truth (D-2026-10-11-4, refined by D-2026-10-11-17/18). Gated structured JSON is the serving form once export ships — **no silent dual-write**.

---

## 7. OpenAPI mapping

Read-only paths (design): `/sources`, `/sites`, `/periods`, `/objects`, `/claims`, `/media`, `/civilizations`, `/deliberations` — see [`openapi.v0.yaml`](openapi.v0.yaml) and [API §4.6](api.md).
