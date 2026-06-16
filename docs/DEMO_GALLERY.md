# Demo Gallery

This gallery shows the behavior NeuroFlow should produce in common research sessions. Each demo is intentionally compact: the goal is to make the workflow value visible before users read the full skill library.

## EEG Reconstruction Baseline Gap

User asks:

```text
My EEG reconstruction result is worse than the baseline. What should I check next?
```

Naive agent likely does:

- Suggest a bigger model, longer training, or more augmentation.
- Ignore split protocol, metric parity, output routing, and checkpoint selection.

NeuroFlow route:

```text
neuro-orchestrator -> benchmark-to-baseline or experiment-to-paper -> experiment-copilot -> ai-bci-research guardrails
```

Evidence gates:

- Same subject/session/stimulus split across baseline and proposed method.
- Same preprocessing, normalization, metric, evaluator, and checkpoint selection.
- No train/test leakage through repeated stimuli, adjacent windows, or cached targets.
- Baseline reproduced before model-capacity changes.

Final artifact:

```markdown
Likely failure point:
First inspection:
Expected evidence:
Decision after check:
Memory candidate:
```

Why this prevents a research error:

It keeps the agent from treating a protocol or evaluator bug as a modeling problem.

## Benchmark Leakage Audit

User asks:

```text
Is this EEG benchmark fair for claiming cross-subject visual reconstruction?
```

Naive agent likely does:

- List dataset popularity and reported metrics.
- Miss whether the split actually supports cross-subject claims.

NeuroFlow route:

```text
neuro-orchestrator -> benchmark-to-baseline -> eeg-benchmark-hunter -> reviewer-simulator
```

Evidence gates:

- Access route, license, and human-subject restrictions.
- Subject, session, stimulus, repetition, and temporal split structure.
- Standard baselines and whether they use identical preprocessing and metrics.
- Claim boundary: cross-subject, cross-session, within-subject, or stimulus reconstruction.

Final artifact:

```markdown
Benchmark:
Verification status:
Split protocol:
Known baselines:
Leakage risks:
Use for:
Do not use for:
Reviewer risk:
```

Why this prevents a research error:

It stops the paper from making a generalization claim that the benchmark cannot support.

## Experiment Results to Paper Claim

User asks:

```text
Help me turn these experiment results into a paper claim.
```

Naive agent likely does:

- Polish the sentence first.
- Use broad words such as robust, general, or significant without checking evidence.

NeuroFlow route:

```text
neuro-orchestrator -> experiment-to-paper -> experiment-copilot -> oral-writer -> reviewer-simulator
```

Evidence gates:

- Claim maps to named table, figure, metric, baseline, split, and uncertainty.
- Ablations support the claimed mechanism.
- Reviewer risk is checked before final wording.

Final artifact:

```markdown
Original claim:
Evidence available:
Unsupported parts:
Safer claim:
Missing evidence:
Reviewer risk:
```

Why this prevents a research error:

It prevents polished prose from outrunning the actual experiment evidence.

## Paper-to-Repro Contract

User asks:

```text
Make this repository reproducible enough for a baseline table.
```

Naive agent likely does:

- Start refactoring before defining the minimal runnable path.
- Miss missing weights, gated data, or expected outputs.

NeuroFlow route:

```text
neuro-orchestrator -> paper-to-repro -> repro-pack -> eeg-benchmark-hunter -> experiment-copilot
```

Evidence gates:

- Environment, data, weights, commands, expected output, and smoke test.
- Data access and license status.
- Baseline protocol and table fields.

Final artifact:

```markdown
Environment:
Data:
Weights:
Command:
Expected output:
Smoke test:
Failure recovery:
Baseline table fields:
```

Why this prevents a research error:

It makes reproducibility concrete before adding new experiments or claims.

## Session-to-Memory

User asks:

```text
This debugging pattern came up again. Make it reusable.
```

Naive agent likely does:

- Save a long transcript or vague note.
- Mix private results with public workflow memory.

NeuroFlow route:

```text
neuro-orchestrator -> session-to-memory -> neuro-memory -> ai-bci-research index update
```

Evidence gates:

- Reusable behavior-changing lesson.
- Privacy filter for raw logs, unpublished results, credentials, and human-subject details.
- Target file and future eval prompt.

Final artifact:

```markdown
Memory type:
Reusable lesson:
Target file:
Privacy risk:
Suggested eval:
```

Why this prevents a research error:

It turns one useful session into a future first-read rule without leaking sensitive context.
