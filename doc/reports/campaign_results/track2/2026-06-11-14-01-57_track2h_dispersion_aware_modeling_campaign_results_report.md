# Track 2H Dispersion-Aware Modeling Campaign Results

## Overview

This report closes the approved `Track 2H` robust-loss dispersion-aware
campaign. The campaign tested whether less outlier-sensitive pointwise losses
help the curve-aware harmonic residual-offset probe handle locally dispersed
TE data before moving to quantile, probabilistic, mixture, latent-state, or
multi-head architectures.

The campaign completed all planned entries:

- `9` completed runs;
- `0` failed runs;
- `3` robust loss profiles;
- `3` required direction surfaces: `global`, `Fw`, and `Bw`.

The runner-level scalar first entry is `te_track2h_smooth_l1_robust_bw`.
This is not a deployment winner by itself. Track 2H must still pass the
official curve-first Track 2 verification refresh before promotion decisions.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10` |
| Leaderboard | `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/campaign_leaderboard.yaml` |
| Best-run pointer | `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/campaign_best_run.yaml` |
| Execution report | `output/training_campaigns/2026-06-11-11-51-10_track2h_dispersion_aware_modeling_campaign_2026_06_10/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/track2/2026-06-10-16-56-36_track2h_dispersion_aware_modeling_probe_campaign_plan_report.md` |
| Campaign package | `config/training/track2h_dispersion_aware_modeling/campaigns/2026-06-10_track2h_dispersion_aware_modeling_campaign` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `track2h_dispersion_aware_modeling_campaign_2026_06_10` |
| Completed runs | 9 |
| Failed runs | 0 |
| Model type | `curve_aware_harmonic_residual_offset_probe` |
| Loss profiles | `mae`, `smooth_l1`, `log_cosh` |
| Tested surfaces | `global`, `Fw`, `Bw` |
| Runner-level scalar first entry | `te_track2h_smooth_l1_robust_bw` |
| Program-level scalar winner changed | no |

## Directional Branch Results

| Surface | Candidate | Loss Profile | Test MAE | Test RMSE | Val MAE |
| --- | --- | --- | ---: | ---: | ---: |
| `global` | `mae_robust_global` | `mae` | 0.003406 | 0.003807 | 0.003645 |
| `Fw` | `mae_robust_fw` | `mae` | 0.003146 | 0.003527 | 0.003258 |
| `Bw` | `smooth_l1_robust_bw` | `smooth_l1` | 0.003074 | 0.003662 | 0.003372 |

These rows are the branch-level closeout result. The `Bw` row is also the
campaign scalar leader, but it does not replace the `global` or `Fw` branch.

## Robust-Loss Leaderboard

| Rank | Surface | Candidate | Loss Profile | Test MAE | Test RMSE | Val MAE |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | `Bw` | `smooth_l1_robust_bw` | `smooth_l1` | 0.003074 | 0.003662 | 0.003372 |
| 2 | `Fw` | `mae_robust_fw` | `mae` | 0.003146 | 0.003527 | 0.003258 |
| 3 | `Fw` | `smooth_l1_robust_fw` | `smooth_l1` | 0.003314 | 0.003679 | 0.003235 |
| 4 | `Fw` | `log_cosh_robust_fw` | `log_cosh` | 0.003355 | 0.003708 | 0.003280 |
| 5 | `global` | `mae_robust_global` | `mae` | 0.003406 | 0.003807 | 0.003645 |
| 6 | `global` | `smooth_l1_robust_global` | `smooth_l1` | 0.003422 | 0.003810 | 0.003641 |
| 7 | `Bw` | `mae_robust_bw` | `mae` | 0.003430 | 0.004029 | 0.003579 |
| 8 | `Bw` | `log_cosh_robust_bw` | `log_cosh` | 0.003481 | 0.004029 | 0.003774 |
| 9 | `global` | `log_cosh_robust_global` | `log_cosh` | 0.003505 | 0.003935 | 0.003645 |

## Baseline Comparison

| Surface | T2H Best | T2H MAE | T2G Ref. | Ref. MAE | Delta |
| --- | --- | ---: | --- | ---: | ---: |
| `global` | `mae_robust_global` | 0.003406 | `full_curve_composite_global` | 0.003345 | -1.82% |
| `Fw` | `mae_robust_fw` | 0.003146 | `raw_centered_shape_fw` | 0.003181 | +1.10% |
| `Bw` | `smooth_l1_robust_bw` | 0.003074 | `pointwise_control_bw` | 0.003430 | +10.38% |

Scalar training metrics show a useful but direction-dependent result. Robust
losses clearly improve the backward scalar branch relative to the Track 2G
backward reference and slightly improve the forward scalar branch. The global
branch does not improve over the Track 2G full-curve-composite reference.

## Loss Interpretation

| Loss Profile | Observed Signal | Interpretation |
| --- | --- | --- |
| `mae` | Best `global` and best `Fw` Track 2H scalar result. | Absolute-error pressure is useful where local dispersion likely distorts MSE-style training. |
| `smooth_l1` | Best `Bw` and campaign scalar leader. | Huber-like behavior is the strongest first signal for the backward dispersion/offset problem. |
| `log_cosh` | No branch winner and weakest global result. | It is stable but not competitive in this first robust-loss campaign. |

The main modeling result is not that robust losses solve Track 2. The useful
result is that robust loss selection matters, especially on the backward
surface. This supports continuing the dispersion-aware plan before freezing a
multi-head architecture.

## Registry Effects

The campaign runner refreshed family registries for all nine Track 2H
families and updated the program registry. The program-level scalar best did
not move: `te_periodic_gru_sequence_remote_Bw` remains the current scalar
program winner with test `MAE = 0.002344`.

| Registry Scope | Best Run | Test MAE |
| --- | --- | ---: |
| `Track 2H global robust` | `te_track2h_mae_robust_global` | 0.003406 |
| `Track 2H Fw robust` | `te_track2h_mae_robust_fw` | 0.003146 |
| `Track 2H Bw robust` | `te_track2h_smooth_l1_robust_bw` | 0.003074 |

## Track 2 Boundary

Official Track 2 curve-first verification was not run as part of this normal
campaign closeout. Under campaign governance, that remains a separate
operator-approved workflow after this campaign-results report and PDF are
complete.

The next Track 2 package should add all nine Track 2H candidates and report
accepted results separately for:

- `global`;
- `Fw`;
- `Bw`.

The verification must compare raw curve error, centered-shape error, offset,
amplitude, harmonic behavior, collage plots, and overlay plots against Track
2G, Track 2F-bis, Wave 2B, and the current accepted Track 2 baselines.

## Closeout Decision

Track 2H robust-loss execution is complete: all planned candidates have
successful training artifacts, no failed run remains, registries were
refreshed by the runner, and the active campaign state can be cleared.

From a modeling standpoint:

- carry `mae_robust_global` forward as the strongest Track 2H global scalar
  candidate;
- carry `mae_robust_fw` forward as the strongest Track 2H forward scalar
  candidate;
- carry `smooth_l1_robust_bw` forward as the strongest Track 2H backward
  scalar candidate;
- keep `log_cosh` as a completed negative/weak baseline, not the next default
  loss profile;
- do not promote Track 2H before official Track 2 verification.

## Recommended Follow-Up

1. Accept this closeout and clear the active campaign state.
2. Prepare a separate operator-launched Track 2 verification refresh for all
   nine Track 2H candidates.
3. If the official Track 2 refresh confirms the scalar backward improvement,
   make robust losses part of the candidate set for later multi-task /
   multi-head models.
4. Prepare the next Track 2H package in staged order: quantile/probabilistic
   regression, mixture-density heads, then latent-state or hysteresis-aware
   models.
5. Keep `Fw`, `Bw`, and `global` as parallel branch decisions.
