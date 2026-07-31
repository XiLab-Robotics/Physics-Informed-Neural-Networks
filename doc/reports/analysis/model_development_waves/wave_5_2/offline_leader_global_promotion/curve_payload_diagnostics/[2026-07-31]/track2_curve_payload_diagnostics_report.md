# CVP 1.2 Curve Payload Diagnostics Report

## Overview

This report evaluates a screened `TE Curve Verification Pipeline` candidate set with full truth/prediction curve payloads. It does not train models, alter the dataset structure, or provide future curve samples to runtime model inputs.

- Run Instance: `2026-07-31-13-29-13__track2c_curve_payload_diagnostics`
- Config Path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\wave52r_offline_leader_cross_surface_promotion_matrix.yaml`
- Output Directory: `output\analysis\wave_5_2r\offline_leader_cross_surface_track2\curve_payload_diagnostics\2026-07-31-13-29-13__track2c_curve_payload_diagnostics`
- Evaluated Curve Payload Count: `3104`
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
| 1 | `wave52r_promotion_k01_fw_seed_271828` | `wave52r_promotion_k01` | Fw | forward | 97 | 2.681389 | 0.000491 | 0.001209 | 5.991485 | 2.770279 | 6.924540 | 0.014806 | 0.000875 | 3.567116 |
| 2 | `wave52r_promotion_k01_global_seed_271828` | `wave52r_promotion_k01` | global | backward, forward | 194 | 2.893177 | 0.000577 | 0.001225 | 4.838683 | 2.829332 | 6.472221 | 0.015095 | 0.000872 | 3.669466 |
| 3 | `wave52r_promotion_k01_bw_seed_271828` | `wave52r_promotion_k01` | Bw | backward | 97 | 3.018482 | 0.000564 | 0.001344 | 3.690767 | 2.523682 | 8.100626 | 0.015630 | 0.000869 | 3.670047 |
| 4 | `wave52r_promotion_k01_fw_seed_314159` | `wave52r_promotion_k01` | Fw | forward | 97 | 2.785613 | 0.000508 | 0.001262 | 5.747123 | 3.840578 | 7.836666 | 0.014891 | 0.000876 | 3.701269 |
| 5 | `wave52r_promotion_k01_global_seed_314159` | `wave52r_promotion_k01` | global | backward, forward | 194 | 3.064424 | 0.000569 | 0.001372 | 4.291357 | 2.622167 | 8.106238 | 0.015419 | 0.000880 | 3.778854 |
| 6 | `wave52r_promotion_k01_bw_seed_161803` | `wave52r_promotion_k01` | Bw | backward | 97 | 3.064198 | 0.000511 | 0.001428 | 4.775704 | 2.678780 | 8.145979 | 0.015802 | 0.000883 | 3.833723 |
| 7 | `wave52r_promotion_k01_bw_seed_314159` | `wave52r_promotion_k01` | Bw | backward | 97 | 3.195788 | 0.000572 | 0.001466 | 3.497964 | 2.738321 | 7.773517 | 0.015858 | 0.000886 | 3.841082 |
| 8 | `wave52r_promotion_k01_global_seed_161803` | `wave52r_promotion_k01` | global | backward, forward | 194 | 3.105528 | 0.000603 | 0.001368 | 5.486312 | 3.020697 | 7.683125 | 0.015413 | 0.000880 | 3.959325 |
| 9 | `wave52r_promotion_k01_fw_seed_161803` | `wave52r_promotion_k01` | Fw | forward | 97 | 3.175951 | 0.000674 | 0.001270 | 6.900554 | 3.083149 | 7.813405 | 0.014905 | 0.000876 | 4.169210 |
| 10 | `wave52r_promotion_h08_fw_seed_161803` | `wave52r_promotion_h08` | Fw | forward | 97 | 3.477261 | 0.000862 | 0.001320 | 5.931030 | 4.713399 | 7.958770 | 0.014914 | 0.000872 | 4.455170 |
| 11 | `wave52r_promotion_h08_global_seed_314159` | `wave52r_promotion_h08` | global | backward, forward | 194 | 3.730638 | 0.000837 | 0.001517 | 5.646331 | 4.005448 | 8.064387 | 0.015556 | 0.000868 | 4.651100 |
| 12 | `wave52r_promotion_h08_bw_seed_161803` | `wave52r_promotion_h08` | Bw | backward | 97 | 3.709500 | 0.000704 | 0.001658 | 5.856456 | 4.259231 | 8.464420 | 0.016123 | 0.000865 | 4.669337 |
| 13 | `wave52r_promotion_h08_global_seed_161803` | `wave52r_promotion_h08` | global | backward, forward | 194 | 3.726649 | 0.000844 | 0.001514 | 5.586455 | 5.277255 | 8.178362 | 0.015557 | 0.000868 | 4.704723 |
| 14 | `wave52r_promotion_h08_fw_seed_314159` | `wave52r_promotion_h08` | Fw | forward | 97 | 3.483289 | 0.000835 | 0.001364 | 10.375270 | 4.087762 | 8.022709 | 0.014955 | 0.000873 | 4.874750 |
| 15 | `accepted_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | Fw | forward | 97 | 3.278427 | 0.000690 | 0.001382 | 12.186769 | 5.083881 | 8.443678 | 0.014968 | 0.000892 | 4.900974 |
| 16 | `wave52r_promotion_h08_bw_seed_314159` | `wave52r_promotion_h08` | Bw | backward | 97 | 3.848769 | 0.000748 | 0.001679 | 6.468947 | 4.945342 | 7.605193 | 0.016143 | 0.000866 | 4.904360 |
| 17 | `accepted_periodic_gru_sequence_Bw` | `periodic_gru_sequence` | Bw | backward | 97 | 3.494409 | 0.000606 | 0.001649 | 11.116268 | 5.991176 | 6.640831 | 0.016085 | 0.001313 | 5.066444 |
| 18 | `wave52r_promotion_h08_fw_seed_271828` | `wave52r_promotion_h08` | Fw | forward | 97 | 3.480340 | 0.000825 | 0.001366 | 11.316240 | 9.245234 | 8.498375 | 0.014951 | 0.000869 | 5.223736 |
| 19 | `accepted_periodic_mlp_harmonic_global` | `periodic_mlp_harmonic` | global | backward, forward | 194 | 3.384645 | 0.000686 | 0.001476 | 13.577255 | 6.719809 | 9.352661 | 0.015521 | 0.000869 | 5.233566 |
| 20 | `accepted_periodic_mlp_harmonic_Bw` | `periodic_mlp_harmonic` | Bw | backward | 97 | 3.581163 | 0.000612 | 0.001677 | 12.263749 | 6.514344 | 11.625378 | 0.016237 | 0.000861 | 5.295624 |
| 21 | `accepted_periodic_gru_sequence_global` | `periodic_gru_sequence` | global | backward, forward | 194 | 3.567012 | 0.000759 | 0.001517 | 13.121518 | 6.872783 | 8.623264 | 0.015537 | 0.001018 | 5.378178 |
| 22 | `wave52r_promotion_h08_bw_seed_271828` | `wave52r_promotion_h08` | Bw | backward | 97 | 3.877630 | 0.000761 | 0.001706 | 10.625918 | 6.990961 | 8.009367 | 0.016151 | 0.000866 | 5.451282 |
| 23 | `wave52r_promotion_h08_global_seed_271828` | `wave52r_promotion_h08` | global | backward, forward | 194 | 3.721975 | 0.000823 | 0.001527 | 12.604938 | 6.560702 | 7.713137 | 0.015557 | 0.000868 | 5.466078 |
| 24 | `accepted_periodic_mlp_harmonic_Fw` | `periodic_mlp_harmonic` | Fw | forward | 97 | 3.438600 | 0.000825 | 0.001390 | 14.751961 | 10.572248 | 11.801784 | 0.014963 | 0.000881 | 5.592041 |

