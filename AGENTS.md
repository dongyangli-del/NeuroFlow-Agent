# AGENTS

This repository uses NeuroFlow as the default research workflow layer for Codex.

## Default Entry

For any non-trivial AI x BCI, NeuroAI, EEG decoding, neural reconstruction, benchmark, reproduction, experiment, paper writing, review, rebuttal, or research-memory task in this repository:

1. Start with `neuro-orchestrator`.
2. Do not wait for the user to mention workflow, plan, routing, or skills.
3. First classify task depth: shallow, standard, deep, or persistent.
4. Choose the smallest NeuroFlow pipeline chain that can satisfy the request.
5. Name the primary artifact and evidence gates before detailed work.
6. Use specialist skills only as optional modules selected by `neuro-orchestrator`.
7. For simple implementation, shell, or documentation tasks, keep the NeuroFlow preflight internal and concise.
8. For commit, push, branch deletion, or remote synchronization tasks, apply the git publish safety gate: confirm the target branch, fetch remote state, verify ancestry, and do not leave temporary branches unless the user asked for them.
9. For workflow or skill evolution, record structured feedback, generate the smallest candidate patch plus an incident eval, compare it with the parent on protected and held-out cases, and retain a rollback path.
10. Never let a candidate modify protected evals, inspect hidden holdout prompts, self-approve public memory, or automatically promote skill, routing, pipeline, or code changes.
11. Never bind a long-running training, evaluation, transfer, render, or benchmark job to the Codex/IDE PTY. Launch it under `tmux`, `nohup` plus `setsid`, or `systemd-run`; persist its log and PID/session plus a completion marker; verify that it has an independent ownership tree; and use Codex only for short, read-only monitoring. Follow `skills-codex/neuro-orchestrator/references/long-running-task-execution.md`.

`ai-bci-research` provides shared domain guardrails and public memory. It is not the default workflow router.

## Evolution Runtime

The semi-automatic control plane is documented in `docs/EVOLUTION.md`. Its default mode is `shadow`. Low-risk automatic promotion requires an explicit `NEUROFLOW_EVOLUTION_MODE=semi-auto`; all high-risk changes require human approval. Promotion never commits or pushes.

## Preflight Behavior

Run this internal preflight before acting:

```markdown
Task type:
Task depth:
Pipeline chain:
Primary artifact:
Evidence gates:
Git publish safety:
Optional specialist modules:
Stop condition:
Memory candidate:
```

Expose the full preflight only when the user asks for a plan, the task is deep or persistent, the work spans multiple stages, or a handoff would be ambiguous. For shallow and standard tasks, proceed directly and mention only the selected route when it helps the user.

## Documentation

`AGENT_GUIDE.md` is explanatory documentation for the NeuroFlow workflow. This `AGENTS.md` file is the repository-level operating rule that agents should follow first.
