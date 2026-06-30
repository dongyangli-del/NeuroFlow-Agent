<!-- neuroflow-managed -->
# NeuroFlow Workflow Command

Use this command when a research task needs NeuroFlow routing, evidence gates, or submission-facing checks.

Arguments: `$ARGUMENTS`

## Procedure

1. Treat the user request as a NeuroFlow task unless it is a trivial shell or formatting task.
2. Start from the NeuroFlow single-entry policy in `AGENTS.md` or the installed `neuro-orchestrator` skill.
3. Classify the task depth: shallow, standard, deep, or persistent.
4. Choose the smallest pipeline chain that satisfies the request.
5. Apply evidence gates before writing claims, paper text, citations, benchmark conclusions, or reproduction statements.
6. Use specialist modules only when their check order or output template is needed.
7. End with the requested artifact, unresolved evidence, and memory candidate decision.

## High-Risk Gates

- Claims need source span, evidence tier, weakest link, and safer wording.
- High-risk claim, citation, experiment, reproduction, and public-memory artifacts need executor/reviewer separation; final approval cannot be self-approved by the same model/pass.
- Result tables need numeric self-consistency.
- Reproduction statements need L0/L1/L2/L3 observability.
- Reviewer-facing output needs method-vs-writing diagnosis and integrity findings.
- Knowledge-base hits are retrieval memory, not final citation proof.
- Git publish tasks need target-branch confirmation, fresh remote state, ancestry checks, and temporary-branch cleanup only after target reachability.
