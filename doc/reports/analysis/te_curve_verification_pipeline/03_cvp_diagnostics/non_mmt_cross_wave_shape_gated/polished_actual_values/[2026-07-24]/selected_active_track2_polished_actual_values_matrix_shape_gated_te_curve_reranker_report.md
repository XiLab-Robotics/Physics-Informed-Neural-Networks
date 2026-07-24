# Shape-Gated TE Curve Reranker Report

## Overview

This report applies a reduced shape-first gate to the
selected-active `TE Curve Verification Pipeline` candidate set. It does
not run training and does not change the deployable runtime input
contract.

## Scope

- run instance: `2026-07-24-14-38-10__shape_gated_te_curve_reranker`;
- config path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\selected_active_track2_polished_actual_values_matrix.yaml`;
- dataset: `polished_dataset`;
- evaluated surfaces: `forward`, `backward`;
- non-evaluated surfaces remain unchanged by this reduced selection pass;

## Gate Thresholds

| Metric | Threshold |
| --- | ---: |
| FFT amplitude similarity | >= 0.820 |
| Raw derivative correlation | >= 0.700 |
| Smoothed derivative correlation | >= 0.250 |
| Derivative sign agreement rate | >= 0.540 |
| Normalized derivative RMSE | <= 1.000 |
| Mean harmonic amplitude error [%] | <= 55.000 |
| Mean harmonic phase error [deg] | <= 75.000 |
| Peak-to-peak error [%] | <= 35.000 |
| Per-curve shape pass rate | >= 0.600 |
| Near-pass FFT amplitude similarity | >= 0.950 |
| Near-pass mean harmonic amplitude error [%] | <= 38.000 |
| Near-pass mean harmonic phase error [deg] | <= 55.000 |
| Near-pass peak-to-peak error [%] | <= 32.000 |
| Near-pass derivative sign agreement rate | >= 0.500 |
| Near-pass normalized derivative RMSE | <= 1.350 |

## Surface Decisions

### Forward

| Rank | Candidate | Label | Raw MAE [deg] | Centered MAE [deg] | FFT Similarity | Harmonic Amp Err [%] | Harmonic Phase Err [deg] | Raw Deriv Corr | Smoothed Deriv Corr | Deriv Sign Rate | Norm Deriv RMSE | Shape Pass Rate | Composite |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `polished_actual_values_periodic_gru_sequence_Fw` | `recommended_candidate` | 0.001676 | 0.001463 | 0.986 | 19.865 | 11.101 | 0.139 | 0.297 | 0.542 | 0.360 | 0.960 | 0.031 |
| 2 | `polished_actual_values_wave4_1_mae_robust_loss_Fw` | `candidate` | 0.001681 | 0.001547 | 0.982 | 21.713 | 15.048 | -0.029 | 0.220 | 0.492 | 0.368 | 0.900 | 0.124 |
| 3 | `polished_actual_values_wave4_2_quantile_p10_p50_p90_Fw` | `candidate` | 0.001719 | 0.001554 | 0.982 | 25.783 | 15.160 | 0.010 | 0.238 | 0.505 | 0.364 | 0.830 | 0.131 |
| 4 | `polished_actual_values_residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `candidate` | 0.001858 | 0.001712 | 0.981 | 40.123 | 32.972 | 0.077 | 0.130 | 0.524 | 0.357 | 0.860 | 0.234 |
| 5 | `polished_actual_values_residual_harmonic_gru_sequence_sparse_rcim_Fw` | `candidate` | 0.001919 | 0.001709 | 0.981 | 38.548 | 30.340 | 0.062 | 0.141 | 0.519 | 0.354 | 0.850 | 0.290 |
| 6 | `polished_actual_values_periodic_mlp_harmonic_Fw` | `candidate` | 0.001900 | 0.001507 | 0.984 | 15.446 | 13.643 | -0.009 | 0.245 | 0.497 | 0.375 | 0.910 | 0.374 |
| 7 | `polished_actual_values_tree_Fw` | `shape_gate_failed` | 0.002120 | 0.001919 | 0.978 | 51.180 | 39.559 | -0.030 | -0.007 | 0.280 | 0.680 | 0.480 | 0.620 |
| 8 | `polished_actual_values_feedforward_Fw` | `shape_gate_failed` | 0.002181 | 0.001949 | 0.977 | 64.170 | 67.411 | -0.115 | -0.050 | 0.464 | 0.384 | 0.040 | 0.683 |
| 9 | `polished_actual_values_harmonic_regression_Fw` | `shape_gate_failed` | 0.002355 | 0.001938 | 0.977 | 64.509 | 68.083 | -0.117 | -0.051 | 0.464 | 0.380 | 0.010 | 0.903 |

