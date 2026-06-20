# Wave 2.1 Temporal Model Entry Campaign Results

## Overview

This report closes the approved `Wave 2.1` temporal-model entry campaign. The
campaign tested whether short temporal windows improve TE prediction beyond
the closed static `Wave 1` baselines.

The campaign completed all `9` planned runs with zero launcher failures. The
campaign winner by the configured selection policy, minimum `test_mae` with
`test_rmse`, `val_mae`, and parameter count as tie breakers, is
`te_gru_sequence_remote_Fw`.

This result is a training-campaign winner. It is not yet an accepted `TE Curve Verification Pipeline`
model-verification winner, because the official curve-verification matrix and visual
reports still need to be refreshed with the new temporal candidates.

## Campaign Artifacts

| Artifact | Path |
| --- | --- |
| Campaign output | `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |
| Campaign leaderboard | `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/campaign_leaderboard.yaml` |
| Best-run pointer | `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/campaign_best_run.yaml` |
| Execution report | `output/training_campaigns/2026-05-24-11-20-37_wave2_temporal_model_entry_campaign_2026_05_24_11_01_15/campaign_execution_report.md` |
| Planning report | `doc/reports/campaign_plans/wave_2/2026-05-21-16-46-08_wave2_temporal_model_entry_campaign_plan_report.md` |
| Technical document | `doc/technical/2026-05/2026-05-21/2026-05-21-16-46-08_wave2_temporal_model_entry_plan.md` |

## Execution Summary

| Field | Value |
| --- | --- |
| Campaign name | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |
| Started at | `2026-05-24T11:20:37` |
| Finished at | `2026-05-24T12:27:31` |
| Completed runs | 9 |
| Failed runs | 0 |
| Tested model types | `temporal_convolution`, `gru_sequence`, `lstm_sequence` |
| Tested direction scopes | `global`, `Fw`, `Bw` |
| Input contract | centered sequence windows, length `33`, stride `4` |

## Campaign Winner

| Field | Value |
| --- | --- |
| Run name | `te_gru_sequence_remote_Fw` |
| Run instance | `2026-05-24-11-54-04__te_gru_sequence_remote_fw` |
| Model family | `gru_sequence_fw` |
| Model type | `gru_sequence` |
| Direction scope | forward only |
| Trainable parameters | 151,041 |
| Validation MAE | 0.003409 |
| Validation RMSE | 0.004010 |
| Test MAE | 0.003333 |
| Test RMSE | 0.003881 |

The winning checkpoint is stored at
`output/training_runs/gru_sequence_fw/2026-05-24-11-54-04__te_gru_sequence_remote_fw/checkpoints/gru_sequence-epoch=045-val_mae=0.00340867.ckpt`.

## Leaderboard

| Rank | Run | Family | Scope | Test MAE | Test RMSE | Val MAE | Params |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | `te_gru_sequence_remote_Fw` | `gru_sequence_fw` | `Fw` | 0.003333 | 0.003881 | 0.003409 | 151,041 |
| 2 | `te_lstm_sequence_remote_Fw` | `lstm_sequence_fw` | `Fw` | 0.003370 | 0.003921 | 0.003448 | 201,345 |
| 3 | `te_lstm_sequence_remote_global` | `lstm_sequence` | `global` | 0.003482 | 0.003948 | 0.003681 | 201,345 |
| 4 | `te_lstm_sequence_remote_Bw` | `lstm_sequence_bw` | `Bw` | 0.003557 | 0.004201 | 0.003815 | 201,345 |
| 5 | `te_gru_sequence_remote_global` | `gru_sequence` | `global` | 0.003591 | 0.004110 | 0.003707 | 151,041 |
| 6 | `te_temporal_convolution_sequence_remote_Fw` | `temporal_convolution_fw` | `Fw` | 0.003611 | 0.004183 | 0.003490 | 147,009 |
| 7 | `te_gru_sequence_remote_Bw` | `gru_sequence_bw` | `Bw` | 0.003631 | 0.004297 | 0.003867 | 151,041 |
| 8 | `te_temporal_convolution_sequence_remote_Bw` | `temporal_convolution_bw` | `Bw` | 0.003739 | 0.004369 | 0.003933 | 147,009 |
| 9 | `te_temporal_convolution_sequence_remote_global` | `temporal_convolution` | `global` | 0.003754 | 0.004266 | 0.003935 | 147,009 |

## Technical Interpretation

The strongest temporal result is the forward-only `GRU` surface. It slightly
outperforms the forward-only `LSTM` candidate in scalar test MAE while using
about `25%` fewer parameters. The `GRU` result is therefore the first temporal
candidate to carry into the `TE Curve Verification Pipeline` visual refresh.

The `LSTM` family is still important: it is the best global temporal result
and the best backward temporal result. The campaign does not show a universal
dominance of one temporal family across all direction scopes.

The temporal convolution family is the smallest and simplest of the three
families, but it ranks below both recurrent families in this first campaign.
It remains useful as a lightweight local-context reference, not as the first
promotion candidate.

The campaign does not displace the existing program-level `tree_fw` winner.
The current registered program best remains
`te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` with test MAE `0.002743`.

## Registry Effects

| Registry Scope | Current Family Best | Test MAE | Interpretation |
| --- | --- | ---: | --- |
| `temporal_convolution` | `te_temporal_convolution_sequence_remote_global` | 0.003754 | New global temporal-convolution family best |
| `temporal_convolution_fw` | `te_temporal_convolution_sequence_remote_Fw` | 0.003611 | New forward temporal-convolution family best |
| `temporal_convolution_bw` | `te_temporal_convolution_sequence_remote_Bw` | 0.003739 | New backward temporal-convolution family best |
| `gru_sequence` | `te_gru_sequence_remote_global` | 0.003591 | New global GRU family best |
| `gru_sequence_fw` | `te_gru_sequence_remote_Fw` | 0.003333 | Campaign winner and strongest temporal scalar result |
| `gru_sequence_bw` | `te_gru_sequence_remote_Bw` | 0.003631 | New backward GRU family best |
| `lstm_sequence` | `te_lstm_sequence_remote_global` | 0.003482 | Best global temporal scalar result |
| `lstm_sequence_fw` | `te_lstm_sequence_remote_Fw` | 0.003370 | Second-best temporal scalar result |
| `lstm_sequence_bw` | `te_lstm_sequence_remote_Bw` | 0.003557 | Best backward temporal scalar result |

## TE Curve Verification Pipeline Boundary

`TE Curve Verification Pipeline` remains the official offline model-verification surface. The Wave 2.1
campaign provides trained candidates and scalar evidence, but it does not by
itself establish official acceptance.

The following candidates should be prioritized in the TE Curve Verification refresh:

- `te_gru_sequence_remote_Fw` as the campaign winner;
- `te_lstm_sequence_remote_global` as the best global temporal candidate;
- `te_lstm_sequence_remote_Bw` as the best backward temporal candidate;
- all remaining Wave 2.1 candidates as matrix rows if the refresh budget allows.

The official refresh must compare these candidates against the current
`tree`, paper-derived, and RCIM Model-Bank Reproduction anchors on the same direction-aware curve
reconstruction protocol.

## Closeout Decision

The campaign is complete and successful from an execution standpoint: all `9`
runs completed, the leaderboard and best-run artifacts exist, and the family
registries were refreshed.

From a modeling standpoint, Wave 2.1 should remain open for official
verification rather than immediate promotion. The `GRU` forward result is
promising, while the `LSTM` global and backward results make the recurrent
branch the useful temporal direction to inspect visually.

## Recommended Follow-Up

1. Refresh the `TE Curve Verification Pipeline` direction-aware matrix with the `9` Wave 2.1 temporal
   candidates.
2. Regenerate TE Curve Verification Pipeline best-model collages for the temporal winners.
3. Regenerate TE Curve Verification Pipeline multi-model overlays against `tree`, paper-derived, and
   RCIM Model-Bank Reproduction anchors.
4. Update the official TE curve-verification report ledger only after the refreshed matrix
   and visual PDFs have been validated.
5. Do not promote a temporal model to deployment planning until TE Curve Verification Pipeline visual
   review confirms curve-level benefit.
