# Track 2 Official Model Verification Report

## Executive Verdict

This automated official refresh report closes `Wave 3 harmonic-prior residual refresh`.

Decision:

- `wave3_harmonic_prior_residual_registry` is closed as verified exploratory baseline; not promoted over the accepted direction-parallel leaders.
- The strongest refreshed aggregate candidate is `wave3_harmonic_prior_residual_pointwise_control_Bw`.
- The accepted direction-parallel baseline changes only after a human closure review records that promotion explicitly.
- This launcher-generated report is part of the same operator run as the matrix, collage, overlay, and PDF exports.

## Source Package

This official report consolidates these refreshed artifacts:

- metric matrix:
  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;
- matrix summary:
  `output/validation_checks/track2_reference_comparison/2026-06-15-20-25-36__track2_full_directional_family_matrix_wave3_harmonic_prior_residual_track2_refresh_2026_06_15/validation_summary.yaml`;
- per-condition metrics:
  `output/validation_checks/track2_reference_comparison/2026-06-15-20-25-36__track2_full_directional_family_matrix_wave3_harmonic_prior_residual_track2_refresh_2026_06_15/per_condition_metrics.csv`;
- best-model collage report:
  `doc/reports/analysis/track2/best_model_collage_report/[2026-06-15]/track2_best_model_collage_report.md`;
- multi-model curve comparison report:
  `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-06-15]/track2_multi_model_curve_comparison_report.md`;
- operator launch logs:
  `output/validation_checks/track2_operator_launch_logs/2026-06-15-20-25-26_wave3_harmonic_prior_residual_track2_refresh_2026_06_15`.

## Candidate Refresh

The refresh added `6` candidates from `wave3_harmonic_prior_residual_registry` into the official `159`-candidate matrix.

| Surface | Candidate | Family |
| --- | --- | --- |
| global | `wave3_harmonic_prior_residual_pointwise_control_global` | `wave3_harmonic_prior_residual_pointwise_control` |
| Fw | `wave3_harmonic_prior_residual_pointwise_control_Fw` | `wave3_harmonic_prior_residual_pointwise_control` |
| Bw | `wave3_harmonic_prior_residual_pointwise_control_Bw` | `wave3_harmonic_prior_residual_pointwise_control` |
| global | `wave3_harmonic_prior_residual_smooth_l1_structured_global` | `wave3_harmonic_prior_residual_smooth_l1_structured` |
| Fw | `wave3_harmonic_prior_residual_smooth_l1_structured_Fw` | `wave3_harmonic_prior_residual_smooth_l1_structured` |
| Bw | `wave3_harmonic_prior_residual_smooth_l1_structured_Bw` | `wave3_harmonic_prior_residual_smooth_l1_structured` |

## Refreshed Source Leaders

The table ranks the refreshed source by aggregate offline Track 2 metrics.

| Surface | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| Fw | `wave3_harmonic_prior_residual_pointwise_control_Fw` | 0.003374 | 0.003655 | 7.501 | 12.728 |
| Bw | `wave3_harmonic_prior_residual_pointwise_control_Bw` | 0.003360 | 0.003677 | 7.363 | 13.296 |
| global | `wave3_harmonic_prior_residual_smooth_l1_structured_global` | 0.003399 | 0.003714 | 7.502 | 12.356 |

## Refreshed Source Leaderboard

| Rank | Surface | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | Bw | `wave3_harmonic_prior_residual_pointwise_control_Bw` | 0.003360 | 0.003677 | 7.363 | 13.296 |
| 2 | Fw | `wave3_harmonic_prior_residual_pointwise_control_Fw` | 0.003374 | 0.003655 | 7.501 | 12.728 |
| 3 | global | `wave3_harmonic_prior_residual_smooth_l1_structured_global` | 0.003399 | 0.003714 | 7.502 | 12.356 |
| 4 | Bw | `wave3_harmonic_prior_residual_smooth_l1_structured_Bw` | 0.003431 | 0.003739 | 7.523 | 13.200 |
| 5 | global | `wave3_harmonic_prior_residual_pointwise_control_global` | 0.003442 | 0.003755 | 7.597 | 14.110 |
| 6 | Fw | `wave3_harmonic_prior_residual_smooth_l1_structured_Fw` | 0.003514 | 0.003768 | 7.812 | 13.703 |

## Current Direction Leaders

These leaders are read from the matrix direction breakdown after the refresh.

| Direction | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| backward | `periodic_gru_sequence_Bw` | 0.002392 | 0.002639 | 5.466 | 14.820 |
| forward | `rcim_retuned_GBM19_Fw` | 0.001089 | 0.001299 | 2.372 | 4.912 |

## Visual Evidence

The same launcher run regenerated the visual companion reports and verified
that the refreshed source appears in the visual package.

| Source | Collage | Overlay Forward | Overlay Backward |
| --- | ---: | ---: | ---: |
| `wave3_harmonic_prior_residual_registry` | 6 | 2 | 2 |

## Closeout Decision

`Wave 3 harmonic-prior residual refresh` is closed as: verified exploratory baseline; not promoted over the accepted direction-parallel leaders.

Use the Wave 3 Track 2 curve, offset, collage, and overlay evidence to decide whether to continue Wave 3, move to Wave 4, or reopen latent-state modeling.
