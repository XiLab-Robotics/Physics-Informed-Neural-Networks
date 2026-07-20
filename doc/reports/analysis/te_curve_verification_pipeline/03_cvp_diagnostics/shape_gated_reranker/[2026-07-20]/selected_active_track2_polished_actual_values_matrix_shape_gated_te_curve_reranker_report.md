# Shape-Gated TE Curve Reranker Report

## Overview

This report applies a reduced forward/backward shape-first gate to the
selected-active `TE Curve Verification Pipeline` candidate set. It does
not run training and does not change the deployable runtime input
contract.

## Scope

- run instance: `2026-07-20-16-49-05__shape_gated_te_curve_reranker`;
- config path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\selected_active_track2_polished_actual_values_matrix.yaml`;
- dataset: `polished_dataset`;
- reduced surfaces: `forward`, `backward`;
- `global` remains paused for this reduced selection pass;

## Gate Thresholds

| Metric | Threshold |
| --- | ---: |
| FFT amplitude similarity | >= 0.820 |
| Derivative correlation | >= 0.700 |
| Mean harmonic amplitude error [%] | <= 55.000 |
| Mean harmonic phase error [deg] | <= 75.000 |
| Peak-to-peak error [%] | <= 35.000 |
| Per-curve shape pass rate | >= 0.600 |

## Surface Decisions

### Forward

| Rank | Candidate | Label | Raw MAE [deg] | Centered MAE [deg] | FFT Similarity | Harmonic Amp Err [%] | Harmonic Phase Err [deg] | Derivative Corr | Shape Pass Rate | Composite |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `polished_actual_values_periodic_gru_sequence_Fw` | `shape_gate_failed` | 0.001676 | 0.001463 | 0.986 | 19.865 | 11.101 | 0.139 | 0.000 | 0.030 |
| 2 | `polished_actual_values_wave4_1_mae_robust_loss_Fw` | `shape_gate_failed` | 0.001681 | 0.001547 | 0.982 | 21.713 | 15.048 | -0.029 | 0.000 | 0.167 |
| 3 | `polished_actual_values_wave4_2_quantile_p10_p50_p90_Fw` | `shape_gate_failed` | 0.001719 | 0.001554 | 0.982 | 25.783 | 15.160 | 0.010 | 0.000 | 0.174 |
| 4 | `polished_actual_values_periodic_mlp_harmonic_Fw` | `shape_gate_failed` | 0.001900 | 0.001507 | 0.984 | 15.446 | 13.643 | -0.009 | 0.000 | 0.404 |
| 5 | `polished_actual_values_tree_Fw` | `shape_gate_failed` | 0.002120 | 0.001919 | 0.978 | 51.180 | 39.559 | -0.030 | 0.000 | 0.594 |
| 6 | `polished_actual_values_feedforward_Fw` | `shape_gate_failed` | 0.002181 | 0.001949 | 0.977 | 64.170 | 67.411 | -0.115 | 0.000 | 0.777 |
| 7 | `polished_actual_values_harmonic_regression_Fw` | `shape_gate_failed` | 0.002355 | 0.001938 | 0.977 | 64.509 | 68.083 | -0.117 | 0.000 | 0.996 |

### Backward

| Rank | Candidate | Label | Raw MAE [deg] | Centered MAE [deg] | FFT Similarity | Harmonic Amp Err [%] | Harmonic Phase Err [deg] | Derivative Corr | Shape Pass Rate | Composite |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | `polished_actual_values_periodic_gru_sequence_Bw` | `shape_gate_failed` | 0.001333 | 0.001222 | 0.992 | 18.469 | 14.176 | 0.267 | 0.053 | 0.000 |
| 2 | `polished_actual_values_wave4_2_quantile_p10_p50_p90_Bw` | `shape_gate_failed` | 0.002188 | 0.002103 | 0.968 | 29.165 | 20.963 | 0.028 | 0.000 | 0.520 |
| 3 | `polished_actual_values_wave4_1_mae_robust_loss_Bw` | `shape_gate_failed` | 0.002315 | 0.002138 | 0.967 | 26.130 | 18.326 | 0.079 | 0.011 | 0.561 |
| 4 | `polished_actual_values_periodic_mlp_harmonic_Bw` | `shape_gate_failed` | 0.002483 | 0.002042 | 0.975 | 22.165 | 19.788 | 0.043 | 0.000 | 0.592 |
| 5 | `polished_actual_values_tree_Bw` | `shape_gate_failed` | 0.002759 | 0.002397 | 0.964 | 50.774 | 51.741 | -0.026 | 0.000 | 0.783 |
| 6 | `polished_actual_values_feedforward_Bw` | `shape_gate_failed` | 0.002769 | 0.002398 | 0.963 | 64.202 | 74.205 | -0.100 | 0.000 | 0.838 |
| 7 | `polished_actual_values_harmonic_regression_Bw` | `shape_gate_failed` | 0.002966 | 0.002372 | 0.963 | 63.064 | 74.103 | -0.122 | 0.000 | 0.995 |

## Interpretation Rules

- `recommended_candidate` is the first active candidate that passes the
  shape gate after block-score reranking.
- `baseline_anchor_only` entries remain useful references, but they do not
  replace the active development baseline in this reduced pass.
- `shape_gate_failed` entries may still have good scalar error, but they
  are demoted until the curve-shape evidence improves.
- `insufficient_evidence` entries could not be evaluated from their
  referenced artifact and must not be promoted until provenance is
  repaired.
- All FFT, centered-shape, derivative, and harmonic diagnostics are
  validation-time evidence only, not deployable runtime corrections.

## Output Artifacts

- per-curve metrics: `output\validation_checks\shape_gated_te_curve_reranker\2026-07-20-16-49-05__shape_gated_te_curve_reranker\shape_gated_per_curve_metrics.csv`;
- candidate summary: `output\validation_checks\shape_gated_te_curve_reranker\2026-07-20-16-49-05__shape_gated_te_curve_reranker\shape_gated_candidate_summary.csv`;
- surface decisions: `output\validation_checks\shape_gated_te_curve_reranker\2026-07-20-16-49-05__shape_gated_te_curve_reranker\shape_gated_surface_decisions.yaml`;
