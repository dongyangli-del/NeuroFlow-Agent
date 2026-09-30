# Zotero Memory Policy

Use this policy when converting private Zotero exports into durable NeuroFlow memory.

## Entry Criteria

Public memory is allowed when it is:

- General academic metadata.
- A cleaned paper index entry.
- A method, dataset, taxonomy, or claim-to-citation map.
- A reusable citation or reviewer-risk rule.
- A public workflow or eval constraint that changes future agent behavior.

Private memory is required when it contains:

- Raw Zotero BIB exports.
- Local PDF paths or attachment metadata.
- Personal reading notes.
- Unpublished project judgments.
- Private experiment associations.
- Participant-sensitive or IRB-sensitive details.

## Update Mechanism

1. Keep raw exports under `.private/zotero/`.
2. Run the Paper-RAG++ importer.
3. Store generated public maps under `skills/paper-rag-plus/references/`.
4. Store local import bookkeeping under `.private/references/`.
5. Add or update Paper-RAG++ evals when the import creates a new required retrieval behavior.
6. Run validation before trusting the generated memory.

## Agent Calling Permissions

- `paper-rag-plus` may read public maps by default.
- `neuro-memory` may reason about whether updates should persist.
- Private overlays are used only when the user explicitly provides or requests private context.
- Public answers must not expose private filenames, local paths, raw notes, or unpublished judgments.

## Memory Candidate Template

```markdown
Memory candidate:
- Should enter repo? yes/no
- Type: paper-index/claim-map/dataset-map/method-map/taxonomy/eval/private/no-repo
- Target file:
- Minimal patch:
- Risk of leaking private info:
- Suggested eval:
```
