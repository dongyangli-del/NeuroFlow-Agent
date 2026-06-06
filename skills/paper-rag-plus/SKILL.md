---
name: paper-rag-plus
description: AI neuroscience and BCI literature grounding skill. Use for paper discovery, claim-to-citation mapping, related work synthesis, dataset and method mapping, and preventing unsupported neuroscience or AI claims.
---

# Paper-RAG++

Use this skill to ground AI x neuroscience claims in inspected literature. It should organize papers by modality, task, method, dataset, metric, and claim support.

## First Reads

- `references/paper-entry-template.md`: Read before adding or summarizing papers.
- `references/claim-grounding.md`: Read when mapping claims to citations or reviewer-facing evidence.
- `references/rag-eval-constraints.md`: Read for citation-critical RAG answers, novelty checks, and reviewer-facing claim support.
- `references/zotero-import-protocol.md`: Read when importing, updating, or auditing Zotero-derived memory.
- `references/zotero-library-index.md`: Read for Zotero-derived candidate papers; verify before citation-critical use.
- `references/paper-taxonomy.md`, `references/method-map.md`, `references/dataset-map.md`, `references/claim-to-citation.md`: Read selectively for taxonomy, method, dataset, and claim-support retrieval.

## Operating Rules

- Use `paper-lookup` for specific papers and `literature-review` for topic synthesis.
- Use `citation-management` when citation consistency matters.
- Do not invent citations, venues, datasets, subject counts, or metrics.
- Mark uncertain metadata as needs verification.
- Separate paper facts from inferred relevance to the user's project.
- Treat Zotero-derived maps as retrieval memory, not final citation proof.
- For novelty or related-work answers, distinguish prior work, method innovation, application innovation, missing citations, and safer claim wording.

## Output Formats

For a paper:

```markdown
Title:
Venue/year:
Signal modality:
Task:
Method:
Dataset:
Metric:
Main claim:
Reusable insight:
Limitations:
Relation to user's work:
Use when:
Do not cite for:
```

For a claim:

```markdown
Claim:
Closest support:
Weakest link:
Missing citation:
Reviewer risk:
Safer wording:
```
