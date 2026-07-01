# Training Results Master Summary

## Executive Snapshot

- Generated At: `2026-06-29T10:40:05`
- Program State: active.
- Current Completed Wave: `polished_dataset` early-wave parallel training closeout
- Current Focus: wait for the externally running full-wave
  `polished_dataset` retraining campaign, then apply a dataset-aware roadmap
  that separates clean polished deployment, simplified noise-aware research,
  and cross-dataset transfer / reduced-point robustness.
- Active Campaign Status: `completed`
- Active Campaign Name: `polished_dataset_early_wave_parallel_training_2026_06_25`
- Current Program Winner: `te_periodic_gru_sequence_bw` | Family `periodic_gru_sequence_bw` | Test MAE `0.001084`

## Main Takeaways

- Strongest current neural family: `periodic_gru_sequence_bw`
- Current plain MLP anchor: `te_feedforward_trial`
- Active family-improvement branch count: `3`
- Implemented and benchmarked family count: `118`
- Latest polished RCIM Model-Bank Reproduction closeout accepted
  direction-specific ERT winners on both `forward` and `backward`; official
  curve-verified leaders are unchanged because the `TE Curve Verification
  Pipeline` refresh was not run inside normal closeout.
- `Wave 5.2` and `Wave 6` planning is now dataset-aware: `polished_dataset`
  is the final-comparison and deployment surface, `simplified_dataset` is the
  dirty/noise-aware diagnostic surface, and paired dataset work will evaluate
  backbone transfer, dirty-to-clean supervision, fine-tuning, and reduced-point
  robustness.

## Current Project Status

### Latest Polished RCIM Model-Bank Reproduction Closeout

The `polished_dataset_rcim_model_bank_reproduction_2026_06_22` campaign
completed both paper-faithful RCIM model-bank reproduction surfaces on
`polished_dataset`.

| Surface | Winner | Mean MAPE % | Mean MAE | Mean RMSE | Export Status |
| --- | --- | ---: | ---: | ---: | --- |
| `forward` | `ERT / ExtraTreesRegressor` | 11.939192 | 0.062217 | 0.149061 | `190` Python, `190` ONNX, `0` ONNX failures |
| `backward` | `ERT / ExtraTreesRegressor` | 18.399598 | 0.043815 | 0.110706 | `190` Python, `190` ONNX, `0` ONNX failures |

The generated model bundles remain local artifacts because the forward and
backward `paper_family_model_bank.pkl` files exceed the GitHub `100 MB`
single-file limit. The official `TE Curve Verification Pipeline` matrix was
not refreshed during this normal closeout.

### Dataset-Aware Roadmap Update

The full-wave `polished_dataset` retraining package is operator-reported as
running on another workstation. This checkout must not close out, verify, or
reinterpret that campaign until the final artifacts are synchronized.

Future architecture planning is split into three branches:

| Branch | Dataset surface | Planning role |
| --- | --- | --- |
| Clean deployment | `polished_dataset` | Final comparable model selection, curve-first promotion, and deployment-oriented decisions. |
| Noise-aware research | `simplified_dataset` | Diagnostic stress testing for robust losses, structured constraints, PINN-style soft losses, and multi-task denoising ideas. |
| Cross-dataset transfer | paired datasets | Backbone pretraining, fine-tuning on `polished_dataset`, dirty-to-clean supervision, and reduced-point robustness. |

The old `simplified_dataset`-centered `Wave 4` evidence remains useful as
noise-aware research evidence, but it is no longer sufficient by itself to
choose production-oriented `Wave 5.2` or `Wave 6` designs. The full `Wave
5.2A` paired matrix now evaluates all `1938` paired directional records
without touching training state. It shows near-zero peak-to-peak and
smoothness deltas, mean absolute offset delta `0.003216838 deg`, and a split
between `901` offset-shifted, `944` nonzero-harmonic changed, `65` nearly
identical, `27` sampling-anomaly, and `1` smoothness-changed pairs.

### Implemented And Benchmarked Families

- Multi-scope waves must keep `global`, `Fw`, and `Bw` reporting surfaces separated in this canonical summary.

#### Global Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `periodic_lstm_sequence_global` | Implemented Benchmark | `te_periodic_lstm_sequence_global` | `periodic_lstm_sequence` | 0.001187 | 210,049 | `2026-06-26 19:15:48` |
| `periodic_gru_sequence_global` | Implemented Benchmark | `te_periodic_gru_sequence_global` | `periodic_gru_sequence` | 0.001257 | 157,569 | `2026-06-26 15:05:37` |
| `periodic_mlp_harmonic_global` | Implemented Benchmark | `te_periodic_mlp_harmonic_global` | `periodic_mlp` | 0.001264 | 28,417 | `2026-06-26 05:02:22` |
| `periodic_gru_sequence` | Implemented Benchmark | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | 0.001279 | 157,569 | `2026-06-22 14:06:48` |
| `feedforward_global` | Implemented Benchmark | `te_feedforward_global` | `feedforward` | 0.001734 | 109,697 | `2026-06-25 20:23:10` |
| `tree` | Implemented Benchmark | `te_hist_gbr_tabular_global` | `hist_gradient_boosting` | 0.001753 | 4 | `2026-06-22 16:58:47` |
| `tree_global` | Implemented Benchmark | `te_tree_global` | `hist_gradient_boosting` | 0.001753 | 4 | `2026-06-25 16:04:23` |
| `periodic_mlp_global` | Implemented Benchmark | `te_periodic_mlp_global` | `periodic_mlp` | 0.001774 | 27,137 | `2026-06-26 01:57:07` |
| `residual_harmonic_mlp_global` | Implemented Benchmark | `te_residual_harmonic_mlp_global` | `residual_harmonic_mlp` | 0.001841 | 26,138 | `2026-06-25 16:42:24` |
| `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global` | Implemented Benchmark | `te_track2g_curve_aware_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | 0.002008 | 85,440 | `2026-06-22 15:16:05` |
| `residual_harmonic_gru_sequence_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.002112 | 150,676 | `2026-06-22 14:31:08` |
| `wave3_harmonic_prior_residual_smooth_l1_structured_global` | Implemented Benchmark | `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | 0.002168 | 7,168 | `2026-06-22 15:37:36` |
| `gru_sequence_global` | Implemented Benchmark | `te_gru_sequence_global` | `gru_sequence` | 0.002229 | 150,657 | `2026-06-26 08:53:33` |
| `lstm_sequence_global` | Implemented Benchmark | `te_lstm_sequence_global` | `lstm_sequence` | 0.002258 | 200,833 | `2026-06-26 11:02:54` |
| `periodic_temporal_convolution_global` | Implemented Benchmark | `te_periodic_temporal_convolution_global` | `periodic_temporal_convolution` | 0.002319 | 157,889 | `2026-06-26 13:03:57` |
| `track2h_latent_state_hysteresis_gru_offset_residual_global` | Implemented Benchmark | `te_track2h_l_gru_offset_residual_global` | `latent_state_hysteresis_probe` | 0.002339 | 124,899 | `2026-06-22 16:00:39` |
| `temporal_convolution_global` | Implemented Benchmark | `te_temporal_convolution_global` | `temporal_convolution` | 0.002411 | 146,369 | `2026-06-26 06:49:42` |
| `periodic_lstm_sequence` | Implemented Benchmark | `te_periodic_lstm_sequence_remote_global` | `periodic_lstm_sequence` | 0.002682 | 210,561 | `2026-05-25 19:20:56` |
| `feedforward` | Current Plain MLP Anchor | `te_feedforward_trial` | `feedforward` | 0.002877 | 26,113 | `2026-06-22 13:13:25` |
| `track2h_quantile_probabilistic_gaussian_nll_global` | Implemented Benchmark | `te_track2h_gaussian_nll_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003013 | 85,958 | `2026-06-12 13:12:35` |
| `residual_harmonic_mlp` | Active Improvement | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.003034 | 26,266 | `2026-05-20 11:41:03` |
| `periodic_mlp` | Active Improvement | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.003186 | 27,265 | `2026-05-21 08:12:57` |
| `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global` | Implemented Benchmark | `te_track2g_curve_aware_raw_centered_shape_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003350 | 85,747 | `2026-06-08 19:45:16` |
| `track2h_latent_state_hysteresis_causal_tcn_offset_residual_global` | Implemented Benchmark | `te_track2h_l_causal_tcn_offset_residual_global` | `latent_state_hysteresis_probe` | 0.003368 | 97,923 | `2026-06-16 19:16:49` |
| `residual_harmonic_lstm_sequence_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003368 | 201,364 | `2026-05-27 20:55:58` |
| `track2h_quantile_probabilistic_quantile_p10_p50_p90_global` | Implemented Benchmark | `te_track2h_quantile_p10_p50_p90_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003383 | 86,169 | `2026-06-12 11:34:56` |
| `track2h_dispersion_aware_mae_robust_global` | Implemented Benchmark | `te_track2h_mae_robust_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003406 | 85,747 | `2026-06-11 12:07:43` |
| `track2h_dispersion_aware_smooth_l1_robust_global` | Implemented Benchmark | `te_track2h_smooth_l1_robust_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003422 | 85,747 | `2026-06-11 12:48:44` |
| `wave3_harmonic_prior_residual_pointwise_control_global` | Implemented Benchmark | `te_wave3_harmonic_prior_residual_pointwise_control_global` | `wave3_harmonic_prior_residual` | 0.003451 | 7,283 | `2026-06-15 14:27:23` |
| `track2g_curve_aware_harmonic_residual_offset_raw_offset_global` | Implemented Benchmark | `te_track2g_curve_aware_raw_offset_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003465 | 85,747 | `2026-06-08 20:43:53` |
| `residual_harmonic_lstm_sequence_dense240` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_global_dense240` | `residual_harmonic_lstm_sequence` | 0.003473 | 201,826 | `2026-05-27 21:22:30` |
| `residual_harmonic_lstm_sequence_dense360` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_global_dense360` | `residual_harmonic_lstm_sequence` | 0.003477 | 202,066 | `2026-05-27 22:09:01` |
| `lstm_sequence` | Implemented Benchmark | `te_lstm_sequence_remote_global` | `lstm_sequence` | 0.003482 | 201,345 | `2026-05-24 12:16:30` |
| `track2h_mixture_density_heads_mdn_k2_global` | Implemented Benchmark | `te_track2h_mdn_k2_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003503 | 86,802 | `2026-06-13 11:32:06` |
| `track2h_dispersion_aware_log_cosh_robust_global` | Implemented Benchmark | `te_track2h_log_cosh_robust_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003505 | 85,747 | `2026-06-11 13:43:04` |
| `periodic_temporal_convolution` | Implemented Benchmark | `te_periodic_temporal_convolution_sequence_remote_global` | `periodic_temporal_convolution` | 0.003508 | 158,529 | `2026-05-25 16:10:13` |
| `residual_harmonic_gru_sequence_dense240` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_global_dense240` | `residual_harmonic_gru_sequence` | 0.003511 | 151,522 | `2026-05-27 19:32:17` |
| `track2f_bis_clean_sequential_residual_offset_global` | Implemented Benchmark | `te_track2f_bis_clean_residual_offset_global` | `sequential_residual_offset_probe` | 0.003528 | 92,802 | `2026-06-04 23:43:38` |
| `residual_harmonic_gru_sequence_dense360` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_global_dense360` | `residual_harmonic_gru_sequence` | 0.003535 | 151,762 | `2026-05-27 20:21:50` |
| `sequential_residual_offset_probe` | Implemented Benchmark | `te_sequential_residual_offset_probe_remote_global` | `sequential_residual_offset_probe` | 0.003537 | 92,802 | `2026-06-04 11:45:31` |
| `track2f_bis_harmonic_residual_offset_global` | Implemented Benchmark | `te_track2f_bis_harmonic_residual_offset_global` | `harmonic_residual_offset_probe` | 0.003538 | 85,747 | `2026-06-05 16:19:21` |
| `track2h_mixture_density_heads_mdn_k3_global` | Implemented Benchmark | `te_track2h_mdn_k3_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003564 | 87,435 | `2026-06-13 12:34:37` |
| `track2g_curve_aware_harmonic_residual_offset_pointwise_control_global` | Implemented Benchmark | `te_track2g_curve_aware_pointwise_control_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003587 | 85,747 | `2026-06-08 18:56:59` |
| `gru_sequence` | Implemented Benchmark | `te_gru_sequence_remote_global` | `gru_sequence` | 0.003591 | 151,041 | `2026-05-24 11:54:03` |
| `temporal_convolution` | Implemented Benchmark | `te_temporal_convolution_sequence_remote_global` | `temporal_convolution` | 0.003754 | 147,009 | `2026-05-24 11:30:23` |
| `harmonic_regression_global` | Implemented Benchmark | `te_harmonic_regression_global` | `harmonic_regression` | 0.003795 | 125 | `2026-06-26 03:44:24` |
| `harmonic_regression` | Active Improvement | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.003839 | 125 | `2026-06-22 13:26:44` |
| `feedforward_recovery_micro` | Implemented Benchmark | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004164 | 109,953 | `2026-05-12 11:12:51` |
| `feedforward_recovery_probe_dense` | Implemented Benchmark | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004602 | 109,953 | `2026-05-12 17:16:41` |

