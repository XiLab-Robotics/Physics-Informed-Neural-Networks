# Stage 11 Uncertainty And Physics-Trust Calibration Model Report

## Model Description

The Stage 11 component is a trust estimator around a frozen TE predictor. It
does not predict a replacement transmission-error curve. Instead, it receives
causal operating-condition and model-disagreement signals and estimates where
the frozen Stage 9 K01 curve is likely to be unreliable.

The component has three conceptual layers:

1. deterministic signal generation;
2. validation-only monotonic error calibration;
3. conformal interval construction around the unchanged K01 prediction.

## Operating Principle

For operating condition vector `u`, the frozen models produce:

```text
PF-A(u, theta)
H04(u, theta)
K01(u, theta, causal history)
R00(u, theta)
```

where `theta` is the fixed angular grid. The trust estimator derives signals
such as:

```text
distance_to_training_support(u)
abs(PF-A - H04)
abs(H04 - K01)
abs(PF-A - K01)
abs(R00 - K01)
std(K01_seed_1, ..., K01_seed_5)
```

The measured TE curve is absent from this path. It is used only after
prediction to score whether uncertainty ranked and covered the actual error.

## Conceptual Structure

```text
operating conditions
        |
        +--> training-support distance --------+
        |                                      |
        +--> PF-A / H04 / R00 predictions -----+--> causal trust signals
        |                                      |            |
causal history --> K01 seed ensemble ----------+            v
                                                   validation-only calibration
                                                              |
                                                              v
K01 primary mean prediction --------------------------> calibrated intervals
```

The separation between the prediction center and uncertainty is deliberate.
Stage 11 cannot improve its apparent calibration by moving the mean curve.

## Advantages In This Project

- uses the exact polished-setpoint forward split already audited by Stage 2;
- preserves the analytical-versus-learned distinction;
- tests whether disagreement between incomplete models is informative;
- exposes operating-support distance as a PLC-friendly intermediate quantity;
- permits a cheap single-score deployment path if simple signals pass;
- treats ensemble cost explicitly rather than assuming it is acceptable;
- can abstain or flag a curve without claiming that PF-A is exact physics.

## Disadvantages And Limits

- ensemble spread measures model sensitivity, not total physical uncertainty;
- disagreement can be small when multiple models share the same bias;
- only `97` held-out curves are available for the final calibration audit;
- sparse boundary tiers limit strong subgroup conclusions;
- validation-fitted calibration can overfit if too many signal combinations are
  searched;
- conformal coverage is empirical and split-dependent;
- a qualified trust score does not make K01 a promoted TE predictor;
- a full five-member ensemble is not automatically PLC-friendly.

## Planned Python Components

The implementation will introduce an explicit reusable module under
`scripts/models/` containing:

- operating-condition standardization and nearest-support distance;
- support-tier and boundary-margin scoring;
- curvewise and pointwise disagreement aggregation;
- deterministic ensemble spread;
- isotonic error-scale calibration;
- validation-fitted composite trust estimation;
- split-conformal interval construction;
- rank, capture, risk-coverage, coverage, and subgroup metrics.

The Stage 11 campaign driver will own:

- frozen artifact loading and identity alignment;
- additional K01 seed training through the Stage 9 contract;
- candidate evaluation;
- immutable artifact writing;
- campaign leaderboard and winner selection;
- preflight checks and failure summaries.

## Interpretation Boundary

The intended statement from a passing Stage 11 result is:

> A declared causal signal identifies a useful fraction of high-error
> polished-setpoint forward K01 predictions and supports calibrated empirical
> intervals on the frozen test split.

It is not:

> The uncertainty is a mechanistic probability distribution of RV-reducer
> transmission error.

That stronger claim would require independently validated stochastic physics,
repeatability measurements, and broader operating-domain evidence.

## Completed Evidence

The campaign
`2026-07-29-20-49-33_wave52r_stage11_uncertainty_trust_calibration_2026_07_29`
completed all `10 / 10` declared entries without execution failure.

- D01 dense-model disagreement was the strongest overall diagnostic candidate:
  Spearman correlation `0.2810`, average precision `0.4988`, top-error capture
  `0.40`, and selective `MAE@80%` of `0.001241 deg`. It missed the fixed
  rank-correlation and selective-risk gates.
- M01 composite calibration reached Spearman correlation `0.3040` and average
  precision `0.3624`, but top-error capture remained `0.35` and selective
  `MAE@80%` remained `0.001252 deg`.
- E01 five-seed ensemble spread reached Spearman correlation `0.3523`, but
  missed average precision, capture, selective risk, and the one-model
  deployment-cost constraint.
- Marginal conformal coverage and operating-band checks were feasible, but
  interval calibration did not repair insufficient error localization.

No candidate passed the complete Stage 11 gate. K01 remains a qualified
research component without official promotion, and no uncertainty or
physics-trust mechanism advances into the next objective automatically.

The canonical campaign result is
`doc/reports/campaign_results/model_development_waves/wave_5_2/2026-07-29-21-21-32_wave52r_stage11_uncertainty_and_physics_trust_calibration_results_report.md`
with a validated PDF companion beside it.
