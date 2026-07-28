# CVP 1.2 Curve Payload Diagnostics Report

## Overview

This report evaluates a screened `TE Curve Verification Pipeline` candidate set with full truth/prediction curve payloads. It does not train models, alter the dataset structure, or provide future curve samples to runtime model inputs.

- Run Instance: `2026-07-28-15-44-59__track2c_curve_payload_diagnostics`
- Config Path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\wave52r_stage4_data_only_residual_common_test_matrix.yaml`
- Output Directory: `output\validation_checks\wave52r_stage4_data_only_residual_curve_diagnostics\2026-07-28-15-44-59__track2c_curve_payload_diagnostics`
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
| 1 | `stage4_c04_r1_deep` | `stage4_c04_r1_deep` | Fw | forward | 97 | 4.096282 | 0.001216 | 0.001498 | 17.007556 | 14.373442 | 8.994818 | 0.015032 | 0.000870 | 6.666026 |
| 2 | `stage4_c01_r1_compact` | `stage4_c01_r1_compact` | Fw | forward | 97 | 4.128148 | 0.001209 | 0.001500 | 21.650865 | 15.933761 | 8.969251 | 0.015045 | 0.000870 | 7.240371 |
| 3 | `stage4_c05_r1_compact` | `stage4_c05_r1_compact` | Fw | forward | 97 | 4.128148 | 0.001209 | 0.001500 | 21.650865 | 15.933761 | 8.969251 | 0.015045 | 0.000870 | 7.240371 |
| 4 | `stage4_c03_r1_compact` | `stage4_c03_r1_compact` | Fw | forward | 97 | 4.119029 | 0.001084 | 0.001581 | 23.524183 | 16.521671 | 9.888208 | 0.015066 | 0.000872 | 7.448190 |
| 5 | `stage4_c06_r1_deep` | `stage4_c06_r1_deep` | Fw | forward | 97 | 4.165134 | 0.001022 | 0.001599 | 24.306587 | 16.706419 | 9.481974 | 0.015092 | 0.000869 | 7.582034 |
| 6 | `stage4_c02_r1_deep` | `stage4_c02_r1_deep` | Fw | forward | 97 | 4.426188 | 0.001184 | 0.001691 | 22.768536 | 19.768898 | 11.258983 | 0.015143 | 0.000869 | 7.842921 |
| 7 | `stage4_a04_r5_compact` | `stage4_a04_r5_compact` | Fw | forward | 97 | 17.979881 | 0.008091 | 0.002098 | 60.265297 | 36.728414 | 8.722420 | 0.015565 | 0.000880 | 25.998486 |
| 8 | `stage4_a03_r5_compact` | `stage4_a03_r5_compact` | Fw | forward | 97 | 17.265115 | 0.007784 | 0.002077 | 90.651771 | 24.825142 | 11.642372 | 0.015600 | 0.000878 | 27.727549 |
| 9 | `stage4_h03_r3_compact` | `stage4_h03_r3_compact` | Fw | forward | 97 | 33.552096 | 0.014887 | 0.001411 | 21.367862 | 14.533843 | 10.229634 | 0.014978 | 0.000869 | 36.565357 |
| 10 | `stage4_h04_r3_deep` | `stage4_h04_r3_deep` | Fw | forward | 97 | 34.222609 | 0.015138 | 0.001416 | 19.780121 | 14.367219 | 10.320126 | 0.015030 | 0.000868 | 37.069283 |
| 11 | `stage4_a02_r2_compact` | `stage4_a02_r2_compact` | Fw | forward | 97 | 122.188016 | 0.055871 | 0.002268 | 94.610772 | 27.619124 | 10.573830 | 0.015973 | 0.000867 | 133.189780 |
| 12 | `stage4_h05_r4_compact` | `stage4_h05_r4_compact` | Fw | forward | 97 | 131.978255 | 0.060409 | 0.001389 | 17.475491 | 12.552860 | 7.936480 | 0.015010 | 0.000878 | 134.503549 |
| 13 | `stage4_h06_r4_deep` | `stage4_h06_r4_deep` | Fw | forward | 97 | 132.470641 | 0.060621 | 0.001369 | 17.475373 | 12.553020 | 7.960162 | 0.014973 | 0.000875 | 134.995557 |
| 14 | `stage4_h02_r2_deep` | `stage4_h02_r2_deep` | Fw | forward | 97 | 130.819454 | 0.059868 | 0.002037 | 80.401088 | 26.563116 | 10.608567 | 0.015533 | 0.000879 | 140.343051 |
| 15 | `stage4_h07_r5_compact` | `stage4_h07_r5_compact` | Fw | forward | 97 | 131.383637 | 0.060163 | 0.002079 | 86.418823 | 25.455374 | 10.876730 | 0.015649 | 0.000884 | 141.454779 |
| 16 | `stage4_h01_r2_compact` | `stage4_h01_r2_compact` | Fw | forward | 97 | 131.651569 | 0.060261 | 0.002117 | 85.298923 | 26.184198 | 10.333951 | 0.015702 | 0.000872 | 141.647692 |
| 17 | `stage4_h08_r5_deep` | `stage4_h08_r5_deep` | Fw | forward | 97 | 132.710492 | 0.060723 | 0.002036 | 83.465654 | 25.055313 | 10.231114 | 0.015563 | 0.000880 | 142.465454 |
| 18 | `stage4_a01_r2_compact` | `stage4_a01_r2_compact` | Fw | forward | 97 | 132.486487 | 0.060574 | 0.002262 | 98.520110 | 25.964376 | 11.279580 | 0.015932 | 0.000872 | 143.796039 |

## Interpretation

The strongest screened diagnostic score is `stage4_c04_r1_deep`. The score is an analysis aid, not a registry-promotion rule.

Paper-reference and tree-bank candidates may remain strong on curve shape metrics while still being less attractive for deployment. Repository-owned neural candidates should therefore be judged by both diagnostic behavior and future export/runtime feasibility.

## Decision

This bounded Stage 4 diagnostic rejects scalar-only promotion. The six direct
`R1` controls occupy the first six diagnostic positions. Every primary hybrid
fails the separate cancellation audit against the causal `PF-A` anchor and its
capacity-matched direct control. No Stage 4 residual architecture advances,
and no stability-repeat campaign is required.

Stage 5 must align complex sine/cosine coefficient targets, full-curve
reconstruction, and evaluation on the same canonical resampled curve
representation. This report does not alter any official TE Curve Verification
Pipeline decision.

## Runtime Input Boundary

All diagnostics are computed after prediction. Candidate models still consume only current point-level operating state, supported short causal history, or derived causal features. Full curves remain a validation and promotion surface only.

## Machine-Readable Artifacts

- `output\validation_checks\wave52r_stage4_data_only_residual_curve_diagnostics\2026-07-28-15-44-59__track2c_curve_payload_diagnostics\candidate_payload_diagnostics.csv`
- `output\validation_checks\wave52r_stage4_data_only_residual_curve_diagnostics\2026-07-28-15-44-59__track2c_curve_payload_diagnostics\curve_payload_diagnostics.csv`
- `output\validation_checks\wave52r_stage4_data_only_residual_curve_diagnostics\2026-07-28-15-44-59__track2c_curve_payload_diagnostics\harmonic_payload_diagnostics.csv`
- `output\validation_checks\wave52r_stage4_data_only_residual_curve_diagnostics\2026-07-28-15-44-59__track2c_curve_payload_diagnostics\curve_payload_samples.jsonl`
- `output\validation_checks\wave52r_stage4_data_only_residual_curve_diagnostics\2026-07-28-15-44-59__track2c_curve_payload_diagnostics\track2_curve_payload_diagnostics_summary.yaml`
