"""Knowledge-base search and summary helpers for NeuroFlow."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

KB_FILES = (
    "docs/KNOWLEDGE_GRAPH.md",
    "docs/VERIFICATION_DASHBOARD.md",
    "skills/paper-rag-plus/references/papers-index-summary.md",
    "skills/paper-rag-plus/references/paper-taxonomy.md",
    "skills/paper-rag-plus/references/method-map.md",
    "skills/paper-rag-plus/references/dataset-map.md",
    "skills/paper-rag-plus/references/claim-to-citation.md",
    "skills/paper-rag-plus/references/manual-review-needed.md",
    "skills/ai-bci-research/references/knowledge-index.md",
    "skills/ai-bci-research/references/papers-index.md",
    "skills/ai-bci-research/references/bci-workflows.md",
    "skills/ai-bci-research/references/reviewer-objections.md",
    "skills/ai-bci-research/references/venue-workflows.md",
)


@dataclass(frozen=True)
class SearchHit:
    score: int
    path: Path
    line: int
    heading: str
    snippet: str


def _terms(query: str) -> list[str]:
    return [term for term in re.split(r"[^A-Za-z0-9_+\-/]+", query.lower()) if term]


def _heading_for_line(lines: list[str], index: int) -> str:
    for line in reversed(lines[: index + 1]):
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return ""


def _score_line(line: str, terms: list[str]) -> int:
    lower = line.lower()
    score = 0
    for term in terms:
        if term in lower:
            score += 4 if " " not in term else 6
    if all(term in lower for term in terms):
        score += 8
    if "scripts/neuroflow_runtime/cli.py kb search" in lower:
        score = max(0, score - 12)
    return score


def search_kb(root: Path, query: str, limit: int = 8) -> list[SearchHit]:
    terms = _terms(query)
    if not terms:
        return []
    hits: list[SearchHit] = []
    for rel in KB_FILES:
        path = root / rel
        if not path.exists():
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for index, line in enumerate(lines):
            score = _score_line(line, terms)
            if score <= 0:
                continue
            context_start = max(0, index - 1)
            context_end = min(len(lines), index + 2)
            snippet = " ".join(part.strip() for part in lines[context_start:context_end] if part.strip())
            hits.append(
                SearchHit(
                    score=score,
                    path=path.relative_to(root),
                    line=index + 1,
                    heading=_heading_for_line(lines, index),
                    snippet=snippet[:360],
                )
            )
    hits.sort(key=lambda hit: (-hit.score, str(hit.path), hit.line))
    return hits[:limit]


def kb_summary(root: Path) -> dict[str, str]:
    paper_taxonomy = root / "skills/paper-rag-plus/references/paper-taxonomy.md"
    source_report = root / "skills/paper-rag-plus/references/source-verification-report.md"
    manual_review = root / "skills/paper-rag-plus/references/manual-review-needed.md"
    summary = {
        "taxonomy": "missing",
        "source_traced": "missing",
        "manual_review": "missing",
        "entrypoint": "docs/KNOWLEDGE_GRAPH.md",
    }
    if paper_taxonomy.exists():
        text = paper_taxonomy.read_text(encoding="utf-8", errors="ignore")
        match = re.search(r"Parsed papers:\s*(\d+)", text)
        if match:
            summary["taxonomy"] = f"{match.group(1)} Zotero-aligned papers"
    if source_report.exists():
        text = source_report.read_text(encoding="utf-8", errors="ignore")
        match = re.search(r"Source-traced title matches:\s*(\d+)", text)
        if match:
            summary["source_traced"] = f"{match.group(1)} priority source-traced matches"
    if manual_review.exists():
        text = manual_review.read_text(encoding="utf-8", errors="ignore")
        match = re.search(r"entries:\s*(\d+)", text)
        if match:
            summary["manual_review"] = f"{match.group(1)} unresolved manual-review entries"
    return summary