#### Forward Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `periodic_gru_sequence_fw` | Implemented Benchmark | `te_periodic_gru_sequence_fw` | `periodic_gru_sequence` | 0.001101 | 157,569 | `2026-06-26 16:26:19` |
| `periodic_mlp_harmonic_fw` | Implemented Benchmark | `te_periodic_mlp_harmonic_fw` | `periodic_mlp` | 0.001326 | 28,417 | `2026-06-26 05:40:23` |
| `periodic_lstm_sequence_fw` | Implemented Benchmark | `te_periodic_lstm_sequence_fw` | `periodic_lstm_sequence` | 0.001547 | 210,049 | `2026-06-26 20:15:05` |
| `feedforward_fw` | Implemented Benchmark | `te_feedforward_fw` | `feedforward` | 0.001726 | 109,697 | `2026-06-25 22:07:36` |
| `periodic_mlp_fw` | Implemented Benchmark | `te_periodic_mlp_fw` | `periodic_mlp` | 0.001742 | 27,137 | `2026-06-26 02:41:02` |
| `tree_fw` | Implemented Benchmark | `te_tree_fw` | `hist_gradient_boosting` | 0.001753 | 4 | `2026-06-25 16:06:52` |
| `residual_harmonic_mlp_fw` | Implemented Benchmark | `te_residual_harmonic_mlp_fw` | `residual_harmonic_mlp` | 0.001808 | 26,138 | `2026-06-25 17:06:54` |
| `periodic_temporal_convolution_fw` | Implemented Benchmark | `te_periodic_temporal_convolution_fw` | `periodic_temporal_convolution` | 0.002178 | 157,889 | `2026-06-26 13:35:38` |
| `gru_sequence_fw` | Implemented Benchmark | `te_gru_sequence_fw` | `gru_sequence` | 0.002260 | 150,657 | `2026-06-26 09:28:46` |
| `lstm_sequence_fw` | Implemented Benchmark | `te_lstm_sequence_fw` | `lstm_sequence` | 0.002266 | 200,833 | `2026-06-26 11:50:45` |
| `temporal_convolution_fw` | Implemented Benchmark | `te_temporal_convolution_fw` | `temporal_convolution` | 0.002399 | 146,369 | `2026-06-26 07:23:08` |
| `track2f_bis_harmonic_residual_offset_fw` | Implemented Benchmark | `te_track2f_bis_harmonic_residual_offset_fw` | `harmonic_residual_offset_probe` | 0.002862 | 85,747 | `2026-06-05 16:32:38` |
| `harmonic_regression_fw` | Implemented Benchmark | `te_harmonic_dense360_tracking_Fw` | `harmonic_regression` | 0.002916 | 4,326 | `2026-06-26 04:00:06` |
| `track2h_dispersion_aware_mae_robust_fw` | Implemented Benchmark | `te_track2h_mae_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003146 | 85,747 | `2026-06-11 12:14:52` |
| `track2h_quantile_probabilistic_gaussian_nll_fw` | Implemented Benchmark | `te_track2h_gaussian_nll_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003165 | 85,958 | `2026-06-12 13:25:53` |
| `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw` | Implemented Benchmark | `te_track2g_curve_aware_raw_centered_shape_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003181 | 85,747 | `2026-06-08 19:56:04` |
| `residual_harmonic_gru_sequence_fw_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003200 | 151,060 | `2026-05-27 19:12:38` |
| `residual_harmonic_gru_sequence_fw_dense240` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Fw_dense240` | `residual_harmonic_gru_sequence` | 0.003219 | 151,522 | `2026-05-27 19:40:30` |
| `residual_harmonic_lstm_sequence_fw_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003234 | 201,364 | `2026-05-27 21:00:48` |
| `track2h_mixture_density_heads_mdn_k3_fw` | Implemented Benchmark | `te_track2h_mdn_k3_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003235 | 87,435 | `2026-06-13 12:43:18` |
| `residual_harmonic_gru_sequence_fw_dense360` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Fw_dense360` | `residual_harmonic_gru_sequence` | 0.003241 | 151,762 | `2026-05-27 20:33:03` |
| `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw` | Implemented Benchmark | `te_track2g_curve_aware_full_curve_composite_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003260 | 85,747 | `2026-06-08 21:49:46` |
| `residual_harmonic_lstm_sequence_fw_dense240` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Fw_dense240` | `residual_harmonic_lstm_sequence` | 0.003262 | 201,826 | `2026-05-27 21:29:55` |
| `track2g_curve_aware_harmonic_residual_offset_raw_offset_fw` | Implemented Benchmark | `te_track2g_curve_aware_raw_offset_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003279 | 85,747 | `2026-06-08 20:51:34` |
| `track2h_quantile_probabilistic_quantile_p10_p50_p90_fw` | Implemented Benchmark | `te_track2h_quantile_p10_p50_p90_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003285 | 86,169 | `2026-06-12 11:43:50` |
| `track2h_dispersion_aware_smooth_l1_robust_fw` | Implemented Benchmark | `te_track2h_smooth_l1_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003314 | 85,747 | `2026-06-11 12:56:26` |
| `track2h_mixture_density_heads_mdn_k2_fw` | Implemented Benchmark | `te_track2h_mdn_k2_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003339 | 86,802 | `2026-06-13 11:41:07` |
| `residual_harmonic_lstm_sequence_fw_dense360` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Fw_dense360` | `residual_harmonic_lstm_sequence` | 0.003351 | 202,066 | `2026-05-27 22:19:22` |
| `track2h_dispersion_aware_log_cosh_robust_fw` | Implemented Benchmark | `te_track2h_log_cosh_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003355 | 85,747 | `2026-06-11 13:51:00` |
| `track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw` | Implemented Benchmark | `te_track2g_curve_aware_pointwise_control_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003371 | 85,747 | `2026-06-08 19:08:39` |
| `wave3_harmonic_prior_residual_pointwise_control_fw` | Implemented Benchmark | `te_wave3_harmonic_prior_residual_pointwise_control_fw` | `wave3_harmonic_prior_residual` | 0.003382 | 7,283 | `2026-06-15 14:34:34` |
| `sequential_residual_offset_probe_fw` | Implemented Benchmark | `te_sequential_residual_offset_probe_remote_fw` | `sequential_residual_offset_probe` | 0.003385 | 92,802 | `2026-06-04 11:57:40` |
| `track2f_bis_clean_sequential_residual_offset_fw` | Implemented Benchmark | `te_track2f_bis_clean_residual_offset_fw` | `sequential_residual_offset_probe` | 0.003446 | 92,802 | `2026-06-04 23:48:53` |
| `track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw` | Implemented Benchmark | `te_track2h_l_causal_tcn_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.003470 | 97,923 | `2026-06-16 19:22:12` |
| `wave3_harmonic_prior_residual_smooth_l1_structured_fw` | Implemented Benchmark | `te_wave3_harmonic_prior_residual_smooth_l1_structured_fw` | `wave3_harmonic_prior_residual` | 0.003527 | 7,283 | `2026-06-15 15:16:24` |
| `track2h_latent_state_hysteresis_gru_offset_residual_fw` | Implemented Benchmark | `te_track2h_l_gru_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.003537 | 125,475 | `2026-06-16 18:34:12` |

#### Backward Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `periodic_gru_sequence_bw` | Current Program Winner | `te_periodic_gru_sequence_bw` | `periodic_gru_sequence` | 0.001084 | 157,569 | `2026-06-26 17:47:56` |
| `periodic_mlp_harmonic_bw` | Implemented Benchmark | `te_periodic_mlp_harmonic_bw` | `periodic_mlp` | 0.001279 | 28,417 | `2026-06-26 06:20:09` |
| `periodic_lstm_sequence_bw` | Implemented Benchmark | `te_periodic_lstm_sequence_bw` | `periodic_lstm_sequence` | 0.001338 | 210,049 | `2026-06-26 21:30:02` |
| `residual_harmonic_mlp_bw` | Implemented Benchmark | `te_residual_harmonic_mlp_bw` | `residual_harmonic_mlp` | 0.001712 | 26,138 | `2026-06-25 17:47:36` |
| `feedforward_bw` | Implemented Benchmark | `te_feedforward_bw` | `feedforward` | 0.001719 | 109,697 | `2026-06-26 01:27:10` |
| `tree_bw` | Implemented Benchmark | `te_tree_bw` | `hist_gradient_boosting` | 0.001753 | 4 | `2026-06-25 16:09:16` |
| `periodic_mlp_bw` | Implemented Benchmark | `te_periodic_mlp_bw` | `periodic_mlp` | 0.001758 | 27,137 | `2026-06-26 03:21:12` |
| `periodic_temporal_convolution_bw` | Implemented Benchmark | `te_periodic_temporal_convolution_bw` | `periodic_temporal_convolution` | 0.002238 | 157,889 | `2026-06-26 14:02:44` |
| `lstm_sequence_bw` | Implemented Benchmark | `te_lstm_sequence_bw` | `lstm_sequence` | 0.002240 | 200,833 | `2026-06-26 12:41:41` |
| `gru_sequence_bw` | Implemented Benchmark | `te_gru_sequence_bw` | `gru_sequence` | 0.002271 | 150,657 | `2026-06-26 10:10:50` |
| `temporal_convolution_bw` | Implemented Benchmark | `te_temporal_convolution_bw` | `temporal_convolution` | 0.002391 | 146,369 | `2026-06-26 07:57:05` |
| `track2h_mixture_density_heads_mdn_k2_bw` | Implemented Benchmark | `te_track2h_mdn_k2_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002658 | 86,802 | `2026-06-13 12:14:13` |
| `track2h_mixture_density_heads_mdn_k3_bw` | Implemented Benchmark | `te_track2h_mdn_k3_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002721 | 87,435 | `2026-06-13 13:10:07` |
| `track2h_quantile_probabilistic_quantile_p10_p50_p90_bw` | Implemented Benchmark | `te_track2h_quantile_p10_p50_p90_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002927 | 86,169 | `2026-06-12 12:10:23` |
| `track2h_quantile_probabilistic_gaussian_nll_bw` | Implemented Benchmark | `te_track2h_gaussian_nll_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002998 | 85,958 | `2026-06-12 13:53:26` |
| `track2h_dispersion_aware_smooth_l1_robust_bw` | Implemented Benchmark | `te_track2h_smooth_l1_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003074 | 85,747 | `2026-06-11 13:24:47` |
| `track2f_bis_harmonic_residual_offset_bw` | Implemented Benchmark | `te_track2f_bis_harmonic_residual_offset_bw` | `harmonic_residual_offset_probe` | 0.003336 | 85,747 | `2026-06-05 16:44:49` |
| `wave3_harmonic_prior_residual_pointwise_control_bw` | Implemented Benchmark | `te_wave3_harmonic_prior_residual_pointwise_control_bw` | `wave3_harmonic_prior_residual` | 0.003363 | 7,283 | `2026-06-15 14:49:19` |
| `harmonic_regression_bw` | Implemented Benchmark | `te_harmonic_dense240_tracking_Bw` | `harmonic_regression` | 0.003400 | 2,886 | `2026-06-26 04:20:03` |
| `track2h_dispersion_aware_mae_robust_bw` | Implemented Benchmark | `te_track2h_mae_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003430 | 85,747 | `2026-06-11 12:33:14` |
| `track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw` | Implemented Benchmark | `te_track2g_curve_aware_pointwise_control_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003430 | 85,747 | `2026-06-08 19:23:08` |
| `wave3_harmonic_prior_residual_smooth_l1_structured_bw` | Implemented Benchmark | `te_wave3_harmonic_prior_residual_smooth_l1_structured_bw` | `wave3_harmonic_prior_residual` | 0.003431 | 7,283 | `2026-06-15 15:30:20` |
| `residual_harmonic_lstm_sequence_bw_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003440 | 201,364 | `2026-05-27 21:08:36` |
| `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw` | Implemented Benchmark | `te_track2g_curve_aware_raw_centered_shape_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003465 | 85,747 | `2026-06-08 20:11:41` |
| `residual_harmonic_gru_sequence_bw_dense360` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Bw_dense360` | `residual_harmonic_gru_sequence` | 0.003468 | 151,762 | `2026-05-27 20:46:25` |
| `track2g_curve_aware_harmonic_residual_offset_raw_offset_bw` | Implemented Benchmark | `te_track2g_curve_aware_raw_offset_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003471 | 85,747 | `2026-06-08 21:06:56` |
| `track2h_dispersion_aware_log_cosh_robust_bw` | Implemented Benchmark | `te_track2h_log_cosh_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003481 | 85,747 | `2026-06-11 14:01:57` |
| `residual_harmonic_gru_sequence_bw_dense240` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Bw_dense240` | `residual_harmonic_gru_sequence` | 0.003492 | 151,522 | `2026-05-27 20:00:10` |
| `residual_harmonic_gru_sequence_bw_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003502 | 151,060 | `2026-05-27 19:18:56` |
| `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw` | Implemented Benchmark | `te_track2g_curve_aware_full_curve_composite_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003511 | 85,747 | `2026-06-08 22:05:10` |
| `track2f_bis_clean_sequential_residual_offset_bw` | Implemented Benchmark | `te_track2f_bis_clean_residual_offset_bw` | `sequential_residual_offset_probe` | 0.003540 | 92,802 | `2026-06-04 23:58:31` |
| `track2h_latent_state_hysteresis_gru_offset_residual_bw` | Implemented Benchmark | `te_track2h_l_gru_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.003545 | 125,475 | `2026-06-16 18:48:13` |
| `residual_harmonic_lstm_sequence_bw_dense360` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Bw_dense360` | `residual_harmonic_lstm_sequence` | 0.003556 | 202,066 | `2026-05-27 22:35:20` |
| `residual_harmonic_lstm_sequence_bw_dense240` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_remote_Bw_dense240` | `residual_harmonic_lstm_sequence` | 0.003605 | 201,826 | `2026-05-27 21:40:13` |
| `track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw` | Implemented Benchmark | `te_track2h_l_causal_tcn_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.003630 | 97,923 | `2026-06-16 19:34:05` |
| `sequential_residual_offset_probe_bw` | Implemented Benchmark | `te_sequential_residual_offset_probe_remote_bw` | `sequential_residual_offset_probe` | 0.003638 | 92,802 | `2026-06-04 12:04:47` |

### Active Training Or Improvement Branches

- Current campaign: `polished_dataset_early_wave_parallel_training_2026_06_25`
- Launch mode: `N/A`
- Families under active improvement: `harmonic_regression`, `periodic_mlp`, `residual_harmonic_mlp`
- Planning report: `doc/reports/campaign_plans/cross_wave/polished_dataset/2026-06-25-15-28-26_polished_early_wave_parallel_training_campaign_plan_report.md`

### Roadmap And Planned Work

