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
| `simplified_feedforward_Bw` | `simplified_legacy_model_development_registry` | `feedforward` | `Bw` | `backward` |
| `simplified_tree_Bw` | `simplified_legacy_model_development_registry` | `tree` | `Bw` | `backward` |
| `simplified_harmonic_regression_Bw` | `simplified_legacy_model_development_registry` | `harmonic_regression` | `Bw` | `backward` |
| `simplified_periodic_gru_sequence_Bw` | `simplified_legacy_model_development_registry` | `periodic_gru_sequence` | `Bw` | `backward` |

## Forward Comparison

## Backward Comparison

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
| `simplified_feedforward_Bw` | Selected candidate | 0.003586 | 0.004023 | 7.832 | 14.856 |
| `simplified_tree_Bw` | Selected candidate | 0.003258 | 0.003651 | 7.051 | 14.116 |
| `simplified_harmonic_regression_Bw` | Selected candidate | 0.003678 | 0.004012 | 8.058 | 15.071 |
| `simplified_periodic_gru_sequence_Bw` | Surface leader | 0.002392 | 0.002639 | 5.466 | 14.820 |

### simplified_feedforward_Bw

![simplified_feedforward_Bw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_backward_report/simplified_feedforward_bw.png)

### simplified_tree_Bw

![simplified_tree_Bw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_backward_report/simplified_tree_bw.png)

### simplified_harmonic_regression_Bw

![simplified_harmonic_regression_Bw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_backward_report/simplified_harmonic_regression_bw.png)

### simplified_periodic_gru_sequence_Bw

![simplified_periodic_gru_sequence_Bw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_backward_report/simplified_periodic_gru_sequence_bw.png)

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-07-01-22-16__track2_reduced_selected_model_matrix_track2_selected_simplified_dataset_backward_2026_07_06/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-07-01-22-16__track2_reduced_selected_model_matrix_track2_selected_simplified_dataset_backward_2026_07_06\per_condition_metrics.csv`;
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
