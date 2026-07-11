"""Static Markdown and HTML evolution reports."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from jinja2 import Environment, select_autoescape

from .storage import EvolutionStore

MARKDOWN_TEMPLATE = """# NeuroFlow Evolution Report

Generated from the local evolution control plane.

## Summary

- Candidates: {{ candidates|length }}
- Eval runs: {{ eval_runs|length }}
- Decisions: {{ decisions|length }}
- Promoted: {{ promoted }}
- Awaiting review: {{ awaiting_review }}

## Candidates

| ID | Target | Status | Risk | Human approval | Expected gain |
|---|---|---|---|---|---:|
{% for candidate in candidates -%}
| `{{ candidate.id }}` | {{ candidate.target_component|replace('|', '&#124;') }} | {{ candidate.status }} | {{ candidate.risk_level }} | {{ candidate.requires_human }} | {{ '%.3f'|format(candidate.expected_gain) }} |
{% endfor %}

## Candidate Details

{% for candidate in candidates -%}
### `{{ candidate.id }}`

- Target: {{ candidate.target_component }}
- Risk: {{ candidate.risk_level }}
- Comparison: `{{ candidate.comparison }}`
- Executor: `{{ candidate.executor }}`
- Reviewer: `{{ candidate.reviewer }}`
- Review verdict/disagreements: `{{ candidate.review_verdict }}`
- Patch integrity: {{ candidate.patch_integrity }}
- Status history: `{{ candidate.status_history }}`
- Rollback: `neuroflow evolve rollback {{ candidate.id }} --actor project-owner --reason "reason"`

```diff
{{ candidate.patch }}
```

{% endfor %}

## Evaluation Runs

| ID | Candidate | Score | Critical | Regressions | Cost |
|---|---|---:|---|---|---:|
{% for run in eval_runs -%}
| `{{ run.id }}` | `{{ run.candidate_id or 'parent' }}` | {{ '%.3f'|format(run.score) }} | {{ run.critical_pass }} | {{ run.regressions|join(', ') or 'none' }} | {{ run.cost }} |
{% endfor %}

## Decisions

| Time | Candidate | Decision | Actor | Automatic | Reason |
|---|---|---|---|---|---|
{% for decision in decisions -%}
| {{ decision.created_at }} | `{{ decision.candidate_id }}` | {{ decision.decision }} | {{ decision.actor }} | {{ decision.automatic }} | {{ decision.reason|replace('|', '&#124;')|replace('\n', ' ') }} |
{% endfor %}

## Evaluation Details

{% for run in eval_runs -%}
### `{{ run.id }}`

- Candidate: `{{ run.candidate_id or 'parent' }}`
- Dimensions: `{{ run.dimension_scores }}`
- Regressions: `{{ run.regressions }}`
- Per-case mean/variance: `{{ run.case_statistics }}`
- Result artifact: `{{ run.result_path }}`

