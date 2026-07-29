# Stage 9 Causal Temporal Analytical-Residual Model

## Model Description

The Stage 9 model predicts a complete forward transmission-error curve from
causal angular order and setpoint operating conditions. It combines a
unidirectional GRU with one of four explicit anchor contracts:

- no anchor for direct temporal learning;
- zero anchor for the matched residual control;
- frozen PF-A;
- frozen Stage 5 H04;
- H04 mean only for explicit mean/shape separation.

The model is a physics-guided temporal residual, not a full dynamical PINN. The
recorded dataset provides angular sequences inside steady-state curves but no
ordered load trajectories between operating conditions.

## Operating Principle

For each curve, the GRU receives the current angular features and repeated
setpoint torque, speed, and temperature:

```text
current angle harmonics + causal setpoints + previous hidden state
    -> unidirectional GRU
    -> point residual or coefficient residual
    -> analytical anchor + bounded correction
    -> current TE prediction
```

The hidden state is initialized explicitly to zero at every curve boundary.
It may be carried across contiguous chunks of the same curve. Chunk boundaries
are processing boundaries only: they cannot reset or mix physical curves.

The default angular feature block uses the Stage 5 core harmonic orders
`1, 3, 39, 40, 78, 81, 156, 162, 240`. This gives the recurrent model direct
access to known periodic coordinates while preserving chronological order.

## Point-Residual Mode

The GRU emits one residual value for each angular point:

```text
predicted_TE(theta_t) = anchor_TE(theta_t) + bounded_residual(theta_<=t)
```

The H01 and L01 candidates use frozen H04 as the anchor. P01 uses PF-A. R00
uses zero as a parameter-matched data-only residual control.

## Coefficient-Residual Mode

K01 emits bounded corrections to the Stage 5 complex Fourier coefficient
vector at every causal step. The current angle is reconstructed from the
current coefficient estimate:

```text
c_hat(theta_<=t) = c_H04 + bounded_delta_c(theta_<=t)
TE_hat(theta_t) = FourierReconstruct(c_hat(theta_<=t), theta_t)
```

The early predictions may use only short prefixes; no final hidden state is
back-propagated to earlier angles during inference.

## Mean-Static And Shape-Temporal Mode

M01 retains the H04 curve mean as a static causal anchor and asks the GRU to
predict the angular shape. Exact offline mean-centering is forbidden because
it would require the full future predicted curve. Mean error and centered
shape are therefore diagnostics, not target-derived runtime operations.

## Advantages

- directly tests the value of chronological angular context;
- preserves explicit PF-A and H04 anchor comparisons;
- exposes hidden state, reset, chunk carry, and residual magnitude;
- supports point and coefficient residuals;
- uses only setpoints and angle at inference;
- has a direct PLC-friendly reset and state-carry contract;
- includes an accepted-GRU replay and shuffled-order specificity control.

## Disadvantages

- angular context is not the same as load-history memory;
- setpoints remain constant inside each curve;
- no trajectory connects one operating-condition file to the next;
- long sequences can learn periodic interpolation without learning mechanics;
- the accepted historical GRU used centered windows and a different split;
- coefficient estimates can vary with prefix length even when the true
  structured coefficients are curve-level quantities;
- recurrent inference carries more PLC state than H04 alone.

## Planned Python Components

`scripts/models/causal_temporal_analytical_residual_network.py`

- `CausalTemporalAnalyticalResidualNetwork`;
- `build_angular_feature_tensor`;
- `initial_hidden_state`;
- `forward_sequence`;
- `forward_in_chunks`;
- `reconstruct_current_harmonic_value`;
- explicit point-residual and coefficient-residual outputs.

`scripts/campaigns/wave_5_2/run_wave52r_stage9_temporal_analytical_residual_models.py`

- Stage 0 dataset and split reconstruction;
- PF-A and H04 anchor replay;
- accepted periodic-GRU checkpoint reconstruction and replay;
- deterministic causal curve batching;
- explicit zero-state reset and chunk equivalence;
- shuffled-order negative control;
- bounded first-screen and conditional stability;
- curve-first multi-index gates;
- immutable campaign artifacts.

## Qualification Boundary

No Stage 9 model advances because recurrence lowers scalar MAE alone.
Promotion requires a structured hybrid to beat frozen H04, the accepted GRU
replay, the matched data-only residual GRU, and the shuffled-order control on
the same Stage 0 test curves while preserving the full curve-first diagnostic
surface and deterministic hidden-state behavior across three seeds.

## Completed Evidence

The first screen completed all ten entries without runtime failure. The
coefficient-residual GRU `K01` was the strongest candidate:

- raw MAE: `0.001371553 deg`;
- mean MAE: `0.000495866 deg`;
- mean-centered shape MAE: `0.001227270 deg`;
- improvement relative to frozen H04: `20.53%` raw, `43.93%` mean, and
  `9.46%` shape.

The accepted temporal replay was corrected before closeout to use the
canonical five-input polished-setpoint forward archive checkpoint. The
corrected `G00` raw MAE is `0.001924689 deg`. The initial replay had referenced
an older actual-values checkpoint and is not used in the final evidence.

`H01`, `K01`, and `L01` beat the shuffled-order control on raw and mean error,
so chronological state adds measurable value. The shuffled control remained
competitive, however, showing that angle features, the H04 anchor, and model
capacity explain a substantial part of the improvement.

No model advanced. All structured candidates failed at least the periodic
closure, P95 tail, and declared `1e-6 deg` chunk-equivalence gates. Reset
reproducibility remained exact and the absolute chunk differences were small,
but the predeclared threshold was not changed after observing the results.
`K01` is retained as a qualified research component rather than an official
promotion.
