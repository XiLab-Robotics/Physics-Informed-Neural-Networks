# Shape-Gated TE Curve Reranker Report

## Overview

This report applies a reduced forward/backward shape-first gate to the
selected-active `TE Curve Verification Pipeline` candidate set. It does
not run training and does not change the deployable runtime input
contract.

## Scope

- run instance: `2026-07-20-17-54-14__shape_gated_te_curve_reranker`;
- config path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\selected_active_track2_polished_setpoints_matrix.yaml`;
- dataset: `polished_dataset`;
- reduced surfaces: `forward`, `backward`;
- `global` remains paused for this reduced selection pass;

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
| 1 | `polished_setpoints_wave4_1_mae_robust_loss_Fw` | `recommended_candidate` | 0.016970 | 0.002293 | 0.982 | 30.976 | 44.291 | 0.017 | 0.089 | 0.506 | 0.407 | 0.890 | 0.146 |
| 2 | `polished_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | `candidate` | 0.051176 | 0.002170 | 0.982 | 31.251 | 39.677 | 0.053 | 0.123 | 0.517 | 0.406 | 0.880 | 0.621 |
| 3 | `polished_setpoints_harmonic_regression_Fw` | `shape_gate_failed` | 0.017019 | 0.001937 | 0.975 | 76.094 | 73.205 | 0.001 | 0.020 | 0.501 | 0.362 | 0.000 | 0.233 |
| 4 | `polished_setpoints_periodic_gru_sequence_Fw` | `shape_gate_failed` | 0.038470 | 0.004025 | 0.981 | 47.889 | 32.427 | 0.033 | 0.078 | 0.510 | 0.354 | 0.310 | 0.459 |
| 5 | `polished_setpoints_tree_Fw` | `shape_gate_failed` | 0.035091 | 0.001940 | 0.978 | 63.898 | 32.266 | 0.008 | 0.036 | 0.139 | 0.392 | 0.070 | 0.540 |
| 6 | `polished_setpoints_feedforward_Fw` | `shape_gate_failed` | 0.036872 | 0.003768 | 0.971 | 80.076 | 73.998 | -0.012 | 0.008 | 0.497 | 0.378 | 0.000 | 0.653 |
| 7 | `polished_setpoints_periodic_mlp_harmonic_Fw` | `shape_gate_failed` | 0.046156 | 0.004498 | 0.980 | 54.177 | 56.407 | 0.021 | -0.008 | 0.506 | 0.395 | 0.280 | 0.734 |

### Backward

| Rank | Candidate | Label | Raw MAE [deg] | Centered MAE [deg] | FFT Similarity | Harmonic Amp Err [%] | Harmonic Phase Err [deg] | Raw Deriv Corr | Smoothed Deriv Corr | Deriv Sign Rate | Norm Deriv RMSE | Shape Pass Rate | Composite |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `polished_setpoints_periodic_gru_sequence_Bw` | `recommended_candidate` | 0.007298 | 0.002215 | 0.968 | 35.421 | 38.679 | 0.131 | 0.225 | 0.540 | 0.397 | 0.777 | 0.170 |
| 2 | `polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw` | `candidate` | 0.008246 | 0.002154 | 0.967 | 34.621 | 35.321 | 0.084 | 0.227 | 0.526 | 0.411 | 0.798 | 0.214 |
| 3 | `polished_setpoints_wave4_1_mae_robust_loss_Bw` | `candidate` | 0.006179 | 0.002194 | 0.969 | 28.171 | 35.653 | -0.010 | 0.121 | 0.498 | 0.642 | 0.787 | 0.230 |
| 4 | `polished_setpoints_periodic_mlp_harmonic_Bw` | `candidate` | 0.009651 | 0.002413 | 0.969 | 39.879 | 30.522 | -0.002 | 0.206 | 0.496 | 0.424 | 0.745 | 0.321 |
| 5 | `polished_setpoints_tree_Bw` | `shape_gate_failed` | 0.003928 | 0.002318 | 0.962 | 61.347 | 31.794 | 0.012 | 0.042 | 0.141 | 0.417 | 0.202 | 0.239 |
| 6 | `polished_setpoints_feedforward_Bw` | `shape_gate_failed` | 0.010159 | 0.002783 | 0.961 | 64.682 | 71.823 | -0.077 | -0.044 | 0.474 | 0.434 | 0.000 | 0.597 |
| 7 | `polished_setpoints_harmonic_regression_Bw` | `shape_gate_failed` | 0.017296 | 0.002333 | 0.961 | 74.320 | 69.246 | -0.007 | 0.012 | 0.499 | 0.408 | 0.000 | 0.815 |

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

- per-curve metrics: `output\validation_checks\shape_gated_te_curve_reranker\2026-07-20-17-54-14__shape_gated_te_curve_reranker\shape_gated_per_curve_metrics.csv`;
- candidate summary: `output\validation_checks\shape_gated_te_curve_reranker\2026-07-20-17-54-14__shape_gated_te_curve_reranker\shape_gated_candidate_summary.csv`;
- threshold sweep: `output\validation_checks\shape_gated_te_curve_reranker\2026-07-20-17-54-14__shape_gated_te_curve_reranker\shape_gate_threshold_sweep.csv`;
- surface decisions: `output\validation_checks\shape_gated_te_curve_reranker\2026-07-20-17-54-14__shape_gated_te_curve_reranker\shape_gated_surface_decisions.yaml`;
