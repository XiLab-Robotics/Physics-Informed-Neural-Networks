# Causal Offset Mean Calibration Pilot Model Report

## Overview

This report documents the `causal_offset_mean_calibration` pilot prepared after
the shape-first distillation screen failed to improve the accepted
`polished_dataset` setpoint `Fw` baseline. The branch tests whether explicit
curve-mean / offset pressure can reduce the remaining measured-versus-predicted
vertical displacement without abandoning the two active development roads:
time-windowed temporal models and non-windowed harmonic models.

The pilot does not introduce a new PyTorch module. It reuses existing
repository-supported model families and loss hooks so the experiment stays
small enough for a bounded campaign decision.

## Model Description

The windowed arm uses `sequential_residual_offset_probe`. The model computes a
pointwise base transmission-error estimate from the selected readout position
of a short causal sequence and adds a recurrent residual-offset prediction from
the same causal history.

The non-windowed arm uses `periodic_mlp` with explicit sparse RCIM harmonic
features and the existing curve-aware training objective. This arm keeps a
PLC-friendlier non-windowed candidate active, even though it cannot use a
sequence-derived residual-offset branch.

## Operating Principle

The pilot is based on the evidence that the recent shape-first loss branches
did not beat the accepted GRU baseline after bounded `TE Curve Verification
Pipeline` screening. The remaining useful signal is therefore not another
stronger shape-only rule, but a narrower attempt to control curve mean and
offset while preserving shape fidelity.

The windowed model predicts:

```text
TE_prediction = base_point_prediction + residual_offset_prediction
```

The residual offset is causal because it is read from the same short sequence
window used during training and does not inspect future curve positions beyond
the configured readout contract.

## Conceptual Structure

- `base_branch`: point-level feedforward TE predictor at the sequence readout
  position.
- `residual_offset_branch`: GRU sequence branch that estimates the additive
  residual offset from the local causal window.
- `prediction_tensor`: final summed TE prediction consumed by the shared
  regression module.
- `residual_offset_prediction_tensor`: auxiliary tensor logged by the shared
  regression module as `residual_offset_mean_abs`.
- curve-aware loss terms: existing centered-shape, curve-offset, amplitude,
  and sparse harmonic terms used as training pressure.

## Project-Context Advantages

- Keeps the current best windowed path alive instead of discarding the GRU
  sequence family after the shape-first distillation failure.
- Tests offset control directly rather than inferring it only from
  post-training curve screens.
- Preserves a non-windowed harmonic comparator in the same campaign package, as
  required by the active model-selection policy.
- Reuses existing training infrastructure, reducing implementation risk.
- Keeps promotion gated by a later bounded `TE Curve Verification Pipeline`
  screen, not by scalar validation `MAE` alone.

## Project-Context Disadvantages

- The residual-offset branch can still overfit local curve context if the
  offset weight is too strong.
- The non-windowed arm has no sequence state and therefore cannot reproduce the
  exact causal residual-offset mechanism.
- A better validation `MAE` is insufficient evidence; the branch can only be
  accepted after visual and multi-index curve-first verification.
- The pilot is forward-only, so any positive result still needs `Bw` and
  broader dataset/input-mode follow-up before program-level promotion.

## Implemented Python Components

- `scripts/models/sequential_residual_offset_network.py`
  - `SequentialResidualOffsetNetwork`
  - `resolve_readout_feature_tensor`
  - `compute_auxiliary_output_dictionary`
  - `forward_with_input_context`
- `scripts/models/model_factory.py`
  - existing construction path for `sequential_residual_offset_probe`
  - existing construction path for `periodic_mlp`
- `scripts/training/transmission_error_regression_module.py`
  - existing curve-aware loss composition
  - existing residual-offset auxiliary logging
- `scripts/training/run_training_campaign.py`
  - existing campaign dispatch for both selected model types

## Acceptance Discipline

The campaign winner is not automatically promotable. Normal closeout must
produce the campaign leaderboard and best-run files, then a separate bounded
`TE Curve Verification Pipeline` screen must compare the pilot outputs against:

- `polished_setpoints_periodic_gru_sequence_Fw`
- `polished_setpoints_periodic_mlp_harmonic_Fw`

The screen must keep raw error, mean-centered shape, offset behavior, harmonic
evidence, robustness, visual plots, and deployment readiness separate.
