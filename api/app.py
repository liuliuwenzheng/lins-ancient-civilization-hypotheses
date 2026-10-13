"""FastAPI read-only archive application."""
from __future__ import annotations

from typing import Any, Optional

from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from api import __version__
from api.loader import get_store, ROOT as REPO_ROOT
from api.report import report_for_civilization

SERVICE_INFO = {
    "name": "Lin's Ancient Civilization Hypotheses — Archive API",
    "name_zh": "林的古文明猜想 — 档案接口",
    "version": __version__,
    "product": "archive + read-only API; prose and /ui are presentation",
    "principles": [
        "fact ≠ hypothesis — kind is required; hypotheses stay visually and structurally labeled",
        "citation fail-closed — fact claims need non-empty resolvable sources[]",
        "read-only — no write routes; changes via git/PR",
        "craft in seen and unseen — schemas, gates, and calm UI; no forged artifact images",
        "restraint — one accent, honest envelopes, no decorative lies",
    ],
    "browse_ui": "/ui",
    "docs": {
        "api_zh": "docs/api.zh.md",
        "api_en": "docs/api.md",
        "openapi": "docs/openapi.v0.yaml",
        "archive_model": "docs/archive-data-model.zh.md",
        "design_taste": "docs/design-taste.md",
        "design_taste_zh": "docs/design-taste.zh.md",
    },
    "pagination": {
        "style": "limit + offset (v0)",
        "defaults": {"limit": 50, "offset": 0},
        "max_limit": 200,
        "response_fields": ["items", "total", "count", "limit", "offset", "has_more"],
    },
}



def _period_sort_key(rec: dict[str, Any]) -> tuple:
    """Chronological order for periods: older (higher BCE) first; nulls last.

    Spans are cited author schemes (`time.label` / scheme_note), not a unique calendar.
    """
    t = rec.get("time") or {}
    from_bce = t.get("approx_from_bce")
    to_bce = t.get("approx_to_bce")
    return (
        from_bce is None,
        -(from_bce if from_bce is not None else 0),
        to_bce is None,
        -(to_bce if to_bce is not None else 0),
        rec.get("id") or "",
    )


