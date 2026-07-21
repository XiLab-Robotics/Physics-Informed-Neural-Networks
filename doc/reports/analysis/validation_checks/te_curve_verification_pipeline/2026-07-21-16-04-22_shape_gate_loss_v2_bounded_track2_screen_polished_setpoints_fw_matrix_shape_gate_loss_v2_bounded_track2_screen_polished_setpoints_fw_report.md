# TE Curve Verification Pipeline Selected Active Model Report

## Overview

This report evaluates only the currently selected active model families
against the repository held-out TE-curve test split. The `global` surface
is intentionally excluded from this reduced decision report.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `selected_active_model_matrix`;
- candidate count: `9`;
- held-out curve count before candidate filtering: `100`;
- percentage-error denominator: `peak_to_peak_truth`;
- evaluated surface: `Fw`;
- evaluated direction: `forward`;

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_Fw` | `shape_gate_loss_v2_checkpoint_selection` | `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw` | `Fw` | `forward` |
| `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | `shape_gate_loss_pilot` | `shape_gate_loss_pilot_periodic_gru_sequence` | `Fw` | `forward` |
| `polished_setpoints_feedforward_Fw` | `polished_setpoints_model_archive` | `feedforward` | `Fw` | `forward` |
| `polished_setpoints_tree_Fw` | `polished_setpoints_model_archive` | `tree` | `Fw` | `forward` |
| `polished_setpoints_harmonic_regression_Fw` | `polished_setpoints_model_archive` | `harmonic_regression` | `Fw` | `forward` |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `polished_setpoints_model_archive` | `periodic_mlp_harmonic` | `Fw` | `forward` |
| `polished_setpoints_periodic_gru_sequence_Fw` | `polished_setpoints_model_archive` | `periodic_gru_sequence` | `Fw` | `forward` |
| `polished_setpoints_wave4_1_mae_robust_loss_Fw` | `polished_setpoints_model_archive` | `wave4_1_mae_robust_loss` | `Fw` | `forward` |
| `polished_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | `polished_setpoints_model_archive` | `wave4_2_quantile_p10_p50_p90` | `Fw` | `forward` |

## Exact Model Paths

| Candidate | Family | Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- | --- | --- |
| `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_Fw` | `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw` | `Fw` | `` | `None` |
| `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | `shape_gate_loss_pilot_periodic_gru_sequence` | `Fw` | `` | `None` |
| `polished_setpoints_feedforward_Fw` | `feedforward` | `Fw` | `models/polished_dataset/setpoints/feedforward/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/feedforward/forward/python/feedforward-epoch=042-val_mae=0.00168289.ckpt` |
| `polished_setpoints_tree_Fw` | `tree` | `Fw` | `models/polished_dataset/setpoints/tree/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/tree/forward/python/tree_model.pkl` |
| `polished_setpoints_harmonic_regression_Fw` | `harmonic_regression` | `Fw` | `models/polished_dataset/setpoints/harmonic_regression/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/harmonic_regression/forward/python/harmonic_regression-epoch=032-val_mae=0.01714993.ckpt` |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `periodic_mlp_harmonic` | `Fw` | `models/polished_dataset/setpoints/periodic_mlp_harmonic/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/periodic_mlp_harmonic/forward/python/periodic_mlp-epoch=051-val_mae=0.00120808.ckpt` |
| `polished_setpoints_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | `Fw` | `models/polished_dataset/setpoints/periodic_gru_sequence/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/periodic_gru_sequence/forward/python/periodic_gru_sequence-epoch=091-val_mae=0.00183161.ckpt` |
| `polished_setpoints_wave4_1_mae_robust_loss_Fw` | `wave4_1_mae_robust_loss` | `Fw` | `models/polished_dataset/setpoints/wave4_1_mae_robust_loss/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/wave4_1_mae_robust_loss/forward/python/curve_aware_harmonic_residual_offset_probe-epoch=105-val_mae=0.00179190.ckpt` |
| `polished_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | `wave4_2_quantile_p10_p50_p90` | `Fw` | `models/polished_dataset/setpoints/wave4_2_quantile_p10_p50_p90/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/wave4_2_quantile_p10_p50_p90/forward/python/curve_aware_harmonic_residual_offset_probe-epoch=157-val_mae=0.00180121.ckpt` |

## Metric Ranking

| Rank | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `polished_setpoints_wave4_1_mae_robust_loss_Fw` | 0.001767 | 0.002107 | 3.571 | 8.554 |
| 2 | `polished_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | 0.001835 | 0.002193 | 3.733 | 8.562 |
| 3 | `polished_setpoints_periodic_gru_sequence_Fw` | 0.001837 | 0.002179 | 3.751 | 8.248 |
| 4 | `polished_setpoints_periodic_mlp_harmonic_Fw` | 0.001938 | 0.002276 | 3.988 | 10.017 |
| 5 | `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_Fw` | 0.001973 | 0.002325 | 4.085 | 11.752 |
| 6 | `polished_setpoints_tree_Fw` | 0.002098 | 0.002536 | 4.314 | 8.754 |
| 7 | `polished_setpoints_feedforward_Fw` | 0.002407 | 0.002885 | 5.036 | 10.659 |
| 8 | `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | 0.002398 | 0.002780 | 5.063 | 9.691 |
| 9 | `polished_setpoints_harmonic_regression_Fw` | 0.017220 | 0.017494 | 38.404 | 78.948 |

## Direction Breakdown

| Direction | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `forward` | `polished_setpoints_wave4_1_mae_robust_loss_Fw` | 0.001767 | 0.002107 | 3.571 | 8.554 |
| `forward` | `polished_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | 0.001835 | 0.002193 | 3.733 | 8.562 |
| `forward` | `polished_setpoints_periodic_gru_sequence_Fw` | 0.001837 | 0.002179 | 3.751 | 8.248 |
| `forward` | `polished_setpoints_periodic_mlp_harmonic_Fw` | 0.001938 | 0.002276 | 3.988 | 10.017 |
| `forward` | `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_Fw` | 0.001973 | 0.002325 | 4.085 | 11.752 |
| `forward` | `polished_setpoints_tree_Fw` | 0.002098 | 0.002536 | 4.314 | 8.754 |
| `forward` | `polished_setpoints_feedforward_Fw` | 0.002407 | 0.002885 | 5.036 | 10.659 |
| `forward` | `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | 0.002398 | 0.002780 | 5.063 | 9.691 |
| `forward` | `polished_setpoints_harmonic_regression_Fw` | 0.017220 | 0.017494 | 38.404 | 78.948 |

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-21-16-01-42__shape_gate_loss_v2_bounded_track2_screen_polished_setpoints_fw_matrix_shape_gate_loss_v2_bounded_track2_screen_polished_setpoints_fw/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-21-16-01-42__shape_gate_loss_v2_bounded_track2_screen_polished_setpoints_fw_matrix_shape_gate_loss_v2_bounded_track2_screen_polished_setpoints_fw\per_condition_metrics.csv`;
- grouped report plot root: `doc\reports\campaign_results\track_2\verification_plots\shape_gate_loss_v2_bounded_track2_screen_polished_setpoints_fw`;
- grouped report plot count: `0`;

## Interpretation

Rows are ranked by mean percentage error within this selected-active
surface report. The curve-evidence section uses shared deterministic
held-out operating conditions so visual shape fidelity can be compared
across the selected families.

## Open Gaps

- This remains an offline TE-curve comparison and does not replace the
  future online `Table 9` compensation benchmark.
- RCIM Model-Bank Reproduction remains a separate paper-reference
  benchmark path and is not part of this selected-active model-only
  report.
