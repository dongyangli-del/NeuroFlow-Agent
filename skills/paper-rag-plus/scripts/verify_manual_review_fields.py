#!/usr/bin/env python3
"""Field-level verification for source-traced Paper-RAG++ review entries.

This script consumes `manual-review-needed.md` entries that already passed
strict title matching in `source-verification-report.md`. It upgrades fields
only when there is direct source evidence from matched public metadata or from
the private Zotero BIB title/abstract/keywords. It intentionally writes short
evidence snippets, not full abstracts.
"""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
REFERENCES = ROOT / "skills" / "paper-rag-plus" / "references"
SCRIPTS = ROOT / "skills" / "paper-rag-plus" / "scripts"
PRIVATE_ZOTERO_BIB = ROOT / ".private" / "zotero" / "My Library.bib"
PRIVATE_CACHE = ROOT / ".private" / "paper-verification" / "field-cache.json"

DEFAULT_MANUAL_REVIEW = REFERENCES / "manual-review-needed.md"
DEFAULT_SOURCE_REPORT = REFERENCES / "source-verification-report.md"
DEFAULT_FIELD_REPORT = REFERENCES / "field-verification-report.md"

USER_AGENT = "NeuroFlow-Agent field verifier (https://github.com/dongyangli-del/NeuroFlow-Agent)"
UNVERIFIED_MARKERS = {
    "",
    "needs verification",
    "not identified in imported metadata",
    "待人工核验补充",
    "n/a",
    "none",
}


@dataclass
class ManualEntry:
    title: str
    body: list[str]


@dataclass
class SourceMatch:
    source: str = ""
    matched_title: str = ""
    year: str = ""
    venue: str = ""
    doi: str = ""
    url: str = ""
    authors: str = ""


@dataclass
class FieldEvidence:
    value: str
    source: str
    snippet: str = ""


@dataclass
class EntryVerification:
    entry: ManualEntry
    match: SourceMatch | None = None
    fields: dict[str, FieldEvidence] = field(default_factory=dict)
    unresolved: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def load_zotero_importer():
    spec = importlib.util.spec_from_file_location("neuroflow_zotero_import", SCRIPTS / "import_zotero_bib.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load import_zotero_bib.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def normalize_title(title: str) -> str:
    value = str(title or "").lower()
    value = value.replace("ﬁ", "fi").replace("ﬂ", "fl")
    value = re.sub(r"([a-z])-\s+([a-z])", r"\1\2", value)
    value = re.sub(r"[^a-z0-9\u4E00-\u9FFF]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def clean_value(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", str(value or ""))
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def is_verified_value(value: str) -> bool:
    return clean_value(value).lower() not in UNVERIFIED_MARKERS


def sentence_split(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    if not text:
        return []
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", text) if part.strip()]


def first_matching_sentence(text: str, patterns: list[str]) -> str:
    for sentence in sentence_split(text):
        haystack = sentence.lower()
        if any(re.search(pattern, haystack) for pattern in patterns):
            return sentence[:360]
    return ""


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
            current_title = line[4:].strip()
            current_body = []
        elif current_title is None:
            prefix.append(line)
        else:
            current_body.append(line)
    if current_title is not None:
        entries.append(ManualEntry(current_title, current_body))
    return prefix, entries


def parse_source_report(path: Path) -> dict[str, SourceMatch]:
    matches: dict[str, SourceMatch] = {}
    current_title: str | None = None
    current: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            if current_title:
                matches[normalize_title(current_title)] = source_match_from_fields(current)
            current_title = line[4:].strip()
            current = {}
            continue
        if line.startswith("- ") and ":" in line:
            key, value = line[2:].split(":", 1)
            current[key.strip().lower()] = value.strip()
    if current_title:
        matches[normalize_title(current_title)] = source_match_from_fields(current)
    return matches


def source_match_from_fields(fields: dict[str, str]) -> SourceMatch:
    return SourceMatch(
        source=fields.get("source", ""),
        matched_title=fields.get("matched title", ""),
        year="" if fields.get("year", "").lower() == "needs verification" else fields.get("year", ""),
        venue="" if fields.get("venue", "").lower() == "needs verification" else fields.get("venue", ""),
        doi="" if fields.get("doi", "").lower() == "needs verification" else fields.get("doi", ""),
        url="" if fields.get("url", "").lower() == "needs verification" else fields.get("url", ""),
        authors="" if fields.get("authors", "").lower() == "needs verification" else fields.get("authors", ""),
    )


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


def fetch_json(url: str, cache: dict[str, Any], timeout: float, delay: float) -> dict[str, Any]:
    if url in cache:
        cached = cache[url]
        return cached if isinstance(cached, dict) else {}
    request = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError):
        data = {}
    cache[url] = data
    if delay:
        time.sleep(delay)
    return data


def title_match_score(expected: str, candidate: str) -> float:
    left = set(normalize_title(expected).split())
    right = set(normalize_title(candidate).split())
    if not left or not right:
        return 0.0
    return len(left & right) / max(len(left), len(right))


def decode_openalex_abstract(index: Any) -> str:
    if not isinstance(index, dict):
        return ""
    positions: list[tuple[int, str]] = []
    for word, offsets in index.items():
        if not isinstance(offsets, list):
            continue
        for offset in offsets:
            if isinstance(offset, int):
                positions.append((offset, str(word)))
    return " ".join(word for _, word in sorted(positions))


def openalex_metadata(title: str, doi: str, cache: dict[str, Any], timeout: float, delay: float) -> dict[str, str]:
    if doi:
        url = "https://api.openalex.org/works/" + urllib.parse.quote("https://doi.org/" + doi, safe="")
    else:
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"search": title, "per-page": "1"})
    data = fetch_json(url, cache, timeout, delay)
    if "results" in data and isinstance(data.get("results"), list):
        data = data["results"][0] if data["results"] else {}
    if not isinstance(data, dict) or not data:
        return {}
    returned_title = clean_value(str(data.get("title") or ""))
    if not doi and title_match_score(title, returned_title) < 0.82:
        return {}
    venue = ""
    primary = data.get("primary_location")
    if isinstance(primary, dict):
        source = primary.get("source")
        if isinstance(source, dict):
            venue = clean_value(str(source.get("display_name") or ""))
    return {
        "title": returned_title,
        "year": clean_value(str(data.get("publication_year") or "")),
        "venue": venue,
        "doi": clean_value(str(data.get("doi") or "")).replace("https://doi.org/", ""),
        "abstract": decode_openalex_abstract(data.get("abstract_inverted_index")),
        "source": "OpenAlex",
    }


