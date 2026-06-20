# RCIM Model-Bank Reproduction Exact-Paper LinearSVR Fallback Alignment

## Overview

The recovered-original RCIM workflow already carries a pragmatic fix for the
historical `SVR(kernel="linear")` branch:

- preserve the paper-faithful `SVR(kernel="rbf")` branch;
- replace the impractical linear branch with
  `Pipeline(StandardScaler(), LinearSVR(...))`; and
- serialize the selected `SVR` variant explicitly so `Retune`, `LoadBest`,
  `paper_eval`, and `paper_export` can rebuild the same estimator later.

The RCIM Model-Bank Reproduction exact-paper reimplementation does not yet carry that same
pragmatic fallback. Its shared exact-paper `SVR` surface still builds a single
homogeneous `SVR` estimator and still exposes the historical `linear` branch
through a plain `SVR` grid. That leaves the RCIM Model-Bank Reproduction `SVR` family vulnerable to
the same pathological runtime behavior that was already fixed in the recovered
original pipeline.

This task aligns the RCIM Model-Bank Reproduction exact-paper shared workflow with the already
accepted recovered-original `LinearSVR` fallback pattern, without changing the
overall mathematical search structure outside the `SVR(kernel="linear")`
branch.

## Technical Approach

The exact-paper shared support layer will adopt the same heterogeneous `SVR`
search surface already implemented in commit
`7654d8b1b0664dc50d463920dd571ec5b8b38bae` for the recovered-original
workflow.

The intended behavior is:

1. Keep the exact-paper default `SVR` base estimator as the paper-faithful
   `rbf` configuration.
2. Replace the exact-paper `SVR` hyperparameter grid with a two-branch
   parameter-list setup:
   - one paper-faithful `rbf` branch based on `SVR`;
   - one pragmatic linear branch based on
     `Pipeline(StandardScaler(), LinearSVR(...))`.
3. Serialize the winning `SVR` branch explicitly in the best-parameter summary
   and shared registry using the same variant metadata shape already used by
   the recovered-original workflow.
4. Normalize the exact-paper `loadbest`, `eval`, and `export` replay paths so
   they can rebuild either:
   - the paper-faithful `rbf` branch; or
   - the pragmatic linear fallback branch.
5. Keep the existing exact-paper operator flow, campaign queue structure, and
   artifact roots unchanged.

This is a RCIM Model-Bank Reproduction exact-paper quality-of-execution fix, not a redesign of the
broader paper-faithful workflow.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
  Shared exact-paper family registry, `SVR` grid definition, best-parameter
  serialization, and replay logic.
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py`
  Original-dataset exact-paper reporting surface that may need wording updates
  if `SVR` variant metadata becomes report-visible.
- `scripts/paper_reimplementation/rcim_ml_compensation/README.md`
  Canonical exact-paper operator README that documents the shared RCIM Model-Bank Reproduction
  workflow.
- `doc/guide/project_usage_guide.md`
  User-facing guide entry point if the exact-paper operator surface changes in
  a way that should be documented.
- `doc/running/active_training_campaign.yaml`
  Current campaign state reference. The current RCIM Model-Bank Reproduction paper-faithful
  umbrella campaign is already `cancelled`, so no active-run mutation is
  expected for this implementation.

No subagent is planned for this change.

## Implementation Steps

1. Compare the recovered-original `LinearSVR` fallback implementation against
   the exact-paper shared `SVR` family path and isolate the minimum reusable
   design.
2. Add the same `SVR` variant constants, branch builders, and heterogeneous
   grid-search payload to the exact-paper shared support layer.
3. Extend exact-paper best-parameter serialization and replay logic so stored
   summaries and registry entries can rebuild either `SVR` branch
   deterministically.
4. Update exact-paper operator documentation to state that the RCIM Model-Bank Reproduction `SVR`
   family now mirrors the recovered-original pragmatic linear fallback.
5. Run targeted verification on the exact-paper `SVR` path, including at least
   one `search`-side sanity check and one `loadbest` or `export` replay check.
6. Run Markdown QA on the touched repository-owned Markdown scope before
   closing the task.
