#!/usr/bin/env python3
"""Write data/structured/<pack>/ from tools/pack_seeds/<pack>.json + sources/*.md."""
from __future__ import annotations
import json, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STRUCTURED = ROOT / "data" / "structured"
SOURCES = ROOT / "sources"
SEEDS = Path(__file__).resolve().parent / "pack_seeds"
TODAY = "2026-10-11"


def parse_front(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    block = text[3:end]
    data = {}
    for line in block.splitlines():
        if not line or line.startswith("#") or line.startswith(" ") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
            v = v[1:-1]
        data[k] = v
    return data


def load_source(sid: str) -> dict:
    path = SOURCES / f"{sid}.md"
    if not path.exists():
        raise FileNotFoundError(f"missing {path}")
    fm = parse_front(path)
    return {
        "id": sid,
        "entity": "source",
        "type": fm.get("type") or "monograph",
        "citation": fm.get("citation") or sid,
        "url": fm.get("url") or None,
        "access_date": fm.get("access_date") or TODAY,
        "reliability_tier": fm.get("reliability_tier") or "S",
        "notes": fm.get("notes") or None,
        "editorial": {
            "derived_from": [f"sources/{sid}.md"],
            "derived_on": TODAY,
            "notes": "Copied from source registry front matter; no new bibliographic claims.",
        },
    }


def dump(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_one(seed_path: Path) -> dict:
    seed = json.loads(seed_path.read_text(encoding="utf-8"))
    pack = seed["pack"]
    civ = seed["civilization"]
    civ_id = civ["id"]
    pack_dir = STRUCTURED / pack
    if pack_dir.exists():
        shutil.rmtree(pack_dir)
    pack_dir.mkdir(parents=True)

    for sid in civ["sources"]:
        dump(pack_dir / "sources" / f"{sid}.json", load_source(sid))

    for key, entity in (
        ("sites", "site"),
        ("periods", "period"),
        ("objects", "object"),
        ("claims", "claim"),
        ("media", "media"),
    ):
        items = seed.get(key) or []
        for item in items:
            item = dict(item)
            item.setdefault("entity", entity)
            item.setdefault(
                "editorial",
                {
                    "derived_from": [f"data/civilizations/{civ_id}.md", "sources/src-*"],
                    "derived_on": TODAY,
                    "notes": "Derived only from civ MD + registered sources. No new archaeological inventions.",
                },
            )
            dump(pack_dir / key / f"{item['id']}.json", item)

    sites = seed.get("sites") or []
    periods = seed.get("periods") or []
    objects = seed.get("objects") or []
    claims = seed.get("claims") or []
    media = seed.get("media") or []

    civ_out = {
        **civ,
        "entity": "civilization",
        "kind": "fact",
        "site_ids": [s["id"] for s in sites],
        "period_ids": [p["id"] for p in periods],
        "claim_ids": [c["id"] for c in claims],
        "object_ids": [o["id"] for o in objects],
        "markdown_path": f"data/civilizations/{civ_id}.md",
        "editorial": {
            "derived_from": [f"data/civilizations/{civ_id}.md", "sources/src-*"],
            "derived_on": TODAY,
            "notes": "Derived only from civ MD + registered sources. No new archaeological inventions.",
        },
    }
    dump(pack_dir / "civilization.json", civ_out)

    title_en = seed.get("title_en") or civ["names"]["en"]
    title_zh = seed.get("title_zh") or civ["names"]["zh"]
    (pack_dir / "README.md").write_text(
        f"# Structured archive pack — {title_en}\n\nEnglish | [中文](README.zh.md)\n\n"
        f"Machine-readable records derived **only** from `data/civilizations/{civ_id}.md` "
        f"and registered sources listed there. No new archaeological claims. No forged artifact images.\n\n"
        f"```bash\n.venv/bin/python tools/export_check.py\n```\n",
        encoding="utf-8",
    )
    (pack_dir / "README.zh.md").write_text(
        f"# 结构化档案包 — {title_zh}\n\n[English](README.md) | 中文\n\n"
        f"仅派生自 `data/civilizations/{civ_id}.md` 与已登记来源。无新考古发明。不伪造文物图。\n\n"
        f"```bash\n.venv/bin/python tools/export_check.py\n```\n",
        encoding="utf-8",
    )
    return {
        "pack": pack,
        "sources": len(civ["sources"]),
        "sites": len(sites),
        "periods": len(periods),
        "objects": len(objects),
        "claims": len(claims),
        "media": len(media),
    }


def main() -> int:
    seeds = sorted(SEEDS.glob("*.json"))
    if not seeds:
        print("no seeds in", SEEDS, file=sys.stderr)
        return 1
    for sp in seeds:
        summary = write_one(sp)
        print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
