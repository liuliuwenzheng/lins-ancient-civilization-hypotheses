"""Load all data/structured/<pack>/ JSON into in-memory indexes."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STRUCTURED = ROOT / "data" / "structured"

COLLECTION_DIRS = {
    "sources": "sources",
    "sites": "sites",
    "periods": "periods",
    "objects": "objects",
    "claims": "claims",
    "media": "media",
}


def _load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


class ArchiveStore:
    def __init__(self) -> None:
        self.packs: dict[str, dict[str, Any]] = {}
        self.civilizations: dict[str, dict[str, Any]] = {}
        self.by_entity: dict[str, dict[str, dict[str, Any]]] = {
            k: {} for k in COLLECTION_DIRS
        }
        self.source_index: dict[str, dict[str, Any]] = {}
        self.load_errors: list[str] = []
        self._load()

    def _load(self) -> None:
        if not STRUCTURED.is_dir():
            self.load_errors.append(f"missing {STRUCTURED}")
            return
        for pack_dir in sorted(STRUCTURED.iterdir()):
            if not pack_dir.is_dir():
                continue
            civ_path = pack_dir / "civilization.json"
            if not civ_path.exists():
                continue
            try:
                civ = _load_json(civ_path)
            except (OSError, json.JSONDecodeError) as e:
                self.load_errors.append(f"{civ_path}: {e}")
                continue
            cid = civ.get("id")
            if not cid:
                self.load_errors.append(f"{civ_path}: missing id")
                continue
            pack_name = pack_dir.name
            self.packs[pack_name] = {"path": str(pack_dir.relative_to(ROOT)), "civilization_id": cid}
            self.civilizations[cid] = {**civ, "_pack": pack_name}

            for key, subdir in COLLECTION_DIRS.items():
                d = pack_dir / subdir
                if not d.is_dir():
                    continue
                for path in sorted(d.glob("*.json")):
                    try:
                        data = _load_json(path)
                    except (OSError, json.JSONDecodeError) as e:
                        self.load_errors.append(f"{path}: {e}")
                        continue
                    eid = data.get("id")
                    if not eid:
                        self.load_errors.append(f"{path}: missing id")
                        continue
                    record = {**data, "_pack": pack_name}
                    # last write wins on id collision across packs (should be unique)
                    self.by_entity[key][eid] = record
                    if key == "sources":
                        self.source_index[eid] = record

    def expand_sources(self, source_ids: list[str] | None) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        for sid in source_ids or []:
            src = self.source_index.get(sid)
            if src:
                out.append(
                    {
                        "id": src.get("id"),
                        "reliability_tier": src.get("reliability_tier"),
                        "citation": src.get("citation"),
                        "url": src.get("url"),
                    }
                )
            else:
                out.append({"id": sid, "reliability_tier": None, "citation": None, "url": None})
        return out

    def enrich_site(self, site: dict[str, Any]) -> dict[str, Any]:
        """Return site with sources expanded when present."""
        out = {k: v for k, v in site.items() if not k.startswith("_")}
        ids = list(site.get("sources") or [])
        out["source_ids"] = ids
        out["sources"] = self.expand_sources(ids)
        return out

    def enrich_claim(self, claim: dict[str, Any]) -> dict[str, Any]:
        """Return claim with sources expanded to SourceRef objects (ids preserved)."""
        out = {k: v for k, v in claim.items() if not k.startswith("_")}
        ids = list(claim.get("sources") or [])
        out["source_ids"] = ids
        out["sources"] = self.expand_sources(ids)
        return out

    def enrich_media(self, media: dict[str, Any]) -> dict[str, Any]:
        """Return media with sources expanded; rights stay as registered."""
        out = {k: v for k, v in media.items() if not k.startswith("_")}
        ids = list(media.get("sources") or [])
        out["source_ids"] = ids
        out["sources"] = self.expand_sources(ids)
        lp = media.get("local_path") or ""
        prefix = "data/media-files/"
        # Served by the API at /media-files/… (static mount); UI prefers it, falls back to upstream.
        out["local_url"] = "/media-files/" + lp[len(prefix):] if lp.startswith(prefix) else None
        return out

    def public(self, record: dict[str, Any]) -> dict[str, Any]:
        return {k: v for k, v in record.items() if not k.startswith("_")}


_STORE: ArchiveStore | None = None


def get_store() -> ArchiveStore:
    global _STORE
    if _STORE is None:
        _STORE = ArchiveStore()
    return _STORE


def reload_store() -> ArchiveStore:
    global _STORE
    _STORE = ArchiveStore()
    return _STORE
