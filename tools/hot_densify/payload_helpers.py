
from __future__ import annotations

def L(zh, en, native=None):
    return {"zh": zh, "en": en, "native": native}

def src(id, typ, tier, citation, url=None, notes=""):
    return {"id": id, "type": typ, "tier": tier, "citation": citation, "url": url, "notes": notes}

def site(id, zh, en, kind, region, sources, summary_zh, summary_en, coords=None, native=None):
    return {"id": id, "names": L(zh, en, native), "kind_note": kind, "region": region,
            "sources": sources, "summary": L(summary_zh, summary_en), "coords": coords}

def period(id, zh, en, label, summary_zh, summary_en, sources, from_bce=None, to_bce=None, scheme=""):
    return {"id": id, "names": L(zh, en),
            "time": {"label": label, "approx_from_bce": from_bce, "approx_to_bce": to_bce,
                     "scheme_note": scheme or label},
            "summary": L(summary_zh, summary_en), "sources": sources}

def claim(id, zh, en, sources, site_ids=None, period_ids=None, object_ids=None, kind="fact", disclaimer=None):
    d = {"id": id, "kind": kind, "statement": L(zh, en), "sources": sources,
         "site_ids": site_ids or [], "period_ids": period_ids or [], "object_ids": object_ids or []}
    if disclaimer: d["disclaimer"] = disclaimer
    return d

def obj(id, zh, en, sources, site_ids=None, summary_zh="", summary_en="", period_ids=None):
    return {"id": id, "names": L(zh, en), "sources": sources, "site_ids": site_ids or [],
            "period_ids": period_ids or [], "summary": L(summary_zh or zh, summary_en or en)}

def media(id, zh, en, url, sources, attribution):
    return {"id": id, "title": L(zh, en), "external_url": url, "sources": sources, "attribution": attribution}
