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


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def parse_missing(body: list[str]) -> list[str]:
    for prefix in ("Auto unresolved after field pass:", "Missing or unresolved:"):
        for line in body:
            if line.startswith(prefix):
                return [clean(value) for value in line.split(":", 1)[1].split(",") if clean(value)]
    return []


def parse_known(body: list[str]) -> dict[str, str]:
    known: dict[str, str] = {}
    for key in ("Year", "Venue", "DOI"):
        for line in body:
            if line.startswith(f"{key}:"):
                known[key.lower()] = clean(line.split(":", 1)[1])
                break
        else:
            known[key.lower()] = ""
    return known


def parse_source_url(body: list[str]) -> str:
    for line in body:
        if line.startswith("Auto source URL:"):
            return clean(line.split(":", 1)[1])
    return ""


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
- If no DOI is found in trusted sources, leave DOI unresolved.
- Limitations must come from author discussion, limitations, conclusion, explicit caveats, or clearly stated experimental boundaries.
- Do not return Markdown or commentary outside the JSON array.

Input entries:

```json
{payload}
```
"""


def write_batches(entries: list[ManualEntry], output_dir: Path, batch_size: int, limit: int | None) -> None:
    if limit is not None:
        entries = entries[:limit]
    output_dir.mkdir(parents=True, exist_ok=True)
    batch_count = math.ceil(len(entries) / batch_size) if entries else 0
    manifest: list[dict[str, object]] = []
    for offset in range(0, len(entries), batch_size):
        batch = entries[offset : offset + batch_size]
        batch_index = offset // batch_size + 1
        stem = f"batch-{batch_index:03d}"
        jsonl_path = output_dir / f"{stem}.input.jsonl"
        prompt_path = output_dir / f"{stem}.prompt.md"
        with jsonl_path.open("w", encoding="utf-8") as handle:
            for entry in batch:
                handle.write(json.dumps(entry_to_dict(entry), ensure_ascii=False, sort_keys=True) + "\n")
        prompt_path.write_text(prompt_for_batch(batch, batch_index, batch_count), encoding="utf-8")
        manifest.append(
            {
                "batch": batch_index,
                "entries": len(batch),
                "idx_start": batch[0].idx,
                "idx_end": batch[-1].idx,
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
    args = parser.parse_args()
    if args.batch_size <= 0:
        raise SystemExit("--batch-size must be positive")
    entries = parse_manual_review(args.manual_review)
    write_batches(entries, args.output_dir, args.batch_size, args.limit)
    selected = min(len(entries), args.limit) if args.limit is not None else len(entries)
    print(f"Exported {selected} entries to {args.output_dir}")


if __name__ == "__main__":
    main()
