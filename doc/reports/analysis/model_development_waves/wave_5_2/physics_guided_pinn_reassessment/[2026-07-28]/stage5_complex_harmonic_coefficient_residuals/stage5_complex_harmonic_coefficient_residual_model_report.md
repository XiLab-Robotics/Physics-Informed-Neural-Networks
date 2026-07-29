# Stage 5 Complex Harmonic Coefficient Residual Model

## Model Description

The Stage 5 family predicts a complete forward transmission-error curve from
causal operating setpoints. Unlike the Stage 4 pointwise residual family, every
Stage 5 learned and analytical path uses the same uniformly resampled curve
representation with `2048` angular samples.

The main model predicts explicit Fourier coefficients:

```text
coefficient vector =
    offset,
    sine coefficient for each selected order,
    cosine coefficient for each selected order
```

The reconstructed TE curve is therefore deterministic, periodic, and
inspectable.

## Operating Principle

The network receives three normalized causal condition features:

- signed forward torque setpoint;
- absolute speed setpoint;
- temperature setpoint.

It never receives measured torque, measured speed, measured temperature, or a
target-derived runtime feature.

The direct coefficient control predicts all coefficients from zero. Anchored
candidates receive the frozen causal PF-A coefficient vector and predict only a
correction:

```text
predicted coefficients =
    frozen PF-A coefficients
  + learned coefficient corrections
```

Bounded candidates apply a separate training-only physical-unit limit to every
offset, sine, and cosine correction. Banded candidates keep offset, order one,
low-order, reducer-related middle-order, and high-order errors visible as
separate diagnostic groups.

## Conceptual Structure

```text
causal setpoints
      |
      v
condition MLP ----------------------+
      |                             |
      v                             v
direct coefficients       coefficient correction
                                    |
PF-A coefficients ------------------+
                  |
                  v
     explicit sine/cosine synthesis
                  |
                  v
       uniform 2048-point TE curve
```

The direct curve controls bypass Fourier coefficients and predict the uniform
curve vector directly. They isolate the value of the coefficient bottleneck
from the value of neural capacity.

## Harmonic Order Sets

The immutable preflight produced:

- `core`: `1, 3, 39, 40, 78, 81, 156, 162, 240`;
- `core_plus_residual`: core plus `2, 80, 159, 237`;
- `data_selected`: core plus the eight strongest training-only stable residual
  orders `159, 237, 2, 80, 120, 42, 158, 160`.

The validation and test curves did not influence the selected orders.

## Losses

All learned candidates use full-curve error. Coefficient candidates add
elementwise sine/cosine error normalized with training-only coefficient scales.
Banded candidates add equalized band loss. The two final ablations add weak or
moderate smoothness between nearest training operating conditions.

Amplitude and phase are reporting coordinates only. Direct sine/cosine
training avoids phase-wrap discontinuities.

## Advantages

- training and evaluation share one curve representation;
- all retained periodic components are explicit;
- phase wrapping is removed from the optimization coordinates;
- PF-A contribution and learned correction remain separately observable;
- coefficient and band bounds prevent hidden pointwise cancellation;
- reconstruction is deterministic and PLC-friendly;
- order selection, normalization, and bounds are training-only.

## Disadvantages

- omitted harmonics remain an irreducible reconstruction residual;
- direct curve controls have substantially larger output layers;
- coefficient smoothness may over-regularize real operating-condition changes;
- a Fourier bottleneck is mathematical structure, not by itself a physical
  equation;
- success would validate a structured grey-box component, not yet a full PINN.

## Implemented Files, Classes, And Functions

### Model

`scripts/models/complex_harmonic_coefficient_residual_network.py`

- `ComplexHarmonicCoefficientResidualNetwork`
- `reconstruct_curve`
- `forward`

### Campaign

`scripts/campaigns/wave_5_2/run_wave52r_stage5_complex_harmonic_coefficient_residuals.py`

The script:

- loads the frozen split and uniform Phase 1 curves;
- embeds PF-A coefficients into nested order sets;
- selects exploratory orders using training residuals only;
- derives coefficient normalization and correction bounds;
- creates eighteen queue YAML files, including direct data-selected-order
  controls for H07 and H08;
- validates every model and representation contract;
- runs deterministic full-curve training;
- writes checkpoints, predictions, metrics, leaderboards, and campaign state.

### Launcher

`scripts/campaigns/wave_5_2/run_wave52r_stage5_complex_harmonic_coefficient_residuals.ps1`

The launcher supports local and remote-compatible preflight plus local and
remote campaign execution with bidirectional artifact synchronization.

## Preflight Result

The first complete preflight passed:

- `966` accepted forward curves;
- `675` training, `194` validation, and `97` test curves;
- `2048` identical angular samples per curve;
- all `18` candidate forward and backward gradient checks;
- exact zero-correction PF-A replay for every anchored candidate;
- bounded-coefficient enforcement;
- NumPy/PyTorch reconstruction maximum absolute difference
  `2.581816111180135e-07 deg`;
- no target leakage;
- no measured-runtime operating input.

## Qualification Boundary

The scalar campaign winner cannot be promoted directly. A candidate must beat
PF-A and its matched direct control on canonical full-curve error while also
passing centered-shape, offset, derivative, closure, harmonic amplitude,
harmonic phase, correction-energy, support, and deterministic-stability gates.

## Completed Campaign Decision

All eighteen first-screen runs and all four conditional stability runs
completed without failure.

H08 produced the lowest single-seed raw test MAE at `0.00169334 deg`, but it
regressed closure, harmonic amplitude, and harmonic phase against PF-A. It is
therefore retained only as a raw-error diagnostic leader.

H04, the bounded PF-A-anchored core-order deep candidate, passed all ten
isolated-component gates. Its seed-`314159` test MAE is `0.00172588 deg`, and
its three-seed mean is `0.00174908 +/- 0.00003982 deg`. Every H04 seed beats
both PF-A and the matched C04 direct coefficient control. H04 advances into
Stage 6 as a qualified structured coefficient component.

This decision does not classify H04 as a complete PINN, replace the accepted
forward program leader, or authorize production deployment.
