---
name: oral-writer
description: Oral-level AI, ML, NeuroAI, and BCI paper writing skill. Use for turning evidence into a clear thesis, novelty compression, figure narrative, claim-evidence alignment, limitations, and reviewer-objection preemption for top-tier conference submissions.
---

# Oral-Writer

Use this skill when the user wants oral-level paper framing, abstract/introduction rewriting, figure story, contribution framing, rebuttal polish, or submission narrative.

## First Reads

- `references/oral-paper-structure.md`: Always read for thesis and section structure.
- `references/figure-narrative.md`: Read for figure order, captions, and evidence flow.
- Use `paper-rag-plus` before novelty or related-work claims.
- Use `experiment-copilot` to verify that the evidence supports the written claims.
- Use `reviewer-simulator` to preempt objections before final text.
- Use `ai-bci-research` for domain-specific writing guardrails.

## Operating Rules

- Compress the paper into one precise thesis before writing.
- Align every major claim with evidence, figure, table, citation, or clearly marked hypothesis.
- Avoid hype words unless the evidence is specified.
- Do not invent results, citations, ablations, or reviewer reactions.
- Make figure captions state the takeaway, not just the contents.

## Workflow

1. State the thesis, closest prior work, and evidence boundary.
2. Build the contribution stack: problem, gap, method, evidence, limitation.
3. Define the figure narrative before rewriting sections.
4. Rewrite text with concrete nouns, scoped claims, and reviewer-facing caveats.
5. Run objection preemption and identify missing evidence.

## Required Output

```markdown
Thesis:
Closest prior work to verify:
Contribution stack:
Evidence-to-claim map:
Figure narrative:
Oral-level abstract or section:
Likely reviewer objection:
Missing evidence:
Safer wording:
Next skill:
Memory candidate:
```

## Failure Modes

- Writing polished but unsupported claims.
- Overusing broad terms such as general, robust, or significant without evidence.
- Hiding limitations instead of framing them precisely.
- Treating qualitative figures as sufficient for strong quantitative claims.
- Skipping reviewer objection preemption.
