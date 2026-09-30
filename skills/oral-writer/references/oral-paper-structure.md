# Oral Paper Structure

An oral-level paper needs a compressed thesis and a visible evidence chain.

## Thesis Template

```markdown
This paper shows that [method or principle] improves [specific task] under [specific setting] because [mechanism], supported by [key evidence], while limited by [boundary].
```

## Contribution Stack

1. Problem: what is hard and why current workflows fail.
2. Gap: the closest prior work and the missing capability.
3. Method: the minimal technical idea, not a component inventory.
4. Evidence: the main table, ablations, robustness, and error analysis.
5. Boundary: where the claim does not apply.

## Logic Chain Gate

Before writing prose, verify the paper chain:

```text
research setting
-> limitation in closest prior work
-> key principle or goal
-> concrete challenges
-> method modules or experimental design choices
-> evidence
-> contributions
```

Every limitation should motivate the key principle. Every challenge should arise from implementing that principle. Every module, experiment, and figure should map to a challenge or contribution. If this chain breaks, fix the project structure before polishing language.

## Figure Narrative Gate

Each main figure should have one job:

- motivated example: expose the research problem or failure mode;
- method overview: show the mechanism at the same abstraction level as the method section;
- experimental result: carry one finding with comparable baselines and uncertainty;
- analysis figure: explain behavior, neural representation, error type, or failure mode;
- closed-loop or embodied figure: separate offline training, online interaction, feedback, and safety boundaries.

Require a first-sentence caption takeaway, labels that match paper terminology, and a visible mapping from figure panels to claims.

## Writing Rules

- Use concrete nouns and active structure.
- Put novelty in relation to closest prior work.
- Make each paragraph do one job.
- Replace inflated adjectives with measured evidence.
- Keep limitations visible and scoped.
