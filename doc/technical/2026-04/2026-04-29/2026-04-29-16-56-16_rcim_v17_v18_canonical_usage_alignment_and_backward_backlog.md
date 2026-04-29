# 2026-04-29-16-56-16 Rcim V17 V18 Canonical Usage Alignment And Backward Backlog

## Overview

The RCIM original-pipeline documentation currently captures the recovered code
surface and the author conversation, but one interpretation detail now needs to
be tightened.

The user clarified the canonical operational reading to follow faithfully from
the author-supplied `README.md` under:

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`

That reading is:

- `0-main_createDFforPrediction.py` creates the `Fw` or `Bw` dataframe with
  automatic `.pickle` reuse/creation;
- `1.1-main_prediction_v17.py` is the structure used for full-dataset model
  export;
- `predictorMLCrossValidationWithHyperparameter(...)` is the tuning path to
  enable when starting from the `v17` structure on a changed or restricted
  dataset;
- `1-main_prediction_v18.py` is the structure used to reproduce the paper-side
  `80/20` training and validation flow with already optimized hyperparameters;
- `2-main_evaluatePrediction_v4.py` generates the paper evaluation tables from
  `output_prediction`.

The same clarification should also be reflected in the future backward plan:

- the current shipped artifacts remain `Fw`-centric;
- a future `Bw` branch should mirror the same operational sequence:
  dataframe generation, tuning from the `v17` structure, then paper-style
  replay from the `v18` structure with the found hyperparameters.

## Technical Approach

The documentation pass should do two things.

First, align the recovered-asset reports with the stricter canonical usage
reading above. In particular, the reports should stop implying that `v18`
itself is ambiguous in role when the shipped `README.md` already states the
intended usage order clearly.

Second, update the live backlog so the future backward implementation is not
left as an implicit idea in chat history. The backlog should explicitly record:

- current state: shipped assets and evaluation are still `Fw`-shaped;
- future `Bw` plan: reuse the same `v17 -> tuning -> v18` operational logic;
- repository consequence: the future runner-backed reimplementation should keep
  output folders and artifact placement normalized instead of relying on
  mutable local original paths.

The pass should preserve important evidence distinctions:

- file-level diffs still matter for forensic comparison;
- but the canonical operator guidance should follow the author `README.md`
  unless later execution evidence disproves it.

## Involved Components

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/README.md`
- `doc/reports/analysis/RCIM Recovered Asset Deep Analysis.md`
- `doc/reports/analysis/RCIM Original Pipeline To Reimplementation Companion.md`
- `doc/reports/analysis/RCIM Original Pipeline And Reimplementation Audit.md`
- `doc/running/te_model_live_backlog.md`
- `doc/technical/2026-04/2026-04-29/README.md`
- `doc/README.md`

## Implementation Steps

1. Re-read the author-supplied `original_pipeline/README.md` and treat it as
   the canonical operator-facing usage note for `v17`, `v18`, tuning, and
   paper reproduction.
2. Update the main RCIM recovered-asset analysis reports so they reflect the
   canonical reading:
   - `v17` for full-dataset export;
   - `v17` plus `predictorMLCrossValidationWithHyperparameter(...)` for future
     retuning on changed datasets;
   - `v18` for paper-style `80/20` replay with optimized hyperparameters.
3. Reduce overstated ambiguity language where the current report text is
   stronger than the evidence now justifies.
4. Add an explicit future backward note in the live backlog describing the
   planned `Bw` mirror path and the fact that current shipped artifacts remain
   forward-centered.
5. Run Markdown QA on all touched Markdown files before closing the task.
