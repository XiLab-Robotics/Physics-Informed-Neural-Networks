# TE Curve Verification Pipeline Official Model Verification Report

## Executive Verdict

This update accepts the completed `Wave 4.1` robust-loss dispersion-aware
campaign into the official `TE Curve Verification Pipeline` offline verification matrix.

Decision:

- `Wave 4 series` is verified as an exploratory robust-loss baseline.
- No `Wave 4 series` candidate is promoted over the current accepted `TE Curve Verification Pipeline`
  leaders.
- The project continues to maintain three parallel best surfaces: `Fw`, `Bw`,
  and `global`.
- Within `Wave 4 series`, the strongest forward candidate is
  `track2h_mae_robust_Fw`.
- Within `Wave 4 series`, the strongest backward candidate is
  `track2h_smooth_l1_robust_Bw`.
- Within `Wave 4 series`, the strongest global candidate is
  `track2h_mae_robust_global`.

## Source Package

This official report consolidates these refreshed artifacts:

- metric matrix:
  `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Directional Model Comparison.md`;
- matrix summary:
  `output/validation_checks/track2_reference_comparison/2026-06-11-15-04-04__track2_full_directional_family_matrix_track2h_robust_loss_track2_refresh_2026_06_11/validation_summary.yaml`;
- per-condition metrics:
  `output/validation_checks/track2_reference_comparison/2026-06-11-15-04-04__track2_full_directional_family_matrix_track2h_robust_loss_track2_refresh_2026_06_11/per_condition_metrics.csv`;
- validation report:
  `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/2026-06-11-15-14-38_track2_full_directional_family_matrix_track2h_robust_loss_track2_refresh_2026_06_11_report.md`;
- best-model collage report:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/best_model_collage_report/[2026-06-11]/track2_best_model_collage_report.md`;
- multi-model curve comparison report:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/multi_model_curve_comparison_report/[2026-06-11]/track2_multi_model_curve_comparison_report.md`;
- operator launch logs:
  `output/validation_checks/track2_operator_launch_logs/2026-06-11-15-04-00_track2h_robust_loss_track2_refresh_2026_06_11/`.

## Candidate Refresh

The refresh added `9` registry-backed `Wave 4 series` candidates covering robust
`MAE`, `SmoothL1`, and `LogCosh` losses across the `global`, `Fw`, and `Bw`
surfaces.

| Surface | Robust Loss | Candidate |
| --- | --- | --- |
| `global` | `MAE` | `track2h_mae_robust_global` |
| `Fw` | `MAE` | `track2h_mae_robust_Fw` |
| `Bw` | `MAE` | `track2h_mae_robust_Bw` |
| `global` | `SmoothL1` | `track2h_smooth_l1_robust_global` |
| `Fw` | `SmoothL1` | `track2h_smooth_l1_robust_Fw` |
| `Bw` | `SmoothL1` | `track2h_smooth_l1_robust_Bw` |
| `global` | `LogCosh` | `track2h_log_cosh_robust_global` |
| `Fw` | `LogCosh` | `track2h_log_cosh_robust_Fw` |
| `Bw` | `LogCosh` | `track2h_log_cosh_robust_Bw` |

The matrix source group is
`track2h_dispersion_aware_modeling_registry`. The matrix now contains `141`
candidates.

## Verification Rules

| Surface | Training or Archive Scope | Evaluation Scope |
| --- | --- | --- |
| `Fw` | forward-only training or archive | forward TE Curve Verification Pipeline curves only |
| `Bw` | backward-only training or archive | backward TE Curve Verification Pipeline curves only |
| `global` | forward and backward training together | both directions, reported by direction and combined |

The `global`, `Fw`, and `Bw` branches are carried forward in parallel. They are
not collapsed into one scalar winner.

## Current Leaders

### Overall Direction Leaders

| Direction | Current Strongest Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `forward` | `rcim_retuned_GBM19_Fw` | 0.001089 | 0.001299 | 2.372 | 4.912 |
| `backward` | `periodic_gru_sequence_Bw` | 0.002392 | 0.002639 | 5.466 | 14.820 |
| `global combined` | `periodic_gru_sequence_global` | 0.002704 | 0.002949 | 6.139 | 13.200 |

### Repository-Owned Static Baselines

| Direction | Current Strongest Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `backward` | `tree_Bw` | 0.003258 | 0.003651 | 7.051 | 14.116 |
| `global combined` | `tree_global` | 0.003144 | 0.003533 | 6.854 | 13.314 |

### Repository-Owned Neural Leaders

| Surface | Current Strongest Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| `Bw` | `periodic_gru_sequence_Bw` | 0.002392 | 0.002639 | 5.466 | 14.820 |
| `global combined` | `periodic_gru_sequence_global` | 0.002704 | 0.002949 | 6.139 | 13.200 |

## Wave 4 series Result

