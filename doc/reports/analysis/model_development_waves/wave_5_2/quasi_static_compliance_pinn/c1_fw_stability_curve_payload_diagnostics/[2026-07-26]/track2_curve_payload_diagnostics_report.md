# CVP 1.2 Curve Payload Diagnostics Report

## Overview

This report evaluates a screened `TE Curve Verification Pipeline` candidate set with full truth/prediction curve payloads. It does not train models, alter the dataset structure, or provide future curve samples to runtime model inputs.

- Run Instance: `2026-07-26-20-10-35__track2c_curve_payload_diagnostics`
- Config Path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\phase3_c1_fw_stability_common_test_matrix.yaml`
- Output Directory: `output\validation_checks\phase3_c1_fw_stability_curve_payload_diagnostics\2026-07-26-20-10-35__track2c_curve_payload_diagnostics`
- Evaluated Curve Payload Count: `582`
- Harmonic Orders: `1, 3, 39, 40, 78, 81, 156, 162, 240`
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
| 1 | `accepted_periodic_mlp_harmonic_Fw` | `periodic_mlp_harmonic` | Fw | forward | 97 | 3.438600 | 0.000825 | 0.001390 | 15.380051 | 13.591649 | 11.801784 | 0.014963 | 0.000881 | 5.805821 |
| 2 | `accepted_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | Fw | forward | 97 | 3.278412 | 0.000690 | 0.001382 | 19.237460 | 12.166874 | 8.444949 | 0.014968 | 0.000892 | 5.960178 |
| 3 | `phase3_c1_linear_compliance_soft_Fw` | `phase3_pinn_c1_linear_compliance_soft_fw` | Fw | forward | 97 | 3.824504 | 0.000932 | 0.001481 | 34.128423 | 21.434153 | 10.008700 | 0.014993 | 0.000873 | 8.458984 |
| 4 | `phase3_c1_fw_seed_314159` | `phase3_pinn_c1_linear_compliance_soft_fw_seed_314159` | Fw | forward | 97 | 3.757582 | 0.000872 | 0.001513 | 41.194147 | 20.029616 | 6.383986 | 0.015005 | 0.000872 | 9.028526 |
| 5 | `phase3_c0_learned_mean_control_Fw` | `phase3_pinn_c0_learned_mean_control_fw` | Fw | forward | 97 | 4.076406 | 0.000989 | 0.001608 | 40.929562 | 22.372886 | 6.462809 | 0.015082 | 0.000871 | 9.438823 |
| 6 | `phase3_c1_fw_seed_271828` | `phase3_pinn_c1_linear_compliance_soft_fw_seed_271828` | Fw | forward | 97 | 4.654849 | 0.001350 | 0.001605 | 45.692679 | 22.965806 | 6.827516 | 0.015071 | 0.000873 | 10.523113 |

## Interpretation

The strongest screened diagnostic score is `accepted_periodic_mlp_harmonic_Fw`. The score is an analysis aid, not a registry-promotion rule.

Paper-reference and tree-bank candidates may remain strong on curve shape metrics while still being less attractive for deployment. Repository-owned neural candidates should therefore be judged by both diagnostic behavior and future export/runtime feasibility.

## Decision

The next work should not start from `tree` only because of scalar strength. The practical direction is a set of parallel curve-aware retraining or reranking branches: keep searching the `Fw` surface for a deployable repository-owned candidate, prioritize periodic temporal candidates on the `Bw` surface, and carry the best neural `global` candidate as a dedicated cross-direction surface. Harmonic/phase-aware validation stays separate from runtime inputs.

## Runtime Input Boundary

All diagnostics are computed after prediction. Candidate models still consume only current point-level operating state, supported short causal history, or derived causal features. Full curves remain a validation and promotion surface only.

## Machine-Readable Artifacts

- `output\validation_checks\phase3_c1_fw_stability_curve_payload_diagnostics\2026-07-26-20-10-35__track2c_curve_payload_diagnostics\candidate_payload_diagnostics.csv`
- `output\validation_checks\phase3_c1_fw_stability_curve_payload_diagnostics\2026-07-26-20-10-35__track2c_curve_payload_diagnostics\curve_payload_diagnostics.csv`
- `output\validation_checks\phase3_c1_fw_stability_curve_payload_diagnostics\2026-07-26-20-10-35__track2c_curve_payload_diagnostics\harmonic_payload_diagnostics.csv`
- `output\validation_checks\phase3_c1_fw_stability_curve_payload_diagnostics\2026-07-26-20-10-35__track2c_curve_payload_diagnostics\curve_payload_samples.jsonl`
- `output\validation_checks\phase3_c1_fw_stability_curve_payload_diagnostics\2026-07-26-20-10-35__track2c_curve_payload_diagnostics\track2_curve_payload_diagnostics_summary.yaml`
