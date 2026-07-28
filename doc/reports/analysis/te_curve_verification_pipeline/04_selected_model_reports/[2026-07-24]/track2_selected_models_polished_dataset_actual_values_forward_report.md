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
| `polished_actual_values_feedforward_Fw` | `polished_actual_values_model_archive` | `feedforward` | `Fw` | `forward` |
| `polished_actual_values_tree_Fw` | `polished_actual_values_model_archive` | `tree` | `Fw` | `forward` |
| `polished_actual_values_harmonic_regression_Fw` | `polished_actual_values_model_archive` | `harmonic_regression` | `Fw` | `forward` |
| `polished_actual_values_periodic_mlp_harmonic_Fw` | `polished_actual_values_model_archive` | `periodic_mlp_harmonic` | `Fw` | `forward` |
| `polished_actual_values_periodic_gru_sequence_Fw` | `polished_actual_values_model_archive` | `periodic_gru_sequence` | `Fw` | `forward` |
| `polished_actual_values_residual_harmonic_gru_sequence_sparse_rcim_Fw` | `polished_actual_values_sparse_rcim_temporal_reference` | `residual_harmonic_gru_sequence_sparse_rcim` | `Fw` | `forward` |
| `polished_actual_values_residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `polished_actual_values_sparse_rcim_temporal_reference` | `residual_harmonic_lstm_sequence_sparse_rcim` | `Fw` | `forward` |
| `polished_actual_values_wave4_1_mae_robust_loss_Fw` | `polished_actual_values_model_archive` | `wave4_1_mae_robust_loss` | `Fw` | `forward` |
| `polished_actual_values_wave4_2_quantile_p10_p50_p90_Fw` | `polished_actual_values_model_archive` | `wave4_2_quantile_p10_p50_p90` | `Fw` | `forward` |

## Exact Model Paths

| Candidate | Family | Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- | --- | --- |
| `polished_actual_values_feedforward_Fw` | `feedforward` | `Fw` | `models/polished_dataset/actual_values/feedforward/forward/onnx/model.onnx` | `models/polished_dataset/actual_values/feedforward/forward/python/feedforward-epoch=181-val_mae=0.00161552.ckpt` |
| `polished_actual_values_tree_Fw` | `tree` | `Fw` | `models/polished_dataset/actual_values/tree/forward/onnx/model.onnx` | `models/polished_dataset/actual_values/tree/forward/python/tree_model.pkl` |
| `polished_actual_values_harmonic_regression_Fw` | `harmonic_regression` | `Fw` | `models/polished_dataset/actual_values/harmonic_regression/forward/onnx/model.onnx` | `models/polished_dataset/actual_values/harmonic_regression/forward/python/harmonic_regression-epoch=073-val_mae=0.00182314.ckpt` |
| `polished_actual_values_periodic_mlp_harmonic_Fw` | `periodic_mlp_harmonic` | `Fw` | `models/polished_dataset/actual_values/periodic_mlp_harmonic/forward/onnx/model.onnx` | `models/polished_dataset/actual_values/periodic_mlp_harmonic/forward/python/periodic_mlp-epoch=045-val_mae=0.00131065.ckpt` |
| `polished_actual_values_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | `Fw` | `models/polished_dataset/actual_values/periodic_gru_sequence/forward/onnx/model.onnx` | `models/polished_dataset/actual_values/periodic_gru_sequence/forward/python/periodic_gru_sequence-epoch=200-val_mae=0.00150079.ckpt` |
| `polished_actual_values_residual_harmonic_gru_sequence_sparse_rcim_Fw` | `residual_harmonic_gru_sequence_sparse_rcim` | `Fw` | `models/polished_dataset/actual_values/residual_harmonic_gru_sequence_sparse_rcim/forward/onnx/model.onnx` | `models/polished_dataset/actual_values/residual_harmonic_gru_sequence_sparse_rcim/forward/python/residual_harmonic_gru_sequence-epoch=170-val_mae=0.00195142.ckpt` |
| `polished_actual_values_residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `residual_harmonic_lstm_sequence_sparse_rcim` | `Fw` | `models/polished_dataset/actual_values/residual_harmonic_lstm_sequence_sparse_rcim/forward/onnx/model.onnx` | `models/polished_dataset/actual_values/residual_harmonic_lstm_sequence_sparse_rcim/forward/python/residual_harmonic_lstm_sequence-epoch=219-val_mae=0.00195141.ckpt` |
| `polished_actual_values_wave4_1_mae_robust_loss_Fw` | `wave4_1_mae_robust_loss` | `Fw` | `models/polished_dataset/actual_values/wave4_1_mae_robust_loss/forward/onnx/model.onnx` | `models/polished_dataset/actual_values/wave4_1_mae_robust_loss/forward/python/curve_aware_harmonic_residual_offset_probe-epoch=202-val_mae=0.00173420.ckpt` |
| `polished_actual_values_wave4_2_quantile_p10_p50_p90_Fw` | `wave4_2_quantile_p10_p50_p90` | `Fw` | `models/polished_dataset/actual_values/wave4_2_quantile_p10_p50_p90/forward/onnx/model.onnx` | `models/polished_dataset/actual_values/wave4_2_quantile_p10_p50_p90/forward/python/curve_aware_harmonic_residual_offset_probe-epoch=250-val_mae=0.00176755.ckpt` |

## Metric Ranking

| Rank | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `polished_actual_values_wave4_1_mae_robust_loss_Fw` | 0.001681 | 0.002032 | 3.355 | 8.132 |
| 2 | `polished_actual_values_periodic_gru_sequence_Fw` | 0.001676 | 0.002006 | 3.366 | 7.871 |
| 3 | `polished_actual_values_wave4_2_quantile_p10_p50_p90_Fw` | 0.001719 | 0.002071 | 3.453 | 8.191 |
| 4 | `polished_actual_values_residual_harmonic_lstm_sequence_sparse_rcim_Fw` | 0.001858 | 0.002252 | 3.753 | 8.240 |
| 5 | `polished_actual_values_periodic_mlp_harmonic_Fw` | 0.001900 | 0.002239 | 3.891 | 10.013 |
| 6 | `polished_actual_values_residual_harmonic_gru_sequence_sparse_rcim_Fw` | 0.001919 | 0.002312 | 3.901 | 8.189 |
| 7 | `polished_actual_values_tree_Fw` | 0.002120 | 0.002599 | 4.341 | 8.662 |
| 8 | `polished_actual_values_feedforward_Fw` | 0.002181 | 0.002646 | 4.491 | 8.951 |
| 9 | `polished_actual_values_harmonic_regression_Fw` | 0.002355 | 0.002816 | 4.909 | 10.791 |

## Direction Breakdown

| Direction | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `forward` | `polished_actual_values_wave4_1_mae_robust_loss_Fw` | 0.001681 | 0.002032 | 3.355 | 8.132 |
| `forward` | `polished_actual_values_periodic_gru_sequence_Fw` | 0.001676 | 0.002006 | 3.366 | 7.871 |
| `forward` | `polished_actual_values_wave4_2_quantile_p10_p50_p90_Fw` | 0.001719 | 0.002071 | 3.453 | 8.191 |
| `forward` | `polished_actual_values_residual_harmonic_lstm_sequence_sparse_rcim_Fw` | 0.001858 | 0.002252 | 3.753 | 8.240 |
| `forward` | `polished_actual_values_periodic_mlp_harmonic_Fw` | 0.001900 | 0.002239 | 3.891 | 10.013 |
| `forward` | `polished_actual_values_residual_harmonic_gru_sequence_sparse_rcim_Fw` | 0.001919 | 0.002312 | 3.901 | 8.189 |
| `forward` | `polished_actual_values_tree_Fw` | 0.002120 | 0.002599 | 4.341 | 8.662 |
| `forward` | `polished_actual_values_feedforward_Fw` | 0.002181 | 0.002646 | 4.491 | 8.951 |
| `forward` | `polished_actual_values_harmonic_regression_Fw` | 0.002355 | 0.002816 | 4.909 | 10.791 |

## Curve Evidence

Each selected candidate is shown with the same four deterministic held-out operating conditions for this direction.
The dark line is the measured TE curve and the blue line is the model
prediction for the same operating condition.

Shared operating conditions:

- 200 rpm, 300 Nm, 25 C
- 900 rpm, 200 Nm, 30 C
- 700 rpm, 1400 Nm, 30 C
- 600 rpm, 1800 Nm, 35 C

| Candidate | Role | Curve MAE [deg] | Curve RMSE [deg] | Mean MPE [%] | P95 MPE [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `polished_actual_values_feedforward_Fw` | Selected candidate | 0.002181 | 0.002646 | 4.491 | 8.951 |
| `polished_actual_values_tree_Fw` | Selected candidate | 0.002120 | 0.002599 | 4.341 | 8.662 |
| `polished_actual_values_harmonic_regression_Fw` | Selected candidate | 0.002355 | 0.002816 | 4.909 | 10.791 |
| `polished_actual_values_periodic_mlp_harmonic_Fw` | Selected candidate | 0.001900 | 0.002239 | 3.891 | 10.013 |
| `polished_actual_values_periodic_gru_sequence_Fw` | Selected candidate | 0.001676 | 0.002006 | 3.366 | 7.871 |
| `polished_actual_values_residual_harmonic_gru_sequence_sparse_rcim_Fw` | Selected candidate | 0.001919 | 0.002312 | 3.901 | 8.189 |
| `polished_actual_values_residual_harmonic_lstm_sequence_sparse_rcim_Fw` | Selected candidate | 0.001858 | 0.002252 | 3.753 | 8.240 |
| `polished_actual_values_wave4_1_mae_robust_loss_Fw` | Surface leader | 0.001681 | 0.002032 | 3.355 | 8.132 |
| `polished_actual_values_wave4_2_quantile_p10_p50_p90_Fw` | Selected candidate | 0.001719 | 0.002071 | 3.453 | 8.191 |

### polished_actual_values_feedforward_Fw

![polished_actual_values_feedforward_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_actual_values_forward_report/polished_actual_values_feedforward_fw.png)

### polished_actual_values_tree_Fw

![polished_actual_values_tree_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_actual_values_forward_report/polished_actual_values_tree_fw.png)

### polished_actual_values_harmonic_regression_Fw

![polished_actual_values_harmonic_regression_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_actual_values_forward_report/polished_actual_values_harmonic_regression_fw.png)

### polished_actual_values_periodic_mlp_harmonic_Fw

![polished_actual_values_periodic_mlp_harmonic_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_actual_values_forward_report/polished_actual_values_periodic_mlp_harmonic_fw.png)

### polished_actual_values_periodic_gru_sequence_Fw

![polished_actual_values_periodic_gru_sequence_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_actual_values_forward_report/polished_actual_values_periodic_gru_sequence_fw.png)

### polished_actual_values_residual_harmonic_gru_sequence_sparse_rcim_Fw

![polished_actual_values_residual_harmonic_gru_sequence_sparse_rcim_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_actual_values_forward_report/polished_actual_values_residual_harmonic_gru_sequence_sparse_rcim_fw.png)

### polished_actual_values_residual_harmonic_lstm_sequence_sparse_rcim_Fw

![polished_actual_values_residual_harmonic_lstm_sequence_sparse_rcim_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_actual_values_forward_report/polished_actual_values_residual_harmonic_lstm_sequence_sparse_rcim_fw.png)

### polished_actual_values_wave4_1_mae_robust_loss_Fw

![polished_actual_values_wave4_1_mae_robust_loss_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_actual_values_forward_report/polished_actual_values_wave4_1_mae_robust_loss_fw.png)

### polished_actual_values_wave4_2_quantile_p10_p50_p90_Fw

![polished_actual_values_wave4_2_quantile_p10_p50_p90_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_actual_values_forward_report/polished_actual_values_wave4_2_quantile_p10_p50_p90_fw.png)

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-24-13-37-33__track2_selected_active_polished_actual_values_matrix_track2_selected_polished_dataset_actual_values_forward_2026_07_24_13_30_33/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-24-13-37-33__track2_selected_active_polished_actual_values_matrix_track2_selected_polished_dataset_actual_values_forward_2026_07_24_13_30_33\per_condition_metrics.csv`;
- grouped report plot root: `doc\reports\campaign_results\track_2\verification_plots\selected_active_model_matrix`;
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
