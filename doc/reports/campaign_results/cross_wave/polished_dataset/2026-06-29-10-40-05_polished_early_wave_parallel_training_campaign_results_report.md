# Polished Early-Wave Parallel Training Campaign Results Report

## Executive Summary

The `polished_dataset_early_wave_parallel_training_2026_06_25` campaign
completed the approved early-wave parallel retraining batch with `36`
completed runs and `0` failed runs.

The accepted campaign output directory is
`output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25`.

The scalar leaderboard winner is `te_periodic_gru_sequence_bw`, trained on
`polished_dataset` with the `polished_point_v1` schema:

- surface: `bw` / `backward_only`;
- test MAE: `0.001084 deg`;
- test RMSE: `0.001393 deg`;
- validation MAE: `0.001088 deg`;
- trainable parameters: `157,569`.

This is a normal campaign closeout. It accepts the completed model-development
training batch and synchronizes campaign status. It does not promote a new
official compensation candidate through the `TE Curve Verification Pipeline`;
that curve-first verification remains a separate operator-approved workflow.

## Campaign Scope

The campaign reused the first 36 prepared configurations from the larger
`polished_dataset_full_wave_retraining_2026_06_22` package. It covered `12`
model families across `global`, `fw`, and `bw` surfaces.

All accepted runs used the polished input columns:

| Field | Role |
| --- | --- |
| `theta` | motor position measured in degrees |
| `theta_dot` | motor velocity derived from position |
| `tau_load` | applied load in Nm |
| `T` | oil temperature |
| `theta_TE` | measured transmission error target |

Included model families:

- `feedforward`
- `gru_sequence`
- `harmonic_regression`
- `lstm_sequence`
- `periodic_gru_sequence`
- `periodic_lstm_sequence`
- `periodic_mlp`
- `periodic_mlp_harmonic`
- `periodic_temporal_convolution`
- `residual_harmonic_mlp`
- `temporal_convolution`
- `tree`

## Queue And Artifact Audit

| Check | Result |
| --- | ---: |
| Completed queue entries | `36` |
| Failed queue entries | `0` |
| Running queue entries | `0` |
| Pending queue entries | `0` |
| Leaderboard entries | `36` |
| Dataset entries recorded as `polished_dataset` | `36` |
| Schema entries recorded as `polished_point_v1` | `36` |
| Missing referenced metrics/reports/checkpoints | `0` |

The run logs contain no campaign-level failures. The repeated `Error Message:
N/A` lines in the execution report belong to completed run-detail records, not
to actual failures.

## Surface Winners

| Surface | Best Run | Family | Test MAE | Test RMSE | Val MAE | Params |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| Global | `te_periodic_lstm_sequence_global` | `periodic_lstm_sequence` | 0.001187 | 0.001505 | 0.001185 | 210,049 |
| Forward-only | `te_periodic_gru_sequence_fw` | `periodic_gru_sequence` | 0.001101 | 0.001409 | 0.001099 | 157,569 |
| Backward-only | `te_periodic_gru_sequence_bw` | `periodic_gru_sequence` | 0.001084 | 0.001393 | 0.001088 | 157,569 |

## Scalar Leaderboard Snapshot

The table below shows the first eight entries from the scalar leaderboard. The
full ordered list, with exact run names and artifact paths, is stored in
`output/training_campaigns/2026-06-25-16-01-23_polished_dataset_early_wave_parallel_training_2026_06_25/campaign_leaderboard.yaml`.

| Rank | Compact Run | Surface | Family | Test MAE | Test RMSE | Val MAE |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | `periodic_gru_bw` | `bw` | `periodic_gru` | 0.001084 | 0.001393 | 0.001088 |
| 2 | `periodic_gru_fw` | `fw` | `periodic_gru` | 0.001101 | 0.001409 | 0.001099 |
| 3 | `periodic_lstm_global` | `global` | `periodic_lstm` | 0.001187 | 0.001505 | 0.001185 |
| 4 | `periodic_gru_global` | `global` | `periodic_gru` | 0.001257 | 0.001613 | 0.001252 |
| 5 | `periodic_mlp_harmonic_global` | `global` | `periodic_mlp_harmonic` | 0.001264 | 0.001737 | 0.001196 |
| 6 | `periodic_mlp_harmonic_bw` | `bw` | `periodic_mlp_harmonic` | 0.001279 | 0.001719 | 0.001103 |
| 7 | `periodic_mlp_harmonic_fw` | `fw` | `periodic_mlp_harmonic` | 0.001326 | 0.001780 | 0.001144 |
| 8 | `periodic_lstm_bw` | `bw` | `periodic_lstm` | 0.001338 | 0.001719 | 0.001231 |

## Registry And Program Effects

The completed run updated family-level registries for the early-wave polished
families and the program scalar registry. The current scalar program winner is
`te_periodic_gru_sequence_bw` by campaign `test_mae`.

This scalar winner is useful as a retraining result, but it does not replace
the official direction-parallel curve-verified leaders until a separate
`TE Curve Verification Pipeline` refresh is run and accepted. The repository
must keep `global`, `Fw`, and `Bw` surfaces visible as separate decision
surfaces.

## Acceptance Decision

The early-wave campaign is accepted as a completed polished-dataset retraining
batch because:

- all `36` selected configs completed;
- no queue entries remain pending, running, or failed;
- every leaderboard entry records `polished_dataset`;
- every leaderboard entry records `polished_point_v1`;
- every accepted model uses four input features and one TE target;
- every referenced metric, training report, and checkpoint artifact exists.

## Closeout Notes

The active campaign state has to preserve the parallel
`polished_dataset_rcim_model_bank_reproduction_2026_06_22` provenance because
that RCIM campaign was launched on another workstation and is tracked
separately from this local early-wave batch.

The TE Program Status And Closeout Ledger was checked. It requires a content
update because the latest normal campaign closeout and scalar program winner
changed from the earlier Stage 1 smoke result to this completed early-wave
parallel training result.

## Follow-Up

Recommended next steps:

1. finish or inspect the parallel RCIM Model-Bank Reproduction campaign when
   the other workstation reports completion;
2. keep the remaining 72-run polished full-wave retraining package as the next
   model-development training stage;
3. after normal campaign closeouts are complete, prepare a separate operator-run
   `TE Curve Verification Pipeline` refresh for selected polished-trained
   candidates.
