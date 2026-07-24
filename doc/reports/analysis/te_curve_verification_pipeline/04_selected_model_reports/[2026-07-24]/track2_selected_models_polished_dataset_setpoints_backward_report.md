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
| 1 | `polished_setpoints_wave4_1_mae_robust_loss_Bw` | 0.002455 | 0.002881 | 4.191 | 10.373 |
| 2 | `polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw` | 0.002477 | 0.002907 | 4.250 | 10.313 |
| 3 | `polished_setpoints_periodic_mlp_harmonic_Bw` | 0.002470 | 0.002891 | 4.277 | 9.956 |
| 4 | `polished_setpoints_periodic_gru_sequence_Bw` | 0.002489 | 0.002934 | 4.387 | 10.590 |
| 5 | `polished_setpoints_tree_Bw` | 0.002684 | 0.003182 | 4.716 | 10.570 |
| 6 | `polished_setpoints_feedforward_Bw` | 0.002781 | 0.003291 | 4.940 | 10.609 |
| 7 | `polished_setpoints_harmonic_regression_Bw` | 0.017408 | 0.017823 | 37.675 | 77.694 |

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
| `polished_setpoints_feedforward_Bw` | Selected candidate | 0.002781 | 0.003291 | 4.940 | 10.609 |
| `polished_setpoints_tree_Bw` | Selected candidate | 0.002684 | 0.003182 | 4.716 | 10.570 |
| `polished_setpoints_harmonic_regression_Bw` | Selected candidate | 0.017408 | 0.017823 | 37.675 | 77.694 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | Selected candidate | 0.002470 | 0.002891 | 4.277 | 9.956 |
| `polished_setpoints_periodic_gru_sequence_Bw` | Selected candidate | 0.002489 | 0.002934 | 4.387 | 10.590 |
| `polished_setpoints_wave4_1_mae_robust_loss_Bw` | Surface leader | 0.002455 | 0.002881 | 4.191 | 10.373 |
| `polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw` | Selected candidate | 0.002477 | 0.002907 | 4.250 | 10.313 |

### polished_setpoints_feedforward_Bw

![polished_setpoints_feedforward_Bw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_setpoints_backward_report/polished_setpoints_feedforward_bw.png)

### polished_setpoints_tree_Bw

![polished_setpoints_tree_Bw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_setpoints_backward_report/polished_setpoints_tree_bw.png)

### polished_setpoints_harmonic_regression_Bw

![polished_setpoints_harmonic_regression_Bw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_setpoints_backward_report/polished_setpoints_harmonic_regression_bw.png)

### polished_setpoints_periodic_mlp_harmonic_Bw

![polished_setpoints_periodic_mlp_harmonic_Bw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_setpoints_backward_report/polished_setpoints_periodic_mlp_harmonic_bw.png)

### polished_setpoints_periodic_gru_sequence_Bw

![polished_setpoints_periodic_gru_sequence_Bw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_setpoints_backward_report/polished_setpoints_periodic_gru_sequence_bw.png)

### polished_setpoints_wave4_1_mae_robust_loss_Bw

![polished_setpoints_wave4_1_mae_robust_loss_Bw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_setpoints_backward_report/polished_setpoints_wave4_1_mae_robust_loss_bw.png)

### polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw

![polished_setpoints_wave4_2_quantile_p10_p50_p90_Bw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_setpoints_backward_report/polished_setpoints_wave4_2_quantile_p10_p50_p90_bw.png)

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-24-13-32-58__track2_selected_active_polished_setpoints_matrix_track2_selected_polished_dataset_setpoints_backward_2026_07_24_13_30_33/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-24-13-32-58__track2_selected_active_polished_setpoints_matrix_track2_selected_polished_dataset_setpoints_backward_2026_07_24_13_30_33\per_condition_metrics.csv`;
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
