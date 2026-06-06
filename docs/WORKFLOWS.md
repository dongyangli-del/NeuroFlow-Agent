# Workflows

This project is built around a small set of reusable AI x BCI research workflows. Each workflow should give an agent enough structure to act rigorously without loading unrelated memory.

## Agent Workflow Thesis

An agent has three practical components: model, tools, and workflow. The model and tools can usually be shared across domains, but the workflow must be customized for AI x BCI research because it encodes domain-specific inspection order, validity checks, evidence thresholds, and memory updates.

In this repository, workflow means a persistent operating procedure, not a one-time checklist. A good workflow should decide:

1. which memory to replay before acting;
2. which validity checks must happen before interpretation;
3. which output is appropriate for the task;
4. which lesson should be consolidated for future sessions.

## Persistent Memory Loop

Use after any meaningful paper review, repository inspection, experiment debugging session, or rebuttal.

1. Replay only the relevant memory: profile, paper map, repo notes, BCI workflow, debugging playbook, writing style, or reviewer objections.
2. Execute the domain workflow and keep raw artifacts outside the skill repository.
3. Distill reusable experience into the smallest durable unit: dated finding, playbook update, reviewer objection, workflow rule, eval prompt, or profile update.
4. Rebuild `references/knowledge-index.md`.
5. Run validation and verify that the new memory would change a future agent's behavior.

This is the self-evolution path for the repo. The system should improve through consolidation, not by accumulating long transcripts.

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

## Memory Replay and Consolidation Rules

Use these rules to decide where new information belongs.

| New information | Store as |
|---|---|
| A stable research preference or long-term mission shift | `references/research-profile.md` |
| A paper, dataset, venue, or citation-positioning note | `references/papers-index.md` or `references/venue-workflows.md` |
| A repository setup, structure, or reproducibility note | `references/repositories.md` |
| A repeated experiment failure mode | `references/debugging-playbooks.md` |
| A dated, inspected result that changes future decisions | `references/experiment-findings.md` |
| A claim risk or likely reviewer objection | `references/reviewer-objections.md` |
| A behavior that future agents must preserve | `evals/evals.json` |

## Closed-Loop BCI Planning Loop

Use for EEG-guided stimulus optimization, neural feedback, or bidirectional BCI proposals.

1. Define objective, observation, action, policy, safety constraints, calibration, and evaluation.
2. Separate offline replay from online human-subject claims.
3. Include sham/random/fixed-stimulus controls and fatigue/adverse-response handling.
4. Report latency, calibration time, stop criteria, and statistical testing.
