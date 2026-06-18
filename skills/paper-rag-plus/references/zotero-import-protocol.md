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
- `references/source-verification-report.md`: strict title-match verification results from DBLP, Crossref, and Semantic Scholar.

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
6. Run `verify_paper_terms.py` when `manual-review-needed.md` contains paper-title candidates that can be checked against public metadata.
7. Run `verify_manual_review_fields.py` after title matching to auto-upgrade source-traced fields from matched metadata and short public/Zotero evidence snippets.
8. Run `make validate`.
9. Use `neuro-memory` to decide whether the import produced a reusable workflow, playbook, finding, case, or eval update.

## Source Verification

```bash
python3 skills/paper-rag-plus/scripts/verify_paper_terms.py
```

The verifier follows the local OnlyCCFA-style policy: DBLP first, then strict title metadata lookup through Crossref and Semantic Scholar. It writes source-traced bibliographic facts only when title matching succeeds. If matching fails, it marks the entry as `联网搜索匹配失败，留待人工核验`.

This pass verifies paper identity, year, venue, DOI, URL, and authors when public metadata supports them. It does not automatically validate method advantages, dataset suitability, metrics, limitations, claim support, or reproducibility.

## Field Verification

```bash
python3 skills/paper-rag-plus/scripts/verify_manual_review_fields.py --drop-resolved
```

This pass reads title-matched entries and upgrades fields only when source-traced evidence is available. Bibliographic fields come from the strict title match first, with OpenAlex or Semantic Scholar used only to fill missing values. Content fields use short title/abstract/keyword evidence snippets and keep unsupported fields in `manual-review-needed.md`.

## Citation Discipline

Auto-imported entries are retrieval memory, not citation proof. Before citation-critical use, inspect the paper or trusted metadata and verify venue, year, dataset, metric, and claim support.
