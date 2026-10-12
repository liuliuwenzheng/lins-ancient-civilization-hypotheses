#!/usr/bin/env python3
"""Shared helpers for Wave-3 densify (D-2026-10-12-17)."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TODAY = "2026-10-12"
ED = {
    "derived_from": [
        "tools/wave3_shells/densify_wave3.py",
        "docs/coverage-map.md",
        "docs/decisions.md#d-2026-10-12-17",
    ],
    "derived_on": TODAY,
    "notes": (
        "Wave-3 densify to library-seed-rich (D-2026-10-12-17). "
        "No invented pages/coords/finds/media art. Honest thin > fake dense."
    ),
}

def dump(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def dms(d, m, s, hemi):
    val = abs(d) + m / 60.0 + s / 3600.0
    return round(-val if hemi.upper() in "SW" else val, 6)

def dm(d, m, hemi):
    val = abs(d) + m / 60.0
    return round(-val if hemi.upper() in "SW" else val, 6)

def u(lat, lon, list_id, component=""):
    note = f"UNESCO WHC list {list_id}"
    if component:
        note += f" component {component}"
    note += " published DMS→decimal; access 2026-10-12"
    return {"lat": lat, "lon": lon, "precision_note": note}

def pl(lat, lon, pid, title):
    return {
        "lat": float(lat),
        "lon": float(lon),
        "precision_note": f"Pleiades place {pid} ({title}) representative point; CSV dump 2026-10-12",
    }

def write_source_md(s):
    url = s.get("url")
    access = TODAY if url else None
    body = f"""---
id: {s['id']}
type: {s['type']}
citation: {json.dumps(s['citation'], ensure_ascii=False)}
url: {json.dumps(url)}
access_date: {json.dumps(access)}
reliability_tier: {s['tier']}
notes: {json.dumps(s.get('notes') or '', ensure_ascii=False)}
---

# Source: `{s['id']}`

| Field | Value |
|-------|--------|
| Type | {s['type']} |
| Tier | {s['tier']} |
| Citation | {s['citation']} |
| URL | {url or '—'} |
| Accessed | {access or '—'} |

## Notes

