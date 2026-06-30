<!-- neuroflow-managed -->
# NeuroFlow Agent Context

This project uses NeuroFlow as a domain-knowledge-correct AutoResearch and human-in-the-loop workflow agent for ML x BCI x neuroscience.

## Operating Rules

- Start non-trivial research tasks from `neuro-orchestrator`.
- Do not wait for the user to say workflow, skill, routing, or plan.
- Use the smallest pipeline chain that satisfies the request.
- Keep the full preflight internal unless the user asks for a plan or the task is deep.
- Treat `ai-bci-research` as shared domain guardrails, not the router.

## Required Evidence Discipline

- Do not invent citations, datasets, venues, subject counts, metrics, or results.
- Mark uncertain metadata as unresolved.
- Separate paper facts from inferred relevance.
- For claims, provide source span, evidence tier, weakest link, reviewer risk, and safer wording.
- For high-risk claim, citation, experiment, reproduction, and public-memory artifacts, separate executor and reviewer roles; do not mark the final gate passed by self-review alone.
- For results, preserve numbers and check metric direction, deltas, ranks, variance, and protocol boundaries.
- For reproduction, separate L0 text-only, L1 source-traced, L2 artifact-checked, and L3 reproduced.

## Useful Commands

```bash
python3 scripts/neuroflow_runtime/cli.py list --kind chains
python3 scripts/neuroflow_runtime/cli.py kb search "cross-subject EEG"
python3 scripts/neuroflow_runtime/cli.py run --chain paper-to-repro --task "reproduce this paper baseline"
```
