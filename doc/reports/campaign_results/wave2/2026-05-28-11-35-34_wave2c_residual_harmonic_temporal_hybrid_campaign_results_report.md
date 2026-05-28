# Wave 2C Residual Harmonic Temporal Hybrid Campaign Results

## Overview

This report closes the approved `Wave 2C` residual harmonic temporal hybrid
campaign. The campaign tested residual harmonic `GRU` and residual harmonic
`LSTM` sequence regressors across `global`, `Fw`, and `Bw` direction surfaces,
with three harmonic-basis tiers per surface: sparse `RCIM`, dense `0..240`,
and dense `0..360`.

The campaign completed all 18 planned runs with zero launcher failures. The
campaign winner by the configured selection policy, minimum `test_mae` with
`test_rmse`, `val_mae`, and trainable parameter count as tie breakers, is
`te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim`.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-05-27-18-55-47_wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |
| Campaign leaderboard | `output/training_campaigns/2026-05-27-18-55-47_wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27/campaign_leaderboard.yaml` |
| Best-run pointer | `output/training_campaigns/2026-05-27-18-55-47_wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27/campaign_best_run.yaml` |
| Execution report | `output/training_campaigns/2026-05-27-18-55-47_wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/wave2/2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrid_campaign_plan_report.md` |
| Model technical document | `doc/technical/2026-05/2026-05-27/2026-05-27-18-08-32_wave2c_residual_harmonic_temporal_hybrids.md` |
| Remote launcher standard | `doc/technical/2026-05/2026-05-27/2026-05-27-18-35-06_campaign_launcher_remote_execution_standard.md` |
| Closeout technical document | `doc/technical/2026-05/2026-05-28/2026-05-28-11-35-34_wave2c_campaign_closeout.md` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |
| Started at | `2026-05-27T18:55:47` |
| Finished at | `2026-05-27T22:35:20` |
| Completed runs | 18 |
| Failed runs | 0 |
| Tested model types | `residual_harmonic_gru_sequence`, `residual_harmonic_lstm_sequence` |
| Tested direction scopes | `global`, `Fw`, `Bw` |
| Harmonic basis tiers | `sparse_rcim`, `dense_240`, `dense_360` |
| Sparse harmonic list | `[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]` |

## Campaign Winner

| Field | Value |
| --- | --- |
| Run name | `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim` |
| Run instance | `2026-05-27-19-07-31__te_residual_harmonic_gru_sequence_remote_fw_sparse_rcim` |
| Model family | `residual_harmonic_gru_sequence_fw_sparse_rcim` |
| Model type | `residual_harmonic_gru_sequence` |
| Direction scope | forward only |
| Trainable parameters | 151,060 |
| Validation MAE | 0.003309 |
| Validation RMSE | 0.003828 |
| Test MAE | 0.003200 |
| Test RMSE | 0.003635 |

The winning checkpoint is stored at
`output/training_runs/residual_harmonic_gru_sequence_fw_sparse_rcim/2026-05-27-19-07-31__te_residual_harmonic_gru_sequence_remote_fw_sparse_rcim/checkpoints/residual_harmonic_gru_sequence-epoch=015-val_mae=0.00330934.ckpt`.

## Leaderboard

