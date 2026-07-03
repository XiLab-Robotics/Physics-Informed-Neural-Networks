# Curve-First TE Training Strategy

## Overview

The repository now has enough evidence to separate two ideas that were
previously coupled:

- pointwise dataset accuracy, usually reported as scalar `MAE` or `RMSE`;
- full TE-curve tracking quality on the direction-valid `TE Curve Verification Pipeline` held-out
  surface.
- curve mean / `DC` offset tracking versus mean-centered waveform shape
  tracking.

The final application is continuous Transmission Error compensation. A deployed
predictor will run through many consecutive motor revolutions, so the useful
offline question is not only whether a single dataset sample has a low absolute
error. The useful question is whether the predicted TE curve preserves the
measured waveform over repeated cycles under the right speed, torque,
temperature, direction, angular-position, and `DataValid` conditions.

This report defines the curve-first strategy for the next training and
selection work. It is a planning and analysis document, not a completed
training campaign.

## Causal Input Contract

Curve-first selection does not change the runtime input contract.

The real TestRig / TwinCAT predictor must remain causal. At inference time the
model can consume only:

- the current point-level operating state;
- a short historical window of already observed samples, when the selected
  family explicitly supports a sequence input;
- derived features computed from the current point and past samples.

The model must not require a future TE sample, a future angular sample, or a
complete future revolution curve as input. Curve-first means that training,
validation, and promotion aggregate the model's causal predictions over
complete held-out curves to judge compensation quality. It does not mean that
the dataset is redesigned so the model sees the full curve in advance.

This also constrains future feature engineering:

- harmonic features are allowed when computed from current angular position
  and known operating variables;
- derivative or history features are allowed only if they use past samples;
- future-looking smoothing, centered windows that include future points, and
  full-curve normalization unavailable at runtime are not deployment-valid
  model inputs.

## Current Evidence

### Repository Facts

Current training and registry infrastructure still promotes best runs with the
shared scalar policy:

- primary metric: `test_mae`;
- first tie-breaker: `test_rmse`;
- second tie-breaker: `val_mae`;
- third tie-breaker: trainable parameter count.

`TE Curve Verification Pipeline`, however, already evaluates candidates on complete held-out TE
curves. The official matrix uses:

- `194` held-out curves before candidate filtering;
- direction-valid evaluation for `Fw`, `Bw`, and `global` candidates;
- per-curve `MAE`, `RMSE`, mean percentage error, and P95 percentage error;
- visual collages and multi-model overlays for local waveform inspection.

The current `Wave 1` closeout shows the risk clearly. The scalar HPO leader is
`tree_fw` with test `MAE = 0.002743 deg`, but the TE Curve Verification Pipeline visual reports are
the correct surface for judging whether the model follows the TE waveform well
enough for compensation.

The `Wave 2.2` periodic sequence branch is the strongest current
repository-owned neural branch in TE Curve Verification Pipeline. `Wave 2.3` confirms another important
point: sparse `RCIM` harmonic structure helps, while dense `240` and dense
`360` residual harmonic variants over-expand the basis and are not
competitive on the official TE Curve Verification Pipeline curve surface.

### Mean-Centered TE Curve Verification Pipeline Evidence

The mean-centered curve-verification collage diagnostic is now the strongest evidence that
raw pointwise error mixes at least two different failure modes:

- per-curve vertical offset error;
- mean-centered shape error.

Canonical report:

- `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/mean_centered_collage_report/[2026-06-02]/track2_mean_centered_collage_report.md`

Key observed signal:

- `harmonic_regression_global` four-curve collage MAE improves from
  `0.031130 deg` to `0.000888 deg` after subtracting each curve mean from
  prediction and truth, a `97.1%` improvement;
- `periodic_lstm_sequence_global`, `periodic_temporal_convolution_global`, and
  `periodic_gru_sequence_global` also improve strongly after mean-centering;
- dense `Wave 2.3` residual harmonic variants improve much less, which means
  their issue is not only offset but also centered shape quality.

This is diagnostic evidence only. Mean-centering with the full truth curve is
not a deployment-valid runtime correction, because the deployed predictor will
not know the future curve mean. It does, however, show that future training and
selection must measure mean offset and shape separately.

### Mean Offset Failure Mode

The current neural training path optimizes normalized pointwise MSE. For
pointwise batches, the data module concatenates samples from selected curves
and may shuffle the points within the batch. For sequence batches, the model
sees causal windows, but the checkpoint objective is still pointwise. This is
valid for a pointwise regression objective, but it does not explicitly tell the
model that a complete held-out revolution has a curve-level mean that must be
matched.

