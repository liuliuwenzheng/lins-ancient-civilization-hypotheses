#!/usr/bin/env python3
"""HEAD-check every hotlinked media image_url / thumb_url (D-2026-10-20-01).

Stdlib only. Network required. Exit 1 if any URL is not HTTP 200 with an image/* content type.

  python3 tools/check_media_images.py            # all packs
  python3 tools/check_media_images.py egypt      # one pack
"""
from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = "LACH-media-check/0.1 (https://github.com/liuliuwenzheng/lins-ancient-civilization-hypotheses)"


def head(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:  # noqa: BLE001
        return 0, str(e)


def main() -> int:
    packs = sys.argv[1:] or [p.name for p in sorted((ROOT / "data/structured").iterdir()) if p.is_dir()]
    bad = n = 0
    for pack in packs:
        for path in sorted((ROOT / "data/structured" / pack / "media").glob("*.json")):
            rec = json.loads(path.read_text(encoding="utf-8"))
            for key in ("image_url", "thumb_url"):
                url = rec.get(key)
                if not url:
                    continue
                n += 1
                status, ctype = head(url)
                ok = status == 200 and ctype.startswith("image/")
                bad += not ok
                print(f"{'OK ' if ok else 'BAD'} {status} {ctype or '-':<12} {rec['id']} {key}")
    print(f"checked={n} bad={bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