### Backward

| Rank | Candidate | Label | Raw MAE [deg] | Centered MAE [deg] | FFT Similarity | Harmonic Amp Err [%] | Harmonic Phase Err [deg] | Raw Deriv Corr | Smoothed Deriv Corr | Deriv Sign Rate | Norm Deriv RMSE | Shape Pass Rate | Composite |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `polished_actual_values_periodic_gru_sequence_Bw` | `recommended_candidate` | 0.001333 | 0.001222 | 0.992 | 18.469 | 14.176 | 0.267 | 0.453 | 0.594 | 0.355 | 0.989 | 0.000 |
| 2 | `polished_actual_values_wave4_2_quantile_p10_p50_p90_Bw` | `candidate` | 0.002188 | 0.002103 | 0.968 | 29.165 | 20.963 | 0.028 | 0.274 | 0.508 | 0.411 | 0.883 | 0.439 |
| 3 | `polished_actual_values_residual_harmonic_gru_sequence_sparse_rcim_Bw` | `candidate` | 0.002306 | 0.002224 | 0.967 | 41.324 | 35.086 | 0.105 | 0.209 | 0.530 | 0.374 | 0.830 | 0.473 |
| 4 | `polished_actual_values_wave4_1_mae_robust_loss_Bw` | `candidate` | 0.002315 | 0.002138 | 0.967 | 26.130 | 18.326 | 0.079 | 0.300 | 0.526 | 0.438 | 0.883 | 0.483 |
| 5 | `polished_actual_values_periodic_mlp_harmonic_Bw` | `candidate` | 0.002483 | 0.002042 | 0.975 | 22.165 | 19.788 | 0.043 | 0.266 | 0.515 | 0.427 | 0.883 | 0.533 |
| 6 | `polished_actual_values_residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `candidate` | 0.002669 | 0.002268 | 0.966 | 37.403 | 34.789 | 0.096 | 0.179 | 0.538 | 0.408 | 0.851 | 0.612 |
| 7 | `polished_actual_values_feedforward_Bw` | `shape_gate_failed` | 0.002769 | 0.002398 | 0.963 | 64.202 | 74.205 | -0.100 | -0.078 | 0.468 | 0.435 | 0.000 | 0.765 |
| 8 | `polished_actual_values_tree_Bw` | `shape_gate_failed` | 0.002759 | 0.002397 | 0.964 | 50.774 | 51.741 | -0.026 | -0.005 | 0.311 | 0.676 | 0.543 | 0.791 |
| 9 | `polished_actual_values_harmonic_regression_Bw` | `shape_gate_failed` | 0.002966 | 0.002372 | 0.963 | 63.064 | 74.103 | -0.122 | -0.083 | 0.460 | 0.427 | 0.000 | 0.921 |

## Interpretation Rules

- `recommended_candidate` is the first active candidate that passes the
  shape gate after block-score reranking.
- `baseline_anchor_only` entries remain useful references, but they do not
  replace the active development baseline in this reduced pass.
- `near_pass` entries miss the strict per-curve pass-rate gate but keep
  enough aggregate FFT, harmonic, peak-to-peak, and derivative evidence
  to remain visible for review.
- `shape_gate_failed` entries may still have good scalar error, but they
  are demoted until the curve-shape evidence improves.
- `insufficient_evidence` entries could not be evaluated from their
  referenced artifact and must not be promoted until provenance is
  repaired.
- All FFT, centered-shape, derivative, and harmonic diagnostics are
  validation-time evidence only, not deployable runtime corrections.
- The threshold sweep is calibration evidence only; it is not a second
  promotion policy.

## Output Artifacts

- per-curve metrics: `output\validation_checks\non_mmt_cross_wave_shape_gated\polished_actual_values\2026-07-24-14-38-10__shape_gated_te_curve_reranker\shape_gated_per_curve_metrics.csv`;
- candidate summary: `output\validation_checks\non_mmt_cross_wave_shape_gated\polished_actual_values\2026-07-24-14-38-10__shape_gated_te_curve_reranker\shape_gated_candidate_summary.csv`;
- threshold sweep: `output\validation_checks\non_mmt_cross_wave_shape_gated\polished_actual_values\2026-07-24-14-38-10__shape_gated_te_curve_reranker\shape_gate_threshold_sweep.csv`;
- surface decisions: `output\validation_checks\non_mmt_cross_wave_shape_gated\polished_actual_values\2026-07-24-14-38-10__shape_gated_te_curve_reranker\shape_gated_surface_decisions.yaml`;
