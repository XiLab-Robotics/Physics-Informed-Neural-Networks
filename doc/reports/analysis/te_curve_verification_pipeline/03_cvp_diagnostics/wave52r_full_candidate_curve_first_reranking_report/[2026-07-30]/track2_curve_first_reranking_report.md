# CVP 1.1 Curve-First Reranking Report

## Overview

This report reranks the already accepted `TE Curve Verification Pipeline` candidate matrix by full-curve validation behavior. It does not execute training, does not alter the dataset structure, and does not provide future curve samples to any model.

- Run Instance: `2026-07-30-11-09-17__track2b_curve_first_reranking`
- Source TE Curve Verification Pipeline Run: `output\validation_checks\track2_reference_comparison\2026-07-30-10-45-46__wave52r_full_candidate_parallel_temporal_non_temporal_wave52r_full_candidate_parallel_temporal_non_temporal`
- Source Curve Count: `97`
- Source Candidate Count: `98`
- Generated Artifact Directory: `output\validation_checks\wave52r_full_candidate_track2_curve_first_reranking\2026-07-30-11-09-17__track2b_curve_first_reranking`

## Method

The primary ordering key is mean `TE Curve Verification Pipeline` mean-percentage-error over each candidate's valid direction surface. Ties are resolved by P95 mean-percentage-error, worst mean-percentage-error, and mean curve `MAE`. This keeps scalar pointwise registry metrics separate from curve-following evidence.

Available diagnostics from the existing `TE Curve Verification Pipeline` matrix:

- mean curve `MAE` and `RMSE` per operating condition;
- mean percentage error per operating condition;
- P95, worst-condition, and standard-deviation aggregates across conditions.

Deferred diagnostics requiring a future curve-payload export:

- harmonic amplitude and phase error by order;
- derivative or slope continuity error;
- per-revolution residual drift and continuity checks across stitched curves.

## Causal Input Boundary

The validation surface is full-curve because the compensation target is continuous `TE` over many consecutive motor revolutions. The runtime input contract remains causal: current point-level operating state, optional short history of already observed samples, or derived causal features only.

## Overall Curve-First Leaders

