# Track 2C Curve Payload Diagnostics Report

## Overview

This report evaluates a screened `Track 2` candidate set with full truth/prediction curve payloads. It does not train models, alter the dataset structure, or provide future curve samples to runtime model inputs.

- Run Instance: `2026-05-28-19-55-32__track2c_curve_payload_diagnostics`
- Config Path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\full_track2_matrix_template.yaml`
- Output Directory: `output\validation_checks\track2_curve_payload_diagnostics\2026-05-28-19-55-32__track2c_curve_payload_diagnostics`
- Evaluated Curve Payload Count: `1164`
- Harmonic Orders: `1, 2, 3, 4, 5, 6, 8, 10, 12, 19`
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
| 1 | `rcim_retuned_GBM19_Fw` | `GBM` | Fw | forward | 97 | 2.371752 | 33.021378 | 28.258963 | 8.089395 | 0.014046 | 0.000676 | 7.227298 |
| 2 | `periodic_gru_sequence_Bw` | `periodic_gru_sequence` | Bw | backward | 97 | 5.465990 | 14.792262 | 8.570493 | 5.458720 | 0.014554 | 0.001096 | 7.519285 |
| 3 | `periodic_lstm_sequence_global` | `periodic_lstm_sequence` | global | backward, forward | 194 | 6.119950 | 17.757138 | 11.622748 | 5.863664 | 0.014515 | 0.001083 | 8.621953 |
| 4 | `tree_global` | `tree` | global | backward, forward | 194 | 6.854374 | 19.143975 | 11.526651 | 18.028018 | 0.015841 | 0.000994 | 9.503512 |
| 5 | `tree_Bw` | `tree` | Bw | backward | 97 | 7.051484 | 19.173838 | 7.988429 | 17.916583 | 0.016235 | 0.001254 | 9.530644 |
| 6 | `harmonic_regression_Bw` | `harmonic_regression` | Bw | backward | 97 | 8.170944 | 9.758297 | 5.090618 | 18.926302 | 0.015682 | 0.000750 | 9.558129 |
| 7 | `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `residual_harmonic_lstm_sequence_sparse_rcim` | Bw | backward | 97 | 7.510266 | 27.574565 | 7.534689 | 10.580972 | 0.015573 | 0.000772 | 10.800185 |
| 8 | `residual_harmonic_lstm_sequence_sparse_rcim_global` | `residual_harmonic_lstm_sequence_sparse_rcim` | global | backward, forward | 194 | 7.409051 | 31.641801 | 28.653671 | 13.339015 | 0.015170 | 0.000819 | 12.157611 |
| 9 | `rcim_retuned_GBM19_Bw` | `GBM` | Bw | backward | 97 | 5.398275 | 32.964035 | 76.738397 | 5.703129 | 0.017353 | 0.000801 | 12.705128 |

## Interpretation

The strongest screened diagnostic score is `rcim_retuned_GBM19_Fw`. The score is an analysis aid, not a registry-promotion rule.

The strongest screened forward candidate is still the paper-reference `rcim_retuned_GBM19_Fw`. The forward repository-owned branch therefore remains open and should not be closed just because the backward neural branch is stronger.

The strongest screened repository-owned backward candidate is `periodic_gru_sequence_Bw`. It is close to `rcim_retuned_GBM19_Bw` on mean percentage error, but has much better selected-harmonic phase behavior in this diagnostic pass.

`periodic_lstm_sequence_global` is the strongest screened global-surface neural candidate. It keeps low peak-to-peak error on both directions and must remain a separate global branch, not a weaker substitute for the backward-only `periodic_gru_sequence_Bw` branch.

`harmonic_regression_Bw` has the cleanest selected-harmonic amplitude and phase diagnostics in the backward-only set, but its mean percentage error and peak-to-peak error remain worse than the periodic temporal candidates.

`tree_Bw` and `tree_global` confirm the visual concern from Track 2: scalar error can look competitive while peak-to-peak and shape diagnostics remain weaker.

Paper-reference and tree-bank candidates may remain strong on some curve metrics while still being less attractive for deployment. Repository-owned neural candidates should therefore be judged by both diagnostic behavior and future export/runtime feasibility.

## Decision

The next work should not start from `tree`, despite its scalar strength. The practical direction is a set of parallel curve-aware retraining or reranking branches: keep searching the `Fw` surface for a deployable repository-owned candidate, prioritize `periodic_gru_sequence_Bw` on the `Bw` surface, and carry `periodic_lstm_sequence_global` as the dedicated global-surface candidate. Harmonic/phase-aware validation stays separate from runtime inputs.

## Runtime Input Boundary

All diagnostics are computed after prediction. Candidate models still consume only current point-level operating state, supported short causal history, or derived causal features. Full curves remain a validation and promotion surface only.

## Machine-Readable Artifacts

- `output\validation_checks\track2_curve_payload_diagnostics\2026-05-28-19-55-32__track2c_curve_payload_diagnostics\candidate_payload_diagnostics.csv`
- `output\validation_checks\track2_curve_payload_diagnostics\2026-05-28-19-55-32__track2c_curve_payload_diagnostics\curve_payload_diagnostics.csv`
- `output\validation_checks\track2_curve_payload_diagnostics\2026-05-28-19-55-32__track2c_curve_payload_diagnostics\curve_payload_samples.jsonl`
- `output\validation_checks\track2_curve_payload_diagnostics\2026-05-28-19-55-32__track2c_curve_payload_diagnostics\track2_curve_payload_diagnostics_summary.yaml`
