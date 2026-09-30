# Paper Entry Template

```markdown
## Paper Title

Bibliographic:
- year:
- venue:
- doi:

Paper type:
- type: primary_research | review | perspective | theory | benchmark | dataset | system

Evidence fields:
- signal_modality:
- input_modality:
- task_taxonomy:
- paper_objective:
- method_family:
- method_summary:
- dataset:
- dataset_role: created | used | benchmark | cited_only | none_review | unresolved
- metric:
- metric_status: applicable | not_applicable | unresolved
- limitations:
- limitation_source: explicit | discussion | experimental_boundary | unresolved

Verification:
- final_unresolved_fields:
- verification_status:
- evidence_sources:
- evidence_tier:
- confidence:
```

## Required Checks

- Is the modality EEG, iEEG, fMRI, MEG, LFP, spike, multimodal, or non-neural?
- Is the input modality separate from the biological signal modality?
- Is the task taxonomy separate from the paper-specific objective?
- Is the method family separate from the paper-specific method summary?
- Are dataset splits and subject/session protocols clear?
- Is the dataset role created, used, benchmark, cited-only, none-review, or unresolved?
- Are metrics comparable to the user's target claim?
- If the paper is a review, perspective, or theory article, is `metric_status` explicitly `not_applicable` instead of leaving `metric` unresolved?
- Do limitations come from an explicit author limitation, discussion caveat, or experimental boundary rather than generic motivation?
- Is the paper evidence strong enough for the claim being made?
