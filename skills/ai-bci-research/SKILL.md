---
name: ai-bci-research
description: Shared AI x BCI guardrail and public memory skill for NeuroFlow-Agent. Use for neural decoding, reconstruction, brain-language alignment, closed-loop BCI, leakage checks, safety cautions, and domain assumptions. Do not use as the default workflow router; start multi-step workflows with neuro-orchestrator.
---

# AI x BCI Research

Use this skill as the shared AI x BCI guardrail and public memory layer for NeuroFlow-Agent. Treat the user as the domain expert and use the bundled references as public workflow memory. If a local private overlay exists outside version control, use it only when the user explicitly asks for personalized project memory.

For any multi-step workflow, route through `neuro-orchestrator` first. This skill should support the pipeline with domain validity checks, not replace the orchestrator.

## First Reads

Read only the files needed for the task:

- `references/research-profile.md`: Always read first for public mission, scope, and non-negotiable assumptions.
- `references/papers-index.md`: Read for public paper-positioning templates, citation discipline, baselines, novelty framing, or literature-to-project mapping.
- `references/repositories.md`: Read for public repo-memory templates, repo-aware edits, dataset setup, or implementation planning.
- `references/bci-workflows.md`: Read for experiment design, neural signal processing, decoding, reconstruction, and closed-loop BCI tasks.
- `references/writing-style.md`: Read for abstracts, introductions, related work, rebuttals, figure captions, and reviewer-facing edits.
- `references/venue-workflows.md`: Read for conference submissions, venue targeting, camera-ready preparation, checklists, and rebuttals.
- `references/reviewer-objections.md`: Read for pre-review, response-to-reviewer drafts, rebuttals, and paper risk audits.
- `references/experiment-log-template.md`: Read when planning, recording, comparing, or debugging experiments.
- `references/experiment-findings.md`: Read when interpreting completed experiment batches, comparing model families, preserving diagnostic conclusions, or deciding the next ablation after surprising results.
- `references/debugging-playbooks.md`: Read when an experiment result is suspicious, a generative model underperforms a regression baseline, metrics collapse, generated neural signals have wrong scale, or code/protocol bugs are suspected.
- `references/workflows/skill-factory.md`: Read when a session should produce durable skill memory or the user asks for self-evolving workflow behavior.
- `references/playbooks/session-memory-consolidation.md`: Read when a completed session contains a reusable failure mode, check order, first-read rule, or reviewer-facing criterion.
- `references/cases/demo-case-template.md`: Read before adding a public demo case from a real session.
- `references/update-protocol.md`: Read when the user adds a new paper, repo, dataset, or experimental note.

## Operating Rules

- If the user asks for a broad workflow, paper plan, benchmark plan, reproduction plan, experiment matrix, review, writing, or memory consolidation, hand off to `neuro-orchestrator` and provide AI x BCI guardrails as supporting context.
- Ground claims in public references, user-supplied papers, repositories, or explicitly inspected files. If evidence is missing, say what is uncertain.
- Do not invent results, citations, datasets, ablations, subject counts, sampling rates, or statistical significance.
- Separate `established from user's work`, `inferred from context`, and `speculative next step` when proposing ideas.
- Before editing code, inspect the target repository structure and reuse local utilities, config conventions, and scripts.
- For paper text, preserve scientific caution: avoid inflated novelty claims, unsupported causal language, and over-broad "first" claims.
- For BCI evaluations, check subject-wise/session-wise leakage, train/test image overlap, stimulus leakage, model-selection leakage, and metric validity.
- For closed-loop or human-subject work, surface safety, IRB/ethics, calibration, latency, and online/offline mismatch concerns.

## Task Workflows

### Code Reproduction

1. Read `references/repositories.md`.
2. Inspect the local repo if available; otherwise use the public repository URL only as a pointer and avoid assuming unseen implementation details.
3. Identify environment setup, data paths, pretrained weights, run scripts, expected outputs, and evaluation metrics.
4. Produce a minimal runnable path before broad refactors.
5. Add or update focused README/run notes only when they reduce repeated setup ambiguity.

### Experiment Design

1. Read `references/research-profile.md` and `references/bci-workflows.md`.
2. Specify signal modality, task paradigm, stimulus space, participants, acquisition setup, synchronization, preprocessing, model, baselines, metrics, and statistics.
3. Explicitly define whether the experiment is decoding, encoding, reconstruction, alignment, closed-loop modulation, or bidirectional interaction.
4. Include leakage checks and failure modes before suggesting model complexity.

### Paper Writing

1. Read `references/papers-index.md` and `references/writing-style.md`.
2. If a venue, deadline, rebuttal, camera-ready, or submission checklist is involved, also read `references/venue-workflows.md`.
3. Position the work relative to the inspected project trajectory; if no private trajectory is provided, use the public AI x BCI progression: neural embeddings -> multimodal alignment -> reconstruction/generation -> closed-loop interaction.
4. Keep method descriptions reproducible and reviewer-facing.
5. Flag missing baselines, missing ablations, weak claims, or unsupported conclusions.

### Review and Rebuttal

1. Read `references/reviewer-objections.md`, `references/venue-workflows.md`, and the relevant paper/project references.
2. Separate factual errors, missing evidence, weak comparisons, unclear writing, and valid limitations.
3. Lead with blocking issues: leakage, baselines, claim scope, reconstruction metrics, online/offline validity, and reproducibility.
4. Draft reviewer responses that answer directly, cite concrete evidence, and narrow claims when evidence is missing.


### Experiment Debugging

1. Read `references/debugging-playbooks.md` and the relevant workflow reference.
2. Stop expensive training or sampling jobs before continuing if the run appears broken.
3. Treat large performance gaps, collapsed metrics, implausible signal scale, or unexpectedly low loss as possible protocol bugs before model limitations.
4. Check data normalization, train/test alignment, checkpoint selection, sampling/evaluation consistency, metric definitions, and baseline parity.
5. Propose the smallest code or numeric probe that can confirm or falsify each suspected root cause.

### Experiment Logging

1. Read `references/experiment-log-template.md` and `references/bci-workflows.md`.
2. Record dataset version, split protocol, seed, model checkpoint, hyperparameters, metrics, command, environment, and output path.
3. Treat surprising results as bugs until leakage, preprocessing, checkpoint selection, and metric definitions are checked.
4. Link each experiment to the paper claim, figure, table, or reviewer concern it supports.

### Skill Memory Consolidation

1. Read `references/workflows/skill-factory.md` and `references/update-protocol.md`.
2. Ask or answer the five compression questions: reusable check order, failure pattern, next first-read file, non-skippable criteria, and memory type.
3. Emit a `Memory candidate` block for meaningful research sessions.
4. Route public durable memory into `references/workflows/`, `references/playbooks/`, `references/cases/`, `references/experiment-findings.md`, or `evals/evals.json`.
5. Route private or sensitive details into ignored private memory, not public files.
6. Rebuild `references/knowledge-index.md` and validate after memory patches.

### Research Ideation

1. Start from the public mission in `references/research-profile.md` and any user-provided private context.
2. Propose ideas that connect MLLMs, generative models, brain-inspired intelligence, bidirectional BCI, Physical AI, and NeuroAI.
3. For each idea, include: hypothesis, technical route, required data, expected metric, strongest baseline, key risk, and fastest validation experiment.

## Useful Scripts

- `scripts/update_knowledge_index.py`: summarize local reference files into a compact index after adding new papers/repos/notes.
- `scripts/repo_inventory.py`: generate a lightweight inventory for a local code repository without reading large binary/data files.
