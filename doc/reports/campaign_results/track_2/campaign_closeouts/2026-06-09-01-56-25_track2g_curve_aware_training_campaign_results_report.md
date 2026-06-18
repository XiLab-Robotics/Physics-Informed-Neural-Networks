# Track 2G Curve-Aware Training Campaign Results

## Overview

This report closes the approved `Track 2G` curve-aware training campaign. The
campaign goal was to test whether adding curve-aware loss terms to the
harmonic residual-offset architecture improves the scalar training surface
before returning the candidates to official Track 2 curve-first verification.

The campaign completed all planned entries:

- `12` completed runs;
- `0` failed runs;
- `4` loss profiles;
- `3` required direction surfaces: `global`, `Fw`, and `Bw`.

The runner-level scalar first entry is
`te_track2g_curve_aware_raw_centered_shape_fw`, but this is not a single
deployment winner. The closeout keeps one best candidate for each required
surface. Official Track 2 verification remains a separate operator-approved
step.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08` |
| Leaderboard | `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/campaign_leaderboard.yaml` |
| Best-run pointer | `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/campaign_best_run.yaml` |
| Execution report | `output/training_campaigns/2026-06-08-18-36-30_track2g_curve_aware_training_campaign_2026_06_08/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/track_2/2026-06-08-18-01-40_track2g_curve_aware_training_campaign_plan_report.md` |
| Campaign package | `config/training/track2g_curve_aware_training/campaigns/2026-06-08_track2g_curve_aware_training_campaign` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `track2g_curve_aware_training_campaign_2026_06_08` |
| Completed runs | 12 |
| Failed runs | 0 |
| Model type | `curve_aware_harmonic_residual_offset_probe` |
| Loss profiles | `pointwise_control`, `raw_centered_shape`, `raw_offset`, `full_curve_composite` |
| Tested surfaces | `global`, `Fw`, `Bw` |
| Runner-level scalar first entry | `te_track2g_curve_aware_raw_centered_shape_fw` |
| Program-level scalar winner changed | no |

## Directional Branch Results

| Surface | Candidate | Loss Profile | Test MAE | Test RMSE | Val MAE |
| --- | --- | --- | ---: | ---: | ---: |
| `global` | `full_curve_composite_global` | `full_curve_composite` | 0.003345 | 0.003713 | 0.003616 |
| `Fw` | `raw_centered_shape_fw` | `raw_centered_shape` | 0.003181 | 0.003571 | 0.003251 |
| `Bw` | `pointwise_control_bw` | `pointwise_control` | 0.003430 | 0.003945 | 0.003749 |

These three rows are the branch-level closeout result. The `Fw` row is also
the campaign scalar leader, but it does not replace the `global` or `Bw`
branches.

## Loss Profile Leaderboard

| Rank | Surface | Candidate | Loss Profile | Test MAE | Test RMSE | Val MAE |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | `Fw` | `raw_centered_shape_fw` | `raw_centered_shape` | 0.003181 | 0.003571 | 0.003251 |
| 2 | `Fw` | `full_curve_composite_fw` | `full_curve_composite` | 0.003260 | 0.003630 | 0.003320 |
| 3 | `Fw` | `raw_offset_fw` | `raw_offset` | 0.003279 | 0.003698 | 0.003328 |
| 4 | `global` | `full_curve_composite_global` | `full_curve_composite` | 0.003345 | 0.003713 | 0.003616 |
| 5 | `global` | `raw_centered_shape_global` | `raw_centered_shape` | 0.003350 | 0.003753 | 0.003636 |
| 6 | `Fw` | `pointwise_control_fw` | `pointwise_control` | 0.003371 | 0.003763 | 0.003291 |
| 7 | `Bw` | `pointwise_control_bw` | `pointwise_control` | 0.003430 | 0.003945 | 0.003749 |
| 8 | `global` | `raw_offset_global` | `raw_offset` | 0.003465 | 0.003829 | 0.003564 |
| 9 | `Bw` | `raw_centered_shape_bw` | `raw_centered_shape` | 0.003465 | 0.003998 | 0.003740 |
| 10 | `Bw` | `raw_offset_bw` | `raw_offset` | 0.003471 | 0.003992 | 0.003751 |
| 11 | `Bw` | `full_curve_composite_bw` | `full_curve_composite` | 0.003511 | 0.004113 | 0.003803 |
| 12 | `global` | `pointwise_control_global` | `pointwise_control` | 0.003587 | 0.004001 | 0.003607 |

## Baseline Comparison

| Surface | Track 2G Best | Track 2G MAE | Track 2F-Bis Ref. | Ref. MAE | Delta |
| --- | --- | ---: | --- | ---: | ---: |
| `global` | `full_curve_composite` | 0.003345 | `T2F-bis clean global` | 0.003528 | +5.20% |
| `Fw` | `raw_centered_shape` | 0.003181 | `T2F-bis harmonic Fw` | 0.002862 | -11.14% |
| `Bw` | `pointwise_control` | 0.003430 | `T2F-bis harmonic Bw` | 0.003336 | -2.83% |

Scalar training metrics show a mixed result. The full composite loss improves
the `global` Track 2G scalar branch versus the previous Track 2F-bis global
control. The `Fw` and `Bw` branches do not beat the strongest Track 2F-bis
direction-specific harmonic candidates on scalar `test_mae`.

This does not yet decide curve-first promotion. Track 2G was designed to test
curve-aware behavior, so the next evidence must come from official Track 2
curve playback, overlays, offset diagnostics, and mean-centered shape checks.

## Loss Interpretation

| Loss Profile | Observed Signal | Interpretation |
| --- | --- | --- |
| `pointwise_control` | Best `Bw` Track 2G scalar result. | The curve-aware add-ons are not automatically beneficial on the backward branch. |
| `raw_centered_shape` | Best `Fw` Track 2G scalar result and campaign scalar winner. | Centered-shape pressure is useful for forward scalar training, but not enough to beat Track 2F-bis harmonic `Fw`. |
| `raw_offset` | No branch winner. | Offset-only pressure did not dominate the first scalar campaign. |
| `full_curve_composite` | Best `global` Track 2G scalar result. | Combining pointwise, centered-shape, offset, amplitude, and sparse harmonic terms is most promising for the global branch. |

The main modeling result is not "Track 2G wins". The useful result is narrower:
the composite objective is promising for `global`, centered-shape is promising
for `Fw`, and `Bw` still resists the first curve-aware loss profiles.

## Registry Effects

The campaign runner refreshed family registries for all twelve Track 2G
families and updated the program registry. The program-level scalar best did
not move: `te_periodic_gru_sequence_remote_Bw` remains the current scalar
program winner with test `MAE = 0.002344`.

| Registry Scope | Best Run | Test MAE |
| --- | --- | ---: |
| `Track 2G global composite` | `full_curve_composite_global` | 0.003345 |
| `Track 2G Fw centered-shape` | `raw_centered_shape_fw` | 0.003181 |
| `Track 2G Bw pointwise` | `pointwise_control_bw` | 0.003430 |

## Track 2 Boundary

Official Track 2 curve-first verification was not run as part of this normal
campaign closeout. Under campaign governance, that remains a separate
operator-approved workflow after this campaign-results report and PDF are
complete.

The next Track 2 package should add all twelve Track 2G candidates and report
the accepted result separately for:

- `global`;
- `Fw`;
- `Bw`.

The verification must compare raw curve error, centered-shape error, offset,
amplitude, harmonic behavior, collage plots, and overlay plots against Track
2F, Track 2F-bis, Wave 2B, and the current accepted Track 2 baselines.

## Closeout Decision

Track 2G is complete from an execution standpoint: all planned candidates have
successful training artifacts, no failed run remains, registries were
refreshed by the runner, and the active campaign state can be cleared.

From a modeling standpoint:

- carry `full_curve_composite_global` forward as the strongest Track 2G global
  scalar candidate;
- carry `raw_centered_shape_fw` forward as the strongest Track 2G forward
  scalar candidate;
- carry `pointwise_control_bw` forward as the strongest Track 2G backward
  scalar candidate;
- do not promote Track 2G over Track 2F-bis or Wave 2B before official Track 2
  verification.

## Recommended Follow-Up

1. Accept this closeout and clear the active campaign state.
2. Prepare a separate operator-launched Track 2 verification refresh for all
   twelve Track 2G candidates.
3. Use the Track 2 result to decide whether Track 2G should continue as a
   loss-only branch or whether the next campaign should move to the explicit
   multi-head shape/offset architecture.
4. Keep `Fw`, `Bw`, and `global` as parallel branch decisions.
