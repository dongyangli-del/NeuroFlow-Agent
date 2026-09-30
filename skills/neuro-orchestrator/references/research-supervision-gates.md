# Research Supervision Gates

This reference distills advisor-style research supervision into NeuroFlow's AI x brain workflow language. It is an original NeuroFlow abstraction inspired by the public Supervisor-Skills project:

- Source: https://github.com/HKUSTDial/Supervisor-Skills
- License note: Supervisor-Skills is CC BY-NC-SA 4.0. Do not copy its text, templates, examples, or handbook passages into this MIT-licensed repository. Use this file as a license-safe abstraction of reusable supervision principles.

## Gate 1: Idea Commitment

Use before investing implementation time, data construction time, or paper-writing time.

An idea should not proceed until it has:

- a falsifiable hypothesis;
- a clear task mode: encoding, decoding, analysis, representation, modulation, or embodied interaction;
- a realistic data path and split protocol;
- a strongest baseline that could plausibly win;
- a cheap first experiment that can kill the idea;
- a reviewer objection that would block acceptance if unresolved;
- a capability fit check: whether current time, compute, data access, and technical depth are enough for the proposed claim.

Reject or pivot when the idea has no measurable failure condition, depends on unavailable data, requires a full system before any signal appears, or only sounds novel because the closest prior work has not been inspected.

## Gate 2: Paper Logic Chain

Use before drafting an abstract, introduction, method section, or figure narrative.

A submission-facing project needs a one-to-one logic chain:

```text
research setting
-> limitation in closest prior work
-> key principle or goal
-> concrete challenges
-> method modules or experimental design choices
-> evidence
-> contributions
```

Every link should be checkable:

- limitations point to specific missing capabilities or invalid assumptions;
- the key principle directly addresses those limitations;
- challenges arise from implementing the principle, not from a desire to justify extra modules;
- each method module or experiment answers one challenge;
- contributions map to method sections, figures, tables, or claims;
- the paper's thesis is narrower than the weakest evidence.

If this chain breaks, do not polish prose. Fix the project story, evidence plan, or claim scope first.

## Gate 3: Benchmark and Evaluation Substance

Use when proposing a new dataset, benchmark, evaluation suite, leaderboard, or baseline comparison.

A benchmark-style contribution must define the measurement, not only collect data. Require:

- evaluation gap: what existing benchmarks cannot diagnose;
- construction path: where examples, stimuli, labels, annotations, or tasks come from;
- quality control: how noise, ambiguity, artifacts, and leakage are detected;
- evaluation taxonomy: dimensions, difficulty tiers, error types, or behavioral/neural conditions;
- baseline suite: deterministic, neural, behavioral, and model-family baselines as appropriate;
- empirical findings: actionable capability boundaries, not only a ranking table;
- governance: access, license, human-subject, privacy, consent, and redistribution constraints.

For AI x brain work, also check stimulus overlap, subject/session splits, neural preprocessing parity, behavioral confounds, and whether benchmark difficulty reflects the intended cognitive or neural claim.

## Gate 4: Figure Narrative

Use before creating or revising paper figures.

Each main figure should have one job:

- motivated example: reveal the research problem, failure mode, or scientific opportunity;
- method overview: show the mechanism or workflow at the same abstraction level as the method section;
- experimental result: carry one finding with honest axes, uncertainty, and comparable baselines;
- analysis figure: explain behavior, neural representation, error taxonomy, or failure mode;
- closed-loop or embodied figure: separate offline training, online interaction, feedback, and safety boundaries.

Audit every figure for:

- a first-sentence caption takeaway;
- labels that match paper terminology;
- visible mapping from figure panels to claims;
- vector or high-resolution export;
- readable font after scaling;
- colorblind-safe encoding and no color-only semantics;
- no decorative complexity that hides the evidence.

## Gate 5: Pre-Submission Review

Use before submission, rebuttal, camera-ready, or public release.

Classify every issue by severity:

- **Blocking**: invalid split, leakage, missing baseline, unsupported main claim, fabricated or unverified citation, unavailable data required by the claim, online claim from offline evidence, privacy/IRB risk.
- **Major**: weak ablation, unclear metric, incomplete reproducibility, mismatched figure/story, vague contribution, overbroad novelty, missing limitation.
- **Minor**: wording, formatting, grammar, caption polish, citation style, small LaTeX issues.

Review across five dimensions:

1. logic chain and claim support;
2. experiment and benchmark validity;
3. figure and table evidence;
4. writing clarity and scoped claims;
5. reproducibility, ethics, safety, and data governance.

Do not let minor language polish hide blocking scientific issues.

## Gate 6: AI-Assisted Research Integrity

Use whenever AI tools help with coding, figures, writing, literature organization, or review.

AI may accelerate:

- code scaffolding, debugging, and test generation;
- figure drafting and plotting utilities;
- language polish and structure checks;
- literature organization and claim-to-citation bookkeeping;
- reviewer-risk simulation.

The researcher must own:

- research direction, novelty, and claim scope;
- experimental design, data provenance, and metrics;
- factual correctness, citations, and limitations;
- final interpretation of neural, behavioral, cognitive, or embodied results;
- venue-specific AI disclosure and collaboration norms.

Stop and repair the workflow if AI introduces unverified citations, invented results, hidden data transformations, untested code, private information leakage, or claims the user cannot defend.

## NeuroFlow Routing

Apply these gates by pipeline:

| Pipeline chain | Required supervision gates |
|---|---|
| idea-to-experiment | Idea Commitment, Paper Logic Chain, Pre-Submission Review if claims are drafted |
| paper-to-repro | Paper Logic Chain, Pre-Submission Review, AI-Assisted Research Integrity |
| benchmark-to-baseline | Benchmark and Evaluation Substance, Figure Narrative, Pre-Submission Review |
| continual-adaptation | Idea Commitment, Benchmark and Evaluation Substance, AI-Assisted Research Integrity |
| experiment-to-paper | Paper Logic Chain, Figure Narrative, Pre-Submission Review |
| paper-to-rebuttal | Paper Logic Chain, Pre-Submission Review |
| session-to-memory | AI-Assisted Research Integrity plus privacy review |
