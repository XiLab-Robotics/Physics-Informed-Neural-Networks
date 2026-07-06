# TE Curve Verification Pipeline Directional Model Comparison

## Overview

This report is the reduced selected-model `TE Curve Verification Pipeline`
offline comparison for one dataset and one direction. It includes only the
active selected model-development candidates plus reduced baseline anchors.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\simplified_dataset`;
- comparison mode: `reduced_selected_model_matrix`;
- candidate count: `9`;
- held-out curve count before candidate filtering: `97`;
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
| `wave52b_offset_centered_shape_harmonic_Fw` | 0.058653 | 0.058748 | 128.839 | 229.455 |

### Polished Model-Development Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `polished_harmonic_regression_Fw` | 0.003230 | 0.003494 | 7.185 | 11.606 |
| `polished_tree_Fw` | 0.066315 | 0.066379 | 145.420 | 257.447 |
| `polished_wave4_3_mixture_density_k3_Fw` | 0.083190 | 0.083242 | 182.913 | 318.098 |
| `polished_periodic_mlp_harmonic_Fw` | 0.085830 | 0.085880 | 188.420 | 317.347 |
| `polished_periodic_gru_sequence_Fw` | 0.086270 | 0.086329 | 189.713 | 317.966 |
| `polished_feedforward_Fw` | 0.086931 | 0.087006 | 190.832 | 319.925 |

### Polished RCIM Model-Bank Reproduction Forward Models

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `polished_rcim_model_bank_reproduction_GBM19_Fw` | 0.035161 | 0.035261 | 77.115 | 138.019 |
| `polished_rcim_model_bank_reproduction_ET19_Fw` | 0.038726 | 0.038810 | 85.150 | 149.396 |

## Backward Comparison

## Curve Evidence

Each selected candidate is shown with four deterministic held-out curves.
The dark line is the measured TE curve and the blue line is the model
prediction for the same operating condition.

| Candidate | Role | Curve MAE [deg] | Curve RMSE [deg] | Mean MPE [%] | P95 MPE [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `polished_rcim_model_bank_reproduction_GBM19_Fw` | Selected candidate | 0.035161 | 0.035261 | 77.115 | 138.019 |
| `polished_rcim_model_bank_reproduction_ET19_Fw` | Selected candidate | 0.038726 | 0.038810 | 85.150 | 149.396 |
| `polished_feedforward_Fw` | Selected candidate | 0.086931 | 0.087006 | 190.832 | 319.925 |
| `polished_tree_Fw` | Selected candidate | 0.066315 | 0.066379 | 145.420 | 257.447 |
| `polished_harmonic_regression_Fw` | Surface leader | 0.003230 | 0.003494 | 7.185 | 11.606 |
| `polished_periodic_gru_sequence_Fw` | Selected candidate | 0.086270 | 0.086329 | 189.713 | 317.966 |
| `polished_periodic_mlp_harmonic_Fw` | Selected candidate | 0.085830 | 0.085880 | 188.420 | 317.347 |
| `polished_wave4_3_mixture_density_k3_Fw` | Selected candidate | 0.083190 | 0.083242 | 182.913 | 318.098 |
| `wave52b_offset_centered_shape_harmonic_Fw` | Selected candidate | 0.058653 | 0.058748 | 128.839 | 229.455 |

### polished_rcim_model_bank_reproduction_GBM19_Fw

![polished_rcim_model_bank_reproduction_GBM19_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/polished_rcim_model_bank_reproduction_gbm19_fw.png)

### polished_rcim_model_bank_reproduction_ET19_Fw

![polished_rcim_model_bank_reproduction_ET19_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/polished_rcim_model_bank_reproduction_et19_fw.png)

### polished_feedforward_Fw

![polished_feedforward_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/polished_feedforward_fw.png)

### polished_tree_Fw

![polished_tree_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/polished_tree_fw.png)

### polished_harmonic_regression_Fw

![polished_harmonic_regression_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/polished_harmonic_regression_fw.png)

### polished_periodic_gru_sequence_Fw

![polished_periodic_gru_sequence_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/polished_periodic_gru_sequence_fw.png)

### polished_periodic_mlp_harmonic_Fw

![polished_periodic_mlp_harmonic_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/polished_periodic_mlp_harmonic_fw.png)

### polished_wave4_3_mixture_density_k3_Fw

![polished_wave4_3_mixture_density_k3_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/polished_wave4_3_mixture_density_k3_fw.png)

### wave52b_offset_centered_shape_harmonic_Fw

![wave52b_offset_centered_shape_harmonic_Fw measured-versus-predicted TE collage](assets/track2_selected_models_simplified_dataset_forward_report/wave52b_offset_centered_shape_harmonic_fw.png)

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-06-19-53-27__track2_reduced_selected_model_matrix_track2_selected_simplified_dataset_forward_2026_07_06/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-06-19-53-27__track2_reduced_selected_model_matrix_track2_selected_simplified_dataset_forward_2026_07_06\per_condition_metrics.csv`;
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