| Wave Or Track | Status |
| --- | --- |
| Wave 0. Shared Infrastructure | completed. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 1. Structured Static Baselines | planning report: completed;; implementation: completed;; smoke tests: completed;; validation checks: completed;; campaign execution: completed;; directional HPO closeout: completed;; exported `global`, `forward`, and `backward` surfaces: completed;; results report: completed;; status: closed. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| RCIM Model-Bank Reproduction. RCIM Paper-Faithful Model Bank | recovered original workflow: preserved;; original-dataset reimplementation: completed;; retuned reference archive: completed;; forward campaign: completed;; backward campaign: completed;; paper-reference archives: refreshed;; Tables `2`-`5`: repopulated;; status: closed as faithful full-bank reproduction, not all-green |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| TE Curve Verification Pipeline. Directional Offline Comparison | direction-aware loader and candidate matrix: completed;; recovered original forward candidates: included;; retuned forward and backward candidates: included;; `RCIM Model-Bank Reproduction` forward and backward candidates: included;; `Wave 1` `global`, `forward`, and `backward` exports: included;; `Wave 2.1` temporal `global`, `forward`, and `backward` registry candidates:; grouped source tables: completed;; composite best-reference visibility: completed;; direction/truth and preview audit: completed;; official model-verification report: completed;; multi-index curve-first selection policy: adopted;; complete multi-index reranking over all current official candidates:; status: closed. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 2.1. Temporal Models | status: entry campaign completed; closeout report prepared; official; initial families: `temporal_convolution`, `gru_sequence`, `lstm_sequence`;; configuration root: `config/training/hydra/wave2/`;; preliminary campaign plan:; closeout report:; campaign winner: `te_gru_sequence_remote_Fw` from family; refresh plan:; official verification report:; curve-verification decision: verified exploratory baselines, not promoted over `tree`;; mandatory rule: prepare or justify `global`, `forward`, and `backward`; baseline comparison: TE Curve Verification Pipeline plus closed Wave 1. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 2.2. Harmonic Temporal Hybrid Models | status: harmonic-temporal hybrid campaign completed; normal closeout report; families: `periodic_temporal_convolution`, `periodic_gru_sequence`,; configuration root:; preliminary campaign plan:; closeout report:; campaign winner: `te_periodic_gru_sequence_remote_Bw` from family; strongest bidirectional candidate: `te_periodic_gru_sequence_remote_global`; curve-verification decision: strongest repository-owned neural branch after official; mandatory rule: prepare or justify `global`, `forward`, and `backward`; baseline comparison: official curve-verification matrix plus visual collage and overlay |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 2.3. Residual Harmonic Temporal Hybrid Models | status: residual harmonic temporal hybrid campaign completed; official; families: `residual_harmonic_gru_sequence`,; harmonic banks: sparse `RCIM`, dense `240`, dense `360`;; closeout report:; official verification report:; strongest Wave 2.3 forward candidate:; strongest Wave 2.3 backward candidate:; strongest Wave 2.3 global candidate:; curve-verification decision: verified exploratory baseline, not promoted over the; design conclusion: sparse `RCIM` harmonics remain useful, while dense `240` |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 3.1. Offset-Aware Sequential Residual Probe | status: offset-aware probe campaign completed; official `TE Curve Verification Pipeline` matrix; family: `sequential_residual_offset_probe`;; official verification report:; strongest Wave 3.1 forward candidate:; strongest Wave 3.1 backward candidate:; strongest Wave 3.1 global candidate:; curve-verification decision: verified exploratory baseline, not promoted over the; design conclusion: a sequential residual offset head alone does not solve |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 3.2. Harmonic-Offset Probe | status: campaign completed after runner registration repair; official; families:; `track2f_bis_clean_sequential_residual_offset_global`;; `track2f_bis_clean_sequential_residual_offset_fw`;; `track2f_bis_clean_sequential_residual_offset_bw`;; `track2f_bis_harmonic_residual_offset_global`;; `track2f_bis_harmonic_residual_offset_fw`;; `track2f_bis_harmonic_residual_offset_bw`;; closeout report:; official verification report:; clean global candidate:; harmonic global candidate:; clean forward candidate:; harmonic forward candidate:; clean backward candidate:; harmonic backward candidate:; strongest Wave 3.2 forward candidate:; strongest Wave 3.2 backward candidate:; strongest Wave 3.2 global candidate:; curve-verification decision: verified exploratory baseline, not promoted over the; design conclusion: harmonic forcing helps the direction-specific `Fw` and |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 4.1. Dispersion-Aware Robust-Loss Probe | status: robust-loss campaign completed; official `TE Curve Verification Pipeline` matrix refresh; families:; `track2h_dispersion_aware_mae_robust_global`;; `track2h_dispersion_aware_mae_robust_fw`;; `track2h_dispersion_aware_mae_robust_bw`;; `track2h_dispersion_aware_smooth_l1_robust_global`;; `track2h_dispersion_aware_smooth_l1_robust_fw`;; `track2h_dispersion_aware_smooth_l1_robust_bw`;; `track2h_dispersion_aware_log_cosh_robust_global`;; `track2h_dispersion_aware_log_cosh_robust_fw`;; `track2h_dispersion_aware_log_cosh_robust_bw`;; closeout report:; official verification report:; robust global candidate:; robust forward candidate:; robust backward candidate:; campaign scalar winner:; TE Curve Verification Pipeline strongest forward candidate:; TE Curve Verification Pipeline strongest backward candidate:; TE Curve Verification Pipeline strongest global candidate:; curve-verification decision: verified exploratory baseline, not promoted over the; design conclusion: robust losses are useful enough to keep in the |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 4.2. Quantile Probabilistic Probe | status: quantile/probabilistic campaign completed; official `TE Curve Verification Pipeline` matrix; families:; `track2h_quantile_probabilistic_quantile_p10_p50_p90_global`;; `track2h_quantile_probabilistic_quantile_p10_p50_p90_fw`;; `track2h_quantile_probabilistic_quantile_p10_p50_p90_bw`;; `track2h_quantile_probabilistic_gaussian_nll_global`;; `track2h_quantile_probabilistic_gaussian_nll_fw`;; `track2h_quantile_probabilistic_gaussian_nll_bw`;; closeout report:; official verification report:; strongest probabilistic global candidate:; strongest probabilistic forward-only candidate:; strongest probabilistic forward-evaluated candidate:; strongest probabilistic backward candidate:; curve-verification decision: verified exploratory baseline, not promoted over the; design conclusion: probabilistic losses improve over robust losses on the |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 4.3. Mixture Density Heads Probe | status: mixture-density heads campaign completed; official `TE Curve Verification Pipeline` matrix; families:; `track2h_mixture_density_heads_mdn_k2_global`;; `track2h_mixture_density_heads_mdn_k2_fw`;; `track2h_mixture_density_heads_mdn_k2_bw`;; `track2h_mixture_density_heads_mdn_k3_global`;; `track2h_mixture_density_heads_mdn_k3_fw`;; `track2h_mixture_density_heads_mdn_k3_bw`;; closeout report:; official verification report:; matrix output:; strongest MDN global candidate:; strongest MDN forward candidate:; strongest MDN backward candidate:; strongest TE Curve Verification Pipeline forward MDN candidate:; strongest TE Curve Verification Pipeline backward MDN candidate:; strongest TE Curve Verification Pipeline global MDN candidate:; campaign scalar winner:; program scalar winner changed: no, `te_periodic_gru_sequence_remote_Bw`; curve-verification decision: verified exploratory baseline, not promoted over the; design conclusion: MDN improves the scalar `Bw` dispersion-aware branch by |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 4.4. Latent-State Hysteresis Probe | status: latent-state / hysteresis-aware campaign completed; official; families:; `track2h_latent_state_hysteresis_gru_offset_residual_global`;; `track2h_latent_state_hysteresis_gru_offset_residual_fw`;; `track2h_latent_state_hysteresis_gru_offset_residual_bw`;; `track2h_latent_state_hysteresis_causal_tcn_offset_residual_global`;; `track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw`;; `track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw`;; closeout report:; official TE curve-verification report:; official curve-verification matrix:; strongest `Wave 4.4` global candidate:; strongest `Wave 4.4` forward candidate:; strongest `Wave 4.4` backward candidate:; campaign scalar winner:; program scalar winner changed: no, `te_periodic_gru_sequence_remote_Bw`; scalar comparison: `Wave 4.4` improves the `global` scalar surface versus MDN; official TE Curve Verification Pipeline strongest refreshed candidates:; curve-verification decision: verified exploratory baseline, not promoted over; design conclusion: causal history is useful as a diagnostic signal, but this |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 5.1. Hybrid Structured Models | status: first real campaign closed successfully as a scalar training; current scaffold:; model type: `wave3_harmonic_prior_residual`;; model class:; dry-run skeleton checker:; training-smoke-ready checker:; final one-batch validation artifact:; prepared package:; prepared launcher:; campaign closeout report:; scalar training winner:; scalar decision: no program-best promotion; the current program winner; official TE Curve Verification Pipeline launcher:; official TE curve-verification report:; strongest Wave 5.1 TE Curve Verification Pipeline candidate:; updated priority: use the completed Wave 5.1 curve, offset, collage, overlay,; mandatory rule: prepare or justify `global`, `forward`, and `backward`; paper-reproduction scope:; compare hybrid structured predictors against the paper-style harmonic stack;; test condition-conditioned residual structure and separate treatment of; prepare the repository-owned deployable predictor package after the; next implementation steps:; proceed to `Wave 5.2` / integrated multi-head planning with hidden-state |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 5.2. PINN Formulation And First PINN | status: pre-implemented at `Wave 5.2A` diagnostic level, not campaign-ready;; current scaffold:; diagnostic adapter:; diagnostic report builder:; parameter-inventory report builder:; generated diagnostic report:; generated parameter-inventory report:; companion artifacts:; parameter-inventory artifacts:; updated priority: execute dataset-aligned diagnostic calibration after the; mandatory rule: prepare or justify `global`, `forward`, and `backward`; paper-reproduction scope:; prepare PINN-side model and loss formulations for later offline and; test whether soft physics, periodicity, smoothness, harmonic-consistency,; keep online compensation execution out of Wave 5.2 unless Track 3 is; completed inventory conclusions:; known geometry constants are safe for diagnostics and feature generation;; operating metadata can be used for stratification and causal conditioning;; five equivalent-error groups are train-only calibratable;; contact geometry remains unavailable or ambiguous and blocks calibrated; measured TE remains target-only and must not become an inference input.; next implementation steps:; compare MMT diagnostic signatures against dataset-aligned curve summaries; design a train-only equivalent-error calibration policy for candidate; decide whether the MMT path remains diagnostic-only, becomes a feature; do not treat the current demonstration harmonic summary as dataset |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 5. Cross-Wave Comparison And Best Solution | status: pending;; mandatory rule: preserve direction-separated reporting;; paper-reproduction scope:; compare closed offline waves and Track 3 results when available;; finalize the real `paper vs repository` comparison only after Track 3 |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Track 3. Online Compensation And Deployment Evaluation | status: future implementation branch;; canonical objective: close `Target B`;; scope:; online compensation loop in the TestRig / TwinCAT path;; old future Pipelines `8-10`;; `Robot` and `Cycloidal` motion-profile validation;; uncompensated versus compensated `TE RMS` and `TE max`;; final paper-style `Table 9` report;; deployment-readiness interpretation for the selected repository model path. |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`

## Recent Campaign Changes

| Campaign | Generated At | Completed | Failed | Winner | Impact |
| --- | --- | ---: | ---: | --- | --- |
| `polished_dataset_early_wave_parallel_training_2026_06_25` | `2026-06-26 21:30:02` | 36 | 0 | `te_periodic_gru_sequence_bw` | Updated global best |
| `polished_dataset_stage1_smoke_2026_06_21` | `2026-06-22 16:00:39` | 8 | 0 | `te_periodic_gru_sequence_remote_global` | Updated periodic_gru_sequence family best |
| `polished_dataset_stage1_smoke_2026_06_21` | `2026-06-22 12:04:16` | 0 | 1 | N/A | No winner artifact |
| `track2h_latent_state_hysteresis_campaign_2026_06_16` | `2026-06-16 19:34:05` | 6 | 0 | `te_track2h_l_causal_tcn_offset_residual_global` | Updated track2h_latent_state_hysteresis_causal_tcn_offset_residual_global family best |
| `wave3_harmonic_prior_residual_campaign_2026_06_14` | `2026-06-15 15:30:20` | 6 | 0 | `te_wave3_harmonic_prior_residual_pointwise_control_bw` | Updated wave3_harmonic_prior_residual_pointwise_control_bw family best |

## Ranking Policy

- Primary metric: `test_mae`
- First tie-breaker: `test_rmse`
- Second tie-breaker: `val_mae`
- Third tie-breaker: `trainable_parameter_count`
- Direction: `minimize`

## Best Result Per Family

- Scope-separated family ranking is mandatory for every future wave that introduces more than one canonical training surface.

### Global Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `periodic_lstm_sequence_global` | `te_periodic_lstm_sequence_global` | `periodic_lstm_sequence` | 0.001185 | 0.001187 | 0.001505 | 210,049 | N/A | Unknown | Implemented Benchmark |
| `periodic_gru_sequence_global` | `te_periodic_gru_sequence_global` | `periodic_gru_sequence` | 0.001252 | 0.001257 | 0.001613 | 157,569 | N/A | Unknown | Implemented Benchmark |
| `periodic_mlp_harmonic_global` | `te_periodic_mlp_harmonic_global` | `periodic_mlp` | 0.001196 | 0.001264 | 0.001737 | 28,417 | N/A | Unknown | Implemented Benchmark |
| `periodic_gru_sequence` | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | 0.001274 | 0.001279 | 0.001638 | 157,569 | 1.82 MB | High | Implemented Benchmark |
| `feedforward_global` | `te_feedforward_global` | `feedforward` | 0.001637 | 0.001734 | 0.002220 | 109,697 | N/A | Unknown | Implemented Benchmark |
| `tree` | `te_hist_gbr_tabular_global` | `hist_gradient_boosting` | 0.001591 | 0.001753 | 0.002892 | 4 | 0.44 MB | Very Low | Implemented Benchmark |
| `tree_global` | `te_tree_global` | `hist_gradient_boosting` | 0.001591 | 0.001753 | 0.002892 | 4 | N/A | Unknown | Implemented Benchmark |
| `periodic_mlp_global` | `te_periodic_mlp_global` | `periodic_mlp` | 0.001634 | 0.001774 | 0.002355 | 27,137 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_mlp_global` | `te_residual_harmonic_mlp_global` | `residual_harmonic_mlp` | 0.001660 | 0.001841 | 0.002433 | 26,138 | N/A | Unknown | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global` | `te_track2g_curve_aware_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001872 | 0.002008 | 0.002581 | 85,440 | 1.00 MB | High | Implemented Benchmark |
| `residual_harmonic_gru_sequence_sparse_rcim` | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.001978 | 0.002112 | 0.002699 | 150,676 | 1.74 MB | Medium | Implemented Benchmark |
| `wave3_harmonic_prior_residual_smooth_l1_structured_global` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | 0.001889 | 0.002168 | 0.002763 | 7,168 | 0.10 MB | Medium | Implemented Benchmark |
| `gru_sequence_global` | `te_gru_sequence_global` | `gru_sequence` | 0.002126 | 0.002229 | 0.002872 | 150,657 | N/A | Unknown | Implemented Benchmark |
| `lstm_sequence_global` | `te_lstm_sequence_global` | `lstm_sequence` | 0.002151 | 0.002258 | 0.002894 | 200,833 | N/A | Unknown | Implemented Benchmark |
| `periodic_temporal_convolution_global` | `te_periodic_temporal_convolution_global` | `periodic_temporal_convolution` | 0.002202 | 0.002319 | 0.002900 | 157,889 | N/A | Unknown | Implemented Benchmark |
| `track2h_latent_state_hysteresis_gru_offset_residual_global` | `te_track2h_l_gru_offset_residual_global` | `latent_state_hysteresis_probe` | 0.002232 | 0.002339 | 0.002986 | 124,899 | 1.48 MB | Medium | Implemented Benchmark |
| `temporal_convolution_global` | `te_temporal_convolution_global` | `temporal_convolution` | 0.002308 | 0.002411 | 0.003063 | 146,369 | N/A | Unknown | Implemented Benchmark |
| `periodic_lstm_sequence` | `te_periodic_lstm_sequence_remote_global` | `periodic_lstm_sequence` | 0.002526 | 0.002682 | 0.002969 | 210,561 | 2.43 MB | High | Implemented Benchmark |
| `feedforward` | `te_feedforward_trial` | `feedforward` | 0.002725 | 0.002877 | 0.003835 | 26,113 | 0.32 MB | Low | Current Plain MLP Anchor |
| `track2h_quantile_probabilistic_gaussian_nll_global` | `te_track2h_gaussian_nll_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003267 | 0.003013 | 0.003388 | 85,958 | 1.00 MB | High | Implemented Benchmark |
| `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.002895 | 0.003034 | 0.003550 | 26,266 | 0.32 MB | Unknown | Active Improvement |
| `periodic_mlp` | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.002994 | 0.003186 | 0.003690 | 27,265 | 0.33 MB | Unknown | Active Improvement |
| `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global` | `te_track2g_curve_aware_raw_centered_shape_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003636 | 0.003350 | 0.003753 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `track2h_latent_state_hysteresis_causal_tcn_offset_residual_global` | `te_track2h_l_causal_tcn_offset_residual_global` | `latent_state_hysteresis_probe` | 0.003543 | 0.003368 | 0.003860 | 97,923 | 1.17 MB | Medium | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_sparse_rcim` | `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003632 | 0.003368 | 0.003808 | 201,364 | 2.32 MB | Low | Implemented Benchmark |
| `track2h_quantile_probabilistic_quantile_p10_p50_p90_global` | `te_track2h_quantile_p10_p50_p90_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003606 | 0.003383 | 0.003764 | 86,169 | 1.01 MB | Medium | Implemented Benchmark |
| `track2h_dispersion_aware_mae_robust_global` | `te_track2h_mae_robust_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003645 | 0.003406 | 0.003807 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `track2h_dispersion_aware_smooth_l1_robust_global` | `te_track2h_smooth_l1_robust_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003641 | 0.003422 | 0.003810 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `wave3_harmonic_prior_residual_pointwise_control_global` | `te_wave3_harmonic_prior_residual_pointwise_control_global` | `wave3_harmonic_prior_residual` | 0.003611 | 0.003451 | 0.003851 | 7,283 | 0.11 MB | Medium | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_raw_offset_global` | `te_track2g_curve_aware_raw_offset_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003564 | 0.003465 | 0.003829 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_dense240` | `te_residual_harmonic_lstm_sequence_remote_global_dense240` | `residual_harmonic_lstm_sequence` | 0.003624 | 0.003473 | 0.003925 | 201,826 | 2.33 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_dense360` | `te_residual_harmonic_lstm_sequence_remote_global_dense360` | `residual_harmonic_lstm_sequence` | 0.003648 | 0.003477 | 0.003940 | 202,066 | 2.33 MB | Medium | Implemented Benchmark |
| `lstm_sequence` | `te_lstm_sequence_remote_global` | `lstm_sequence` | 0.003681 | 0.003482 | 0.003948 | 201,345 | 2.32 MB | Low | Implemented Benchmark |
| `track2h_mixture_density_heads_mdn_k2_global` | `te_track2h_mdn_k2_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003654 | 0.003503 | 0.003938 | 86,802 | 1.01 MB | Medium | Implemented Benchmark |
| `track2h_dispersion_aware_log_cosh_robust_global` | `te_track2h_log_cosh_robust_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003645 | 0.003505 | 0.003935 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `periodic_temporal_convolution` | `te_periodic_temporal_convolution_sequence_remote_global` | `periodic_temporal_convolution` | 0.003634 | 0.003508 | 0.003929 | 158,529 | 1.83 MB | Medium | Implemented Benchmark |
| `residual_harmonic_gru_sequence_dense240` | `te_residual_harmonic_gru_sequence_remote_global_dense240` | `residual_harmonic_gru_sequence` | 0.003600 | 0.003511 | 0.003983 | 151,522 | 1.75 MB | Low | Implemented Benchmark |
| `track2f_bis_clean_sequential_residual_offset_global` | `te_track2f_bis_clean_residual_offset_global` | `sequential_residual_offset_probe` | 0.003717 | 0.003528 | 0.004010 | 92,802 | 1.09 MB | Low | Implemented Benchmark |
| `residual_harmonic_gru_sequence_dense360` | `te_residual_harmonic_gru_sequence_remote_global_dense360` | `residual_harmonic_gru_sequence` | 0.003628 | 0.003535 | 0.003999 | 151,762 | 1.75 MB | Medium | Implemented Benchmark |
| `sequential_residual_offset_probe` | `te_sequential_residual_offset_probe_remote_global` | `sequential_residual_offset_probe` | 0.003783 | 0.003537 | 0.004005 | 92,802 | 1.09 MB | Low | Implemented Benchmark |
| `track2f_bis_harmonic_residual_offset_global` | `te_track2f_bis_harmonic_residual_offset_global` | `harmonic_residual_offset_probe` | 0.003659 | 0.003538 | 0.003932 | 85,747 | 1.00 MB | Very Low | Implemented Benchmark |
| `track2h_mixture_density_heads_mdn_k3_global` | `te_track2h_mdn_k3_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003617 | 0.003564 | 0.003986 | 87,435 | 1.02 MB | Medium | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_pointwise_control_global` | `te_track2g_curve_aware_pointwise_control_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003607 | 0.003587 | 0.004001 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `gru_sequence` | `te_gru_sequence_remote_global` | `gru_sequence` | 0.003707 | 0.003591 | 0.004110 | 151,041 | 1.74 MB | Low | Implemented Benchmark |
| `temporal_convolution` | `te_temporal_convolution_sequence_remote_global` | `temporal_convolution` | 0.003935 | 0.003754 | 0.004266 | 147,009 | 1.70 MB | Low | Implemented Benchmark |
| `harmonic_regression_global` | `te_harmonic_regression_global` | `harmonic_regression` | 0.003879 | 0.003795 | 0.004515 | 125 | N/A | Unknown | Implemented Benchmark |
| `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.003904 | 0.003839 | 0.004555 | 125 | 0.01 MB | Low | Active Improvement |
| `feedforward_recovery_micro` | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004266 | 0.004164 | 0.005109 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |
| `feedforward_recovery_probe_dense` | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004257 | 0.004602 | 0.005262 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |

