# Track 2H Quantile Probabilistic Campaign Results

## Overview

This report closes the approved second `Track 2H` dispersion-aware campaign:
quantile and Gaussian probabilistic regression for locally dispersed TE
curves.

The campaign completed all planned entries:

- `6` completed runs;
- `0` failed runs;
- `2` probabilistic profiles;
- `3` required direction surfaces: `global`, `Fw`, and `Bw`.

The runner-level scalar first entry is
`te_track2h_quantile_p10_p50_p90_bw`. The program-level scalar winner did not
change: `te_periodic_gru_sequence_remote_Bw` remains the best registry entry.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-06-12-11-16-18_track2h_quantile_probabilistic_campaign_2026_06_12` |
| Leaderboard | `output/training_campaigns/2026-06-12-11-16-18_track2h_quantile_probabilistic_campaign_2026_06_12/campaign_leaderboard.yaml` |
| Best-run pointer | `output/training_campaigns/2026-06-12-11-16-18_track2h_quantile_probabilistic_campaign_2026_06_12/campaign_best_run.yaml` |
| Execution report | `output/training_campaigns/2026-06-12-11-16-18_track2h_quantile_probabilistic_campaign_2026_06_12/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/track_2/2026-06-12-00-01-04_track2h_quantile_probabilistic_campaign_plan_report.md` |
| Campaign package | `config/training/track2h_quantile_probabilistic_modeling/campaigns/2026-06-12_track2h_quantile_probabilistic_campaign` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `track2h_quantile_probabilistic_campaign_2026_06_12` |
| Completed runs | 6 |
| Failed runs | 0 |
| Model type | `curve_aware_harmonic_residual_offset_probe` |
| Profiles | `quantile_p10_p50_p90`, `gaussian_nll` |
| Tested surfaces | `global`, `Fw`, `Bw` |
| Runner-level scalar first entry | `te_track2h_quantile_p10_p50_p90_bw` |
| Program-level scalar winner changed | no |

## Directional Branch Results

| Surface | Candidate | Profile | Curve | Test MAE | Test RMSE | Val MAE |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `global` | `gaussian_nll_global` | `gaussian_nll` | `mu` | 0.003013 | 0.003388 | 0.003267 |
| `Fw` | `gaussian_nll_fw` | `gaussian_nll` | `mu` | 0.003165 | 0.003548 | 0.003293 |
| `Bw` | `quantile_p10_p50_p90_bw` | `quantile` | `p50` | 0.002927 | 0.003519 | 0.003436 |

These rows are the branch-level closeout result. The `Bw` quantile row is also
the campaign scalar leader, but it does not replace the `global` or `Fw`
branch.

## Probabilistic Leaderboard

| Rank | Surface | Candidate | Profile | Test MAE | Test RMSE | Val MAE |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | `Bw` | `quantile_p10_p50_p90_bw` | `quantile` | 0.002927 | 0.003519 | 0.003436 |
| 2 | `Bw` | `gaussian_nll_bw` | `gaussian_nll` | 0.002998 | 0.003608 | 0.003298 |
| 3 | `global` | `gaussian_nll_global` | `gaussian_nll` | 0.003013 | 0.003388 | 0.003267 |
| 4 | `Fw` | `gaussian_nll_fw` | `gaussian_nll` | 0.003165 | 0.003548 | 0.003293 |
| 5 | `Fw` | `quantile_p10_p50_p90_fw` | `quantile` | 0.003285 | 0.003668 | 0.003269 |
| 6 | `global` | `quantile_p10_p50_p90_global` | `quantile` | 0.003383 | 0.003764 | 0.003606 |

## Calibration Snapshot

| Surface | Candidate | Test Coverage | Test Width | Extra Diagnostic |
| --- | --- | ---: | ---: | --- |
| `global` | `quantile_p10_p50_p90_global` | 0.849 | 0.011449 | crossing 0.000 |
| `Fw` | `quantile_p10_p50_p90_fw` | 0.849 | 0.010536 | crossing 0.000 |
| `Bw` | `quantile_p10_p50_p90_bw` | 0.710 | 0.007536 | crossing 0.000 |
| `global` | `gaussian_nll_global` | 0.747 | 0.008761 | sigma 0.003418 |
| `Fw` | `gaussian_nll_fw` | 0.903 | 0.011687 | sigma 0.004560 |
| `Bw` | `gaussian_nll_bw` | 0.758 | 0.008887 | sigma 0.003467 |

The quantile heads did not exhibit quantile crossing in the serialized metrics.
Coverage is direction-dependent: `Fw` is well covered for both families, while
`Bw` achieves the best deterministic MAE with narrower and lower-coverage
intervals.

## Robust-Loss Comparison

| Surface | Probabilistic Best | Prob. MAE | Robust Best | Robust MAE | Delta |
| --- | --- | ---: | --- | ---: | ---: |
| `global` | `gaussian_nll_global` | 0.003013 | `mae_robust_global` | 0.003406 | +11.53% |
| `Fw` | `gaussian_nll_fw` | 0.003165 | `mae_robust_fw` | 0.003146 | -0.60% |
| `Bw` | `quantile_p10_p50_p90_bw` | 0.002927 | `smooth_l1_robust_bw` | 0.003074 | +4.77% |

The probabilistic package is therefore stronger than the robust-loss package
on scalar training metrics for `global` and `Bw`. It is not stronger for `Fw`,
where the robust `mae` candidate remains slightly ahead.

## Profile Interpretation

| Profile | Observed Signal | Interpretation |
| --- | --- | --- |
| `quantile_p10_p50_p90` | Best campaign scalar result on `Bw`; no quantile crossing. | Promising for backward dispersion, but needs Track 2 curve playback before promotion. |
| `gaussian_nll` | Best `global` and `Fw` probabilistic branch results. | Useful as a stable uncertainty-aware control and possibly the better global/Fw probabilistic default. |

The main modeling result is not that probabilistic heads solve Track 2. The
useful result is that explicit uncertainty-aware heads can beat the first
robust-loss package on `global` and `Bw` scalar metrics, while exposing
calibration diagnostics that robust point losses cannot provide.

## Registry Effects

The campaign runner refreshed family registries for all six probabilistic
families and updated the program registry. The program-level scalar best did
not move: `te_periodic_gru_sequence_remote_Bw` remains the current scalar
program winner with test `MAE = 0.002344`.

| Registry Scope | Best Run | Test MAE |
| --- | --- | ---: |
| `Track 2H global probabilistic` | `te_track2h_gaussian_nll_global` | 0.003013 |
| `Track 2H Fw probabilistic` | `te_track2h_gaussian_nll_fw` | 0.003165 |
| `Track 2H Bw probabilistic` | `te_track2h_quantile_p10_p50_p90_bw` | 0.002927 |

## Track 2 Boundary

Official Track 2 curve-first verification was not run as part of this normal
campaign closeout. Under campaign governance, that remains a separate
operator-approved workflow after this campaign-results report and PDF are
complete.

The next Track 2 package should add all six probabilistic candidates and report
accepted results separately for:

- `global`;
- `Fw`;
- `Bw`.

The verification must compare raw curve error, centered-shape error, offset,
amplitude, harmonic behavior, collage plots, and overlay plots against Track
2G, Track 2H robust-loss, Track 2F-bis, Wave 2B, and the current accepted Track
2 baselines.

## Closeout Decision

Track 2H quantile/probabilistic execution is complete: all planned candidates
have successful training artifacts, no failed run remains, registries were
refreshed by the runner, and the active campaign state can be cleared.

From a modeling standpoint:

- carry `gaussian_nll_global` forward as the strongest probabilistic global
  scalar candidate;
- carry `gaussian_nll_fw` forward as the strongest probabilistic forward
  scalar candidate, while noting it is slightly behind robust `mae_robust_fw`;
- carry `quantile_p10_p50_p90_bw` forward as the strongest probabilistic
  backward scalar candidate;
- keep both quantile and Gaussian heads alive until official Track 2 curve
  verification decides whether scalar gains translate into curve quality;
- do not promote Track 2H probabilistic candidates before official Track 2
  verification.

## Recommended Follow-Up

1. Accept this closeout and clear the active campaign state.
2. Prepare a separate operator-launched Track 2 verification refresh for all
   six probabilistic candidates.
3. If the official Track 2 refresh confirms the scalar `global` and `Bw`
   gains, carry probabilistic heads into later mixture-density, latent-state,
   and multi-head design.
4. Keep robust `mae_robust_fw` visible as the current stronger `Fw`
   dispersion-aware scalar candidate.
5. Keep `Fw`, `Bw`, and `global` as parallel branch decisions.
