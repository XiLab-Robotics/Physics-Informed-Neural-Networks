# CVP 1.1 Curve-First Reranking Report

## Overview

This report reranks the already accepted `TE Curve Verification Pipeline` candidate matrix by full-curve validation behavior. It does not execute training, does not alter the dataset structure, and does not provide future curve samples to any model.

- Run Instance: `2026-05-28-19-27-46__track2b_curve_first_reranking`
- Source TE Curve Verification Pipeline Run: `output\validation_checks\track2_reference_comparison\2026-05-28-12-22-56__track2_full_directional_family_matrix_wave2c_residual_harmonic_temporal_hybrid_track2_refresh_2026_05_28`
- Source Curve Count: `194`
- Source Candidate Count: `111`
- Generated Artifact Directory: `output\validation_checks\track2_curve_first_reranking\2026-05-28-19-27-46__track2b_curve_first_reranking`

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
| 1 | `rcim_retuned_GBM19_Fw` | `GBM` | rcim_retuned | Fw | all_valid | 97 | 2.371752 | 4.911649 | 5.680916 | 0.001089 |
| 2 | `rcim_original_ERT19_Fw` | `ERT` | rcim_original | Fw | all_valid | 97 | 3.252972 | 6.145160 | 7.841177 | 0.001471 |
| 3 | `rcim_retuned_RF19_Fw` | `RF` | rcim_retuned | Fw | all_valid | 97 | 3.291549 | 5.997536 | 7.048587 | 0.001487 |
| 4 | `rcim_original_RF19_Fw` | `RF` | rcim_original | Fw | all_valid | 97 | 3.939860 | 6.872174 | 9.475785 | 0.001767 |
| 5 | `rcim_original_LGBM19_Fw` | `LGBM` | rcim_original | Fw | all_valid | 97 | 4.016685 | 10.054446 | 11.877265 | 0.001801 |
| 6 | `rcim_retuned_ERT19_Fw` | `ERT` | rcim_retuned | Fw | all_valid | 97 | 4.038649 | 7.599022 | 9.427596 | 0.001807 |
| 7 | `paper_retuned_best_Fw` | `best_composite` | rcim_retuned | Fw | all_valid | 97 | 4.108527 | 9.865680 | 11.737393 | 0.001839 |
| 8 | `rcim_retuned_HGBM19_Fw` | `HGBM` | rcim_retuned | Fw | all_valid | 97 | 4.126307 | 9.401102 | 13.400433 | 0.001851 |
| 9 | `rcim_retuned_LGBM19_Fw` | `LGBM` | rcim_retuned | Fw | all_valid | 97 | 4.135160 | 9.865585 | 11.737457 | 0.001851 |
| 10 | `rcim_retuned_DT19_Fw` | `DT` | rcim_retuned | Fw | all_valid | 97 | 4.305731 | 9.062969 | 12.531740 | 0.001919 |
| 11 | `rcim_original_DT19_Fw` | `DT` | rcim_original | Fw | all_valid | 97 | 4.305735 | 9.062969 | 12.531740 | 0.001919 |
| 12 | `rcim_original_GBM19_Fw` | `GBM` | rcim_original | Fw | all_valid | 97 | 4.312144 | 8.193384 | 10.648506 | 0.001921 |
| 13 | `rcim_retuned_ET19_Fw` | `ET` | rcim_retuned | Fw | all_valid | 97 | 4.425530 | 9.533169 | 12.508938 | 0.002001 |
| 14 | `rcim_original_HGBM19_Fw` | `HGBM` | rcim_original | Fw | all_valid | 97 | 4.493305 | 10.616761 | 14.461187 | 0.002011 |
| 15 | `rcim_retuned_XGBM19_Fw` | `XGBM` | rcim_retuned | Fw | all_valid | 97 | 4.587646 | 10.487803 | 12.008064 | 0.002054 |

## Forward Curve-First Leaders

| Rank | Candidate | Family | Source | Surface | Direction | Curves | Mean MPE [%] | P95 MPE [%] | Worst MPE [%] | Mean Curve MAE [deg] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `rcim_retuned_GBM19_Fw` | `GBM` | rcim_retuned | Fw | forward | 97 | 2.371752 | 4.911649 | 5.680916 | 0.001089 |
| 2 | `rcim_original_ERT19_Fw` | `ERT` | rcim_original | Fw | forward | 97 | 3.252972 | 6.145160 | 7.841177 | 0.001471 |
| 3 | `rcim_retuned_RF19_Fw` | `RF` | rcim_retuned | Fw | forward | 97 | 3.291549 | 5.997536 | 7.048587 | 0.001487 |
| 4 | `rcim_original_RF19_Fw` | `RF` | rcim_original | Fw | forward | 97 | 3.939860 | 6.872174 | 9.475785 | 0.001767 |
| 5 | `rcim_original_LGBM19_Fw` | `LGBM` | rcim_original | Fw | forward | 97 | 4.016685 | 10.054446 | 11.877265 | 0.001801 |
| 6 | `rcim_retuned_ERT19_Fw` | `ERT` | rcim_retuned | Fw | forward | 97 | 4.038649 | 7.599022 | 9.427596 | 0.001807 |
| 7 | `paper_retuned_best_Fw` | `best_composite` | rcim_retuned | Fw | forward | 97 | 4.108527 | 9.865680 | 11.737393 | 0.001839 |
| 8 | `rcim_retuned_HGBM19_Fw` | `HGBM` | rcim_retuned | Fw | forward | 97 | 4.126307 | 9.401102 | 13.400433 | 0.001851 |
| 9 | `rcim_retuned_LGBM19_Fw` | `LGBM` | rcim_retuned | Fw | forward | 97 | 4.135160 | 9.865585 | 11.737457 | 0.001851 |
| 10 | `rcim_retuned_DT19_Fw` | `DT` | rcim_retuned | Fw | forward | 97 | 4.305731 | 9.062969 | 12.531740 | 0.001919 |
| 11 | `rcim_original_DT19_Fw` | `DT` | rcim_original | Fw | forward | 97 | 4.305735 | 9.062969 | 12.531740 | 0.001919 |
| 12 | `rcim_original_GBM19_Fw` | `GBM` | rcim_original | Fw | forward | 97 | 4.312144 | 8.193384 | 10.648506 | 0.001921 |