### Forward Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `periodic_gru_sequence_fw` | `te_periodic_gru_sequence_fw` | `periodic_gru_sequence` | 0.001099 | 0.001101 | 0.001409 | 157,569 | N/A | Unknown | Implemented Benchmark |
| `periodic_mlp_harmonic_fw` | `te_periodic_mlp_harmonic_fw` | `periodic_mlp` | 0.001144 | 0.001326 | 0.001780 | 28,417 | N/A | Unknown | Implemented Benchmark |
| `periodic_lstm_sequence_fw` | `te_periodic_lstm_sequence_fw` | `periodic_lstm_sequence` | 0.001495 | 0.001547 | 0.001976 | 210,049 | N/A | Unknown | Implemented Benchmark |
| `feedforward_fw` | `te_feedforward_fw` | `feedforward` | 0.001628 | 0.001726 | 0.002205 | 109,697 | N/A | Unknown | Implemented Benchmark |
| `periodic_mlp_fw` | `te_periodic_mlp_fw` | `periodic_mlp` | 0.001597 | 0.001742 | 0.002329 | 27,137 | N/A | Unknown | Implemented Benchmark |
| `tree_fw` | `te_tree_fw` | `hist_gradient_boosting` | 0.001591 | 0.001753 | 0.002892 | 4 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_mlp_fw` | `te_residual_harmonic_mlp_fw` | `residual_harmonic_mlp` | 0.001647 | 0.001808 | 0.002420 | 26,138 | N/A | Unknown | Implemented Benchmark |
| `periodic_temporal_convolution_fw` | `te_periodic_temporal_convolution_fw` | `periodic_temporal_convolution` | 0.002065 | 0.002178 | 0.002730 | 157,889 | N/A | Unknown | Implemented Benchmark |
| `gru_sequence_fw` | `te_gru_sequence_fw` | `gru_sequence` | 0.002156 | 0.002260 | 0.002905 | 150,657 | N/A | Unknown | Implemented Benchmark |
| `lstm_sequence_fw` | `te_lstm_sequence_fw` | `lstm_sequence` | 0.002151 | 0.002266 | 0.002915 | 200,833 | N/A | Unknown | Implemented Benchmark |
| `temporal_convolution_fw` | `te_temporal_convolution_fw` | `temporal_convolution` | 0.002311 | 0.002399 | 0.003061 | 146,369 | N/A | Unknown | Implemented Benchmark |
| `track2f_bis_harmonic_residual_offset_fw` | `te_track2f_bis_harmonic_residual_offset_fw` | `harmonic_residual_offset_probe` | 0.002941 | 0.002862 | 0.003334 | 85,747 | 1.00 MB | Very Low | Implemented Benchmark |
| `harmonic_regression_fw` | `te_harmonic_dense360_tracking_Fw` | `harmonic_regression` | 0.002610 | 0.002916 | 0.003237 | 4,326 | 0.06 MB | Low | Implemented Benchmark |
| `track2h_dispersion_aware_mae_robust_fw` | `te_track2h_mae_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003258 | 0.003146 | 0.003527 | 85,747 | 1.00 MB | Low | Implemented Benchmark |
| `track2h_quantile_probabilistic_gaussian_nll_fw` | `te_track2h_gaussian_nll_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003293 | 0.003165 | 0.003548 | 85,958 | 1.00 MB | Low | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw` | `te_track2g_curve_aware_raw_centered_shape_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003251 | 0.003181 | 0.003571 | 85,747 | 1.00 MB | Low | Implemented Benchmark |
| `residual_harmonic_gru_sequence_fw_sparse_rcim` | `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003309 | 0.003200 | 0.003635 | 151,060 | 1.75 MB | Low | Implemented Benchmark |
| `residual_harmonic_gru_sequence_fw_dense240` | `te_residual_harmonic_gru_sequence_remote_Fw_dense240` | `residual_harmonic_gru_sequence` | 0.003270 | 0.003219 | 0.003653 | 151,522 | 1.75 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_fw_sparse_rcim` | `te_residual_harmonic_lstm_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003344 | 0.003234 | 0.003679 | 201,364 | 2.32 MB | Low | Implemented Benchmark |
| `track2h_mixture_density_heads_mdn_k3_fw` | `te_track2h_mdn_k3_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003253 | 0.003235 | 0.003613 | 87,435 | 1.02 MB | Low | Implemented Benchmark |
| `residual_harmonic_gru_sequence_fw_dense360` | `te_residual_harmonic_gru_sequence_remote_Fw_dense360` | `residual_harmonic_gru_sequence` | 0.003265 | 0.003241 | 0.003677 | 151,762 | 1.75 MB | Low | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw` | `te_track2g_curve_aware_full_curve_composite_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003320 | 0.003260 | 0.003630 | 85,747 | 1.00 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_fw_dense240` | `te_residual_harmonic_lstm_sequence_remote_Fw_dense240` | `residual_harmonic_lstm_sequence` | 0.003307 | 0.003262 | 0.003706 | 201,826 | 2.33 MB | Low | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_raw_offset_fw` | `te_track2g_curve_aware_raw_offset_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003328 | 0.003279 | 0.003698 | 85,747 | 1.00 MB | Low | Implemented Benchmark |
| `track2h_quantile_probabilistic_quantile_p10_p50_p90_fw` | `te_track2h_quantile_p10_p50_p90_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003269 | 0.003285 | 0.003668 | 86,169 | 1.01 MB | Low | Implemented Benchmark |
| `track2h_dispersion_aware_smooth_l1_robust_fw` | `te_track2h_smooth_l1_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003235 | 0.003314 | 0.003679 | 85,747 | 1.00 MB | Low | Implemented Benchmark |
| `track2h_mixture_density_heads_mdn_k2_fw` | `te_track2h_mdn_k2_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003285 | 0.003339 | 0.003721 | 86,802 | 1.01 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_fw_dense360` | `te_residual_harmonic_lstm_sequence_remote_Fw_dense360` | `residual_harmonic_lstm_sequence` | 0.003302 | 0.003351 | 0.003774 | 202,066 | 2.33 MB | Low | Implemented Benchmark |
| `track2h_dispersion_aware_log_cosh_robust_fw` | `te_track2h_log_cosh_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003280 | 0.003355 | 0.003708 | 85,747 | 1.00 MB | Low | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw` | `te_track2g_curve_aware_pointwise_control_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003291 | 0.003371 | 0.003763 | 85,747 | 1.00 MB | Low | Implemented Benchmark |
| `wave3_harmonic_prior_residual_pointwise_control_fw` | `te_wave3_harmonic_prior_residual_pointwise_control_fw` | `wave3_harmonic_prior_residual` | 0.003315 | 0.003382 | 0.003779 | 7,283 | 0.11 MB | Low | Implemented Benchmark |
| `sequential_residual_offset_probe_fw` | `te_sequential_residual_offset_probe_remote_fw` | `sequential_residual_offset_probe` | 0.003380 | 0.003385 | 0.003931 | 92,802 | 1.09 MB | Low | Implemented Benchmark |
| `track2f_bis_clean_sequential_residual_offset_fw` | `te_track2f_bis_clean_residual_offset_fw` | `sequential_residual_offset_probe` | 0.003474 | 0.003446 | 0.003972 | 92,802 | 1.09 MB | Low | Implemented Benchmark |
| `track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw` | `te_track2h_l_causal_tcn_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.003565 | 0.003470 | 0.004068 | 97,923 | 1.17 MB | Low | Implemented Benchmark |
| `wave3_harmonic_prior_residual_smooth_l1_structured_fw` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_fw` | `wave3_harmonic_prior_residual` | 0.003310 | 0.003527 | 0.003900 | 7,283 | 0.11 MB | Low | Implemented Benchmark |
| `track2h_latent_state_hysteresis_gru_offset_residual_fw` | `te_track2h_l_gru_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.003468 | 0.003537 | 0.004110 | 125,475 | 1.48 MB | Low | Implemented Benchmark |

### Backward Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `periodic_gru_sequence_bw` | `te_periodic_gru_sequence_bw` | `periodic_gru_sequence` | 0.001088 | 0.001084 | 0.001393 | 157,569 | N/A | Unknown | Current Program Winner |
| `periodic_mlp_harmonic_bw` | `te_periodic_mlp_harmonic_bw` | `periodic_mlp` | 0.001103 | 0.001279 | 0.001719 | 28,417 | N/A | Unknown | Implemented Benchmark |
| `periodic_lstm_sequence_bw` | `te_periodic_lstm_sequence_bw` | `periodic_lstm_sequence` | 0.001231 | 0.001338 | 0.001719 | 210,049 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_mlp_bw` | `te_residual_harmonic_mlp_bw` | `residual_harmonic_mlp` | 0.001609 | 0.001712 | 0.002294 | 26,138 | N/A | Unknown | Implemented Benchmark |
| `feedforward_bw` | `te_feedforward_bw` | `feedforward` | 0.001606 | 0.001719 | 0.002205 | 109,697 | N/A | Unknown | Implemented Benchmark |
| `tree_bw` | `te_tree_bw` | `hist_gradient_boosting` | 0.001591 | 0.001753 | 0.002892 | 4 | N/A | Unknown | Implemented Benchmark |
| `periodic_mlp_bw` | `te_periodic_mlp_bw` | `periodic_mlp` | 0.001611 | 0.001758 | 0.002334 | 27,137 | N/A | Unknown | Implemented Benchmark |
| `periodic_temporal_convolution_bw` | `te_periodic_temporal_convolution_bw` | `periodic_temporal_convolution` | 0.002161 | 0.002238 | 0.002791 | 157,889 | N/A | Unknown | Implemented Benchmark |
| `lstm_sequence_bw` | `te_lstm_sequence_bw` | `lstm_sequence` | 0.002151 | 0.002240 | 0.002892 | 200,833 | N/A | Unknown | Implemented Benchmark |
| `gru_sequence_bw` | `te_gru_sequence_bw` | `gru_sequence` | 0.002147 | 0.002271 | 0.002908 | 150,657 | N/A | Unknown | Implemented Benchmark |
| `temporal_convolution_bw` | `te_temporal_convolution_bw` | `temporal_convolution` | 0.002303 | 0.002391 | 0.003044 | 146,369 | N/A | Unknown | Implemented Benchmark |
| `track2h_mixture_density_heads_mdn_k2_bw` | `te_track2h_mdn_k2_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002914 | 0.002658 | 0.003198 | 86,802 | 1.01 MB | Medium | Implemented Benchmark |
| `track2h_mixture_density_heads_mdn_k3_bw` | `te_track2h_mdn_k3_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002775 | 0.002721 | 0.003250 | 87,435 | 1.02 MB | Medium | Implemented Benchmark |
| `track2h_quantile_probabilistic_quantile_p10_p50_p90_bw` | `te_track2h_quantile_p10_p50_p90_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003436 | 0.002927 | 0.003519 | 86,169 | 1.01 MB | Medium | Implemented Benchmark |
| `track2h_quantile_probabilistic_gaussian_nll_bw` | `te_track2h_gaussian_nll_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003298 | 0.002998 | 0.003608 | 85,958 | 1.00 MB | Medium | Implemented Benchmark |
| `track2h_dispersion_aware_smooth_l1_robust_bw` | `te_track2h_smooth_l1_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003372 | 0.003074 | 0.003662 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `track2f_bis_harmonic_residual_offset_bw` | `te_track2f_bis_harmonic_residual_offset_bw` | `harmonic_residual_offset_probe` | 0.003555 | 0.003336 | 0.003935 | 85,747 | 1.00 MB | Very Low | Implemented Benchmark |
| `wave3_harmonic_prior_residual_pointwise_control_bw` | `te_wave3_harmonic_prior_residual_pointwise_control_bw` | `wave3_harmonic_prior_residual` | 0.003634 | 0.003363 | 0.003902 | 7,283 | 0.11 MB | Low | Implemented Benchmark |
| `harmonic_regression_bw` | `te_harmonic_dense240_tracking_Bw` | `harmonic_regression` | 0.003588 | 0.003400 | 0.003886 | 2,886 | 0.04 MB | Low | Implemented Benchmark |
| `track2h_dispersion_aware_mae_robust_bw` | `te_track2h_mae_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003579 | 0.003430 | 0.004029 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw` | `te_track2g_curve_aware_pointwise_control_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003749 | 0.003430 | 0.003945 | 85,747 | 1.00 MB | Low | Implemented Benchmark |
| `wave3_harmonic_prior_residual_smooth_l1_structured_bw` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_bw` | `wave3_harmonic_prior_residual` | 0.003644 | 0.003431 | 0.003953 | 7,283 | 0.11 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_bw_sparse_rcim` | `te_residual_harmonic_lstm_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003764 | 0.003440 | 0.004030 | 201,364 | 2.32 MB | Low | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw` | `te_track2g_curve_aware_raw_centered_shape_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003740 | 0.003465 | 0.003998 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `residual_harmonic_gru_sequence_bw_dense360` | `te_residual_harmonic_gru_sequence_remote_Bw_dense360` | `residual_harmonic_gru_sequence` | 0.003773 | 0.003468 | 0.004050 | 151,762 | 1.75 MB | Low | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_raw_offset_bw` | `te_track2g_curve_aware_raw_offset_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003751 | 0.003471 | 0.003992 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `track2h_dispersion_aware_log_cosh_robust_bw` | `te_track2h_log_cosh_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003774 | 0.003481 | 0.004029 | 85,747 | 1.00 MB | Low | Implemented Benchmark |
| `residual_harmonic_gru_sequence_bw_dense240` | `te_residual_harmonic_gru_sequence_remote_Bw_dense240` | `residual_harmonic_gru_sequence` | 0.003585 | 0.003492 | 0.004074 | 151,522 | 1.75 MB | Medium | Implemented Benchmark |
| `residual_harmonic_gru_sequence_bw_sparse_rcim` | `te_residual_harmonic_gru_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003833 | 0.003502 | 0.004061 | 151,060 | 1.75 MB | Low | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw` | `te_track2g_curve_aware_full_curve_composite_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003803 | 0.003511 | 0.004113 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `track2f_bis_clean_sequential_residual_offset_bw` | `te_track2f_bis_clean_residual_offset_bw` | `sequential_residual_offset_probe` | 0.003820 | 0.003540 | 0.004203 | 92,802 | 1.09 MB | Low | Implemented Benchmark |
| `track2h_latent_state_hysteresis_gru_offset_residual_bw` | `te_track2h_l_gru_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.003837 | 0.003545 | 0.004175 | 125,475 | 1.48 MB | Low | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_bw_dense360` | `te_residual_harmonic_lstm_sequence_remote_Bw_dense360` | `residual_harmonic_lstm_sequence` | 0.003729 | 0.003556 | 0.004125 | 202,066 | 2.33 MB | Medium | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_bw_dense240` | `te_residual_harmonic_lstm_sequence_remote_Bw_dense240` | `residual_harmonic_lstm_sequence` | 0.003742 | 0.003605 | 0.004129 | 201,826 | 2.33 MB | Low | Implemented Benchmark |
| `track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw` | `te_track2h_l_causal_tcn_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.003840 | 0.003630 | 0.004312 | 97,923 | 1.17 MB | Low | Implemented Benchmark |
| `sequential_residual_offset_probe_bw` | `te_sequential_residual_offset_probe_remote_bw` | `sequential_residual_offset_probe` | 0.003840 | 0.003638 | 0.004280 | 92,802 | 1.09 MB | Low | Implemented Benchmark |