{% endfor %}
"""

HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>NeuroFlow Evolution Report</title>
  <style>
    :root { color-scheme: light; font-family: Inter, ui-sans-serif, system-ui, sans-serif; }
    body { margin: 0; color: #17211d; background: #f5f7f6; }
    header { padding: 24px max(24px, calc((100vw - 1180px) / 2)); background: #fff; border-bottom: 1px solid #dce4df; }
    h1 { margin: 0; font-size: 24px; letter-spacing: 0; }
    main { max-width: 1180px; margin: 0 auto; padding: 24px; }
    .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; }
    .stat { padding: 16px; background: #fff; border: 1px solid #dce4df; border-radius: 6px; }
    .stat strong { display: block; font-size: 26px; }
    section { margin-top: 28px; }
    .table-wrap { overflow-x: auto; border: 1px solid #dce4df; border-radius: 6px; background: #fff; }
    table { width: 100%; border-collapse: collapse; font-size: 14px; }
    th, td { padding: 10px 12px; border-bottom: 1px solid #e7ece9; text-align: left; vertical-align: top; }
    th { background: #eef3f0; font-weight: 650; }
    code { font-size: 12px; }
    .low { color: #087443; } .medium { color: #9a6200; } .high, .critical { color: #b42318; }
  </style>
</head>
<body>
<header><h1>NeuroFlow Evolution Report</h1></header>
<main>
  <div class="stats">
    <div class="stat"><strong>{{ candidates|length }}</strong>Candidates</div>
    <div class="stat"><strong>{{ eval_runs|length }}</strong>Eval runs</div>
    <div class="stat"><strong>{{ decisions|length }}</strong>Decisions</div>
    <div class="stat"><strong>{{ promoted }}</strong>Promoted</div>
  </div>
  <section><h2>Candidates</h2><div class="table-wrap"><table>
    <thead><tr><th>ID</th><th>Target</th><th>Status</th><th>Risk</th><th>Expected gain</th></tr></thead>
    <tbody>{% for c in candidates %}<tr><td><code>{{ c.id }}</code></td><td>{{ c.target_component }}</td><td>{{ c.status }}</td><td class="{{ c.risk_level }}">{{ c.risk_level }}</td><td>{{ '%.3f'|format(c.expected_gain) }}</td></tr>{% endfor %}</tbody>
  </table></div></section>
  <section><h2>Candidate Diffs</h2>
    {% for c in candidates %}<details><summary><code>{{ c.id }}</code> - {{ c.target_component }}</summary>
      <p>Comparison: <code>{{ c.comparison }}</code></p>
      <p>Executor: <code>{{ c.executor }}</code> Reviewer: <code>{{ c.reviewer }}</code></p>
      <p>Review verdict/disagreements: <code>{{ c.review_verdict }}</code></p>
      <p>Patch integrity: <code>{{ c.patch_integrity }}</code></p>
      <p>Status history: <code>{{ c.status_history }}</code></p>
      <pre>{{ c.patch }}</pre>
      <p><code>neuroflow evolve rollback {{ c.id }} --actor project-owner --reason "reason"</code></p>
    </details>{% endfor %}
  </section>
  <section><h2>Evaluation Runs</h2><div class="table-wrap"><table>
    <thead><tr><th>ID</th><th>Candidate</th><th>Score</th><th>Critical</th><th>Regressions</th><th>Cost</th></tr></thead>
    <tbody>{% for r in eval_runs %}<tr><td><code>{{ r.id }}</code></td><td><code>{{ r.candidate_id or 'parent' }}</code></td><td>{{ '%.3f'|format(r.score) }}</td><td>{{ r.critical_pass }}</td><td>{{ r.regressions|join(', ') or 'none' }}</td><td><code>{{ r.cost }}</code></td></tr>{% endfor %}</tbody>
  </table></div></section>
  <section><h2>Decisions</h2><div class="table-wrap"><table>
    <thead><tr><th>Time</th><th>Candidate</th><th>Decision</th><th>Actor</th><th>Reason</th></tr></thead>
    <tbody>{% for d in decisions %}<tr><td>{{ d.created_at }}</td><td><code>{{ d.candidate_id }}</code></td><td>{{ d.decision }}</td><td>{{ d.actor }}</td><td>{{ d.reason }}</td></tr>{% endfor %}</tbody>
  </table></div></section>
  <section><h2>Evaluation Details</h2>
    {% for r in eval_runs %}<details><summary><code>{{ r.id }}</code> - {{ r.candidate_id or 'parent' }}</summary>
      <p>Dimensions: <code>{{ r.dimension_scores }}</code></p>
      <p>Regressions: <code>{{ r.regressions }}</code></p>
      <p>Per-case mean/variance: <code>{{ r.case_statistics }}</code></p>
      <p>Cost: <code>{{ r.cost }}</code></p>
      <p>Result: <code>{{ r.result_path }}</code></p>
    </details>{% endfor %}
  </section>
</main>
</body></html>
"""


def build_report(root: Path, store: EvolutionStore, output_dir: Path | None = None) -> dict[str, str]:
    candidate_models = store.list_candidates()
    candidates = []
    for candidate in candidate_models:
        patch_path = Path(candidate.patch_path)
        patch = patch_path.read_text(encoding="utf-8") if patch_path.exists() else "<missing patch>"
        patch_integrity = (
            patch != "<missing patch>"
            and hashlib.sha256(patch.encode("utf-8")).hexdigest() == candidate.patch_sha256
        )
        metadata = candidate.metadata
        candidates.append(
            {
                **candidate.model_dump(mode="json"),
                "patch": patch,
                "patch_integrity": patch_integrity,
                "comparison": metadata.get("comparison", {}),
                "executor": metadata.get("executor", {}),
                "reviewer": metadata.get("reviewer", {}),
                "review_verdict": metadata.get("review_verdict", {}),
                "status_history": metadata.get("status_history", []),
            }
        )
    eval_runs = store.list_eval_runs()
    for run in eval_runs:
        result_path = Path(run["result_path"])
        run["case_statistics"] = {}
        if result_path.exists():
            try:
                payload = json.loads(result_path.read_text(encoding="utf-8"))
                run["case_statistics"] = payload.get("case_statistics", {})
            except (OSError, ValueError):
                run["case_statistics"] = {"error": "unreadable result artifact"}
    decisions = store.list_decisions()
    output_dir = output_dir or root / ".private" / "evolution" / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)
    context: dict[str, Any] = {
        "candidates": candidates,
        "eval_runs": eval_runs,
        "decisions": decisions,
        "promoted": sum(candidate.status.value == "promoted" for candidate in candidate_models),
        "awaiting_review": sum(candidate.status.value == "awaiting_review" for candidate in candidate_models),
    }
    environment = Environment(autoescape=select_autoescape(["html", "xml"]))
    markdown = Environment(autoescape=False).from_string(MARKDOWN_TEMPLATE).render(**context)
    rendered_html = environment.from_string(HTML_TEMPLATE).render(**context)
    markdown_path = output_dir / "evolution-report.md"
    html_path = output_dir / "evolution-report.html"
    markdown_path.write_text(markdown, encoding="utf-8")
    html_path.write_text(rendered_html, encoding="utf-8")
    return {"markdown": str(markdown_path), "html": str(html_path)}
