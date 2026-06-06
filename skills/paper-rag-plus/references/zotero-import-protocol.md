# Zotero Import Protocol

Use this protocol to convert private Zotero BIB exports into public Paper-RAG++ memory.

## Source

Raw Zotero exports must stay under `.private/zotero/`. Do not copy raw BIB, PDF attachments, local paths, personal notes, or unpublished project judgments into public skill files.

## Command

```bash
python3 skills/paper-rag-plus/scripts/import_zotero_bib.py \
  --input ".private/zotero/My Library.bib" \
  --enrich-web \
  --request-timeout 6
```

`--enrich-web` queries OpenAlex public metadata by DOI or title and stores the cache under `.private/zotero/openalex-cache.json`. The cache is private bookkeeping and is not required in public repository files.

## Public Outputs

- `references/zotero-library-index.md`: full structured paper index.
- `references/paper-taxonomy.md`: inferred research direction, modality, task, and tag taxonomy.
- `references/method-map.md`: method-to-paper map.
- `references/dataset-map.md`: dataset-to-paper map.
- `references/claim-to-citation.md`: claim-to-candidate-citation map.
- `references/manual-review-needed.md`: fields that could not be verified from Zotero BIB or public web metadata.

## Private Outputs

- `.private/references/zotero-import.private.md`: local import bookkeeping.
- `.private/zotero/My Library.bib`: raw source file, ignored by git.

## Public Field Policy

Allowed public fields:

- title
- year
- venue
- authors
- DOI
- URL when public
- cleaned Zotero tags
- inferred modality, task, method, dataset, and domain

Disallowed public fields:

- `file`
- local attachment paths
- personal notes or annotations
- raw abstracts copied in bulk
- unpublished project links or private experiment judgments
- credentials, tokens, participant-sensitive information, or IRB-sensitive details

## Update Procedure

1. Export the Zotero library as BIB into `.private/zotero/`.
2. Run the importer with `--enrich-web`.
3. Inspect generated maps for obvious parsing errors.
4. Use `manual-review-needed.md` for items that could not be verified by Zotero metadata or public web metadata.
5. Manually fill unresolved fields only after inspecting the paper or a trusted public source.
6. Run `make validate`.
7. Use `neuro-memory` to decide whether the import produced a reusable workflow, playbook, finding, case, or eval update.

## Citation Discipline

Auto-imported entries are retrieval memory, not citation proof. Before citation-critical use, inspect the paper or trusted metadata and verify venue, year, dataset, metric, and claim support.
