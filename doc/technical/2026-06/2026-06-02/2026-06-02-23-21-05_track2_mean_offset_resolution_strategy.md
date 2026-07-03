# TE Curve Verification Pipeline Mean Offset Resolution Strategy

## Overview

This document plans a documentation update to the curve-first TE training
strategy after the `TE Curve Verification Pipeline` mean-centered diagnostic committed in
`940a16b934e29ca83fef36da010fdf671bdd52c4`.

The new diagnostic confirms that persistent vertical prediction offset is a
material part of the observed `TE Curve Verification Pipeline` curve error for many candidates. The
clearest example is `harmonic_regression_global`, whose four-curve collage
average `MAE` drops from `0.031130` deg to `0.000888` deg after subtracting the
truth and prediction curve means independently. Several temporal global
candidates also improve strongly after mean-centering, while dense `Wave 2.3`
residual-harmonic temporal variants improve much less.

The planned update will extend the curve-first strategy introduced by commit
`b73220679410276246421b7e2832d8878cff90a0` so future work explicitly separates
mean offset, centered shape, amplitude, and phase behavior.

## Technical Approach

The documentation update should record the current interpretation:

- current neural training optimizes pointwise normalized `MSE`;
- current batches concatenate points or causal sequence windows from multiple
  curves and may shuffle those points or windows inside the batch;
- this setup can encourage a conditional-average prediction when the model
  does not receive enough information to distinguish each curve's mean offset;
- the result is a plausible under-prediction of high-mean curves and
  over-prediction of low-mean curves on the `TE Curve Verification Pipeline` playback surface;
- the solution is not to make non-causal full curves into model inputs, but to
  make training and validation losses aggregate causal predictions at curve
  level.

The update should preserve the existing causal runtime contract: a deployable
model may consume only the current point-level state, optional short causal
history, or causal derived features.

## Involved Components

The approved implementation should update these documentation surfaces:

- `doc/reports/analysis/te_modeling/strategy/Curve-First TE Training Strategy.md`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
- `doc/running/te_model_live_backlog.md`
- `doc/README.md`

The update should cite these existing evidence sources:

- commit `b73220679410276246421b7e2832d8878cff90a0`;
- commit `940a16b934e29ca83fef36da010fdf671bdd52c4`;
- the mean-centered report under
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/mean_centered_collage_report/[2026-06-02]/`;
- the current training module and datamodule loss/batch behavior.

## Implementation Steps

1. Add a dedicated section to the curve-first strategy explaining the mean
   offset failure mode and why pointwise `MSE` can favor curve-mean averaging.
2. Record the `TE Curve Verification Pipeline` mean-centered diagnostic findings, including the
   numeric `harmonic_regression_global` example and the dense `Wave 2.3`
   counterexample.
3. Add the next diagnostic step: full-matrix curve decomposition into mean
   offset, centered shape error, amplitude error, harmonic phase error, and
   operating-condition dependence.
4. Add the next training step: curve-aware loss terms that combine pointwise
   `MSE`, curve-level bias loss, centered shape loss, derivative loss, and
   selected harmonic amplitude/phase loss.
5. Add the model-architecture options:
   - a multi-task or multi-head model with separate offset and shape heads;
   - a sequential residual calibration model that learns the offset left by a
     frozen base model;
   - a spectral or mean-independent metric used as a shape component, not as
     the only objective.
6. Update the master summary and live backlog so the next plan is a `CVP 1.4`
   offset-source audit before launching new training.
7. Run scoped Markdown QA on the touched authored Markdown files.
