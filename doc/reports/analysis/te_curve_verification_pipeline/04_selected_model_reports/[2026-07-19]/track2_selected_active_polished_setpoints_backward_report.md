# TE Curve Verification Pipeline Selected Active Model Report

## Overview

This report evaluates only the currently selected active model families
against the repository held-out TE-curve test split. The `global` surface
is intentionally excluded from this reduced decision report.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `selected_active_model_matrix`;
- candidate count: `7`;
- held-out curve count before candidate filtering: `94`;
- percentage-error denominator: `peak_to_peak_truth`;
- evaluated surface: `Bw`;
- evaluated direction: `backward`;

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
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
| 1 | `polished_setpoints_tree_Bw` | 0.003928 | 0.004502 | 7.417 | 14.932 |
| 2 | `polished_setpoints_wave4_1_mae_robust_loss_Bw` | 0.006179 | 0.006697 | 12.394 | 23.419 |
| 3 | `polished_setpoints_periodic_gru_sequence_Bw` | 0.007298 | 0.007811 | 14.582 | 29.283 |
| 4 | `polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw` | 0.008246 | 0.008717 | 16.914 | 29.922 |
| 5 | `polished_setpoints_periodic_mlp_harmonic_Bw` | 0.009651 | 0.010153 | 19.771 | 37.058 |
| 6 | `polished_setpoints_feedforward_Bw` | 0.010159 | 0.010736 | 20.741 | 42.533 |
| 7 | `polished_setpoints_harmonic_regression_Bw` | 0.017296 | 0.017715 | 37.398 | 77.577 |

## Direction Breakdown

| Direction | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `backward` | `polished_setpoints_tree_Bw` | 0.003928 | 0.004502 | 7.417 | 14.932 |
| `backward` | `polished_setpoints_wave4_1_mae_robust_loss_Bw` | 0.006179 | 0.006697 | 12.394 | 23.419 |
| `backward` | `polished_setpoints_periodic_gru_sequence_Bw` | 0.007298 | 0.007811 | 14.582 | 29.283 |
| `backward` | `polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw` | 0.008246 | 0.008717 | 16.914 | 29.922 |
| `backward` | `polished_setpoints_periodic_mlp_harmonic_Bw` | 0.009651 | 0.010153 | 19.771 | 37.058 |
| `backward` | `polished_setpoints_feedforward_Bw` | 0.010159 | 0.010736 | 20.741 | 42.533 |
| `backward` | `polished_setpoints_harmonic_regression_Bw` | 0.017296 | 0.017715 | 37.398 | 77.577 |

## Curve Evidence

Each selected candidate is shown with the same four deterministic held-out operating conditions for this direction.
The dark line is the measured TE curve and the blue line is the model
prediction for the same operating condition.

Shared operating conditions:
- 100 rpm, 300 Nm, 25 C
- 1300 rpm, 1700 Nm, 25 C
- 300 rpm, 200 Nm, 35 C
- 1300 rpm, 1700 Nm, 35 C

| Candidate | Role | Curve MAE [deg] | Curve RMSE [deg] | Mean MPE [%] | P95 MPE [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `polished_setpoints_feedforward_Bw` | Selected candidate | 0.010159 | 0.010736 | 20.741 | 42.533 |
| `polished_setpoints_tree_Bw` | Surface leader | 0.003928 | 0.004502 | 7.417 | 14.932 |
| `polished_setpoints_harmonic_regression_Bw` | Selected candidate | 0.017296 | 0.017715 | 37.398 | 77.577 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | Selected candidate | 0.009651 | 0.010153 | 19.771 | 37.058 |
| `polished_setpoints_periodic_gru_sequence_Bw` | Selected candidate | 0.007298 | 0.007811 | 14.582 | 29.283 |
| `polished_setpoints_wave4_1_mae_robust_loss_Bw` | Selected candidate | 0.006179 | 0.006697 | 12.394 | 23.419 |
| `polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw` | Selected candidate | 0.008246 | 0.008717 | 16.914 | 29.922 |

### polished_setpoints_feedforward_Bw

![polished_setpoints_feedforward_Bw measured-versus-predicted TE collage](assets/track2_selected_active_polished_setpoints_backward_report/polished_setpoints_feedforward_bw.png)

### polished_setpoints_tree_Bw

![polished_setpoints_tree_Bw measured-versus-predicted TE collage](assets/track2_selected_active_polished_setpoints_backward_report/polished_setpoints_tree_bw.png)

### polished_setpoints_harmonic_regression_Bw

![polished_setpoints_harmonic_regression_Bw measured-versus-predicted TE collage](assets/track2_selected_active_polished_setpoints_backward_report/polished_setpoints_harmonic_regression_bw.png)

### polished_setpoints_periodic_mlp_harmonic_Bw

![polished_setpoints_periodic_mlp_harmonic_Bw measured-versus-predicted TE collage](assets/track2_selected_active_polished_setpoints_backward_report/polished_setpoints_periodic_mlp_harmonic_bw.png)

### polished_setpoints_periodic_gru_sequence_Bw

![polished_setpoints_periodic_gru_sequence_Bw measured-versus-predicted TE collage](assets/track2_selected_active_polished_setpoints_backward_report/polished_setpoints_periodic_gru_sequence_bw.png)

### polished_setpoints_wave4_1_mae_robust_loss_Bw

![polished_setpoints_wave4_1_mae_robust_loss_Bw measured-versus-predicted TE collage](assets/track2_selected_active_polished_setpoints_backward_report/polished_setpoints_wave4_1_mae_robust_loss_bw.png)

### polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw

![polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw measured-versus-predicted TE collage](assets/track2_selected_active_polished_setpoints_backward_report/polished_setpoints_wave4_2_quantile_p10_p50_p90_bw.png)

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-19-17-44-49__track2_selected_active_polished_setpoints_matrix_track2_selected_active_polished_setpoints_backward_2026_07_19/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-19-17-44-49__track2_selected_active_polished_setpoints_matrix_track2_selected_active_polished_setpoints_backward_2026_07_19\per_condition_metrics.csv`;
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
