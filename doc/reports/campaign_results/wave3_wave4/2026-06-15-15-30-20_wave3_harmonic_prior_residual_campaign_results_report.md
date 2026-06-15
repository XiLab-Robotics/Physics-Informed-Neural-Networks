# Wave 3 Harmonic-Prior Residual Campaign Results Report

## Overview

The first real `Wave 3` harmonic-prior residual campaign completed all six
runs successfully; the scalar winner is the backward pointwise-control branch,
but the campaign does not replace the current program winner.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14` |
| Execution report | `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14/campaign_execution_report.md` |
| Leaderboard | `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14/campaign_leaderboard.yaml` |
| Best run pointer | `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14/campaign_best_run.yaml` |
| Manifest | `output/training_campaigns/2026-06-15-14-01-15_wave3_harmonic_prior_residual_campaign_2026_06_14/campaign_manifest.yaml` |
| Planning report | `doc/reports/campaign_plans/wave3_wave4/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_plan_report.md` |
| Technical package | `doc/technical/2026-06/2026-06-14/2026-06-14-19-54-55_wave3_harmonic_prior_residual_campaign_package.md` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign | `wave3_harmonic_prior_residual_campaign_2026_06_14` |
| Generated at | `2026-06-15T15:30:20` |
| Completed runs | `6` |
| Failed runs | `0` |
| Profiles | `pointwise_control`, `smooth_l1_structured` |
| Surfaces | `global`, `Fw`, `Bw` |
| Best scalar run | `te_wave3_harmonic_prior_residual_pointwise_control_bw` |
| Best scalar family | `wave3_harmonic_prior_residual_pointwise_control_bw` |
| Best scalar test MAE | `0.003363` |
| Best scalar test RMSE | `0.003902` |
| Program winner changed | `no` |
| Current program winner | `te_periodic_gru_sequence_remote_Bw` |
| Track 2 status | not run during normal closeout |

## Directional Branch Results

| Surface | Candidate | Profile | Test MAE | Test RMSE | Val MAE |
| --- | --- | --- | ---: | ---: | ---: |
| `global` | `sl1_global` | `sl1` | 0.003403 | 0.003785 | 0.003633 |
| `Fw` | `pw_fw` | `pw` | 0.003382 | 0.003779 | 0.003315 |
| `Bw` | `pw_bw` | `pw` | 0.003363 | 0.003902 | 0.003634 |

## Wave 3 Leaderboard

Candidate labels are aliases for the corresponding
`te_wave3_harmonic_prior_residual_*` run names stored in the campaign
leaderboard. All candidates have `7,283` trainable parameters.

| Rank | Candidate | Surface | Test MAE | Test RMSE | Val MAE |
| ---: | --- | --- | ---: | ---: | ---: |
| 1 | `pw_bw` | `Bw` | 0.003363 | 0.003902 | 0.003634 |
| 2 | `pw_fw` | `Fw` | 0.003382 | 0.003779 | 0.003315 |
| 3 | `sl1_global` | `global` | 0.003403 | 0.003785 | 0.003633 |
| 4 | `sl1_bw` | `Bw` | 0.003431 | 0.003953 | 0.003644 |
| 5 | `pw_global` | `global` | 0.003451 | 0.003851 | 0.003611 |
| 6 | `sl1_fw` | `Fw` | 0.003527 | 0.003900 | 0.003310 |

## Profile Comparison

| Surface | Pointwise MAE | Smooth-L1 MAE | Better Profile | Relative Gap |
| --- | ---: | ---: | --- | ---: |
| `global` | 0.003451 | 0.003403 | `sl1` | 1.40% |
| `Fw` | 0.003382 | 0.003527 | `pw` | 4.12% |
| `Bw` | 0.003363 | 0.003431 | `pw` | 1.97% |

## Interpretation

`Wave 3` validates the lightweight harmonic-prior residual implementation as a
real trainable branch, with all six directional candidates completing cleanly
and registering as implemented benchmarks. The best scalar result is backward
only, while the best global result comes from the `smooth_l1_structured`
profile.

The result is useful but not yet promotable. The best `Wave 3` scalar test MAE
of `0.003363 deg` is weaker than the current program winner
`te_periodic_gru_sequence_remote_Bw` at `0.002344 deg`, and also weaker than
the best recent `Track 2H` mixture-density backward branch on scalar MAE. The
main positive signal is architectural: the candidate has only `7,283`
trainable parameters and keeps an explicit harmonic-prior residual structure.

The profile comparison does not support treating the robust `SmoothL1` branch
as a universal default. It helps on the global surface, but the plain
pointwise-control profile wins on both direction-specific surfaces. The next
decision should therefore be curve-first and direction-specific, not based on
scalar training MAE alone.

## Registry Effects

| Registry Scope | Effect |
| --- | --- |
| Family registries | Six new `wave3_harmonic_prior_residual_*` family bests are registered. |
| Program registry | No program-best promotion; `te_periodic_gru_sequence_remote_Bw` remains current. |
| Active campaign state | Cleared by this closeout after report and PDF validation. |
| Master summary | Updated to show `Wave 3` campaign closeout and separate `Track 2` boundary. |

## Track 2 Boundary

Normal campaign closeout intentionally did not execute the heavy official
`Track 2` offline verification matrix. The next optional step is a separate
`Track 2` verification refresh for the six `Wave 3` candidates, including
collage and overlay reports, so the harmonic-prior residual branch can be
compared on curve shape, offset, and direction-specific compensation behavior.

## Closeout Decision

Accept the campaign as successfully closed at the training-campaign level.
Do not promote a new program winner from scalar metrics. Plan official
`Track 2` verification as the next separate acceptance step before deciding
whether `Wave 3` should feed the later multi-head or `Wave 4` integration
roadmap.
