# Stage 7 Mean And Centered-Shape Multi-Head Model

## Model Description

The Stage 7 family predicts the complete forward transmission-error curve as
an explicit scalar cycle mean plus an exactly zero-mean periodic shape.

```text
TE_hat(theta, u) = mean_head(u) + centered_shape_head(theta, u)
```

The model uses only normalized speed, torque, and temperature setpoints at
inference. PF-A provides the inspectable analytical coefficient anchor.

## Operating Principle

The mean head corrects only the constant Fourier coefficient. The shape head
corrects only the sine and cosine coefficients for the Stage 5 H04 core orders:

`1`, `3`, `39`, `40`, `78`, `81`, `156`, `162`, and `240`.

The non-constant basis reconstructs a periodic shape. Its computed cycle mean
is subtracted before the scalar mean is added. This makes the decomposition an
architectural invariant rather than a soft penalty.

## Conceptual Structure

```text
causal setpoints
    -> shared, partial, or independent condition encoder
    -> bounded mean correction
    -> bounded non-constant coefficient corrections
    -> exact centered-shape projection
    -> mean + centered shape
    -> complete periodic TE curve
```

## Candidate Topologies

- monolithic Stage 5 H04 control;
- fully shared trunk with separate heads;
- partially shared trunk with private branches;
- independent mean and shape networks;
- shared trunk with projected conflicting gradients;
- frozen PF-A mean plus learned shape;
- learned mean plus frozen PF-A shape.

## Advantages

- offset and angular shape cannot silently absorb one another;
- component errors remain separately measurable;
- the periodic shape has exact zero cycle mean;
- the complete reconstruction remains inspectable and PLC-oriented;
- analytical-mean and analytical-shape ablations localize where learning adds
  value;
- gradient conflict is measured instead of hidden inside a scalar loss.

## Disadvantages

- explicit decomposition does not guarantee that either task becomes easier;
- shared features can create negative transfer;
- independent heads increase parameter count;
- gradient projection can improve one task while degrading curve-level error;
- the model remains a structured grey-box predictor, not a governing-equation
  PINN.

## Implemented Python Components

`scripts/models/mean_centered_shape_multi_head_network.py`

- `build_tanh_network`;
- `MeanCenteredShapeMultiHeadNetwork`;
- `shared_parameter_list`;
- `forward`.

`scripts/campaigns/wave_5_2/run_wave52r_stage7_mean_centered_shape_multi_head.py`

- immutable dataset and checkpoint loading;
- synthetic structural preflight;
- matched candidate construction;
- named mean, shape, and curve losses;
- gradient-cosine and projected-conflict training;
- full-curve multi-index evaluation;
- conditional multi-seed stability;
- persistent campaign artifacts and state.

## Qualification Boundary

No candidate is qualified merely because the shape mean is exactly zero.
Promotion requires simultaneous held-out raw, offset, centered-shape,
derivative, harmonic, tail, control, parameter-efficiency, and stability
evidence.

## Completed Campaign Result

All `7 / 7` first-screen runs completed and every structural invariant passed.
No shared or partially shared formulation passed the predictive gate, so the
conditional stability continuation was skipped.

C01, the monolithic H04 fine-tuning control, led raw error at
`0.001712731 deg`. It improved raw MAE by `0.76%` and mean MAE by `2.32%`
relative to frozen H04, but centered-shape MAE worsened by `0.04%`. S01 and
P01 reduced parameters relative to independent I01 but regressed all primary
curve metrics. G01 matched S01 because its non-negative shared gradient cosine
never triggered projection.

The family therefore closes as a valid negative result. Exact mean-shape
decomposition is retained as an interpretability tool, no Stage 7 candidate is
promoted, and H04 remains the qualified structured component for Stage 8.
