# Tools

## `export_check.py`

Validate **all** packs under `data/structured/*/`, against `schemas/`, and enforce citation fail-closed for `Claim.kind=fact`.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/export_check.py
```
