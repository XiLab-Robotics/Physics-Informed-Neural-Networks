# Track 2F Offset-Aware Probe Campaign Results

## Overview

This report closes the approved `Track 2F` offset-aware probe campaign. The
executed package trained the first learned `sequential_residual_offset_probe`
candidate across the three required direction surfaces: `global`, `Fw`, and
`Bw`.

The campaign completed all 3 planned runs with zero
training failures. A terminal-level `conda run` message appeared after the
runner printed the completed-campaign summary, but the generated campaign
artifacts show `0` failed runs, per-run process return code `0`, and no
traceback in the run logs.

The scalar leaderboard ranks `Fw` first by `test_mae`, but that ranking is only
a diagnostic ordering. `Track 2F` keeps three parallel best branches for future
verification and deployment analysis: one `global`, one `Fw`, and one `Bw`
candidate.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-06-04-11-36-09_track2f_offset_aware_probe_campaign_2026_06_03` |
| Campaign leaderboard | `output/training_campaigns/2026-06-04-11-36-09_track2f_offset_aware_probe_campaign_2026_06_03/campaign_leaderboard.yaml` |
| Branch scalar pointer | `output/training_campaigns/2026-06-04-11-36-09_track2f_offset_aware_probe_campaign_2026_06_03/campaign_best_run.yaml` |
| Execution report | `output/training_campaigns/2026-06-04-11-36-09_track2f_offset_aware_probe_campaign_2026_06_03/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/track_2/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign_plan_report.md` |
| Campaign technical document | `doc/technical/2026-06/2026-06-03/2026-06-03-17-25-37_track2f_offset_aware_probe_campaign.md` |
| Model technical document | `doc/technical/2026-06/2026-06-03/2026-06-03-18-18-20_track2f_sequential_residual_offset_probe.md` |
| Closeout technical document | `doc/technical/2026-06/2026-06-04/2026-06-04-12-28-46_track2f_campaign_closeout.md` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `track2f_offset_aware_probe_campaign_2026_06_03` |
| Started at | `2026-06-04T11:36:09` |
| Finished at | `2026-06-04T12:04:47` |
| Completed runs | 3 |
| Failed runs | 0 |
| Tested model type | `sequential_residual_offset_probe` |
| Tested direction scopes | `global`, `Fw`, `Bw` |
| Runner-level scalar first entry | `te_sequential_residual_offset_probe_remote_fw` |

## Directional Branch Results

| Surface | Role | Run | Family | Test MAE | Test RMSE | Val MAE | Params |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| global | bidirectional | `te_sequential_residual_offset_probe_remote_global` | `sequential_residual_offset_probe` | 0.003537 | 0.004005 | 0.003783 | 92,802 |
| Fw | forward only | `te_sequential_residual_offset_probe_remote_fw` | `sequential_residual_offset_probe_fw` | 0.003385 | 0.003931 | 0.003380 | 92,802 |
| Bw | backward only | `te_sequential_residual_offset_probe_remote_bw` | `sequential_residual_offset_probe_bw` | 0.003638 | 0.004280 | 0.003840 | 92,802 |

These three rows are the closeout result. The `Fw` row is the scalar first
entry in this small campaign, but it does not replace the required `global` or
`Bw` branch candidates.

## Execution Details

| Surface | Run | Status | Duration | Return Code |
| --- | --- | --- | ---: | ---: |
| global | `te_sequential_residual_offset_probe_remote_global` | `completed` | 9m 22s | 0 |
| Fw | `te_sequential_residual_offset_probe_remote_fw` | `completed` | 12m 09s | 0 |
| Bw | `te_sequential_residual_offset_probe_remote_bw` | `completed` | 7m 07s | 0 |

## Scalar Leaderboard

| Rank | Surface | Run | Family | Test MAE | Test RMSE | Val MAE | Params |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | Fw | `te_sequential_residual_offset_probe_remote_fw` | `sequential_residual_offset_probe_fw` | 0.003385 | 0.003931 | 0.003380 | 92,802 |
| 2 | global | `te_sequential_residual_offset_probe_remote_global` | `sequential_residual_offset_probe` | 0.003537 | 0.004005 | 0.003783 | 92,802 |
| 3 | Bw | `te_sequential_residual_offset_probe_remote_bw` | `sequential_residual_offset_probe_bw` | 0.003638 | 0.004280 | 0.003840 | 92,802 |

## Technical Interpretation

The sequential residual-offset probe is execution-valid and provides the first
learned branch that directly targets the mean-offset failure mode found by the
`Track 2` mean-centered diagnostic, `Track 2D`, and `Track 2E`.

The scalar test metrics do not beat the current program-level scalar training
winner, `te_periodic_gru_sequence_remote_Bw`, which remains at test `MAE`
`0.002344`. This is expected for a narrow offset-aware probe: the campaign was
designed to test whether the offset branch is feasible, not to promote a new
global scalar winner from pointwise training alone.

Track 2F is also a clean non-harmonic baseline. The
`sequential_residual_offset_probe` architecture does not include explicit
harmonic forcing, periodic `sin`/`cos` feature expansion, `RCIM` harmonic
indices, or a structured harmonic branch. It should therefore not be judged as
the harmonic shape-preserving intervention. Its value is to show how far a
causal feedforward-plus-sequence residual structure can go when the future
comparison introduces new curve indices, multi-head shape/offset training, or
composite losses.

The important closeout result is therefore structural. The repository now has
three trained sequential residual-offset candidates that can be evaluated in
the official curve-first `Track 2` surface:

- `global`: bidirectional/general candidate.
- `Fw`: forward-only candidate.
- `Bw`: backward-only candidate.

## Registry Effects

| Registry Scope | Current Family Best | Test MAE | Interpretation |
| --- | --- | ---: | --- |
| `sequential_residual_offset_probe` | `te_sequential_residual_offset_probe_remote_global` | 0.003537 | New `global` Track 2F branch candidate |
| `sequential_residual_offset_probe_fw` | `te_sequential_residual_offset_probe_remote_fw` | 0.003385 | New forward-only Track 2F branch candidate |
| `sequential_residual_offset_probe_bw` | `te_sequential_residual_offset_probe_remote_bw` | 0.003638 | New backward-only Track 2F branch candidate |

The campaign runner refreshed the family registries for all three branch
families and updated the program registry. The program-level scalar best did
not move because the existing Wave 2B periodic `GRU` backward-only model is
still stronger on scalar `test_mae`.

## Track 2 Boundary

`Track 2` was not run as part of this closeout. Under campaign governance, the
official curve-first verification remains a separate operator-approved workflow
after the final campaign-results report and PDF are complete.

The next verification package should evaluate all three Track 2F branches in
parallel, not only the scalar-first `Fw` row. The goal is to measure whether
the offset-aware structure improves curve following and mean-offset behavior on
the matching `global`, `Fw`, and `Bw` surfaces.

## Closeout Decision

The campaign is complete and successful from an execution standpoint: all three
runs completed, the leaderboard and best-run artifacts exist, and the three
family registries were refreshed.

From a modeling standpoint, Track 2F is a completed feasibility branch. It is
not promoted over the current scalar program winner until a separate official
Track 2 curve-first refresh confirms a real curve-level gain.

## Recommended Follow-Up

1. Keep all three Track 2F branch candidates: `global`, `Fw`, and `Bw`.
2. Do not collapse Track 2F to the scalar-first `Fw` candidate.
3. Keep Track 2F as the clean non-harmonic baseline for future comparisons
   against harmonic-offset, new-index, multi-head, and composite-loss models.
4. Prepare the optional Track 2 curve-first verification refresh as the next
   operator-launched step.
