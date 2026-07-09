#!/usr/bin/env python3
"""Audit NeuroFlow skill routing physics.

This is a lightweight, dependency-free manager for the NeuroFlow skill surface.
It enforces routing boundaries, scores local competition, and can simulate the
risk of adding a candidate skill manifest before it enters the flat pool.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
DEFAULT_THRESHOLD = 0.68

STOPWORDS = {
    "and",
    "the",
    "for",
    "with",
    "when",
    "into",
    "from",
    "this",
    "that",
    "use",
    "uses",
    "using",
    "skill",
    "skills",
    "research",
    "workflow",
    "task",
    "tasks",
    "artifact",
    "artifacts",
    "evidence",
    "status",
    "verification",
    "source",
    "traced",
}
GENERIC_TERMS = {
    "analyze",
    "assist",
    "check",
    "create",
    "generate",
    "handle",
    "help",
    "manage",
    "process",
    "research",
    "review",
    "support",
    "workflow",
}
REQUIRED_BOUNDARY_FIELDS = ("do_not_use_when", "prefer_over", "defer_to", "competes_with")
REQUIRED_ANCHOR_FIELDS = ("verbs", "objects", "constraints")
DEPENDENCY_WEIGHTS = {"tight": 1.0, "loose": 0.45, "independent": 0.12}


@dataclass(slots=True)
class SkillProfile:
    name: str
    path: str
    purpose: str
    natural_triggers: list[str]
    anchors: dict[str, list[str]]
    routing_boundary: dict[str, bool]
    outputs: dict[str, str]


@dataclass(slots=True)
class PipelineEdge:
    upstream_skill: str
    downstream_skill: str
    dependency_type: str
    weight: float
    notes: str = ""


@dataclass(slots=True)
class PairScore:
    left_skill_id: str
    right_skill_id: str
    lexical_similarity: float
    anchor_overlap: float
    competition_risk: float
    weak_drag_risk: float
    merge_candidate_score: float
    shared_anchors: dict[str, list[str]]


@dataclass(slots=True)
class SkillScore:
    skill_id: str
    anchor_strength: float
    anchor_weakness: float
    abstraction_score: float
    top_neighbor_similarity: float
    competition_score: float
    black_hole_risk: float
    routing_fragility: float
    rewrite_priority: float


@dataclass(slots=True)
class LibraryScore:
    size: int
    competition_density: float
    danger_zone_mass: float
    anchor_weakness_mass: float
    predicted_routing_stability: float
    predicted_black_hole_exposure: float
    pipeline_fragility_index: float
    top_pairs: list[PairScore] = field(default_factory=list)
    fragile_skills: list[SkillScore] = field(default_factory=list)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def top_field(text: str, name: str) -> str:
    match = re.search(rf"^{re.escape(name)}:\s*(.*?)\s*$", text, re.MULTILINE)
    return match.group(1).strip().strip('"') if match else ""


def section_body(text: str, section: str) -> str:
    match = re.search(
        rf"^{re.escape(section)}:\n(?P<body>(?:[ \t]+.*\n?)*)",
        text,
        re.MULTILINE,
    )
    return match.group("body") if match else ""


def parse_block_list(text: str, section: str) -> list[str]:
    body = section_body(text, section)
    return [item.strip().strip('"') for item in re.findall(r"^\s+-\s+(.+?)\s*$", body, re.MULTILINE)]


def parse_inline_list(value: str) -> list[str]:
    value = value.strip()
    if not (value.startswith("[") and value.endswith("]")):
        return []
    raw = value[1:-1]
    return [item.strip().strip('"').strip("'") for item in raw.split(",") if item.strip()]


def parse_nested_lists(text: str, section: str) -> dict[str, list[str]]:
    body = section_body(text, section)
    result: dict[str, list[str]] = {}
    current_key = ""
    for line in body.splitlines():
        key_match = re.match(r"^\s{2}([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if key_match:
            current_key = key_match.group(1)
            inline = parse_inline_list(key_match.group(2))
            result[current_key] = inline
            continue
        item_match = re.match(r"^\s{4}-\s+(.+?)\s*$", line)
        if item_match and current_key:
            result.setdefault(current_key, []).append(item_match.group(1).strip().strip('"'))
    return result


def parse_outputs(text: str) -> dict[str, str]:
    body = section_body(text, "outputs")
    outputs: dict[str, str] = {}
    for line in body.splitlines():
        match = re.match(r"^\s{2}([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if match:
            outputs[match.group(1)] = match.group(2).strip()
    return outputs


def parse_routing_boundary(text: str) -> dict[str, bool]:
    body = section_body(text, "routing_boundary")
    return {field: f"  {field}:" in body for field in REQUIRED_BOUNDARY_FIELDS}


def parse_pipeline_edges(text: str) -> list[PipelineEdge]:
    body = section_body(text, "pipeline_edges")
    edges: list[PipelineEdge] = []
    current: dict[str, str] = {}
    for line in body.splitlines():
        first = re.match(r"^\s{2}-\s+([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if first:
            if current:
                edges.append(edge_from_mapping(current))
            current = {first.group(1): first.group(2).strip()}
            continue
        item = re.match(r"^\s{4}([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if item and current:
            current[item.group(1)] = item.group(2).strip()
    if current:
        edges.append(edge_from_mapping(current))
    return edges


def edge_from_mapping(mapping: dict[str, str]) -> PipelineEdge:
    try:
        weight = float(mapping.get("weight", "1.0"))
    except ValueError:
        weight = 1.0
    return PipelineEdge(
        upstream_skill=mapping.get("upstream_skill", ""),
        downstream_skill=mapping.get("downstream_skill", ""),
        dependency_type=mapping.get("dependency_type", ""),
        weight=weight,
        notes=mapping.get("notes", "").strip('"'),
    )


def load_skill(path: Path) -> SkillProfile:
    text = path.read_text(encoding="utf-8")
    try:
        display_path = str(path.resolve().relative_to(ROOT))
    except ValueError:
        display_path = str(path)
    return SkillProfile(
        name=top_field(text, "name") or path.parent.name,
        path=display_path,
        purpose=top_field(text, "purpose"),
        natural_triggers=parse_block_list(text, "natural_triggers"),
        anchors=parse_nested_lists(text, "anchors"),
        routing_boundary=parse_routing_boundary(text),
        outputs=parse_outputs(text),
    )


def load_library(candidate: Path | None = None) -> tuple[list[SkillProfile], list[PipelineEdge]]:
    manifests = sorted(SKILLS_DIR.glob("*/manifest.yaml"))
    skills = [load_skill(path) for path in manifests]
    edges: list[PipelineEdge] = []
    for path in manifests:
        edges.extend(parse_pipeline_edges(path.read_text(encoding="utf-8")))
    if candidate:
        skills.append(load_skill(candidate))
    return skills, edges


def tokenize(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{2,}", text.lower())
        if token not in STOPWORDS
    }


def skill_surface(skill: SkillProfile) -> str:
    parts = [skill.name, skill.purpose, " ".join(skill.natural_triggers)]
    for field in REQUIRED_ANCHOR_FIELDS:
        parts.extend(skill.anchors.get(field, []))
    return " ".join(parts)


def lexical_similarity(left: SkillProfile, right: SkillProfile) -> float:
    left_tokens = tokenize(skill_surface(left))
    right_tokens = tokenize(skill_surface(right))
    union = left_tokens | right_tokens
    if not union:
        return 0.0
    return len(left_tokens & right_tokens) / len(union)


def anchor_strength(skill: SkillProfile) -> float:
    verbs = len(skill.anchors.get("verbs", []))
    objects = len(skill.anchors.get("objects", []))
    constraints = len(skill.anchors.get("constraints", []))
    score = 0.12 * min(verbs, 4) + 0.15 * min(objects, 4) + 0.10 * min(constraints, 4)
    if skill.outputs:
        score += 0.12
    return min(1.0, score)


def abstraction_score(skill: SkillProfile) -> float:
    tokens = tokenize(skill.purpose)
    if not tokens:
        return 1.0
    generic_hits = len(tokens & GENERIC_TERMS) / max(1, len(tokens))
    anchor_penalty = 1.0 - anchor_strength(skill)
    broad_trigger_penalty = 0.15 if any(len(tokenize(trigger)) <= 3 for trigger in skill.natural_triggers) else 0.0
    return min(1.0, 0.55 * generic_hits + 0.35 * anchor_penalty + broad_trigger_penalty)


def pair_scores(skills: list[SkillProfile]) -> list[PairScore]:
    scores: list[PairScore] = []
    for index, left in enumerate(skills):
        for right in skills[index + 1 :]:
            similarity = lexical_similarity(left, right)
            shared: dict[str, list[str]] = {}
            shared_count = 0
            for field_name in REQUIRED_ANCHOR_FIELDS:
                overlap = sorted(set(left.anchors.get(field_name, [])) & set(right.anchors.get(field_name, [])))
                if overlap:
                    shared[field_name] = overlap
                    shared_count += len(overlap)
            anchor_overlap = min(1.0, 0.18 * shared_count)
            risk = min(1.0, 0.72 * similarity + 0.28 * anchor_overlap)
            weak_drag = min(1.0, 0.60 * similarity + 0.25 * anchor_overlap)
            merge_score = min(1.0, risk + (0.10 if anchor_overlap >= 0.36 else 0.0))
            scores.append(
                PairScore(
                    left_skill_id=left.name,
                    right_skill_id=right.name,
                    lexical_similarity=round(similarity, 3),
                    anchor_overlap=round(anchor_overlap, 3),
                    competition_risk=round(risk, 3),
                    weak_drag_risk=round(weak_drag, 3),
                    merge_candidate_score=round(merge_score, 3),
                    shared_anchors=shared,
                )
            )
    return sorted(scores, key=lambda card: (card.competition_risk, card.lexical_similarity), reverse=True)


def skill_scores(skills: list[SkillProfile], pairs: list[PairScore]) -> list[SkillScore]:
    by_skill: dict[str, list[PairScore]] = {skill.name: [] for skill in skills}
    for pair in pairs:
        by_skill.setdefault(pair.left_skill_id, []).append(pair)
        by_skill.setdefault(pair.right_skill_id, []).append(pair)
    profiles = {skill.name: skill for skill in skills}
    result: list[SkillScore] = []
    for name, skill in profiles.items():
        neighbors = by_skill.get(name, [])
        top_similarity = max((pair.lexical_similarity for pair in neighbors), default=0.0)
        competition = max((pair.competition_risk for pair in neighbors), default=0.0)
        strength = anchor_strength(skill)
        weakness = 1.0 - strength
        abstraction = abstraction_score(skill)
        black_hole = min(1.0, 0.35 * competition + 0.35 * weakness + 0.30 * abstraction)
        fragility = min(1.0, 0.45 * competition + 0.35 * weakness + 0.20 * abstraction)
        rewrite = min(1.0, 0.50 * black_hole + 0.25 * top_similarity + 0.25 * weakness)
        result.append(
            SkillScore(
                skill_id=name,
                anchor_strength=round(strength, 3),
                anchor_weakness=round(weakness, 3),
                abstraction_score=round(abstraction, 3),
                top_neighbor_similarity=round(top_similarity, 3),
                competition_score=round(competition, 3),
                black_hole_risk=round(black_hole, 3),
                routing_fragility=round(fragility, 3),
                rewrite_priority=round(rewrite, 3),
            )
        )
    return sorted(result, key=lambda card: card.rewrite_priority, reverse=True)


def pipeline_fragility(edges: list[PipelineEdge], skill_cards: list[SkillScore]) -> float:
    if not edges:
        return 0.0
    by_skill = {card.skill_id: card for card in skill_cards}
    total = 0.0
    valid_edges = 0
    for edge in edges:
        weight = DEPENDENCY_WEIGHTS.get(edge.dependency_type, 0.3) * edge.weight
        upstream = by_skill.get(edge.upstream_skill)
        downstream = by_skill.get(edge.downstream_skill)
        if upstream and downstream:
            weight *= 0.5 + 0.5 * max(upstream.routing_fragility, downstream.routing_fragility)
        total += weight
        valid_edges += 1
    return round(min(1.0, total / max(1, valid_edges)), 3)


def build_library_score(skills: list[SkillProfile], edges: list[PipelineEdge]) -> tuple[LibraryScore, list[PairScore], list[SkillScore]]:
    pairs = pair_scores(skills)
    skill_cards = skill_scores(skills, pairs)
    density = sum(pair.competition_risk for pair in pairs) / len(pairs) if pairs else 0.0
    danger_cards = [card.competition_score for card in skill_cards if 0.45 <= card.competition_score <= 0.80]
    danger = sum(danger_cards) / len(danger_cards) if danger_cards else 0.0
    weakness = sum(card.anchor_weakness for card in skill_cards) / len(skill_cards) if skill_cards else 0.0
    black_hole = sum(card.black_hole_risk for card in skill_cards) / len(skill_cards) if skill_cards else 0.0
    size_accuracy = max(0.0, 0.834 - 0.042 * math.log(max(1, len(skills))))
    stability = max(0.0, min(1.0, size_accuracy - 0.22 * density - 0.18 * weakness))
    library = LibraryScore(
        size=len(skills),
        competition_density=round(density, 3),
        danger_zone_mass=round(danger, 3),
        anchor_weakness_mass=round(weakness, 3),
        predicted_routing_stability=round(stability, 3),
        predicted_black_hole_exposure=round(black_hole, 3),
        pipeline_fragility_index=pipeline_fragility(edges, skill_cards),
        top_pairs=pairs[:8],
        fragile_skills=skill_cards[:8],
    )
    return library, pairs, skill_cards


def validate_schema(skills: list[SkillProfile], edges: list[PipelineEdge], *, candidate: Path | None) -> list[str]:
    errors: list[str] = []
    for skill in skills:
        for field_name, present in skill.routing_boundary.items():
            if not present:
                errors.append(f"{skill.path} missing routing_boundary.{field_name}")
        for field_name in REQUIRED_BOUNDARY_FIELDS:
            if field_name not in skill.routing_boundary:
                errors.append(f"{skill.path} missing routing_boundary.{field_name}")
        for field_name in REQUIRED_ANCHOR_FIELDS:
            if not skill.anchors.get(field_name):
                errors.append(f"{skill.path} missing anchors.{field_name}")
        if not skill.outputs.get("primary"):
            errors.append(f"{skill.path} missing outputs.primary")

    skill_names = {skill.name for skill in skills}
    if not candidate:
        if not edges:
            errors.append("No pipeline_edges found in manifests")
        for edge in edges:
            if edge.upstream_skill not in skill_names:
                errors.append(f"pipeline edge has unknown upstream_skill: {edge.upstream_skill}")
            if edge.downstream_skill not in skill_names:
                errors.append(f"pipeline edge has unknown downstream_skill: {edge.downstream_skill}")
            if edge.dependency_type not in DEPENDENCY_WEIGHTS:
                errors.append(f"pipeline edge has invalid dependency_type: {edge.dependency_type}")
            if not (0.0 < edge.weight <= 1.0):
                errors.append(f"pipeline edge has invalid weight: {edge.weight}")
    return errors


def payload_dict(library: LibraryScore, pairs: list[PairScore], skill_cards: list[SkillScore], edges: list[PipelineEdge]) -> dict[str, Any]:
    return {
        "report_type": "neuroflow_skill_competition_scorecard",
        "library_scorecard": asdict(library),
        "pair_scorecards": [asdict(pair) for pair in pairs],
        "skill_scorecards": [asdict(card) for card in skill_cards],
        "pipeline_edges": [asdict(edge) for edge in edges],
    }


def print_summary(library: LibraryScore, *, candidate: Path | None) -> None:
    mode = "candidate simulation" if candidate else "library audit"
    print(f"Skill competition {mode} passed.")
    print(
        "Library scorecard: "
        f"size={library.size}, "
        f"competition_density={library.competition_density:.3f}, "
        f"anchor_weakness_mass={library.anchor_weakness_mass:.3f}, "
        f"routing_stability={library.predicted_routing_stability:.3f}, "
        f"pipeline_fragility={library.pipeline_fragility_index:.3f}"
    )
    if library.top_pairs:
        print("Top competition pairs:")
        for pair in library.top_pairs[:5]:
            print(
                f"- {pair.left_skill_id} <-> {pair.right_skill_id}: "
                f"risk={pair.competition_risk:.3f}, lexical={pair.lexical_similarity:.3f}, anchors={pair.anchor_overlap:.3f}"
            )
    if library.fragile_skills:
        print("Highest rewrite priorities:")
        for card in library.fragile_skills[:5]:
            print(
                f"- {card.skill_id}: rewrite={card.rewrite_priority:.3f}, "
                f"black_hole={card.black_hole_risk:.3f}, anchor_strength={card.anchor_strength:.3f}"
            )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, help="Candidate manifest to simulate before adding")
    parser.add_argument("--json", action="store_true", help="Emit full JSON scorecard")
    parser.add_argument("--report", type=Path, help="Write full JSON scorecard to a file")
    parser.add_argument("--max-candidate-risk", type=float, default=DEFAULT_THRESHOLD)
    args = parser.parse_args()

    if args.candidate and not args.candidate.exists():
        fail(f"Candidate manifest not found: {args.candidate}")

    skills, edges = load_library(args.candidate)
    errors = validate_schema(skills, edges, candidate=args.candidate)
    if errors:
        fail("Skill competition audit failed:\n- " + "\n- ".join(errors))

    library, pairs, skill_cards = build_library_score(skills, edges)
    payload = payload_dict(library, pairs, skill_cards, edges)

    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.candidate:
        candidate_name = load_skill(args.candidate).name
        candidate_pairs = [
            pair for pair in pairs if candidate_name in {pair.left_skill_id, pair.right_skill_id}
        ]
        top_risk = max((pair.competition_risk for pair in candidate_pairs), default=0.0)
        if top_risk > args.max_candidate_risk:
            fail(
                f"Candidate {candidate_name} exceeds max competition risk "
                f"{args.max_candidate_risk:.2f}: observed {top_risk:.2f}"
            )

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_summary(library, candidate=args.candidate)


if __name__ == "__main__":
    main()
