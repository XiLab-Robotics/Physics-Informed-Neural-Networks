# Polished Full-Wave Retraining Campaign Results Report

## Executive Summary

The `polished_dataset_full_wave_retraining_2026_06_22` campaign completed the
approved full non-paper model-development retraining batch with `108`
completed runs and `0` failed runs.

The accepted campaign output directory is
`output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22`.

The full-wave campaign scalar leaderboard winner is
`te_periodic_gru_sequence_fw`, trained on `polished_dataset` with the
`polished_point_v1` schema:

- surface: `fw` / `forward_only`;
- test MAE: `0.001121 deg`;
- test RMSE: `0.001444 deg`;
- validation MAE: `0.001084 deg`;
- trainable parameters: `157,569`.

The program scalar registry still keeps the earlier polished early-wave
`te_periodic_gru_sequence_bw` run as the current scalar program winner because
its test MAE is lower at `0.001084 deg`.

This is a normal campaign closeout. It accepts the completed model-development
training batch and synchronizes campaign status. It does not promote a new
official compensation candidate through the `TE Curve Verification Pipeline`;
that curve-first verification remains a separate operator-approved workflow.

## Campaign Scope

The campaign used the prepared
`polished_dataset_full_wave_retraining_2026_06_22` package. It covered `36`
model families across `global`, `fw`, and `bw` surfaces for `108` total
training configurations.

All accepted runs used the polished input columns:

| Field | Role |
| --- | --- |
| `theta` | motor position measured in degrees |
| `theta_dot` | motor velocity derived from position |
| `tau_load` | applied load in Nm |
| `T` | oil temperature |
| `theta_TE` | measured transmission error target |

Included model families:

| Family A | Family B | Family C |
| --- | --- | --- |
| `feedforward` | `gru_sequence` | `harmonic_regression` |
| `lstm_sequence` | `periodic_gru_sequence` | `periodic_lstm_sequence` |
| `periodic_mlp` | `periodic_mlp_harmonic` | `periodic_temporal_convolution` |
| `residual_harmonic_gru_sequence_dense240` | `residual_harmonic_gru_sequence_dense360` | `residual_harmonic_gru_sequence_sparse_rcim` |
| `residual_harmonic_lstm_sequence_dense240` | `residual_harmonic_lstm_sequence_dense360` | `residual_harmonic_lstm_sequence_sparse_rcim` |
| `residual_harmonic_mlp` | `temporal_convolution` | `tree` |
| `wave3_1_sequential_residual_offset_probe` | `wave3_2_clean_sequential_residual_offset` | `wave3_2_harmonic_residual_offset` |
| `wave3_3_curve_aware_pointwise_control` | `wave3_3_full_curve_composite` | `wave3_3_raw_centered_shape_curve_aware` |
| `wave3_3_raw_offset_curve_aware` | `wave4_1_log_cosh_robust_loss` | `wave4_1_mae_robust_loss` |
| `wave4_1_smooth_l1_robust_loss` | `wave4_2_gaussian_nll` | `wave4_2_quantile_p10_p50_p90` |
| `wave4_3_mixture_density_k2` | `wave4_3_mixture_density_k3` | `wave4_4_causal_tcn_latent_offset_residual` |
| `wave4_4_gru_latent_offset_residual` | `wave5_1_harmonic_prior_pointwise_control` | `wave5_1_harmonic_prior_smooth_l1_structured` |

## Queue And Artifact Audit

| Check | Result |
| --- | ---: |
| Completed queue entries | `108` |
| Failed queue entries | `0` |
| Running queue entries | `0` |
| Pending queue entries | `0` |
| Leaderboard entries | `108` |
| Dataset entries recorded as `polished_dataset` | `108` |
| Schema entries recorded as `polished_point_v1` | `108` |
| Missing referenced metrics/reports/checkpoints | `0` |

The campaign completed cleanly. All accepted leaderboard rows use the four
polished input features `theta`, `theta_dot`, `tau_load`, and `T`, with
`theta_TE` as the single target.

## Surface Winners

| Surface | Best Run | Family | Test MAE | Test RMSE | Val MAE | Params |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| Global | `te_periodic_gru_sequence_global` | `periodic_gru` | 0.001159 | 0.001465 | 0.001132 | 157,569 |
| Forward-only | `te_periodic_gru_sequence_fw` | `periodic_gru` | 0.001121 | 0.001444 | 0.001084 | 157,569 |
| Backward-only | `te_periodic_gru_sequence_bw` | `periodic_gru` | 0.001166 | 0.001481 | 0.001158 | 157,569 |

