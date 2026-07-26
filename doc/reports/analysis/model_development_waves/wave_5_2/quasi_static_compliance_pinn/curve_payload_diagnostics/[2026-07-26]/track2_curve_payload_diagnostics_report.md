# CVP 1.2 Curve Payload Diagnostics Report

## Overview

This report evaluates a screened `TE Curve Verification Pipeline` candidate set with full truth/prediction curve payloads. It does not train models, alter the dataset structure, or provide future curve samples to runtime model inputs.

- Run Instance: `2026-07-26-19-39-21__track2c_curve_payload_diagnostics`
- Config Path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\phase3_quasi_static_compliance_pinn_common_test_matrix.yaml`
- Output Directory: `output\validation_checks\phase3_quasi_static_compliance_pinn_curve_payload_diagnostics\2026-07-26-19-39-21__track2c_curve_payload_diagnostics`
- Evaluated Curve Payload Count: `1746`
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
| 3 | `accepted_periodic_mlp_harmonic_Bw` | `periodic_mlp_harmonic` | Bw | backward | 97 | 3.581163 | 0.000612 | 0.001677 | 21.132345 | 17.127352 | 11.625377 | 0.016237 | 0.000861 | 6.713134 |
| 4 | `accepted_periodic_gru_sequence_Bw` | `periodic_gru_sequence` | Bw | backward | 97 | 3.494424 | 0.000606 | 0.001649 | 31.497772 | 15.321099 | 6.640877 | 0.016085 | 0.001313 | 7.571105 |
| 5 | `phase3_c1_linear_compliance_soft_Fw` | `phase3_pinn_c1_linear_compliance_soft_fw` | Fw | forward | 97 | 3.824504 | 0.000932 | 0.001481 | 34.128423 | 21.434153 | 10.008700 | 0.014993 | 0.000873 | 8.458984 |
| 6 | `phase3_c4_hard_elastic_offset_Fw` | `phase3_pinn_c4_hard_elastic_offset_fw` | Fw | forward | 97 | 5.092447 | 0.001585 | 0.001476 | 30.878826 | 18.526879 | 8.996117 | 0.015012 | 0.000873 | 9.256791 |
| 7 | `phase3_c0_learned_mean_control_Fw` | `phase3_pinn_c0_learned_mean_control_fw` | Fw | forward | 97 | 4.076406 | 0.000989 | 0.001608 | 40.929562 | 22.372886 | 6.462809 | 0.015082 | 0.000871 | 9.438823 |
| 8 | `phase3_c0_learned_mean_control_Bw` | `phase3_pinn_c0_learned_mean_control_bw` | Bw | backward | 97 | 4.524874 | 0.001068 | 0.001830 | 39.341202 | 28.222791 | 6.107871 | 0.016250 | 0.000867 | 10.032637 |
| 9 | `phase3_c2_temperature_compliance_soft_Fw` | `phase3_pinn_c2_temperature_compliance_soft_fw` | Fw | forward | 97 | 3.970839 | 0.000979 | 0.001563 | 49.503735 | 23.277599 | 6.550004 | 0.015044 | 0.000873 | 10.235533 |
| 10 | `phase3_c5_shared_stiffness_global` | `phase3_pinn_c5_shared_stiffness_global` | global | backward, forward | 194 | 5.195131 | 0.001635 | 0.001643 | 39.427848 | 23.655728 | 8.576689 | 0.015626 | 0.000868 | 10.476965 |
| 11 | `phase3_c2_temperature_compliance_soft_Bw` | `phase3_pinn_c2_temperature_compliance_soft_bw` | Bw | backward | 97 | 4.069327 | 0.000746 | 0.001859 | 47.274485 | 30.608303 | 6.424044 | 0.016274 | 0.000862 | 10.489927 |
| 12 | `phase3_c3_nonlinear_compliance_soft_Fw` | `phase3_pinn_c3_nonlinear_compliance_soft_fw` | Fw | forward | 97 | 4.359661 | 0.001099 | 0.001662 | 44.033041 | 32.643434 | 11.283580 | 0.015098 | 0.000866 | 10.546113 |
| 13 | `phase3_c3_nonlinear_compliance_soft_Bw` | `phase3_pinn_c3_nonlinear_compliance_soft_bw` | Bw | backward | 97 | 4.755507 | 0.001051 | 0.001978 | 60.411089 | 25.983818 | 7.398145 | 0.016351 | 0.000867 | 12.259314 |
| 14 | `phase3_c0_learned_mean_control_global` | `phase3_pinn_c0_learned_mean_control_global` | global | backward, forward | 194 | 4.963159 | 0.001238 | 0.001834 | 51.201162 | 42.068480 | 7.977089 | 0.015787 | 0.000865 | 12.344572 |
| 15 | `phase3_c4_hard_elastic_offset_Bw` | `phase3_pinn_c4_hard_elastic_offset_bw` | Bw | backward | 97 | 5.755080 | 0.001655 | 0.002031 | 58.129531 | 32.574035 | 8.019210 | 0.016320 | 0.000863 | 13.359935 |
| 16 | `phase3_c1_linear_compliance_soft_Bw` | `phase3_pinn_c1_linear_compliance_soft_bw` | Bw | backward | 97 | 4.656223 | 0.000973 | 0.001985 | 69.396038 | 33.184439 | 5.992358 | 0.016363 | 0.000862 | 13.418680 |

## Interpretation

The strongest screened diagnostic score is `accepted_periodic_mlp_harmonic_Fw`. The score is an analysis aid, not a registry-promotion rule.

Paper-reference and tree-bank candidates may remain strong on curve shape metrics while still being less attractive for deployment. Repository-owned neural candidates should therefore be judged by both diagnostic behavior and future export/runtime feasibility.

## Decision

The next work should not start from `tree` only because of scalar strength. The practical direction is a set of parallel curve-aware retraining or reranking branches: keep searching the `Fw` surface for a deployable repository-owned candidate, prioritize periodic temporal candidates on the `Bw` surface, and carry the best neural `global` candidate as a dedicated cross-direction surface. Harmonic/phase-aware validation stays separate from runtime inputs.

## Runtime Input Boundary

All diagnostics are computed after prediction. Candidate models still consume only current point-level operating state, supported short causal history, or derived causal features. Full curves remain a validation and promotion surface only.

## Machine-Readable Artifacts

- `output\validation_checks\phase3_quasi_static_compliance_pinn_curve_payload_diagnostics\2026-07-26-19-39-21__track2c_curve_payload_diagnostics\candidate_payload_diagnostics.csv`
- `output\validation_checks\phase3_quasi_static_compliance_pinn_curve_payload_diagnostics\2026-07-26-19-39-21__track2c_curve_payload_diagnostics\curve_payload_diagnostics.csv`
- `output\validation_checks\phase3_quasi_static_compliance_pinn_curve_payload_diagnostics\2026-07-26-19-39-21__track2c_curve_payload_diagnostics\harmonic_payload_diagnostics.csv`
- `output\validation_checks\phase3_quasi_static_compliance_pinn_curve_payload_diagnostics\2026-07-26-19-39-21__track2c_curve_payload_diagnostics\curve_payload_samples.jsonl`
- `output\validation_checks\phase3_quasi_static_compliance_pinn_curve_payload_diagnostics\2026-07-26-19-39-21__track2c_curve_payload_diagnostics\track2_curve_payload_diagnostics_summary.yaml`
