"""Parse civilization markdown report columns for the read-only API / UI."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

# Known entry-depth headings → stable ids + bilingual titles.
# Matching is case-insensitive on the English (or bilingual) ## title text.
_KNOWN: list[tuple[str, str, str, tuple[str, ...]]] = [
    # id, title_en, title_zh, match aliases (lower)
    ("summary", "Summary", "摘要", ("summary",)),
    (
        "geography-environment",
        "Geography & environment",
        "地理与环境",
        ("geography & environment", "geography and environment"),
    ),
    (
        "chronology-periodization",
        "Chronology / periodization",
        "年代与分期",
        ("chronology / periodization", "chronology/periodization", "chronology"),
    ),
    ("key-sites", "Key sites", "关键遗址", ("key sites",)),
    (
        "urbanism-architecture-institutions",
        "Urbanism, architecture & institutions",
        "城市、建筑与制度",
        (
            "urbanism, architecture & institutions",
            "urbanism, architecture and institutions",
        ),
    ),
    (
        "writing-language-administration",
        "Writing, language & administration",
        "文字、语言与行政",
        (
            "writing, language & administration",
            "writing, language and administration",
        ),
    ),
    (
        "economy-subsistence-craft",
        "Economy, subsistence & craft",
        "经济、生计与手工业",
        (
            "economy, subsistence & craft",
            "economy, subsistence and craft",
        ),
    ),
    ("material-culture", "Material culture", "物质文化", ("material culture",)),
    ("external-contacts", "External contacts", "对外接触", ("external contacts",)),
    ("research-history", "Research history", "研究史", ("research history",)),
    ("sources", "Sources", "来源", ("sources", "registered sources")),
    (
        "related-civilizations",
        "Related civilizations",
        "相关文明",
        ("related civilizations",),
    ),
    ("notes", "Notes", "备注", ("notes",)),
]

_CJK_RE = re.compile(r"[\u4e00-\u9fff]")
_LATIN_RE = re.compile(r"[A-Za-z]")
_HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
_FRONT_MATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


def _slug(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"[^\w\s\-&/]+", "", s, flags=re.UNICODE)
    s = s.replace("&", " and ").replace("/", " ")
    s = re.sub(r"\s+", "-", s.strip())
    return s or "section"


def _match_known(title: str) -> tuple[str, str, str] | None:
    raw = title.strip()
    # Allow "中文 / English" or "English" style titles
    lower = raw.lower()
    # If bilingual "zh / en", try the English side after /
    if " / " in raw:
        parts = [p.strip() for p in raw.split(" / ")]
        candidates = [lower, parts[-1].lower(), parts[0].lower()]
    else:
        candidates = [lower]
    for cid, en, zh, aliases in _KNOWN:
        for cand in candidates:
            for alias in aliases:
                if cand == alias or cand.startswith(alias + " ") or alias in cand:
                    # Prefer exact / startswith over loose "in"
                    if cand == alias or cand.startswith(alias):
                        return cid, en, zh
    # Second pass: alias equality only on english-looking segment
    for cid, en, zh, aliases in _KNOWN:
        for cand in candidates:
            if cand in aliases:
                return cid, en, zh
    return None


def _strip_front_matter(text: str) -> str:
    if text.startswith("---"):
        m = _FRONT_MATTER_RE.match(text)
        if m:
            return text[m.end() :]
    return text


def _paragraphs(body: str) -> list[str]:
    parts = re.split(r"\n\s*\n", body.strip())
    return [p.strip() for p in parts if p.strip()]


def _script_score(text: str) -> tuple[int, int]:
    # Neutralize citation noise so zh paragraphs with `src-*` / Latin names still score as zh.
    cleaned = re.sub(r"`?src-[a-z0-9-]+`?", " ", text, flags=re.I)
    cleaned = re.sub(r"\[[^\]]*\]", " ", cleaned)
    return len(_CJK_RE.findall(cleaned)), len(_LATIN_RE.findall(cleaned))


def _split_bilingual(body: str) -> tuple[str | None, str | None]:
    """Best-effort: group CJK-heavy vs Latin-heavy paragraphs. Never invent text."""
    paras = _paragraphs(body)
    if not paras:
        return None, None
    zh_parts: list[str] = []
    en_parts: list[str] = []
    for p in paras:
        cjk, lat = _script_score(p)
        if cjk == 0 and lat == 0:
            continue
        if cjk > 0 and (lat == 0 or cjk >= max(6, lat // 3)):
            zh_parts.append(p)
        elif lat > 0 and cjk == 0:
            en_parts.append(p)
        elif cjk > 0:
            zh_parts.append(p)
        else:
            en_parts.append(p)
    # If everything landed in one bucket, don't pretend we split
    if zh_parts and en_parts:
        return "\n\n".join(zh_parts), "\n\n".join(en_parts)
    return None, None


def parse_markdown_report(path: Path) -> dict[str, Any]:
    """Parse ## sections from a civilization markdown file.

    Returns { available, markdown_path, sections: [...] }.
    Missing file → available False, sections [].
    """
    rel = str(path).replace("\\", "/")
    if not path.is_file():
        return {
            "available": False,
            "markdown_path": rel,
            "sections": [],
            "error": "markdown file not found",
        }
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        return {
            "available": False,
            "markdown_path": rel,
            "sections": [],
            "error": str(e),
        }

    body = _strip_front_matter(text)
    # Drop a leading # title line (single H1) — not a report column
    body = re.sub(r"^#\s+.+?\n+", "", body.lstrip(), count=1)

    matches = list(_HEADING_RE.finditer(body))
    sections: list[dict[str, Any]] = []
    if not matches:
        return {
            "available": False,
            "markdown_path": rel,
            "sections": [],
            "error": "no ## sections found",
        }

    for i, m in enumerate(matches):
        title_raw = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        section_body = body[start:end].strip()
        if not section_body:
            continue  # omit empty honestly
        known = _match_known(title_raw)
        if known:
            sid, title_en, title_zh = known
        else:
            sid = _slug(title_raw)
            title_en = title_raw
            title_zh = title_raw
        body_zh, body_en = _split_bilingual(section_body)
        sec: dict[str, Any] = {
            "id": sid,
            "title": title_raw,
            "title_en": title_en,
            "title_zh": title_zh,
            "body_md": section_body,
        }
        if body_zh:
            sec["body_zh"] = body_zh
        if body_en:
            sec["body_en"] = body_en
        sections.append(sec)

    return {
        "available": bool(sections),
        "markdown_path": rel,
        "sections": sections,
    }


def report_for_civilization(root: Path, civ: dict[str, Any]) -> dict[str, Any]:
    """Build report payload for one civilization record."""
    md_rel = civ.get("markdown_path")
    out: dict[str, Any] = {
        "civilization_id": civ.get("id"),
        "markdown_path": md_rel,
        "available": False,
        "sections": [],
    }
    if not md_rel or not isinstance(md_rel, str):
        out["error"] = "no markdown_path on civilization"
        return out
    path = root / md_rel
    parsed = parse_markdown_report(path)
    out["available"] = parsed["available"]
    out["markdown_path"] = md_rel
    out["sections"] = parsed["sections"]
    if parsed.get("error"):
        out["error"] = parsed["error"]
    return out
