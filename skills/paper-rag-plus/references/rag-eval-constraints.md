# RAG Evaluation Constraints

Use these constraints when Paper-RAG++ retrieves from Zotero-derived memory.

## Required Distinctions

- Prior work versus current user contribution.
- Method innovation versus application innovation.
- Dataset contribution versus model contribution.
- Neural evidence versus AI benchmark evidence.
- Offline evidence versus online closed-loop evidence.
- Citation candidate versus verified citation.

## Retrieval Requirements

1. Match the claim to the closest prior work before suggesting novelty.
2. Prefer papers with aligned modality, task, dataset, and metric.
3. Identify missing citations when a claim lacks direct support.
4. Flag weak links such as qualitative-only evidence, unclear splits, weak baselines, or offline-only validation.
5. Use safer wording when the retrieved evidence supports only a narrower claim.

## Forbidden Behavior

- Do not cite auto-imported metadata as verified evidence without paper inspection.
- Do not infer subject counts, metrics, or significance from title alone.
- Do not treat general ML papers as direct neuroscience evidence.
- Do not use dataset availability as proof of method superiority.
- Do not claim first, robust, general, or closed-loop unless the evidence supports that exact scope.

## Output Check

For citation-critical answers, include:

```markdown
Claim:
Retrieved candidates:
Closest prior work:
Method novelty:
Application novelty:
Missing citation:
Reviewer risk:
Safer wording:
Verification needed:
```
