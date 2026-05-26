# Wave 2B Harmonic Temporal Hybrid Campaign Results

## Overview

This report closes the approved `Wave 2B` harmonic-temporal hybrid campaign.
The campaign tested explicit sparse `RCIM` harmonic features inside temporal
convolution, `GRU`, and `LSTM` sequence regressors.

The campaign completed all 9 planned runs with zero launcher failures.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |
| Campaign leaderboard | `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/campaign_leaderboard.yaml` |
| Best-run pointer | `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/campaign_best_run.yaml` |
| Execution report | `output/training_campaigns/2026-05-25-15-44-37_wave2b_harmonic_temporal_hybrid_campaign_2026_05_25/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/wave2/2026-05-25-13-34-12_wave2b_harmonic_temporal_hybrid_campaign_plan_report.md` |
| Model technical document | `doc/technical/2026-05/2026-05-25/2026-05-25-03-17-26_wave2b_harmonic_temporal_hybrids.md` |
| Closeout workflow document | `doc/technical/2026-05/2026-05-26/2026-05-26-14-01-40_campaign_closeout_and_manual_track2_gate.md` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |
| Started at | `2026-05-25T15:44:37` |
| Finished at | `2026-05-25T20:05:38` |
| Completed runs | 9 |
| Failed runs | 0 |
| Tested model types | `periodic_temporal_convolution`, `periodic_gru_sequence`, `periodic_lstm_sequence` |
| Tested direction scopes | `global`, `Fw`, `Bw` |
| Harmonic feature list | `[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]` |

## Campaign Winner

| Field | Value |
| --- | --- |
| Run name | `te_periodic_gru_sequence_remote_Bw` |
| Run instance | `2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw` |
| Model family | `periodic_gru_sequence_bw` |
| Model type | `periodic_gru_sequence` |
| Direction scope | backward only |
| Trainable parameters | 157,953 |
| Validation MAE | 0.002523 |
| Validation RMSE | 0.002965 |
| Test MAE | 0.002344 |
| Test RMSE | 0.002747 |

The winning checkpoint is stored at
`output/training_runs/periodic_gru_sequence_bw/2026-05-25-17-38-18__te_periodic_gru_sequence_remote_bw/checkpoints/periodic_gru_sequence-epoch=252-val_mae=0.00252321.ckpt`.

## Leaderboard

| Rank | Run | Family | Scope | Test MAE | Test RMSE | Val MAE | Params |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `te_periodic_gru_sequence_remote_Bw` | `periodic_gru_sequence_bw` | Bw | 0.002344 | 0.002747 | 0.002523 | 157,953 |
| 2 | `te_periodic_lstm_sequence_remote_Bw` | `periodic_lstm_sequence_bw` | Bw | 0.002556 | 0.002953 | 0.002432 | 210,561 |
| 3 | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | global | 0.002681 | 0.002971 | 0.002507 | 157,953 |
| 4 | `te_periodic_lstm_sequence_remote_global` | `periodic_lstm_sequence` | global | 0.002682 | 0.002969 | 0.002526 | 210,561 |
| 5 | `te_periodic_gru_sequence_remote_Fw` | `periodic_gru_sequence_fw` | Fw | 0.003193 | 0.003583 | 0.003227 | 157,953 |
| 6 | `te_periodic_lstm_sequence_remote_Fw` | `periodic_lstm_sequence_fw` | Fw | 0.003274 | 0.003651 | 0.003254 | 210,561 |
| 7 | `te_periodic_temporal_convolution_sequence_remote_Fw` | `periodic_temporal_convolution_fw` | Fw | 0.003337 | 0.003830 | 0.003321 | 158,529 |
| 8 | `te_periodic_temporal_convolution_sequence_remote_global` | `periodic_temporal_convolution` | global | 0.003508 | 0.003929 | 0.003634 | 158,529 |
| 9 | `te_periodic_temporal_convolution_sequence_remote_Bw` | `periodic_temporal_convolution_bw` | Bw | 0.003614 | 0.004163 | 0.003890 | 158,529 |