## Interpretation

The strongest screened diagnostic score is `wave52r_promotion_k01_fw_seed_271828`. The score is an analysis aid, not a registry-promotion rule.

Paper-reference and tree-bank candidates may remain strong on curve shape metrics while still being less attractive for deployment. Repository-owned neural candidates should therefore be judged by both diagnostic behavior and future export/runtime feasibility.

## Decision

The next work should not start from `tree` only because of scalar strength. The practical direction is a set of parallel curve-aware retraining or reranking branches: keep searching the `Fw` surface for a deployable repository-owned candidate, prioritize periodic temporal candidates on the `Bw` surface, and carry the best neural `global` candidate as a dedicated cross-direction surface. Harmonic/phase-aware validation stays separate from runtime inputs.

## Runtime Input Boundary

All diagnostics are computed after prediction. Candidate models still consume only current point-level operating state, supported short causal history, or derived causal features. Full curves remain a validation and promotion surface only.

## Machine-Readable Artifacts

- `output\analysis\wave_5_2r\offline_leader_cross_surface_track2\curve_payload_diagnostics\2026-07-31-13-29-13__track2c_curve_payload_diagnostics\candidate_payload_diagnostics.csv`
- `output\analysis\wave_5_2r\offline_leader_cross_surface_track2\curve_payload_diagnostics\2026-07-31-13-29-13__track2c_curve_payload_diagnostics\curve_payload_diagnostics.csv`
- `output\analysis\wave_5_2r\offline_leader_cross_surface_track2\curve_payload_diagnostics\2026-07-31-13-29-13__track2c_curve_payload_diagnostics\harmonic_payload_diagnostics.csv`
- `output\analysis\wave_5_2r\offline_leader_cross_surface_track2\curve_payload_diagnostics\2026-07-31-13-29-13__track2c_curve_payload_diagnostics\curve_payload_samples.jsonl`
- `output\analysis\wave_5_2r\offline_leader_cross_surface_track2\curve_payload_diagnostics\2026-07-31-13-29-13__track2c_curve_payload_diagnostics\track2_curve_payload_diagnostics_summary.yaml`
