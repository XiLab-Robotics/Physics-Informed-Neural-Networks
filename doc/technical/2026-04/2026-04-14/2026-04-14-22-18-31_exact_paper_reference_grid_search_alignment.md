# Exact Paper Reference Grid Search Alignment

## Overview

The current `exact-paper` RCIM model-bank workflow uses recovered paper-side
base estimators, but it does not yet reproduce the original reference-code
hyperparameter-search path. In particular, `SVR` is instantiated with the
recovered base values (`C=1`, `epsilon=0.0001`, `gamma=1.1e-06`,
`kernel='rbf'`) and then fit directly, while the recovered paper code wraps the
family estimator with `GridSearchCV` and family-specific parameter grids before
training.

This task aligns the repository workflow with the paper more faithfully by
implementing the reference `GridSearchCV` path in the `exact-paper` branch and
by structuring that behavior so future paper families can use the same
reference-backed training pattern instead of repository-invented tuning sweeps.

## Technical Approach

The implementation will promote the recovered reference-code behavior to a
first-class workflow component inside the repository exact-paper branch.

The change will follow these rules:

- keep the paper-recovered base estimator definitions as the default estimator
  seeds;
- add a reference-backed family-to-grid resolver that reproduces the parameter
  grids found in the recovered code snapshots;
- add an exact-paper training mode that wraps each family estimator with
  `GridSearchCV` before the `MultiOutputRegressor` fit path, instead of fitting
  the base estimator directly;
- preserve deterministic repository behavior by keeping explicit split control
  and explicit serialized summary fields for the chosen search configuration;
- make the `GridSearchCV` path reusable across `SVR`, `MLP`, `RF`, `DT`, `ET`,
  `ERT`, `GBM`, `HGBM`, `XGBM`, and `LGBM`, but only with parameter grids that
  are actually justified by the recovered paper reference code.

The first implementation target is `SVR`, because it is the family where the
gap between current repository behavior and the reference pipeline is already
confirmed. The code structure will be generalized so the remaining families can
be migrated into the same paper-faithful path without redesigning the training
workflow again.

## Involved Components

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/1-prediction/1-predictorML_v7.py`
  Reference source for the original `GridSearchCV` path and family-specific
  parameter grids.
- `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/predictorML_v7.py`
  Supporting recovered snapshot for cross-checking the later paper-era grid
  definitions.
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
  Current exact-paper training support module where base estimators are created
  and trained.
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
  Main exact-paper workflow entry point that must preserve repository artifact
  and reporting behavior after the tuning-path change.
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/`
  Exact-paper configuration surface, expected to gain an explicit switch for
  paper-reference hyperparameter search behavior.
- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`
  Explanatory report that should be kept semantically aligned once the workflow
  becomes truly `GridSearchCV`-backed instead of base-estimator-only.

## Implementation Steps

1. Extract the recovered `GridSearchCV` grids and training pattern from the
   original and latest recovered predictor code, starting with `SVR` and then
   mapping the remaining supported families.
2. Refactor the exact-paper support module to separate:
   base estimator creation,
   paper-reference parameter-grid resolution,
   and optional `GridSearchCV` wrapping.
3. Add configuration-controlled exact-paper search behavior so the repository
   can run the true paper-faithful path explicitly and serialize the chosen
   search mode in validation outputs.
4. Update exact-paper reporting so the produced Markdown summaries expose
   whether a family was trained with direct recovered hyperparameters or with
   recovered reference `GridSearchCV`.
5. Validate the changed workflow on at least the `SVR` branch and confirm that
   the resulting exact-paper path now matches the reference-code training logic
   much more closely than the current seed/split-only repair campaigns.
