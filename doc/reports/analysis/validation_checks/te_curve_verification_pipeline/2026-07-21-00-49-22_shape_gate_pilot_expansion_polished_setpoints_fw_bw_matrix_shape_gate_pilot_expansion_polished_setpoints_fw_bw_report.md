# TE Curve Verification Pipeline Selected Active Model Report

## Overview

This report evaluates only the currently selected active model families
against the repository held-out TE-curve test split. The `global` surface
is intentionally excluded from this reduced decision report.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `selected_active_model_matrix`;
- candidate count: `15`;
- held-out curve count before candidate filtering: `194`;
- percentage-error denominator: `peak_to_peak_truth`;
- evaluated surface: `Bw, Fw`;
- evaluated direction: `backward, forward`;

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | `shape_gate_loss_pilot` | `shape_gate_loss_pilot_periodic_gru_sequence` | `Fw` | `forward` |
| `polished_setpoints_feedforward_Fw` | `polished_setpoints_model_archive` | `feedforward` | `Fw` | `forward` |
| `polished_setpoints_tree_Fw` | `polished_setpoints_model_archive` | `tree` | `Fw` | `forward` |
| `polished_setpoints_harmonic_regression_Fw` | `polished_setpoints_model_archive` | `harmonic_regression` | `Fw` | `forward` |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `polished_setpoints_model_archive` | `periodic_mlp_harmonic` | `Fw` | `forward` |
| `polished_setpoints_periodic_gru_sequence_Fw` | `polished_setpoints_model_archive` | `periodic_gru_sequence` | `Fw` | `forward` |
| `polished_setpoints_wave4_1_mae_robust_loss_Fw` | `polished_setpoints_model_archive` | `wave4_1_mae_robust_loss` | `Fw` | `forward` |
| `polished_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | `polished_setpoints_model_archive` | `wave4_2_quantile_p10_p50_p90` | `Fw` | `forward` |
| `polished_setpoints_feedforward_Bw` | `polished_setpoints_model_archive` | `feedforward` | `Bw` | `backward` |
| `polished_setpoints_tree_Bw` | `polished_setpoints_model_archive` | `tree` | `Bw` | `backward` |
| `polished_setpoints_harmonic_regression_Bw` | `polished_setpoints_model_archive` | `harmonic_regression` | `Bw` | `backward` |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `polished_setpoints_model_archive` | `periodic_mlp_harmonic` | `Bw` | `backward` |
| `polished_setpoints_periodic_gru_sequence_Bw` | `polished_setpoints_model_archive` | `periodic_gru_sequence` | `Bw` | `backward` |
| `polished_setpoints_wave4_1_mae_robust_loss_Bw` | `polished_setpoints_model_archive` | `wave4_1_mae_robust_loss` | `Bw` | `backward` |
| `polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw` | `polished_setpoints_model_archive` | `wave4_2_quantile_p10_p50_p90` | `Bw` | `backward` |

## Exact Model Paths

| Candidate | Family | Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- | --- | --- |
| `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | `shape_gate_loss_pilot_periodic_gru_sequence` | `Fw` | `` | `None` |
| `polished_setpoints_feedforward_Fw` | `feedforward` | `Fw` | `models/polished_dataset/setpoints/feedforward/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/feedforward/forward/python/feedforward-epoch=042-val_mae=0.00168289.ckpt` |
| `polished_setpoints_tree_Fw` | `tree` | `Fw` | `models/polished_dataset/setpoints/tree/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/tree/forward/python/tree_model.pkl` |
| `polished_setpoints_harmonic_regression_Fw` | `harmonic_regression` | `Fw` | `models/polished_dataset/setpoints/harmonic_regression/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/harmonic_regression/forward/python/harmonic_regression-epoch=032-val_mae=0.01714993.ckpt` |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `periodic_mlp_harmonic` | `Fw` | `models/polished_dataset/setpoints/periodic_mlp_harmonic/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/periodic_mlp_harmonic/forward/python/periodic_mlp-epoch=051-val_mae=0.00120808.ckpt` |
| `polished_setpoints_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | `Fw` | `models/polished_dataset/setpoints/periodic_gru_sequence/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/periodic_gru_sequence/forward/python/periodic_gru_sequence-epoch=091-val_mae=0.00183161.ckpt` |
| `polished_setpoints_wave4_1_mae_robust_loss_Fw` | `wave4_1_mae_robust_loss` | `Fw` | `models/polished_dataset/setpoints/wave4_1_mae_robust_loss/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/wave4_1_mae_robust_loss/forward/python/curve_aware_harmonic_residual_offset_probe-epoch=105-val_mae=0.00179190.ckpt` |
| `polished_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | `wave4_2_quantile_p10_p50_p90` | `Fw` | `models/polished_dataset/setpoints/wave4_2_quantile_p10_p50_p90/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/wave4_2_quantile_p10_p50_p90/forward/python/curve_aware_harmonic_residual_offset_probe-epoch=157-val_mae=0.00180121.ckpt` |
| `polished_setpoints_feedforward_Bw` | `feedforward` | `Bw` | `models/polished_dataset/setpoints/feedforward/backward/onnx/model.onnx` | `models/polished_dataset/setpoints/feedforward/backward/python/feedforward-epoch=057-val_mae=0.00164066.ckpt` |
| `polished_setpoints_tree_Bw` | `tree` | `Bw` | `models/polished_dataset/setpoints/tree/backward/onnx/model.onnx` | `models/polished_dataset/setpoints/tree/backward/python/tree_model.pkl` |
| `polished_setpoints_harmonic_regression_Bw` | `harmonic_regression` | `Bw` | `models/polished_dataset/setpoints/harmonic_regression/backward/onnx/model.onnx` | `models/polished_dataset/setpoints/harmonic_regression/backward/python/harmonic_regression-epoch=044-val_mae=0.01715066.ckpt` |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `periodic_mlp_harmonic` | `Bw` | `models/polished_dataset/setpoints/periodic_mlp_harmonic/backward/onnx/model.onnx` | `models/polished_dataset/setpoints/periodic_mlp_harmonic/backward/python/periodic_mlp-epoch=081-val_mae=0.00121896.ckpt` |
| `polished_setpoints_periodic_gru_sequence_Bw` | `periodic_gru_sequence` | `Bw` | `models/polished_dataset/setpoints/periodic_gru_sequence/backward/onnx/model.onnx` | `models/polished_dataset/setpoints/periodic_gru_sequence/backward/python/periodic_gru_sequence-epoch=064-val_mae=0.00189811.ckpt` |
| `polished_setpoints_wave4_1_mae_robust_loss_Bw` | `wave4_1_mae_robust_loss` | `Bw` | `models/polished_dataset/setpoints/wave4_1_mae_robust_loss/backward/onnx/model.onnx` | `models/polished_dataset/setpoints/wave4_1_mae_robust_loss/backward/python/curve_aware_harmonic_residual_offset_probe-epoch=088-val_mae=0.00183184.ckpt` |
| `polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw` | `wave4_2_quantile_p10_p50_p90` | `Bw` | `models/polished_dataset/setpoints/wave4_2_quantile_p10_p50_p90/backward/onnx/model.onnx` | `models/polished_dataset/setpoints/wave4_2_quantile_p10_p50_p90/backward/python/curve_aware_harmonic_residual_offset_probe-epoch=063-val_mae=0.00181729.ckpt` |

