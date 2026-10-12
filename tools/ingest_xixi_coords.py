#!/usr/bin/env python3
"""Ingest 嘻嘻 P-grade coordinate reply (D-2026-10-12-20).

Integrity rules:
- NEVER ingest 鱼凫/Yufu (false hit = Yufu-shi, Japan). Leave empty / clear if wrongly filled.
- Prefer P(UNESCO) upgrades; S(wiki/wikidata) only for carefully matched existing site ids.
- Skip ambiguous/frame/orientation sites and empty lat/lon rows.
- Record grade + source URL in precision_note; append editorial note.
- Do not invent archaeology beyond coordinates.
"""
from __future__ import annotations

import csv
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "docs/handoffs/2026-10-12-xixi-coords-P-grade.csv"
TODAY = "2026-10-12"
DECISION = "D-2026-10-12-20"

PACK_FROM_CELL = {
    "sanxingdui": "sanxingdui",
    "china-bronze": "china-bronze",
    "andes": "andes",
    "indus": "indus",
    "olmec": "olmec",
    "early-maya": "early-maya",
    "egypt": "egypt",
    "mesopotamia": "mesopotamia",
    "aegean": "aegean",
}


def norm(s: str) -> str:
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s


# Explicit pack + english-name → site id. SKIP_* = leave alone.
MATCH = {
    ("sanxingdui", "sanxingdui"): "site-sanxingdui",
    ("sanxingdui", "jinsha site"): "site-jinsha-comparative",
    ("sanxingdui", "baodun culture"): "site-baodun",
    ("sanxingdui", "yufu"): "SKIP_YUFU",
    ("sanxingdui", "qingguanshan"): "SKIP_EMPTY",
    ("china-bronze", "erlitou culture"): "site-erlitou",
    ("china-bronze", "yinxu"): "site-anyang-yinxu",
    ("china-bronze", "panlongcheng"): "site-panlongcheng",
    ("china-bronze", "taosi"): "site-taosi",
    ("china-bronze", "zhengzhou shang city"): "site-zhengzhou-erligang",
    ("china-bronze", "tianma qucun"): "site-tianma-qucun",
    ("china-bronze", "liulihe"): "site-liulihe",
    ("china-bronze", "wucheng"): "SKIP_EMPTY",
    ("china-bronze", "tonglushan"): "SKIP_EMPTY",
    ("china-bronze", "houma"): "SKIP_EMPTY",
    ("andes", "caral"): "site-caral",
    ("andes", "aspero"): "site-aspero",
    ("andes", "bandurria"): "SKIP_EMPTY",
    ("andes", "vichama"): "SKIP_NO_SITE",
    ("andes", "chavin de huantar"): "site-chavin-de-huantar",
    ("andes", "huaca prieta"): "site-huaca-prieta",
    ("andes", "el paraiso"): "site-el-paraiso",
    ("andes", "cerro sechin"): "site-cerro-sechin",
    ("andes", "kotosh"): "site-kotosh",
    ("andes", "la galgada"): "site-la-galgada",
    ("andes", "caballo muerto"): "site-caballo-muerto",
    ("indus", "harappa"): "site-harappa",
    ("indus", "mohenjo daro"): "site-mohenjo-daro",
    ("indus", "lothal"): "site-lothal",
    ("indus", "kalibangan"): "site-kalibangan",
    ("indus", "dholavira"): "site-dholavira",
    ("indus", "rakhigarhi"): "site-rakhigarhi",
    ("indus", "mehrgarh"): "site-mehrgarh",
    ("indus", "kot diji"): "site-kot-diji",
    ("indus", "chanhudaro"): "SKIP_NO_SITE",
    ("indus", "amri"): "site-amri",
    ("indus", "banawali"): "site-banawali",
    ("indus", "ganweriwala"): "SKIP_EMPTY",
    ("olmec", "san lorenzo tenochtitlan"): "site-san-lorenzo",
    ("olmec", "la venta"): "site-la-venta",
    ("olmec", "tres zapotes"): "site-tres-zapotes",
    ("olmec", "laguna de los cerros"): "site-laguna-de-los-cerros",
    ("olmec", "el manati"): "site-el-manati",
    ("olmec", "chalcatzingo"): "site-chalcatzingo",
    ("olmec", "cascajal block"): "SKIP_AMBIGUOUS",
    ("early-maya", "el mirador"): "site-el-mirador",
    ("early-maya", "nakbe"): "site-nakbe",
    ("early-maya", "cival"): "site-cival",
    ("early-maya", "san bartolo"): "SKIP_EMPTY",  # CSV empty; keep existing San Bartolo fill
    ("early-maya", "aguada fenix"): "site-aguada-fenix",
    ("early-maya", "cuello"): "site-cuello",
    ("early-maya", "cahal pech"): "site-cahal-pech",
    ("early-maya", "cerros"): "site-cerros",
    ("early-maya", "kaminaljuyu"): "SKIP_FRAME",  # site-kaminaljuyu marked frame/orientation
    ("early-maya", "holmul"): "site-holmul",
    ("early-maya", "mundo perdido"): "SKIP_AMBIGUOUS",  # Tikal subunit / deepen
    ("egypt", "buto"): "site-buto",
    ("egypt", "badari culture"): "site-badari",
    ("egypt", "dahshur"): "site-dahshur",  # keep S; do NOT P-upgrade (series WH pit)
    ("egypt", "tarkhan egypt"): "SKIP_EMPTY",
    ("egypt", "tell el farkha"): "site-tell-el-farkha",
    ("egypt", "bubastis"): "site-bubastis",
    ("mesopotamia", "khafajah"): "site-khafajah",
    ("mesopotamia", "ishchali"): "SKIP_EMPTY",
    ("mesopotamia", "shuruppak"): "site-shuruppak-fara",
    ("mesopotamia", "assur"): "site-assur",
    ("mesopotamia", "ur"): "site-ur",
    ("aegean", "palaikastro"): "site-palaikastro",
    ("aegean", "ayia irini"): "SKIP_EMPTY",
    ("aegean", "lefkandi"): "site-lefkandi-toumba",  # prefer concrete locus over frame
    ("aegean", "tiryns"): "site-tiryns",
    ("aegean", "troy"): "site-troy-hissarlik",
}


