# Verification Dashboard

This dashboard summarizes the public verification state of NeuroFlow knowledge artifacts. It is intended for external users who need to know which files are retrieval memory, which are source-traced, and which fields still require human review.

## Current Status

| Knowledge category | Public artifact | Current status | What is safe to do | Remaining risk |
|---|---|---|---|---|
| Zotero-aligned paper taxonomy | [paper-taxonomy.md](../skills/paper-rag-plus/references/paper-taxonomy.md) | `source-traced` collection alignment | Browse and route papers by collection/task/method area. | Citation-critical use still requires paper inspection. |
| Source title matching | [source-verification-report.md](../skills/paper-rag-plus/references/source-verification-report.md) | `source-traced` for 177 priority entries | Trust that retained priority entries have strict title matches. | Title match is not the same as full paper-content verification. |
| Field extraction | [field-verification-report.md](../skills/paper-rag-plus/references/field-verification-report.md) | `agent-source-traced` for accepted updates | Use extracted fields as workflow memory with evidence tier visible. | Not human-reviewed or expert-reviewed. |
| Method map | [method-map.md](../skills/paper-rag-plus/references/method-map.md) | high-precision metadata evidence | Retrieve method candidates and method-family examples. | Some differences, caveats, and limitations remain unresolved. |
| Dataset map | [dataset-map.md](../skills/paper-rag-plus/references/dataset-map.md) | neural-dataset filtered metadata evidence | Retrieve likely neural/BCI dataset usage. | Dataset access, license, split, and misuse boundaries may need manual checks. |
| Claim-to-citation map | [claim-to-citation.md](../skills/paper-rag-plus/references/claim-to-citation.md) | single-paper metadata evidence | Find candidate support and reviewer risk language. | Do not treat cluster membership as consensus. |
| Manual review queue | [manual-review-needed.md](../skills/paper-rag-plus/references/manual-review-needed.md) | `needs_human_review` | See exactly which fields are unresolved. | Listed fields should not support final claims. |
| Runtime registry | [WORKFLOWS.md](WORKFLOWS.md) and `.private/runs/` | scaffolded traceability | Record chosen chain, artifact, evidence gates, and stop condition. | Trace scaffolds are not scientific evidence until filled. |
| Behavior evals | skill `evals/evals.json` files | regression checks | Catch workflow behavior regressions. | Evals are prompts, not exhaustive tests. |

## Public Counts

| Metric | Count | Source |
|---|---:|---|
| Zotero-aligned parsed papers | 1497 | `paper-taxonomy.md` collection provenance audit |
| Papers with Zotero Collection assignments | 1497 | `paper-taxonomy.md` collection provenance audit |
| Priority entries checked for source title matching | 177 | `source-verification-report.md` |
| Source-traced priority title matches | 177 | `source-verification-report.md` |
| Failed public matches dropped from review lists | 123 | `source-verification-report.md` |
| Remaining manual-review entries | 6 | `manual-review-needed.md` |
| Remaining unresolved DOI fields | 4 | `manual-review-needed.md` |
| Remaining unresolved limitation fields | 2 | `manual-review-needed.md` |

## Launch Interpretation

- The knowledge graph is useful as a retrieval and workflow-routing substrate.
- The source-traced priority set is safe to expose publicly as inspected matching metadata.
- The manual-review queue is intentionally small and explicit.
- The maps should not be advertised as a fully read, fully reproduced paper database.

## Next Verification Upgrades

1. Add a generated `kb refresh` command that rebuilds this dashboard from the source reports.
2. Add field-level confidence histograms for dataset, metric, method, limitation, and DOI fields.
3. Add public examples showing how a raw retrieval hit becomes a claim ledger row.
4. Add reproduction-status rows once repo-level examples reach L2 or L3 observability.
