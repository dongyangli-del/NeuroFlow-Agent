# Writing Operations

This taxonomy turns common paper-writing requests into explicit NeuroFlow operations. It is adapted at the task-category level from public AI research writing prompt libraries, including `Leey21/awesome-ai-research-writing`, but NeuroFlow uses evidence gates and operation checks instead of copying prompt templates.

## Operation Taxonomy

| Operation | Use when | Required checks |
|---|---|---|
| `zh-to-en-latex` | Chinese notes should become English LaTeX paper prose. | Preserve formulas, citations, labels, variables, datasets, metrics, and technical meaning; escape LaTeX-sensitive characters only when needed. |
| `en-to-zh-reading` | English LaTeX or paper text should become Chinese for reading or checking. | Translate for meaning, remove or verbalize formatting only when the user asks, and do not silently repair weak logic. |
| `zh-to-en-word` | Chinese notes should become English paper prose for Word or plain text. | Do not emit Markdown; do not LaTeX-escape normal text; preserve formulas and symbols in readable form. |
| `zh-to-zh-word` | Chinese notes should become formal Chinese academic prose. | Convert loose notes into coherent paragraphs while preserving technical terms and original claim scope. |
| `shorten` | Text must be compressed. | Remove redundancy, not evidence; keep datasets, metrics, numbers, conditions, and limitations. |
| `expand` | Text needs more connective tissue or reviewer-facing explanation. | Add only logical bridges supported by the supplied material; mark missing evidence instead of inventing it. |
| `polish-en` | English paper prose needs style and clarity improvement. | Prefer concrete nouns, active structure, common precise words, and scoped claims. |
| `polish-zh` | Chinese paper prose needs style and clarity improvement. | Keep author intent, remove口语化 phrasing, and avoid unnecessary rewriting when the original is already clear. |
| `logic-check` | User asks whether a paragraph, section, or claim is coherent. | Report only material logic breaks, contradictions, ambiguous terms, unsupported claims, and severe grammar issues. |
| `anti-ai-style-latex` | English LaTeX sounds mechanically generated. | Remove boilerplate transitions and vague flourish while preserving LaTeX, claims, variables, and citations. |
| `anti-ai-style-word` | Chinese or plain text sounds mechanically generated. | Replace empty emphasis with concrete claims, preserve domain terms, and avoid Markdown. |
| `architecture-figure-plan` | A method description needs a paper architecture figure plan. | Identify modules, data flow, supervision, inference path, and what the figure must prove. |
| `plot-recommendation` | Experiment results need a figure type. | Use `plot-type-selector.md`; choose plots based on comparison structure, variance, metric type, label length, and the intended claim. |
| `latex-table` | Results should become a LaTeX paper table. | Use `table-writing.md`; preserve numbers, define metric direction, compare only comparable rows, and avoid significance claims without uncertainty. |
| `figure-title` | A figure needs an English title or caption seed. | State the finding directly and avoid ornamental verbs. |
| `table-title` | A table needs an English title or caption seed. | Name the comparison, metric, dataset/protocol, and key takeaway when known. |
| `experiment-analysis` | Results should become a paper paragraph. | Use `experiment-analysis.md`; only use supplied values, distinguish main result from ablation/robustness/error analysis, and include uncertainty when available. |
| `reviewer-view-audit` | The user wants a whole-paper writing and claim review. | Lead with blocking issues, evidence gaps, fairness of baselines, missing ablations, and fixable writing problems. |
| `model-choice-rationale` | The paper needs a rationale for method/model selection. | Tie model choice to task constraints, data scale, modality, latency, interpretability, and baseline parity. |

## Target Surfaces

| Surface | Output rule |
|---|---|
| `latex` | Keep valid LaTeX fragments, preserve math and commands, and avoid decorative formatting. |
| `word` | Emit direct-copy plain text without Markdown headings, bullets, code fences, or LaTeX-specific escaping unless the source formula requires it. |
| `plain_text` | Emit the requested prose only, with minimal labels when useful for review. |
| `review_report` | Use issue-first structure with concrete evidence gaps and repair actions. |
| `caption` | State what is shown, the main takeaway, how it supports the claim, and the relevant protocol limitation. |

## Operation Preflight

Before rewriting, decide:

```markdown
Writing operation:
Target surface:
Input evidence:
Claims that must not change:
Terms that must not change:
Format constraints:
Evidence gate needed:
```

Keep this preflight internal for simple polishing. Expose it when the request is ambiguous, the text makes scientific claims, or the rewrite could change evidence scope.

## Meaning Preservation Rules

- Never change datasets, metrics, baselines, subject/session conditions, p-values, confidence intervals, model names, or task labels during style work.
- Do not upgrade a weak statement into a strong claim.
- Do not turn an observed association into causality.
- Do not add citations or closest-prior-work claims without `paper-rag-plus`.
- If the input lacks evidence for a claim, keep the claim scoped or mark the missing evidence.
- If shortening would remove a limitation, preserve the limitation and shorten elsewhere.

## Style Rules

- Prefer common precise words over inflated wording.
- Use transitions only when they express a real relation: contrast, cause, condition, evidence, or limitation.
- Avoid generic praise words such as significant, robust, effective, general, novel, and powerful unless the evidence is explicit.
- Use one paragraph for one job: motivation, gap, method, evidence, or limitation.
- When the original text is already clear, make minimal edits and say so in the operation checks.
