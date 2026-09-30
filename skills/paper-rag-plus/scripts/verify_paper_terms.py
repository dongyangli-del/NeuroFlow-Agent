#!/usr/bin/env python3
"""Verify public paper terms with DBLP and web metadata sources.

This script follows the conservative matching policy used by OnlyCCFA:
prefer source metadata, require strict title similarity, and never fabricate
unmatched fields. It updates `manual-review-needed.md` with source-traced
paper facts when title matching succeeds, otherwise it marks the entry as a
web-search match failure for human review.
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import html
import http.client
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
REFERENCES = ROOT / "skills" / "paper-rag-plus" / "references"
PRIVATE_DIR = ROOT / ".private" / "paper-verification"
DEFAULT_MANUAL_REVIEW = REFERENCES / "manual-review-needed.md"
DEFAULT_REPORT = REFERENCES / "source-verification-report.md"
DEFAULT_CACHE = PRIVATE_DIR / "metadata-cache.json"

USER_AGENT = "NeuroFlow-Agent paper verifier (https://github.com/dongyangli-del/NeuroFlow-Agent)"
ONLYCCFA_NOTE = (
    "Matching policy adapted from the local OnlyCCFA workflow: DBLP first, "
    "then strict title metadata lookup through public web sources."
)


@dataclass
class ManualEntry:
    title: str
    body: list[str]


@dataclass
class Candidate:
    source: str
    title: str
    year: str = ""
    venue: str = ""
    doi: str = ""
    url: str = ""
    authors: list[str] = field(default_factory=list)
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class Verification:
    entry: ManualEntry
    status: str
    candidate: Candidate | None = None
    score: float = 0.0
    reason: str = ""


def normalize_title(title: str) -> str:
    source = (
        str(title or "")
        .lower()
        .replace("&", " and ")
        .replace("ﬁ", "fi")
        .replace("ﬂ", "fl")
        .replace("–", "-")
        .replace("—", "-")
        .replace("‑", "-")
    )
    return re.sub(r"([a-z])-\s+([a-z])", r"\1\2", source)


def clean_for_match(title: str) -> str:
    return re.sub(r"[^a-z0-9\u4E00-\u9FFF]+", " ", normalize_title(title)).strip()


def title_score(expected: str, candidate: str) -> float:
    expected_title = clean_for_match(expected)
    candidate_title = clean_for_match(candidate)
    if not expected_title or not candidate_title:
        return 0.0
    if expected_title == candidate_title:
        return 1.0
    expected_tokens = {token for token in expected_title.split() if token}
    candidate_tokens = {token for token in candidate_title.split() if token}
    if not expected_tokens or not candidate_tokens:
        return 0.0
    overlap = len(expected_tokens & candidate_tokens)
    return overlap / max(len(expected_tokens), len(candidate_tokens), 1)


def char_score(expected: str, candidate: str) -> float:
    expected_title = clean_for_match(expected)
    candidate_title = clean_for_match(candidate)
    if not expected_title or not candidate_title:
        return 0.0
    return difflib.SequenceMatcher(None, expected_title, candidate_title).ratio()


def is_low_information_title(title: str) -> bool:
    normalized = clean_for_match(title)
    tokens = normalized.split()
    if len(tokens) <= 3 and re.match(r"^(university|institute|department|school)\b", normalized):
        return True
    if "_" in title and len(tokens) <= 3:
        return True
    return False


def content_tokens(title: str) -> list[str]:
    stopwords = {
        "a",
        "an",
        "the",
        "to",
        "towards",
        "toward",
        "for",
        "with",
        "and",
        "or",
        "of",
        "in",
        "on",
        "based",
        "using",
    }
    return [token for token in clean_for_match(title).split() if token not in stopwords]


def is_successful_title_match(expected: str, candidate: str, min_score: float) -> bool:
    if is_low_information_title(expected):
        return False
    token_similarity = title_score(expected, candidate)
    character_similarity = char_score(expected, candidate)
    if clean_for_match(expected) == clean_for_match(candidate):
        return True
    expected_tokens = content_tokens(expected)
    candidate_tokens = content_tokens(candidate)
    first_core_matches = bool(
        expected_tokens and candidate_tokens and expected_tokens[0] == candidate_tokens[0]
    )
    return (
        token_similarity >= min_score
        and character_similarity >= 0.82
        and (first_core_matches or character_similarity >= 0.94)
    )


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", str(value or ""))
    return html.unescape(re.sub(r"\s+", " ", value)).strip()


def parse_manual_review(path: Path) -> tuple[list[str], list[ManualEntry]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    prefix: list[str] = []
    entries: list[ManualEntry] = []
    current_title: str | None = None
    current_body: list[str] = []

    for line in lines:
        if line.startswith("### "):
            if current_title is not None:
                entries.append(ManualEntry(current_title, current_body))
            elif not entries:
                prefix = prefix or current_body
            current_title = line[4:].strip()
            current_body = []
        else:
            if current_title is None:
                prefix.append(line)
            else:
                current_body.append(line)

    if current_title is not None:
        entries.append(ManualEntry(current_title, current_body))

    return prefix, entries


def unresolved_counts(entries: list[ManualEntry]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for entry in entries:
        for line in entry.body:
            if not line.startswith("Missing or unresolved:"):
                continue
            values = line.split(":", 1)[1]
            for value in values.split(","):
                key = value.strip()
                if key:
                    counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def build_manual_prefix(entries: list[ManualEntry]) -> list[str]:
    lines = [
        "# Manual Review Needed",
        "",
        "This report lists fields that could not be verified from cleaned Zotero BIB metadata or OpenAlex public metadata. Fill these only after inspecting the paper or a trusted public source.",
        "",
        "## Summary",
        "",
    ]
    counts = unresolved_counts(entries)
    if counts:
        lines.extend(f"- {key}: {value}" for key, value in counts.items())
    else:
        lines.append("- No unresolved entries remain.")
    lines.extend(["", "## Priority Entries", ""])
    return lines


def write_manual_review(path: Path, prefix: list[str], verifications: list[Verification]) -> None:
    del prefix
    output: list[str] = build_manual_prefix([verification.entry for verification in verifications])
    for verification in verifications:
        entry = verification.entry
        body = [
            line
            for line in entry.body
            if not line.startswith("Auto verification")
            and not line.startswith("Auto matched")
            and not line.startswith("Auto source")
            and not line.startswith("Auto verified")
            and not line.startswith("Auto search")
        ]
        output.append(f"### {entry.title}")
        output.extend(body)
        if output and output[-1] != "":
            output.append("")
        if verification.status == "not-checked":
            pass
        elif verification.candidate:
            candidate = verification.candidate
            fields = []
            if candidate.year:
                fields.append(f"year={candidate.year}")
            if candidate.venue:
                fields.append(f"venue={candidate.venue}")
            if candidate.doi:
                fields.append(f"doi={candidate.doi}")
            output.append(
                f"Auto verification status: source-traced via {candidate.source} strict title match"
            )
            output.append(f"Auto matched title: {candidate.title}")
            output.append(f"Auto source URL: {candidate.url or 'needs verification'}")
            output.append(f"Auto verified fields: {', '.join(fields) if fields else 'title identity only'}")
        else:
            output.append("Auto verification status: 联网搜索匹配失败，留待人工核验")
            output.append("Auto search sources: DBLP, Crossref, Semantic Scholar")
        output.append("")

    path.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")


def load_cache(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_cache(path: Path, cache: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def fetch_json(url: str, cache: dict[str, Any], delay: float, timeout: float) -> dict[str, Any]:
    if url in cache:
        return cache[url]
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (
        urllib.error.URLError,
        TimeoutError,
        json.JSONDecodeError,
        http.client.RemoteDisconnected,
        ConnectionError,
        OSError,
    ):
        data = {}
    cache[url] = data
    if delay:
        time.sleep(delay)
    return data


def dblp_candidates(title: str, cache: dict[str, Any], delay: float, timeout: float) -> list[Candidate]:
    url = "https://dblp.org/search/publ/api?" + urllib.parse.urlencode(
        {"q": title, "format": "json", "h": "5"}
    )
    data = fetch_json(url, cache, delay, timeout)
    hits = data.get("result", {}).get("hits", {}).get("hit", [])
    candidates: list[Candidate] = []
    for hit in hits:
        info = hit.get("info", {})
        authors = info.get("authors", {}).get("author", [])
        if isinstance(authors, dict):
            authors = [authors]
        author_names = [
            str(author.get("text", author)).strip() if isinstance(author, dict) else str(author).strip()
            for author in authors
        ]
        candidates.append(
            Candidate(
                source="DBLP",
                title=strip_tags(info.get("title", "")),
                year=str(info.get("year", "") or ""),
                venue=str(info.get("venue", "") or ""),
                doi=str(info.get("doi", "") or ""),
                url=str(info.get("ee", "") or info.get("url", "") or ""),
                authors=[name for name in author_names if name],
                raw=info,
            )
        )
    return candidates


def crossref_candidates(title: str, cache: dict[str, Any], delay: float, timeout: float) -> list[Candidate]:
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(
        {
            "query.title": title,
            "rows": "5",
            "select": "DOI,title,issued,container-title,short-container-title,author,URL,type",
        }
    )
    data = fetch_json(url, cache, delay, timeout)
    items = data.get("message", {}).get("items", [])
    candidates: list[Candidate] = []
    for item in items:
        item_title = (item.get("title") or [""])[0]
        issued = item.get("issued", {}).get("date-parts", [[]])
        year = str((issued[0] or [""])[0] or "")
        venue = ""
        for key in ("container-title", "short-container-title"):
            values = item.get(key) or []
            if values:
                venue = str(values[0] or "")
                break
        authors = []
        for author in item.get("author", []) or []:
            given = author.get("given", "")
            family = author.get("family", "")
            name = " ".join(part for part in [given, family] if part).strip()
            if name:
                authors.append(name)
        candidates.append(
            Candidate(
                source="Crossref",
                title=strip_tags(item_title),
                year=year,
                venue=venue,
                doi=str(item.get("DOI", "") or ""),
                url=str(item.get("URL", "") or ""),
                authors=authors,
                raw=item,
            )
        )
    return candidates


def semantic_scholar_candidates(
    title: str, cache: dict[str, Any], delay: float, timeout: float
) -> list[Candidate]:
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(
        {
            "query": title,
            "limit": "5",
            "fields": "title,year,venue,authors,externalIds,url",
        }
    )
    data = fetch_json(url, cache, delay, timeout)
    papers = data.get("data", []) if isinstance(data, dict) else []
    candidates: list[Candidate] = []
    for paper in papers:
        external_ids = paper.get("externalIds") or {}
        candidates.append(
            Candidate(
                source="Semantic Scholar",
                title=strip_tags(paper.get("title", "")),
                year=str(paper.get("year", "") or ""),
                venue=str(paper.get("venue", "") or ""),
                doi=str(external_ids.get("DOI", "") or ""),
                url=str(paper.get("url", "") or ""),
                authors=[author.get("name", "") for author in paper.get("authors", []) if author.get("name")],
                raw=paper,
            )
        )
    return candidates


def best_match(
    entry: ManualEntry,
    cache: dict[str, Any],
    min_score: float,
    delay: float,
    timeout: float,
) -> Verification:
    source_fns = (dblp_candidates, crossref_candidates, semantic_scholar_candidates)
    best: tuple[float, Candidate] | None = None
    for source_fn in source_fns:
        for candidate in source_fn(entry.title, cache, delay, timeout):
            score = title_score(entry.title, candidate.title)
            if best is None or score > best[0]:
                best = (score, candidate)
            if is_successful_title_match(entry.title, candidate.title, min_score):
                return Verification(entry=entry, status="source-traced", candidate=candidate, score=score)

    if best:
        return Verification(
            entry=entry,
            status="match-failed",
            score=best[0],
            reason=f"best candidate from {best[1].source}: {best[1].title}",
        )
    return Verification(entry=entry, status="match-failed", reason="no public metadata candidates")


def build_report(
    verifications: list[Verification],
    limit_note: str,
    dropped_failed_count: int = 0,
) -> str:
    now = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    matched = [item for item in verifications if item.candidate]
    failed = [item for item in verifications if not item.candidate]
    lines = [
        "# Source Verification Report",
        "",
        f"Generated: {now}",
        "",
        ONLYCCFA_NOTE,
        "",
        "## Summary",
        "",
        f"- Entries checked: {len(verifications)}{limit_note}",
        f"- Source-traced title matches: {len(matched)}",
        f"- Unmatched entries retained: {len(failed)}",
        f"- Dropped failed matches from public review lists: {dropped_failed_count}",
        "",
        "## Source-Traced Matches",
        "",
    ]
    for verification in matched:
        candidate = verification.candidate
        assert candidate is not None
        lines.extend(
            [
                f"### {verification.entry.title}",
                "",
                f"- Source: {candidate.source}",
                f"- Match score: {verification.score:.2f}",
                f"- Matched title: {candidate.title}",
                f"- Year: {candidate.year or 'needs verification'}",
                f"- Venue: {candidate.venue or 'needs verification'}",
                f"- DOI: {candidate.doi or 'needs verification'}",
                f"- URL: {candidate.url or 'needs verification'}",
                f"- Authors: {', '.join(candidate.authors[:6]) if candidate.authors else 'needs verification'}",
                "",
            ]
        )
    if failed:
        lines.extend(["## Failed Matches", ""])
        for verification in failed:
            lines.extend(
                [
                    f"### {verification.entry.title}",
                    "",
                    "- Status: 联网搜索匹配失败，留待人工核验",
                    f"- Search sources: DBLP, Crossref, Semantic Scholar",
                    f"- Best evidence: {verification.reason or 'none'}",
                    f"- Best score: {verification.score:.2f}",
                    "",
                ]
            )
    lines.extend(
        [
            "## Related P0/P1 Map Follow-Up",
            "",
            "- `claim-to-citation.md`, `method-map.md`, `dataset-map.md`, and `paper-taxonomy.md` still require field-level inspection for claims, method advantages, limitations, dataset use, metrics, and inappropriate-use judgments.",
            "- This report verifies paper identity and bibliographic facts only when strict title matching succeeds.",
            "- Do not upgrade method, dataset, metric, or claim-support fields unless the paper text or trusted metadata explicitly supports the term.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manual-review", type=Path, default=DEFAULT_MANUAL_REVIEW)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--limit", type=int, default=0, help="0 means check all entries")
    parser.add_argument("--min-score", type=float, default=0.86)
    parser.add_argument("--delay", type=float, default=0.15)
    parser.add_argument("--timeout", type=float, default=4.0)
    parser.add_argument("--no-update-manual-review", action="store_true")
    parser.add_argument(
        "--drop-failed",
        action="store_true",
        help="Remove failed public-metadata matches from the manual review file and report.",
    )
    args = parser.parse_args()

    prefix, entries = parse_manual_review(args.manual_review)
    selected_entries = entries[: args.limit] if args.limit else entries
    cache = load_cache(args.cache)
    verifications: list[Verification] = []
    interrupted = False
    try:
        for index, entry in enumerate(selected_entries, start=1):
            verification = best_match(entry, cache, args.min_score, args.delay, args.timeout)
            verifications.append(verification)
            if index == 1 or index % 10 == 0 or index == len(selected_entries):
                save_cache(args.cache, cache)
                matched = sum(1 for item in verifications if item.candidate)
                print(
                    f"[{index}/{len(selected_entries)}] matched={matched} failed={len(verifications) - matched}",
                    flush=True,
                )
    except KeyboardInterrupt:
        interrupted = True
        print("Interrupted; writing partial verification report.", flush=True)
    finally:
        save_cache(args.cache, cache)

    if not args.no_update_manual_review:
        remaining = entries[len(verifications) :]
        remaining_verifications = [
            Verification(entry=entry, status="not-checked", reason="not checked in this run")
            for entry in remaining
        ]
        output_verifications = verifications + remaining_verifications
        if args.drop_failed:
            output_verifications = [
                verification
                for verification in output_verifications
                if verification.status != "match-failed"
            ]
        write_manual_review(args.manual_review, prefix, output_verifications)

    limit_note = f" (limited to first {args.limit})" if args.limit else ""
    if interrupted:
        limit_note += " (interrupted partial run)"
    report_verifications = verifications
    dropped_failed_count = 0
    if args.drop_failed:
        dropped_failed_count = sum(1 for item in verifications if item.status == "match-failed")
        report_verifications = [
            verification for verification in verifications if verification.status != "match-failed"
        ]
    args.report.write_text(
        build_report(report_verifications, limit_note, dropped_failed_count),
        encoding="utf-8",
    )
    print(
        f"Checked {len(verifications)} entries; "
        f"matched {sum(1 for item in verifications if item.candidate)}; "
        f"failed {sum(1 for item in verifications if not item.candidate)}"
    )
    if interrupted:
        raise SystemExit(130)


if __name__ == "__main__":
    main()
