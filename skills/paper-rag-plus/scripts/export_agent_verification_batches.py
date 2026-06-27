#!/usr/bin/env python3
"""Export manual-review entries into sub-agent verification batches."""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REFERENCES = ROOT / "skills" / "paper-rag-plus" / "references"
PRIVATE_DIR = ROOT / ".private" / "paper-verification-batches"
DEFAULT_MANUAL_REVIEW = REFERENCES / "manual-review-needed.md"


@dataclass
class ManualEntry:
    idx: int
    title: str
    body: list[str]
    known: dict[str, str] = field(default_factory=dict)
    source_url: str = ""
    missing: list[str] = field(default_factory=list)
    statuses: dict[str, str] = field(default_factory=dict)


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def parse_missing(body: list[str]) -> list[str]:
    section = ""
    for line in body:
        if line in {"Bibliographic:", "Paper type:", "Evidence fields:", "Verification:", "Field evidence:", "Identity trace:"}:
            section = line[:-1]
            continue
        if section == "Verification" and line.startswith("- final_unresolved_fields:"):
            return [
                clean(value)
                for value in line.split(":", 1)[1].split(",")
                if clean(value) and clean(value).lower() not in {"none", "n/a", "null", "unresolved"}
            ]
    for prefix in ("Auto unresolved after field pass:", "Missing or unresolved:"):
        for line in body:
            if line.startswith(prefix):
                return [
                    clean(value)
                    for value in line.split(":", 1)[1].split(",")
                    if clean(value) and clean(value).lower() != "none"
                ]
    return []


def parse_known(body: list[str]) -> dict[str, str]:
    known: dict[str, str] = {}
    section = ""
    for line in body:
        if line in {"Bibliographic:", "Paper type:", "Evidence fields:", "Verification:", "Field evidence:", "Identity trace:"}:
            section = line[:-1]
            continue
        if section == "Bibliographic" and line.startswith("- ") and ":" in line:
            key, value = line[2:].split(":", 1)
            key = clean(key).lower()
            if key in {"year", "venue", "doi"}:
                known[key] = clean(value)
    for key in ("Year", "Venue", "DOI"):
        for line in body:
            if line.startswith(f"{key}:"):
                known.setdefault(key.lower(), clean(line.split(":", 1)[1]))
                break
        else:
            known.setdefault(key.lower(), "")
    return known


def parse_source_url(body: list[str]) -> str:
    section = ""
    for line in body:
        if line in {"Bibliographic:", "Paper type:", "Evidence fields:", "Verification:", "Field evidence:", "Identity trace:"}:
            section = line[:-1]
            continue
        if section == "Identity trace" and line.startswith("- auto_source_url:"):
            return clean(line.split(":", 1)[1])
        if section == "Verification" and line.startswith("- evidence_sources:"):
            sources = clean(line.split(":", 1)[1])
            if sources and sources != "unresolved":
                return clean(sources.split(";", 1)[0])
        if line.startswith("Auto source URL:"):
            return clean(line.split(":", 1)[1])
    return ""


def parse_statuses(body: list[str]) -> dict[str, str]:
    statuses: dict[str, str] = {}
    section = ""
    for line in body:
        if line in {"Bibliographic:", "Paper type:", "Evidence fields:", "Verification:", "Field evidence:", "Identity trace:"}:
            section = line[:-1]
            continue
        if section == "Paper type" and line.startswith("- type:"):
            statuses["paper_type"] = clean(line.split(":", 1)[1])
        elif section == "Evidence fields" and line.startswith("- metric_status:"):
            statuses["metric_status"] = clean(line.split(":", 1)[1])
        elif section == "Evidence fields" and line.startswith("- dataset_role:"):
            statuses["dataset_role"] = clean(line.split(":", 1)[1])
        elif section == "Evidence fields" and line.startswith("- limitation_source:"):
            statuses["limitation_source"] = clean(line.split(":", 1)[1])
        elif section == "Verification" and line.startswith("- verification_status:"):
            statuses["verification_status"] = clean(line.split(":", 1)[1])
    return statuses


