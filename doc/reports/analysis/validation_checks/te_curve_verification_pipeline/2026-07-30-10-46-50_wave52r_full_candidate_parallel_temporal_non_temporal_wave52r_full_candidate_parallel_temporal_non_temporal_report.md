# TE Curve Verification Pipeline Directional Model Comparison

## Overview

This report is the canonical `TE Curve Verification Pipeline` offline comparison between
`RCIM Model-Bank Reproduction`, recovered original, retuned paper-reference model banks, and
repository-owned `Wave 1` and `Wave 2.1` model candidates. It starts from
the current direction-aware comparison matrix.

## Dataset And Split

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\polished_dataset`;
- comparison mode: `wave52r_full_candidate_forward_curve_first`;
- candidate count: `98`;
- held-out curve count before candidate filtering: `97`;
- percentage-error denominator: `peak_to_peak_truth`;
- `Fw` candidates are evaluated only on forward curves;
- `Bw` candidates are evaluated only on backward curves;

## Candidate Inventory

| Candidate | Source | Family | Surface | Valid Directions |
| --- | --- | --- | --- | --- |
| `stage4_c01_r1_compact` | `wave52r_stage4_screening_campaign` | `stage4_c01_r1_compact` | `Fw` | `forward` |
| `stage4_c02_r1_deep` | `wave52r_stage4_screening_campaign` | `stage4_c02_r1_deep` | `Fw` | `forward` |
| `stage4_c03_r1_compact` | `wave52r_stage4_screening_campaign` | `stage4_c03_r1_compact` | `Fw` | `forward` |
| `stage4_c04_r1_deep` | `wave52r_stage4_screening_campaign` | `stage4_c04_r1_deep` | `Fw` | `forward` |
| `stage4_c05_r1_compact` | `wave52r_stage4_screening_campaign` | `stage4_c05_r1_compact` | `Fw` | `forward` |
| `stage4_c06_r1_deep` | `wave52r_stage4_screening_campaign` | `stage4_c06_r1_deep` | `Fw` | `forward` |
| `stage4_h01_r2_compact` | `wave52r_stage4_screening_campaign` | `stage4_h01_r2_compact` | `Fw` | `forward` |
| `stage4_h02_r2_deep` | `wave52r_stage4_screening_campaign` | `stage4_h02_r2_deep` | `Fw` | `forward` |
| `stage4_h03_r3_compact` | `wave52r_stage4_screening_campaign` | `stage4_h03_r3_compact` | `Fw` | `forward` |
| `stage4_h04_r3_deep` | `wave52r_stage4_screening_campaign` | `stage4_h04_r3_deep` | `Fw` | `forward` |
| `stage4_h05_r4_compact` | `wave52r_stage4_screening_campaign` | `stage4_h05_r4_compact` | `Fw` | `forward` |
| `stage4_h06_r4_deep` | `wave52r_stage4_screening_campaign` | `stage4_h06_r4_deep` | `Fw` | `forward` |
| `stage4_h07_r5_compact` | `wave52r_stage4_screening_campaign` | `stage4_h07_r5_compact` | `Fw` | `forward` |
| `stage4_h08_r5_deep` | `wave52r_stage4_screening_campaign` | `stage4_h08_r5_deep` | `Fw` | `forward` |
| `stage4_a01_r2_compact` | `wave52r_stage4_screening_campaign` | `stage4_a01_r2_compact` | `Fw` | `forward` |
| `stage4_a02_r2_compact` | `wave52r_stage4_screening_campaign` | `stage4_a02_r2_compact` | `Fw` | `forward` |
| `stage4_a03_r5_compact` | `wave52r_stage4_screening_campaign` | `stage4_a03_r5_compact` | `Fw` | `forward` |
| `stage4_a04_r5_compact` | `wave52r_stage4_screening_campaign` | `stage4_a04_r5_compact` | `Fw` | `forward` |
| `wave52r_stage5_h08_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_banded_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_h06_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_banded_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_h04_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_bounded_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_h02_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_anchored_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_h03_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_bounded_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_h01_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_anchored_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_h07_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_banded_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_h05_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_banded_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_a01_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_banded_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_a02_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_banded_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_c07_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_direct_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_c08_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_direct_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_c03_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_direct_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_c06_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_direct_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_c05_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_direct_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_c04_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_direct_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_c01_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_direct_curve` | `Fw` | `forward` |
| `wave52r_stage5_c02_seed_314159` | `wave52r_stage5_non_temporal` | `wave52r_stage5_direct_curve` | `Fw` | `forward` |
| `wave52r_stage5_c04_seed_271828` | `wave52r_stage5_non_temporal` | `wave52r_stage5_direct_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_h04_seed_271828` | `wave52r_stage5_non_temporal` | `wave52r_stage5_bounded_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_c04_seed_161803` | `wave52r_stage5_non_temporal` | `wave52r_stage5_direct_coefficient` | `Fw` | `forward` |
| `wave52r_stage5_h04_seed_161803` | `wave52r_stage5_non_temporal` | `wave52r_stage5_bounded_coefficient` | `Fw` | `forward` |
| `wave52r_stage6_fi01` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_cu01` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_ds01` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_c02` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_d01` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_c01` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_w01` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_ds02` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_s02` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_si00` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_ff01` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_si01` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_ff00` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_c03` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage6_c04` | `wave52r_stage6_non_temporal` | `wave52r_stage6_diagnostic` | `Fw` | `forward` |
| `wave52r_stage7_c01` | `wave52r_stage7_non_temporal` | `wave52r_stage7_diagnostic` | `Fw` | `forward` |
| `wave52r_stage7_i01` | `wave52r_stage7_non_temporal` | `wave52r_stage7_diagnostic` | `Fw` | `forward` |
| `wave52r_stage7_a02` | `wave52r_stage7_non_temporal` | `wave52r_stage7_diagnostic` | `Fw` | `forward` |
| `wave52r_stage7_g01` | `wave52r_stage7_non_temporal` | `wave52r_stage7_diagnostic` | `Fw` | `forward` |
| `wave52r_stage7_s01` | `wave52r_stage7_non_temporal` | `wave52r_stage7_diagnostic` | `Fw` | `forward` |
| `wave52r_stage7_p01` | `wave52r_stage7_non_temporal` | `wave52r_stage7_diagnostic` | `Fw` | `forward` |
| `wave52r_stage7_a01` | `wave52r_stage7_non_temporal` | `wave52r_stage7_diagnostic` | `Fw` | `forward` |
| `wave52r_stage8_c00` | `wave52r_stage8_non_temporal` | `wave52r_stage8_data_only` | `Fw` | `forward` |
| `wave52r_stage8_n01` | `wave52r_stage8_non_temporal` | `wave52r_stage8_shuffled_interval` | `Fw` | `forward` |
| `wave52r_stage8_s01` | `wave52r_stage8_non_temporal` | `wave52r_stage8_sign_only` | `Fw` | `forward` |
| `wave52r_stage8_a01` | `wave52r_stage8_non_temporal` | `wave52r_stage8_delayed_interval` | `Fw` | `forward` |
| `wave52r_stage8_w01` | `wave52r_stage8_non_temporal` | `wave52r_stage8_confidence_interval` | `Fw` | `forward` |
| `wave52r_stage8_b01` | `wave52r_stage8_non_temporal` | `wave52r_stage8_broad_interval` | `Fw` | `forward` |
| `wave52r_stage8_r01` | `wave52r_stage8_non_temporal` | `wave52r_stage8_adaptive_interval` | `Fw` | `forward` |
| `wave52r_stage8_t01` | `wave52r_stage8_non_temporal` | `wave52r_stage8_temperature_interval` | `Fw` | `forward` |
| `wave52r_stage8_h01` | `wave52r_stage8_non_temporal` | `wave52r_stage8_hard_equation` | `Fw` | `forward` |
| `wave52r_stage9_k01` | `wave52r_stage9_temporal` | `wave52r_stage9_h04_coefficient_residual_gru` | `Fw` | `forward` |
| `wave52r_stage9_l01` | `wave52r_stage9_temporal` | `wave52r_stage9_h04_context_curriculum_residual_gru` | `Fw` | `forward` |
| `wave52r_stage9_h01` | `wave52r_stage9_temporal` | `wave52r_stage9_h04_causal_residual_gru` | `Fw` | `forward` |
| `wave52r_stage9_p01` | `wave52r_stage9_temporal` | `wave52r_stage9_pf_a_causal_residual_gru` | `Fw` | `forward` |
| `wave52r_stage9_n01` | `wave52r_stage9_temporal` | `wave52r_stage9_h04_shuffled_angular_order_residual_gru` | `Fw` | `forward` |
| `wave52r_stage9_m01` | `wave52r_stage9_temporal` | `wave52r_stage9_h04_static_mean_temporal_shape_gru` | `Fw` | `forward` |
| `wave52r_stage9_c00` | `wave52r_stage9_temporal` | `wave52r_stage9_causal_periodic_gru` | `Fw` | `forward` |
| `wave52r_stage9_r00` | `wave52r_stage9_temporal` | `wave52r_stage9_parameter_matched_zero_anchor_residual_gru` | `Fw` | `forward` |
| `wave52r_stage10_r00` | `wave52r_stage10_non_temporal` | `wave52r_stage10_dense_ridge_extended_library` | `Fw` | `forward` |
| `wave52r_stage10_s01` | `wave52r_stage10_non_temporal` | `wave52r_stage10_sequential_thresholded_ridge` | `Fw` | `forward` |
| `wave52r_stage10_s03` | `wave52r_stage10_non_temporal` | `wave52r_stage10_hierarchy_constrained_stable_sparse_refit` | `Fw` | `forward` |
| `wave52r_stage10_s02` | `wave52r_stage10_non_temporal` | `wave52r_stage10_bootstrap_stable_sparse_refit` | `Fw` | `forward` |
| `wave52r_stage10_y01` | `wave52r_stage10_non_temporal` | `wave52r_stage10_bounded_separable_symbolic_library` | `Fw` | `forward` |
| `wave52r_stage10_q00` | `wave52r_stage10_non_temporal` | `wave52r_stage10_complete_quadratic_coefficient_residual` | `Fw` | `forward` |
| `wave52r_stage10_n01` | `wave52r_stage10_non_temporal` | `wave52r_stage10_shuffled_label_stability_control` | `Fw` | `forward` |
| `wave52r_stage12_f01` | `wave52r_stage12_temporal` | `wave52r_stage12_failure_informed_resampling` | `Fw` | `forward` |
| `wave52r_stage12_s01` | `wave52r_stage12_temporal` | `wave52r_stage12_self_adaptive_curve_weighting` | `Fw` | `forward` |
| `wave52r_stage12_c01` | `wave52r_stage12_temporal` | `wave52r_stage12_standard_adamw` | `Fw` | `forward` |
| `wave52r_stage12_a01` | `wave52r_stage12_temporal` | `wave52r_stage12_augmented_lagrangian` | `Fw` | `forward` |
| `wave52r_stage12_l01` | `wave52r_stage12_temporal` | `wave52r_stage12_adamw_lbfgs_refinement` | `Fw` | `forward` |
| `wave52r_stage12_r01` | `wave52r_stage12_temporal` | `wave52r_stage12_relobralo_style` | `Fw` | `forward` |
| `wave52r_stage12_g01` | `wave52r_stage12_temporal` | `wave52r_stage12_gradient_statistics` | `Fw` | `forward` |
| `wave52r_stage12_u01` | `wave52r_stage12_temporal` | `wave52r_stage12_curriculum_regularization` | `Fw` | `forward` |
| `wave52r_stage12_p01` | `wave52r_stage12_temporal` | `wave52r_stage12_main_loss_preserving_projection` | `Fw` | `forward` |
| `wave52r_stage15_pf_a_setpoint_quadratic_Fw` | `frozen_analytical_anchor` | `polynomial_fourier_pf_a` | `Fw` | `forward` |
| `accepted_periodic_mlp_harmonic_Fw` | `accepted_non_windowed_reference` | `periodic_mlp_harmonic` | `Fw` | `forward` |
| `accepted_periodic_gru_sequence_Fw` | `accepted_time_windowed_incumbent` | `periodic_gru_sequence` | `Fw` | `forward` |

## Forward Comparison

## Backward Comparison

## Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-07-30-10-45-46__wave52r_full_candidate_parallel_temporal_non_temporal_wave52r_full_candidate_parallel_temporal_non_temporal/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-07-30-10-45-46__wave52r_full_candidate_parallel_temporal_non_temporal_wave52r_full_candidate_parallel_temporal_non_temporal\per_condition_metrics.csv`;
- grouped report plot root: `None`;
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