## Metric Ranking

| Rank | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `polished_setpoints_wave4_1_mae_robust_loss_Fw` | 0.001767 | 0.002107 | 3.571 | 8.554 |
| 2 | `polished_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | 0.001835 | 0.002193 | 3.733 | 8.562 |
| 3 | `polished_setpoints_periodic_gru_sequence_Fw` | 0.001837 | 0.002179 | 3.751 | 8.248 |
| 4 | `polished_setpoints_periodic_mlp_harmonic_Fw` | 0.001938 | 0.002276 | 3.988 | 10.017 |
| 5 | `polished_setpoints_wave4_1_mae_robust_loss_Bw` | 0.002455 | 0.002881 | 4.191 | 10.373 |
| 6 | `polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw` | 0.002477 | 0.002907 | 4.250 | 10.313 |
| 7 | `polished_setpoints_periodic_mlp_harmonic_Bw` | 0.002470 | 0.002891 | 4.277 | 9.956 |
| 8 | `polished_setpoints_tree_Fw` | 0.002098 | 0.002536 | 4.314 | 8.754 |
| 9 | `polished_setpoints_periodic_gru_sequence_Bw` | 0.002489 | 0.002934 | 4.387 | 10.590 |
| 10 | `polished_setpoints_tree_Bw` | 0.002684 | 0.003182 | 4.716 | 10.570 |
| 11 | `polished_setpoints_feedforward_Bw` | 0.002781 | 0.003291 | 4.940 | 10.609 |
| 12 | `polished_setpoints_feedforward_Fw` | 0.002407 | 0.002885 | 5.036 | 10.659 |
| 13 | `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | 0.002398 | 0.002780 | 5.063 | 9.691 |
| 14 | `polished_setpoints_harmonic_regression_Bw` | 0.017408 | 0.017823 | 37.675 | 77.694 |
| 15 | `polished_setpoints_harmonic_regression_Fw` | 0.017220 | 0.017494 | 38.404 | 78.948 |