## Scalar Leaderboard Snapshot

The table below shows the first 12 entries from the scalar leaderboard. The
full ordered list, with exact run names and artifact paths, is stored in
`output/training_campaigns/2026-06-29-15-54-18_polished_dataset_full_wave_retraining_2026_06_22/campaign_leaderboard.yaml`.

| Rank | Compact Run | Surface | Family | Test MAE | Test RMSE | Val MAE |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | `periodic_gru_fw` | `fw` | `periodic_gru` | 0.001121 | 0.001444 | 0.001084 |
| 2 | `periodic_gru_global` | `global` | `periodic_gru` | 0.001159 | 0.001465 | 0.001132 |
| 3 | `periodic_gru_bw` | `bw` | `periodic_gru` | 0.001166 | 0.001481 | 0.001158 |
| 4 | `periodic_lstm_bw` | `bw` | `periodic_lstm` | 0.001226 | 0.001558 | 0.001230 |
| 5 | `periodic_mlp_harmonic_global` | `global` | `periodic_mlp_harmonic` | 0.001309 | 0.001794 | 0.001265 |
| 6 | `periodic_mlp_harmonic_bw` | `bw` | `periodic_mlp_harmonic` | 0.001342 | 0.001807 | 0.001188 |
| 7 | `periodic_mlp_harmonic_fw` | `fw` | `periodic_mlp_harmonic` | 0.001360 | 0.001845 | 0.001209 |
| 8 | `wave4_3_mdn_k3_global` | `global` | `wave4_3_mixture_density_k3` | 0.001544 | 0.001992 | 0.001407 |
| 9 | `periodic_lstm_fw` | `fw` | `periodic_lstm` | 0.001555 | 0.001983 | 0.001513 |
| 10 | `periodic_lstm_global` | `global` | `periodic_lstm` | 0.001601 | 0.002029 | 0.001536 |
| 11 | `wave4_3_mdn_k3_fw` | `fw` | `wave4_3_mixture_density_k3` | 0.001671 | 0.002181 | 0.001501 |
| 12 | `feedforward_bw` | `bw` | `feedforward` | 0.001686 | 0.002175 | 0.001630 |

## Registry And Program Effects

The completed run updated family-level registries for the full polished model
bank and refreshed the program scalar registry timestamp.

The campaign-level scalar winner is `te_periodic_gru_sequence_fw`, but the
current program-level scalar winner remains the earlier polished early-wave
`te_periodic_gru_sequence_bw` run because it has the lower test MAE
(`0.001084 deg` versus `0.001121 deg`).

This scalar result is useful as a retraining result, but it does not replace
the official direction-parallel curve-verified leaders until a separate
`TE Curve Verification Pipeline` refresh is run and accepted. The repository
must keep `global`, `Fw`, and `Bw` surfaces visible as separate decision
surfaces.

## Acceptance Decision

The full-wave campaign is accepted as a completed polished-dataset retraining
batch because:

- all `108` selected configs completed;
- no queue entries remain pending, running, or failed;
- every leaderboard entry records `polished_dataset`;
- every leaderboard entry records `polished_point_v1`;
- every accepted model uses four input features and one TE target;
- every referenced metric, training report, and checkpoint artifact exists.

## Closeout Notes

This closeout supersedes the earlier early-wave parallel training closeout as
the latest normal model-development campaign closeout. The early-wave and RCIM
polished closeouts remain preserved as previous completed campaign evidence.

The `TE Program Status And Closeout Ledger` requires a content update because
the latest normal campaign closeout changed from the early-wave parallel batch
to the full-wave retraining campaign. The official curve-verified leaders do
not change in this closeout because the `TE Curve Verification Pipeline` was
not run.

## Follow-Up

Recommended next steps:

1. prepare a separate operator-run `TE Curve Verification Pipeline` refresh
   that includes the polished RCIM, early-wave, and full-wave candidate set;
2. keep the scalar full-wave winner visible as campaign evidence, but use the
   curve-first policy for promotion;
3. evaluate whether the full-wave retraining results should feed a compact
   TwinCAT-facing candidate export set after curve verification.