| Rank | Run | Family | Scope | Test MAE | Test RMSE | Val MAE | Params |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_gru_sequence_fw_sparse_rcim` | Fw | 0.003200 | 0.003635 | 0.003309 | 151,060 |
| 2 | `te_residual_harmonic_gru_sequence_remote_Fw_dense240` | `residual_harmonic_gru_sequence_fw_dense240` | Fw | 0.003219 | 0.003653 | 0.003270 | 151,522 |
| 3 | `te_residual_harmonic_lstm_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_lstm_sequence_fw_sparse_rcim` | Fw | 0.003234 | 0.003679 | 0.003344 | 201,364 |
| 4 | `te_residual_harmonic_gru_sequence_remote_Fw_dense360` | `residual_harmonic_gru_sequence_fw_dense360` | Fw | 0.003241 | 0.003677 | 0.003265 | 151,762 |
| 5 | `te_residual_harmonic_lstm_sequence_remote_Fw_dense240` | `residual_harmonic_lstm_sequence_fw_dense240` | Fw | 0.003262 | 0.003706 | 0.003307 | 201,826 |
| 6 | `te_residual_harmonic_lstm_sequence_remote_Fw_dense360` | `residual_harmonic_lstm_sequence_fw_dense360` | Fw | 0.003351 | 0.003774 | 0.003302 | 202,066 |
| 7 | `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim` | `residual_harmonic_lstm_sequence_sparse_rcim` | global | 0.003368 | 0.003808 | 0.003632 | 201,364 |
| 8 | `te_residual_harmonic_lstm_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_lstm_sequence_bw_sparse_rcim` | Bw | 0.003440 | 0.004030 | 0.003764 | 201,364 |
| 9 | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence_sparse_rcim` | global | 0.003440 | 0.003848 | 0.003607 | 151,060 |
| 10 | `te_residual_harmonic_gru_sequence_remote_Bw_dense360` | `residual_harmonic_gru_sequence_bw_dense360` | Bw | 0.003468 | 0.004050 | 0.003773 | 151,762 |
| 11 | `te_residual_harmonic_lstm_sequence_remote_global_dense240` | `residual_harmonic_lstm_sequence_dense240` | global | 0.003473 | 0.003925 | 0.003624 | 201,826 |
| 12 | `te_residual_harmonic_lstm_sequence_remote_global_dense360` | `residual_harmonic_lstm_sequence_dense360` | global | 0.003477 | 0.003940 | 0.003648 | 202,066 |
| 13 | `te_residual_harmonic_gru_sequence_remote_Bw_dense240` | `residual_harmonic_gru_sequence_bw_dense240` | Bw | 0.003492 | 0.004074 | 0.003585 | 151,522 |
| 14 | `te_residual_harmonic_gru_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_gru_sequence_bw_sparse_rcim` | Bw | 0.003502 | 0.004061 | 0.003833 | 151,060 |
| 15 | `te_residual_harmonic_gru_sequence_remote_global_dense240` | `residual_harmonic_gru_sequence_dense240` | global | 0.003511 | 0.003983 | 0.003600 | 151,522 |
| 16 | `te_residual_harmonic_gru_sequence_remote_global_dense360` | `residual_harmonic_gru_sequence_dense360` | global | 0.003535 | 0.003999 | 0.003628 | 151,762 |
| 17 | `te_residual_harmonic_lstm_sequence_remote_Bw_dense360` | `residual_harmonic_lstm_sequence_bw_dense360` | Bw | 0.003556 | 0.004125 | 0.003729 | 202,066 |
| 18 | `te_residual_harmonic_lstm_sequence_remote_Bw_dense240` | `residual_harmonic_lstm_sequence_bw_dense240` | Bw | 0.003605 | 0.004129 | 0.003742 | 201,826 |

## Technical Interpretation

The strongest Wave 2C scalar training result is the forward-only sparse `RCIM`
residual harmonic `GRU`, with test MAE 0.003200.
The dense harmonic branches did not improve the campaign winner: the second
ranked model is the forward-only dense `0..240` residual harmonic `GRU`, and
the third ranked model is the forward-only sparse `RCIM` residual harmonic
`LSTM`.

This result is execution-valid and useful as a model-family probe, but it does
not exceed the current Wave 2B scalar training winner. The program-level scalar best remains `te_periodic_gru_sequence_remote_Bw` with test MAE 0.002344.
That means Wave 2C should be retained as a completed comparison branch, while
Wave 2B remains the stronger scalar training baseline until a future campaign
or official `Track 2` review changes that conclusion.

The campaign also shows that adding a recurrent residual branch over an
explicit harmonic base is not automatically superior to feeding the harmonic
prior directly into the recurrent temporal model. That is a useful negative
result: the residual decomposition remains inspectable, but the sparse
periodic recurrent Wave 2B formulation is still the better scalar candidate.

## Registry Effects

