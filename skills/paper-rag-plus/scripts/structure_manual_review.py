#!/usr/bin/env python3
"""Rewrite Paper-RAG++ manual-review entries into the structured schema.

The source file may be the older flat `manual-review-needed.md` format with
`Year:`, `Agent verified metric:`, and repeated unresolved-status lines. This
script preserves the verified evidence while normalizing each entry into:

- Bibliographic
- Paper type
- Evidence fields
- Verification
"""

from __future__ import annotations

import argparse
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REFERENCES = ROOT / "skills" / "paper-rag-plus" / "references"
DEFAULT_MANUAL_REVIEW = REFERENCES / "manual-review-needed.md"

PAPER_TYPES = {"primary_research", "review", "perspective", "theory", "benchmark", "dataset", "system"}
FINAL_FIELDS = {
    "year",
    "venue",
    "doi",
    "signal_modality",
    "input_modality",
    "task_taxonomy",
    "paper_objective",
    "method_family",
    "method_summary",
    "dataset",
    "dataset_role",
    "metric",
    "metric_status",
    "limitations",
    "limitation_source",
}
EMPTY_VALUES = {"", "needs verification", "not identified in imported metadata", "unresolved", "n/a", "none", "null"}
LIMITATION_REQUIRES_PAPER_TEXT = {
    "brain machine coupled learning method for facial emotion recognition",
    "fast neural distance field based three dimensional reconstruction method for geometrical parameter extraction of walnut shell from multiview images",
}


@dataclass
class Entry:
    idx: int
    title: str
    body: list[str]
    year: str = ""
    venue: str = ""
    doi: str = ""
    auto_status: str = ""
    auto_matched_title: str = ""
    auto_source_url: str = ""
    auto_fields: dict[str, str] = field(default_factory=dict)
    agent_fields: dict[str, str] = field(default_factory=dict)
    agent_evidence: dict[str, str] = field(default_factory=dict)
    agent_confidence: dict[str, str] = field(default_factory=dict)
    agent_sources: dict[str, str] = field(default_factory=dict)
    agent_source_tier: dict[str, str] = field(default_factory=dict)
    unresolved: set[str] = field(default_factory=set)


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def canonical_field(value: str) -> str:
    field_name = clean(value).lower().replace(" ", "_")
    return {
        "signal_modality": "signal_modality",
        "signal_modality:": "signal_modality",
        "signal": "signal_modality",
        "task": "task_taxonomy",
        "method": "method_summary",
    }.get(field_name, field_name)


def parse_fields(value: str) -> set[str]:
    fields: set[str] = set()
    for item in value.split(","):
        field_name = canonical_field(item)
        if field_name and field_name not in {"none", "n/a", "null"}:
            fields.add(field_name)
    return fields


def normalize_key(value: str) -> str:
    return clean(value).lower().replace(" ", "_")


