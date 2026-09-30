# Verified Evolution Loop

Use this workflow when a real session should change future NeuroFlow behavior rather than only add a note.

## Trigger

- A user correction, evidence-gate failure, tool failure, reviewer objection, or eval regression occurred.
- The same failure pattern appeared across multiple runs.
- A proposed workflow or skill change needs measurable promotion evidence.

## Check Order

1. Record a versioned trace and structured feedback event.
2. Cluster failures by behavior, not by transcript wording.
3. Choose the smallest mutation target: reference, eval, existing skill, route, tool, then new skill.
4. Add an incident regression eval without exposing hidden holdout cases.
5. Evaluate the unmodified parent and candidate under the same providers, cases, repeats, and cost accounting.
6. Reject safety regressions, retention regressions, insufficient gain, or excessive cost.
7. Require independent review for public memory and human approval for skill, routing, pipeline, or code changes.
8. Run post-apply canary validation and retain a reversible patch.

## Acceptance Criteria

- The candidate improves the target slice by at least the configured promotion margin.
- Protected gates all pass and previously passing behavior does not regress.
- The candidate was not optimized against hidden holdout content.
- The decision records executor, reviewer, evidence, cost, actor, and rollback target.
- Promotion changes only the local worktree; commit and publication remain separate explicit operations.

## Failure Modes

- Treating an LLM preference as external evidence.
- Reusing the same model response as executor and independent reviewer.
- Adding a new skill when a reference or eval fixes the failure.
- Promoting a public reference without source traceability.
- Mutating protected evals or using hidden cases as prompt context.
- Reporting static validation as longitudinal self-improvement.
