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

`ai-bci-research` provides shared domain guardrails and public memory. It is not the default workflow router.

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
