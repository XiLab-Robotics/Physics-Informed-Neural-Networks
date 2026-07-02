# TE Curve Verification Pipeline Official Model Verification Report

## Executive Verdict

This automated official refresh report closes `Wave 5.2B offset and harmonic guided refresh`.

Decision:

- `wave52b_offset_harmonic_guided_registry` is closed as pending operator review; do not promote from scalar metrics alone.
- The strongest refreshed aggregate candidate is `wave52b_offset_centered_shape_harmonic_Fw`.
- The accepted direction-parallel baseline changes only after a human closure review records that promotion explicitly.
- This launcher-generated report is part of the same operator run as the matrix, collage, overlay, and PDF exports.

## Source Package

This official report consolidates these refreshed artifacts:

- metric matrix:
  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;
- matrix summary:
  `output/validation_checks/track2_reference_comparison/2026-07-02-12-43-56__track2_full_directional_family_matrix_wave52b_offset_harmonic_guided_track2_refresh_2026_07_02/validation_summary.yaml`;
- per-condition metrics:
  `output/validation_checks/track2_reference_comparison/2026-07-02-12-43-56__track2_full_directional_family_matrix_wave52b_offset_harmonic_guided_track2_refresh_2026_07_02/per_condition_metrics.csv`;
- best-model collage report:
  `doc/reports/analysis/track2/best_model_collage_report/[2026-07-02]/track2_best_model_collage_report.md`;
- multi-model curve comparison report:
  `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-07-02]/track2_multi_model_curve_comparison_report.md`;
- operator launch logs:
  `output/validation_checks/track2_operator_launch_logs/2026-07-02-12-43-48_wave52b_offset_harmonic_guided_track2_refresh_2026_07_02`.

## Candidate Refresh

The refresh added `3` candidates from `wave52b_offset_harmonic_guided_registry` into the official `168`-candidate matrix.

| Surface | Candidate | Family |
| --- | --- | --- |
| global | `wave52b_offset_centered_shape_harmonic_global` | `wave52b_offset_harmonic_guided` |
| Fw | `wave52b_offset_centered_shape_harmonic_Fw` | `wave52b_offset_harmonic_guided` |
| Bw | `wave52b_offset_centered_shape_harmonic_Bw` | `wave52b_offset_harmonic_guided` |

## Refreshed Source Leaders

The table ranks the refreshed source by aggregate offline TE Curve Verification Pipeline metrics.

| Surface | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| Fw | `wave52b_offset_centered_shape_harmonic_Fw` | 0.001695 | 0.002045 | 3.391 | 8.270 |
| Bw | `wave52b_offset_centered_shape_harmonic_Bw` | 0.002266 | 0.002708 | 3.986 | 9.758 |
| global | `wave52b_offset_centered_shape_harmonic_global` | 0.002221 | 0.002629 | 4.184 | 9.818 |

## Refreshed Source Leaderboard

| Rank | Surface | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | Fw | `wave52b_offset_centered_shape_harmonic_Fw` | 0.001695 | 0.002045 | 3.391 | 8.270 |
| 2 | global | `wave52b_offset_centered_shape_harmonic_global` | 0.002221 | 0.002629 | 4.184 | 9.818 |
| 3 | Bw | `wave52b_offset_centered_shape_harmonic_Bw` | 0.002266 | 0.002708 | 3.986 | 9.758 |

## Current Direction Leaders

These leaders are read from the matrix direction breakdown after the refresh.

| Direction | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| backward | `track2g_curve_aware_full_curve_composite_global` | 0.002258 | 0.002737 | 4.040 | 10.132 |
| forward | `rcim_retuned_GBM19_Fw` | 0.001089 | 0.001299 | 2.372 | 4.912 |

## Visual Evidence

The same launcher run regenerated the visual companion reports and verified
that the refreshed source appears in the visual package.

| Source | Collage | Overlay Forward | Overlay Backward |
| --- | ---: | ---: | ---: |
| `wave52b_offset_harmonic_guided_registry` | 3 | 1 | 1 |

## Closeout Decision

`Wave 5.2B offset and harmonic guided refresh` is closed as: pending operator review; do not promote from scalar metrics alone.

Use the Wave 5.2B curve-first evidence to decide whether harmonic-guided offset and centered-shape structure should enter Wave 5.2C or Wave 6 integration.