## Technical Interpretation

The strongest Wave 2B result is the backward-only `periodic_gru_sequence`
surface, with test MAE 0.002344. The two recurrent
hybrid families dominate the periodic temporal-convolution family in this
campaign, and the global `periodic_gru_sequence` and `periodic_lstm_sequence`
results are almost tied on scalar test error.

The campaign is a clear improvement over the first Wave 2 temporal-sequence
entry campaign on the same scalar training-registry metric surface. The best
first-wave temporal entry campaign result was `te_gru_sequence_remote_Fw` at
test MAE `0.003333`, while Wave 2B reaches `0.002344` on the backward-only
periodic `GRU` surface and `0.002681` on the global periodic `GRU` surface.

This closeout does not promote the Wave 2B winner as the official deployed or
accepted `Track 2` baseline. Campaign metrics are training-registry metrics;
the direction-aware offline curve matrix and visual overlays remain a separate
approval step. The interrupted `Track 2` attempt produced no valid result
artifact and was removed from the verification surface.

## Registry Effects

| Registry Scope | Current Family Best | Test MAE | Interpretation |
| --- | --- | --- | --- |
| `periodic_temporal_convolution` | `te_periodic_temporal_convolution_sequence_remote_global` | 0.003508 | Updated by this campaign |
| `periodic_temporal_convolution_fw` | `te_periodic_temporal_convolution_sequence_remote_Fw` | 0.003337 | Updated by this campaign |
| `periodic_temporal_convolution_bw` | `te_periodic_temporal_convolution_sequence_remote_Bw` | 0.003614 | Updated by this campaign |
| `periodic_gru_sequence` | `te_periodic_gru_sequence_remote_global` | 0.002681 | Updated by this campaign |
| `periodic_gru_sequence_fw` | `te_periodic_gru_sequence_remote_Fw` | 0.003193 | Updated by this campaign |
| `periodic_gru_sequence_bw` | `te_periodic_gru_sequence_remote_Bw` | 0.002344 | Updated by this campaign |
| `periodic_lstm_sequence` | `te_periodic_lstm_sequence_remote_global` | 0.002682 | Updated by this campaign |
| `periodic_lstm_sequence_fw` | `te_periodic_lstm_sequence_remote_Fw` | 0.003274 | Updated by this campaign |
| `periodic_lstm_sequence_bw` | `te_periodic_lstm_sequence_remote_Bw` | 0.002556 | Updated by this campaign |

The program-level training registry now points to
`te_periodic_gru_sequence_remote_Bw` as the scalar best training result. That registry
state is not the same thing as official `Track 2` acceptance.

## Track 2 Boundary

`Track 2` was not completed as part of this closeout. Under the updated
campaign governance rule, a future `Track 2` refresh must be prepared as a
separate operator-launched PowerShell workflow with local and `-Remote`
execution modes. Codex should provide the launcher and exact command, then
wait for the operator to run it and report completion.

## Closeout Decision

The campaign is complete and successful from an execution standpoint: all 9
runs completed, the leaderboard and best-run artifacts exist, and the family
registries were refreshed.

From a modeling standpoint, the periodic recurrent sequence families are worth
keeping as verified training candidates. The backward-only periodic `GRU` is
the scalar campaign winner, while the global periodic `GRU` and periodic
`LSTM` are the strongest bidirectional candidates to carry into a future
optional `Track 2` review.

## Recommended Follow-Up

1. Review and commit the normal closeout package if the report and PDF are
   accepted.
2. Prepare the separate operator-run `Track 2` launcher only after explicit
   approval.
3. Use the future `Track 2` matrix and visual reports to decide whether Wave
   2B changes any official baseline, rather than using this campaign
   leaderboard alone.