def semantic_scholar_metadata(title: str, cache: dict[str, Any], timeout: float, delay: float) -> dict[str, str]:
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(
        {"query": title, "limit": "1", "fields": "title,year,venue,abstract,externalIds,url"}
    )
    data = fetch_json(url, cache, timeout, delay)
    papers = data.get("data", []) if isinstance(data, dict) else []
    if not papers:
        return {}
    paper = papers[0]
    returned_title = clean_value(str(paper.get("title") or ""))
    if title_match_score(title, returned_title) < 0.82:
        return {}
    external_ids = paper.get("externalIds") or {}
    return {
        "title": returned_title,
        "year": clean_value(str(paper.get("year") or "")),
        "venue": clean_value(str(paper.get("venue") or "")),
        "doi": clean_value(str(external_ids.get("DOI") or "")),
        "abstract": clean_value(str(paper.get("abstract") or "")),
        "source": "Semantic Scholar",
    }


def unresolved_from_body(body: list[str]) -> list[str]:
    unresolved: list[str] = []
    for line in body:
        if line.startswith("Missing or unresolved:"):
            unresolved.extend(item.strip() for item in line.split(":", 1)[1].split(",") if item.strip() and item.strip() != "none")
        for field_name in ("signal modality", "task", "method", "dataset", "metric", "limitations"):
            if line.startswith(f"Auto verified {field_name}:"):
                unresolved.append(field_name)
    return sorted(dict.fromkeys(unresolved))


def line_value(body: list[str], label: str) -> str:
    prefix = f"{label}:"
    for line in body:
        if line.startswith(prefix):
            return clean_value(line.split(":", 1)[1])
    return ""


def build_paper_lookup(zotero) -> dict[str, Any]:
    if not PRIVATE_ZOTERO_BIB.exists():
        return {}
    papers = [paper for paper in zotero.parse_bib(PRIVATE_ZOTERO_BIB.read_text(encoding="utf-8")) if zotero.is_importable_reference(paper)]
    zotero.enrich(papers)
    lookup: dict[str, Any] = {}
    for paper in papers:
        lookup.setdefault(normalize_title(paper.title), paper)
    return lookup


def add_field(
    fields: dict[str, FieldEvidence],
    name: str,
    value: str,
    source: str,
    snippet: str = "",
    overwrite: bool = True,
) -> None:
    value = clean_value(value)
    if not is_verified_value(value):
        return
    if name in fields and not overwrite:
        return
    fields[name] = FieldEvidence(value=value, source=source, snippet=clean_value(snippet))