The suspected mechanism is therefore not that random mini-batches are
incorrect. The issue is that pointwise `MSE` and `RMSE` reward the conditional
average prediction when the input features do not encode enough information to
identify the per-curve offset. In TE Curve Verification Pipeline playback this appears as
under-prediction on high-mean TE curves and over-prediction on low-mean TE
curves. Global target normalization can reinforce the visual tendency toward a
global center, but it is not the root cause by itself because denormalization
restores the global scale.

The next work should decompose each candidate's residuals before changing
training:

- `bias_c = mean(prediction_c - truth_c)`;
- centered residual after removing `bias_c`;
- peak-to-peak and amplitude error;
- selected harmonic amplitude and phase error;
- dependence of each component on speed, torque, temperature, direction, and
  valid-window identity.

### Reference-Backed Constraints

The RCIM compensation reference frames the real target as online TE prediction
and TwinCAT compensation, not only offline tabular regression. It keeps speed,
torque, oil temperature, direction, and angular position as first-class
variables.

The data-series reference also matters: TE is defined on valid steady-state
segments selected by `DataValid`. Any future curve-first split, loss, or
evaluation protocol must preserve that valid-window meaning.

The TwinCAT-friendly modeling synthesis adds a deployment constraint: the
candidate should preserve a credible path to inspectable, stable compensation.
That favors harmonic, periodic, and hybrid structured predictors over opaque
models when scalar performance is close.

## External Technique Review

### Curve-Level Reranking

The lowest-risk improvement is not a new algorithm. It is to rerank existing
candidate artifacts on the full TE Curve Verification Pipeline curve surface before accepting a
family best or program best.

Recommended metrics:

- mean per-curve `MAE`;
- mean per-curve `RMSE`;
- mean percentage error normalized by curve peak-to-peak truth;
- P95 and worst-condition percentage error;
- direction-separated `Fw`, `Bw`, and `global` summaries;
- count of unacceptable curves above a project-defined threshold.

This strategy is directly compatible with the existing TE Curve Verification Pipeline scripts and can
be applied to `Wave 1`, `Wave 2.1`, `Wave 2.2`, and `Wave 2.3` without retraining.

### Shape-Aware Diagnostics

Pointwise `MAE` can hide visually poor curve behavior. The next diagnostics
should measure curve shape explicitly:

- first-derivative error for local slope;
- second-derivative or curvature error for oscillation shape;
- peak and trough location error;
- peak-to-peak amplitude error;
- phase offset on selected harmonics;
- local correlation between predicted and measured curves;
- residual autocorrelation along the angular coordinate.

These metrics should first be diagnostic and promotion-facing. Only after they
are stable should they become training losses.

### Frequency And Harmonic Metrics

TE is strongly periodic in angular position, and the RCIM paper works through
harmonic amplitude and phase terms. A curve-first benchmark should therefore
add harmonic-space diagnostics:

- amplitude error on the sparse `RCIM` harmonic set;
- phase error on the sparse `RCIM` harmonic set;
- weighted error on the high-value harmonics used by the paper reference;
- spectral leakage outside the selected harmonic bank;
- low-frequency bias versus high-frequency tracking gap.

This class is especially relevant because neural networks can show spectral
bias toward low-frequency functions. Frequency-aware diagnostics explain why a
model may achieve acceptable average error while smoothing out important TE
oscillations.

A spectral or harmonic metric that removes the `DC` term is useful as a
mean-independent shape score, but it cannot replace an offset metric. The
promotion surface should report both:

- explicit `DC` / curve-bias error;
- non-`DC` harmonic amplitude and phase error for centered waveform quality.

Relevant sources:

