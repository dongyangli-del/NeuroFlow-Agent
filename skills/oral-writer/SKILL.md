---
name: oral-writer
description: Oral-level AI, ML, NeuroAI, and BCI paper writing skill. Use for turning evidence into a clear thesis, novelty compression, figure narrative, claim-evidence alignment, limitations, reviewer-objection preemption, paper polishing, LaTeX/Word rewriting, logic checks, anti-AI-style cleanup, captions, and experiment analysis for top-tier conference submissions.
---

# Oral-Writer

Use this skill when the user wants oral-level paper framing, abstract/introduction rewriting, figure story, contribution framing, rebuttal polish, submission narrative, Chinese-to-English academic rewriting, English-to-Chinese reading translation, shortening, expansion, logic checking, anti-AI-style cleanup, figure/table titles, captions, LaTeX result tables, or experiment-result analysis.

## First Reads

- `references/oral-paper-structure.md`: Always read for thesis and section structure.
- `references/writing-operations.md`: Always read for writing operation taxonomy, format targets, and operation-specific gates.
- `references/figure-narrative.md`: Read for figure order, captions, and evidence flow.
- `references/plot-type-selector.md`: Read when recommending plots or figure types for results.
- `references/table-writing.md`: Read for LaTeX tables, result-table captions, metric directions, best-value marking, and uncertainty reporting.
- `references/experiment-analysis.md`: Read when turning results into a paper paragraph or result-section analysis.
- `references/numeric-self-consistency.md`: Read when writing abstracts, Results text, captions, tables, rebuttals, or claims that contain numbers.
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
- Classify the requested writing operation before rewriting.
- Preserve formulas, citations, labels, variables, metrics, datasets, and experimental conditions unless the user explicitly asks to remove them.
- Respect the target surface: LaTeX output stays clean LaTeX, Word output stays plain text, and direct-copy outputs avoid Markdown decorations.
- For anti-AI-style cleanup, remove mechanical transitions and vague flourish without changing technical meaning.
- For experiment analysis, only state trends and conclusions present in the supplied data.
- For plot recommendations, choose the simplest plot that exposes the comparison, uncertainty, and protocol boundary needed by the intended claim.
- For result tables, preserve all supplied numbers, define metric direction, mark best values only under comparable protocols, and never imply statistical significance without uncertainty or tests.
- For any numbered claim, preserve values exactly, check ranks and deltas, and keep metric direction, protocol boundary, uncertainty, and significance wording consistent.

## Workflow

1. State the thesis, closest prior work, and evidence boundary.
2. Classify the writing operation and target surface.
3. Build the contribution stack: problem, gap, method, evidence, limitation.
4. Define the figure narrative before rewriting sections, captions, or titles.
5. Rewrite text with concrete nouns, scoped claims, and reviewer-facing caveats.
6. Run operation-specific checks for format, logic, evidence, and meaning preservation.
7. Run objection preemption and identify missing evidence when the output makes or strengthens a paper claim.

## Required Output

```markdown
Thesis:
Closest prior work to verify:
Writing operation:
Target surface:
Contribution stack:
Evidence-to-claim map:
Numeric self-consistency:
Figure narrative:
Rewritten text or requested writing artifact:
Operation checks:
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
- Changing technical meaning during polishing, translation, shortening, or anti-AI-style cleanup.
- Producing Markdown, escaped LaTeX, or prose formatting that conflicts with the target surface.
- Turning experiment tables into unsupported narrative claims.
