# Paper Reference Alignment And Gap Tracking

## Overview

This task formalizes a repository-owned reference package around the paper
`reference/RCIM_ML-compensation.pdf` so the project can track its current
position against the paper baseline in a clear and reusable way.

The requested outcome is broader than a one-off comparison note. The
repository needs:

1. a canonical reference report that extracts and organizes the paper metrics,
   target conditions, model-selection conclusions, and deployment constraints;
2. a dedicated `paper vs repository` comparison section inside the canonical
   training-results master summary;
3. explicit paper-derived targets in the live backlog;
4. a roadmap update that plans the missing implementation and validation
   pipelines required to reproduce the paper inside this repository.

The same task should also state clearly which pipeline components are still
missing before the repository results become truly comparable with the paper's
Table 9 online-compensation benchmark.

## Technical Approach

The implementation should create one new analysis report under
`doc/reports/analysis/` dedicated to the paper reference baseline. That report
should be human-readable, colleague-facing, and easy to reuse during reviews,
planning, and presentations.

The report should include at least:

1. guided reading notes for the paper;
2. extracted paper metrics and test conditions;
3. minimum practical targets the repository should reach;
4. the paper model-selection conclusions, especially the boosting/tree-heavy
   pattern visible in the harmonic-level selection;
5. an evidence-grounded comparison between the paper baseline and the current
   repository results;
6. a prepared dedicated section for online-compensation validation and
   `Table 9`-style tracking, even if it initially records that the repository is
   not yet comparable online;
7. an explicit missing-pipeline section that explains why the current
   repository does not yet have a like-for-like Table 9 comparison.

The canonical `doc/reports/analysis/Training Results Master Summary.md` should
then be extended with a dedicated reference-benchmark section containing:

- extracted paper targets;
- a compact `paper vs repository` comparison table;
- a running statement of whether each paper-aligned target is currently met,
  not yet met, or not yet comparable;
- an explicit distinction between the currently comparable offline benchmark
  scope and the still-missing online-compensation benchmark scope.

The live backlog in `doc/running/te_model_live_backlog.md` should be updated
to make the paper-derived targets operational. In particular it should record:

- `Target A`: match or beat the paper on the comparable prediction benchmark;
- `Target B`: reproduce the online compensation benchmark and reach at least
  `83%` robot RMS reduction and `90%` cycloidal RMS reduction.

The repository rules should also be updated so future online-compensation
results explicitly refresh both:

- the new paper-reference analysis report;
- `doc/reports/analysis/Training Results Master Summary.md`.

Until online-compensation validation exists in the repository, the comparison
should be stated explicitly as an offline-only comparison rather than an
end-to-end paper-equivalent benchmark.

The roadmap should also be expanded so future waves explicitly cover the
missing paper-aligned implementation path: harmonic-component prediction,
TwinCAT-ready export/integration path, compensation-loop validation, and
motion-profile reproduction.

No subagent is planned for this implementation. The task is tightly coupled to
repository-owned references, reports, and backlog state.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/analysis/`
- `doc/running/te_model_live_backlog.md`
- `doc/README.md`
- `site/reports/`

## Implementation Steps

1. Create a canonical analysis report that extracts the paper baseline and
   organizes its metrics, target conditions, and implementation implications.
2. Extend the canonical training-results master summary with a dedicated
   `paper vs repository` benchmark section.
3. Prepare the new paper-reference report with a dedicated online-compensation
   results section that can later be updated when real online tests are
   implemented.
4. Update the live backlog with explicit `Target A` and `Target B` paper
   milestones and with the tests required to validate them.
5. Expand the wave roadmap so the remaining paper-aligned pipelines are
   planned explicitly inside the repository execution path.
6. Update the repository rules so future online-compensation results must
   refresh both the new paper-reference report and the canonical master
   summary.
7. Update the documentation index and Sphinx-facing report entry points as
   needed.
8. Run the required Markdown checks on the touched Markdown scope.
9. Report completion and wait for explicit approval before creating any Git
   commit.