## Cross-Family Interpretation

- Current program-registry winner: `te_periodic_gru_sequence_bw` from family `periodic_gru_sequence_bw`.
- Strongest current neural family: `periodic_gru_sequence_bw`.
- Current plain-MLP comparison anchor: `te_feedforward_trial`.
- Predictive quality and deployment suitability must stay separate: the best leaderboard entry is not automatically the best TwinCAT/PLC candidate.
- Large tree artifacts should be treated cautiously even when tree-based accuracy remains strong, because model weight and memory footprint can dominate deployment feasibility.

## Paper Reference Benchmark

The repository benchmark paper is `reference/RCIM_ML-compensation.pdf`.
At the current repository state, the comparison is explicitly `offline-only`. A real paper-equivalent comparison still requires repository-owned online compensation tests.

### Extracted Paper Targets

- Paper dataset size: `1026` operating-condition samples.
- Paper input axes: `input speed`, `applied torque`, `oil temperature`.
- Offline prediction target: TE-curve mean percentage error at or below `4.7%` on unseen validation scenarios.
- Online `robot` compensation target: at least `83.6%` TE RMS reduction.
- Online `cycloidal` compensation target: at least `94.0%` TE RMS reduction and `91.7%` TE max reduction.
- Paper compensation harmonics baseline: `0, 1, 39` with additional checks on `40, 78`.

### Paper Vs Repository

| Comparison Item | Paper Reference | Repository Status | Current Verdict |
| --- | --- | --- | --- |
| Offline model-selection direction | Boosting/tree-heavy deployed harmonic predictors | Current winner `te_periodic_gru_sequence_bw` from family `periodic_gru_sequence_bw` with model type `periodic_gru_sequence` | not_aligned |
| Strongest neural branch role | Neural models are evaluated, but not the primary deployed winners | Strongest repository neural family is `periodic_gru_sequence_bw` and still trails the tree winner | aligned |
| RCIM Model-Bank Reproduction canonical closure rule | Paper Tables `3-6` replicated per target and per harmonic | Exact-paper report currently shows `0/0` harmonics fully closed, `0/0` partially closed, `0/0` still open | not_yet_met |
| Supporting harmonic-wise TE metric | Mean percentage error over full TE curves | Latest harmonic-wise validation reports `11.212%` mean percentage error on held-out curves using harmonics `0, 1, 3, 39, 40, 78, 81, 156, 162, 240` | supporting_only_not_yet_met |
| Online robot-profile compensation | TE RMS reduction `83.6%` | No repository-owned online compensation result yet | not_yet_comparable |
| Online cycloidal-profile compensation | TE RMS reduction `94.0%`, TE max reduction `91.7%` | No repository-owned online compensation result yet | not_yet_comparable |
| Table 9-style end-to-end benchmark | PLC-integrated motion-profile compensation benchmark | Missing in the repository at the current state | not_yet_comparable |

### RCIM Model-Bank Reproduction Canonical Status

- Latest exact-paper validation summary: `N/A`
- Table `3` amplitude `RMSE`: `0/0` harmonics at or below the paper target
- Table `4` phase `MAE`: `0/0` harmonics at or below the paper target
- Table `5` phase `RMSE`: `0/0` harmonics at or below the paper target
- Target-level expected-family direction: `0/0`
- Harmonic-level Table `6` closure: `0/0` fully matched, `0/0` partially matched, `0/0` still open
- Highest-priority open harmonics: `N/A`

### Latest Harmonic-Wise Validation Support

- Latest harmonic-wise validation summary: `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/family_exploration/rf/2026-04-13-16-00-30__track1_rf_h039_h162240_bridge_control_campaign_run/validation_summary.yaml`
- Harmonic-wise test mean percentage error: `11.212%`
- `Target A` status from the latest harmonic-wise run: `not_yet_met`

### Online Compensation Tracking Placeholder

- Repository online compensation status: `not yet available`.
- When online compensation tests are implemented, update this master summary with TE RMS, TE max, and reduction percentages for both robot and cycloidal motion profiles.
- Until those tests exist, present the paper comparison as `offline-only` rather than end-to-end equivalent.

### Gap Summary

- `RCIM Model-Bank Reproduction` remains open primarily because the canonical Tables `3-6` are not yet fully matched.
- Offline benchmark scope remains `partially comparable` rather than like-for-like.
- Not yet aligned: the current repository winner is not tree-based, while the paper deployment path is dominated by boosting/tree models.
- Neural models remain secondary in the repository (`periodic_gru_sequence_bw`), which is also consistent with the paper not promoting a plain neural winner for deployment.
- End-to-end paper comparison remains `not yet comparable` until repository-owned online compensation tests exist.

## Family-By-Family Result Breakdowns

- For multi-scope waves, family breakdowns are grouped by canonical reporting scope before the per-family ranking tables.

### Global Models

#### feedforward_recovery_micro

- Best run: `te_feedforward_optuna_recovery_micro_global_optuna_t0000`
- Best test MAE: `0.004164`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004164 | 0.005109 | 0.004266 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |

#### feedforward_recovery_probe_dense

- Best run: `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000`
- Best test MAE: `0.004602`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004602 | 0.005262 | 0.004257 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |

#### gru_sequence

- Best run: `te_gru_sequence_remote_global`
- Best test MAE: `0.003591`
- Completed tracked runs: `4`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_gru_sequence_global` | `gru_sequence` | 0.002229 | 0.002872 | 0.002126 | 150,657 | 56m 28s | 1.74 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_gru_sequence_fw` | `gru_sequence` | 0.002260 | 0.002905 | 0.002156 | 150,657 | 35m 12s | 1.74 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_gru_sequence_bw` | `gru_sequence` | 0.002271 | 0.002908 | 0.002147 | 150,657 | 42m 04s | 1.74 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_gru_sequence_remote_global` | `gru_sequence` | 0.003591 | 0.004110 | 0.003707 | 151,041 | 8m 44s | 1.74 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### harmonic_regression

- Best run: `te_harmonic_order12_linear_conditioned_recovery_global`
- Best test MAE: `0.003839`
- Completed tracked runs: `10`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_regression_global` | `harmonic_regression` | 0.003795 | 0.004515 | 0.003879 | 125 | 23m 12s | 0.01 MB | Very Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_harmonic_regression_fw` | `harmonic_regression` | 0.003806 | 0.004524 | 0.003887 | 125 | 15m 42s | 0.01 MB | Very Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_harmonic_regression_bw` | `harmonic_regression` | 0.003811 | 0.004529 | 0.003888 | 125 | 19m 57s | 0.01 MB | Very Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.003839 | 0.004555 | 0.003904 | 125 | 11m 27s | 0.01 MB | Very Low | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 5 | `te_harmonic_rcim_sparse_tracking_global` | `harmonic_regression` | 0.020767 | 0.022376 | 0.016995 | 114 | 6m 17s | 0.01 MB | Very Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 6 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.020774 | 0.022412 | 0.017025 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 7 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr0001_stride1` | `harmonic_regression` | 0.020775 | 0.022417 | 0.017013 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 8 | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.020779 | 0.022403 | 0.017017 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 9 | `te_harmonic_dense360_tracking_global` | `harmonic_regression` | 0.020780 | 0.022399 | 0.016991 | 4,326 | 8m 57s | 0.06 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 10 | `te_harmonic_dense240_tracking_global` | `harmonic_regression` | 0.020787 | 0.022388 | 0.016989 | 2,886 | 6m 02s | 0.04 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |

#### periodic_lstm_sequence

- Best run: `te_periodic_lstm_sequence_remote_global`
- Best test MAE: `0.002682`
- Completed tracked runs: `4`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_lstm_sequence_global` | `periodic_lstm_sequence` | 0.001187 | 0.001505 | 0.001185 | 210,049 | 1h 27m 51s | 2.42 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_periodic_lstm_sequence_bw` | `periodic_lstm_sequence` | 0.001338 | 0.001719 | 0.001231 | 210,049 | 1h 14m 57s | 2.42 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_periodic_lstm_sequence_fw` | `periodic_lstm_sequence` | 0.001547 | 0.001976 | 0.001495 | 210,049 | 59m 17s | 2.42 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_periodic_lstm_sequence_remote_global` | `periodic_lstm_sequence` | 0.002682 | 0.002969 | 0.002526 | 210,561 | 1h 11m 12s | 2.43 MB | Very High | High | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### periodic_mlp_harmonic

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_harmonic_global` | `periodic_mlp` | 0.001264 | 0.001737 | 0.001196 | 28,417 | 42m 19s | 0.35 MB | Medium | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_periodic_mlp_harmonic_bw` | `periodic_mlp` | 0.001279 | 0.001719 | 0.001103 | 28,417 | 39m 46s | 0.35 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_periodic_mlp_harmonic_fw` | `periodic_mlp` | 0.001326 | 0.001780 | 0.001144 | 28,417 | 38m 01s | 0.35 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |

#### residual_harmonic_gru_sequence_dense240

- Best run: `te_residual_harmonic_gru_sequence_remote_global_dense240`
- Best test MAE: `0.003511`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_global_dense240` | `residual_harmonic_gru_sequence` | 0.003511 | 0.003983 | 0.003600 | 151,522 | 13m 21s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_dense360

- Best run: `te_residual_harmonic_gru_sequence_remote_global_dense360`
- Best test MAE: `0.003535`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_global_dense360` | `residual_harmonic_gru_sequence` | 0.003535 | 0.003999 | 0.003628 | 151,762 | 21m 39s | 1.75 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_sparse_rcim

- Best run: `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim`
- Best test MAE: `0.002112`
- Completed tracked runs: `2`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.002112 | 0.002699 | 0.001978 | 150,676 | 24m 21s | 1.74 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |
| 2 | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003440 | 0.003848 | 0.003607 | 151,060 | 11m 44s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_dense240

- Best run: `te_residual_harmonic_lstm_sequence_remote_global_dense240`
- Best test MAE: `0.003473`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_global_dense240` | `residual_harmonic_lstm_sequence` | 0.003473 | 0.003925 | 0.003624 | 201,826 | 13m 54s | 2.33 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_dense360

- Best run: `te_residual_harmonic_lstm_sequence_remote_global_dense360`
- Best test MAE: `0.003477`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_global_dense360` | `residual_harmonic_lstm_sequence` | 0.003477 | 0.003940 | 0.003648 | 202,066 | 28m 49s | 2.33 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_sparse_rcim

- Best run: `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim`
- Best test MAE: `0.003368`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003368 | 0.003808 | 0.003632 | 201,364 | 9m 32s | 2.32 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### sequential_residual_offset_probe

- Best run: `te_sequential_residual_offset_probe_remote_global`
- Best test MAE: `0.003537`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_sequential_residual_offset_probe_remote_global` | `sequential_residual_offset_probe` | 0.003537 | 0.004005 | 0.003783 | 92,802 | 9m 22s | 1.09 MB | High | Low | `track2f_offset_aware_probe_campaign_2026_06_03` |

#### track2f_bis_clean_sequential_residual_offset_global

- Best run: `te_track2f_bis_clean_residual_offset_global`
- Best test MAE: `0.003528`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2f_bis_clean_residual_offset_global` | `sequential_residual_offset_probe` | 0.003528 | 0.004010 | 0.003717 | 92,802 | 11m 40s | 1.09 MB | High | Low | `track2f_bis_harmonic_offset_probe_campaign_2026_06_04` |

#### track2f_bis_harmonic_residual_offset_global

- Best run: `te_track2f_bis_harmonic_residual_offset_global`
- Best test MAE: `0.003538`
- Completed tracked runs: `1`
- Known failed campaign attempts: `1`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2f_bis_harmonic_residual_offset_global` | `harmonic_residual_offset_probe` | 0.003538 | 0.003932 | 0.003659 | 85,747 | 0s | 1.00 MB | High | Very Low | `track2f_bis_harmonic_offset_probe_campaign_2026_06_04` |

Known failed campaign attempts for this family:

- `te_track2f_bis_harmonic_residual_offset_global` | campaign `track2f_bis_harmonic_offset_probe_campaign_2026_06_04` | model type `harmonic_residual_offset_probe` | error `Unsupported Model Type for Campaign Runner | harmonic_residual_offset_probe | Supported: ['feedforward', 'gru_sequence', 'harmonic_regression', 'hist_gradient_boosting', 'lstm_sequence', 'periodic_gru_sequence', 'periodic_lstm_sequence', 'periodic_mlp', 'periodic_temporal_convolution', 'random_forest', 'residual_harmonic_gru_sequence', 'residual_harmonic_lstm_sequence', 'residual_harmonic_mlp', 'sequential_residual_offset_probe', 'temporal_convolution']`

