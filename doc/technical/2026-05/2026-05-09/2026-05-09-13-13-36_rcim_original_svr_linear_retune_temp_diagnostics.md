# RCIM Original SVR Linear Retune Temporary Diagnostics

## Overview

This document plans a temporary diagnostic pass for the recovered-original
RCIM `SVR` backward retune path that appears to stall on the `linear` kernel
branch while the `rbf` branch completes quickly.

The work will stay outside the canonical workflow implementation. All new
diagnostic scripts will be created under `temp/` and treated as disposable.
The goal is to answer three concrete questions before any durable workflow
change is proposed:

1. Does a minimal mixed `rbf` plus `linear` `SVR` search terminate cleanly on
   the recovered-original dataset?
2. If it does terminate, what runtime can be extrapolated for the original
   `48`-candidate `SVR` retune search?
3. If the `linear` branch remains impractical, is there a regression-appropriate
   alternative such as `LinearSVR` worth evaluating as a diagnostic proxy?

## Technical Approach

The diagnostic pass will compare the recovered original pipeline and the
repository reimplementation without mutating either code path.

Step 1 will create a temporary Python harness under `temp/` that loads the same
runtime dataframe used by the recovered-original workflow, reconstructs the
same `SVR` multi-output wrapper surface, and runs a very small search grid with
only a few `rbf` and `linear` candidates. The harness will print timestamps,
per-candidate progress, and coarse fit timing so that the operator can see
whether the `linear` candidates terminate or remain pathologically slow.

Step 2 will extend the temporary harness to run a controlled series of broader
`SVR` search subsets and estimate the runtime of the original `48`-candidate
search from measured elapsed times instead of from theoretical fit counts
alone.

Step 3 will add an optional temporary comparison branch for regression-only
alternatives. Per the scikit-learn regression documentation, the relevant
alternative is `LinearSVR`, not classification `SVM` classes. Any such
comparison will remain explicitly diagnostic and will not be promoted into the
canonical workflow during this task.

No changes will be made to:

- `scripts/campaigns/paper_reference/rcim_original/`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`
- `doc/running/active_training_campaign.yaml`

## Involved Components

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`
- `temp/`
- `doc/reports/campaign_plans/mixed_training/2026-05-09-13-13-36_rcim_original_svr_linear_retune_temp_diagnostics_plan.md`

## Implementation Steps

1. Create a temporary diagnostic harness in `temp/` that reproduces the
   recovered-original `SVR` multi-output search path on the canonical backward
   dataframe with a tiny mixed `rbf` plus `linear` grid.
2. Run the tiny-grid diagnostic and collect elapsed times, completion status,
   and any warnings or exceptions.
3. If the tiny-grid diagnostic completes, run one or more slightly larger
   temporary grids and estimate the runtime of the original `48`-candidate
   search from measured timings.
4. If the `linear` branch remains impractical, add a separate temporary
   diagnostic script comparing `SVR(kernel="linear")` and `LinearSVR` on the
   same regression surface.
5. Summarize the findings and propose either:
   - a runtime-based decision that the original `SVR` search is feasible, or
   - a follow-up durable fix proposal for the canonical workflow.
