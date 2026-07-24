# Shape-Gated TE Curve Reranker Report

## Overview

This report applies a reduced shape-first gate to the
selected-active `TE Curve Verification Pipeline` candidate set. It does
not run training and does not change the deployable runtime input
contract.

## Scope

- run instance: `2026-07-24-14-31-25__shape_gated_te_curve_reranker`;
- config path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\selected_active_track2_simplified_setpoints_matrix.yaml`;
- dataset: `simplified_dataset`;
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
| 1 | `simplified_setpoints_periodic_mlp_harmonic_Fw` | `recommended_candidate` | 0.003111 | 0.001170 | 0.990 | 14.714 | 12.225 | 0.158 | 0.331 | 0.550 | 0.316 | 0.969 | 0.006 |
| 2 | `simplified_setpoints_periodic_gru_sequence_Fw` | `candidate` | 0.003153 | 0.001169 | 0.990 | 21.803 | 12.117 | 0.151 | 0.306 | 0.548 | 0.316 | 0.969 | 0.021 |
| 3 | `simplified_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | `candidate` | 0.003377 | 0.001251 | 0.988 | 28.374 | 19.212 | 0.134 | 0.290 | 0.540 | 0.318 | 0.907 | 0.079 |
| 4 | `simplified_setpoints_wave4_1_mae_robust_loss_Fw` | `candidate` | 0.003371 | 0.001256 | 0.988 | 31.601 | 18.009 | 0.131 | 0.284 | 0.539 | 0.317 | 0.959 | 0.080 |
| 5 | `simplified_setpoints_tree_Fw` | `shape_gate_failed` | 0.003065 | 0.001521 | 0.984 | 58.805 | 21.109 | 0.012 | 0.054 | 0.207 | 0.334 | 0.340 | 0.347 |
| 6 | `simplified_setpoints_feedforward_Fw` | `shape_gate_failed` | 0.003438 | 0.001761 | 0.981 | 75.182 | 79.089 | 0.018 | 0.039 | 0.506 | 0.320 | 0.000 | 0.366 |
| 7 | `simplified_setpoints_harmonic_regression_Fw` | `shape_gate_failed` | 0.018064 | 0.001686 | 0.981 | 75.051 | 66.672 | 0.018 | 0.038 | 0.506 | 0.320 | 0.000 | 0.883 |

### Backward

| Rank | Candidate | Label | Raw MAE [deg] | Centered MAE [deg] | FFT Similarity | Harmonic Amp Err [%] | Harmonic Phase Err [deg] | Raw Deriv Corr | Smoothed Deriv Corr | Deriv Sign Rate | Norm Deriv RMSE | Shape Pass Rate | Composite |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `simplified_setpoints_periodic_gru_sequence_Bw` | `recommended_candidate` | 0.003364 | 0.001484 | 0.985 | 24.784 | 19.330 | 0.181 | 0.323 | 0.559 | 0.338 | 0.928 | 0.004 |
| 2 | `simplified_setpoints_periodic_mlp_harmonic_Bw` | `candidate` | 0.003842 | 0.001501 | 0.984 | 23.890 | 19.648 | 0.165 | 0.302 | 0.552 | 0.338 | 0.887 | 0.045 |
| 3 | `simplified_setpoints_wave4_2_quantile_p10_p50_p90_Bw` | `candidate` | 0.003473 | 0.001516 | 0.981 | 24.184 | 28.934 | 0.152 | 0.290 | 0.548 | 0.338 | 0.948 | 0.060 |
| 4 | `simplified_setpoints_wave4_1_mae_robust_loss_Bw` | `candidate` | 0.003519 | 0.001554 | 0.981 | 30.574 | 26.141 | 0.146 | 0.275 | 0.546 | 0.339 | 0.938 | 0.079 |
| 5 | `simplified_setpoints_feedforward_Bw` | `shape_gate_failed` | 0.003594 | 0.001871 | 0.975 | 74.786 | 63.642 | 0.016 | 0.034 | 0.505 | 0.342 | 0.000 | 0.349 |
| 6 | `simplified_setpoints_tree_Bw` | `shape_gate_failed` | 0.003345 | 0.001776 | 0.976 | 60.255 | 35.213 | 0.013 | 0.050 | 0.206 | 0.352 | 0.289 | 0.373 |
| 7 | `simplified_setpoints_harmonic_regression_Bw` | `shape_gate_failed` | 0.017958 | 0.001819 | 0.975 | 74.188 | 88.623 | 0.016 | 0.034 | 0.505 | 0.342 | 0.000 | 0.898 |

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

- per-curve metrics: `output\validation_checks\non_mmt_cross_wave_shape_gated\simplified_setpoints\2026-07-24-14-31-25__shape_gated_te_curve_reranker\shape_gated_per_curve_metrics.csv`;
- candidate summary: `output\validation_checks\non_mmt_cross_wave_shape_gated\simplified_setpoints\2026-07-24-14-31-25__shape_gated_te_curve_reranker\shape_gated_candidate_summary.csv`;
- threshold sweep: `output\validation_checks\non_mmt_cross_wave_shape_gated\simplified_setpoints\2026-07-24-14-31-25__shape_gated_te_curve_reranker\shape_gate_threshold_sweep.csv`;
- surface decisions: `output\validation_checks\non_mmt_cross_wave_shape_gated\simplified_setpoints\2026-07-24-14-31-25__shape_gated_te_curve_reranker\shape_gated_surface_decisions.yaml`;
