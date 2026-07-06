# TE Curve Verification Pipeline Directional Model Comparison

## Overview

This report is the reduced selected-model `TE Curve Verification Pipeline`
offline comparison for one dataset and one direction. It includes only the
active selected model-development candidates plus reduced baseline anchors.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `reduced_selected_model_matrix`;
- candidate count: `9`;
- held-out curve count before candidate filtering: `100`;
- percentage-error denominator: `peak_to_peak_truth`;
- this reduced report excludes `global` candidates by design;
- only candidates valid for this direction are evaluated.

## Candidate Inventory

| Candidate | Family | Source | Kind | Surface | Valid Directions | Model Source |
| --- | --- | --- | --- | --- | --- | --- |
| `polished_rcim_model_bank_reproduction_GBM19_Fw` | `GBM` | `polished_rcim_model_bank_reproduction` | `track1_reference_bank` | `Fw` | `forward` | `output\validation_checks\rcim_model_bank_reproduction\reference_inventories\forward\gbm_reference_models\reference_inventory.yaml` |
| `polished_rcim_model_bank_reproduction_ET19_Fw` | `ET` | `polished_rcim_model_bank_reproduction` | `track1_reference_bank` | `Fw` | `forward` | `output\validation_checks\rcim_model_bank_reproduction\reference_inventories\forward\et_reference_models\reference_inventory.yaml` |
| `polished_feedforward_Fw` | `feedforward` | `polished_model_development_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\feedforward_fw\latest_family_best.yaml` |
| `polished_tree_Fw` | `tree` | `polished_model_development_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\tree_fw\latest_family_best.yaml` |
| `polished_harmonic_regression_Fw` | `harmonic_regression` | `polished_model_development_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\harmonic_regression_fw\latest_family_best.yaml` |
| `polished_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | `polished_model_development_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\periodic_gru_sequence_fw\latest_family_best.yaml` |
| `polished_periodic_mlp_harmonic_Fw` | `periodic_mlp_harmonic` | `polished_model_development_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\periodic_mlp_harmonic_fw\latest_family_best.yaml` |
| `polished_wave4_3_mixture_density_k3_Fw` | `wave4_3_mixture_density_k3` | `polished_model_development_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\wave4_3_mixture_density_k3_fw\latest_family_best.yaml` |
| `wave52b_offset_centered_shape_harmonic_Fw` | `wave52b_offset_harmonic_guided` | `wave52b_offset_harmonic_guided_registry` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw\latest_family_best.yaml` |

## Forward Comparison

### Wave 5.2B Offset And Harmonic Guided Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_Fw` | 0.001695 | 0.002045 | 3.391 | 8.270 |

### Polished Model-Development Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `polished_periodic_gru_sequence_Fw` | 0.001195 | 0.001461 | 2.559 | 5.193 |
| `polished_wave4_3_mixture_density_k3_Fw` | 0.001528 | 0.001867 | 3.161 | 7.018 |
| `polished_periodic_mlp_harmonic_Fw` | 0.001735 | 0.002062 | 3.511 | 7.554 |
| `polished_tree_Fw` | 0.002125 | 0.002612 | 4.355 | 8.534 |
| `polished_feedforward_Fw` | 0.002130 | 0.002586 | 4.378 | 8.431 |
| `polished_harmonic_regression_Fw` | 0.062598 | 0.062702 | 133.783 | 271.628 |

### Polished RCIM Model-Bank Reproduction Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `polished_rcim_model_bank_reproduction_ET19_Fw` | 0.001155 | 0.001394 | 2.401 | 4.928 |
| `polished_rcim_model_bank_reproduction_GBM19_Fw` | 0.001644 | 0.001903 | 3.449 | 9.961 |

## Backward Comparison

## Curve Evidence

Each selected candidate is shown with four deterministic held-out curves.
The dark line is the measured TE curve and the blue line is the model
prediction for the same operating condition.

| Candidate | Role | Curve MAE [deg] | Curve RMSE [deg] | Mean MPE [%] | P95 MPE [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `polished_rcim_model_bank_reproduction_GBM19_Fw` | Selected candidate | 0.001644 | 0.001903 | 3.449 | 9.961 |
| `polished_rcim_model_bank_reproduction_ET19_Fw` | Surface leader | 0.001155 | 0.001394 | 2.401 | 4.928 |
| `polished_feedforward_Fw` | Selected candidate | 0.002130 | 0.002586 | 4.378 | 8.431 |
| `polished_tree_Fw` | Selected candidate | 0.002125 | 0.002612 | 4.355 | 8.534 |
| `polished_harmonic_regression_Fw` | Selected candidate | 0.062598 | 0.062702 | 133.783 | 271.628 |
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

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-06-19-49-25__track2_reduced_selected_model_matrix_track2_selected_polished_dataset_forward_2026_07_06/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-06-19-49-25__track2_reduced_selected_model_matrix_track2_selected_polished_dataset_forward_2026_07_06\per_condition_metrics.csv`;
- grouped report plot root: `doc\reports\campaign_results\track_2\verification_plots\paused_reduced_selected_model_matrix`;
- grouped report plot count: `0`;

## Interpretation

Rows are ranked by mean percentage error within each source group
and direction. Directional candidates are never evaluated on the opposite
direction in this reduced report. `global` is paused for the active reduced
pipeline and is not included in the candidate inventory.
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
