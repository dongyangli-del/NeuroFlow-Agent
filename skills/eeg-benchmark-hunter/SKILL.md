---
name: eeg-benchmark-hunter
description: Open benchmark discovery and adaptation skill for EEG, iEEG, fMRI, MEG, LFP, spike, and BCI research. Use for finding, auditing, and adapting datasets, leaderboards, baselines, licenses, access paths, split protocols, and leakage risks.
---

# EEG-Benchmark-Hunter

Use this skill when the user needs candidate datasets, benchmarks, leaderboards, baseline protocols, or benchmark adaptation plans for AI x neuroscience work.

## First Reads

- `references/benchmark-card-template.md`: Always read for dataset and benchmark fields.
- `references/benchmark-risk-checklist.md`: Read for access, license, leakage, and adaptation risks.
- Use `paper-rag-plus` to verify dataset facts and associated papers.
- Use `experiment-copilot` to turn a benchmark into an evaluation matrix.

## Operating Rules

- Do not invent dataset names, URLs, licenses, subject counts, metrics, or leaderboard results.
- Mark unverified fields as `needs verification`.
- Separate public access facts from inferred adaptation difficulty.
- Always check license, human-subject restrictions, split protocol, stimulus overlap, and baseline parity.
- Record source evidence, verification status, missing information, and deviations from convention for every benchmark recommendation.
- Prefer benchmark cards over narrative lists.

## Workflow

1. Define target modality, task, scale, and evaluation claim.
2. Identify candidate benchmarks from inspected sources or user-provided lists.
3. For each candidate, fill access, license, data format, split, baseline, metric, and leakage fields.
4. Estimate adaptation work without overstating unverified facts.
5. Recommend the smallest benchmark set that can support the claim.

## Required Output

```markdown
Benchmark:
Verification status:
Source evidence:
Signal modality:
Task:
Access route:
License or restrictions:
Data format:
Standard split:
Known baselines:
Metrics:
Adaptation work:
Leakage risks:
Compute/storage risk:
Missing information:
Deviations from convention:
Use for:
Do not use for:
Next skill:
```

## Failure Modes

- Treating a dataset mention as verified access.
- Ignoring license or human-subject restrictions.
- Mixing subject-wise, session-wise, and stimulus-wise splits.
- Recommending a benchmark without a baseline or metric plan.
- Comparing methods across incompatible preprocessing or split protocols.