def parse_manual_review(path: Path) -> list[ManualEntry]:
    lines = path.read_text(encoding="utf-8").splitlines()
    entries: list[ManualEntry] = []
    current_title: str | None = None
    current_body: list[str] = []
    for line in lines:
        if line.startswith("### "):
            if current_title is not None:
                idx = len(entries) + 1
                entries.append(
                    ManualEntry(
                        idx=idx,
                        title=current_title,
                        body=current_body,
                        known=parse_known(current_body),
                        source_url=parse_source_url(current_body),
                        missing=parse_missing(current_body),
                        statuses=parse_statuses(current_body),
                    )
                )
            current_title = line[4:].strip()
            current_body = []
        elif current_title is not None:
            current_body.append(line)
    if current_title is not None:
        idx = len(entries) + 1
        entries.append(
            ManualEntry(
                idx=idx,
                title=current_title,
                body=current_body,
                known=parse_known(current_body),
                source_url=parse_source_url(current_body),
                missing=parse_missing(current_body),
                statuses=parse_statuses(current_body),
            )
        )
    return entries


def entry_to_dict(entry: ManualEntry) -> dict[str, object]:
    return {
        "idx": entry.idx,
        "title": entry.title,
        "known": entry.known,
        "source_url": entry.source_url,
        "missing": entry.missing,
        "statuses": entry.statuses,
    }


def field_record_to_dict(entry: ManualEntry, field_name: str) -> dict[str, object]:
    return {
        "idx": entry.idx,
        "title": entry.title,
        "field": field_name,
        "known": entry.known,
        "source_url": entry.source_url,
        "missing": entry.missing,
        "statuses": entry.statuses,
    }


def prompt_for_batch(batch: list[ManualEntry], batch_index: int, batch_count: int) -> str:
    payload = json.dumps([entry_to_dict(entry) for entry in batch], ensure_ascii=False, indent=2)
    return f"""You are verifying Paper-RAG++ manual-review entries for NeuroFlow-Agent.

Batch: {batch_index}/{batch_count}

Do not edit files. Use public sources as needed: source-traced paper pages, abstracts, PDFs, official proceedings, arXiv, DOI pages, Semantic Scholar, Crossref, OpenReview, CVF, PMLR, publisher pages, or official project pages.

For each input entry, verify only fields listed in `missing`. Do not infer unsupported fields. Return JSON only: an array with one object per entry.

Required object keys:
- idx
- title
- verified_fields: object with field names from `missing` only
- evidence: object mapping each verified field to a short evidence snippet or source basis
- sources: array of URLs
- confidence: object mapping each verified field to high, medium, or low
- unresolved: array of still-unresolved fields
- notes

Rules:
- Use `signal_modality` as the JSON key for signal modality.
- If a paper is non-neural AI, set signal_modality to "Non-neural AI baseline" with evidence.
- If a paper has no named dataset, describe the empirical data only when supported; otherwise leave dataset unresolved.
- If the paper is review/perspective/theory and has no paper-specific quantitative evaluation, set metric_status to not_applicable and do not return metric as unresolved.
- If no DOI is found in trusted sources, leave DOI unresolved.
- Limitations must come from author discussion, limitations, conclusion, explicit caveats, or clearly stated experimental boundaries.
- Do not return Markdown or commentary outside the JSON array.

Input entries:

```json
{payload}
```
"""


def prompt_for_field_batch(records: list[dict[str, object]], batch_index: int, batch_count: int) -> str:
    payload = json.dumps(records, ensure_ascii=False, indent=2)
    return f"""You are verifying Paper-RAG++ unresolved field targets for NeuroFlow-Agent.

Batch: {batch_index}/{batch_count}

Do not edit files. Use public sources as needed: strict metadata sources, paper pages, abstracts, PDFs, official proceedings, arXiv, DOI pages, Semantic Scholar, Crossref, OpenAlex, PubMed, OpenReview, CVF, PMLR, publisher pages, official project pages, or official data/code artifacts.

For each input target, verify only the listed `field`. Return JSONL only: one object per target.

Required JSONL keys:
- idx
- title
- field
- value
- evidence
- sources
- source_tier
- confidence
- action

Rules:
- Use action=accept only when the field is directly supported.
- Use action=not_applicable only for field=metric_status with value="not_applicable" when paper_type and source evidence show no paper-specific quantitative evaluation.
- Use action=keep_unresolved with value="" when the field cannot be verified from trusted sources.
- DOI requires tier0_metadata or tier1_paper_text evidence.
- Dataset, metric, and limitations require paper text, official PDF, PMC, OpenReview, CVF, PMLR, ACL, publisher full text, or equivalent official paper evidence.
- A metric target for a review/perspective/theory article may be closed by returning field=metric_status, value=not_applicable, action=not_applicable, and evidence from paper type/no primary evaluation.
- Official GitHub, Zenodo, OSF, or Hugging Face can support dataset access details but cannot alone support paper metric or limitations.
- Blogs, WeChat posts, tutorials, and media articles are only leads; mark them action=needs_human and source_tier=tier3_grey_literature.
- Limitations must come from explicit author limitations, discussion/conclusion caveats, or clearly stated experimental boundaries. Do not invent generic critiques.
- Do not return Markdown or commentary outside JSONL.

Input targets:

```json
{payload}
```
"""


