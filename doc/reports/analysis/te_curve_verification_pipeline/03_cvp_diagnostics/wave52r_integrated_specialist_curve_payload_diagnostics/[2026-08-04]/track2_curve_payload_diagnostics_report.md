# CVP 1.2 Curve Payload Diagnostics Report

## Overview

This report evaluates a screened `TE Curve Verification Pipeline` candidate set with full truth/prediction curve payloads. It does not train models, alter the dataset structure, or provide future curve samples to runtime model inputs.

- Run Instance: `2026-08-04-00-31-50__track2c_curve_payload_diagnostics`
- Config Path: `config\paper_reimplementation\rcim_ml_compensation\reference_family_vs_feedforward\wave52r_integrated_specialist_track2_matrix.yaml`
- Output Directory: `output\validation_checks\wave52r_integrated_specialist_track2_curve_payload_diagnostics\2026-08-04-00-31-50__track2c_curve_payload_diagnostics`
- Evaluated Curve Payload Count: `1649`
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
| 1 | `wave52r_integrated_a02_seed_314159` | `wave52r_integrated_specialist_a02` | global | backward, forward | 194 | 2.889637 | 0.000577 | 0.001222 | 4.666271 | 2.905623 | 6.506941 | 0.015090 | 0.000872 | 3.652449 |
| 2 | `wave52r_integrated_a07_seed_314159` | `wave52r_integrated_specialist_a07` | global | backward, forward | 194 | 2.888332 | 0.000577 | 0.001223 | 4.892993 | 2.816239 | 6.563035 | 0.015095 | 0.000873 | 3.669398 |
| 3 | `wave52r_promotion_k01_global_seed_271828` | `wave52r_promotion_k01` | global | backward, forward | 194 | 2.893177 | 0.000577 | 0.001225 | 4.838683 | 2.829332 | 6.472221 | 0.015095 | 0.000872 | 3.669466 |
| 4 | `wave52r_integrated_a06_seed_271828` | `wave52r_integrated_specialist_a06` | global | backward, forward | 194 | 2.888503 | 0.000577 | 0.001224 | 4.869504 | 2.936109 | 6.475306 | 0.015093 | 0.000870 | 3.673189 |
| 5 | `wave52r_integrated_a04_seed_161803` | `wave52r_integrated_specialist_a04` | global | backward, forward | 194 | 2.877027 | 0.000577 | 0.001216 | 5.054674 | 2.805877 | 6.647853 | 0.015085 | 0.000872 | 3.673642 |
| 6 | `wave52r_integrated_a05_seed_161803` | `wave52r_integrated_specialist_a05` | global | backward, forward | 194 | 2.883889 | 0.000577 | 0.001220 | 5.130035 | 2.797664 | 6.812446 | 0.015089 | 0.000873 | 3.687666 |
| 7 | `wave52r_integrated_a07_seed_161803` | `wave52r_integrated_specialist_a07` | global | backward, forward | 194 | 2.890023 | 0.000577 | 0.001224 | 5.135538 | 2.815074 | 6.553092 | 0.015094 | 0.000869 | 3.695270 |
| 8 | `wave52r_integrated_a03_seed_161803` | `wave52r_integrated_specialist_a03` | global | backward, forward | 194 | 2.885171 | 0.000577 | 0.001218 | 6.277461 | 2.824242 | 6.430037 | 0.015082 | 0.000873 | 3.804948 |
| 9 | `wave52r_promotion_h08_fw_seed_161803` | `wave52r_promotion_h08` | Fw | forward | 97 | 3.477261 | 0.000862 | 0.001320 | 5.931030 | 4.713399 | 7.958770 | 0.014914 | 0.000872 | 4.455170 |

## Interpretation

The strongest screened diagnostic score is `wave52r_integrated_a02_seed_314159`. The score is an analysis aid, not a registry-promotion rule.

Paper-reference and tree-bank candidates may remain strong on curve shape metrics while still being less attractive for deployment. Repository-owned neural candidates should therefore be judged by both diagnostic behavior and future export/runtime feasibility.

## Decision

This shortlist diagnostic supports A02 seed `314159` as the strongest balanced
payload candidate. The separate official multi-index review recommends A02 on
`Fw` and routed `global`, while retaining frozen K01 seed `271828` on `Bw`.
A03-A07 remain diagnostic because their campaign branch gates failed. This
report does not change accepted registries or establish deployment readiness.

## Runtime Input Boundary

All diagnostics are computed after prediction. Candidate models still consume only current point-level operating state, supported short causal history, or derived causal features. Full curves remain a validation and promotion surface only.

## Machine-Readable Artifacts

- `output\validation_checks\wave52r_integrated_specialist_track2_curve_payload_diagnostics\2026-08-04-00-31-50__track2c_curve_payload_diagnostics\candidate_payload_diagnostics.csv`
- `output\validation_checks\wave52r_integrated_specialist_track2_curve_payload_diagnostics\2026-08-04-00-31-50__track2c_curve_payload_diagnostics\curve_payload_diagnostics.csv`
- `output\validation_checks\wave52r_integrated_specialist_track2_curve_payload_diagnostics\2026-08-04-00-31-50__track2c_curve_payload_diagnostics\harmonic_payload_diagnostics.csv`
- `output\validation_checks\wave52r_integrated_specialist_track2_curve_payload_diagnostics\2026-08-04-00-31-50__track2c_curve_payload_diagnostics\curve_payload_samples.jsonl`
- `output\validation_checks\wave52r_integrated_specialist_track2_curve_payload_diagnostics\2026-08-04-00-31-50__track2c_curve_payload_diagnostics\track2_curve_payload_diagnostics_summary.yaml`
