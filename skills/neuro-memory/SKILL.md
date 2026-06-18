---
name: neuro-memory
description: Long-term AI neuroscience research memory consolidation skill. Use after meaningful research sessions to compress reusable workflows, failure modes, findings, demo cases, evals, and private notes without leaking sensitive information.
---

# Neuro-Memory

Use this skill to decide what a completed AI x neuroscience session should preserve. It does not store raw transcripts; it routes compact, behavior-changing memory.

## First Reads

- `references/memory-routing.md`: Always read first for memory type decisions.
- `references/compression-template.md`: Read when producing a memory candidate.
- `references/privacy-policy.md`: Read when content may contain private paths, unpublished details, credentials, participant information, or raw logs.
- `references/zotero-memory-policy.md`: Read when Zotero exports or literature memory are being imported, updated, or audited.

## Operating Rules

- Preserve behavior, not conversation history.
- Public memory must be reusable, compact, and free of private details.
- Private or sensitive notes must go to ignored private overlays, not public skill files.
- Add evals when the future behavior must be enforced.
- Use `skill-creator` when a repeated memory pattern should become a new or updated skill.
- Store the memory's verification status so future agents know whether it is unverified, source-traced, reproduced, user-validated, or expert-reviewed.

## Required Output

```markdown
Memory candidate:
- Should enter repo? yes/no
- Type: workflow/playbook/finding/case/eval/private/no-repo
- Verification status:
- Source evidence:
- Target file:
- Minimal patch:
- Risk of leaking private info:
- Suggested eval:
```

## Acceptance Criteria

- The memory changes a future agent's first read, check order, acceptance criteria, or reviewer-facing interpretation.
- The target file is explicit.
- Sensitive details are removed or routed to private memory.
- Validation steps are named.
