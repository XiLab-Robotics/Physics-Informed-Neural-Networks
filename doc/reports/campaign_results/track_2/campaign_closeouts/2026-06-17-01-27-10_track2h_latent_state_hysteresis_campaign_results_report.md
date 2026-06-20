# Wave 4.4 Latent-State Hysteresis Campaign Results

## Overview

This report closes the approved `Wave 4.4` causal latent-state /
hysteresis-aware campaign; all six planned runs completed, and the
program-level scalar winner did not change.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16` |
| Leaderboard | `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16/campaign_leaderboard.yaml` |
| Best-run pointer | `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16/campaign_best_run.yaml` |
| Execution report | `output/training_campaigns/2026-06-16-18-06-11_track2h_latent_state_hysteresis_campaign_2026_06_16/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/track_2/2026-06-16-16-00-57_track2h_latent_state_hysteresis_campaign_plan_report.md` |
| Campaign package | `config/training/track2h_latent_state_hysteresis/campaigns/2026-06-16_track2h_latent_state_hysteresis_campaign` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `track2h_latent_state_hysteresis_campaign_2026_06_16` |
| Completed runs | 6 |
| Failed runs | 0 |
| Model type | `latent_state_hysteresis_probe` |
| Profiles | `gru`, `tcn` |
| Tested surfaces | `global`, `Fw`, `Bw` |
| Runner-level scalar first entry | `te_track2h_l_causal_tcn_offset_residual_global` |
| Program-level scalar winner changed | no |

## Directional Branch Results

| Surface | Candidate | Profile | Encoder | Test MAE | Test RMSE | Val MAE |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `global` | `tcn_global` | `tcn` | `C-TCN` | 0.003368 | 0.003860 | 0.003543 |
| `Fw` | `tcn_fw` | `tcn` | `C-TCN` | 0.003470 | 0.004068 | 0.003565 |
| `Bw` | `gru_bw` | `gru` | `GRU` | 0.003545 | 0.004175 | 0.003837 |

These rows are the best scalar result per branch. The global causal-TCN entry
is the campaign scalar leader, but it does not replace the forward or backward
branch decisions.

## Latent-State Leaderboard

| Rank | Surface | Candidate | Profile | Encoder | Test MAE | Test RMSE | Val MAE |
| ---: | --- | --- | --- | --- | ---: | ---: | ---: |
| 1 | `global` | `tcn_global` | `tcn` | `C-TCN` | 0.003368 | 0.003860 | 0.003543 |
| 2 | `Fw` | `tcn_fw` | `tcn` | `C-TCN` | 0.003470 | 0.004068 | 0.003565 |
| 3 | `Fw` | `gru_fw` | `gru` | `GRU` | 0.003537 | 0.004110 | 0.003468 |
| 4 | `Bw` | `gru_bw` | `gru` | `GRU` | 0.003545 | 0.004175 | 0.003837 |
| 5 | `global` | `gru_global` | `gru` | `GRU` | 0.003590 | 0.004074 | 0.003717 |
| 6 | `Bw` | `tcn_bw` | `tcn` | `C-TCN` | 0.003630 | 0.004312 | 0.003840 |

## Encoder Split

| Surface | TCN Candidate | TCN MAE | GRU Candidate | GRU MAE | Better |
| --- | --- | ---: | --- | ---: | --- |
| `global` | `tcn_global` | 0.003368 | `gru_global` | 0.003590 | `C-TCN` |
| `Fw` | `tcn_fw` | 0.003470 | `gru_fw` | 0.003537 | `C-TCN` |
| `Bw` | `tcn_bw` | 0.003630 | `gru_bw` | 0.003545 | `GRU` |

The causal-TCN profile is stronger on `global` and `Fw`; the recurrent GRU
profile is stronger only on `Bw`. This suggests that short causal-history
features help, but a generic hidden-state encoder is not enough by itself to
solve the dispersed-offset problem.

## Wave 4 series Dispersion-Aware Comparison

| Surface | Wave 4.4 | Wave 4.4 MAE | MDN | MDN MAE | Prob. | Prob. MAE | Robust | Robust MAE |
| --- | --- | ---: | --- | ---: | --- | ---: | --- | ---: |
| `global` | `tcn_g` | 0.003368 | `mdn2_g` | 0.003503 | `nll_g` | 0.003013 | `mae_g` | 0.003406 |
| `Fw` | `tcn_fw` | 0.003470 | `mdn3_fw` | 0.003235 | `nll_fw` | 0.003165 | `mae_fw` | 0.003146 |
| `Bw` | `gru_bw` | 0.003545 | `mdn2_bw` | 0.002658 | `q_bw` | 0.002927 | `sl1_bw` | 0.003074 |

The latent-state campaign improves the scalar `global` surface versus the MDN
and robust-loss `global` baselines, but it remains behind the Gaussian-NLL
probabilistic `global` candidate. It is weaker than the existing `Fw` and `Bw`
dispersion-aware leaders.

## Registry Effects

The campaign runner refreshed the six family registries and updated the
program registry. The program-level scalar best did not move:
`te_periodic_gru_sequence_remote_Bw` remains the current scalar program winner
with test `MAE = 0.002344`.

| Registry Scope | Best Run | Test MAE |
| --- | --- | ---: |
| `Wave 4.4 global TCN` | `te_track2h_l_causal_tcn_offset_residual_global` | 0.003368 |
| `Wave 4.4 Fw TCN` | `te_track2h_l_causal_tcn_offset_residual_fw` | 0.003470 |
| `Wave 4.4 Bw GRU` | `te_track2h_l_gru_offset_residual_bw` | 0.003545 |
| `Current program scalar winner` | `te_periodic_gru_sequence_remote_Bw` | 0.002344 |

The best `Wave 4.4` branch is about `43.7%` worse than the current program
scalar winner, so it is not a direct program promotion.

## TE Curve Verification Pipeline Boundary

Official `TE Curve Verification Pipeline` curve-first verification was not run as part of this
normal campaign closeout. Under campaign governance, that remains a separate
operator-approved workflow after this campaign-results report and PDF are
complete.

If launched, the next `TE Curve Verification Pipeline` refresh should add all six `Wave 4.4`
candidates and report `global`, `Fw`, and `Bw` decisions separately, comparing
raw error, centered-shape error, offset behavior, amplitude, harmonic
behavior, collage plots, and overlays against the completed `Wave 4 series`,
`Wave 5.1`, `Wave 3.3`, and accepted direction-parallel baselines.

## Closeout Decision

`Wave 4.4` execution is complete: all planned candidates produced successful
training artifacts, no failed run remains, registries were refreshed by the
runner, and the active campaign state can be cleared.

From a modeling standpoint:

- carry the causal-TCN `global` result forward as useful evidence that causal
  history helps the global scalar surface;
- do not promote `Wave 4.4` over the current dispersion-aware `Fw` or `Bw`
  leaders;
- treat GRU hidden state as branch-specific evidence, not as a generally
  superior hysteresis solution;
- keep latent-state / hysteresis-aware modeling available for later multi-head
  integration only if curve-first verification shows offset or continuity
  advantages that scalar MAE does not expose.

## Recommended Follow-Up

1. Accept this closeout and clear the active campaign state.
2. Optionally prepare a separate operator-launched `TE Curve Verification Pipeline` verification
   refresh for all six `Wave 4.4` candidates.
3. If the official `TE Curve Verification Pipeline` refresh does not show a curve-quality gain, move
   the roadmap toward `Wave 5.2` / integrated multi-head design using `Wave 4.4`
   only as diagnostic evidence.
