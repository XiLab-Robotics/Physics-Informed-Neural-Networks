# TE Curve Verification Pipeline Selected Active Model Report

## Overview

This report evaluates only the currently selected active model families
against the repository held-out TE-curve test split. The `global` surface
is intentionally excluded from this reduced decision report.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\simplified_dataset`;
- comparison mode: `selected_active_model_matrix`;
- candidate count: `7`;
- held-out curve count before candidate filtering: `97`;
- percentage-error denominator: `peak_to_peak_truth`;
- evaluated surface: `Fw`;
- evaluated direction: `forward`;

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `simplified_setpoints_feedforward_Fw` | `simplified_setpoints_model_archive` | `feedforward` | `Fw` | `forward` |
| `simplified_setpoints_tree_Fw` | `simplified_setpoints_model_archive` | `tree` | `Fw` | `forward` |
| `simplified_setpoints_harmonic_regression_Fw` | `simplified_setpoints_model_archive` | `harmonic_regression` | `Fw` | `forward` |
| `simplified_setpoints_periodic_mlp_harmonic_Fw` | `simplified_setpoints_model_archive` | `periodic_mlp_harmonic` | `Fw` | `forward` |
| `simplified_setpoints_periodic_gru_sequence_Fw` | `simplified_setpoints_model_archive` | `periodic_gru_sequence` | `Fw` | `forward` |
| `simplified_setpoints_wave4_1_mae_robust_loss_Fw` | `simplified_setpoints_model_archive` | `wave4_1_mae_robust_loss` | `Fw` | `forward` |
| `simplified_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | `simplified_setpoints_model_archive` | `wave4_2_quantile_p10_p50_p90` | `Fw` | `forward` |

## Exact Model Paths

| Candidate | Family | Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- | --- | --- |
| `simplified_setpoints_feedforward_Fw` | `feedforward` | `Fw` | `models/simplified_dataset/setpoints/feedforward/forward/onnx/model.onnx` | `models/simplified_dataset/setpoints/feedforward/forward/python/feedforward-epoch=057-val_mae=0.00299942.ckpt` |
| `simplified_setpoints_tree_Fw` | `tree` | `Fw` | `models/simplified_dataset/setpoints/tree/forward/onnx/model.onnx` | `models/simplified_dataset/setpoints/tree/forward/python/tree_model.pkl` |
| `simplified_setpoints_harmonic_regression_Fw` | `harmonic_regression` | `Fw` | `models/simplified_dataset/setpoints/harmonic_regression/forward/onnx/model.onnx` | `models/simplified_dataset/setpoints/harmonic_regression/forward/python/harmonic_regression-epoch=033-val_mae=0.01699562.ckpt` |
| `simplified_setpoints_periodic_mlp_harmonic_Fw` | `periodic_mlp_harmonic` | `Fw` | `models/simplified_dataset/setpoints/periodic_mlp_harmonic/forward/onnx/model.onnx` | `models/simplified_dataset/setpoints/periodic_mlp_harmonic/forward/python/periodic_mlp-epoch=055-val_mae=0.00280280.ckpt` |
| `simplified_setpoints_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | `Fw` | `models/simplified_dataset/setpoints/periodic_gru_sequence/forward/onnx/model.onnx` | `models/simplified_dataset/setpoints/periodic_gru_sequence/forward/python/periodic_gru_sequence-epoch=056-val_mae=0.00353205.ckpt` |
| `simplified_setpoints_wave4_1_mae_robust_loss_Fw` | `wave4_1_mae_robust_loss` | `Fw` | `models/simplified_dataset/setpoints/wave4_1_mae_robust_loss/forward/onnx/model.onnx` | `models/simplified_dataset/setpoints/wave4_1_mae_robust_loss/forward/python/curve_aware_harmonic_residual_offset_probe-epoch=085-val_mae=0.00364418.ckpt` |
| `simplified_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | `wave4_2_quantile_p10_p50_p90` | `Fw` | `models/simplified_dataset/setpoints/wave4_2_quantile_p10_p50_p90/forward/onnx/model.onnx` | `models/simplified_dataset/setpoints/wave4_2_quantile_p10_p50_p90/forward/python/curve_aware_harmonic_residual_offset_probe-epoch=098-val_mae=0.00349706.ckpt` |

## Metric Ranking

