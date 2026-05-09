# RCIM Original SVR Pragmatic Linear Fallback

## Overview

This document plans one explicit deviation from the recovered-original RCIM
training protocol for the `SVR` family inside:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`

The preserved invariant is that the `rbf` branch must remain identical to the
recovered original search and tuned replay behavior. The deliberate deviation is
limited to the historical `SVR(kernel="linear")` branch, which has been shown
by temporary diagnostics to be operationally impractical on the recovered RCIM
dataset surface. That branch will be replaced by a pragmatic fallback based on:

- `Pipeline(StandardScaler(), LinearSVR(...))`

This change is not a paper-faithful replication and must be documented as such
in the workflow surface. The purpose is to preserve a practical linear-model
comparison branch for retuning and best-parameter replay without keeping the
pathological `SVR(kernel="linear")` solver behavior.

## Technical Approach

The implementation will keep the current recovered-original workflow shape and
modify only the `SVR` family internals where necessary.

For `retune`, the `SVR` parameter grid will be rewritten from one single
`SVR`-only dictionary into a list of two explicit search branches:

1. a paper-faithful `SVR(kernel="rbf")` branch with the original hyperparameter
   surface preserved;
2. a pragmatic linear fallback branch that swaps the underlying estimator to
   `Pipeline(StandardScaler(), LinearSVR(...))`.

This follows the supported `GridSearchCV` pattern for heterogeneous estimator
branches via a list of parameter dictionaries and nested `estimator__...`
parameter names.

The implementation also needs one repository-owned best-parameter serialization
layer. The current recovered workflow writes `str(self.model.best_params_)`
directly into the `summaryBestParameter+` CSV and later reloads it with
`ast.literal_eval(...)` plus `set_params(...)`. That contract is insufficient
once `best_params_` can contain an estimator object such as a `Pipeline`.

To keep the downstream stages runnable, the change will add:

- a stable serialized marker for the selected `SVR` variant;
- one reload path that reconstructs either:
  - the paper-faithful tuned `SVR(rbf)`, or
  - the pragmatic `StandardScaler() + LinearSVR(...)` fallback;
- backward-compatible handling for legacy non-`SVR` summary rows.

The implementation will also update the workflow README so operators can see
that:

- `SVR(rbf)` remains original-protocol;
- the linear branch is now a pragmatic fallback;
- retune-derived best-parameter replays can therefore select one of two
  explicitly documented `SVR` variants.

## Involved Components

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/technical/2026-05/2026-05-09/2026-05-09-13-13-36_rcim_original_svr_linear_retune_temp_diagnostics.md`

No subagents are planned for this implementation. If subagent use becomes
useful later, it will require a separate explicit approval before launch.

## Implementation Steps

1. Replace the current recovered-original `SVR` retune grid with a two-branch
   `GridSearchCV` surface that preserves the historical `rbf` branch and swaps
   the historical `linear` branch to `Pipeline(StandardScaler(), LinearSVR(...))`.
2. Add one explicit normalization and serialization path for `SVR`
   `best_params_` so `summaryBestParameter+` can encode the chosen branch
   without storing non-literal estimator objects.
3. Extend the tuned-parameter reload path in `training_models.py` so
   `paper_eval`, `paper_export`, and `LoadBest` can reconstruct the correct
   `SVR` variant from the serialized retune summary.
4. Update the recovered-original workflow README to document this as a
   pragmatic fallback and not as an exact-paper replication.
5. Run focused validation on the touched Python and Markdown surfaces,
   including at least one temporary `SVR` retune smoke check that proves the
   new linear fallback branch terminates.
