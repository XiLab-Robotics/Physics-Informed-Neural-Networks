# TE Curve Verification Pipeline Selected Active Model Report

## Overview

This report evaluates only the currently selected active model families
against the repository held-out TE-curve test split. The `global` surface
is intentionally excluded from this reduced decision report.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `selected_active_model_matrix`;
- candidate count: `1`;
- held-out curve count before candidate filtering: `100`;
- percentage-error denominator: `peak_to_peak_truth`;
- evaluated surface: `Fw`;
- evaluated direction: `forward`;

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | `shape_gate_loss_pilot` | `shape_gate_loss_pilot_periodic_gru_sequence` | `Fw` | `forward` |

## Exact Model Paths

| Candidate | Family | Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- | --- | --- |
| `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | `shape_gate_loss_pilot_periodic_gru_sequence` | `Fw` | `` | `None` |

## Metric Ranking

| Rank | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | 0.002398 | 0.002780 | 5.063 | 9.691 |

## Direction Breakdown

| Direction | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `forward` | `shape_gate_loss_pilot_periodic_gru_sequence_Fw` | 0.002398 | 0.002780 | 5.063 | 9.691 |

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-21-00-18-53__shape_gate_loss_pilot_only_track2_polished_setpoints_fw_matrix_shape_gate_loss_pilot_only_track2_polished_setpoints_fw_input_mode_fixed/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-21-00-18-53__shape_gate_loss_pilot_only_track2_polished_setpoints_fw_matrix_shape_gate_loss_pilot_only_track2_polished_setpoints_fw_input_mode_fixed\per_condition_metrics.csv`;
- grouped report plot root: `doc\reports\campaign_results\track_2\verification_plots\shape_gate_loss_pilot_track2_polished_setpoints_fw`;
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
