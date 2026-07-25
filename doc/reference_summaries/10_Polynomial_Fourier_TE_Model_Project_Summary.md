# Polynomial Fourier TE Model Project Summary

## Source Set

- Paper:
  `reference/te_modeling/bibliography/polynomial_fourier/2025_bauer_load_velocity_temperature_dependent_cycloidal_te_fourier_model.pdf`
- Internal OneNote export:
  `reference/te_modeling/bibliography/polynomial_fourier/fourier_series_polynomial_internal_design_note.pdf`
- Recovered MATLAB predictor:
  `reference/te_modeling/implementations/polynomial_fourier_te_predictor_matlab/`
- Existing PLC implementation:
  `reference/codes/TestRig/PLC_project/POUs/Library/0_Function Blocks/06_PolynomialFourierSeriesModel/`

## Paper Identity And Scope

The primary paper is Bauer et al., *Modeling Load-, Velocity-, and
Temperature-Dependent Transmission Errors of Cycloidal Drives for Industrial
Robots Using Fourier Series*, IEEE ICIT 2025,
DOI `10.1109/ICIT63637.2025.10965256`.

The paper models the repeatable, angularly periodic TE of a cycloidal drive as
a Fourier series whose coefficients vary with load torque, input velocity, and
lubricant temperature. It is an empirical or semi-analytical curve law, not a
first-principles contact model.

## Mathematical Law

The paper defines the angular transmission error as the difference between the
measured output angle and the ratio-scaled input angle. Its prediction has the
form

```text
TE_hat(theta, x) =
    a0(x) + sum_k A_k(x) * sin(f_k * theta + phi_k(x))

x = [load torque, input velocity, lubricant temperature]
```

For every retained harmonic, the amplitude and phase are separate functions of
the operating condition. The offset is modeled in the same way.

Each scalar coefficient function is a complete quadratic polynomial in the
three operating variables:

```text
g(x1, x2, x3) =
    b1*x1^2 + b2*x2^2 + b3*x3^2
  + b4*x1*x2 + b5*x1*x3 + b6*x2*x3
  + b7*x1 + b8*x2 + b9*x3 + b10
```

The paper fits separate parameter sets for positive and negative directions.
The operating inputs are standardized before linear least-squares
identification and the fitted coefficients are then converted back to the
physical input scale.

## Signal Processing

The paper's identification pipeline is:

1. spatially resample each TE curve;
2. remove the linear trend;
3. apply a Hamming window;
4. zero-pad to more than ten times the next power of two;
5. compute and correctly normalize the single-sided spectrum;
6. obtain amplitude and phase through sine and cosine coefficients;
7. estimate the mean offset separately;
8. regress every retained coefficient against the standardized operating
   variables.

The internal OneNote export also records an alternative Bilancia processing
route based on a uniform time-domain distribution, detrending, and conversion
from a two-sided to a single-sided spectrum. The note reports that the Bauer
processing looked slightly better in the preliminary comparison, while stating
that a formal evaluation was still required.

## Mechanism-Related Orders

For the RH380-N reducer studied in the paper, the selected order groups are:

| Mechanism interpretation | Retained orders |
| --- | --- |
| Output shaft | `1, 3, 6, 9, 13, 14, 18, 19, 27` |
| Planetary stage | `4 * {1, 3}` |
| Cycloidal stage | `46 * {1, 2, 3, 4, 6}` |
| Input gear | `24` |
| Cycloidal disc | `45 * {2, 3, 4}` |

These orders are reducer-specific. They must not be transferred blindly to a
different geometry.

## Identification And Reported Accuracy

The paper used 224 identification measurements over:

- torque: `0, +/-333, +/-500, +/-1000 Nm`;
- input velocity: `+/-2.5, +/-5, +/-7.5, +/-10 deg/s`;
- lubricant temperature: `20, 30, 40, 50 degC`.

It then evaluated 19 independent in-range Sobol conditions.

