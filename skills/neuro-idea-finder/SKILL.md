---
name: neuro-idea-finder
description: AI x neuroscience and BCI research ideation skill. Use for generating EEG, iEEG, fMRI, MEG, LFP, spike, NeuroAI, and BCI research ideas with hypotheses, technical routes, data needs, baselines, metrics, risks, and fastest validation experiments.
---

# Neuro-Idea-Finder

Use this skill when the user asks for new research ideas, hypotheses, project directions, ablation concepts, or grant/paper angles in AI x neuroscience and BCI.

## First Reads

- `references/idea-template.md`: Always read for required idea-card fields.
- `references/modality-opportunity-map.md`: Read to choose signal modality, task family, and opportunity axis.
- Use `ai-bci-research` for shared domain guardrails.
- Use `paper-rag-plus` before making novelty or closest-prior-work claims.
- Use `experiment-copilot` when an idea should become an experiment matrix.

## Operating Rules

- Separate speculative ideas from established facts.
- Do not claim novelty without literature grounding.
- Every idea must include data, baseline, metric, key risk, and fastest validation.
- Prefer ideas that can fail quickly over ideas that require a full system before any signal appears.
- Include leakage, subject/session generalization, modality alignment, and online/offline validity risks when relevant.

## Workflow

1. Identify the modality: EEG, iEEG, fMRI, MEG, LFP, spike, behavior, stimulus, or multimodal.
2. Identify the task class: decoding, reconstruction, alignment, generation, closed-loop adaptation, personalization, or world-modeling.
3. Generate candidate hypotheses across method, data, objective, evaluation, and interaction axes.
4. Filter each idea by feasibility, evidence path, baseline strength, and reviewer risk.
5. Promote only the best ideas into experiment-ready cards.

## Required Output

```markdown
Idea:
Hypothesis:
Why now:
Signal modality:
Task:
Technical route:
Required data:
Strongest baseline:
Primary metric:
Fastest validation experiment:
Key risk:
Reviewer objection:
Next skill:
Memory candidate:
```

## Failure Modes

- Producing broad themes instead of testable hypotheses.
- Claiming "first" or "novel" without `paper-rag-plus`.
- Omitting baselines, metrics, or validation data.
- Ignoring leakage or subject/session split concerns.
- Suggesting a deep full-system build before a cheap falsification probe.
