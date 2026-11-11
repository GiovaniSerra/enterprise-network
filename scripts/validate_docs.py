#!/usr/bin/env python3
"""Validate Portuguese/English Markdown pairs and local links.

This checks repository documentation only. It does not test devices or diagrams.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```[\s\S]*?```", re.MULTILINE)
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")


def markdown_paths() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*") if p.is_file()
                  and p.suffix.lower() == ".md" and ".git" not in p.parts)


def counterpart(path: Path) -> Path:
    if path.name.endswith(".en.md"):
        candidate = path.with_name(path.name[:-6] + ".md")
        if candidate.exists():
            return candidate
        return path.with_name(path.name[:-6] + ".MD")
    return path.with_name(path.stem + ".en.md")


def validate() -> list[str]:
    errors = []
    docs = markdown_paths()
    for doc in docs:
        rel = doc.relative_to(ROOT)
        pair = counterpart(doc)
        if not pair.exists():
            errors.append(f"{rel}: translation missing ({pair.relative_to(ROOT)})")
        text = doc.read_text(encoding="utf-8")
        # Remove code blocks and inline code to avoid false links in samples.
        text = INLINE_CODE_RE.sub("", FENCE_RE.sub("", text))
        for match in LINK_RE.finditer(text):
            raw = match.group(1).strip().split(' "', 1)[0].strip("<>")
            if not raw or raw.startswith("#") or raw.startswith("mailto:"):
                continue
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc:
                continue
            target = (doc.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT.resolve()):
                errors.append(f"{rel}: link escapes repository: {raw}")
            elif not target.exists():
                errors.append(f"{rel}: broken link: {raw}")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("DOCS INVALID:")
        for error in failures:
            print("  -", error)
        sys.exit(1)
    print(f"DOCS VALID: {len(markdown_paths())} bilingual Markdown files, local links OK.")
