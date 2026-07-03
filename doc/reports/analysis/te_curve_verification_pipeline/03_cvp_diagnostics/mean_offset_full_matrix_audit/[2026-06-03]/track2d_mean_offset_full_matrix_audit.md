# CVP 1.4 Mean-Offset Full-Matrix Audit

## Overview

This report extends the `TE Curve Verification Pipeline` mean-centered collage diagnostic to the full official direction-valid candidate matrix. It computes raw curve error, curve-bias / `DC` offset, centered-shape error, peak-to-peak amplitude error, harmonic amplitude error, and harmonic phase error after every candidate produces predictions through its normal causal input path.

This is an analysis-only diagnostic. It does not train models, alter the
dataset structure, update registries, or make full-curve mean-centering
a deployment-time correction.

- Run Instance: `2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit`
- Config Path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\full_track2_matrix_template.yaml`
- Output Directory: `output\validation_checks\track2d_mean_offset_full_matrix_audit\2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit`
- Candidate Count: `111`
- Evaluated Curve Count: `12416`
- Harmonic Orders: `1, 3, 39, 40, 78, 81, 156, 162, 240`

## Method

- raw `MAE` and `RMSE` are computed on the normal prediction residual;
- offset is the absolute difference between predicted and measured curve
  means;
- centered metrics subtract each curve's own mean from truth and
  prediction separately after inference;
- amplitude error compares predicted and measured peak-to-peak TE;
- harmonic amplitude and phase diagnostics are computed on selected
  sparse `RCIM` harmonic orders;
- condition summaries stratify by direction, speed, torque, and oil
  temperature.

## Diagnostic Label Counts

| Label | Candidate Count |
| --- | --- |
| `shape` | 3 |
| `mixed:shape+amp` | 10 |
| `mixed:shape+amp+phase` | 3 |
| `mixed:shape+amp+phase+regime` | 2 |
| `mixed:shape+phase` | 4 |
| `mixed:shape+phase+regime` | 1 |
| `mixed:offset+amp` | 3 |
| `mixed:offset+amp+phase` | 7 |
| `mixed:offset+regime` | 26 |
| `mixed:offset+phase` | 15 |
| `mixed:offset+phase+regime` | 1 |
| `offset` | 36 |

## CVP 1.4 Diagnostic Ranking

| Rank | Candidate | Surface | Raw MAE | Centered MAE | Offset | Gain [%] | Label |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `rcim_retuned_GBM19_Fw` | Fw | 0.001089 | 0.000832 | 0.000634 | 21.8 | shape |
| 2 | `rcim_original_ERT19_Fw` | Fw | 0.001471 | 0.000831 | 0.001138 | 38.6 | offset |
| 3 | `rcim_retuned_RF19_Fw` | Fw | 0.001487 | 0.000834 | 0.001183 | 40.0 | offset |
| 4 | `paper_retuned_best_Fw` | Fw | 0.001839 | 0.000833 | 0.001562 | 43.2 | mixed:offset+regime |
| 5 | `rcim_retuned_ERT19_Fw` | Fw | 0.001807 | 0.000833 | 0.001543 | 46.9 | offset |
| 6 | `rcim_original_RF19_Fw` | Fw | 0.001767 | 0.000837 | 0.001502 | 45.9 | offset |
| 7 | `rcim_original_DT19_Fw` | Fw | 0.001919 | 0.000834 | 0.001590 | 43.2 | offset |
| 8 | `rcim_retuned_DT19_Fw` | Fw | 0.001919 | 0.000834 | 0.001590 | 43.2 | offset |
| 9 | `rcim_original_LGBM19_Fw` | Fw | 0.001801 | 0.000846 | 0.001487 | 40.8 | mixed:offset+regime |
| 10 | `rcim_original_GBM19_Fw` | Fw | 0.001921 | 0.000834 | 0.001672 | 49.1 | offset |
| 11 | `rcim_retuned_ET19_Fw` | Fw | 0.002001 | 0.000835 | 0.001704 | 43.7 | offset |
| 12 | `rcim_retuned_LGBM19_Fw` | Fw | 0.001851 | 0.000846 | 0.001562 | 43.0 | mixed:offset+regime |
| 13 | `rcim_retuned_HGBM19_Fw` | Fw | 0.001851 | 0.000849 | 0.001554 | 42.7 | mixed:offset+regime |
| 14 | `ERT19_Fw` | Fw | 0.002295 | 0.000842 | 0.002062 | 52.6 | mixed:offset+regime |
| 15 | `rcim_original_HGBM19_Fw` | Fw | 0.002011 | 0.000859 | 0.001737 | 45.9 | mixed:offset+regime |
| 16 | `paper_original_best_Fw` | Fw | 0.002769 | 0.000833 | 0.002552 | 54.4 | offset |
| 17 | `rcim_original_ET19_Fw` | Fw | 0.002232 | 0.000896 | 0.001880 | 46.4 | mixed:offset+regime |
| 18 | `RF19_Fw` | Fw | 0.002164 | 0.000889 | 0.001844 | 45.5 | mixed:offset+regime |
| 19 | `rcim_retuned_XGBM19_Fw` | Fw | 0.002054 | 0.000852 | 0.001835 | 48.2 | mixed:offset+regime |
| 20 | `track1_best_Fw` | Fw | 0.003014 | 0.000857 | 0.002894 | 65.1 | offset |

## Surface Leaders

| Rank | Candidate | Surface | Raw MAE | Centered MAE | Offset | Gain [%] | Label |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `DT19_Bw` | Bw | 0.005226 | 0.000882 | 0.004999 | 55.1 | mixed:offset+regime |
| 1 | `rcim_retuned_GBM19_Fw` | Fw | 0.001089 | 0.000832 | 0.000634 | 21.8 | shape |
| 1 | `periodic_gru_sequence_global` | global | 0.002704 | 0.000992 | 0.002501 | 50.9 | offset |

## Largest Mean-Offset Improvements

| Rank | Candidate | Surface | Raw MAE | Centered MAE | Offset | Gain [%] | Label |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 94 | `harmonic_regression_global` | global | 0.018160 | 0.001758 | 0.018035 | 82.3 | mixed:offset+amp+phase |
| 43 | `LGBM19_Fw` | Fw | 0.006812 | 0.001098 | 0.006679 | 73.5 | offset |
| 48 | `XGBM19_Bw` | Bw | 0.007991 | 0.001191 | 0.007742 | 71.2 | mixed:offset+regime |
| 53 | `ELM19_Fw` | Fw | 0.007281 | 0.001437 | 0.007080 | 70.0 | offset |
| 41 | `HGBM19_Bw` | Bw | 0.006619 | 0.001112 | 0.006401 | 68.8 | mixed:offset+regime |
| 91 | `ELM19_Bw` | Bw | 0.010071 | 0.002022 | 0.009682 | 66.5 | mixed:offset+regime |
| 52 | `rcim_retuned_ELM19_Fw` | Fw | 0.007182 | 0.001435 | 0.006948 | 66.4 | mixed:offset+regime |
| 92 | `rcim_retuned_XGBM19_Bw` | Bw | 0.010679 | 0.002800 | 0.010116 | 65.9 | mixed:offset+phase |
| 20 | `track1_best_Fw` | Fw | 0.003014 | 0.000857 | 0.002894 | 65.1 | offset |
| 35 | `XGBM19_Fw` | Fw | 0.004190 | 0.000998 | 0.003987 | 63.2 | mixed:offset+regime |
| 46 | `ET19_Bw` | Bw | 0.006273 | 0.001387 | 0.005763 | 62.2 | mixed:offset+regime |
| 22 | `DT19_Fw` | Fw | 0.003122 | 0.000872 | 0.002972 | 61.9 | offset |
| 50 | `rcim_original_ELM19_Fw` | Fw | 0.005423 | 0.001461 | 0.005039 | 61.6 | mixed:offset+regime |
| 51 | `SVM19_Bw` | Bw | 0.004822 | 0.001544 | 0.004261 | 61.1 | mixed:offset+regime |
| 37 | `SVM19_Fw` | Fw | 0.003236 | 0.001175 | 0.002894 | 61.0 | offset |

## Interpretation

The ranking is a diagnostic ordering, not a promotion rule. Offset-limited candidates need a causal offset-calibration or offset-aware loss strategy. Centered-shape-limited candidates need waveform-shape, derivative, harmonic amplitude, or phase improvements before retraining should be expanded.

The next training decision should keep `Fw`, `Bw`, and `global` surfaces in parallel. A forward leader does not close the backward or global branch, and a backward leader does not close the forward or global branch.

## Runtime Input Boundary

All full-curve operations are post-prediction diagnostics. Candidate models still consume only current point-level state, an explicitly supported short causal history, or causal derived features. The audit does not use future TE samples as model inputs.

## Machine-Readable Artifacts

- `output\validation_checks\track2d_mean_offset_full_matrix_audit\2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit\track2d_per_curve_metrics.csv`
- `output\validation_checks\track2d_mean_offset_full_matrix_audit\2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit\track2d_candidate_summary.csv`
- `output\validation_checks\track2d_mean_offset_full_matrix_audit\2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit\track2d_surface_leaderboard.csv`
- `output\validation_checks\track2d_mean_offset_full_matrix_audit\2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit\track2d_condition_stratified_summary.csv`
- `output\validation_checks\track2d_mean_offset_full_matrix_audit\2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit\track2d_mean_offset_full_matrix_audit_summary.yaml`
