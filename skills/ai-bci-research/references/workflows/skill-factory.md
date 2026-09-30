# Skill Factory Workflow

Use this workflow after a meaningful research session, especially after experiment debugging, paper review, repo reproduction, rebuttal drafting, or repeated user correction.

## Trigger

Run this workflow when at least one of these is true:

- The session found a reusable inspection order.
- The session found a recurring failure pattern.
- The session changed what future agents should read first.
- The session produced a reviewer-facing criterion that should not be skipped.
- The user explicitly asks to turn an experience into skill memory.

## Five-Question Compression

Ask or answer these questions before editing memory:

1. Which checking order from this task is reusable?
2. What common failure pattern appeared?
3. What file should the next agent read first?
4. Which judgment criteria cannot be skipped?
5. Should this become a workflow, playbook, finding, eval, private note, or not enter the repo?

## Memory Candidate Block

End qualifying sessions with this compact block:

```markdown
Memory candidate:
- Should enter repo? yes/no
- Target file:
- Minimal patch:
- Risk of leaking private info:
- Suggested eval:
```

If the answer is `no`, give the reason and do not create a patch. If the content is private, point to `references/private/` or the repo-level `.private/` overlay and keep it out of public files.

## Routing Rules

Use the smallest durable memory type:

| Durable unit | Target |
|---|---|
| Reusable task sequence | `references/workflows/*.md` |
| Repeated failure mode | `references/playbooks/*.md` or `references/debugging-playbooks.md` |
| Dated inspected result | `references/experiment-findings.md` |
| Real demonstration case | `references/cases/*.md` |
| Required future behavior | `evals/evals.json` |
| Personal, unpublished, or sensitive details | `references/private/` or `.private/` |
| One-off transcript detail | Do not enter repo |

## Update Order

1. Write the smallest patch.
2. Add an eval when a future agent must behave differently.
3. Rebuild `references/knowledge-index.md`.
4. Run repository validation.
5. In the final response, report the memory file, eval change, and leakage decision.

## Acceptance Criteria

- The new memory changes a future agent's behavior.
- The patch is template-shaped, not transcript-shaped.
- No private path, participant detail, credential, raw log, or unpublished sensitive claim enters public files.
- The new memory is discoverable from `SKILL.md` or `references/knowledge-index.md`.
