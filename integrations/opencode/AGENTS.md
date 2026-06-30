<!-- neuroflow-managed -->
# NeuroFlow Agent Rules

Use NeuroFlow as the project-level research workflow for ML x BCI x neuroscience.

## Default Entry

For any non-trivial research, writing, review, experiment, benchmark, reproduction, or memory task:

1. Start with `neuro-orchestrator`.
2. Classify task depth: shallow, standard, deep, or persistent.
3. Choose the smallest pipeline chain.
4. Name the primary artifact and evidence gates.
5. Use specialist modules only when they add a distinct check order.
6. Apply integrity gates before paper-facing claims, citations, result tables, and reproduction statements.
7. For high-risk claim, citation, experiment, reproduction, and public-memory artifacts, separate executor and reviewer roles; final approval cannot be self-approved by the same model/pass.
8. For commit, push, branch deletion, or remote sync tasks, confirm the user-named target branch, fetch remote state, verify ancestry, and remove temporary branches only after target reachability.

## Output Discipline

- Lead with blocking issues for reviews.
- Keep claims scoped to inspected evidence.
- Use claim ledgers for citation-sensitive work.
- Use numeric self-consistency for result writing.
- Use observability levels for reproduction.
- Keep private data and raw logs out of public memory.
