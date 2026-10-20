# Tools

## `export_check.py`

Validate **all** packs under `data/structured/*/`, against `schemas/`, and enforce citation fail-closed for `Claim.kind=fact`.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/export_check.py
```

Also enforces the **embed gate** and **local file gate** (D-2026-10-20-01; local copies must sit at `data/media-files/<pack>/<id>.jpg`, <600 KB, listed in `ATTRIBUTION.md`): any media with `image_url`/`thumb_url` must be `rights-cleared` PD / CC0 / CC BY / CC BY-SA with `license_url`, attribution, source page, bilingual caption, a registered `src-*`, and a linked site/object in the pack.

## `check_media_images.py`

Network HEAD check (stdlib) that every hotlinked `image_url` / `thumb_url` returns 200 `image/*`.

```bash
python3 tools/check_media_images.py egypt mesopotamia
```
