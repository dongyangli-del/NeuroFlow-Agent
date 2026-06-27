#!/usr/bin/env python3
"""Preview integration of agent-produced paper field verifications.

The script validates JSON/JSONL emitted by sub-agents for
`manual-review-needed.md` entries and creates a deterministic private preview.
It is intentionally conservative:

- no public reference file is changed unless `--apply-manual-review` is used;
- only fields that are currently unresolved for an entry can be accepted;
- `null`, empty, low-confidence, or evidence-free fields are rejected;
- accepted fields are marked `agent-source-traced`, not human/expert reviewed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
REFERENCES = ROOT / "skills" / "paper-rag-plus" / "references"
PRIVATE_DIR = ROOT / ".private" / "paper-verification-batches"

DEFAULT_MANUAL_REVIEW = REFERENCES / "manual-review-needed.md"
DEFAULT_PREVIEW = PRIVATE_DIR / "agent-verification-preview.md"
DEFAULT_NORMALIZED = PRIVATE_DIR / "agent-verifications.normalized.jsonl"

ALLOWED_CONFIDENCE = {"high", "medium"}
REJECTED_CONFIDENCE = {"low"}

FIELD_ALIASES = {
    "signal_modality": "signal modality",
    "signal modality": "signal modality",
    "dataset": "dataset",
    "doi": "doi",
    "limitations": "limitations",
    "method": "method",
    "metric": "metric",
    "task": "task",
    "venue": "venue",
    "year": "year",
}

SOURCE_TIER_ALIASES = {
    "tier0": "tier0_metadata",
    "tier 0": "tier0_metadata",
    "tier0 metadata": "tier0_metadata",
    "tier0_metadata": "tier0_metadata",
    "tier1": "tier1_paper_text",
    "tier 1": "tier1_paper_text",
    "tier1 pdf": "tier1_paper_text",
    "tier1_pdf": "tier1_paper_text",
    "tier1 paper text": "tier1_paper_text",
    "tier1_paper_text": "tier1_paper_text",
    "tier2": "tier2_official_artifact",
    "tier 2": "tier2_official_artifact",
    "tier2 official artifact": "tier2_official_artifact",
    "tier2_official_artifact": "tier2_official_artifact",
    "tier3": "tier3_grey_literature",
    "tier 3": "tier3_grey_literature",
    "tier3 grey literature": "tier3_grey_literature",
    "tier3_grey_literature": "tier3_grey_literature",
}


@dataclass
class ManualEntry:
    idx: int
    title: str
    body: list[str]
    unresolved: set[str] = field(default_factory=set)


@dataclass
class AcceptedField:
    idx: int
    title: str
    field: str
    value: str
    evidence: str
    confidence: str
    sources: list[str]
    source_tier: str = ""


@dataclass
class RejectedField:
    idx: int
    title: str
    field: str
    reason: str


def normalize_title(value: str) -> str:
    value = str(value or "").lower()
    value = value.replace("ﬁ", "fi").replace("ﬂ", "fl")
    value = re.sub(r"([a-z])-\s+([a-z])", r"\1\2", value)
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def canonical_field(field: str) -> str:
    return FIELD_ALIASES.get(clean(field).lower(), clean(field).lower())


def canonical_source_tier(value: Any) -> str:
    if isinstance(value, list):
        tiers = [canonical_source_tier(item) for item in value]
        return ";".join(dict.fromkeys(item for item in tiers if item))
    text = clean(value).lower().replace("-", " ").replace("_", " ")
    return SOURCE_TIER_ALIASES.get(text, text.replace(" ", "_"))


def canonical_confidence(value: Any) -> str:
    text = clean(value).lower()
    if text in {"high", "medium", "low"}:
        return text
    try:
        score = float(text)
    except ValueError:
        return text
    if score >= 0.8:
        return "high"
    if score >= 0.5:
        return "medium"
    return "low"


def source_tier_allows(field_name: str, source_tier: str) -> tuple[bool, str]:
    tiers = {item.strip() for item in source_tier.split(";") if item.strip()}
    if not tiers:
        return True, ""
    if tiers == {"tier3_grey_literature"}:
        return False, "grey literature cannot be sole evidence"
    if field_name == "doi" and not any(item in tiers for item in {"tier0_metadata", "tier1_paper_text"}):
        return False, "doi requires tier0 metadata or tier1 paper/publisher evidence"
    if field_name in {"dataset", "metric", "limitations", "signal modality"} and tiers == {"tier2_official_artifact"}:
        return False, f"{field_name} requires paper text/metadata support, not only official artifact"
    return True, ""


def parse_unresolved(body: list[str]) -> set[str]:
    unresolved: set[str] = set()
    for line in body:
        if line.startswith("Auto unresolved after field pass:"):
            values = line.split(":", 1)[1]
        elif line.startswith("Missing or unresolved:"):
            values = line.split(":", 1)[1]
        else:
            continue
        for value in values.split(","):
            field_name = canonical_field(value)
            if field_name and field_name not in {"none", "n/a", "null"}:
                unresolved.add(field_name)
    return unresolved


def parse_manual_review(path: Path) -> tuple[list[str], list[ManualEntry]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    prefix: list[str] = []
    entries: list[ManualEntry] = []
    current_title: str | None = None
    current_body: list[str] = []
    for line in lines:
        if line.startswith("### "):
            if current_title is not None:
                entries.append(
                    ManualEntry(
                        idx=len(entries) + 1,
                        title=current_title,
                        body=current_body,
                        unresolved=parse_unresolved(current_body),
                    )
                )
            current_title = line[4:].strip()
            current_body = []
        elif current_title is None:
            prefix.append(line)
        else:
            current_body.append(line)
    if current_title is not None:
        entries.append(
            ManualEntry(
                idx=len(entries) + 1,
                title=current_title,
                body=current_body,
                unresolved=parse_unresolved(current_body),
            )
        )
    return prefix, entries


def load_agent_records(paths: list[Path]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in paths:
        text = path.read_text(encoding="utf-8").strip()
        if not text:
            continue
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            data = None
        if isinstance(data, list):
            records.extend(record for record in data if isinstance(record, dict))
            continue
        if isinstance(data, dict):
            records.append(data)
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path}:{line_number}: invalid JSONL: {exc}") from exc
            if not isinstance(record, dict):
                raise SystemExit(f"{path}:{line_number}: JSONL row must be an object")
            records.append(record)
    return records


def as_sources(value: Any) -> list[str]:
    if isinstance(value, list):
        return [clean(item) for item in value if clean(item)]
    if clean(value):
        return [clean(value)]
    return []


def validate_record(
    record: dict[str, Any],
    entries_by_idx: dict[int, ManualEntry],
    title_to_indices: dict[str, list[int]],
) -> tuple[list[AcceptedField], list[RejectedField]]:
    accepted: list[AcceptedField] = []
    rejected: list[RejectedField] = []
    idx = record.get("idx")
    title = clean(record.get("title"))
    if not isinstance(idx, int):
        rejected.append(RejectedField(idx=-1, title=title, field="record", reason="missing integer idx"))
        return accepted, rejected
    entry = entries_by_idx.get(idx)
    if entry is None:
        rejected.append(RejectedField(idx=idx, title=title, field="record", reason="idx not present in manual review"))
        return accepted, rejected
    if normalize_title(title) != normalize_title(entry.title):
        possible = title_to_indices.get(normalize_title(title), [])
        reason = f"title mismatch for idx {idx}; matching title indices: {possible or 'none'}"
        rejected.append(RejectedField(idx=idx, title=title or entry.title, field="record", reason=reason))
        return accepted, rejected

    if "field" in record and "value" in record:
        return validate_normalized_record(record, entry)

    verified_fields = record.get("verified_fields")
    if not isinstance(verified_fields, dict):
        rejected.append(RejectedField(idx=idx, title=entry.title, field="record", reason="verified_fields missing"))
        return accepted, rejected
    evidence = record.get("evidence") if isinstance(record.get("evidence"), dict) else {}
    confidence = record.get("confidence") if isinstance(record.get("confidence"), dict) else {}
    source_tier = record.get("source_tier") if isinstance(record.get("source_tier"), dict) else {}
    sources = as_sources(record.get("sources"))

    for raw_field, raw_value in verified_fields.items():
        field_name = canonical_field(raw_field)
        action = clean(record.get("action", "accept")).lower()
        if action in {"keep_unresolved", "needs_human"}:
            rejected.append(RejectedField(idx=idx, title=entry.title, field=field_name, reason=f"action={action}"))
            continue
        value = clean(raw_value)
        if field_name not in FIELD_ALIASES.values():
            rejected.append(RejectedField(idx=idx, title=entry.title, field=field_name, reason="unknown field"))
            continue
        if not value or value.lower() in {"none", "null", "n/a"}:
            rejected.append(RejectedField(idx=idx, title=entry.title, field=field_name, reason="empty/null value"))
            continue
        if field_name not in entry.unresolved:
            rejected.append(RejectedField(idx=idx, title=entry.title, field=field_name, reason="field not currently unresolved"))
            continue
        field_evidence = clean(evidence.get(raw_field) or evidence.get(field_name))
        if not field_evidence:
            rejected.append(RejectedField(idx=idx, title=entry.title, field=field_name, reason="missing evidence"))
            continue
        field_confidence = canonical_confidence(confidence.get(raw_field) or confidence.get(field_name))
        if field_confidence in REJECTED_CONFIDENCE:
            rejected.append(RejectedField(idx=idx, title=entry.title, field=field_name, reason="low confidence"))
            continue
        if field_confidence not in ALLOWED_CONFIDENCE:
            rejected.append(RejectedField(idx=idx, title=entry.title, field=field_name, reason="missing/invalid confidence"))
            continue
        field_source_tier = canonical_source_tier(source_tier.get(raw_field) or source_tier.get(field_name) or record.get("source_tier"))
        allowed, reason = source_tier_allows(field_name, field_source_tier)
        if not allowed:
            rejected.append(RejectedField(idx=idx, title=entry.title, field=field_name, reason=reason))
            continue
        accepted.append(
            AcceptedField(
                idx=idx,
                title=entry.title,
                field=field_name,
                value=value,
                evidence=field_evidence,
                confidence=field_confidence,
                sources=sources,
                source_tier=field_source_tier,
            )
        )
    return accepted, rejected


def validate_normalized_record(
    record: dict[str, Any],
    entry: ManualEntry,
) -> tuple[list[AcceptedField], list[RejectedField]]:
    accepted: list[AcceptedField] = []
    rejected: list[RejectedField] = []
    field_name = canonical_field(clean(record.get("field")))
    action = clean(record.get("action", "accept")).lower()
    if action in {"keep_unresolved", "needs_human"}:
        rejected.append(RejectedField(idx=entry.idx, title=entry.title, field=field_name, reason=f"action={action}"))
        return accepted, rejected
    value = clean(record.get("value"))
    if field_name not in FIELD_ALIASES.values():
        rejected.append(RejectedField(idx=entry.idx, title=entry.title, field=field_name, reason="unknown field"))
        return accepted, rejected
    if not value or value.lower() in {"none", "null", "n/a"}:
        rejected.append(RejectedField(idx=entry.idx, title=entry.title, field=field_name, reason="empty/null value"))
        return accepted, rejected
    if field_name not in entry.unresolved:
        rejected.append(RejectedField(idx=entry.idx, title=entry.title, field=field_name, reason="field not currently unresolved"))
        return accepted, rejected
    evidence = clean(record.get("evidence"))
    if not evidence:
        rejected.append(RejectedField(idx=entry.idx, title=entry.title, field=field_name, reason="missing evidence"))
        return accepted, rejected
    confidence = canonical_confidence(record.get("confidence"))
    if confidence in REJECTED_CONFIDENCE:
        rejected.append(RejectedField(idx=entry.idx, title=entry.title, field=field_name, reason="low confidence"))
        return accepted, rejected
    if confidence not in ALLOWED_CONFIDENCE:
        rejected.append(RejectedField(idx=entry.idx, title=entry.title, field=field_name, reason="missing/invalid confidence"))
        return accepted, rejected
    source_tier = canonical_source_tier(record.get("source_tier"))
    allowed, reason = source_tier_allows(field_name, source_tier)
    if not allowed:
        rejected.append(RejectedField(idx=entry.idx, title=entry.title, field=field_name, reason=reason))
        return accepted, rejected
    accepted.append(
        AcceptedField(
            idx=entry.idx,
            title=entry.title,
            field=field_name,
            value=value,
            evidence=evidence,
            confidence=confidence,
            sources=as_sources(record.get("sources")),
            source_tier=source_tier,
        )
    )
    return accepted, rejected


def build_preview(
    entries: list[ManualEntry],
    accepted: list[AcceptedField],
    rejected: list[RejectedField],
    status_label: str,
) -> str:
    accepted_by_idx: dict[int, list[AcceptedField]] = {}
    for item in accepted:
        accepted_by_idx.setdefault(item.idx, []).append(item)
    remaining_by_idx = {entry.idx: set(entry.unresolved) for entry in entries}
    for item in accepted:
        remaining_by_idx.setdefault(item.idx, set()).discard(item.field)
    touched_entries = sorted(accepted_by_idx)
    remaining_touched = sum(len(remaining_by_idx.get(idx, set())) for idx in touched_entries)

    lines = [
        "# Agent Verification Integration Preview",
        "",
        f"Generated: {dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat()}",
        "",
        f"Status label for accepted fields: `{status_label}`",
        "",
        "## Summary",
        "",
        f"- Manual review entries: {len(entries)}",
        f"- Entries with accepted updates: {len(touched_entries)}",
        f"- Accepted field updates: {len(accepted)}",
        f"- Rejected field candidates: {len(rejected)}",
        f"- Remaining unresolved fields in touched entries after preview: {remaining_touched}",
        "",
        "## Accepted Updates",
        "",
    ]
    if not accepted:
        lines.append("- No accepted updates.")
    else:
        for idx in touched_entries:
            entry = entries[idx - 1]
            lines.append(f"### {idx}. {entry.title}")
            lines.append("")
            for item in sorted(accepted_by_idx[idx], key=lambda value: value.field):
                lines.append(f"- `{item.field}` -> {item.value}")
                lines.append(f"  - confidence: {item.confidence}")
                lines.append(f"  - evidence: {item.evidence}")
                if item.source_tier:
                    lines.append(f"  - source tier: {item.source_tier}")
                if item.sources:
                    lines.append(f"  - sources: {'; '.join(item.sources)}")
            remaining = sorted(remaining_by_idx.get(idx, set()))
            lines.append(f"- Remaining unresolved after preview: {', '.join(remaining) if remaining else 'none'}")
            lines.append("")

    lines.extend(["## Rejected Candidates", ""])
    if not rejected:
        lines.append("- No rejected candidates.")
    else:
        for item in rejected:
            label = f"{item.idx}. {item.title}" if item.idx > 0 else item.title or "unknown"
            lines.append(f"- {label} `{item.field}`: {item.reason}")
    lines.append("")
    return "\n".join(lines)


def write_normalized(path: Path, accepted: list[AcceptedField], status_label: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for item in accepted:
            handle.write(
                json.dumps(
                    {
                        "idx": item.idx,
                        "title": item.title,
                        "field": item.field,
                        "value": item.value,
                        "evidence": item.evidence,
                        "confidence": item.confidence,
                        "sources": item.sources,
                        "source_tier": item.source_tier,
                        "verification_status": status_label,
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                )
                + "\n"
            )


def format_unresolved(fields: set[str]) -> str:
    return ", ".join(sorted(fields)) if fields else "none"


def strip_previous_agent_lines(body: list[str], updated_fields: set[str] | None = None) -> list[str]:
    updated_fields = updated_fields or set()
    stripped: list[str] = []
    previous_blank = False
    for line in body:
        if line.startswith("Agent unresolved after preview:"):
            continue
        remove_updated_field = False
        for field_name in updated_fields:
            if line.startswith(f"Agent verified {field_name}:") or line.startswith(
                (
                    f"Agent field evidence ({field_name}):",
                    f"Agent field confidence ({field_name}):",
                    f"Agent field source tier ({field_name}):",
                    f"Agent field sources ({field_name}):",
                )
            ):
                remove_updated_field = True
                break
        if remove_updated_field:
            continue
        if line == "":
            if previous_blank:
                continue
            previous_blank = True
        else:
            previous_blank = False
        stripped.append(line)
    return stripped


def rewrite_entry_body(body: list[str], remaining: set[str], updated_fields: set[str]) -> list[str]:
    rewritten: list[str] = []
    for line in strip_previous_agent_lines(body, updated_fields):
        if line.startswith("Missing or unresolved:"):
            rewritten.append(f"Missing or unresolved: {format_unresolved(remaining)}")
        elif line.startswith("Auto unresolved after field pass:"):
            rewritten.append(f"Auto unresolved after field pass: {format_unresolved(remaining)}")
        else:
            rewritten.append(line)
    return rewritten


def update_prefix_summary(prefix: list[str], remaining_by_idx: dict[int, set[str]]) -> list[str]:
    counts: dict[str, int] = {field_name: 0 for field_name in FIELD_ALIASES.values()}
    for remaining in remaining_by_idx.values():
        for field_name in remaining:
            counts[field_name] = counts.get(field_name, 0) + 1

    output: list[str] = []
    for line in prefix:
        match = re.fullmatch(r"- ([a-z ]+): \d+", line)
        if match and match.group(1) in counts:
            output.append(f"- {match.group(1)}: {counts[match.group(1)]}")
        else:
            output.append(line)
    return output


def apply_manual_review(path: Path, entries: list[ManualEntry], accepted: list[AcceptedField], status_label: str) -> None:
    accepted_by_idx: dict[int, list[AcceptedField]] = {}
    for item in accepted:
        accepted_by_idx.setdefault(item.idx, []).append(item)

    remaining_by_idx = {entry.idx: set(entry.unresolved) for entry in entries}
    for item in accepted:
        remaining_by_idx.setdefault(item.idx, set()).discard(item.field)

    output: list[str] = []
    prefix, _ = parse_manual_review(path)
    output.extend(update_prefix_summary(prefix, remaining_by_idx))
    if output and output[-1] != "":
        output.append("")
    for entry in entries:
        output.append(f"### {entry.title}")
        updates = accepted_by_idx.get(entry.idx, [])
        updated_fields = {item.field for item in updates}
        rewritten_body = rewrite_entry_body(entry.body, remaining_by_idx.get(entry.idx, set()), updated_fields)
        output.extend(rewritten_body)
        if updates:
            if output and output[-1] != "":
                output.append("")
            if not any(line.startswith("Agent field verification status:") for line in rewritten_body):
                output.append(f"Agent field verification status: {status_label}")
            for item in sorted(updates, key=lambda value: value.field):
                output.append(f"Agent verified {item.field}: {item.value}")
                output.append(f"Agent field evidence ({item.field}): {item.evidence}")
                output.append(f"Agent field confidence ({item.field}): {item.confidence}")
                if item.source_tier:
                    output.append(f"Agent field source tier ({item.field}): {item.source_tier}")
                if item.sources:
                    output.append(f"Agent field sources ({item.field}): {'; '.join(item.sources)}")
        if updates or any(line.startswith("Agent verified ") for line in rewritten_body):
            output.append(f"Agent unresolved after preview: {format_unresolved(remaining_by_idx.get(entry.idx, set()))}")
        output.append("")
    path.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("agent_results", nargs="+", type=Path, help="JSON array or JSONL files from sub-agents")
    parser.add_argument("--manual-review", type=Path, default=DEFAULT_MANUAL_REVIEW)
    parser.add_argument("--preview", type=Path, default=DEFAULT_PREVIEW)
    parser.add_argument("--normalized-jsonl", type=Path, default=DEFAULT_NORMALIZED)
    parser.add_argument("--status-label", default="agent-source-traced")
    parser.add_argument("--apply-manual-review", action="store_true")
    args = parser.parse_args()

    if not args.manual_review.exists():
        raise SystemExit(f"Manual review file not found: {args.manual_review}")
    missing_inputs = [path for path in args.agent_results if not path.exists()]
    if missing_inputs:
        raise SystemExit("Agent result file(s) not found: " + ", ".join(str(path) for path in missing_inputs))

    _, entries = parse_manual_review(args.manual_review)
    entries_by_idx = {entry.idx: entry for entry in entries}
    title_to_indices: dict[str, list[int]] = {}
    for entry in entries:
        title_to_indices.setdefault(normalize_title(entry.title), []).append(entry.idx)

    accepted: list[AcceptedField] = []
    rejected: list[RejectedField] = []
    for record in load_agent_records(args.agent_results):
        record_accepted, record_rejected = validate_record(record, entries_by_idx, title_to_indices)
        accepted.extend(record_accepted)
        rejected.extend(record_rejected)

    args.preview.parent.mkdir(parents=True, exist_ok=True)
    args.preview.write_text(build_preview(entries, accepted, rejected, args.status_label), encoding="utf-8")
    write_normalized(args.normalized_jsonl, accepted, args.status_label)
    if args.apply_manual_review:
        apply_manual_review(args.manual_review, entries, accepted, args.status_label)

    print(f"Accepted field updates: {len(accepted)}")
    print(f"Rejected field candidates: {len(rejected)}")
    print(f"Preview written: {args.preview}")
    print(f"Normalized JSONL written: {args.normalized_jsonl}")
    if args.apply_manual_review:
        print(f"Manual review updated: {args.manual_review}")


if __name__ == "__main__":
    main()