| Registry Scope | Current Family Best | Test MAE | Interpretation |
| --- | --- | --- | --- |
| `residual_harmonic_gru_sequence_sparse_rcim` | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | 0.003440 | Updated by this campaign |
| `residual_harmonic_gru_sequence_fw_sparse_rcim` | `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim` | 0.003200 | Updated by this campaign |
| `residual_harmonic_gru_sequence_bw_sparse_rcim` | `te_residual_harmonic_gru_sequence_remote_Bw_sparse_rcim` | 0.003502 | Updated by this campaign |
| `residual_harmonic_gru_sequence_dense240` | `te_residual_harmonic_gru_sequence_remote_global_dense240` | 0.003511 | Updated by this campaign |
| `residual_harmonic_gru_sequence_fw_dense240` | `te_residual_harmonic_gru_sequence_remote_Fw_dense240` | 0.003219 | Updated by this campaign |
| `residual_harmonic_gru_sequence_bw_dense240` | `te_residual_harmonic_gru_sequence_remote_Bw_dense240` | 0.003492 | Updated by this campaign |
| `residual_harmonic_gru_sequence_dense360` | `te_residual_harmonic_gru_sequence_remote_global_dense360` | 0.003535 | Updated by this campaign |
| `residual_harmonic_gru_sequence_fw_dense360` | `te_residual_harmonic_gru_sequence_remote_Fw_dense360` | 0.003241 | Updated by this campaign |
| `residual_harmonic_gru_sequence_bw_dense360` | `te_residual_harmonic_gru_sequence_remote_Bw_dense360` | 0.003468 | Updated by this campaign |
| `residual_harmonic_lstm_sequence_sparse_rcim` | `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim` | 0.003368 | Updated by this campaign |
| `residual_harmonic_lstm_sequence_fw_sparse_rcim` | `te_residual_harmonic_lstm_sequence_remote_Fw_sparse_rcim` | 0.003234 | Updated by this campaign |
| `residual_harmonic_lstm_sequence_bw_sparse_rcim` | `te_residual_harmonic_lstm_sequence_remote_Bw_sparse_rcim` | 0.003440 | Updated by this campaign |
| `residual_harmonic_lstm_sequence_dense240` | `te_residual_harmonic_lstm_sequence_remote_global_dense240` | 0.003473 | Updated by this campaign |
| `residual_harmonic_lstm_sequence_fw_dense240` | `te_residual_harmonic_lstm_sequence_remote_Fw_dense240` | 0.003262 | Updated by this campaign |
| `residual_harmonic_lstm_sequence_bw_dense240` | `te_residual_harmonic_lstm_sequence_remote_Bw_dense240` | 0.003605 | Updated by this campaign |
| `residual_harmonic_lstm_sequence_dense360` | `te_residual_harmonic_lstm_sequence_remote_global_dense360` | 0.003477 | Updated by this campaign |
| `residual_harmonic_lstm_sequence_fw_dense360` | `te_residual_harmonic_lstm_sequence_remote_Fw_dense360` | 0.003351 | Updated by this campaign |
| `residual_harmonic_lstm_sequence_bw_dense360` | `te_residual_harmonic_lstm_sequence_remote_Bw_dense360` | 0.003556 | Updated by this campaign |

The family registries for the new Wave 2C model surfaces were created or
refreshed by this campaign. The program-level training registry did not move
to Wave 2C because the Wave 2B periodic `GRU` backward-only model still has the
lower scalar test MAE.

## Track 2 Boundary

`Track 2` was not run as part of this closeout. Under the campaign governance
rule, optional `Track 2` verification remains a separate operator-approved
workflow with a repository-owned launcher that can run locally or with
`-Remote`.

Because Wave 2C does not beat the existing Wave 2B scalar best, a full `Track
2` refresh is not mandatory for accepting this closeout. If reviewed later,
the forward-only sparse `RCIM` residual harmonic `GRU` is the only Wave 2C
candidate that should be promoted into the optional verification queue first.

## Closeout Decision

The campaign is complete and successful from an execution standpoint: all 18
runs completed, the leaderboard and best-run artifacts exist, and the family
registries were refreshed.

From a modeling standpoint, Wave 2C is a completed comparison branch rather
than a new best branch. The residual harmonic temporal structure remains
available for future analysis, but the current project best should stay on the
Wave 2B periodic recurrent family until official verification says otherwise.

## Recommended Follow-Up

1. Keep the Wave 2C artifacts as a completed negative/neutral comparison
   branch.
2. Do not replace the current Wave 2B scalar best with the Wave 2C winner.
3. Run optional `Track 2` only if visual curve behavior is worth inspecting
   despite the weaker scalar campaign result.