| Surface | Candidate | Robust Loss | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| `Bw` | `track2h_smooth_l1_robust_Bw` | `SmoothL1` | 0.003078 | 0.003403 | 6.676 | 15.410 |
| `Fw` | `track2h_mae_robust_Fw` | `MAE` | 0.003134 | 0.003382 | 6.956 | 12.470 |
| `Fw` | `track2h_smooth_l1_robust_Fw` | `SmoothL1` | 0.003300 | 0.003545 | 7.342 | 13.401 |
| `Fw` | `track2h_log_cosh_robust_Fw` | `LogCosh` | 0.003344 | 0.003595 | 7.427 | 12.598 |
| `global combined` | `track2h_mae_robust_global` | `MAE` | 0.003401 | 0.003715 | 7.504 | 13.873 |
| `global combined` | `track2h_smooth_l1_robust_global` | `SmoothL1` | 0.003417 | 0.003719 | 7.539 | 14.332 |
| `Bw` | `track2h_mae_robust_Bw` | `MAE` | 0.003433 | 0.003750 | 7.506 | 14.575 |
| `Bw` | `track2h_log_cosh_robust_Bw` | `LogCosh` | 0.003486 | 0.003811 | 7.628 | 12.872 |
| `global combined` | `track2h_log_cosh_robust_global` | `LogCosh` | 0.003498 | 0.003819 | 7.697 | 14.405 |

Robust losses improve the previous Wave 3.3 branch on the best `Fw` and `Bw`
surfaces. The strongest `Fw` Wave 4 series candidate improves over the best
Wave 3.3 `Fw` candidate from `0.003174` to `0.003134` MAE. The strongest `Bw`
Wave 4 series candidate improves over the best Wave 3.3 `Bw` candidate from
`0.003436` to `0.003078` MAE. The best Wave 4 series `global` candidate remains
slightly behind the best Wave 3.3 global candidate.

## Visual Evidence

The `2026-06-11` collage and overlay bundles were regenerated with dedicated
Wave 4 series sections:

- `Forward Wave 4.1 Robust-Loss Models`;
- `Backward Wave 4.1 Robust-Loss Models`;
- `Global Wave 4.1 Robust-Loss Models` in the collage report;
- `Forward Reference Tree And Wave 4 series Overlay`;
- `Backward Reference Tree And Wave 4 series Overlay`.

The visual package supports the matrix decision: robust losses are useful
controls for dispersion-aware training, especially in the backward direction,
but they do not yet replace the strongest periodic temporal branch.

## Campaign Update Ledger

| Date | Campaign or Update | Candidate Scope | Matrix Status | Visual Status | Decision |
| --- | --- | --- | --- | --- | --- |
| 2026-06-11 | `Wave 4.1` robust-loss dispersion-aware refresh | `9` robust `global`, `Fw`, and `Bw` candidates | included in the `141`-candidate matrix | dated collage and overlay bundles regenerated with Wave 4 series sections | verified exploratory baseline; not promoted |
| 2026-06-10 | `Wave 3.3` curve-aware training refresh | `12` pointwise-control, centered-shape, offset, and full-composite `global`, `Fw`, and `Bw` candidates | included in the `132`-candidate matrix | dated collage and overlay bundles regenerated with Wave 3.3 sections | verified exploratory baseline; not promoted |
| 2026-06-08 | `Wave 3.2` harmonic-offset probe refresh | `6` clean and harmonic `global`, `Fw`, and `Bw` candidates plus `3` rechecked Wave 3.1 candidates | included in the `120`-candidate matrix | dated collage and overlay bundles regenerated with Wave 3.2 sections | verified exploratory baseline; not promoted |
| 2026-06-04 | `Wave 3.1` offset-aware probe refresh | `3` `global`, `Fw`, and `Bw` sequential residual offset candidates | included in the `114`-candidate matrix | dated collage and overlay bundles regenerated | verified exploratory baseline; not promoted |
| 2026-05-28 | `Wave 2.3` residual harmonic temporal hybrid refresh | `18` `global`, `Fw`, and `Bw` residual harmonic GRU/LSTM candidates | included in the `111`-candidate matrix | collage and overlay reports refreshed with `Wave 2.3` sections | verified exploratory baseline; not promoted over `Wave 2.2` or accepted TE Curve Verification Pipeline baselines |
| 2026-05-26 | `Wave 2.2` harmonic temporal hybrid refresh | periodic temporal convolution, GRU, and LSTM `global`, `Fw`, and `Bw` candidates | included | collage and overlay reports refreshed | strongest repository-owned neural branch |

## Closeout Decision

`Wave 4 series` does not change the accepted `TE Curve Verification Pipeline` baseline. The current
direction-parallel decision remains:

- `Fw`: `rcim_retuned_GBM19_Fw` remains the strongest overall forward
  candidate; `track2h_mae_robust_Fw` is the strongest Wave 4 series forward
  candidate and is slightly better than the best Wave 3.3 forward candidate.
- `Bw`: `periodic_gru_sequence_Bw` remains the strongest practical
  repository-owned backward candidate; `track2h_smooth_l1_robust_Bw` is the
  strongest Wave 4 series candidate and improves over the static `tree_Bw` baseline
  in curve-verification MAE.
- `global`: `periodic_gru_sequence_global` remains the strongest
  repository-owned bidirectional neural candidate; within Wave 4 series, the
  `MAE` robust global candidate is the strongest but remains behind the
  current Wave 3.3 global leader and the accepted periodic temporal global
  branch.

The next modeling step should keep robust losses as a validated ingredient,
but not treat them as sufficient. The evidence supports preparing the next
dispersion-aware package around quantile or probabilistic regression, followed
by mixture-density heads and latent-state or hysteresis-aware variants before
the integrated multi-task / multi-head model branch.