{s.get('notes') or ''}
"""
    (ROOT / "sources" / f"{s['id']}.md").write_text(body, encoding="utf-8")

def write_source_json(pack_dir, s):
    dump(pack_dir / "sources" / f"{s['id']}.json", {
        "id": s["id"], "entity": "source", "type": s["type"],
        "citation": s["citation"], "url": s.get("url"),
        "access_date": TODAY if s.get("url") else None,
        "reliability_tier": s["tier"], "notes": s.get("notes"), "editorial": ED,
    })

def write_site(pack_dir, civ_id, st):
    dump(pack_dir / "sites" / f"{st['id']}.json", {
        "id": st["id"], "entity": "site", "names": st["names"],
        "kind_note": st.get("kind_note"), "region": st.get("region"),
        "civilization_ids": [civ_id], "summary": st["summary"],
        "sources": st["sources"], "coordinates": st.get("coords"), "editorial": ED,
    })

def write_period(pack_dir, civ_id, per):
    dump(pack_dir / "periods" / f"{per['id']}.json", {
        "id": per["id"], "entity": "period", "names": per["names"],
        "civilization_ids": [civ_id], "time": per["time"],
        "summary": per["summary"], "sources": per["sources"], "editorial": ED,
    })

def write_claim(pack_dir, civ_id, cl):
    dump(pack_dir / "claims" / f"{cl['id']}.json", {
        "id": cl["id"], "entity": "claim", "kind": cl.get("kind", "fact"),
        "statement": cl["statement"], "civilization_ids": [civ_id],
        "site_ids": cl.get("site_ids") or [], "period_ids": cl.get("period_ids") or [],
        "object_ids": cl.get("object_ids") or [], "sources": cl["sources"],
        "disclaimer": cl.get("disclaimer"), "editorial": ED,
    })

def write_object(pack_dir, civ_id, obj):
    dump(pack_dir / "objects" / f"{obj['id']}.json", {
        "id": obj["id"], "entity": "object",
        "object_kind": obj.get("object_kind", "assemblage"),
        "names": obj["names"], "civilization_ids": [civ_id],
        "site_ids": obj.get("site_ids") or [], "period_ids": obj.get("period_ids") or [],
        "summary": obj["summary"], "sources": obj["sources"],
        "rights": {"status": "outbound-link-only", "license": None, "attribution": None,
                   "upstream_url": None,
                   "notes": "Metadata-only assemblage; no forged plates or museum numbers."},
        "media_ids": obj.get("media_ids") or [], "editorial": ED,
    })

def write_media(pack_dir, m):
    dump(pack_dir / "media" / f"{m['id']}.json", {
        "id": m["id"], "entity": "media", "title": m["title"],
        "media_type": m.get("media_type", "document-link"),
        "external_url": m["external_url"], "local_path": None,
        "object_ids": m.get("object_ids") or [], "sources": m["sources"],
        "rights": {"status": "outbound-link-only", "license": m.get("license"),
                   "attribution": m.get("attribution"), "upstream_url": m["external_url"],
                   "notes": m.get("rights_notes",
                                  "Outbound landing only. No forged artifact images; local_path null.")},
        "editorial": ED,
    })

def patch_coords(pack_dir, site_id, coords):
    path = pack_dir / "sites" / f"{site_id}.json"
    if not path.exists():
        return
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("coordinates"):
        return
    data["coordinates"] = coords
    ed = data.get("editorial") or {}
    ed["notes"] = ((ed.get("notes") or "") + " | Coords filled D-2026-10-12-17.").strip(" |")
    ed["derived_on"] = TODAY
    data["editorial"] = ed
    dump(path, data)

def apply_pack(pack_name: str, payload: dict) -> dict:
    """Apply densify payload; return before/after counts."""
    civ_id = payload["civ_id"]
    pack_dir = ROOT / "data" / "structured" / pack_name
    before = {sub: len(list((pack_dir / sub).glob("*.json"))) for sub in
              ("sources", "sites", "periods", "objects", "claims", "media")}

    for s in payload.get("sources") or []:
        write_source_md(s)
        write_source_json(pack_dir, s)
    for sid, coords in (payload.get("fill_coords") or {}).items():
        patch_coords(pack_dir, sid, coords)
    for st in payload.get("sites") or []:
        write_site(pack_dir, civ_id, st)
    for per in payload.get("periods") or []:
        write_period(pack_dir, civ_id, per)
    for obj in payload.get("objects") or []:
        write_object(pack_dir, civ_id, obj)
    for cl in payload.get("claims") or []:
        write_claim(pack_dir, civ_id, cl)
    for m in payload.get("media") or []:
        write_media(pack_dir, m)

    # refresh civilization.json
    civ_path = pack_dir / "civilization.json"
    civ = json.loads(civ_path.read_text(encoding="utf-8"))
    src_ids = sorted(p.stem for p in (pack_dir / "sources").glob("*.json"))
    site_ids = sorted(p.stem for p in (pack_dir / "sites").glob("*.json"))
    period_ids = sorted(p.stem for p in (pack_dir / "periods").glob("*.json"))
    claim_ids = sorted(p.stem for p in (pack_dir / "claims").glob("*.json"))
    object_ids = sorted(p.stem for p in (pack_dir / "objects").glob("*.json"))
    civ["status"] = payload.get("status", "library-seed-rich")
    if payload.get("summary"):
        civ["summary"] = payload["summary"]
    civ["sources"] = src_ids
    civ["site_ids"] = site_ids
    civ["period_ids"] = period_ids
    civ["claim_ids"] = claim_ids
    civ["object_ids"] = object_ids
    civ["editorial"] = ED
    dump(civ_path, civ)

    after = {sub: len(list((pack_dir / sub).glob("*.json"))) for sub in
             ("sources", "sites", "periods", "objects", "claims", "media")}
    return {"before": before, "after": after, "civ_id": civ_id, "status": civ["status"]}