#### track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global

- Best run: `te_track2g_curve_aware_full_curve_composite_global`
- Best test MAE: `0.002008`
- Completed tracked runs: `2`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | 0.002008 | 0.002581 | 0.001872 | 85,440 | 44m 57s | 1.00 MB | High | High | `track2g_curve_aware_training_campaign_2026_06_08` |
| 2 | `te_track2g_curve_aware_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003345 | 0.003713 | 0.003616 | 85,747 | 32m 15s | 1.00 MB | High | Medium | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2g_curve_aware_harmonic_residual_offset_pointwise_control_global

- Best run: `te_track2g_curve_aware_pointwise_control_global`
- Best test MAE: `0.003587`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_pointwise_control_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003587 | 0.004001 | 0.003607 | 85,747 | 20m 29s | 1.00 MB | High | Medium | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_global

- Best run: `te_track2g_curve_aware_raw_centered_shape_global`
- Best test MAE: `0.003350`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_raw_centered_shape_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003350 | 0.003753 | 0.003636 | 85,747 | 22m 08s | 1.00 MB | High | Medium | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2g_curve_aware_harmonic_residual_offset_raw_offset_global

- Best run: `te_track2g_curve_aware_raw_offset_global`
- Best test MAE: `0.003465`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_raw_offset_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003465 | 0.003829 | 0.003564 | 85,747 | 32m 11s | 1.00 MB | High | Medium | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2h_dispersion_aware_log_cosh_robust_global

- Best run: `te_track2h_log_cosh_robust_global`
- Best test MAE: `0.003505`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_log_cosh_robust_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003505 | 0.003935 | 0.003645 | 85,747 | 18m 16s | 1.00 MB | High | Medium | `track2h_dispersion_aware_modeling_campaign_2026_06_10` |

#### track2h_dispersion_aware_mae_robust_global

- Best run: `te_track2h_mae_robust_global`
- Best test MAE: `0.003406`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_mae_robust_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003406 | 0.003807 | 0.003645 | 85,747 | 16m 33s | 1.00 MB | High | Medium | `track2h_dispersion_aware_modeling_campaign_2026_06_10` |

#### track2h_dispersion_aware_smooth_l1_robust_global

- Best run: `te_track2h_smooth_l1_robust_global`
- Best test MAE: `0.003422`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_smooth_l1_robust_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003422 | 0.003810 | 0.003641 | 85,747 | 15m 30s | 1.00 MB | High | Medium | `track2h_dispersion_aware_modeling_campaign_2026_06_10` |

#### track2h_latent_state_hysteresis_causal_tcn_offset_residual_global

- Best run: `te_track2h_l_causal_tcn_offset_residual_global`
- Best test MAE: `0.003368`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_l_causal_tcn_offset_residual_global` | `latent_state_hysteresis_probe` | 0.003368 | 0.003860 | 0.003543 | 97,923 | 28m 35s | 1.17 MB | High | Medium | `track2h_latent_state_hysteresis_campaign_2026_06_16` |

#### track2h_latent_state_hysteresis_gru_offset_residual_global

- Best run: `te_track2h_l_gru_offset_residual_global`
- Best test MAE: `0.002339`
- Completed tracked runs: `2`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_l_gru_offset_residual_global` | `latent_state_hysteresis_probe` | 0.002339 | 0.002986 | 0.002232 | 124,899 | 23m 03s | 1.48 MB | High | Medium | `track2h_latent_state_hysteresis_campaign_2026_06_16` |
| 2 | `te_track2h_l_gru_offset_residual_global` | `latent_state_hysteresis_probe` | 0.003590 | 0.004074 | 0.003717 | 125,475 | 17m 28s | 1.48 MB | High | Medium | `track2h_latent_state_hysteresis_campaign_2026_06_16` |

#### track2h_mixture_density_heads_mdn_k2_global

- Best run: `te_track2h_mdn_k2_global`
- Best test MAE: `0.003503`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_mdn_k2_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003503 | 0.003938 | 0.003654 | 86,802 | 20m 19s | 1.01 MB | High | Medium | `track2h_mixture_density_heads_campaign_2026_06_13` |

#### track2h_mixture_density_heads_mdn_k3_global

- Best run: `te_track2h_mdn_k3_global`
- Best test MAE: `0.003564`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_mdn_k3_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003564 | 0.003986 | 0.003617 | 87,435 | 20m 24s | 1.02 MB | High | Medium | `track2h_mixture_density_heads_campaign_2026_06_13` |

#### track2h_quantile_probabilistic_gaussian_nll_global

- Best run: `te_track2h_gaussian_nll_global`
- Best test MAE: `0.003013`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_gaussian_nll_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003013 | 0.003388 | 0.003267 | 85,958 | 1h 02m 12s | 1.00 MB | High | High | `track2h_quantile_probabilistic_campaign_2026_06_12` |

#### track2h_quantile_probabilistic_quantile_p10_p50_p90_global

- Best run: `te_track2h_quantile_p10_p50_p90_global`
- Best test MAE: `0.003383`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_quantile_p10_p50_p90_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003383 | 0.003764 | 0.003606 | 86,169 | 18m 38s | 1.01 MB | High | Medium | `track2h_quantile_probabilistic_campaign_2026_06_12` |

#### tree

- Best run: `te_hist_gbr_tabular_global`
- Best test MAE: `0.001753`
- Completed tracked runs: `7`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_global` | `hist_gradient_boosting` | 0.001753 | 0.002892 | 0.001591 | 4 | 1m 53s | 0.44 MB | Light Artifact | Very Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 2 | `te_tree_global` | `hist_gradient_boosting` | 0.001753 | 0.002892 | 0.001591 | 4 | 3m 00s | 0.44 MB | Light Artifact | Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_tree_fw` | `hist_gradient_boosting` | 0.001753 | 0.002892 | 0.001591 | 4 | 2m 29s | 0.44 MB | Light Artifact | Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_tree_bw` | `hist_gradient_boosting` | 0.001753 | 0.002892 | 0.001591 | 4 | 2m 24s | 0.44 MB | Light Artifact | Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.002782 | 0.003520 | 0.002655 | 5 | N/A | 0.48 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 6 | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf20` | `hist_gradient_boosting` | 0.002782 | 0.003520 | 0.002655 | 5 | N/A | 0.48 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 7 | `te_hist_gbr_tabular_global_grid_depth8_lr008_leaf10` | `hist_gradient_boosting` | 0.002830 | 0.003585 | 0.002677 | 5 | N/A | 0.50 MB | Light Artifact | Unknown | `standalone_or_unknown` |

#### wave3_harmonic_prior_residual_pointwise_control_global

- Best run: `te_wave3_harmonic_prior_residual_pointwise_control_global`
- Best test MAE: `0.003451`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_harmonic_prior_residual_pointwise_control_global` | `wave3_harmonic_prior_residual` | 0.003451 | 0.003851 | 0.003611 | 7,283 | 26m 08s | 0.11 MB | Low | Medium | `wave3_harmonic_prior_residual_campaign_2026_06_14` |

#### wave3_harmonic_prior_residual_smooth_l1_structured_global

- Best run: `te_wave3_harmonic_prior_residual_smooth_l1_structured_global`
- Best test MAE: `0.002168`
- Completed tracked runs: `2`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | 0.002168 | 0.002763 | 0.001889 | 7,168 | 21m 31s | 0.10 MB | Low | Medium | `wave3_harmonic_prior_residual_campaign_2026_06_14` |
| 2 | `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | 0.003403 | 0.003785 | 0.003633 | 7,283 | 19m 38s | 0.11 MB | Low | Medium | `wave3_harmonic_prior_residual_campaign_2026_06_14` |

### Forward Models

#### feedforward_fw

- Best run: `te_feedforward_fw`
- Best test MAE: `0.001726`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0008` | `feedforward` | 0.003203 | 0.003787 | 0.002850 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 2 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0009` | `feedforward` | 0.003229 | 0.003774 | 0.002850 | 143,745 | N/A | 1.67 MB | High | Unknown | `standalone_or_unknown` |
| 3 | `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0014` | `feedforward` | 0.003232 | 0.003812 | 0.002846 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |

#### gru_sequence_fw

- Best run: `te_gru_sequence_fw`
- Best test MAE: `0.002260`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_gru_sequence_remote_Fw` | `gru_sequence` | 0.003333 | 0.003881 | 0.003409 | 151,041 | 6m 01s | 1.74 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### harmonic_regression_fw

- Best run: `te_harmonic_dense360_tracking_Fw`
- Best test MAE: `0.002916`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_dense360_tracking_Fw` | `harmonic_regression` | 0.002916 | 0.003237 | 0.002610 | 4,326 | 7m 00s | 0.06 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 2 | `te_harmonic_dense240_tracking_Fw` | `harmonic_regression` | 0.002935 | 0.003239 | 0.002593 | 2,886 | 5m 56s | 0.04 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 3 | `te_harmonic_rcim_sparse_tracking_Fw` | `harmonic_regression` | 0.002943 | 0.003254 | 0.002566 | 114 | 5m 05s | 0.01 MB | Very Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 4 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr00005_stride5` | `harmonic_regression` | 0.003101 | 0.003527 | 0.002848 | 102 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 5 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.003102 | 0.003528 | 0.002843 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 6 | `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr00005_stride1` | `harmonic_regression` | 0.003105 | 0.003534 | 0.002839 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |

#### lstm_sequence_fw

- Best run: `te_lstm_sequence_fw`
- Best test MAE: `0.002266`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_lstm_sequence_remote_Fw` | `lstm_sequence` | 0.003370 | 0.003921 | 0.003448 | 201,345 | 4m 31s | 2.32 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### periodic_gru_sequence_fw

- Best run: `te_periodic_gru_sequence_fw`
- Best test MAE: `0.001101`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_gru_sequence_remote_Fw` | `periodic_gru_sequence` | 0.003193 | 0.003583 | 0.003227 | 157,953 | 11m 11s | 1.82 MB | Very High | Low | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### periodic_lstm_sequence_fw

- Best run: `te_periodic_lstm_sequence_fw`
- Best test MAE: `0.001547`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_lstm_sequence_remote_Fw` | `periodic_lstm_sequence` | 0.003274 | 0.003651 | 0.003254 | 210,561 | 9m 20s | 2.43 MB | Very High | Low | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### periodic_mlp

- Best run: `te_periodic_mlp_h04_standard_global_optuna_t0010`
- Best test MAE: `0.003186`
- Completed tracked runs: `9`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_fw` | `periodic_mlp` | 0.001742 | 0.002329 | 0.001597 | 27,137 | 43m 55s | 0.33 MB | Medium | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_periodic_mlp_bw` | `periodic_mlp` | 0.001758 | 0.002334 | 0.001611 | 27,137 | 40m 10s | 0.33 MB | Medium | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_periodic_mlp_global` | `periodic_mlp` | 0.001774 | 0.002355 | 0.001634 | 27,137 | 29m 56s | 0.33 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.003186 | 0.003690 | 0.002994 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_periodic_mlp_h04_standard_global_optuna_t0008` | `periodic_mlp` | 0.003200 | 0.003798 | 0.003057 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |
| 6 | `te_periodic_mlp_h04_standard_global_optuna_t0006` | `periodic_mlp` | 0.003233 | 0.003733 | 0.002964 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 7 | `te_periodic_mlp_rcim_sparse_tracking_global` | `periodic_mlp` | 0.003275 | 0.003726 | 0.002863 | 28,545 | 7h 47m 34s | 0.35 MB | Medium | Very High | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 8 | `te_periodic_mlp_dense240_tracking_global` | `periodic_mlp` | 0.003348 | 0.003862 | 0.002962 | 87,681 | 20m 22s | 1.03 MB | High | Medium | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 9 | `te_periodic_mlp_dense360_tracking_global` | `periodic_mlp` | 0.003401 | 0.003831 | 0.002859 | 118,401 | 50m 45s | 1.38 MB | High | High | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |

#### periodic_mlp_fw

- Best run: `te_periodic_mlp_fw`
- Best test MAE: `0.001742`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_dense240_tracking_Fw` | `periodic_mlp` | 0.003055 | 0.003537 | 0.002541 | 87,681 | 13m 21s | 1.03 MB | High | Low | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 2 | `te_periodic_mlp_rcim_sparse_tracking_Fw` | `periodic_mlp` | 0.003131 | 0.003578 | 0.002516 | 28,545 | 9m 28s | 0.35 MB | Medium | Low | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 3 | `te_periodic_mlp_dense360_tracking_Fw` | `periodic_mlp` | 0.003155 | 0.003680 | 0.002524 | 118,401 | 12m 15s | 1.38 MB | High | Low | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 4 | `te_periodic_mlp_h04_standard_Fw_optuna_t0008` | `periodic_mlp` | 0.003287 | 0.003833 | 0.002809 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_periodic_mlp_h04_standard_Fw_optuna_t0001` | `periodic_mlp` | 0.003294 | 0.003899 | 0.002751 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 6 | `te_periodic_mlp_h04_standard_Fw_optuna_t0015` | `periodic_mlp` | 0.003296 | 0.003924 | 0.002802 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |

#### periodic_temporal_convolution

- Best run: `te_periodic_temporal_convolution_sequence_remote_global`
- Best test MAE: `0.003508`
- Completed tracked runs: `4`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_temporal_convolution_fw` | `periodic_temporal_convolution` | 0.002178 | 0.002730 | 0.002065 | 157,889 | 31m 41s | 1.82 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_periodic_temporal_convolution_bw` | `periodic_temporal_convolution` | 0.002238 | 0.002791 | 0.002161 | 157,889 | 27m 06s | 1.82 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_periodic_temporal_convolution_global` | `periodic_temporal_convolution` | 0.002319 | 0.002900 | 0.002202 | 157,889 | 22m 15s | 1.82 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_periodic_temporal_convolution_sequence_remote_global` | `periodic_temporal_convolution` | 0.003508 | 0.003929 | 0.003634 | 158,529 | 25m 37s | 1.83 MB | Very High | Medium | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### periodic_temporal_convolution_fw

- Best run: `te_periodic_temporal_convolution_fw`
- Best test MAE: `0.002178`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_temporal_convolution_sequence_remote_Fw` | `periodic_temporal_convolution` | 0.003337 | 0.003830 | 0.003321 | 158,529 | 8m 15s | 1.83 MB | Very High | Low | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### residual_harmonic_gru_sequence_fw_dense240

- Best run: `te_residual_harmonic_gru_sequence_remote_Fw_dense240`
- Best test MAE: `0.003219`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Fw_dense240` | `residual_harmonic_gru_sequence` | 0.003219 | 0.003653 | 0.003270 | 151,522 | 8m 13s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_fw_dense360

- Best run: `te_residual_harmonic_gru_sequence_remote_Fw_dense360`
- Best test MAE: `0.003241`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Fw_dense360` | `residual_harmonic_gru_sequence` | 0.003241 | 0.003677 | 0.003265 | 151,762 | 11m 14s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_fw_sparse_rcim

- Best run: `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim`
- Best test MAE: `0.003200`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003200 | 0.003635 | 0.003309 | 151,060 | 5m 07s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_fw_dense240

- Best run: `te_residual_harmonic_lstm_sequence_remote_Fw_dense240`
- Best test MAE: `0.003262`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Fw_dense240` | `residual_harmonic_lstm_sequence` | 0.003262 | 0.003706 | 0.003307 | 201,826 | 7m 24s | 2.33 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_fw_dense360

- Best run: `te_residual_harmonic_lstm_sequence_remote_Fw_dense360`
- Best test MAE: `0.003351`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Fw_dense360` | `residual_harmonic_lstm_sequence` | 0.003351 | 0.003774 | 0.003302 | 202,066 | 10m 20s | 2.33 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_fw_sparse_rcim

