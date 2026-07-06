# TE Curve Verification Pipeline Directional Model Comparison

## Overview

This report is the canonical `TE Curve Verification Pipeline` offline comparison between
`RCIM Model-Bank Reproduction`, recovered original, retuned paper-reference model banks, and
repository-owned `Wave 1` and `Wave 2.1` model candidates. It starts from
the current direction-aware comparison matrix.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `reduced_selected_model_matrix`;
- candidate count: `9`;
- held-out curve count before candidate filtering: `100`;
- percentage-error denominator: `peak_to_peak_truth`;
- `Fw` candidates are evaluated only on forward curves;
- `Bw` candidates are evaluated only on backward curves;

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `polished_rcim_model_bank_reproduction_GBM19_Fw` | `polished_rcim_model_bank_reproduction` | `GBM` | `Fw` | `forward` |
| `polished_rcim_model_bank_reproduction_ET19_Fw` | `polished_rcim_model_bank_reproduction` | `ET` | `Fw` | `forward` |
| `polished_feedforward_Fw` | `polished_model_development_registry` | `feedforward` | `Fw` | `forward` |
| `polished_tree_Fw` | `polished_model_development_registry` | `tree` | `Fw` | `forward` |
| `polished_harmonic_regression_Fw` | `polished_model_development_registry` | `harmonic_regression` | `Fw` | `forward` |
| `polished_periodic_gru_sequence_Fw` | `polished_model_development_registry` | `periodic_gru_sequence` | `Fw` | `forward` |
| `polished_periodic_mlp_harmonic_Fw` | `polished_model_development_registry` | `periodic_mlp_harmonic` | `Fw` | `forward` |
| `polished_wave4_3_mixture_density_k3_Fw` | `polished_model_development_registry` | `wave4_3_mixture_density_k3` | `Fw` | `forward` |
| `wave52b_offset_centered_shape_harmonic_Fw` | `wave52b_offset_harmonic_guided_registry` | `wave52b_offset_harmonic_guided` | `Fw` | `forward` |

## Forward Comparison

### Wave 5.2B Offset And Harmonic Guided Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_Fw` | 0.001695 | 0.002045 | 3.391 | 8.270 |

### Polished Model-Development Forward And Global Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `polished_periodic_gru_sequence_Fw` | 0.001195 | 0.001461 | 2.559 | 5.193 |
| `polished_wave4_3_mixture_density_k3_Fw` | 0.001528 | 0.001867 | 3.161 | 7.018 |
| `polished_periodic_mlp_harmonic_Fw` | 0.001735 | 0.002062 | 3.511 | 7.554 |
| `polished_tree_Fw` | 0.002125 | 0.002612 | 4.355 | 8.534 |
| `polished_feedforward_Fw` | 0.002130 | 0.002586 | 4.378 | 8.431 |
| `polished_harmonic_regression_Fw` | 0.003766 | 0.004246 | 8.148 | 15.111 |

### Polished RCIM Model-Bank Reproduction Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `polished_rcim_model_bank_reproduction_ET19_Fw` | 0.001155 | 0.001394 | 2.401 | 4.928 |
| `polished_rcim_model_bank_reproduction_GBM19_Fw` | 0.001644 | 0.001903 | 3.449 | 9.961 |

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
| `polished_rcim_model_bank_reproduction_GBM19_Fw` | Selected candidate | 0.001644 | 0.001903 | 3.449 | 9.961 |
| `polished_rcim_model_bank_reproduction_ET19_Fw` | Surface leader | 0.001155 | 0.001394 | 2.401 | 4.928 |
| `polished_feedforward_Fw` | Selected candidate | 0.002130 | 0.002586 | 4.378 | 8.431 |
| `polished_tree_Fw` | Selected candidate | 0.002125 | 0.002612 | 4.355 | 8.534 |
| `polished_harmonic_regression_Fw` | Selected candidate | 0.003766 | 0.004246 | 8.148 | 15.111 |
| `polished_periodic_gru_sequence_Fw` | Selected candidate | 0.001195 | 0.001461 | 2.559 | 5.193 |
| `polished_periodic_mlp_harmonic_Fw` | Selected candidate | 0.001735 | 0.002062 | 3.511 | 7.554 |
| `polished_wave4_3_mixture_density_k3_Fw` | Selected candidate | 0.001528 | 0.001867 | 3.161 | 7.018 |
| `wave52b_offset_centered_shape_harmonic_Fw` | Selected candidate | 0.001695 | 0.002045 | 3.391 | 8.270 |

### polished_rcim_model_bank_reproduction_GBM19_Fw

![polished_rcim_model_bank_reproduction_GBM19_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_forward_report/polished_rcim_model_bank_reproduction_gbm19_fw.png)

### polished_rcim_model_bank_reproduction_ET19_Fw

![polished_rcim_model_bank_reproduction_ET19_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_forward_report/polished_rcim_model_bank_reproduction_et19_fw.png)

### polished_feedforward_Fw

![polished_feedforward_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_forward_report/polished_feedforward_fw.png)

### polished_tree_Fw

![polished_tree_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_forward_report/polished_tree_fw.png)

### polished_harmonic_regression_Fw

![polished_harmonic_regression_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_forward_report/polished_harmonic_regression_fw.png)

### polished_periodic_gru_sequence_Fw

![polished_periodic_gru_sequence_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_forward_report/polished_periodic_gru_sequence_fw.png)

### polished_periodic_mlp_harmonic_Fw

![polished_periodic_mlp_harmonic_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_forward_report/polished_periodic_mlp_harmonic_fw.png)

### polished_wave4_3_mixture_density_k3_Fw

![polished_wave4_3_mixture_density_k3_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_forward_report/polished_wave4_3_mixture_density_k3_fw.png)

### wave52b_offset_centered_shape_harmonic_Fw

![wave52b_offset_centered_shape_harmonic_Fw measured-versus-predicted TE collage](assets/track2_selected_models_polished_dataset_forward_report/wave52b_offset_centered_shape_harmonic_fw.png)

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-07-01-16-59__track2_reduced_selected_model_matrix_track2_selected_polished_dataset_forward_2026_07_06/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-07-01-16-59__track2_reduced_selected_model_matrix_track2_selected_polished_dataset_forward_2026_07_06\per_condition_metrics.csv`;
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
