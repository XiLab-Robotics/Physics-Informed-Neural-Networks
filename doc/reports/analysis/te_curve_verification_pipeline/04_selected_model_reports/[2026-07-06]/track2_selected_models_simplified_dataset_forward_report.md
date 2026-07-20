# TE Curve Verification Pipeline Directional Model Comparison

## Overview

This report is the canonical `TE Curve Verification Pipeline` offline comparison between
`RCIM Model-Bank Reproduction`, recovered original, retuned paper-reference model banks, and
repository-owned `Wave 1` and `Wave 2.1` model candidates. It starts from
the current direction-aware comparison matrix.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\simplified_dataset`;
- comparison mode: `reduced_selected_model_matrix`;
- candidate count: `4`;
- held-out curve count before candidate filtering: `97`;
- percentage-error denominator: `peak_to_peak_truth`;
- `Fw` candidates are evaluated only on forward curves;
- `Bw` candidates are evaluated only on backward curves;

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `simplified_feedforward_Fw` | `simplified_legacy_model_development_registry` | `feedforward` | `Fw` | `forward` |
| `simplified_tree_Fw` | `simplified_legacy_model_development_registry` | `tree` | `Fw` | `forward` |
| `simplified_harmonic_regression_Fw` | `simplified_legacy_model_development_registry` | `harmonic_regression` | `Fw` | `forward` |
| `simplified_periodic_gru_sequence_Fw` | `simplified_legacy_model_development_registry` | `periodic_gru_sequence` | `Fw` | `forward` |

## Forward Comparison

## Backward Comparison

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
| `simplified_feedforward_Fw` | Selected candidate | 0.003404 | 0.003855 | 7.551 | 13.029 |
| `simplified_tree_Fw` | Surface leader | 0.003053 | 0.003395 | 6.731 | 11.995 |
| `simplified_harmonic_regression_Fw` | Selected candidate | 0.003230 | 0.003494 | 7.185 | 11.606 |
| `simplified_periodic_gru_sequence_Fw` | Selected candidate | 0.003186 | 0.003438 | 7.077 | 11.974 |

### simplified_feedforward_Fw

![simplified_feedforward_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/simplified_feedforward_fw.png)

### simplified_tree_Fw

![simplified_tree_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/simplified_tree_fw.png)

### simplified_harmonic_regression_Fw

![simplified_harmonic_regression_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/simplified_harmonic_regression_fw.png)

### simplified_periodic_gru_sequence_Fw

![simplified_periodic_gru_sequence_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/simplified_periodic_gru_sequence_fw.png)

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-07-01-20-50__track2_reduced_selected_model_matrix_track2_selected_simplified_dataset_forward_2026_07_06/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-07-01-20-50__track2_reduced_selected_model_matrix_track2_selected_simplified_dataset_forward_2026_07_06\per_condition_metrics.csv`;
- grouped report plot root: `doc\reports\campaign_results\track_2\verification_plots\paused_reduced_selected_model_matrix`;
- grouped report plot count: `0`;

## Interpretation

Rows are ranked by mean percentage error within each source group
and direction. Directional paper-reference, Wave 1, and Wave 2.1
models are never evaluated on the opposite direction. Global Wave
models remain valid on both directions and are therefore shown in
the directional sections and again in the global breakdown.
The `rcim_track1` forward reference banks use the opposite stored
`h0` sign convention relative to the TE Curve Verification Pipeline reconstruction
contract, so the TE Curve Verification Pipeline comparison applies the documented
source-specific `h0` compatibility multiplier before curve
reconstruction.

## Open Gaps

- This remains an offline TE-curve comparison and does not replace the
  future online `Table 9` compensation benchmark.
- The report uses the saved Python model artifacts from `models/`; ONNX
  parity checks remain a separate deployment-readiness task.