- [On the Spectral Bias of Neural Networks](https://proceedings.mlr.press/v97/rahaman19a)
- [Fourier Features Let Networks Learn High Frequency Functions in Low
  Dimensional Domains](https://papers.nips.cc/paper_files/paper/2020/hash/55053683268957697aa39fba6f231c68-Abstract.html)

### Differentiable Time-Series Losses

Soft-DTW and DILATE show that deep models can be trained with differentiable
time-series shape objectives instead of plain pointwise loss.

Relevant sources:

- [Soft-DTW: a Differentiable Loss Function for Time-Series](https://proceedings.mlr.press/v70/cuturi17a.html)
- [Shape and Time Distortion Loss for Training Deep Time Series Forecasting
  Models](https://papers.neurips.cc/paper/by-source-2019-2368)

These methods are useful candidates, but they are not the first recommended
implementation for TE compensation. DTW-style losses are designed to tolerate
time shifts and dilations. In this project, physical phase matters: a predictor
that looks good only after temporal warping may still compensate at the wrong
angle. Therefore:

- do not use DTW or Soft-DTW as the primary promotion metric;
- if tested, use a constrained or low-weight term only;
- always keep phase-preserving curve metrics and harmonic phase error ahead of
  any warp-tolerant metric.

### Functional Curve Regularization

Functional data analysis supports the idea of treating each TE revolution as a
curve rather than as disconnected samples. Roughness-penalized curve fitting
uses derivative penalties to control slope and curvature.

Relevant source:

- [Roughness regularization for functional data analysis with free knots spline
  estimation](https://link.springer.com/article/10.1007/s11222-024-10474-w)

For this repository, that suggests two practical directions:

- add derivative and curvature diagnostics for TE Curve Verification Pipeline;
- test loss terms that penalize physically implausible oscillation roughness
  without smoothing away valid high-frequency harmonic content.

### Multi-Curve And Multi-Output Forecast Framing

The real compensation workflow is not a one-point forecast. It is a repeated
curve-output problem. Multi-step forecasting literature distinguishes recursive
prediction, direct prediction, and multiple-output strategies. Multiple-output
strategies preserve dependencies between future points, while recursive
strategies can accumulate errors.

Relevant source:

- [Stratify: unifying multi-step forecasting
  strategies](https://link.springer.com/article/10.1007/s10618-025-01135-1)

Repository implication: do not evaluate future temporal models only as
single-readout regressors if the deployment target requires continuous curve
compensation. Either evaluate full curve playback directly or add a multi-curve
offline playback test before promotion. This is an evaluation requirement, not
permission to feed future curve values to the runtime model.

## Direction-Parallel Best Policy

The real model program needs three best-model surfaces, not one absolute
winner:

| Surface | Required best model | Operational meaning |
| --- | --- | --- |
| `Fw` | best forward model | compensation candidate for forward motion only |
| `Bw` | best backward model | compensation candidate for backward motion only |
| `global` | best combined-surface model | deployable cross-direction model or fallback |

These surfaces must move in parallel. A strong `Fw` result cannot close the
`Bw` or `global` branch, and a strong `Bw` result cannot close the `Fw` or
`global` branch. Curve-first reports should therefore identify leaders per
surface and avoid language that turns the comparison into one single
competition.

## Recommended Strategy

### Phase 1: Standardize Curve-First Selection

Status: completed through `CVP 1.1` and `CVP 1.2`.

The completed `CVP 1.1` and `CVP 1.2` branches did not train new models.
They:

1. evaluate all existing accepted candidates on the same TE Curve Verification Pipeline held-out
   curves;
2. compute the expanded curve-first metric bundle;
3. rerank existing `Wave 1`, `Wave 2.1`, `Wave 2.2`, and `Wave 2.3` candidates;
4. write a promotion table that separates scalar registry winners from
   curve-first leaders for `Fw`, `Bw`, and `global`;
5. update the master summary so best-model status is not read from scalar
   `test_mae` alone and is not collapsed into one surface.

This directly answers the operator concern without spending training time on
an objective that is not yet standardized.

### Phase 2: Run CVP 1.4 Mean-Offset Full-Matrix Audit

This is the immediate next step before any new training campaign.

`CVP 1.4` should apply the mean-centered diagnostic to the official TE Curve Verification Pipeline
matrix rather than only to the small collage subset. It should produce one
row per candidate, surface, direction, and curve group with:

- raw per-curve `MAE` and `RMSE`;
- curve residual mean / `DC` offset;
- centered per-curve `MAE` and `RMSE`;
- raw-to-centered improvement percentage;
- peak-to-peak amplitude error;
- selected harmonic amplitude and phase error;
- condition-stratified summaries by speed, torque, temperature, direction, and
  `DataValid` window.

The output should identify whether a model family is offset-limited,
shape-limited, amplitude-limited, phase-limited, or condition-regime-limited.
Only after this classification should retraining be planned.

### Phase 3: Add Offset-Aware Checkpoint Selection

After CVP 1.4, update training infrastructure so neural checkpoints can be
selected by validation curve metrics instead of only `val_mae`.

Candidate monitor:

- `val_curve_bias_abs_mean_deg`;
- `val_curve_centered_mae_deg`;
- `val_curve_mean_percentage_error_pct`;
- tie-breakers: `val_curve_p95_percentage_error_pct`,
  `val_curve_harmonic_phase_error`, then scalar `val_mae`.

This phase affects `scripts/training/train_feedforward_network.py`,
`scripts/training/transmission_error_regression_module.py`, and shared
registry snapshots. It also requires a curve id or point-to-curve index in the
validation batch so post-forward aggregation can compute per-curve metrics.
It requires a dedicated technical document and campaign plan before training.

### Phase 4: Add Curve-Aware Losses

Only after CVP 1.4 and offset-aware checkpoint selection should retraining
change the loss.

Recommended first composite loss for neural families:

```text
total_loss =
  lambda_point * pointwise_normalized_mse
  + lambda_bias * mean_curve_residual_mse
  + lambda_shape * centered_curve_mse
  + lambda_slope * first_derivative_mae
  + lambda_harmonic_amp * selected_harmonic_amplitude_mae
  + lambda_harmonic_phase * selected_harmonic_phase_mae
```

Use small weights first. The loss should improve curve tracking without
destroying the stable pointwise baseline.

The loss implementation must still operate on causal predictions. It may
aggregate consecutive predictions into curve-level terms after the forward
pass, but it must not make non-causal future samples part of the input tensor
for a deployed candidate.

Soft-DTW or DILATE can be an ablation, but not the main line, because
warp-tolerant shape matching may hide physically harmful phase shifts.

### Phase 5: Test Offset/Shape Model Structures

Status: partially completed by `Wave 3.1`.

`Wave 3.1` implemented and trained the first learned sequential residual-offset
probe across `global`, `Fw`, and `Bw`. That branch is a clean non-harmonic
baseline: it uses a feedforward readout branch plus a causal recurrent
residual branch, but it does not force periodic `sin`/`cos` features, `RCIM`
harmonic indices, or a structured harmonic base.

This result is important even if it is not the shape-leading family. It shows
what a causal non-harmonic offset/residual structure can do under the current
input contract, and it should remain in future comparisons when new curve
indices, multi-head training, or composite losses are introduced.

If CVP 1.4 confirms that the model families are systematically offset-limited,
the next training structures should be evaluated before opening a broad new
model family wave:

- multi-task / multi-head model: shared causal feature trunk with one head for
  curve offset or low-frequency component and one head for centered waveform
  shape, summed into the final TE prediction;
- sequential residual calibration: first run the current best causal model,
  then train a second causal residual or offset calibrator on the prediction
  error using only deployment-valid inputs and past predictions.
- harmonic-offset hybrid: explicit harmonic or periodic shape branch plus a
  separate causal offset, bias, or amplitude branch.

Both structures keep the same runtime data contract. They do not feed a future
curve to the model. Their purpose is to prevent the offset component and the
periodic shape component from competing inside one scalar pointwise objective.

Future campaigns should keep a Wave 3.1-like clean baseline in parallel with
the harmonic-offset candidates. That baseline is required to distinguish gains
from the new objective or multi-head split from gains caused only by forced
harmonic features.

### Phase 6: Decide Whether A New Wave Is Needed

If CVP 1.4 shows that existing harmonic or periodic models are
already better curve-first candidates than the scalar leader, retrain only the
promising families with the new selection policy.

If curve-aware losses and offset/shape structures still fail, then open a
later model-family wave. Good candidates are:

- structured harmonic regression with curve-aware regularization;
- residual harmonic MLP with harmonic-space loss;
- periodic GRU or LSTM sequence models with curve-first checkpoint selection;
- spline or Fourier functional regressors;
- lightweight state-space sequence models;
- kernel ridge or Gaussian-process baselines for small offline comparisons;
- TwinCAT-oriented hybrid harmonic residual models.

## Promotion Policy

Future promotion should use a two-gate policy.

Gate 1: scalar sanity.

- finite validation and test metrics;
- no gross scalar regression failure;
- no direction-scope violation;
- acceptable artifact size and deployment plausibility.

Gate 2: curve-first TE Curve Verification Pipeline promotion.

- direction-valid TE Curve Verification Pipeline curve metrics;
- P95 and worst-condition diagnostics;
- harmonic amplitude and phase diagnostics;
- visual overlay review;
- deployment-facing interpretation.

The direction-specific or global best model should not be updated from Gate 1
alone when the task is TE compensation. Scalar winners can remain useful
baselines, but each `Fw`, `Bw`, and `global` promotion should require Gate 2 on
its own valid surface.

## Concrete Next Step

The mean-offset diagnostic chain has now advanced through CVP 1.4, CVP 1.5,
and the first Wave 3.1 learned probe. The next modeling step should be a
compact harmonic-offset follow-up, while retaining a clean Wave 3.1-like branch
as the non-harmonic control.

Recommended name:

```text
Wave 3.3 Harmonic-Offset Shape Baseline
```

Recommended deliverables:

- technical document;
- campaign plan;
- one clean non-harmonic baseline branch derived from Wave 3.1;
- one harmonic or periodic shape-preserving branch with a separate offset,
  bias, or amplitude head;
- optional composite-loss ablation with pointwise, centered-shape, mean-offset,
  and harmonic diagnostics;
- separate `global`, `Fw`, and `Bw` candidates for every branch;
- TE curve-first verification report comparing raw error, centered-shape
  error, offset, amplitude, and phase behavior.

The promotion decision should not ask whether the new branch merely beats
Wave 3.1 on scalar `MAE`. It should ask whether harmonic forcing plus explicit
offset handling restores TE curve shape while preserving a deployable causal
input contract.
