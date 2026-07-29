# Stage 8 Weak Forward Compliance Prior Model

## Model Description

`WeakForwardComplianceResidualNetwork` wraps the qualified Stage 5 H04
coefficient model and exposes the derivative of predicted curve mean with
respect to causal signed forward torque.

The standard path preserves H04:

```text
PF-A coefficients + bounded learned coefficient correction
    -> exact periodic curve
    -> predicted mean and centered shape
    -> d predicted mean / d signed torque
```

The hard-equation negative control replaces only the predicted constant
coefficient:

```text
mean_TE = zero_torque_intercept + signed_torque / bounded_stiffness
```

## Operating Principle

Weak candidates penalize only a negative response derivative or derivatives
outside broad train-only bootstrap intervals. Confidence and temperature arms
modify those intervals without supplying measured TE at runtime. The delayed
and adaptive arms alter optimization timing or bounded weight, not the
inference graph.

The effective response derivative is an observable modeling quantity. It is
not labelled contact stiffness because the dataset lacks ordered load-unload
cycles, clearances, contact force, and internal stiffness measurements.

## Advantages

- starts from the qualified H04 periodic representation;
- uses only causal setpoints at inference;
- separates prediction, response derivative, and hard-control stiffness;
- admits a shuffled-torque specificity control;
- preserves exact periodic reconstruction;
- exposes PLC-friendly intermediate quantities;
- measures gradient conflict against raw, mean, and shape losses.

## Disadvantages

- static condition files cannot identify hysteresis or lost motion;
- torque and mean TE may share unobserved causes;
- bootstrap bounds are empirical support, not universal mechanics;
- autograd derivatives increase training cost;
- a stable fitted parameter can coexist with unstable prediction;
- the hard equation is intentionally misspecified as a negative control.

## Implemented Components

`scripts/models/weak_forward_compliance_residual_network.py`

- `WeakForwardComplianceResidualNetwork`;
- `signed_torque_from_normalized`;
- `effective_stiffness_nm_per_deg`;
- `forward`;
- `mean_compliance_derivative`.

`scripts/campaigns/wave_5_2/run_wave52r_stage8_weak_forward_compliance_priors.py`

- deterministic train-only bootstrap;
- shuffled-torque negative control;
- temperature-stratified intervals;
- density-derived confidence;
- weak, delayed, adaptive, and hard candidate losses;
- gradient interaction diagnostics;
- full-curve multi-index gates;
- conditional three-seed continuation;
- immutable campaign and run artifacts.

## Qualification Boundary

No candidate advances because it has a positive derivative or stable effective
stiffness. Promotion requires all three seeds to improve raw and curve-mean
error against H04 and C00 while preserving centered shape, derivative,
harmonic, closure, and P95 behavior and outperforming shuffled torque.

## Completed Campaign Result

The approved campaign completed `10 / 10` first-screen runs with no failures.
The training-only bootstrap found a positive curve-mean torque slope in all
`512 / 512` resamples, with a 95% interval from
`3.623920841e-05` to `3.713770981e-05 deg/Nm`. The shuffled-torque control
returned `50.39%` positive support, confirming that the population association
depends on the real torque ordering.

No weak-prior formulation beat data-only C00 while preserving positive
model-local derivatives. C00 remained the raw-error leader at
`0.001716862 deg`; S01 and A01 beat frozen H04 on raw and mean error but not
C00, and their local derivatives remained negative in `37.1%` and `44.3%` of
test conditions. H01 removed every sign violation but raised raw MAE to
`0.002355556 deg` and mean MAE to `0.001581088 deg`.

The family is therefore closed as a valid negative result. No Stage 8 model is
promoted, H04 remains the qualified structured component, and Stage 9 proceeds
with temporal analytical-residual models.