def evidence_for_label(zotero, paper: Any, patterns: list[str]) -> str:
    if paper is None:
        return ""
    return first_matching_sentence(zotero.evidence_text(paper), patterns)


def metric_evidence(text: str) -> FieldEvidence | None:
    patterns = {
        "accuracy": [r"\baccuracy\b", r"\btop[- ]?[15]\b"],
        "correlation": [r"\bcorrelation\b", r"\bpearson\b", r"\bspearman\b", r"\br\b\s*="],
        "precision/recall": [r"\bprecision@\d", r"\baverage precision\b", r"\bprecision[- ]recall\b", r"\brecall@\d", r"\bf1\b"],
        "AUC/AUROC": [r"\bauroc\b", r"\bauc\b"],
        "error": [r"\bmse\b", r"\brmse\b", r"\bmae\b", r"\bmean squared error\b"],
        "generation quality": [r"\bfid\b", r"\bclip score\b", r"\binception score\b", r"\bbleu\b", r"\brouge\b"],
    }
    found = []
    snippets = []
    for label, keys in patterns.items():
        sentence = first_matching_sentence(text, keys)
        if sentence:
            found.append(label)
            snippets.append(sentence)
    if not found:
        return None
    return FieldEvidence(", ".join(found), "public abstract/title evidence", snippets[0][:360])


def precise_limitation_sentence(text: str) -> str:
    patterns = [
        r"\bhowever\b",
        r"\blimitation(s)?\b",
        r"\bshortcoming(s)?\b",
        r"\bfail(s|ed|ing)?\b",
        r"\bcannot\b",
        r"\bconstrain(ed|t|ts)?\b",
        r"\black(s|ed|ing)?\b",
        r"\bchallenge(s|d)?\b",
        r"\bscarce|scarcity\b",
        r"\bsmall (sample|dataset|number|cohort)\b",
        r"\bdespite\b",
        r"\balthough\b",
    ]
    for sentence in sentence_split(text):
        lowered = sentence.lower()
        if "not only" in lowered:
            continue
        if any(re.search(pattern, lowered) for pattern in patterns):
            return sentence[:360]
    return "待人工核验补充"


def verify_entry(
    entry: ManualEntry,
    source_matches: dict[str, SourceMatch],
    paper_lookup: dict[str, Any],
    zotero,
    cache: dict[str, Any],
    timeout: float,
    delay: float,
    enrich_web: bool,
) -> EntryVerification:
    normalized = normalize_title(entry.title)
    match = source_matches.get(normalized)
    paper = paper_lookup.get(normalized)
    fields: dict[str, FieldEvidence] = {}
    notes: list[str] = []

    if match:
        add_field(fields, "year", match.year, f"{match.source} strict title match")
        add_field(fields, "venue", match.venue, f"{match.source} strict title match")
        add_field(fields, "doi", match.doi, f"{match.source} strict title match")

    web_meta: dict[str, str] = {}
    if enrich_web:
        title_for_lookup = match.matched_title if match and match.matched_title else entry.title
        doi_for_lookup = fields.get("doi").value if "doi" in fields else ""
        web_meta = openalex_metadata(title_for_lookup, doi_for_lookup, cache, timeout, delay)
        if not web_meta:
            web_meta = semantic_scholar_metadata(title_for_lookup, cache, timeout, delay)
        if web_meta:
            add_field(fields, "year", web_meta.get("year", ""), web_meta.get("source", "public metadata"), overwrite=False)
            add_field(fields, "venue", web_meta.get("venue", ""), web_meta.get("source", "public metadata"), overwrite=False)
            add_field(fields, "doi", web_meta.get("doi", ""), web_meta.get("source", "public metadata"), overwrite=False)

    evidence_text = ""
    if paper is not None:
        evidence_text = zotero.evidence_text(paper)
        if paper.modalities != [zotero.UNVERIFIED]:
            snippets = [
                evidence_for_label(zotero, paper, patterns)
                for label, patterns in zotero.MODALITY_PATTERNS
                if label in paper.modalities
            ]
            add_field(fields, "signal modality", ", ".join(paper.modalities), "Zotero BIB title/abstract/keywords", next((s for s in snippets if s), ""))
        if paper.tasks != [zotero.UNVERIFIED]:
            add_field(fields, "task", ", ".join(paper.tasks), "Zotero BIB title/abstract/keywords", zotero.task_detail(paper).replace("待人工核验补充", ""))
        if paper.methods != [zotero.UNVERIFIED]:
            snippets = [
                zotero.method_detail(paper, method)
                for method in paper.methods
                if zotero.method_detail(paper, method) != zotero.MANUAL_CHECK
            ]
            if snippets:
                add_field(fields, "method", ", ".join(paper.methods), "Zotero BIB title/abstract/keywords", snippets[0])
        if paper.datasets != [zotero.UNVERIFIED]:
            snippets = [
                zotero.dataset_detail(paper, dataset)
                for dataset in paper.datasets
                if zotero.dataset_detail(paper, dataset) != zotero.MANUAL_CHECK
            ]
            if snippets:
                add_field(fields, "dataset", ", ".join(paper.datasets), "Zotero BIB title/abstract/keywords", snippets[0])
        limitation = precise_limitation_sentence(zotero.evidence_text(paper))
        if limitation != zotero.MANUAL_CHECK:
            add_field(fields, "limitations", "source-traced limitation/caveat sentence", "Zotero BIB title/abstract/keywords", limitation)

    abstract = web_meta.get("abstract", "")
    combined_text = ". ".join(part for part in [evidence_text, abstract] if part)
    metric = metric_evidence(combined_text)
    if metric:
        fields["metric"] = metric

    unresolved = unresolved_from_body(entry.body)
    unresolved = [item for item in unresolved if item not in fields]
    if not match:
        notes.append("No source-verification match found in report.")
    if not paper:
        notes.append("No exact private Zotero BIB title match; content fields limited to public metadata.")

    return EntryVerification(entry=entry, match=match, fields=fields, unresolved=unresolved, notes=notes)


