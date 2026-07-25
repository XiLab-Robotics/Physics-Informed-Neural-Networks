# Phase 1 Polynomial-Fourier Analytical Benchmark

## Executive Decision

Phase 1 is complete on the immutable paired split. The selected analytical
reference is `PF_A_LOCAL_QUADRATIC` and the structurally useful alternative
comparator is `PF_E_REDUCED_QUADRATIC`.

Neither model is a full PINN. They are analytical baselines for the physics
residual tests that begin in Phase 2.

## Evaluation Contract

- eligible paired operating conditions: `966`;
- directional curves: `1932`;
- split assignment SHA-256:
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`;
- normalized angular samples: `2048`;
- fitting uses training conditions only and remains direction-specific;
- validation and test conditions are never used to fit coefficient surfaces;
- the three anomalous Phase 0 training conditions remain quarantined.

## Implemented Formulations

- `PF-A`: standardized complete-quadratic coefficient surfaces using local and
  paper-derived harmonic-order ablations;
- `PF-B`: exact recovered seven-model ONNX coefficient path, valid for `Fw`;
- `PF-C`: parsed PLC degree-10, 35-term polynomial and nine harmonics;
- `PF-D`: direct per-curve Fourier oracle, used only as a target-leaking
  representational ceiling;
- `PF-E`: reduced common-order complete-quadratic formulation.

The paper-derived RH380 orders are treated as an ablation, not as an automatic
transfer of reducer geometry.

## Held-Out Comparison

| Model | Direction | Mean raw MAE [deg] | Mean centered MAE [deg] | Mean offset error [deg] |
| --- | --- | ---: | ---: | ---: |
| PF_A_LOCAL_QUADRATIC | Bw | 0.001967 | 0.001727 | 0.000694 |
| PF_A_LOCAL_QUADRATIC | Fw | 0.001807 | 0.001385 | 0.000965 |
| PF_E_REDUCED_QUADRATIC | Bw | 0.001988 | 0.001736 | 0.000694 |
| PF_E_REDUCED_QUADRATIC | Fw | 0.001823 | 0.001403 | 0.000965 |

The selection uses equal-rank aggregation across held-out raw MAE,
mean-centered shape MAE, offset error, and derivative MAE. It excludes `PF-D`
from deployment selection because it sees the target curve, and it excludes
`PF-B` from the bidirectional selection because the recovered MATLAB evidence
only establishes the forward path.

## Nonselected-Variant Findings

- the paper-order quadratic reaches combined-direction mean raw MAE
  `0.002171 deg`, confirming that RH380 geometry orders should not be
  transferred automatically;
- recovered ONNX reaches mean raw MAE `0.003047 deg` on the common `Fw` test
  surface, while its five original MATLAB examples range from approximately
  `0.000713` to `0.001343 deg`;
- recovered ONNX backward inference is an explicit stress test and fails
  primarily through offset, with mean raw MAE `0.068068 deg`;
- the PLC law reaches mean raw MAE `0.001740 deg` in `Bw`, but its degree-10
  forward polynomial is numerically unsafe across the broader common torque
  domain: median `Fw` MAE is `4.087881 deg` and the mean is dominated by
  extreme high-torque extrapolation;
- the direct Fourier oracle reaches approximately `0.00031 deg` mean raw MAE,
  demonstrating retained harmonic capacity but not deployable prediction.

## Parity And Stability Evidence

- deterministic Fourier reconstruction, phase wrapping, quadratic recovery,
  PLC basis, parser shape, and ONNX I/O tests: `pass`;
- fitted quadratic design condition numbers and all coefficient matrices are
  preserved in the machine-readable coefficient artifact;
- the Bauer detrend, Hamming, greater-than-ten-times zero-padding, and
  single-sided spectral audit is preserved for every held-out curve;
- the five recovered MATLAB experiment files are evaluated independently;
- PLC source identity, units, active polynomial degree, basis size, harmonic
  orders, and intermediate arrays are preserved in the parity artifact.

## Deployment Interpretation

`PF-A` and `PF-E` are compact and inspectable coefficient-surface baselines.
`PF-C` remains the closest executable PLC comparator but its high-order
polynomial should not be generalized outside the recovered operating domain
without explicit edge checks. `PF-B` preserves valuable recovered evidence,
but it is a sparse forward-only comparator rather than a common bidirectional
reference.

## Phase 2 Handoff

The first PINN test may now use the selected analytical reference to construct
harmonic and kinematic residuals. The Phase 2 campaign still requires its own
technical document, preliminary campaign plan, configuration, launcher, and
explicit campaign-plan approval before training.

## Evidence

- `output/analysis/polynomial_fourier_benchmark/phase1_benchmark_summary.yaml`
- `output/analysis/polynomial_fourier_benchmark/phase1_per_curve_metrics.csv`
- `output/analysis/polynomial_fourier_benchmark/phase1_aggregate_metrics.csv`
- `output/analysis/polynomial_fourier_benchmark/phase1_bauer_preprocessing_audit.csv`
- `output/analysis/polynomial_fourier_benchmark/phase1_coefficient_models.yaml`
- `output/analysis/polynomial_fourier_benchmark/phase1_onnx_matlab_example_metrics.csv`
- `output/analysis/polynomial_fourier_benchmark/phase1_plc_parity.yaml`
- `output/analysis/polynomial_fourier_benchmark/phase1_plots`
