# Changelog

All notable public-facing changes to NeuroFlow-Agent are recorded here.

This project uses date-based release notes until semantic versioned releases begin.

## Unreleased

- Added the semi-automatic evolution control plane:
  - trace schema v2 with versions, routes, stage outcomes, gates, cost, and failure tags;
  - executable regression, protected, incident, and hidden-holdout eval partitions;
  - SQLite/Alembic feedback, candidate, eval-run, and promotion lineage;
  - OpenAI-compatible, Anthropic, Ollama, and mock provider adapters;
  - risk classification, shadow comparison, independent review, canary promotion, and rollback;
  - pre-shadow approval for non-low-risk patches, patch integrity checks, exact-parent worktrees, disposable canaries, mandatory configured holdouts, and restricted executable assertions;
  - Typer CLI commands plus Markdown and HTML evolution reports.
- Added manifest coverage for every pipeline stage owner.

- Added public knowledge graph entry points:
  - `docs/KNOWLEDGE_GRAPH.md`
  - `docs/VERIFICATION_DASHBOARD.md`
  - `skills/paper-rag-plus/references/papers-index-summary.md`
- Added `neuroflow kb search` and `neuroflow kb summary` through `scripts/neuroflow_runtime/cli.py`.
- Added multi-platform installer:
  - `scripts/install --check`
  - `scripts/install --update`
  - `scripts/install --prune`
  - targets for Codex, Claude Code, Cursor, Gemini CLI, OpenCode, and generic `AGENTS.md`.
- Added integration templates under `integrations/`.
- Added cross-model review as a default gate for high-risk claim, citation, experiment, reproduction, and public-memory artifacts.
- Added git publish safety as a default gate for commit, push, branch deletion, and remote synchronization tasks.
- Added the Vec2Text paper readiness demo as a public-safe case study distilled from inspected paper, readiness, reproduction, and reviewer-risk artifacts.
- Added skill-physics safeguards inspired by Evolvent's skill-library routing analysis: routing boundaries, routeable anchors, primary output contracts, workflow dependency edges, scorecard-based competition audit, candidate-add simulation, and handoff anchors.

## 2026-06-30

- Refined README positioning around domain-knowledge-correct AutoResearch and human-in-the-loop research harnesses.
- Added the NeuroFlow framework main image.
- Added research-integrity workflow primitives:
  - claim ledger;
  - numeric self-consistency;
  - reproduction observability levels;
  - integrity forensics;
  - shared research-integrity gate.
- Added README and skill documentation for anti low-quality AutoResearch safeguards.

## 2026-06-29

- Added lightweight runtime registry and workflow hooks.
- Added source-traced paper-field verification workflow and cleaned resolved manual-review entries.
- Added writing and reviewer-simulation enhancements for submission-facing workflows.
