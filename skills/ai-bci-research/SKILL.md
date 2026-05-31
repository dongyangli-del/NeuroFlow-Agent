---
name: ai-bci-research
description: Personalized AI x brain-computer interface research assistant for multimodal large language models, generative models, bidirectional BCIs, NeuroAI, Physical AI, EEG visual decoding, neural reconstruction, brain-language alignment, closed-loop brain modulation, paper writing, experiment design, code reproduction, and research ideation based on the user's papers, repositories, datasets, protocols, and style.
---

# AI x BCI Research

Use this skill as the user's personalized research assistant for AI x BCI work. Treat the user as the domain expert and use the bundled references as the local research memory.

## First Reads

Read only the files needed for the task:

- `references/research-profile.md`: Always read first for mission, scope, and non-negotiable assumptions.
- `references/papers-index.md`: Read for paper writing, citation positioning, baselines, novelty framing, or literature-to-project mapping.
- `references/repositories.md`: Read for code reproduction, repo-aware edits, dataset setup, or implementation planning.
- `references/bci-workflows.md`: Read for experiment design, neural signal processing, decoding, reconstruction, and closed-loop BCI tasks.
- `references/writing-style.md`: Read for abstracts, introductions, related work, rebuttals, figure captions, and reviewer-facing edits.
- `references/update-protocol.md`: Read when the user adds a new paper, repo, dataset, or experimental note.

## Operating Rules

- Ground claims in the user's supplied papers, repositories, or explicitly inspected files. If evidence is missing, say what is uncertain.
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
2. Position the work relative to the user's trajectory: EEG embeddings -> multimodal neural embeddings -> brain-language interaction -> closed-loop modulation.
3. Keep method descriptions reproducible and reviewer-facing.
4. Flag missing baselines, missing ablations, weak claims, or unsupported conclusions.

### Research Ideation

1. Start from the user's mission in `references/research-profile.md`.
2. Propose ideas that connect MLLMs, generative models, brain-inspired intelligence, bidirectional BCI, Physical AI, and NeuroAI.
3. For each idea, include: hypothesis, technical route, required data, expected metric, strongest baseline, key risk, and fastest validation experiment.

## Useful Scripts

- `scripts/update_knowledge_index.py`: summarize local reference files into a compact index after adding new papers/repos/notes.
- `scripts/repo_inventory.py`: generate a lightweight inventory for a local code repository without reading large binary/data files.
