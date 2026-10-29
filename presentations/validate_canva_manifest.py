#!/usr/bin/env python3
"""Validate bilingual Canva presentation mappings without requiring API credentials.

Static validation only: public/anonymous Canva access is NOT checked here.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "presentations" / "canva-manifest.json"
DOI_PATTERN = re.compile(r"(?m)^- \*\*DOI\*\*:.*?https://doi\.org/(10\.[^\s\]\)]+)")
HEADINGS = re.compile(r"(?m)^### ([^\r\n]+)")
PRESENTATION = re.compile(
    r"(?m)^- \*\*(?:Presentación académica|Academic presentation)\*\*: "
    r"\[[^\]]+\]\((https://[^)]+)\)"
)


def fail(message: str) -> None:
    raise ValueError(message)


def catalogue(text: str, filename: str) -> dict[str, dict[str, str]]:
    sections = list(HEADINGS.finditer(text))
    out: dict[str, dict[str, str]] = {}
    for i, match in enumerate(sections):
        block = text[match.start():sections[i + 1].start() if i + 1 < len(sections) else len(text)]
        doi = DOI_PATTERN.search(block)
        presentation = PRESENTATION.search(block)
        if not presentation:
            continue
        if not doi:
            fail(f"{filename}: presentation has no DOI: {match.group(1)}")
        key = doi.group(1)
        if key in out:
            fail(f"{filename}: repeated presentation for DOI {key}")
        out[key] = {"title": match.group(1).strip(), "link": presentation.group(1), "block": block}
    return out


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records = manifest.get("records", [])
    if not records:
        fail("Manifest contains no records")
    expected = {r["doi"]: r for r in records}
    if len(expected) != len(records):
        fail("Repeated DOI in manifest")
    total = 0
    for lang, filename in (("es", "README.ES.md"), ("en", "README.md")):
        source = (ROOT / filename).read_text(encoding="utf-8")
        entries = catalogue(source, filename)
        if set(entries) != set(expected):
            missing = sorted(set(expected) - set(entries))
            extra = sorted(set(entries) - set(expected))
            fail(f"{filename}: DOI mismatch; missing={missing}; extra={extra}")
        for doi, record in expected.items():
            entry = entries[doi]
            design = record["presentations"][lang]
            if design["readme"] != filename:
                fail(f"{doi}: wrong README language mapping")
            if entry["link"] != design["link"]:
                fail(f"{doi} {lang}: README and manifest link differ")
            if not re.fullmatch(r"https://(?:www\.canva\.com/d/|canva\.link/)[A-Za-z0-9_-]+", entry["link"]):
                fail(f"{doi} {lang}: unexpected Canva link format")
            if design.get("slides", 0) < 1:
                fail(f"{doi} {lang}: no recorded slide count")
            if lang == "es" and record["title"] != entry["title"]:
                fail(f"{doi}: manifest title differs from README.ES.md")
            if record["status"] == "pending_publication":
                expected_status = "Estado de publicación" if lang == "es" else "Publication status"
                if expected_status not in entry["block"]:
                    fail(f"{doi} {lang}: unpublished paper lacks explicit status warning")
            total += 1
    for doi, record in expected.items():
        if record["status"] == "published":
            path = record.get("source_pdf")
            if not path or not (ROOT / path).is_file():
                fail(f"{doi}: published record is missing the PDF copy: {path!r}")
        if record["relation_to_marianos_work"] == "academic_reviewer":
            if "Mariano Enrique Torres Ponce" in (record.get("authors") or ""):
                fail(f"{doi}: reviewer incorrectly classified as author")
        if record["status"] == "pending_publication" and record.get("evidence_basis") != "readme_abstract_only":
            fail(f"{doi}: manuscript not yet available for full-text review")
    print(
        f"OK: {len(records)} papers, {total} bilingual Canva references, "
        "no DOI or URL discrepancies; PDF sources and authorship metadata checked."
    )
    print("NOTE: anonymous public access and view-only permissions were not tested.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, KeyError, FileNotFoundError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
