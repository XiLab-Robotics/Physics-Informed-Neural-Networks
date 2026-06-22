# Polished Dataset Stage 1 Smoke Campaign Results Report

## Executive Summary

The `polished_dataset_stage1_smoke_2026_06_21` campaign completed the approved
Stage 1 smoke matrix on `2026-06-22` with `8` completed runs and `0` failed
runs in the accepted execution attempt.

The scalar winner is
`te_periodic_gru_sequence_remote_global`, trained on `polished_dataset` with
the `polished_point_v1` schema:

- test MAE: `0.001279 deg`;
- test RMSE: `0.001638 deg`;
- validation MAE: `0.001274 deg`;
- trainable parameters: `157,569`.

This is a normal campaign closeout. It accepts the Stage 1 training smoke
matrix, updates the scalar registries, and records the polished-dataset
artifact state. It does not promote a new official compensation candidate
through the `TE Curve Verification Pipeline`; that curve-first verification
remains a separate operator-approved workflow.

## Campaign Scope

Stage 1 was intentionally small. Its purpose was to prove that representative
repository-owned model families can train end-to-end on the new
`polished_dataset` point schema before preparing larger retraining waves.

The campaign exercised these model branches:

- feedforward baseline;
- tabular tree benchmark;
- harmonic regression baseline;
- periodic GRU sequence model;
- residual harmonic GRU sequence model;
- curve-aware full-curve composite model;
- harmonic-prior residual model;
- latent-state hysteresis GRU offset-residual model.

All accepted runs used the polished input columns:

| Field | Role |
| --- | --- |
| `theta` | motor position measured in degrees |
| `theta_dot` | motor velocity derived from position |
| `tau_load` | applied load in Nm |
| `T` | oil temperature |
| `theta_TE` | measured transmission error target |

The campaign-level leaderboard and family registry metadata were checked after
completion. The tree run was confirmed to have trained on `polished_dataset`
from its real `metrics_summary.yaml`; a legacy registry fallback initially
reported the tree entry as `simplified_dataset`. The aggregation code and
generated registry artifacts were repaired so the tree entry now records
`polished_dataset`, `polished_point_v1`, and input dimension `4`.

## Execution Attempts

| Attempt | Start | Outcome | Closure Handling |
| --- | --- | --- | --- |
| first launch | `2026-06-22 11:55:01` | failed during feedforward best-checkpoint reload | archived as diagnostic evidence; fixed `input_size: auto` reload handling |
| second launch | `2026-06-22 12:46:43` | interrupted during feedforward after dataloader bottleneck warning | archived before relaunch; enabled automatic dataloader worker sizing |
| accepted launch | `2026-06-22 13:09:57` | completed all `8` queued runs | accepted for Stage 1 closeout |

The accepted campaign output directory is:

`output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21`

## Scalar Leaderboard

Identifiers in this table are shortened for PDF readability. The exact
`run_name`, `run_instance_id`, checkpoint, metrics snapshot, and training
report path are recorded in
`output/training_campaigns/2026-06-22-13-09-57_polished_dataset_stage1_smoke_2026_06_21/campaign_leaderboard.yaml`.

| Rank | Run | Family | Test MAE | Test RMSE | Val MAE | Params |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | `periodic_gru_global` | `periodic_gru_sequence` | 0.001279 | 0.001638 | 0.001274 | 157,569 |
| 2 | `hist_gbr_global` | `tree` | 0.001753 | 0.002892 | 0.001591 | 4 |
| 3 | `track2g_full_curve_global` | `track2g_full_curve_composite` | 0.002008 | 0.002581 | 0.001872 | 85,440 |
| 4 | `residual_harmonic_gru_sparse_global` | `residual_harmonic_gru_sparse` | 0.002112 | 0.002699 | 0.001978 | 150,676 |
| 5 | `harmonic_prior_smooth_l1_global` | `harmonic_prior_residual` | 0.002168 | 0.002763 | 0.001889 | 7,168 |
| 6 | `track2h_gru_offset_global` | `track2h_gru_offset_residual` | 0.002339 | 0.002986 | 0.002232 | 124,899 |
| 7 | `feedforward_trial` | `feedforward` | 0.002877 | 0.003835 | 0.002725 | 26,113 |
| 8 | `harmonic_order12_global` | `harmonic_regression` | 0.003839 | 0.004555 | 0.003904 | 125 |

## Run Duration Summary

| Run | Duration |
| --- | ---: |
| `te_feedforward_trial` | `00:03:27` |
| `te_hist_gbr_tabular_global` | `00:01:53` |
| `te_harmonic_order12_linear_conditioned_recovery_global` | `00:11:27` |
| `te_periodic_gru_sequence_remote_global` | `00:40:03` |
| `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `00:24:21` |
| `te_track2g_curve_aware_full_curve_composite_global` | `00:44:57` |
| `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `00:21:31` |
| `te_track2h_l_gru_offset_residual_global` | `00:23:03` |

## Registry And Artifact Effects

The accepted run updated family-level registries for:

- `feedforward`;
- `tree`;
- `harmonic_regression`;
- `periodic_gru_sequence`;
- `residual_harmonic_gru_sequence_sparse_rcim`;
- `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global`;
- `wave3_harmonic_prior_residual_smooth_l1_structured_global`;
- `track2h_latent_state_hysteresis_gru_offset_residual_global`.

The program scalar registry now points to
`te_periodic_gru_sequence_remote_global` as the current scalar best by
test MAE. This supersedes the previous scalar registry winner but does not
replace the direction-parallel curve-verified leaders until an official
`TE Curve Verification Pipeline` refresh is run and accepted.

## Acceptance Decision

Stage 1 is accepted as a polished-dataset training smoke pass because:

- every selected representative config completed in the accepted attempt;
- every accepted campaign leaderboard entry now records `polished_dataset`;
- the schema recorded by accepted metrics is `polished_point_v1`;
- all accepted models use four input features and one TE target;
- the scalar winner is finite and materially improves the previous scalar
  registry level.

The result is not a final full-program retraining conclusion. Stage 1 only
validates the dataset integration and representative training paths.

## Follow-Up

Recommended next steps:

1. prepare the next polished-dataset retraining stage with larger and
   direction-separated queues;
2. keep the `TE Curve Verification Pipeline` refresh separate from normal
   campaign closeout;
3. after the next retraining stage, run curve-first verification on selected
   polished-trained candidates with explicit `global`, `Fw`, and `Bw`
   reporting.