def normalize_title(value: str) -> str:
    value = str(value or "").lower()
    value = value.replace("ﬁ", "fi").replace("ﬂ", "fl")
    value = re.sub(r"([a-z])-\s+([a-z])", r"\1\2", value)
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def parse_manual_review(path: Path) -> tuple[list[str], list[Entry]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    prefix: list[str] = []
    entries: list[Entry] = []
    current_title: str | None = None
    current_body: list[str] = []
    for line in lines:
        if line.startswith("### "):
            if current_title is not None:
                entries.append(parse_entry(len(entries) + 1, current_title, current_body))
            current_title = line[4:].strip()
            current_body = []
        elif current_title is None:
            prefix.append(line)
        else:
            current_body.append(line)
    if current_title is not None:
        entries.append(parse_entry(len(entries) + 1, current_title, current_body))
    return prefix, entries


def parse_entry(idx: int, title: str, body: list[str]) -> Entry:
    entry = Entry(idx=idx, title=title, body=body)
    section = ""
    for line in body:
        if line in {"Bibliographic:", "Paper type:", "Evidence fields:", "Verification:", "Field evidence:", "Identity trace:"}:
            section = line[:-1]
            continue
        if section == "Bibliographic" and line.startswith("- year:"):
            entry.year = clean(line.split(":", 1)[1])
        elif section == "Bibliographic" and line.startswith("- venue:"):
            entry.venue = clean(line.split(":", 1)[1])
        elif section == "Bibliographic" and line.startswith("- doi:"):
            entry.doi = clean(line.split(":", 1)[1])
        elif section == "Evidence fields" and line.startswith("- "):
            key, value = line[2:].split(":", 1)
            key = normalize_key(key)
            value = clean(value)
            if key == "signal_modality":
                entry.agent_fields["signal_modality"] = value
            elif key == "task_taxonomy":
                entry.agent_fields["task_taxonomy"] = value
            elif key in {"method_summary", "dataset", "metric", "limitations", "metric_status"}:
                entry.agent_fields[key] = value
            elif key == "method_family":
                entry.auto_fields["method_summary"] = value
        elif section == "Verification" and line.startswith("- final_unresolved_fields:"):
            entry.unresolved.update(parse_fields(line.split(":", 1)[1]))
        elif section == "Verification" and line.startswith("- evidence_sources:"):
            sources = clean(line.split(":", 1)[1])
            if sources and sources != "unresolved":
                entry.agent_sources["record"] = sources
        elif section == "Verification" and line.startswith("- evidence_tier:"):
            tier = clean(line.split(":", 1)[1])
            if tier and tier != "unresolved":
                entry.agent_source_tier["record"] = tier
        elif section == "Verification" and line.startswith("- confidence:"):
            confidence_value = clean(line.split(":", 1)[1])
            if confidence_value and confidence_value != "unresolved":
                entry.agent_confidence["record"] = confidence_value
        elif section == "Field evidence" and line.startswith("- ") and ":" in line:
            key, value = line[2:].split(":", 1)
            field_name = canonical_field(key)
            for part in value.split("|"):
                part = clean(part)
                if part.startswith("evidence="):
                    entry.agent_evidence[field_name] = clean(part.removeprefix("evidence="))
                elif part.startswith("confidence="):
                    entry.agent_confidence[field_name] = clean(part.removeprefix("confidence="))
                elif part.startswith("tier="):
                    entry.agent_source_tier[field_name] = clean(part.removeprefix("tier="))
        elif section == "Identity trace" and line.startswith("- auto_verification_status:"):
            entry.auto_status = clean(line.split(":", 1)[1])
        elif section == "Identity trace" and line.startswith("- auto_matched_title:"):
            entry.auto_matched_title = clean(line.split(":", 1)[1])
        elif section == "Identity trace" and line.startswith("- auto_source_url:"):
            entry.auto_source_url = clean(line.split(":", 1)[1])
        elif line.startswith("Year:"):
            entry.year = clean(line.split(":", 1)[1])
        elif line.startswith("Venue:"):
            entry.venue = clean(line.split(":", 1)[1])
        elif line.startswith("DOI:"):
            entry.doi = clean(line.split(":", 1)[1])
        elif line.startswith("Auto verification status:"):
            entry.auto_status = clean(line.split(":", 1)[1])
        elif line.startswith("Auto matched title:"):
            entry.auto_matched_title = clean(line.split(":", 1)[1])
        elif line.startswith("Auto source URL:"):
            entry.auto_source_url = clean(line.split(":", 1)[1])
        elif line.startswith("Missing or unresolved:"):
            entry.unresolved.update(parse_fields(line.split(":", 1)[1]))
        elif line.startswith("Auto unresolved after field pass:"):
            entry.unresolved.update(parse_fields(line.split(":", 1)[1]))
        elif line.startswith("Agent unresolved after preview:"):
            entry.unresolved.update(parse_fields(line.split(":", 1)[1]))
        elif line.startswith("Auto verified "):
            name, value = line[len("Auto verified ") :].split(":", 1)
            entry.auto_fields[canonical_field(name)] = clean(value)
        elif line.startswith("Agent verified "):
            name, value = line[len("Agent verified ") :].split(":", 1)
            entry.agent_fields[canonical_field(name)] = clean(value)
        elif line.startswith("Agent field evidence ("):
            name, value = line[len("Agent field evidence (") :].split("):", 1)
            entry.agent_evidence[canonical_field(name)] = clean(value)
        elif line.startswith("Agent field confidence ("):
            name, value = line[len("Agent field confidence (") :].split("):", 1)
            entry.agent_confidence[canonical_field(name)] = clean(value)
        elif line.startswith("Agent field source tier ("):
            name, value = line[len("Agent field source tier (") :].split("):", 1)
            entry.agent_source_tier[canonical_field(name)] = clean(value)
        elif line.startswith("Agent field sources ("):
            name, value = line[len("Agent field sources (") :].split("):", 1)
            entry.agent_sources[canonical_field(name)] = clean(value)
    return entry


def value_for(entry: Entry, field_name: str) -> str:
    for value in (entry.agent_fields.get(field_name), entry.auto_fields.get(field_name)):
        cleaned = clean(value or "")
        if cleaned.lower() not in EMPTY_VALUES:
            return cleaned
    return ""


def evidence_for(entry: Entry, field_name: str) -> str:
    return entry.agent_evidence.get(field_name, "")


def confidence_for(entry: Entry, field_name: str) -> str:
    return entry.agent_confidence.get(field_name, "")


def sources_for(entry: Entry) -> list[str]:
    sources: list[str] = []
    if entry.auto_source_url:
        sources.append(entry.auto_source_url)
    for raw in entry.agent_sources.values():
        for item in raw.split(";"):
            item = clean(item)
            if item and item not in sources:
                sources.append(item)
    return sources


def evidence_tier(entry: Entry) -> str:
    tiers: list[str] = []
    for raw in entry.agent_source_tier.values():
        for item in raw.split(";"):
            item = clean(item)
            if item and item not in tiers:
                tiers.append(item)
    if tiers:
        return "; ".join(tiers)
    if entry.agent_fields:
        return "tier1_paper_text_or_trusted_public_source"
    if entry.auto_source_url:
        return "tier0_metadata"
    return "unverified"


def infer_paper_type(entry: Entry) -> str:
    haystack = " ".join(
        [
            entry.title,
            entry.venue,
            value_for(entry, "method_summary"),
            value_for(entry, "dataset"),
            value_for(entry, "task_taxonomy"),
        ]
    ).lower()
    if any(
        token in haystack
        for token in ("review article", "comprehensive survey", "survey ", "narrative review", "review/synthesis", "review of")
    ):
        return "review"
    if "perspective" in haystack or "opinion" in haystack:
        return "perspective"
    if any(token in haystack for token in ("theory", "theoretical", "proposal for")):
        return "theory"
    if "benchmark" in haystack:
        return "benchmark"
    if "dataset" in haystack and any(token in haystack for token in ("introduces", "large-scale", "new challenge")):
        return "dataset"
    if any(token in haystack for token in ("framework", "system", "platform", "agent")):
        return "system"
    return "primary_research"


def infer_input_modality(entry: Entry) -> str:
    signal = value_for(entry, "signal_modality").lower()
    dataset = value_for(entry, "dataset").lower()
    title = entry.title.lower()
    joined = " ".join([signal, dataset, title])
    if "fmri" in joined:
        return "fMRI"
    if "eeg" in joined:
        return "EEG"
    if any(token in joined for token in ("spike", "neuropixels", "utah", "electrode", "intracortical")):
        return "spiking/electrophysiology"
    if "ecog" in joined:
        return "ECoG"
    if "fnirs" in joined:
        return "fNIRS"
    if any(token in joined for token in ("image", "vision", "video", "visual")):
        return "image/video"
    if any(token in joined for token in ("text", "language", "speech", "word")):
        return "text/speech"
    if "motion" in joined:
        return "motion"
    if "protein" in joined:
        return "protein sequence/structure"
    return "not specified"


def infer_dataset_role(entry: Entry, paper_type: str) -> str:
    dataset = value_for(entry, "dataset").lower()
    if paper_type in {"review", "perspective", "theory"} and (
        not dataset or "no primary dataset" in dataset or "review" in dataset
    ):
        return "none_review"
    if "no primary dataset" in dataset or "no new dataset" in dataset:
        return "none_review"
    if any(token in dataset for token in ("introduces", "introduced", "new dataset", "compiled", "created")):
        return "created"
    if any(token in dataset for token in ("benchmark", "evaluation", "evaluated", "experiments", "uses", "using")):
        return "used"
    if dataset:
        return "used"
    return "unresolved"


def infer_metric_status(entry: Entry, paper_type: str, dataset_role: str) -> str:
    if value_for(entry, "metric"):
        return "applicable"
    if paper_type in {"review", "perspective", "theory"} or dataset_role == "none_review":
        return "not_applicable"
    if "metric_status" in entry.agent_fields:
        status = entry.agent_fields["metric_status"]
        return status if status in {"applicable", "not_applicable", "unresolved"} else "unresolved"
    if "metric" in entry.unresolved:
        return "unresolved"
    return "applicable"


def infer_limitation_source(entry: Entry) -> str:
    evidence = evidence_for(entry, "limitations").lower()
    value = value_for(entry, "limitations").lower()
    if normalize_title(entry.title) in LIMITATION_REQUIRES_PAPER_TEXT and not evidence:
        return "unresolved"
    if not value:
        paper_type = infer_paper_type(entry)
        if paper_type in {"review", "perspective", "theory"}:
            return "experimental_boundary"
        return "unresolved" if "limitations" in entry.unresolved else "experimental_boundary"
    if "limitations section" in evidence or "appendix" in evidence:
        return "explicit"
    if "discussion" in evidence or "conclusion" in evidence or "future" in evidence:
        return "discussion"
    if any(token in value for token in ("boundary", "limited to", "single participant", "small", "scope")):
        return "experimental_boundary"
    return "discussion"


def final_unresolved_fields(entry: Entry, metric_status: str, dataset_role: str, limitation_source: str) -> list[str]:
    fields = set(entry.unresolved)
    if metric_status == "not_applicable":
        fields.discard("metric")
    if dataset_role == "none_review":
        fields.discard("dataset")
    if limitation_source != "unresolved":
        fields.discard("limitations")
    return sorted(fields)


def verification_status(entry: Entry, unresolved: list[str]) -> str:
    if unresolved:
        return "needs_human_review"
    if entry.agent_fields:
        return "agent-source-traced"
    if entry.auto_status or entry.auto_fields:
        return "source-traced"
    return "unverified"


def confidence(entry: Entry, unresolved: list[str]) -> str:
    values = [value for value in entry.agent_confidence.values() if value]
    if any(value == "low" for value in values):
        return "low"
    if unresolved:
        return "medium" if values else "low"
    if values and all(value == "high" for value in values):
        return "high"
    if values:
        return "medium"
    return "medium" if entry.auto_status else "low"


def bullet(key: str, value: str) -> str:
    return f"- {key}: {value or 'unresolved'}"


def render_entry(entry: Entry) -> tuple[list[str], list[str]]:
    year = entry.year if clean(entry.year).lower() != "needs verification" else value_for(entry, "year")
    venue = entry.venue if clean(entry.venue).lower() != "needs verification" else value_for(entry, "venue")
    doi = entry.doi if clean(entry.doi).lower() != "needs verification" else value_for(entry, "doi")
    paper_type = infer_paper_type(entry)
    signal_modality = value_for(entry, "signal_modality")
    input_modality = infer_input_modality(entry)
    task_taxonomy = value_for(entry, "task_taxonomy")
    paper_objective = task_taxonomy or value_for(entry, "method_summary") or "unresolved"
    method_summary = value_for(entry, "method_summary")
    method_family = entry.auto_fields.get("method_summary") or method_summary
    dataset = value_for(entry, "dataset")
    dataset_role = infer_dataset_role(entry, paper_type)
    metric = value_for(entry, "metric")
    metric_status = infer_metric_status(entry, paper_type, dataset_role)
    limitations = value_for(entry, "limitations")
    limitation_source = infer_limitation_source(entry)
    if limitation_source == "unresolved":
        entry.unresolved.add("limitations")
        limitations = ""
    if not limitations and limitation_source == "experimental_boundary":
        limitations = "Paper-type boundary: review/perspective/theory article without a primary empirical experiment-specific limitation."
    unresolved = final_unresolved_fields(entry, metric_status, dataset_role, limitation_source)
    status = verification_status(entry, unresolved)
    source_list = sources_for(entry)

    lines = [
        f"### {entry.title}",
        "",
        "Bibliographic:",
        bullet("year", year),
        bullet("venue", venue),
        bullet("doi", doi),
        "",
        "Paper type:",
        bullet("type", paper_type),
        "",
        "Evidence fields:",
        bullet("signal_modality", signal_modality),
        bullet("input_modality", input_modality),
        bullet("task_taxonomy", task_taxonomy),
        bullet("paper_objective", paper_objective),
        bullet("method_family", method_family),
        bullet("method_summary", method_summary),
        bullet("dataset", dataset),
        bullet("dataset_role", dataset_role),
        bullet("metric", metric),
        bullet("metric_status", metric_status),
        bullet("limitations", limitations),
        bullet("limitation_source", limitation_source),
        "",
        "Verification:",
        bullet("final_unresolved_fields", ", ".join(unresolved) if unresolved else "none"),
        bullet("verification_status", status),
        bullet("evidence_sources", "; ".join(source_list)),
        bullet("evidence_tier", evidence_tier(entry)),
        bullet("confidence", confidence(entry, unresolved)),
    ]

    evidence_lines: list[str] = []
    for field_name in sorted(set(entry.agent_evidence) | set(entry.agent_confidence)):
        details = []
        if entry.agent_evidence.get(field_name):
            details.append(f"evidence={entry.agent_evidence[field_name]}")
        if entry.agent_confidence.get(field_name):
            details.append(f"confidence={entry.agent_confidence[field_name]}")
        if entry.agent_source_tier.get(field_name):
            details.append(f"tier={entry.agent_source_tier[field_name]}")
        if details:
            evidence_lines.append(f"- {field_name}: " + " | ".join(details))
    if evidence_lines:
        lines.extend(["", "Field evidence:"])
        lines.extend(evidence_lines)
    if entry.auto_status or entry.auto_matched_title:
        lines.extend(["", "Identity trace:"])
        if entry.auto_status:
            lines.append(bullet("auto_verification_status", entry.auto_status))
        if entry.auto_matched_title:
            lines.append(bullet("auto_matched_title", entry.auto_matched_title))
        if entry.auto_source_url:
            lines.append(bullet("auto_source_url", entry.auto_source_url))
    lines.append("")
    return lines, unresolved


def build_document(entries: list[Entry]) -> str:
    rendered: list[tuple[list[str], list[str]]] = [render_entry(entry) for entry in entries]
    unresolved_counts = Counter(field for _, unresolved in rendered for field in unresolved)
    type_counts = Counter(infer_paper_type(entry) for entry in entries)
    lines = [
        "# Manual Review Needed",
        "",
        "Schema version: structured-manual-review-v1",
        "",
        "This report uses the structured Paper-RAG++ review schema. It separates bibliographic facts, paper type, evidence fields, and final verification state so review/perspective papers can be closed with explicit `not_applicable` statuses instead of ambiguous unresolved fields.",
        "",
        "## Summary",
        "",
        f"- entries: {len(entries)}",
        f"- entries with final unresolved fields: {sum(1 for _, unresolved in rendered if unresolved)}",
    ]
    if unresolved_counts:
        for field_name, count in sorted(unresolved_counts.items()):
            lines.append(f"- unresolved {field_name}: {count}")
    else:
        lines.append("- unresolved fields: none")
    lines.append("- paper types: " + ", ".join(f"{key}={value}" for key, value in sorted(type_counts.items())))
    lines.extend(
        [
            "",
            "## Schema",
            "",
            "Bibliographic: year, venue, doi.",
            "Paper type: primary_research | review | perspective | theory | benchmark | dataset | system.",
            "Evidence fields: signal_modality, input_modality, task_taxonomy, paper_objective, method_family, method_summary, dataset, dataset_role, metric, metric_status, limitations, limitation_source.",
            "Verification: final_unresolved_fields, verification_status, evidence_sources, evidence_tier, confidence.",
            "",
            "## Priority Entries",
            "",
        ]
    )
    for entry_lines, _ in rendered:
        lines.extend(entry_lines)
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manual-review", type=Path, default=DEFAULT_MANUAL_REVIEW)
    parser.add_argument("--output", type=Path, default=DEFAULT_MANUAL_REVIEW)
    args = parser.parse_args()
    _, entries = parse_manual_review(args.manual_review)
    args.output.write_text(build_document(entries), encoding="utf-8")
    print(f"Structured entries written: {len(entries)} -> {args.output}")


if __name__ == "__main__":
    main()
