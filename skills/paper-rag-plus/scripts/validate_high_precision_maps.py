#!/usr/bin/env python3
"""Validate high-precision Paper-RAG++ generated maps."""

from __future__ import annotations

import sys
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REFERENCES = ROOT / "skills" / "paper-rag-plus" / "references"

REQUIRED = {
    "method-map.md": [
        "High-precision policy:",
        "Core algorithm / architecture / technical point:",
        "Core-method evidence class:",
        "Difference from contemporary related methods:",
    ],
    "dataset-map.md": [
        "High-precision policy:",
        "Official data specification:",
        "Dataset evidence class:",
        "Citation Sources",
    ],
    "claim-to-citation.md": [
        "High-precision policy:",
        "Single-paper original claim:",
        "Claim evidence class:",
        "Do not overuse for:",
    ],
    "paper-taxonomy.md": [
        "Collection Provenance Audit",
        "Papers with Zotero Collection assignments:",
        "Collection assignment source:",
    ],
}

FORBIDDEN_PHRASES = [
    "Generated method map for Paper-RAG++ retrieval. Entries are inferred from public metadata",
    "Representative references:",
    "Applicable scenarios: brain-to-image reconstruction",
    "Strengths to check:",
    "Known risks: split leakage",
    "Candidate support is generated from Zotero metadata",
]

FORBIDDEN_DATASET_HEADINGS = [
    "## ImageNet",
    "## COCO",
    "## LibriSpeech",
    "## LibriSpeech/Libri-light",
    "## HACS",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    limit = 2 * 1024 * 1024
    for name, required_markers in REQUIRED.items():
        path = REFERENCES / name
        if not path.exists():
            fail(f"missing generated map: {path.relative_to(ROOT)}")
        text = path.read_text(encoding="utf-8")
        if path.stat().st_size > limit:
            fail(f"{path.relative_to(ROOT)} exceeds 2MB")
        for marker in required_markers:
            if marker not in text:
                fail(f"{path.relative_to(ROOT)} missing marker: {marker}")
        for phrase in FORBIDDEN_PHRASES:
            if phrase in text:
                fail(f"{path.relative_to(ROOT)} contains old generic phrase: {phrase}")

    dataset_text = (REFERENCES / "dataset-map.md").read_text(encoding="utf-8")
    for heading in FORBIDDEN_DATASET_HEADINGS:
        if heading in dataset_text:
            fail(f"dataset-map.md contains forbidden non-neural dataset heading: {heading}")

    method_text = (REFERENCES / "method-map.md").read_text(encoding="utf-8")
    if re.search(r"Applicable task scenario: [^\n]*\bAbstract\b", method_text):
        fail("method-map.md has task scenarios that look like raw glued title/abstract text")

    claim_text = (REFERENCES / "claim-to-citation.md").read_text(encoding="utf-8")
    if "Careful writing form: This paper reports that 待人工核验补充" in claim_text:
        fail("claim-to-citation.md converts an unsupported claim into a writing sentence")

    print("High-precision map validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