def parse_pack_cell(cell: str) -> str | None:
    # e.g. "三星堆 sanxingdui" or "两河 mesopotamia"
    m = re.search(r"([a-z][a-z0-9-]+)\s*$", cell.strip(), re.I)
    if not m:
        return None
    key = m.group(1).lower()
    return PACK_FROM_CELL.get(key)


def grade_from_level(level: str) -> tuple[str, bool]:
    """Return (grade_letter, is_p)."""
    if level.startswith("P("):
        return "P", True
    if level.startswith("S("):
        return "S", False
    return "S", False


def precision_note(grade: str, level: str, url: str, lat: float, lon: float) -> str:
    # Keep grade + source URL explicit for editorial audit.
    base = f"嘻嘻 reply {TODAY} grade={grade}; {level.strip()}"
    if url:
        base += f"; source={url}"
    base += f"; WGS84 {lat},{lon}"
    if grade == "P":
        base += " (UNESCO WHC official XML poi by id_number)"
    return base


def load_site(pack: str, site_id: str) -> tuple[Path, dict] | None:
    path = ROOT / "data/structured" / pack / "sites" / f"{site_id}.json"
    if not path.exists():
        return None
    return path, json.loads(path.read_text(encoding="utf-8"))


def save_site(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ensure_yufu_empty() -> str:
    path = ROOT / "data/structured/sanxingdui/sites/site-yufu.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    prev = data.get("coordinates")
    if prev is not None:
        data["coordinates"] = None
        ed = data.setdefault("editorial", {})
        notes = ed.get("notes") or ""
        ed["notes"] = (
            notes
            + f" | {DECISION}: cleared false-hit Yufu coords (en:Yufu = Yufu-shi Japan); leave empty pending P-grade Sichuan source."
        ).strip(" |")
        ed["derived_on"] = TODAY
        save_site(path, data)
        return f"CLEARED previous coords {prev}"
    # still stamp editorial note once
    ed = data.setdefault("editorial", {})
    tag = f"{DECISION}: Yufu coords deliberately left null (false hit Yufu-shi Japan)"
    if tag not in (ed.get("notes") or ""):
        ed["notes"] = ((ed.get("notes") or "") + " | " + tag).strip(" |")
        ed["derived_on"] = TODAY
        save_site(path, data)
    return "already null; stamped skip note"


def main() -> None:
    stats = {
        "filled_new": [],
        "p_upgraded": [],
        "s_refreshed": [],
        "skipped": [],
        "yufu": None,
        "errors": [],
    }

    stats["yufu"] = ensure_yufu_empty()

    with CSV_PATH.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        pack_cell = row.get("包") or ""
        en = (row.get("英文名") or "").strip()
        zh = (row.get("中文名") or "").strip()
        lat_s = (row.get("lat") or "").strip()
        lon_s = (row.get("lon") or "").strip()
        level = (row.get("级别") or "").strip()
        url = (row.get("URL") or "").strip()

        pack = parse_pack_cell(pack_cell)
        if not pack:
            stats["skipped"].append({"zh": zh, "en": en, "reason": f"unknown pack cell: {pack_cell}"})
            continue

        key = norm(en)
        action = MATCH.get((pack, key))
        if action is None:
            stats["skipped"].append({"pack": pack, "zh": zh, "en": en, "reason": "no explicit match"})
            continue
        if action.startswith("SKIP"):
            stats["skipped"].append({"pack": pack, "zh": zh, "en": en, "reason": action, "level": level})
            continue
        if not lat_s or not lon_s:
            stats["skipped"].append({"pack": pack, "zh": zh, "en": en, "reason": "empty lat/lon in CSV", "site": action})
            continue

        try:
            lat = float(lat_s)
            lon = float(lon_s)
        except ValueError:
            stats["errors"].append({"pack": pack, "en": en, "reason": f"bad lat/lon {lat_s},{lon_s}"})
            continue

        # Hard guard: reject Japan-range Yufu even if match miswired
        if "yufu" in key or "鱼凫" in zh:
            stats["skipped"].append({"pack": pack, "zh": zh, "en": en, "reason": "YUFU_HARD_BLOCK"})
            continue
        if 30 < lat < 35 and 130 < lon < 133:
            stats["skipped"].append(
                {"pack": pack, "zh": zh, "en": en, "reason": "geo fence Japan-like hit", "lat": lat, "lon": lon}
            )
            continue

        loaded = load_site(pack, action)
        if not loaded:
            stats["errors"].append({"pack": pack, "en": en, "reason": f"site file missing: {action}"})
            continue
        path, data = loaded

        # Skip frame/orientation ontology sites even if matched
        kn = (data.get("kind_note") or "").lower()
        sid = data["id"]
        if any(x in sid for x in ("-frame", "-orientation", "-pointer", "-deepen", "-cluster", "-survey")) or any(
            x in kn for x in ("survey-region", "overview pointer", "heritage documentation frame")
        ):
            # allow jinsha-comparative (has real UNESCO tentative coords already) and similar filled sites
            if "comparative" in sid and data.get("coordinates"):
                pass
            else:
                stats["skipped"].append({"pack": pack, "zh": zh, "en": en, "reason": "frame/orientation site", "site": sid})
                continue

        grade, is_p = grade_from_level(level)
        # Dahshur: force S even if someone marks P later
        if sid == "site-dahshur":
            grade, is_p = "S", False
            level = "S(Wikidata P625); series WHC 86 has no Dahshur poi — not P"

        note = precision_note(grade, level, url, lat, lon)
        prev = data.get("coordinates")
        prev_filled = bool(prev and prev.get("lat") is not None)

        if not prev_filled:
            data["coordinates"] = {"lat": lat, "lon": lon, "precision_note": note}
            ed = data.setdefault("editorial", {})
            ed["notes"] = (
                (ed.get("notes") or "")
                + f" | {DECISION}: filled coords from 嘻嘻 P-grade CSV ({grade})."
            ).strip(" |")
            ed["derived_on"] = TODAY
            df = ed.setdefault("derived_from", [])
            tag = "docs/handoffs/2026-10-12-xixi-coords-P-grade.csv"
            if tag not in df:
                df.append(tag)
            save_site(path, data)
            stats["filled_new"].append({"pack": pack, "site": sid, "grade": grade, "lat": lat, "lon": lon})
            continue

        # Already filled: only overwrite when upgrading to P, or refreshing P with official UNESCO values
        if is_p:
            data["coordinates"] = {"lat": lat, "lon": lon, "precision_note": note}
            ed = data.setdefault("editorial", {})
            ed["notes"] = (
                (ed.get("notes") or "")
                + f" | {DECISION}: P-upgrade / UNESCO official poi refresh from 嘻嘻."
            ).strip(" |")
            ed["derived_on"] = TODAY
            df = ed.setdefault("derived_from", [])
            tag = "docs/handoffs/2026-10-12-xixi-coords-P-grade.csv"
            if tag not in df:
                df.append(tag)
            save_site(path, data)
            stats["p_upgraded"].append(
                {
                    "pack": pack,
                    "site": sid,
                    "from": prev,
                    "to": {"lat": lat, "lon": lon},
                    "grade": "P",
                }
            )
            continue

        # S row on already-filled site: stamp provenance only if grade missing; do not overwrite existing coords
        ed = data.setdefault("editorial", {})
        tag = f"{DECISION}: S-row matched but existing coords kept (no overwrite); CSV={lat},{lon} grade=S url={url}"
        if "S-row matched but existing coords kept" not in (ed.get("notes") or ""):
            # Only stamp once per site when this pass sees an S match
            if f"{DECISION}: S-row matched" not in (ed.get("notes") or ""):
                ed["notes"] = ((ed.get("notes") or "") + " | " + tag).strip(" |")
                ed["derived_on"] = TODAY
                save_site(path, data)
                stats["s_refreshed"].append({"pack": pack, "site": sid, "action": "kept_existing_stamped"})
            else:
                stats["skipped"].append({"pack": pack, "site": sid, "reason": "already stamped S keep"})
        else:
            stats["skipped"].append({"pack": pack, "site": sid, "reason": "already stamped S keep"})

    out = ROOT / "docs/audits/pass-2026-10-12-xixi-coords.json"
    out.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in stats.items()}, ensure_ascii=False, indent=2))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
