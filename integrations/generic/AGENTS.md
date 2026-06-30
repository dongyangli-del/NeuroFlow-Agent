<!-- neuroflow-managed -->
# NeuroFlow Generic Agent Instructions

This repository uses NeuroFlow as the default workflow layer for ML x BCI x neuroscience AutoResearch.

## Default Behavior

- Use `neuro-orchestrator` first for non-trivial research tasks.
- Do not wait for the user to mention workflow, plan, routing, or skills.
- Choose one pipeline chain and one primary artifact.
- Apply evidence gates before writing claims, citations, paper text, benchmark conclusions, or reproduction statements.
- For high-risk claim, citation, experiment, reproduction, and public-memory artifacts, separate executor and reviewer roles; final approval cannot be self-approved by the same model/pass.
- Use specialist skills only when their check order or output template is needed.

## Evidence Gates

- Literature: inspected source or explicit uncertainty.
- Benchmark: access, license, split, metric, baseline, leakage.
- Experiment: matched protocol, baselines, ablations, statistics.
- Reproduction: environment, data, weights, command, expected output, sanity check, observability level.
- Research integrity: claim-evidence consistency, citation fit, numeric self-consistency, protocol truthfulness.
- Memory: privacy filter and explicit target.
