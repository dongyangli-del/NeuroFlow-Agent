# Workflows

This project is built around a small set of reusable AI x BCI research workflows. Each workflow should give an agent enough structure to act rigorously without loading unrelated memory.

## BCI-RIGOR Loop

Use for experiment debugging, reproduction, and model-gap diagnosis.

1. Inspect the local repository and run configuration.
2. Identify the exact dataset, split protocol, target representation, model checkpoint, and metric.
3. Reproduce or verify the strongest deterministic baseline before changing the proposed method.
4. Audit leakage, normalization, output routing, condition alignment, checkpoint choice, and evaluator parity.
5. Localize the issue with train/validation/test probes and ablations.
6. Record the finding as symptom, confirmed facts, ruled-out causes, next probe, and acceptance criteria.

## Paper-to-Reviewer Loop

Use for abstracts, method sections, rebuttals, and submission readiness.

1. Establish the paper claim and the closest prior work.
2. Check whether the evidence actually supports the claim.
3. Separate decoding, reconstruction, alignment, and closed-loop claims.
4. Flag missing baselines, invalid splits, weak metrics, and unclear reproducibility details.
5. Rewrite claims with concrete nouns, measured evidence, and scoped limitations.

## Experiment Memory Loop

Use after new logs or debugging results are available.

1. Keep raw logs in the experiment workspace, not this skill repo.
2. Summarize only reusable conclusions in `references/experiment-findings.md`.
3. Add failure-mode procedures to `references/debugging-playbooks.md`.
4. Rebuild `references/knowledge-index.md`.
5. Add or update eval prompts when the new workflow should change agent behavior.

## Closed-Loop BCI Planning Loop

Use for EEG-guided stimulus optimization, neural feedback, or bidirectional BCI proposals.

1. Define objective, observation, action, policy, safety constraints, calibration, and evaluation.
2. Separate offline replay from online human-subject claims.
3. Include sham/random/fixed-stimulus controls and fatigue/adverse-response handling.
4. Report latency, calibration time, stop criteria, and statistical testing.
