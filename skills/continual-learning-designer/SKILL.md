---
name: continual-learning-designer
description: Continual learning design skill for neural decoding and BCI personalization. Use for cross-subject, cross-session, cross-device, streaming calibration, catastrophic forgetting, replay, regularization, adapter, and test-time adaptation plans.
---

# Continual-Learning-Designer

Use this skill when the user needs a continual, adaptive, personalized, or online learning design for neural decoding or BCI systems.

## First Reads

- `references/continual-bci-design.md`: Always read for design fields.
- `references/evaluation-protocol.md`: Read for forgetting, transfer, calibration, and online/offline evaluation.
- Use `experiment-copilot` to convert the design into experiments.
- Use `reviewer-simulator` before making deployment or closed-loop claims.
- Use `ai-bci-research` for BCI validity and safety guardrails.

## Operating Rules

- Define stream order, adaptation signal, memory budget, and update frequency.
- Separate offline replay, simulated online, and true online human-subject claims.
- Include forgetting metrics, forward/backward transfer, calibration cost, and subject/session/device splits.
- Include baselines such as no-adaptation, fine-tuning, replay, regularization, adapters, or test-time adaptation when appropriate.
- Surface safety, latency, drift, and privacy risks for closed-loop or human-subject settings.

## Workflow

1. Define the deployment axis: subject, session, device, task, stimulus, or environment shift.
2. Define the stream: what arrives, when labels arrive, and what can be stored.
3. Choose adaptation mechanisms and baselines.
4. Define metrics for performance, forgetting, calibration, compute, latency, and safety.
5. Produce an experiment-ready design with reviewer risks.

## Required Output

```markdown
Adaptation goal:
Stream setting:
Available feedback:
Memory budget:
Update rule:
Baselines:
Metrics:
Forgetting checks:
Calibration protocol:
Online/offline boundary:
Safety and latency risks:
Experiment matrix handoff:
Reviewer objection:
Memory candidate:
```

## Failure Modes

- Calling offline fine-tuning an online BCI result.
- Omitting no-adaptation or simple fine-tuning baselines.
- Ignoring catastrophic forgetting or backward transfer.
- Using test data for adaptation without explicitly defining protocol.
- Missing safety, latency, privacy, or calibration constraints.
