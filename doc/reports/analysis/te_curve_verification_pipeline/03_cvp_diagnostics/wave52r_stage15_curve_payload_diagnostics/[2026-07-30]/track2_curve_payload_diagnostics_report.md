# CVP 1.2 Curve Payload Diagnostics Report

## Overview

This report evaluates a screened `TE Curve Verification Pipeline` candidate set with full truth/prediction curve payloads. It does not train models, alter the dataset structure, or provide future curve samples to runtime model inputs.

- Run Instance: `2026-07-30-01-11-50__track2c_curve_payload_diagnostics`
- Config Path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\wave52r_stage15_official_forward_verification_matrix.yaml`
- Output Directory: `output\validation_checks\wave52r_stage15_curve_payload_diagnostics\2026-07-30-01-11-50__track2c_curve_payload_diagnostics`
- Evaluated Curve Payload Count: `388`
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
| 2 | `wave52r_stage15_h04_bounded_coefficient_residual_Fw` | `complex_harmonic_coefficient_residuals` | Fw | forward | 97 | 3.560378 | 0.000884 | 0.001359 | 16.318554 | 11.771944 | 10.600128 | 0.014938 | 0.000869 | 5.930207 |
| 3 | `accepted_periodic_gru_sequence_Fw` | `periodic_gru_sequence` | Fw | forward | 97 | 3.278427 | 0.000690 | 0.001382 | 19.236860 | 12.165789 | 8.443678 | 0.014968 | 0.000892 | 5.960079 |
| 4 | `wave52r_stage15_pf_a_setpoint_quadratic_Fw` | `polynomial_fourier_pf_a` | Fw | forward | 97 | 3.748632 | 0.000975 | 0.001385 | 17.475311 | 12.552995 | 10.567277 | 0.014969 | 0.000869 | 6.273501 |

## Interpretation

The strongest screened diagnostic score is `accepted_periodic_mlp_harmonic_Fw`. The score is an analysis aid, not a registry-promotion rule.

Paper-reference and tree-bank candidates may remain strong on curve shape metrics while still being less attractive for deployment. Repository-owned neural candidates should therefore be judged by both diagnostic behavior and future export/runtime feasibility.

## Decision

The next work should not start from `tree` only because of scalar strength. The practical direction is a set of parallel curve-aware retraining or reranking branches: keep searching the `Fw` surface for a deployable repository-owned candidate, prioritize periodic temporal candidates on the `Bw` surface, and carry the best neural `global` candidate as a dedicated cross-direction surface. Harmonic/phase-aware validation stays separate from runtime inputs.

## Runtime Input Boundary

All diagnostics are computed after prediction. Candidate models still consume only current point-level operating state, supported short causal history, or derived causal features. Full curves remain a validation and promotion surface only.

## Machine-Readable Artifacts

- `output\validation_checks\wave52r_stage15_curve_payload_diagnostics\2026-07-30-01-11-50__track2c_curve_payload_diagnostics\candidate_payload_diagnostics.csv`
- `output\validation_checks\wave52r_stage15_curve_payload_diagnostics\2026-07-30-01-11-50__track2c_curve_payload_diagnostics\curve_payload_diagnostics.csv`
- `output\validation_checks\wave52r_stage15_curve_payload_diagnostics\2026-07-30-01-11-50__track2c_curve_payload_diagnostics\harmonic_payload_diagnostics.csv`
- `output\validation_checks\wave52r_stage15_curve_payload_diagnostics\2026-07-30-01-11-50__track2c_curve_payload_diagnostics\curve_payload_samples.jsonl`
- `output\validation_checks\wave52r_stage15_curve_payload_diagnostics\2026-07-30-01-11-50__track2c_curve_payload_diagnostics\track2_curve_payload_diagnostics_summary.yaml`
