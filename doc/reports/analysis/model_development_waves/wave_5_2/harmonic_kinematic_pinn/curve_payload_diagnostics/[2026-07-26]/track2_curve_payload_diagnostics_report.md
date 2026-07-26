# CVP 1.2 Curve Payload Diagnostics Report

## Overview

This report evaluates a screened `TE Curve Verification Pipeline` candidate set with full truth/prediction curve payloads. It does not train models, alter the dataset structure, or provide future curve samples to runtime model inputs.

- Run Instance: `2026-07-26-16-49-48__track2c_curve_payload_diagnostics`
- Config Path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\phase2_harmonic_kinematic_pinn_common_test_matrix.yaml`
- Output Directory: `output\validation_checks\phase2_harmonic_kinematic_pinn_curve_payload_diagnostics\2026-07-26-16-49-48__track2c_curve_payload_diagnostics`
- Evaluated Curve Payload Count: `1164`
- Harmonic Orders: `1, 3, 39, 40, 78, 81, 156, 162, 240`
- Stored payload samples are downsampled for repository-size control.

## Method

Diagnostics are computed on full held-out `TE` curves after each candidate produces pointwise predictions through its normal causal input path. The report separates the validation surface from the runtime input contract.

Computed diagnostics:

- peak-to-peak amplitude error and residual peak-to-peak ratio;
- selected-harmonic amplitude and wrapped phase error;
- local derivative `RMSE`;
- residual second-derivative smoothness;
- residual lag-one autocorrelation;
- per-revolution closure mismatch and deterministic stitched-boundary surrogate.

## Candidate Diagnostic Ranking

| Rank | Candidate | Family | Surface | Directions | Curves | Mean MPE [%] | Mean Harmonic Amp Error [%] | Mean Harmonic Phase Error [deg] | Mean P2P Error [%] | Derivative RMSE | Closure Mismatch [deg] | Diagnostic Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `accepted_periodic_mlp_harmonic_Fw` | `periodic_mlp_harmonic` | Fw | forward | 97 | 3.438600 | 15.380051 | 13.591649 | 11.801784 | 0.014963 | 0.000881 | 5.805821 |
| 2 | `accepted_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | Fw | forward | 97 | 3.278412 | 19.237460 | 12.166874 | 8.444949 | 0.014968 | 0.000892 | 5.960178 |
| 3 | `accepted_periodic_mlp_harmonic_Bw` | `periodic_mlp_harmonic` | Bw | backward | 97 | 3.581163 | 21.132345 | 17.127352 | 11.625377 | 0.016237 | 0.000861 | 6.713134 |
| 4 | `accepted_periodic_gru_sequence_Bw` | `periodic_gru_sequence` | Bw | backward | 97 | 3.494424 | 31.497772 | 15.321099 | 6.640877 | 0.016085 | 0.001313 | 7.571105 |
| 5 | `phase2_h0_fourier_control_Fw` | `phase2_pinn_h0_fourier_control_fw` | Fw | forward | 97 | 4.173514 | 39.328382 | 21.028767 | 6.794572 | 0.014997 | 0.000872 | 9.307758 |
| 6 | `phase2_h1_oscillator_residual_Fw` | `phase2_pinn_h1_oscillator_residual_fw` | Fw | forward | 97 | 4.733960 | 43.016095 | 19.898644 | 8.212092 | 0.015073 | 0.000857 | 10.181231 |
| 7 | `phase2_h2_oscillator_periodic_closure_Fw` | `phase2_pinn_h2_oscillator_periodic_closure_fw` | Fw | forward | 97 | 4.407004 | 49.490626 | 20.334512 | 8.259385 | 0.015095 | 0.000938 | 10.523739 |
| 8 | `phase2_h1_oscillator_residual_Bw` | `phase2_pinn_h1_oscillator_residual_bw` | Bw | backward | 97 | 4.234332 | 52.096773 | 24.207508 | 9.569042 | 0.016400 | 0.000865 | 10.818388 |
| 9 | `phase2_h3_oscillator_periodic_bauer_anchor_Bw` | `phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw` | Bw | backward | 97 | 4.709867 | 56.021931 | 25.209300 | 10.089244 | 0.016411 | 0.000864 | 11.736637 |
| 10 | `phase2_h0_fourier_control_Bw` | `phase2_pinn_h0_fourier_control_bw` | Bw | backward | 97 | 5.020595 | 48.979093 | 33.574049 | 9.581933 | 0.016394 | 0.000868 | 11.761152 |
| 11 | `phase2_h2_oscillator_periodic_closure_Bw` | `phase2_pinn_h2_oscillator_periodic_closure_bw` | Bw | backward | 97 | 4.801930 | 60.967104 | 25.537411 | 10.003031 | 0.016438 | 0.000869 | 12.339891 |
| 12 | `phase2_h3_oscillator_periodic_bauer_anchor_Fw` | `phase2_pinn_h3_oscillator_periodic_bauer_anchor_fw` | Fw | forward | 97 | 5.643960 | 69.328526 | 27.109743 | 10.300713 | 0.015148 | 0.000957 | 14.083776 |

## Interpretation

The strongest screened diagnostic score is `accepted_periodic_mlp_harmonic_Fw`. The score is an analysis aid, not a registry-promotion rule.

Paper-reference and tree-bank candidates may remain strong on curve shape metrics while still being less attractive for deployment. Repository-owned neural candidates should therefore be judged by both diagnostic behavior and future export/runtime feasibility.

## Decision

The next work should not start from `tree` only because of scalar strength. The practical direction is a set of parallel curve-aware retraining or reranking branches: keep searching the `Fw` surface for a deployable repository-owned candidate, prioritize periodic temporal candidates on the `Bw` surface, and carry the best neural `global` candidate as a dedicated cross-direction surface. Harmonic/phase-aware validation stays separate from runtime inputs.

## Runtime Input Boundary

All diagnostics are computed after prediction. Candidate models still consume only current point-level operating state, supported short causal history, or derived causal features. Full curves remain a validation and promotion surface only.

## Machine-Readable Artifacts

- `output\validation_checks\phase2_harmonic_kinematic_pinn_curve_payload_diagnostics\2026-07-26-16-49-48__track2c_curve_payload_diagnostics\candidate_payload_diagnostics.csv`
- `output\validation_checks\phase2_harmonic_kinematic_pinn_curve_payload_diagnostics\2026-07-26-16-49-48__track2c_curve_payload_diagnostics\curve_payload_diagnostics.csv`
- `output\validation_checks\phase2_harmonic_kinematic_pinn_curve_payload_diagnostics\2026-07-26-16-49-48__track2c_curve_payload_diagnostics\harmonic_payload_diagnostics.csv`
- `output\validation_checks\phase2_harmonic_kinematic_pinn_curve_payload_diagnostics\2026-07-26-16-49-48__track2c_curve_payload_diagnostics\curve_payload_samples.jsonl`
- `output\validation_checks\phase2_harmonic_kinematic_pinn_curve_payload_diagnostics\2026-07-26-16-49-48__track2c_curve_payload_diagnostics\track2_curve_payload_diagnostics_summary.yaml`
