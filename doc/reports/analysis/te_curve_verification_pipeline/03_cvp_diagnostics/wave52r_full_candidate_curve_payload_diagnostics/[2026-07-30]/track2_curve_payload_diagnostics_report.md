# CVP 1.2 Curve Payload Diagnostics Report

## Overview

This report evaluates a screened `TE Curve Verification Pipeline` candidate set with full truth/prediction curve payloads. It does not train models, alter the dataset structure, or provide future curve samples to runtime model inputs.

- Run Instance: `2026-07-30-11-00-18__track2c_curve_payload_diagnostics`
- Config Path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\wave52r_full_candidate_parallel_temporal_non_temporal_matrix.yaml`
- Output Directory: `output\validation_checks\wave52r_full_candidate_track2_curve_payload_diagnostics\2026-07-30-11-00-18__track2c_curve_payload_diagnostics`
- Evaluated Curve Payload Count: `970`
- Harmonic Orders: `1, 2, 3, 4, 5, 6, 8, 10, 12, 19`
- Stored payload samples are downsampled for repository-size control.

## Method

Diagnostics are computed on full held-out `TE` curves after each candidate produces pointwise predictions through its normal causal input path. The report separates the validation surface from the runtime input contract.

Computed diagnostics:

- peak-to-peak amplitude error and residual peak-to-peak ratio;
- signed and absolute curve-mean error plus mean-centered shape MAE;
- selected-harmonic amplitude and wrapped phase error;
- local derivative `RMSE`;
- residual second-derivative smoothness;
- residual lag-one autocorrelation;
- per-revolution closure mismatch and deterministic stitched-boundary surrogate.

## Candidate Diagnostic Ranking

| Rank | Candidate | Family | Surface | Directions | Curves | Mean MPE [%] | Mean Abs Offset Error [deg] | Centered Shape MAE [deg] | Mean Harmonic Amp Error [%] | Mean Harmonic Phase Error [deg] | Mean P2P Error [%] | Derivative RMSE | Closure Mismatch [deg] | Diagnostic Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `wave52r_stage9_k01` | `wave52r_stage9_h04_coefficient_residual_gru` | Fw | forward | 97 | 2.716282 | 0.000496 | 0.001230 | 5.965385 | 3.431078 | 7.228580 | 0.014831 | 0.000876 | 3.632689 |
| 2 | `wave52r_stage12_f01` | `wave52r_stage12_failure_informed_resampling` | Fw | forward | 97 | 2.992959 | 0.000740 | 0.001147 | 5.998512 | 3.330207 | 6.445238 | 0.014619 | 0.000873 | 3.905511 |
| 3 | `wave52r_stage12_s01` | `wave52r_stage12_self_adaptive_curve_weighting` | Fw | forward | 97 | 3.040627 | 0.000677 | 0.001216 | 5.702734 | 3.166801 | 7.719964 | 0.014785 | 0.000875 | 3.917092 |
| 4 | `wave52r_stage5_h08_seed_314159` | `wave52r_stage5_banded_coefficient` | Fw | forward | 97 | 3.483289 | 0.000835 | 0.001364 | 10.375270 | 4.087762 | 8.022709 | 0.014955 | 0.000873 | 4.874750 |
| 5 | `accepted_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | Fw | forward | 97 | 3.278427 | 0.000690 | 0.001382 | 12.186769 | 5.083881 | 8.443678 | 0.014968 | 0.000892 | 4.900974 |
| 6 | `accepted_periodic_mlp_harmonic_Fw` | `periodic_mlp_harmonic` | Fw | forward | 97 | 3.438600 | 0.000825 | 0.001390 | 14.751961 | 10.572248 | 11.801784 | 0.014963 | 0.000881 | 5.592041 |
| 7 | `wave52r_stage10_s01` | `wave52r_stage10_sequential_thresholded_ridge` | Fw | forward | 97 | 3.422431 | 0.000767 | 0.001406 | 34.371677 | 31.881368 | 9.386195 | 0.014884 | 0.000869 | 8.602503 |
| 8 | `wave52r_stage10_r00` | `wave52r_stage10_dense_ridge_extended_library` | Fw | forward | 97 | 3.422123 | 0.000757 | 0.001408 | 34.381092 | 32.075880 | 9.383452 | 0.014888 | 0.000869 | 8.612908 |
| 9 | `wave52r_stage15_pf_a_setpoint_quadratic_Fw` | `polynomial_fourier_pf_a` | Fw | forward | 97 | 3.748632 | 0.000975 | 0.001385 | 35.164774 | 31.881827 | 10.567277 | 0.014969 | 0.000869 | 9.008888 |
| 10 | `wave52r_stage5_h04_seed_314159` | `wave52r_stage5_bounded_coefficient` | Fw | forward | 97 | 3.557641 | 0.000884 | 0.001357 | 35.078488 | 36.229104 | 10.685185 | 0.014940 | 0.000869 | 9.026341 |

## Interpretation

The strongest screened diagnostic score is `wave52r_stage9_k01`. The score is an analysis aid, not a registry-promotion rule.

Paper-reference and tree-bank candidates may remain strong on curve shape metrics while still being less attractive for deployment. Repository-owned neural candidates should therefore be judged by both diagnostic behavior and future export/runtime feasibility.

## Decision

The next work should not start from `tree` only because of scalar strength. The practical direction is a set of parallel curve-aware retraining or reranking branches: keep searching the `Fw` surface for a deployable repository-owned candidate, prioritize periodic temporal candidates on the `Bw` surface, and carry the best neural `global` candidate as a dedicated cross-direction surface. Harmonic/phase-aware validation stays separate from runtime inputs.

## Runtime Input Boundary

All diagnostics are computed after prediction. Candidate models still consume only current point-level operating state, supported short causal history, or derived causal features. Full curves remain a validation and promotion surface only.

## Machine-Readable Artifacts

- `output\validation_checks\wave52r_full_candidate_track2_curve_payload_diagnostics\2026-07-30-11-00-18__track2c_curve_payload_diagnostics\candidate_payload_diagnostics.csv`
- `output\validation_checks\wave52r_full_candidate_track2_curve_payload_diagnostics\2026-07-30-11-00-18__track2c_curve_payload_diagnostics\curve_payload_diagnostics.csv`
- `output\validation_checks\wave52r_full_candidate_track2_curve_payload_diagnostics\2026-07-30-11-00-18__track2c_curve_payload_diagnostics\harmonic_payload_diagnostics.csv`
- `output\validation_checks\wave52r_full_candidate_track2_curve_payload_diagnostics\2026-07-30-11-00-18__track2c_curve_payload_diagnostics\curve_payload_samples.jsonl`
- `output\validation_checks\wave52r_full_candidate_track2_curve_payload_diagnostics\2026-07-30-11-00-18__track2c_curve_payload_diagnostics\track2_curve_payload_diagnostics_summary.yaml`
