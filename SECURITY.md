# Security Policy

## Public Repository Rules

Do not commit private or sensitive research material to this repository.

Keep the following out of public files:

- API keys, access tokens, private keys, passwords, and service credentials.
- Local machine paths, private server paths, and unpublished repository setup notes.
- Human-subject data, participant identifiers, raw EEG or neural recordings, consent material, and IRB documents.
- Unpublished numeric results, reviewer strategy, paper drafts under embargo, rebuttal plans, private experiment logs, checkpoints, datasets, and generated outputs.
- Zotero exports or paper maps that include private notes, unpublished annotations, or non-public lab strategy.

Use ignored private overlays such as `.private/` for local memory that should not be published. When a private lesson is broadly reusable, distill only the public-safe workflow, check order, or eval prompt into `skills/*/references/`.

## Validation

Run the repository validator before publishing changes:

```bash
make validate
```

The validator scans public text files for common secret patterns and local path leaks, checks required skill files, validates JSON evals, resolves local Markdown links, and blocks large generated files.

## Reporting Issues

If you find a leaked secret, private dataset detail, human-subject material, or unpublished result in public files, remove it from the branch immediately and rotate any affected credential. For public reports, open a GitHub issue that describes the affected file path without copying the sensitive content.
