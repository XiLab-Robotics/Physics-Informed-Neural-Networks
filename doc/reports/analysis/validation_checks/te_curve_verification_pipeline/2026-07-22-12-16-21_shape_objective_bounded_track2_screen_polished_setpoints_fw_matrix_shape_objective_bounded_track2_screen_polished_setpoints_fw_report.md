# TE Curve Verification Pipeline Selected Active Model Report

## Overview

This report evaluates only the currently selected active model families
against the repository held-out TE-curve test split. The `global` surface
is intentionally excluded from this reduced decision report.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `selected_active_model_matrix`;
- candidate count: `3`;
- held-out curve count before candidate filtering: `100`;
- percentage-error denominator: `peak_to_peak_truth`;
- evaluated surface: `Fw`;
- evaluated direction: `forward`;

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `shape_objective_periodic_mlp_harmonic_Fw` | `shape_objective_followup` | `shape_objective_periodic_mlp_harmonic_fw` | `Fw` | `forward` |
| `polished_setpoints_periodic_gru_sequence_Fw` | `polished_setpoints_model_archive` | `periodic_gru_sequence` | `Fw` | `forward` |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `polished_setpoints_model_archive` | `periodic_mlp_harmonic` | `Fw` | `forward` |

## Exact Model Paths

| Candidate | Family | Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- | --- | --- |
| `shape_objective_periodic_mlp_harmonic_Fw` | `shape_objective_periodic_mlp_harmonic_fw` | `Fw` | `` | `None` |
| `polished_setpoints_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | `Fw` | `models/polished_dataset/setpoints/periodic_gru_sequence/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/periodic_gru_sequence/forward/python/periodic_gru_sequence-epoch=091-val_mae=0.00183161.ckpt` |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `periodic_mlp_harmonic` | `Fw` | `models/polished_dataset/setpoints/periodic_mlp_harmonic/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/periodic_mlp_harmonic/forward/python/periodic_mlp-epoch=051-val_mae=0.00120808.ckpt` |

## Metric Ranking

| Rank | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `polished_setpoints_periodic_gru_sequence_Fw` | 0.001837 | 0.002179 | 3.751 | 8.248 |
| 2 | `polished_setpoints_periodic_mlp_harmonic_Fw` | 0.001938 | 0.002276 | 3.988 | 10.017 |
| 3 | `shape_objective_periodic_mlp_harmonic_Fw` | 0.002035 | 0.002412 | 4.222 | 10.956 |

## Direction Breakdown

| Direction | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `forward` | `polished_setpoints_periodic_gru_sequence_Fw` | 0.001837 | 0.002179 | 3.751 | 8.248 |
| `forward` | `polished_setpoints_periodic_mlp_harmonic_Fw` | 0.001938 | 0.002276 | 3.988 | 10.017 |
| `forward` | `shape_objective_periodic_mlp_harmonic_Fw` | 0.002035 | 0.002412 | 4.222 | 10.956 |

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-22-12-15-43__shape_objective_bounded_track2_screen_polished_setpoints_fw_matrix_shape_objective_bounded_track2_screen_polished_setpoints_fw/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-22-12-15-43__shape_objective_bounded_track2_screen_polished_setpoints_fw_matrix_shape_objective_bounded_track2_screen_polished_setpoints_fw\per_condition_metrics.csv`;
- grouped report plot root: `doc\reports\campaign_results\track_2\verification_plots\shape_objective_bounded_track2_screen_polished_setpoints_fw`;
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