def create_app() -> FastAPI:
    app = FastAPI(
        title=SERVICE_INFO["name"],
        version=__version__,
        description="Read-only archive API. Fact ≠ hypothesis. Citation fail-closed.",
        docs_url="/api/v1/docs",
        redoc_url="/api/v1/redoc",
        openapi_url="/api/v1/openapi.json",
    )

    static_dir = Path(__file__).resolve().parent / "static"
    ui_file = static_dir / "ui.html"

    @app.get("/ui")
    @app.get("/ui/")
    def browse_ui() -> FileResponse:
        if not ui_file.is_file():
            raise HTTPException(status_code=404, detail="ui not found")
        return FileResponse(ui_file, media_type="text/html; charset=utf-8")

    if static_dir.is_dir():
        app.mount("/ui/static", StaticFiles(directory=str(static_dir)), name="ui-static")

    @app.get("/")
    @app.get("/api/v1/")
    @app.get("/api/v1")
    def root() -> dict[str, Any]:
        store = get_store()
        return {
            **SERVICE_INFO,
            "message": (
                "Archive first. Human prose is a view; /ui is a calm browse surface. "
                "Every fact claim must cite sources; hypotheses stay labeled."
            ),
            "message_zh": (
                "档案优先。人类文案只是视图；/ui 是克制的浏览面。"
                "事实主张必有出处；假说始终标注。"
            ),
            "packs_loaded": sorted(store.packs.keys()),
            "civilization_count": len(store.civilizations),
            "load_errors": store.load_errors,
            "endpoints": [
                "GET /ui",
                "GET /api/v1/healthz",
                "GET /api/v1/civilizations",
                "GET /api/v1/civilizations/{id}",
                "GET /api/v1/civilizations/{id}/report",
                "GET /api/v1/sources",
                "GET /api/v1/sites",
                "GET /api/v1/periods",
                "GET /api/v1/objects",
                "GET /api/v1/claims",
                "GET /api/v1/media",
            ],
        }

    @app.get("/api/v1/healthz")
    def healthz() -> dict[str, Any]:
        store = get_store()
        ok = not store.load_errors and len(store.civilizations) > 0
        body = {
            "status": "ok" if ok else "degraded",
            "version": __version__,
            "packs": sorted(store.packs.keys()),
            "civilizations": len(store.civilizations),
            "counts": {k: len(v) for k, v in store.by_entity.items()},
            "load_errors": store.load_errors,
            "citation_gate": "export_check.py enforces fact→sources fail-closed before publish",
        }
        return JSONResponse(content=body, status_code=200 if ok else 503)

    def _paginate(items: list[dict[str, Any]], limit: int, offset: int) -> dict[str, Any]:
        limit = max(1, min(limit, 200))
        offset = max(0, offset)
        total = len(items)
        page = items[offset : offset + limit]
        return {
            "items": page,
            "total": total,
            "count": len(page),
            "limit": limit,
            "offset": offset,
            "has_more": offset + len(page) < total,
        }

    def _match_civ(rec: dict[str, Any], civilization: Optional[str]) -> bool:
        if not civilization:
            return True
        if rec.get("id") == civilization:
            return True
        cids = rec.get("civilization_ids") or []
        return civilization in cids

    def _match_region(rec: dict[str, Any], region: Optional[str]) -> bool:
        if not region:
            return True
        needle = region.lower()
        for field in ("region",):
            val = rec.get(field)
            if isinstance(val, str) and needle in val.lower():
                return True
        # civilization region filter for nested
        for cid in rec.get("civilization_ids") or []:
            civ = get_store().civilizations.get(cid)
            if civ and isinstance(civ.get("region"), str) and needle in civ["region"].lower():
                return True
        if isinstance(rec.get("region"), str) and needle in rec["region"].lower():
            return True
        return False

    @app.get("/api/v1/civilizations")
    def list_civilizations(
        region: Optional[str] = Query(None, description="Substring match on region"),
        limit: int = Query(50, ge=1, le=200),
        offset: int = Query(0, ge=0),
    ) -> dict[str, Any]:
        store = get_store()
        items = []
        for civ in sorted(store.civilizations.values(), key=lambda c: c.get("id") or ""):
            if region and not _match_region(civ, region):
                continue
            items.append(store.public(civ))
        return _paginate(items, limit, offset)

    @app.get("/api/v1/civilizations/{civ_id}")
    def get_civilization(civ_id: str) -> dict[str, Any]:
        store = get_store()
        civ = store.civilizations.get(civ_id)
        if not civ:
            raise HTTPException(status_code=404, detail=f"civilization not found: {civ_id}")
        out = store.public(civ)
        md = out.get("markdown_path")
        out["report_available"] = bool(md)
        return out

    @app.get("/api/v1/civilizations/{civ_id}/report")
    def get_civilization_report(civ_id: str) -> dict[str, Any]:
        """Parsed markdown report columns (entry-depth). Never invents missing sections."""
        store = get_store()
        civ = store.civilizations.get(civ_id)
        if not civ:
            raise HTTPException(status_code=404, detail=f"civilization not found: {civ_id}")
        return report_for_civilization(REPO_ROOT, civ)

    def _list_collection(
        collection: str,
        civilization: Optional[str],
        region: Optional[str],
        kind: Optional[str],
        limit: int,
        offset: int,
    ) -> dict[str, Any]:
        store = get_store()
        items: list[dict[str, Any]] = []
        records = list(store.by_entity[collection].values())
        if collection == "periods":
            records.sort(key=_period_sort_key)
        else:
            records.sort(key=lambda r: r.get("id") or "")
        for rec in records:
            if not _match_civ(rec, civilization):
                continue
            if not _match_region(rec, region):
                continue
            if kind and rec.get("kind") != kind:
                continue
            if collection == "claims":
                items.append(store.enrich_claim(rec))
            elif collection == "sites":
                items.append(store.enrich_site(rec))
            else:
                items.append(store.public(rec))
        return _paginate(items, limit, offset)

    @app.get("/api/v1/sources")
    def list_sources(
        civilization: Optional[str] = Query(None, description="Filter sources cited by this civ (via pack)"),
        limit: int = Query(50, ge=1, le=200),
        offset: int = Query(0, ge=0),
    ) -> dict[str, Any]:
        store = get_store()
        allowed: set[str] | None = None
        if civilization:
            civ = store.civilizations.get(civilization)
            if not civ:
                raise HTTPException(status_code=404, detail=f"civilization not found: {civilization}")
            allowed = set(civ.get("sources") or [])
        items = []
        for rec in sorted(store.by_entity["sources"].values(), key=lambda r: r.get("id") or ""):
            if allowed is not None and rec.get("id") not in allowed:
                continue
            items.append(store.public(rec))
        return _paginate(items, limit, offset)

    @app.get("/api/v1/sites")
    def list_sites(
        civilization: Optional[str] = None,
        region: Optional[str] = None,
        limit: int = Query(50, ge=1, le=200),
        offset: int = Query(0, ge=0),
    ) -> dict[str, Any]:
        return _list_collection("sites", civilization, region, None, limit, offset)

    @app.get("/api/v1/periods")
    def list_periods(
        civilization: Optional[str] = Query(
            None,
            description="Filter by civilization id. Results sorted chronologically "
            "(approx_from_bce desc; nulls last). Spans are cited schemes, not a unique calendar.",
        ),
        limit: int = Query(50, ge=1, le=200),
        offset: int = Query(0, ge=0),
    ) -> dict[str, Any]:
        return _list_collection("periods", civilization, None, None, limit, offset)

    @app.get("/api/v1/objects")
    def list_objects(
        civilization: Optional[str] = None,
        limit: int = Query(50, ge=1, le=200),
        offset: int = Query(0, ge=0),
    ) -> dict[str, Any]:
        return _list_collection("objects", civilization, None, None, limit, offset)

    @app.get("/api/v1/claims")
    def list_claims(
        civilization: Optional[str] = None,
        kind: Optional[str] = Query(None, description="fact | hypothesis"),
        limit: int = Query(50, ge=1, le=200),
        offset: int = Query(0, ge=0),
    ) -> dict[str, Any]:
        if kind is not None and kind not in ("fact", "hypothesis"):
            raise HTTPException(status_code=400, detail="kind must be fact or hypothesis")
        return _list_collection("claims", civilization, None, kind, limit, offset)

    @app.get("/api/v1/media")
    def list_media(
        civilization: Optional[str] = Query(
            None,
            description="Filter by civilization: same pack and/or linked object_ids",
        ),
        limit: int = Query(50, ge=1, le=200),
        offset: int = Query(0, ge=0),
    ) -> dict[str, Any]:
        # media may lack civilization_ids; filter via pack and linked objects
        store = get_store()
        pack_name: str | None = None
        object_ids: set[str] = set()
        if civilization:
            civ = store.civilizations.get(civilization)
            if not civ:
                raise HTTPException(status_code=404, detail=f"civilization not found: {civilization}")
            pack_name = civ.get("_pack")
            object_ids = set(civ.get("object_ids") or [])
        items = []
        for rec in sorted(store.by_entity["media"].values(), key=lambda r: r.get("id") or ""):
            if pack_name is not None:
                linked = set(rec.get("object_ids") or [])
                same_pack = rec.get("_pack") == pack_name
                if not same_pack and not linked.intersection(object_ids):
                    continue
            items.append(store.enrich_media(rec))
        return _paginate(items, limit, offset)

    return app


app = create_app()
