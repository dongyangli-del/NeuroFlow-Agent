# Memory Routing

## Memory Types

| Type | Use when | Target |
|---|---|---|
| workflow | A reusable task sequence emerged | `references/workflows/*.md` |
| playbook | A repeated failure mode or diagnostic order emerged | `references/playbooks/*.md` |
| finding | A dated inspected result changes future decisions | `references/experiment-findings.md` |
| case | A public example demonstrates workflow value | `references/cases/*.md` |
| eval | A future agent must preserve behavior | `evals/evals.json` |
| private | The note includes sensitive or unpublished project memory | `.private/` or ignored private references |
| no-repo | The detail is one-off or not behavior-changing | No patch |

## Five Questions

1. Which checking order is reusable?
2. What failure pattern appeared?
3. What should the next agent read first?
4. Which judgment criteria cannot be skipped?
5. Which memory type fits, or should it stay out of the repo?