## Backward Curve-First Leaders

| Rank | Candidate | Family | Source | Surface | Direction | Curves | Mean MPE [%] | P95 MPE [%] | Worst MPE [%] | Mean Curve MAE [deg] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `rcim_retuned_GBM19_Bw` | `GBM` | rcim_retuned | Bw | backward | 97 | 5.398275 | 12.280348 | 29.298779 | 0.002766 |
| 2 | `periodic_gru_sequence_Bw` | `periodic_gru_sequence` | wave2_temporal_entry_registry | Bw | backward | 97 | 5.465946 | 14.820350 | 18.759599 | 0.002392 |
| 3 | `periodic_gru_sequence_global` | `periodic_gru_sequence` | wave2_temporal_entry_registry | global | backward | 97 | 6.010388 | 12.692963 | 17.220297 | 0.002630 |
| 4 | `periodic_lstm_sequence_Bw` | `periodic_lstm_sequence` | wave2_temporal_entry_registry | Bw | backward | 97 | 6.013045 | 15.382036 | 17.697190 | 0.002625 |
| 5 | `periodic_lstm_sequence_global` | `periodic_lstm_sequence` | wave2_temporal_entry_registry | global | backward | 97 | 6.097733 | 14.674261 | 17.806152 | 0.002689 |
| 6 | `rcim_retuned_ET19_Bw` | `ET` | rcim_retuned | Bw | backward | 97 | 7.021055 | 15.287358 | 28.924505 | 0.003441 |
| 7 | `tree_Bw` | `tree` | wave1 | Bw | backward | 97 | 7.051484 | 14.115584 | 15.808625 | 0.003258 |
| 8 | `tree_global` | `tree` | wave1 | global | backward | 97 | 7.118450 | 13.703254 | 15.694393 | 0.003290 |
| 9 | `rcim_retuned_ERT19_Bw` | `ERT` | rcim_retuned | Bw | backward | 97 | 7.269106 | 13.186813 | 29.804962 | 0.003551 |
| 10 | `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `residual_harmonic_lstm_sequence_sparse_rcim` | wave2c_residual_harmonic_temporal_registry | Bw | backward | 97 | 7.510266 | 13.159550 | 15.012015 | 0.003440 |
| 11 | `rcim_retuned_RF19_Bw` | `RF` | rcim_retuned | Bw | backward | 97 | 7.542522 | 15.083100 | 28.325982 | 0.003649 |
| 12 | `paper_retuned_best_Bw` | `best_composite` | rcim_retuned | Bw | backward | 97 | 7.571630 | 15.644903 | 29.854827 | 0.003675 |

## Surface Leaders

| Surface | Leader | Family | Source | Curves | Mean MPE [%] | P95 MPE [%] | Mean Curve MAE [deg] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bw | `rcim_retuned_GBM19_Bw` | `GBM` | rcim_retuned | 97 | 5.398275 | 12.280348 | 0.002766 |
| Fw | `rcim_retuned_GBM19_Fw` | `GBM` | rcim_retuned | 97 | 2.371752 | 4.911649 | 0.001089 |
| global | `periodic_lstm_sequence_global` | `periodic_lstm_sequence` | wave2_temporal_entry_registry | 194 | 6.119950 | 14.716986 | 0.002707 |

## Scalar Registry Context

- Current scalar registry winner: `te_periodic_gru_sequence_remote_Bw` from family `periodic_gru_sequence_bw`.
- Scalar test `MAE`: `0.002344` and scalar test `RMSE`: `0.002747`.

The strongest forward curve-first candidate in this reranking is `rcim_retuned_GBM19_Fw` from family `GBM` with mean `MPE` `2.371752` percent and P95 `MPE` `4.911649` percent. This does not replace the backward or global branches.

## Decision

This pass standardizes the curve-first evidence surface and should be read as three parallel selection tracks: `Fw`, `Bw`, and `global`. It does not promote one single program-best model by itself because the real application needs one best candidate per surface and richer harmonic/phase diagnostics still require curve-payload export.

Machine-readable artifacts:

- `output\validation_checks\track2_curve_first_reranking\2026-05-28-19-27-46__track2b_curve_first_reranking\candidate_curve_first_ranking.csv`
- `output\validation_checks\track2_curve_first_reranking\2026-05-28-19-27-46__track2b_curve_first_reranking\direction_curve_first_ranking.csv`
- `output\validation_checks\track2_curve_first_reranking\2026-05-28-19-27-46__track2b_curve_first_reranking\track2_curve_first_reranking_summary.yaml`