def summary_counts(verifications: list[EntryVerification]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for verification in verifications:
        for item in verification.unresolved:
            counts[item] = counts.get(item, 0) + 1
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def build_manual_prefix(verifications: list[EntryVerification]) -> list[str]:
    lines = [
        "# Manual Review Needed",
        "",
        "This report lists fields that could not be verified from cleaned Zotero BIB metadata, strict title-matched public metadata, or short source evidence snippets. Fill remaining fields only after inspecting the paper or a trusted public source.",
        "",
        "## Summary",
        "",
    ]
    counts = summary_counts(verifications)
    if counts:
        lines.extend(f"- {key}: {value}" for key, value in counts.items())
    else:
        lines.append("- No unresolved entries remain.")
    lines.extend(["", "## Priority Entries", ""])
    return lines


def rewrite_entry_body(verification: EntryVerification) -> list[str]:
    body = [
        line
        for line in verification.entry.body
        if not line.startswith("Auto field")
        and not line.startswith("Auto verified signal")
        and not line.startswith("Auto verified task")
        and not line.startswith("Auto verified method")
        and not line.startswith("Auto verified dataset")
        and not line.startswith("Auto verified metric")
        and not line.startswith("Auto verified limitations")
        and not line.startswith("Auto unresolved after field pass")
        and not line.startswith("Missing or unresolved:")
        and not line.startswith("Suggested next action:")
    ]
    replacements = {
        "Year": verification.fields.get("year"),
        "Venue": verification.fields.get("venue"),
        "DOI": verification.fields.get("doi"),
    }
    rewritten: list[str] = []
    replaced = set()
    for line in body:
        matched = False
        for label, evidence in replacements.items():
            if line.startswith(f"{label}:") and evidence:
                original = line_value([line], label)
                rewritten.append(f"{label}: {evidence.value}")
                if original and original != evidence.value and is_verified_value(original):
                    rewritten.append(f"Auto field note: replaced {label}={original} with source-traced {evidence.value}.")
                replaced.add(label)
                matched = True
                break
        if not matched:
            rewritten.append(line)
    for label, evidence in replacements.items():
        if evidence and label not in replaced:
            rewritten.append(f"{label}: {evidence.value}")

    if verification.unresolved:
        rewritten.append(f"Missing or unresolved: {', '.join(verification.unresolved)}")
        rewritten.append("Suggested next action: inspect paper text or trusted public source for the remaining unresolved fields.")
    else:
        rewritten.append("Missing or unresolved: none")

    rewritten.append("")
    rewritten.append("Auto field verification status: source-traced field pass")
    for name in ("signal modality", "task", "method", "dataset", "metric", "limitations"):
        evidence = verification.fields.get(name)
        if not evidence:
            continue
        line_name = name if name != "signal modality" else "signal modality"
        rewritten.append(f"Auto verified {line_name}: {evidence.value}")
        if evidence.snippet:
            rewritten.append(f"Auto field evidence ({name}): {evidence.snippet}")
        rewritten.append(f"Auto field source ({name}): {evidence.source}")
    if verification.unresolved:
        rewritten.append(f"Auto unresolved after field pass: {', '.join(verification.unresolved)}")
    for note in verification.notes:
        rewritten.append(f"Auto field note: {note}")
    return rewritten


def write_manual(path: Path, verifications: list[EntryVerification], drop_resolved: bool) -> None:
    retained = [item for item in verifications if item.unresolved or not drop_resolved]
    lines = build_manual_prefix(retained)
    for verification in retained:
        lines.append(f"### {verification.entry.title}")
        lines.append("")
        lines.extend(rewrite_entry_body(verification))
        lines.append("")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def build_report(verifications: list[EntryVerification], dropped: int) -> str:
    now = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    field_names = ["year", "venue", "doi", "signal modality", "task", "method", "dataset", "metric", "limitations"]
    lines = [
        "# Field Verification Report",
        "",
        f"Generated: {now}",
        "",
        "This report verifies fields for entries that already passed strict title matching. Content fields are upgraded only when a short title/abstract/keyword evidence snippet supports the field.",
        "",
        "## Summary",
        "",
        f"- Entries checked: {len(verifications)}",
        f"- Fully resolved entries dropped from manual review: {dropped}",
    ]
    for field_name in field_names:
        lines.append(f"- Auto-verified {field_name}: {sum(1 for item in verifications if field_name in item.fields)}")
    counts = summary_counts(verifications)
    if counts:
        lines.append("- Remaining unresolved fields: " + ", ".join(f"{key}={value}" for key, value in counts.items()))
    else:
        lines.append("- Remaining unresolved fields: none")
    lines.extend(["", "## Per-Entry Results", ""])
    for verification in verifications:
        lines.extend([f"### {verification.entry.title}", ""])
        for field_name in field_names:
            evidence = verification.fields.get(field_name)
            if not evidence:
                continue
            lines.append(f"- {field_name}: {evidence.value} [{evidence.source}]")
            if evidence.snippet:
                lines.append(f"  Evidence: {evidence.snippet}")
        lines.append(f"- Unresolved: {', '.join(verification.unresolved) if verification.unresolved else 'none'}")
        if verification.notes:
            lines.append(f"- Notes: {'; '.join(verification.notes)}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manual-review", type=Path, default=DEFAULT_MANUAL_REVIEW)
    parser.add_argument("--source-report", type=Path, default=DEFAULT_SOURCE_REPORT)
    parser.add_argument("--field-report", type=Path, default=DEFAULT_FIELD_REPORT)
    parser.add_argument("--cache", type=Path, default=PRIVATE_CACHE)
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument("--delay", type=float, default=0.05)
    parser.add_argument("--limit", type=int, default=0, help="0 means all entries")
    parser.add_argument("--no-enrich-web", action="store_true")
    parser.add_argument("--drop-resolved", action="store_true")
    args = parser.parse_args()

    zotero = load_zotero_importer()
    _, entries = parse_manual_review(args.manual_review)
    selected = entries[: args.limit] if args.limit else entries
    source_matches = parse_source_report(args.source_report)
    paper_lookup = build_paper_lookup(zotero)
    cache = load_cache(args.cache)
    verifications: list[EntryVerification] = []
    for index, entry in enumerate(selected, start=1):
        verifications.append(
            verify_entry(
                entry=entry,
                source_matches=source_matches,
                paper_lookup=paper_lookup,
                zotero=zotero,
                cache=cache,
                timeout=args.timeout,
                delay=args.delay,
                enrich_web=not args.no_enrich_web,
            )
        )
        if index == 1 or index % 25 == 0 or index == len(selected):
            save_cache(args.cache, cache)
            resolved = sum(1 for item in verifications if not item.unresolved)
            print(f"[{index}/{len(selected)}] fully_resolved={resolved}", flush=True)
    save_cache(args.cache, cache)

    dropped = sum(1 for item in verifications if not item.unresolved) if args.drop_resolved else 0
    write_manual(args.manual_review, verifications, drop_resolved=args.drop_resolved)
    args.field_report.write_text(build_report(verifications, dropped), encoding="utf-8")
    print(
        f"Checked {len(verifications)} entries; "
        f"fully resolved {sum(1 for item in verifications if not item.unresolved)}; "
        f"retained unresolved {sum(1 for item in verifications if item.unresolved)}"
    )


if __name__ == "__main__":
    main()