| Rank | Candidate | Family | Source | Surface | Direction | Curves | Mean MPE [%] | P95 MPE [%] | Worst MPE [%] | Mean Curve MAE [deg] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `wave52r_stage9_k01` | `wave52r_stage9_h04_coefficient_residual_gru` | wave52r_stage9_temporal | Fw | all_valid | 97 | 2.716282 | 7.751271 | 12.059574 | 0.001374 |
| 2 | `wave52r_stage12_f01` | `wave52r_stage12_failure_informed_resampling` | wave52r_stage12_temporal | Fw | all_valid | 97 | 2.992959 | 6.554012 | 14.230071 | 0.001444 |
| 3 | `wave52r_stage12_s01` | `wave52r_stage12_self_adaptive_curve_weighting` | wave52r_stage12_temporal | Fw | all_valid | 97 | 3.040627 | 8.194179 | 11.572735 | 0.001495 |
| 4 | `wave52r_stage9_l01` | `wave52r_stage9_h04_context_curriculum_residual_gru` | wave52r_stage9_temporal | Fw | all_valid | 97 | 3.103236 | 9.260897 | 12.740246 | 0.001539 |
| 5 | `wave52r_stage9_h01` | `wave52r_stage9_h04_causal_residual_gru` | wave52r_stage9_temporal | Fw | all_valid | 97 | 3.108158 | 9.304905 | 12.923443 | 0.001542 |
| 6 | `wave52r_stage9_p01` | `wave52r_stage9_pf_a_causal_residual_gru` | wave52r_stage9_temporal | Fw | all_valid | 97 | 3.121500 | 9.446223 | 13.112899 | 0.001550 |
| 7 | `wave52r_stage9_n01` | `wave52r_stage9_h04_shuffled_angular_order_residual_gru` | wave52r_stage9_temporal | Fw | all_valid | 97 | 3.167184 | 9.090898 | 12.641496 | 0.001565 |
| 8 | `wave52r_stage12_a01` | `wave52r_stage12_augmented_lagrangian` | wave52r_stage12_temporal | Fw | all_valid | 97 | 3.203346 | 7.164627 | 12.752699 | 0.001582 |
| 9 | `wave52r_stage12_c01` | `wave52r_stage12_standard_adamw` | wave52r_stage12_temporal | Fw | all_valid | 97 | 3.203346 | 7.164627 | 12.752699 | 0.001582 |
| 10 | `wave52r_stage12_l01` | `wave52r_stage12_adamw_lbfgs_refinement` | wave52r_stage12_temporal | Fw | all_valid | 97 | 3.203346 | 7.164627 | 12.752699 | 0.001582 |
| 11 | `wave52r_stage12_r01` | `wave52r_stage12_relobralo_style` | wave52r_stage12_temporal | Fw | all_valid | 97 | 3.257255 | 9.009867 | 12.533281 | 0.001604 |
| 12 | `accepted_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | accepted_time_windowed_incumbent | Fw | all_valid | 97 | 3.278427 | 7.224709 | 12.528394 | 0.001618 |
| 13 | `wave52r_stage9_m01` | `wave52r_stage9_h04_static_mean_temporal_shape_gru` | wave52r_stage9_temporal | Fw | all_valid | 97 | 3.342412 | 9.050011 | 13.439414 | 0.001650 |
| 14 | `wave52r_stage12_g01` | `wave52r_stage12_gradient_statistics` | wave52r_stage12_temporal | Fw | all_valid | 97 | 3.360955 | 8.400424 | 12.714322 | 0.001640 |
| 15 | `wave52r_stage12_u01` | `wave52r_stage12_curriculum_regularization` | wave52r_stage12_temporal | Fw | all_valid | 97 | 3.414693 | 8.308448 | 12.957999 | 0.001666 |

## Forward Curve-First Leaders

| Rank | Candidate | Family | Source | Surface | Direction | Curves | Mean MPE [%] | P95 MPE [%] | Worst MPE [%] | Mean Curve MAE [deg] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `wave52r_stage9_k01` | `wave52r_stage9_h04_coefficient_residual_gru` | wave52r_stage9_temporal | Fw | forward | 97 | 2.716282 | 7.751271 | 12.059574 | 0.001374 |
| 2 | `wave52r_stage12_f01` | `wave52r_stage12_failure_informed_resampling` | wave52r_stage12_temporal | Fw | forward | 97 | 2.992959 | 6.554012 | 14.230071 | 0.001444 |
| 3 | `wave52r_stage12_s01` | `wave52r_stage12_self_adaptive_curve_weighting` | wave52r_stage12_temporal | Fw | forward | 97 | 3.040627 | 8.194179 | 11.572735 | 0.001495 |
| 4 | `wave52r_stage9_l01` | `wave52r_stage9_h04_context_curriculum_residual_gru` | wave52r_stage9_temporal | Fw | forward | 97 | 3.103236 | 9.260897 | 12.740246 | 0.001539 |
| 5 | `wave52r_stage9_h01` | `wave52r_stage9_h04_causal_residual_gru` | wave52r_stage9_temporal | Fw | forward | 97 | 3.108158 | 9.304905 | 12.923443 | 0.001542 |
| 6 | `wave52r_stage9_p01` | `wave52r_stage9_pf_a_causal_residual_gru` | wave52r_stage9_temporal | Fw | forward | 97 | 3.121500 | 9.446223 | 13.112899 | 0.001550 |
| 7 | `wave52r_stage9_n01` | `wave52r_stage9_h04_shuffled_angular_order_residual_gru` | wave52r_stage9_temporal | Fw | forward | 97 | 3.167184 | 9.090898 | 12.641496 | 0.001565 |
| 8 | `wave52r_stage12_a01` | `wave52r_stage12_augmented_lagrangian` | wave52r_stage12_temporal | Fw | forward | 97 | 3.203346 | 7.164627 | 12.752699 | 0.001582 |
| 9 | `wave52r_stage12_c01` | `wave52r_stage12_standard_adamw` | wave52r_stage12_temporal | Fw | forward | 97 | 3.203346 | 7.164627 | 12.752699 | 0.001582 |
| 10 | `wave52r_stage12_l01` | `wave52r_stage12_adamw_lbfgs_refinement` | wave52r_stage12_temporal | Fw | forward | 97 | 3.203346 | 7.164627 | 12.752699 | 0.001582 |
| 11 | `wave52r_stage12_r01` | `wave52r_stage12_relobralo_style` | wave52r_stage12_temporal | Fw | forward | 97 | 3.257255 | 9.009867 | 12.533281 | 0.001604 |
| 12 | `accepted_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | accepted_time_windowed_incumbent | Fw | forward | 97 | 3.278427 | 7.224709 | 12.528394 | 0.001618 |

## Backward Curve-First Leaders

| Rank | Candidate | Family | Source | Surface | Direction | Curves | Mean MPE [%] | P95 MPE [%] | Worst MPE [%] | Mean Curve MAE [deg] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Surface Leaders

| Surface | Leader | Family | Source | Curves | Mean MPE [%] | P95 MPE [%] | Mean Curve MAE [deg] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fw | `wave52r_stage9_k01` | `wave52r_stage9_h04_coefficient_residual_gru` | wave52r_stage9_temporal | 97 | 2.716282 | 7.751271 | 0.001374 |

## Scalar Registry Context

- Current scalar registry winner: `te_periodic_gru_sequence_bw` from family `periodic_gru_sequence_bw`.
- Scalar test `MAE`: `0.001084` and scalar test `RMSE`: `0.001393`.

The strongest forward curve-first candidate in this reranking is `wave52r_stage9_k01` from family `wave52r_stage9_h04_coefficient_residual_gru` with mean `MPE` `2.716282` percent and P95 `MPE` `7.751271` percent.

## Decision

This pass standardizes the curve-first evidence surface and should be read as three parallel selection tracks: `Fw`, `Bw`, and `global`. It does not promote one single program-best model by itself because the real application needs one best candidate per surface and richer harmonic/phase diagnostics still require curve-payload export.

Machine-readable artifacts:

- `output\validation_checks\wave52r_full_candidate_track2_curve_first_reranking\2026-07-30-11-09-17__track2b_curve_first_reranking\candidate_curve_first_ranking.csv`
- `output\validation_checks\wave52r_full_candidate_track2_curve_first_reranking\2026-07-30-11-09-17__track2b_curve_first_reranking\direction_curve_first_ranking.csv`
- `output\validation_checks\wave52r_full_candidate_track2_curve_first_reranking\2026-07-30-11-09-17__track2b_curve_first_reranking\track2_curve_first_reranking_summary.yaml`