| Rank | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `simplified_setpoints_tree_Fw` | 0.003065 | 0.003435 | 6.740 | 11.934 |
| 2 | `simplified_setpoints_periodic_mlp_harmonic_Fw` | 0.003111 | 0.003363 | 6.899 | 11.570 |
| 3 | `simplified_setpoints_periodic_gru_sequence_Fw` | 0.003153 | 0.003412 | 7.004 | 12.187 |
| 4 | `simplified_setpoints_wave4_1_mae_robust_loss_Fw` | 0.003371 | 0.003640 | 7.482 | 13.794 |
| 5 | `simplified_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | 0.003377 | 0.003645 | 7.512 | 14.422 |
| 6 | `simplified_setpoints_feedforward_Fw` | 0.003438 | 0.003872 | 7.631 | 14.406 |
| 7 | `simplified_setpoints_harmonic_regression_Fw` | 0.018064 | 0.018299 | 41.176 | 78.839 |

## Direction Breakdown

| Direction | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `forward` | `simplified_setpoints_tree_Fw` | 0.003065 | 0.003435 | 6.740 | 11.934 |
| `forward` | `simplified_setpoints_periodic_mlp_harmonic_Fw` | 0.003111 | 0.003363 | 6.899 | 11.570 |
| `forward` | `simplified_setpoints_periodic_gru_sequence_Fw` | 0.003153 | 0.003412 | 7.004 | 12.187 |
| `forward` | `simplified_setpoints_wave4_1_mae_robust_loss_Fw` | 0.003371 | 0.003640 | 7.482 | 13.794 |
| `forward` | `simplified_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | 0.003377 | 0.003645 | 7.512 | 14.422 |
| `forward` | `simplified_setpoints_feedforward_Fw` | 0.003438 | 0.003872 | 7.631 | 14.406 |
| `forward` | `simplified_setpoints_harmonic_regression_Fw` | 0.018064 | 0.018299 | 41.176 | 78.839 |

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
| `simplified_setpoints_feedforward_Fw` | Selected candidate | 0.003438 | 0.003872 | 7.631 | 14.406 |
| `simplified_setpoints_tree_Fw` | Surface leader | 0.003065 | 0.003435 | 6.740 | 11.934 |
| `simplified_setpoints_harmonic_regression_Fw` | Selected candidate | 0.018064 | 0.018299 | 41.176 | 78.839 |
| `simplified_setpoints_periodic_mlp_harmonic_Fw` | Selected candidate | 0.003111 | 0.003363 | 6.899 | 11.570 |
| `simplified_setpoints_periodic_gru_sequence_Fw` | Selected candidate | 0.003153 | 0.003412 | 7.004 | 12.187 |
| `simplified_setpoints_wave4_1_mae_robust_loss_Fw` | Selected candidate | 0.003371 | 0.003640 | 7.482 | 13.794 |
| `simplified_setpoints_wave4_2_quantile_p10_p50_p90_Fw` | Selected candidate | 0.003377 | 0.003645 | 7.512 | 14.422 |

### simplified_setpoints_feedforward_Fw

![simplified_setpoints_feedforward_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_setpoints_forward_report/simplified_setpoints_feedforward_fw.png)

### simplified_setpoints_tree_Fw

![simplified_setpoints_tree_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_setpoints_forward_report/simplified_setpoints_tree_fw.png)

### simplified_setpoints_harmonic_regression_Fw

![simplified_setpoints_harmonic_regression_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_setpoints_forward_report/simplified_setpoints_harmonic_regression_fw.png)

### simplified_setpoints_periodic_mlp_harmonic_Fw

![simplified_setpoints_periodic_mlp_harmonic_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_setpoints_forward_report/simplified_setpoints_periodic_mlp_harmonic_fw.png)

### simplified_setpoints_periodic_gru_sequence_Fw

![simplified_setpoints_periodic_gru_sequence_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_setpoints_forward_report/simplified_setpoints_periodic_gru_sequence_fw.png)

### simplified_setpoints_wave4_1_mae_robust_loss_Fw

![simplified_setpoints_wave4_1_mae_robust_loss_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_setpoints_forward_report/simplified_setpoints_wave4_1_mae_robust_loss_fw.png)

### simplified_setpoints_wave4_2_quantile_p10_p50_p90_Fw

![simplified_setpoints_wave4_2_quantile_p10_p50_p90_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_setpoints_forward_report/simplified_setpoints_wave4_2_quantile_p10_p50_p90_fw.png)

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-24-13-34-22__track2_selected_active_simplified_setpoints_matrix_track2_selected_simplified_dataset_setpoints_forward_2026_07_24_13_30_33/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-24-13-34-22__track2_selected_active_simplified_setpoints_matrix_track2_selected_simplified_dataset_setpoints_forward_2026_07_24_13_30_33\per_condition_metrics.csv`;
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
