# Wave 4.3 Mixture Density Heads Campaign Results

## Overview

This report closes the approved `Wave 4.3` dispersion-aware campaign:
two- and three-component mixture-density heads for locally dispersed TE
curves.

The campaign completed all planned entries:

- `6` completed runs;
- `0` failed runs;
- `2` mixture profiles;
- `3` required direction surfaces: `global`, `Fw`, and `Bw`.

The runner-level scalar first entry is `te_track2h_mdn_k2_bw`. The
program-level scalar winner did not change: `te_periodic_gru_sequence_remote_Bw`
remains the best registry entry.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-06-13-11-11-47_track2h_mixture_density_heads_campaign_2026_06_13` |
| Leaderboard | `output/training_campaigns/2026-06-13-11-11-47_track2h_mixture_density_heads_campaign_2026_06_13/campaign_leaderboard.yaml` |
| Best-run pointer | `output/training_campaigns/2026-06-13-11-11-47_track2h_mixture_density_heads_campaign_2026_06_13/campaign_best_run.yaml` |
| Execution report | `output/training_campaigns/2026-06-13-11-11-47_track2h_mixture_density_heads_campaign_2026_06_13/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/track_2/2026-06-13-10-40-25_track2h_mixture_density_heads_campaign_plan_report.md` |
| Campaign package | `config/training/track2h_mixture_density_heads/campaigns/2026-06-13_track2h_mixture_density_heads_campaign` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `track2h_mixture_density_heads_campaign_2026_06_13` |
| Completed runs | 6 |
| Failed runs | 0 |
| Model type | `curve_aware_harmonic_residual_offset_probe` |
| Profiles | `mdn_k2`, `mdn_k3` |
| Tested surfaces | `global`, `Fw`, `Bw` |
| Runner-level scalar first entry | `te_track2h_mdn_k2_bw` |
| Program-level scalar winner changed | no |

## Directional Branch Results

| Surface | Candidate | Profile | Curve | Test MAE | Test RMSE | Val MAE |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `global` | `mdn_k2_global` | `mdn_k2` | mixture expectation | 0.003503 | 0.003938 | 0.003654 |
| `Fw` | `mdn_k3_fw` | `mdn_k3` | mixture expectation | 0.003235 | 0.003613 | 0.003253 |
| `Bw` | `mdn_k2_bw` | `mdn_k2` | mixture expectation | 0.002658 | 0.003198 | 0.002914 |

These rows are the branch-level closeout result. The `Bw` `mdn_k2` row is
also the campaign scalar leader, but it does not replace the `global` or `Fw`
branch.

## Mixture Density Leaderboard

| Rank | Surface | Candidate | Profile | Test MAE | Test RMSE | Val MAE |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | `Bw` | `mdn_k2_bw` | `mdn_k2` | 0.002658 | 0.003198 | 0.002914 |
| 2 | `Bw` | `mdn_k3_bw` | `mdn_k3` | 0.002721 | 0.003250 | 0.002775 |
| 3 | `Fw` | `mdn_k3_fw` | `mdn_k3` | 0.003235 | 0.003613 | 0.003253 |
| 4 | `Fw` | `mdn_k2_fw` | `mdn_k2` | 0.003339 | 0.003721 | 0.003285 |
| 5 | `global` | `mdn_k2_global` | `mdn_k2` | 0.003503 | 0.003938 | 0.003654 |
| 6 | `global` | `mdn_k3_global` | `mdn_k3` | 0.003564 | 0.003986 | 0.003617 |

## Mixture Diagnostics Snapshot

| Surface | Candidate | Entropy | Eff. Comp. | Mean Sigma | Separation |
| --- | --- | ---: | ---: | ---: | ---: |
| `Bw` | `mdn_k2_bw` | 0.032 | 1.040 | 0.005300 | 0.012931 |
| `Bw` | `mdn_k3_bw` | 0.033 | 1.041 | 0.012381 | 0.036078 |
| `Fw` | `mdn_k3_fw` | 0.019 | 1.019 | 0.030782 | 0.048651 |
| `Fw` | `mdn_k2_fw` | 0.025 | 1.026 | 0.140972 | 0.039158 |
| `global` | `mdn_k2_global` | 0.016 | 1.016 | 0.135948 | 0.059065 |
| `global` | `mdn_k3_global` | 0.012 | 1.013 | 0.080886 | 0.107899 |

The mixture heads mostly collapsed toward one effective component. The scalar
`Bw` gain is therefore useful, but it should be interpreted as useful MDN
training pressure and expectation playback rather than confirmed learned
multimodality.

## Wave 4 series Dispersion-Aware Comparison

| Surface | MDN | MDN MAE | Prob. | Prob. MAE | Robust | Robust MAE |
| --- | --- | ---: | --- | ---: | --- | ---: |
| `global` | `mdn_k2_global` | 0.003503 | `gaussian_nll_global` | 0.003013 | `mae_robust_global` | 0.003406 |
| `Fw` | `mdn_k3_fw` | 0.003235 | `gaussian_nll_fw` | 0.003165 | `mae_robust_fw` | 0.003146 |
| `Bw` | `mdn_k2_bw` | 0.002658 | `quantile_p10_p50_p90_bw` | 0.002927 | `smooth_l1_robust_bw` | 0.003074 |

The MDN package is direction-selective. It improves the scalar `Bw` surface by
`9.19%` versus the previous best probabilistic `Bw` result and by about
`13.5%` versus the robust-loss `Bw` result. It does not improve the current
`global` or `Fw` dispersion-aware scalar leaders.

## Registry Effects

The campaign runner refreshed family registries for all six MDN families and
updated the program registry. The program-level scalar best did not move:
`te_periodic_gru_sequence_remote_Bw` remains the current scalar program winner
with test `MAE = 0.002344`.

| Registry Scope | Best Run | Test MAE |
| --- | --- | ---: |
| `Wave 4.3 global MDN` | `te_track2h_mdn_k2_global` | 0.003503 |
| `Wave 4.3 Fw MDN` | `te_track2h_mdn_k3_fw` | 0.003235 |
| `Wave 4.3 Bw MDN` | `te_track2h_mdn_k2_bw` | 0.002658 |
| `Current program scalar winner` | `te_periodic_gru_sequence_remote_Bw` | 0.002344 |

The best MDN branch remains about `13.41%` worse than the current program
scalar winner, so it is not a direct program promotion.

## TE Curve Verification Pipeline Boundary

Official TE curve-first verification was not run as part of this normal
campaign closeout. Under campaign governance, that remains a separate
operator-approved workflow after this campaign-results report and PDF are
complete.

The next TE Curve Verification Pipeline package should add all six mixture-density candidates and
report accepted results separately for:

- `global`;
- `Fw`;
- `Bw`.

The verification must compare raw curve error, centered-shape error, offset,
amplitude, harmonic behavior, collage plots, and overlay plots against Track
2G, Wave 4.1 robust-loss, Wave 4.2 quantile/probabilistic, Wave 3.2, Wave
2B, and the current accepted TE Curve Verification Pipeline baselines.

## Closeout Decision

Wave 4.3 mixture-density execution is complete: all planned candidates have
successful training artifacts, no failed run remains, registries were refreshed
by the runner, and the active campaign state can be cleared.

From a modeling standpoint:

- carry `mdn_k2_bw` forward as the strongest MDN scalar candidate and the
  strongest Wave 4 series scalar `Bw` candidate so far;
- do not carry MDN as the `global` or `Fw` default, because probabilistic and
  robust-loss candidates remain stronger there;
- treat the mixture-collapse diagnostics as a warning that this branch has not
  yet proven true multi-modal TE behavior;
- keep MDN alive until official TE curve verification decides whether the
  scalar `Bw` gain translates into curve-quality gain;
- do not promote Wave 4.3 MDN candidates before official TE curve verification.

## Recommended Follow-Up

1. Accept this closeout and clear the active campaign state.
2. Prepare a separate operator-launched TE curve verification refresh for all
   six MDN candidates.
3. If the official TE Curve Verification refresh confirms the `Bw` gain, keep `mdn_k2_bw`
   available for later multi-head integration.
4. If the official TE Curve Verification refresh shows mixture collapse also at curve level,
   prioritize latent-state / hysteresis-aware models or the `Wave 5.1` hybrid
   structured campaign before broadening MDN variants.
5. Keep `Fw`, `Bw`, and `global` as parallel branch decisions.