## Direction Breakdown

| Direction | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `backward` | `polished_setpoints_wave4_1_mae_robust_loss_Bw` | 0.002455 | 0.002881 | 4.191 | 10.373 |
| `backward` | `polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw` | 0.002477 | 0.002907 | 4.250 | 10.313 |
| `backward` | `polished_setpoints_periodic_mlp_harmonic_Bw` | 0.002470 | 0.002891 | 4.277 | 9.956 |
| `backward` | `polished_setpoints_periodic_gru_sequence_Bw` | 0.002489 | 0.002934 | 4.387 | 10.590 |
| `backward` | `polished_setpoints_tree_Bw` | 0.002684 | 0.003182 | 4.716 | 10.570 |
| `backward` | `polished_setpoints_feedforward_Bw` | 0.002781 | 0.003291 | 4.940 | 10.609 |
| `backward` | `polished_setpoints_harmonic_regression_Bw` | 0.017408 | 0.017823 | 37.675 | 77.694 |
| `forward` | `polished_setpoints_wave4_1_mae_robust_loss_Fw` | 0.001767 | 0.002107 | 3.571 | 8.554 |
| `forward` | `polished_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | 0.001835 | 0.002193 | 3.733 | 8.562 |
| `forward` | `polished_setpoints_periodic_gru_sequence_Fw` | 0.001837 | 0.002179 | 3.751 | 8.248 |
| `forward` | `polished_setpoints_periodic_mlp_harmonic_Fw` | 0.001938 | 0.002276 | 3.988 | 10.017 |
| `forward` | `polished_setpoints_tree_Fw` | 0.002098 | 0.002536 | 4.314 | 8.754 |
| `forward` | `polished_setpoints_feedforward_Fw` | 0.002407 | 0.002885 | 5.036 | 10.659 |
| `forward` | `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | 0.002398 | 0.002780 | 5.063 | 9.691 |
| `forward` | `polished_setpoints_harmonic_regression_Fw` | 0.017220 | 0.017494 | 38.404 | 78.948 |

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-21-00-46-07__shape_gate_pilot_expansion_polished_setpoints_fw_bw_matrix_shape_gate_pilot_expansion_polished_setpoints_fw_bw/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-21-00-46-07__shape_gate_pilot_expansion_polished_setpoints_fw_bw_matrix_shape_gate_pilot_expansion_polished_setpoints_fw_bw\per_condition_metrics.csv`;
- grouped report plot root: `doc\reports\campaign_results\track_2\verification_plots\shape_gate_pilot_expansion_polished_setpoints_fw_bw`;
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