| Surface | Mean validation RMSE | Mean validation MAE |
| --- | ---: | ---: |
| Positive direction | `2.40e-5 rad` | `1.92e-5 rad` |
| Negative direction | `2.82e-5 rad` | `2.26e-5 rad` |

The abstract summarizes the average RMSE as `0.026 mrad`. The paper does not
establish extrapolation performance outside the sampled operating domain.

## Internal Reproduction Note

The internal design note records:

- successful reproduction of the Bilancia compensation path;
- adaptation of the previous-paper pipeline to XiLab data;
- evaluation of load-side and input-side angle conventions;
- a data-design concern: the available set lacks same-sign velocity and torque
  cases;
- a recommendation that full-factorial conditions suit Fourier identification,
  while randomized conditions are more suitable for ML training and testing;
- preliminary results in which the polynomial route was approximately one
  order of magnitude worse than the Bauer route;
- the need to optimize polynomial degree and structure and to standardize
  operating inputs.

The note reports input-side RMSE values of `0.0130 deg` in the positive
direction and `0.0234 deg` in the negative direction. These values belong to
the preliminary internal reproduction and must not be conflated with the paper
validation results.

## Recovered MATLAB Predictor

`TE_Predictor_FromONNX.m` predicts the coefficient set

```text
A0, A1, phi1, A39, phi39, A40, phi40
```

from input velocity, oil temperature, and output torque. It reconstructs

```text
A0
+ A1  * cos(theta + phi1)
+ A39 * cos(39 * theta + phi39)
+ A40 * cos(40 * theta + phi40)
```

The coefficient predictors are heterogeneous ONNX regressors:

- `A0`: Extremely Randomized Trees;
- `A1`: Random Forest;
- `phi1`: Random Forest;
- `A39`: Histogram Gradient Boosting;
- `phi39`: Histogram Gradient Boosting;
- `A40`: Extremely Randomized Trees;
- `phi40`: Gradient Boosting.

This implementation is not the Bauer quadratic-polynomial law. It is a hybrid
learned-coefficient Fourier predictor with a smaller harmonic set. Its ONNX
files were already present in the recovered RCIM asset archive, so the
SharePoint copies were registered as duplicates rather than copied again.

## Existing PLC Implementation

The PLC reference uses direction-specific polynomial coefficient evaluation for
the offset, amplitude, and phase terms and reconstructs a curve using the
orders:

```text
1, 3, 39, 40, 78, 81, 156, 162, 240
```

The supporting polynomial function exposes 35 explicit terms up to degree ten,
including cross terms. This makes the inference path inspectable and
PLC-friendly, but the exact fit provenance, units, coefficient selection, and
validity range still require a dedicated equation audit.

## Wave 5.2 Interpretation

The collection contains three distinct formulations that must remain separate:

| Formulation | Coefficient model | Current interpretation |
| --- | --- | --- |
| Bauer paper | Complete quadratic polynomial | Primary reproducible semi-analytical baseline |
| Recovered MATLAB predictor | Heterogeneous ONNX regressors | Hybrid learned-coefficient baseline |
| PLC reference | Explicit order-10 polynomial evaluation | Deployment-oriented recovered implementation |

The Bauer formulation is the strongest first candidate because it is explicit,
differentiable, direction-aware, condition-dependent, and directly falsifiable
with current operating variables. It is not yet a full PINN. It can become an
analytical component of one only if training includes a clear physical or
compatibility residual beyond curve reconstruction loss.

## Required Next Audit

Before implementation:

1. reconcile input-side and output-side angular conventions;
2. verify units and signs for torque, speed, temperature, phase, and TE;
3. map the applicable harmonic orders to the repository reducer geometry;
4. reproduce the paper preprocessing on the current dataset;
5. compare quadratic, recovered ONNX, and PLC coefficient laws on identical
   forward and backward splits;
6. test interpolation and held-out operating conditions separately;
7. quantify raw error, mean-centered shape, offset, amplitude, phase,
   continuity, and deployment cost;
8. identify which additional constraint would make the pilot genuinely
   physics-informed.