- Best run: `te_residual_harmonic_lstm_sequence_remote_Fw_sparse_rcim`
- Best test MAE: `0.003234`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Fw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003234 | 0.003679 | 0.003344 | 201,364 | 4m 50s | 2.32 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_mlp_fw

- Best run: `te_residual_harmonic_mlp_fw`
- Best test MAE: `0.001808`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_rcim_sparse_tracking_Fw` | `residual_harmonic_mlp` | 0.003089 | 0.003498 | 0.002704 | 26,260 | 4m 56s | 0.32 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 2 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0005` | `residual_harmonic_mlp` | 0.003168 | 0.003871 | 0.002870 | 34,978 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0006` | `residual_harmonic_mlp` | 0.003194 | 0.003809 | 0.002827 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_residual_h12_deep_joint_wave1_Fw_optuna_t0009` | `residual_harmonic_mlp` | 0.003211 | 0.003828 | 0.002794 | 34,970 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_residual_harmonic_dense240_tracking_Fw` | `residual_harmonic_mlp` | 0.003304 | 0.003773 | 0.002649 | 26,722 | 5m 04s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 6 | `te_residual_harmonic_dense360_tracking_Fw` | `residual_harmonic_mlp` | 0.003568 | 0.004118 | 0.002598 | 26,962 | 6m 12s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |

#### sequential_residual_offset_probe_fw

- Best run: `te_sequential_residual_offset_probe_remote_fw`
- Best test MAE: `0.003385`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_sequential_residual_offset_probe_remote_fw` | `sequential_residual_offset_probe` | 0.003385 | 0.003931 | 0.003380 | 92,802 | 12m 09s | 1.09 MB | High | Low | `track2f_offset_aware_probe_campaign_2026_06_03` |

#### temporal_convolution_fw

- Best run: `te_temporal_convolution_fw`
- Best test MAE: `0.002399`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_temporal_convolution_sequence_remote_Fw` | `temporal_convolution` | 0.003611 | 0.004183 | 0.003490 | 147,009 | 6m 45s | 1.70 MB | High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### track2f_bis_clean_sequential_residual_offset_fw

- Best run: `te_track2f_bis_clean_residual_offset_fw`
- Best test MAE: `0.003446`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2f_bis_clean_residual_offset_fw` | `sequential_residual_offset_probe` | 0.003446 | 0.003972 | 0.003474 | 92,802 | 5m 16s | 1.09 MB | High | Low | `track2f_bis_harmonic_offset_probe_campaign_2026_06_04` |

#### track2f_bis_harmonic_residual_offset_fw

- Best run: `te_track2f_bis_harmonic_residual_offset_fw`
- Best test MAE: `0.002862`
- Completed tracked runs: `1`
- Known failed campaign attempts: `1`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2f_bis_harmonic_residual_offset_fw` | `harmonic_residual_offset_probe` | 0.002862 | 0.003334 | 0.002941 | 85,747 | 0s | 1.00 MB | High | Very Low | `track2f_bis_harmonic_offset_probe_campaign_2026_06_04` |

Known failed campaign attempts for this family:

- `te_track2f_bis_harmonic_residual_offset_fw` | campaign `track2f_bis_harmonic_offset_probe_campaign_2026_06_04` | model type `harmonic_residual_offset_probe` | error `Unsupported Model Type for Campaign Runner | harmonic_residual_offset_probe | Supported: ['feedforward', 'gru_sequence', 'harmonic_regression', 'hist_gradient_boosting', 'lstm_sequence', 'periodic_gru_sequence', 'periodic_lstm_sequence', 'periodic_mlp', 'periodic_temporal_convolution', 'random_forest', 'residual_harmonic_gru_sequence', 'residual_harmonic_lstm_sequence', 'residual_harmonic_mlp', 'sequential_residual_offset_probe', 'temporal_convolution']`

#### track2g_curve_aware_harmonic_residual_offset_full_curve_composite_fw

- Best run: `te_track2g_curve_aware_full_curve_composite_fw`
- Best test MAE: `0.003260`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_full_curve_composite_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003260 | 0.003630 | 0.003320 | 85,747 | 10m 35s | 1.00 MB | High | Low | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2g_curve_aware_harmonic_residual_offset_pointwise_control_fw

- Best run: `te_track2g_curve_aware_pointwise_control_fw`
- Best test MAE: `0.003371`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_pointwise_control_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003371 | 0.003763 | 0.003291 | 85,747 | 11m 40s | 1.00 MB | High | Low | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_fw

- Best run: `te_track2g_curve_aware_raw_centered_shape_fw`
- Best test MAE: `0.003181`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_raw_centered_shape_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003181 | 0.003571 | 0.003251 | 85,747 | 10m 48s | 1.00 MB | High | Low | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2g_curve_aware_harmonic_residual_offset_raw_offset_fw

- Best run: `te_track2g_curve_aware_raw_offset_fw`
- Best test MAE: `0.003279`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_raw_offset_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003279 | 0.003698 | 0.003328 | 85,747 | 7m 42s | 1.00 MB | High | Low | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2h_dispersion_aware_log_cosh_robust_fw

- Best run: `te_track2h_log_cosh_robust_fw`
- Best test MAE: `0.003355`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_log_cosh_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003355 | 0.003708 | 0.003280 | 85,747 | 7m 56s | 1.00 MB | High | Low | `track2h_dispersion_aware_modeling_campaign_2026_06_10` |

#### track2h_dispersion_aware_mae_robust_fw

- Best run: `te_track2h_mae_robust_fw`
- Best test MAE: `0.003146`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_mae_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003146 | 0.003527 | 0.003258 | 85,747 | 7m 09s | 1.00 MB | High | Low | `track2h_dispersion_aware_modeling_campaign_2026_06_10` |

#### track2h_dispersion_aware_smooth_l1_robust_fw

- Best run: `te_track2h_smooth_l1_robust_fw`
- Best test MAE: `0.003314`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_smooth_l1_robust_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003314 | 0.003679 | 0.003235 | 85,747 | 7m 42s | 1.00 MB | High | Low | `track2h_dispersion_aware_modeling_campaign_2026_06_10` |

#### track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw

- Best run: `te_track2h_l_causal_tcn_offset_residual_fw`
- Best test MAE: `0.003470`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_l_causal_tcn_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.003470 | 0.004068 | 0.003565 | 97,923 | 5m 24s | 1.17 MB | High | Low | `track2h_latent_state_hysteresis_campaign_2026_06_16` |

#### track2h_latent_state_hysteresis_gru_offset_residual_fw

- Best run: `te_track2h_l_gru_offset_residual_fw`
- Best test MAE: `0.003537`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_l_gru_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.003537 | 0.004110 | 0.003468 | 125,475 | 10m 34s | 1.48 MB | High | Low | `track2h_latent_state_hysteresis_campaign_2026_06_16` |

#### track2h_mixture_density_heads_mdn_k2_fw

- Best run: `te_track2h_mdn_k2_fw`
- Best test MAE: `0.003339`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_mdn_k2_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003339 | 0.003721 | 0.003285 | 86,802 | 9m 01s | 1.01 MB | High | Low | `track2h_mixture_density_heads_campaign_2026_06_13` |

#### track2h_mixture_density_heads_mdn_k3_fw

- Best run: `te_track2h_mdn_k3_fw`
- Best test MAE: `0.003235`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_mdn_k3_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003235 | 0.003613 | 0.003253 | 87,435 | 8m 40s | 1.02 MB | High | Low | `track2h_mixture_density_heads_campaign_2026_06_13` |

#### track2h_quantile_probabilistic_gaussian_nll_fw

- Best run: `te_track2h_gaussian_nll_fw`
- Best test MAE: `0.003165`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_gaussian_nll_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003165 | 0.003548 | 0.003293 | 85,958 | 13m 18s | 1.00 MB | High | Low | `track2h_quantile_probabilistic_campaign_2026_06_12` |

#### track2h_quantile_probabilistic_quantile_p10_p50_p90_fw

- Best run: `te_track2h_quantile_p10_p50_p90_fw`
- Best test MAE: `0.003285`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_quantile_p10_p50_p90_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.003285 | 0.003668 | 0.003269 | 86,169 | 8m 53s | 1.01 MB | High | Low | `track2h_quantile_probabilistic_campaign_2026_06_12` |

#### tree_fw

- Best run: `te_tree_fw`
- Best test MAE: `0.001753`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002743 | 0.003409 | 0.002677 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 2 | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf20` | `hist_gradient_boosting` | 0.002743 | 0.003409 | 0.002677 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 3 | `te_hist_gbr_tabular_Fw` | `hist_gradient_boosting` | 0.002845 | 0.003476 | 0.002666 | 5 | N/A | 0.50 MB | Very Low | Unknown | `standalone_or_unknown` |

#### wave3_harmonic_prior_residual_pointwise_control_fw

- Best run: `te_wave3_harmonic_prior_residual_pointwise_control_fw`
- Best test MAE: `0.003382`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_harmonic_prior_residual_pointwise_control_fw` | `wave3_harmonic_prior_residual` | 0.003382 | 0.003779 | 0.003315 | 7,283 | 7m 10s | 0.11 MB | Low | Low | `wave3_harmonic_prior_residual_campaign_2026_06_14` |

#### wave3_harmonic_prior_residual_smooth_l1_structured_fw

- Best run: `te_wave3_harmonic_prior_residual_smooth_l1_structured_fw`
- Best test MAE: `0.003527`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_harmonic_prior_residual_smooth_l1_structured_fw` | `wave3_harmonic_prior_residual` | 0.003527 | 0.003900 | 0.003310 | 7,283 | 7m 28s | 0.11 MB | Low | Low | `wave3_harmonic_prior_residual_campaign_2026_06_14` |

### Backward Models

#### feedforward

- Best run: `te_feedforward_trial`
- Best test MAE: `0.002877`
- Completed tracked runs: `7`
- Known failed campaign attempts: `1`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_bw` | `feedforward` | 0.001719 | 0.002205 | 0.001606 | 109,697 | 3h 19m 34s | 1.28 MB | High | Very High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_feedforward_fw` | `feedforward` | 0.001726 | 0.002205 | 0.001628 | 109,697 | 1h 44m 25s | 1.28 MB | High | Very High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_feedforward_global` | `feedforward` | 0.001734 | 0.002220 | 0.001637 | 109,697 | 2h 35m 35s | 1.28 MB | High | Very High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_feedforward_trial` | `feedforward` | 0.002877 | 0.003835 | 0.002725 | 26,113 | 3m 27s | 0.32 MB | Medium | Low | `polished_dataset_stage1_smoke_2026_06_21` |
| 5 | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003150 | 0.003603 | 0.003056 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 6 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0017` | `feedforward` | 0.003208 | 0.003810 | 0.002962 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 7 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0012` | `feedforward` | 0.003217 | 0.003847 | 0.003014 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |

Known failed campaign attempts for this family:

- `te_feedforward_trial` | campaign `polished_dataset_stage1_smoke_2026_06_21` | model type `feedforward` | error `invalid literal for int() with base 10: 'auto'`

#### feedforward_bw

- Best run: `te_feedforward_bw`
- Best test MAE: `0.001719`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005` | `feedforward` | 0.003099 | 0.003630 | 0.003018 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 2 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0013` | `feedforward` | 0.003106 | 0.003700 | 0.002989 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 3 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0016` | `feedforward` | 0.003173 | 0.003818 | 0.002901 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |

#### gru_sequence_bw

- Best run: `te_gru_sequence_bw`
- Best test MAE: `0.002271`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_gru_sequence_remote_Bw` | `gru_sequence` | 0.003631 | 0.004297 | 0.003867 | 151,041 | 6m 29s | 1.74 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### harmonic_regression_bw

- Best run: `te_harmonic_dense240_tracking_Bw`
- Best test MAE: `0.003400`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_dense240_tracking_Bw` | `harmonic_regression` | 0.003400 | 0.003886 | 0.003588 | 2,886 | 5m 00s | 0.04 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 2 | `te_harmonic_dense360_tracking_Bw` | `harmonic_regression` | 0.003403 | 0.003866 | 0.003637 | 4,326 | 6m 43s | 0.06 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 3 | `te_harmonic_rcim_sparse_tracking_Bw` | `harmonic_regression` | 0.003406 | 0.003894 | 0.003570 | 114 | 5m 56s | 0.01 MB | Very Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 4 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0002_stride5` | `harmonic_regression` | 0.003494 | 0.004081 | 0.003638 | 102 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 5 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr00005_stride1` | `harmonic_regression` | 0.003497 | 0.004053 | 0.003743 | 102 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 6 | `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.003506 | 0.004063 | 0.003729 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |

#### lstm_sequence

- Best run: `te_lstm_sequence_remote_global`
- Best test MAE: `0.003482`
- Completed tracked runs: `4`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_lstm_sequence_bw` | `lstm_sequence` | 0.002240 | 0.002892 | 0.002151 | 200,833 | 50m 56s | 2.31 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_lstm_sequence_global` | `lstm_sequence` | 0.002258 | 0.002894 | 0.002151 | 200,833 | 52m 04s | 2.31 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_lstm_sequence_fw` | `lstm_sequence` | 0.002266 | 0.002915 | 0.002151 | 200,833 | 47m 50s | 2.31 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_lstm_sequence_remote_global` | `lstm_sequence` | 0.003482 | 0.003948 | 0.003681 | 201,345 | 9m 56s | 2.32 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### lstm_sequence_bw

- Best run: `te_lstm_sequence_bw`
- Best test MAE: `0.002240`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_lstm_sequence_remote_Bw` | `lstm_sequence` | 0.003557 | 0.004201 | 0.003815 | 201,345 | 6m 29s | 2.32 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### periodic_gru_sequence

- Best run: `te_periodic_gru_sequence_remote_global`
- Best test MAE: `0.001279`
- Completed tracked runs: `5`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_gru_sequence_bw` | `periodic_gru_sequence` | 0.001084 | 0.001393 | 0.001088 | 157,569 | 1h 21m 37s | 1.82 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_periodic_gru_sequence_fw` | `periodic_gru_sequence` | 0.001101 | 0.001409 | 0.001099 | 157,569 | 1h 20m 41s | 1.82 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_periodic_gru_sequence_global` | `periodic_gru_sequence` | 0.001257 | 0.001613 | 0.001252 | 157,569 | 1h 02m 53s | 1.82 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | 0.001279 | 0.001638 | 0.001274 | 157,569 | 40m 03s | 1.82 MB | Very High | High | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |
| 5 | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | 0.002681 | 0.002971 | 0.002507 | 157,953 | 1h 00m 14s | 1.82 MB | Very High | High | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### periodic_gru_sequence_bw

- Best run: `te_periodic_gru_sequence_bw`
- Best test MAE: `0.001084`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_gru_sequence_remote_Bw` | `periodic_gru_sequence` | 0.002344 | 0.002747 | 0.002523 | 157,953 | 31m 26s | 1.82 MB | Very High | Medium | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### periodic_lstm_sequence_bw

- Best run: `te_periodic_lstm_sequence_bw`
- Best test MAE: `0.001338`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_lstm_sequence_remote_Bw` | `periodic_lstm_sequence` | 0.002556 | 0.002953 | 0.002432 | 210,561 | 35m 21s | 2.43 MB | Very High | Medium | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### periodic_mlp_bw

