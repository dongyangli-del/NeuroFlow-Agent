# Session Memory Consolidation Playbook

## Failure Pattern

A research session produces a useful lesson, but the agent leaves it as chat history. Future sessions repeat the same file-reading mistake, skip the same diagnostic check, or make the same reviewer-facing overclaim.

## When to Trigger

Use this playbook at the end of a completed task when the session included debugging, paper-risk analysis, repository reproduction, experiment interpretation, or a user correction that should affect future behavior.

## Required First Reads

- `references/workflows/skill-factory.md`
- `references/update-protocol.md`
- The specific workflow, playbook, finding, or eval file that would receive the memory

## Checks in Order

1. Decide whether the lesson is reusable, private, or one-off.
2. Classify it as workflow, playbook, case, finding, eval, or no-repo.
3. Strip task-private details, local absolute paths, raw logs, credentials, and participant-sensitive details.
4. Convert the lesson into the fixed template for that memory type.
5. Add a minimal eval if the failure should be behaviorally enforced.
6. Rebuild the knowledge index and run validation.

## Minimal Probe

Ask: "Would a future agent change its first read, check order, acceptance criteria, or reviewer-facing interpretation because this note exists?"

If the answer is no, do not add it.

## Acceptance Criteria

- The memory unit is shorter than the transcript it came from.
- The trigger condition is explicit.
- The first-read file is named.
- The check order is testable.
- The acceptance criteria describe what good future behavior looks like.
- Private material is excluded or routed to ignored private memory.

## Reviewer-Facing Interpretation

Session memory is not evidence. It is a reproducibility and review-readiness aid. Claims still require inspected data, fair baselines, leakage checks, metric definitions, and documented experimental conditions.
