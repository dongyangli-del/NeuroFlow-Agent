# Proportional Execution Gate

Use this gate for every NeuroFlow task so optional confidence work does not displace the requested deliverable. It adapts the live-uncertainty and reachability ideas from [HERO Anti-OverDefense](https://github.com/wanshuiyin/HERO-Anti-OverDefense) to NeuroFlow's research-integrity boundaries.

## Core Rule

Keep one primary deliverable. Before adding a check, reviewer, specialist handoff, artifact, compatibility layer, or memory update, identify:

1. the uncertainty that is still live;
2. the supported input, consumer, claim, or failure it can affect; and
3. the next action that would change if the result fails.

Skip the addition when those answers are absent. A bounded class of failures is sufficient when a shared interface changed and the exact failing consumer is not knowable in advance. A path that already passed against unchanged code is settled.

## Scope Boundaries

- Treat documented inputs, public interfaces, and real project data as reachable even when they look rare. Merely constructible scenarios are not enough.
- Do not add hashes, checksums, or fingerprints unless they replace materially more expensive work and change execution, cache, integrity, lineage, or rollback decisions.
- Do not add feature flags, migration frameworks, wrappers, compatibility layers, audit trails, or permanent versions for unrequested futures or recoverable local failures.
- Use specialist modules or multiple agents only when they contribute distinct evidence or non-overlapping work. Do not fan out repeated reads or reviews.
- Treat full output templates as field menus. For a narrow request, emit only the fields needed to answer it.
- Create durable memory only for a reusable behavior change, changed scientific semantics, or a result whose lineage must remain reproducible.

## Required Work That Remains Required

This gate does not weaken explicit user, project, or higher-priority requirements. Preserve checks for real adversaries or untrusted inputs, privacy, data corruption, destructive actions, human-subject safety, train/test leakage, protocol validity, claim-evidence consistency, and final claim-bearing decisions. Existing integrity hashes that control execution or rollback are proportionate.

Run one targeted validation for the changed path. Use broader regression coverage when the change reaches a bounded set of shared consumers. Run independent review at the final consequential milestone when its result can change publication, promotion, release, or another high-risk decision.

## Stop Rule

Stop when the requested deliverable exists and the smallest relevant validation has passed. Report optional confidence work as a non-blocking suggestion instead of performing it. Say plainly when the result is correct; do not manufacture findings to justify a review.