def filter_entries(entries: list[ManualEntry], fields: set[str]) -> list[ManualEntry]:
    if not fields:
        return entries
    filtered: list[ManualEntry] = []
    for entry in entries:
        missing = [field_name for field_name in entry.missing if field_name in fields]
        if not missing:
            continue
        filtered.append(
            ManualEntry(
                idx=entry.idx,
                title=entry.title,
                body=entry.body,
                known=entry.known,
                source_url=entry.source_url,
                missing=missing,
                statuses=entry.statuses,
            )
        )
    return filtered


def write_batches(
    entries: list[ManualEntry],
    output_dir: Path,
    batch_size: int,
    limit: int | None,
    field_records: bool,
) -> None:
    if limit is not None:
        entries = entries[:limit]
    output_dir.mkdir(parents=True, exist_ok=True)
    items: list[ManualEntry] | list[dict[str, object]]
    if field_records:
        items = [field_record_to_dict(entry, field_name) for entry in entries for field_name in entry.missing]
    else:
        items = entries
    batch_count = math.ceil(len(items) / batch_size) if items else 0
    manifest: list[dict[str, object]] = []
    for offset in range(0, len(items), batch_size):
        batch = items[offset : offset + batch_size]
        batch_index = offset // batch_size + 1
        stem = f"batch-{batch_index:03d}"
        jsonl_path = output_dir / f"{stem}.input.jsonl"
        prompt_path = output_dir / f"{stem}.prompt.md"
        with jsonl_path.open("w", encoding="utf-8") as handle:
            for item in batch:
                payload = item if isinstance(item, dict) else entry_to_dict(item)
                handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")
        if field_records:
            prompt_path.write_text(prompt_for_field_batch(batch, batch_index, batch_count), encoding="utf-8")
            idx_values = [int(item["idx"]) for item in batch if isinstance(item, dict)]
        else:
            prompt_path.write_text(prompt_for_batch(batch, batch_index, batch_count), encoding="utf-8")
            idx_values = [item.idx for item in batch if isinstance(item, ManualEntry)]
        manifest.append(
            {
                "batch": batch_index,
                "entries": len(batch),
                "idx_start": min(idx_values) if idx_values else None,
                "idx_end": max(idx_values) if idx_values else None,
                "input_jsonl": str(jsonl_path),
                "prompt": str(prompt_path),
            }
        )
    (output_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manual-review", type=Path, default=DEFAULT_MANUAL_REVIEW)
    parser.add_argument("--output-dir", type=Path, default=PRIVATE_DIR / "full-run-inputs")
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--fields", help="Comma-separated unresolved fields to export")
    parser.add_argument("--field-records", action="store_true", help="Export one JSONL row per unresolved field")
    args = parser.parse_args()
    if args.batch_size <= 0:
        raise SystemExit("--batch-size must be positive")
    entries = parse_manual_review(args.manual_review)
    fields = {clean(field_name) for field_name in (args.fields or "").split(",") if clean(field_name)}
    entries = filter_entries(entries, fields)
    write_batches(entries, args.output_dir, args.batch_size, args.limit, args.field_records)
    selected = min(len(entries), args.limit) if args.limit is not None else len(entries)
    print(f"Exported {selected} entries to {args.output_dir}")


if __name__ == "__main__":
    main()