- Best run: `te_periodic_mlp_bw`
- Best test MAE: `0.001758`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_h04_standard_Bw_optuna_t0006` | `periodic_mlp` | 0.003233 | 0.003792 | 0.002907 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 2 | `te_periodic_mlp_h04_standard_Bw_optuna_t0007` | `periodic_mlp` | 0.003239 | 0.003820 | 0.002933 | 28,289 | N/A | 0.35 MB | Medium | Unknown | `standalone_or_unknown` |
| 3 | `te_periodic_mlp_h04_standard_Bw_optuna_t0010` | `periodic_mlp` | 0.003248 | 0.003817 | 0.002963 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_periodic_mlp_rcim_sparse_tracking_Bw` | `periodic_mlp` | 0.003398 | 0.003922 | 0.003011 | 28,545 | 9m 57s | 0.35 MB | Medium | Low | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 5 | `te_periodic_mlp_dense240_tracking_Bw` | `periodic_mlp` | 0.003417 | 0.004005 | 0.003041 | 87,681 | 20m 05s | 1.03 MB | High | Medium | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 6 | `te_periodic_mlp_dense360_tracking_Bw` | `periodic_mlp` | 0.003424 | 0.004006 | 0.003072 | 118,401 | 20m 33s | 1.38 MB | High | Medium | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |

#### periodic_temporal_convolution_bw

- Best run: `te_periodic_temporal_convolution_bw`
- Best test MAE: `0.002238`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_temporal_convolution_sequence_remote_Bw` | `periodic_temporal_convolution` | 0.003614 | 0.004163 | 0.003890 | 158,529 | 8m 25s | 1.83 MB | Very High | Low | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### residual_harmonic_gru_sequence_bw_dense240

- Best run: `te_residual_harmonic_gru_sequence_remote_Bw_dense240`
- Best test MAE: `0.003492`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Bw_dense240` | `residual_harmonic_gru_sequence` | 0.003492 | 0.004074 | 0.003585 | 151,522 | 19m 40s | 1.75 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_bw_dense360

- Best run: `te_residual_harmonic_gru_sequence_remote_Bw_dense360`
- Best test MAE: `0.003468`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Bw_dense360` | `residual_harmonic_gru_sequence` | 0.003468 | 0.004050 | 0.003773 | 151,762 | 13m 22s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_bw_sparse_rcim

- Best run: `te_residual_harmonic_gru_sequence_remote_Bw_sparse_rcim`
- Best test MAE: `0.003502`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003502 | 0.004061 | 0.003833 | 151,060 | 6m 18s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_bw_dense240

- Best run: `te_residual_harmonic_lstm_sequence_remote_Bw_dense240`
- Best test MAE: `0.003605`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Bw_dense240` | `residual_harmonic_lstm_sequence` | 0.003605 | 0.004129 | 0.003742 | 201,826 | 10m 18s | 2.33 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_bw_dense360

- Best run: `te_residual_harmonic_lstm_sequence_remote_Bw_dense360`
- Best test MAE: `0.003556`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Bw_dense360` | `residual_harmonic_lstm_sequence` | 0.003556 | 0.004125 | 0.003729 | 202,066 | 15m 59s | 2.33 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_bw_sparse_rcim

- Best run: `te_residual_harmonic_lstm_sequence_remote_Bw_sparse_rcim`
- Best test MAE: `0.003440`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_remote_Bw_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003440 | 0.004030 | 0.003764 | 201,364 | 7m 48s | 2.32 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_mlp

- Best run: `te_residual_h12_deep_joint_wave1_global_optuna_t0006`
- Best test MAE: `0.003034`
- Completed tracked runs: `9`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_mlp_bw` | `residual_harmonic_mlp` | 0.001712 | 0.002294 | 0.001609 | 26,138 | 40m 41s | 0.32 MB | Medium | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_residual_harmonic_mlp_fw` | `residual_harmonic_mlp` | 0.001808 | 0.002420 | 0.001647 | 26,138 | 24m 31s | 0.32 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_residual_harmonic_mlp_global` | `residual_harmonic_mlp` | 0.001841 | 0.002433 | 0.001660 | 26,138 | 33m 07s | 0.32 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.003034 | 0.003550 | 0.002895 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_residual_h12_deep_joint_wave1_global_optuna_t0010` | `residual_harmonic_mlp` | 0.003067 | 0.003568 | 0.002903 | 26,258 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 6 | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | 0.003152 | 0.003640 | 0.003024 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 7 | `te_residual_harmonic_dense240_tracking_global` | `residual_harmonic_mlp` | 0.003162 | 0.003598 | 0.002976 | 26,722 | 11m 07s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 8 | `te_residual_harmonic_rcim_sparse_tracking_global` | `residual_harmonic_mlp` | 0.003378 | 0.003902 | 0.002969 | 26,260 | 8m 03s | 0.32 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 9 | `te_residual_harmonic_dense360_tracking_global` | `residual_harmonic_mlp` | 0.003434 | 0.003957 | 0.002943 | 26,962 | 13m 52s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |

#### residual_harmonic_mlp_bw

- Best run: `te_residual_harmonic_mlp_bw`
- Best test MAE: `0.001712`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_rcim_sparse_tracking_Bw` | `residual_harmonic_mlp` | 0.003042 | 0.003548 | 0.002953 | 26,260 | 6m 07s | 0.32 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 2 | `te_residual_harmonic_dense360_tracking_Bw` | `residual_harmonic_mlp` | 0.003068 | 0.003545 | 0.002826 | 26,962 | 14m 01s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 3 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0007` | `residual_harmonic_mlp` | 0.003162 | 0.003862 | 0.002948 | 34,962 | N/A | 0.42 MB | Medium | Unknown | `standalone_or_unknown` |
| 4 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0012` | `residual_harmonic_mlp` | 0.003180 | 0.003642 | 0.002979 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 5 | `te_residual_harmonic_dense240_tracking_Bw` | `residual_harmonic_mlp` | 0.003188 | 0.003717 | 0.002861 | 26,722 | 8m 25s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 6 | `te_residual_h12_deep_joint_wave1_Bw_optuna_t0013` | `residual_harmonic_mlp` | 0.003195 | 0.003636 | 0.003051 | 43,026 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |

#### sequential_residual_offset_probe_bw

- Best run: `te_sequential_residual_offset_probe_remote_bw`
- Best test MAE: `0.003638`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_sequential_residual_offset_probe_remote_bw` | `sequential_residual_offset_probe` | 0.003638 | 0.004280 | 0.003840 | 92,802 | 7m 07s | 1.09 MB | High | Low | `track2f_offset_aware_probe_campaign_2026_06_03` |

#### temporal_convolution

- Best run: `te_temporal_convolution_sequence_remote_global`
- Best test MAE: `0.003754`
- Completed tracked runs: `4`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_temporal_convolution_bw` | `temporal_convolution` | 0.002391 | 0.003044 | 0.002303 | 146,369 | 33m 57s | 1.69 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_temporal_convolution_fw` | `temporal_convolution` | 0.002399 | 0.003061 | 0.002311 | 146,369 | 33m 25s | 1.69 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_temporal_convolution_global` | `temporal_convolution` | 0.002411 | 0.003063 | 0.002308 | 146,369 | 29m 33s | 1.69 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_temporal_convolution_sequence_remote_global` | `temporal_convolution` | 0.003754 | 0.004266 | 0.003935 | 147,009 | 9m 46s | 1.70 MB | High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### temporal_convolution_bw

- Best run: `te_temporal_convolution_bw`
- Best test MAE: `0.002391`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_temporal_convolution_sequence_remote_Bw` | `temporal_convolution` | 0.003739 | 0.004369 | 0.003933 | 147,009 | 8m 12s | 1.70 MB | High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### track2f_bis_clean_sequential_residual_offset_bw

- Best run: `te_track2f_bis_clean_residual_offset_bw`
- Best test MAE: `0.003540`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2f_bis_clean_residual_offset_bw` | `sequential_residual_offset_probe` | 0.003540 | 0.004203 | 0.003820 | 92,802 | 9m 37s | 1.09 MB | High | Low | `track2f_bis_harmonic_offset_probe_campaign_2026_06_04` |

#### track2f_bis_harmonic_residual_offset_bw

- Best run: `te_track2f_bis_harmonic_residual_offset_bw`
- Best test MAE: `0.003336`
- Completed tracked runs: `1`
- Known failed campaign attempts: `1`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2f_bis_harmonic_residual_offset_bw` | `harmonic_residual_offset_probe` | 0.003336 | 0.003935 | 0.003555 | 85,747 | 0s | 1.00 MB | High | Very Low | `track2f_bis_harmonic_offset_probe_campaign_2026_06_04` |

Known failed campaign attempts for this family:

- `te_track2f_bis_harmonic_residual_offset_bw` | campaign `track2f_bis_harmonic_offset_probe_campaign_2026_06_04` | model type `harmonic_residual_offset_probe` | error `Unsupported Model Type for Campaign Runner | harmonic_residual_offset_probe | Supported: ['feedforward', 'gru_sequence', 'harmonic_regression', 'hist_gradient_boosting', 'lstm_sequence', 'periodic_gru_sequence', 'periodic_lstm_sequence', 'periodic_mlp', 'periodic_temporal_convolution', 'random_forest', 'residual_harmonic_gru_sequence', 'residual_harmonic_lstm_sequence', 'residual_harmonic_mlp', 'sequential_residual_offset_probe', 'temporal_convolution']`

#### track2g_curve_aware_harmonic_residual_offset_full_curve_composite_bw

- Best run: `te_track2g_curve_aware_full_curve_composite_bw`
- Best test MAE: `0.003511`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_full_curve_composite_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003511 | 0.004113 | 0.003803 | 85,747 | 15m 23s | 1.00 MB | High | Medium | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2g_curve_aware_harmonic_residual_offset_pointwise_control_bw

- Best run: `te_track2g_curve_aware_pointwise_control_bw`
- Best test MAE: `0.003430`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_pointwise_control_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003430 | 0.003945 | 0.003749 | 85,747 | 14m 29s | 1.00 MB | High | Low | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2g_curve_aware_harmonic_residual_offset_raw_centered_shape_bw

- Best run: `te_track2g_curve_aware_raw_centered_shape_bw`
- Best test MAE: `0.003465`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_raw_centered_shape_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003465 | 0.003998 | 0.003740 | 85,747 | 15m 37s | 1.00 MB | High | Medium | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2g_curve_aware_harmonic_residual_offset_raw_offset_bw

- Best run: `te_track2g_curve_aware_raw_offset_bw`
- Best test MAE: `0.003471`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2g_curve_aware_raw_offset_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003471 | 0.003992 | 0.003751 | 85,747 | 15m 22s | 1.00 MB | High | Medium | `track2g_curve_aware_training_campaign_2026_06_08` |

#### track2h_dispersion_aware_log_cosh_robust_bw

- Best run: `te_track2h_log_cosh_robust_bw`
- Best test MAE: `0.003481`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_log_cosh_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003481 | 0.004029 | 0.003774 | 85,747 | 10m 56s | 1.00 MB | High | Low | `track2h_dispersion_aware_modeling_campaign_2026_06_10` |

#### track2h_dispersion_aware_mae_robust_bw

- Best run: `te_track2h_mae_robust_bw`
- Best test MAE: `0.003430`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_mae_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003430 | 0.004029 | 0.003579 | 85,747 | 18m 22s | 1.00 MB | High | Medium | `track2h_dispersion_aware_modeling_campaign_2026_06_10` |

#### track2h_dispersion_aware_smooth_l1_robust_bw

- Best run: `te_track2h_smooth_l1_robust_bw`
- Best test MAE: `0.003074`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_smooth_l1_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003074 | 0.003662 | 0.003372 | 85,747 | 28m 21s | 1.00 MB | High | Medium | `track2h_dispersion_aware_modeling_campaign_2026_06_10` |

#### track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw

- Best run: `te_track2h_l_causal_tcn_offset_residual_bw`
- Best test MAE: `0.003630`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_l_causal_tcn_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.003630 | 0.004312 | 0.003840 | 97,923 | 11m 52s | 1.17 MB | High | Low | `track2h_latent_state_hysteresis_campaign_2026_06_16` |

#### track2h_latent_state_hysteresis_gru_offset_residual_bw

- Best run: `te_track2h_l_gru_offset_residual_bw`
- Best test MAE: `0.003545`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_l_gru_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.003545 | 0.004175 | 0.003837 | 125,475 | 14m 01s | 1.48 MB | High | Low | `track2h_latent_state_hysteresis_campaign_2026_06_16` |

#### track2h_mixture_density_heads_mdn_k2_bw

- Best run: `te_track2h_mdn_k2_bw`
- Best test MAE: `0.002658`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_mdn_k2_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002658 | 0.003198 | 0.002914 | 86,802 | 33m 06s | 1.01 MB | High | Medium | `track2h_mixture_density_heads_campaign_2026_06_13` |

#### track2h_mixture_density_heads_mdn_k3_bw

- Best run: `te_track2h_mdn_k3_bw`
- Best test MAE: `0.002721`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_mdn_k3_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002721 | 0.003250 | 0.002775 | 87,435 | 26m 49s | 1.02 MB | High | Medium | `track2h_mixture_density_heads_campaign_2026_06_13` |

#### track2h_quantile_probabilistic_gaussian_nll_bw

- Best run: `te_track2h_gaussian_nll_bw`
- Best test MAE: `0.002998`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_gaussian_nll_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002998 | 0.003608 | 0.003298 | 85,958 | 27m 33s | 1.00 MB | High | Medium | `track2h_quantile_probabilistic_campaign_2026_06_12` |

#### track2h_quantile_probabilistic_quantile_p10_p50_p90_bw

- Best run: `te_track2h_quantile_p10_p50_p90_bw`
- Best test MAE: `0.002927`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_track2h_quantile_p10_p50_p90_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002927 | 0.003519 | 0.003436 | 86,169 | 26m 33s | 1.01 MB | High | Medium | `track2h_quantile_probabilistic_campaign_2026_06_12` |

#### tree_bw

- Best run: `te_tree_bw`
- Best test MAE: `0.001753`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002954 | 0.003749 | 0.002681 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 2 | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf20` | `hist_gradient_boosting` | 0.002954 | 0.003749 | 0.002681 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 3 | `te_hist_gbr_tabular_Bw_grid_depth8_lr008_leaf10` | `hist_gradient_boosting` | 0.003002 | 0.003809 | 0.002650 | 5 | N/A | 0.44 MB | Very Low | Unknown | `standalone_or_unknown` |

#### wave3_harmonic_prior_residual_pointwise_control_bw

- Best run: `te_wave3_harmonic_prior_residual_pointwise_control_bw`
- Best test MAE: `0.003363`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_harmonic_prior_residual_pointwise_control_bw` | `wave3_harmonic_prior_residual` | 0.003363 | 0.003902 | 0.003634 | 7,283 | 14m 45s | 0.11 MB | Low | Low | `wave3_harmonic_prior_residual_campaign_2026_06_14` |

#### wave3_harmonic_prior_residual_smooth_l1_structured_bw

- Best run: `te_wave3_harmonic_prior_residual_smooth_l1_structured_bw`
- Best test MAE: `0.003431`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_harmonic_prior_residual_smooth_l1_structured_bw` | `wave3_harmonic_prior_residual` | 0.003431 | 0.003953 | 0.003644 | 7,283 | 13m 56s | 0.11 MB | Low | Low | `wave3_harmonic_prior_residual_campaign_2026_06_14` |

## Source Of Truth

- Live backlog: `doc/running/te_model_live_backlog.md`
- Active campaign state: `doc/running/active_training_campaign.yaml`
- Program registry: `output/registries/program/current_best_solution.yaml`
- Family registries root: `output/registries/families`
- Training campaign root: `output/training_campaigns`
- Training run root: `output/training_runs`
- Paper reference report: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

This document is repository-generated. Regenerate it after new campaign results so the cross-family snapshot stays aligned with the canonical registries and campaign artifacts.
