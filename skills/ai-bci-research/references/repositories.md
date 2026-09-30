# Repository Index

This public file defines how repository memory should be recorded without exposing private paths, credentials, unreleased project state, or lab-internal run details. Project-specific repo notes can be kept in a local gitignored private overlay.

## Public Repository Entry Template

Use this structure for public repositories:

```text
## Repository Name

- URL:
- Related paper or project:
- Public scope:
- Important public structure:
- Setup signals:
- Data/checkpoint dependencies:
- Common tasks:
- Known caveats:
```

## AI x BCI Repository Types

- Decoding/reconstruction repositories: usually include preprocessing, encoder training, retrieval, reconstruction/generation, and evaluation code.
- Dataset repositories: usually include acquisition protocol, preprocessing, metadata, alignment scripts, and access instructions.
- Closed-loop BCI repositories: usually include model training, stimulus/action search, client/server or online interaction code, latency handling, safety constraints, and offline/online evaluation.
- Project-page repositories: usually include paper metadata, figures, links, static pages, and result summaries.

## Local Repo Workflow

When the user provides a local path:

1. Inspect structure with the fastest available file lister.
2. Read `README`, environment files, config files, and entry scripts before editing.
3. Identify data path assumptions and checkpoint dependencies.
4. Run lightweight checks first: import checks, config validation, dry runs, or unit tests if present.
5. Preserve existing experiment outputs and do not delete data/checkpoints unless explicitly asked.
6. Do not copy private local paths, credentials, raw logs, or unpublished results into public reference files.
