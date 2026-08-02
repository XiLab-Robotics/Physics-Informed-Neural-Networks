# Training Results Master Summary

## Executive Snapshot

- Generated At: `2026-08-02T17:15:58+02:00`
- Program State: active.
- Current Completed Wave: polished-dataset RCIM, early-wave, and full-wave
- Current Focus: parallel PLC qualification and the approval-gated integrated-specialist roadmap.
- Active Campaign Status: `completed`
- Active Campaign Name: `wave52r_offline_leader_cross_surface_promotion_2026_07_30`
- Current Program Winner: `te_periodic_gru_sequence_bw` | Family `periodic_gru_sequence_bw` | Test MAE `0.001084`

## Main Takeaways

- Strongest current neural family: `periodic_gru_sequence_bw`
- Current plain MLP anchor: `te_feedforward_trial`
- Active family-improvement branch count: `0`
- Implemented and benchmarked family count: `254`
- Wave 5.2R progress: all `16 / 16` stages and the subsequent full-candidate
  forward verification are complete. The `98`-candidate, `97`-curve matrix
  identifies K01 as the temporal offline leader and H08 as the balanced
  non-temporal offline leader. The accepted periodic GRU and periodic harmonic
  MLP remain the deployment references. K01 and H08 have passed local replay,
  causal/state, export-parity, fallback, and host-latency gates. The approved
  `Fw`/`Bw`/`global` campaign completed `27 / 27` runs with zero failures; K01
  led mean scalar MAE on every surface. The subsequent official multi-index
  refresh promoted K01 as the cross-surface temporal offline leader. H08
  remains a forward non-temporal specialist because it regressed raw error and
  offset on `Bw` and `global`. Both non-PINN incumbents remain accepted and
  unchanged; K01 TwinCAT runtime checks remain pending. The curated polished
  setpoint archive now preserves K01 seed `271828` on all three surfaces, H08
  seed `161803` on `Fw`, and exploratory Stage 15 H04 on `Fw`. This archive
  update does not change the accepted registries or deployment leaders. The
  subsequent frozen-payload H08 diagnostic confirms that the backward defect
  is offset-dominant and that the combined global formulation is worse than
  the corresponding directional H08 specialists on both directions. H08
  therefore remains forward-only, and its current global formulation is an
  explicit exclusion and ablation control for the next integrated-specialist
  roadmap.

## Current Project Status

### Implemented And Benchmarked Families

- Multi-scope waves must keep `global`, `Fw`, and `Bw` reporting surfaces separated in this canonical summary.

#### Global Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `periodic_gru_sequence_global` | Implemented Benchmark | `te_periodic_gru_sequence_global` | `periodic_gru_sequence` | 0.001159 | 157,569 | `2026-07-09 00:29:12` |
| `periodic_lstm_sequence_global` | Implemented Benchmark | `te_periodic_lstm_sequence_global` | `periodic_lstm_sequence` | 0.001187 | 210,049 | `2026-07-09 05:06:07` |
| `periodic_mlp_harmonic_global` | Implemented Benchmark | `te_periodic_mlp_harmonic_global` | `periodic_mlp` | 0.001264 | 28,417 | `2026-07-08 03:17:38` |
| `periodic_gru_sequence` | Implemented Benchmark | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | 0.001279 | 157,569 | `2026-06-22 14:06:48` |
| `wave4_3_mixture_density_k3_global` | Implemented Benchmark | `te_wave4_3_mixture_density_k3_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001544 | 86,976 | `2026-07-15 14:38:59` |
| `tree_global` | Implemented Benchmark | `te_tree_global__polished_setpoints` | `hist_gradient_boosting` | 0.001699 | 5 | `2026-07-07 10:07:53` |
| `residual_harmonic_mlp_global` | Implemented Benchmark | `te_residual_harmonic_mlp_global` | `residual_harmonic_mlp` | 0.001710 | 26,138 | `2026-07-07 13:50:19` |
| `feedforward_global` | Implemented Benchmark | `te_feedforward_global` | `feedforward` | 0.001734 | 109,697 | `2026-07-07 18:43:03` |
| `periodic_mlp_global` | Implemented Benchmark | `te_periodic_mlp_global` | `periodic_mlp` | 0.001741 | 27,137 | `2026-07-07 21:58:17` |
| `wave4_3_mixture_density_k2_global` | Implemented Benchmark | `te_wave4_3_mixture_density_k2_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001743 | 86,400 | `2026-07-15 05:01:50` |
| `tree` | Implemented Benchmark | `te_hist_gbr_tabular_global` | `hist_gradient_boosting` | 0.001753 | 4 | `2026-06-22 16:58:47` |
| `wave4_2_quantile_p10_p50_p90_global` | Implemented Benchmark | `te_wave4_2_quantile_p10_p50_p90_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001878 | 85,824 | `2026-07-14 16:15:03` |
| `wave4_1_mae_robust_loss_global` | Implemented Benchmark | `te_wave4_1_mae_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001890 | 85,440 | `2026-07-12 18:19:09` |
| `wave4_1_log_cosh_robust_loss_global` | Implemented Benchmark | `te_wave4_1_log_cosh_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001913 | 85,440 | `2026-07-01 06:59:33` |
| `wave3_2_harmonic_residual_offset_global` | Implemented Benchmark | `te_wave3_2_harmonic_residual_offset_global` | `harmonic_residual_offset_probe` | 0.001914 | 85,440 | `2026-07-11 05:29:51` |
| `wave3_3_raw_centered_shape_curve_aware_global` | Implemented Benchmark | `te_wave3_3_raw_centered_shape_curve_aware_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001954 | 85,440 | `2026-07-11 20:11:00` |
| `wave3_3_curve_aware_pointwise_control_global` | Implemented Benchmark | `te_wave3_3_curve_aware_pointwise_control_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001971 | 85,440 | `2026-07-11 13:46:39` |
| `periodic_temporal_convolution_global` | Implemented Benchmark | `te_periodic_temporal_convolution_global__polished_actual_values` | `periodic_temporal_convolution` | 0.001999 | 158,529 | `2026-07-08 21:06:17` |
| `wave3_3_raw_offset_curve_aware_global` | Implemented Benchmark | `te_wave3_3_raw_offset_curve_aware_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002001 | 85,747 | `2026-07-12 02:24:38` |
| `wave4_2_gaussian_nll_global` | Implemented Benchmark | `te_wave4_2_gaussian_nll_global` | `curve_aware_harmonic_residual_offset_probe` | 0.002001 | 85,632 | `2026-07-14 20:42:59` |
| `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global` | Implemented Benchmark | `te_track2g_curve_aware_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | 0.002008 | 85,440 | `2026-06-22 15:16:05` |
| `wave4_1_smooth_l1_robust_loss_global` | Implemented Benchmark | `te_wave4_1_smooth_l1_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | 0.002017 | 85,440 | `2026-07-13 00:54:21` |
| `wave3_3_full_curve_composite_global` | Implemented Benchmark | `te_wave3_3_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | 0.002023 | 85,440 | `2026-07-12 12:13:42` |
| `phase3_pinn_c0_learned_mean_control_global` | Implemented Benchmark | `te_phase3_pinn_c0_learned_mean_control_global__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002050 | 7,212 | `2026-07-26 18:14:00` |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_sparse_rcim_global` | `residual_harmonic_lstm_sequence` | 0.002062 | 200,852 | `2026-07-09 21:46:24` |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002062 | 151,060 | `2026-07-09 08:19:20` |
| `harmonic_regression_global` | Implemented Benchmark | `te_harmonic_regression_global__polished_actual_values` | `harmonic_regression` | 0.002071 | 150 | `2026-07-08 00:15:14` |
| `residual_harmonic_gru_sequence_dense240_global` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_dense240_global` | `residual_harmonic_gru_sequence` | 0.002076 | 151,138 | `2026-07-09 11:57:58` |
| `residual_harmonic_gru_sequence_dense360_global` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002088 | 151,762 | `2026-07-09 17:18:37` |
| `phase3_pinn_c5_shared_stiffness_global` | Implemented Benchmark | `te_phase3_pinn_c5_shared_stiffness_global__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002103 | 5,611 | `2026-07-26 19:23:35` |
| `residual_harmonic_gru_sequence_sparse_rcim` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.002112 | 150,676 | `2026-06-22 14:31:08` |
| `wave5_1_harmonic_prior_smooth_l1_structured_global` | Implemented Benchmark | `te_wave5_1_harmonic_prior_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | 0.002119 | 7,168 | `2026-07-16 06:39:53` |
| `wave5_1_harmonic_prior_pointwise_control_global` | Implemented Benchmark | `te_wave5_1_harmonic_prior_pointwise_control_global` | `wave3_harmonic_prior_residual` | 0.002159 | 7,168 | `2026-07-16 02:44:33` |
| `residual_harmonic_lstm_sequence_dense240_global` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_dense240_global` | `residual_harmonic_lstm_sequence` | 0.002161 | 201,314 | `2026-07-10 02:31:07` |
| `wave3_harmonic_prior_residual_smooth_l1_structured_global` | Implemented Benchmark | `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | 0.002168 | 7,168 | `2026-06-22 15:37:36` |
| `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global` | `wave52b_offset_harmonic_guided` | 0.002215 | 22,593 | `2026-07-02 01:24:47` |
| `residual_harmonic_lstm_sequence_dense360_global` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_dense360_global` | `residual_harmonic_lstm_sequence` | 0.002223 | 201,554 | `2026-07-10 06:59:39` |
| `gru_sequence_global` | Implemented Benchmark | `te_gru_sequence_global` | `gru_sequence` | 0.002229 | 150,657 | `2026-07-08 13:44:26` |
| `lstm_sequence_global` | Implemented Benchmark | `te_lstm_sequence_global` | `lstm_sequence` | 0.002258 | 200,833 | `2026-07-08 17:20:19` |
| `wave3_1_sequential_residual_offset_probe_global` | Implemented Benchmark | `te_wave3_1_sequential_residual_offset_probe_global` | `sequential_residual_offset_probe` | 0.002261 | 92,418 | `2026-07-10 11:09:33` |
| `wave4_4_gru_latent_offset_residual_global` | Implemented Benchmark | `te_wave4_4_gru_latent_offset_residual_global__polished_actual_values` | `latent_state_hysteresis_probe` | 0.002271 | 125,475 | `2026-07-15 18:51:23` |
| `wave3_2_clean_sequential_residual_offset_global` | Implemented Benchmark | `te_wave3_2_clean_sequential_residual_offset_global` | `sequential_residual_offset_probe` | 0.002276 | 92,418 | `2026-07-10 22:06:08` |
| `wave4_4_causal_tcn_latent_offset_residual_global` | Implemented Benchmark | `te_wave4_4_causal_tcn_latent_offset_residual_global` | `latent_state_hysteresis_probe` | 0.002315 | 97,155 | `2026-07-15 22:40:16` |
| `temporal_convolution_global` | Implemented Benchmark | `te_temporal_convolution_global__polished_actual_values` | `temporal_convolution` | 0.002327 | 147,009 | `2026-07-08 10:20:02` |
| `track2h_latent_state_hysteresis_gru_offset_residual_global` | Implemented Benchmark | `te_track2h_l_gru_offset_residual_global` | `latent_state_hysteresis_probe` | 0.002339 | 124,899 | `2026-06-22 16:00:39` |
| `wave52b_offset_harmonic_guided_pointwise_control_global` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_pointwise_control_global` | `wave52b_offset_harmonic_guided` | 0.002461 | 22,593 | `2026-07-01 19:54:22` |
| `wave52b_offset_harmonic_guided_offset_head_global` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_offset_head_global` | `wave52b_offset_harmonic_guided` | 0.002483 | 22,593 | `2026-07-01 21:42:42` |
| `wave52b_offset_harmonic_guided_offset_centered_shape_global` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_offset_centered_shape_global` | `wave52b_offset_harmonic_guided` | 0.002540 | 22,593 | `2026-07-01 23:25:44` |
| `periodic_lstm_sequence` | Implemented Benchmark | `te_periodic_lstm_sequence_remote_global` | `periodic_lstm_sequence` | 0.002682 | 210,561 | `2026-05-25 19:20:56` |
| `feedforward` | Current Plain MLP Anchor | `te_feedforward_trial` | `feedforward` | 0.002877 | 26,113 | `2026-06-22 13:13:25` |
| `track2h_quantile_probabilistic_gaussian_nll_global` | Implemented Benchmark | `te_track2h_gaussian_nll_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003013 | 85,958 | `2026-06-12 13:12:35` |
| `residual_harmonic_mlp` | Implemented Benchmark | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.003034 | 26,266 | `2026-05-20 11:41:03` |
| `periodic_mlp` | Implemented Benchmark | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.003186 | 27,265 | `2026-05-21 08:12:57` |
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
| `harmonic_regression` | Implemented Benchmark | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.003839 | 125 | `2026-06-22 13:26:44` |
| `feedforward_recovery_micro` | Implemented Benchmark | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004164 | 109,953 | `2026-05-12 11:12:51` |
| `feedforward_recovery_probe_dense` | Implemented Benchmark | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004602 | 109,953 | `2026-05-12 17:16:41` |

#### Forward Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `periodic_gru_sequence_fw` | Implemented Benchmark | `te_periodic_gru_sequence_fw` | `periodic_gru_sequence` | 0.001101 | 157,569 | `2026-07-09 01:09:21` |
| `shape_objective_periodic_mlp_harmonic_fw` | Implemented Benchmark | `te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints` | `periodic_mlp` | 0.001236 | 28,545 | `2026-07-21 19:12:09` |
| `causal_offset_mean_periodic_mlp_harmonic_fw` | Implemented Benchmark | `te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints` | `periodic_mlp` | 0.001277 | 28,545 | `2026-07-22 18:23:32` |
| `periodic_mlp_harmonic_fw` | Implemented Benchmark | `te_periodic_mlp_harmonic_fw` | `periodic_mlp` | 0.001326 | 28,417 | `2026-07-08 03:31:01` |
| `phase2_pinn_h0_fourier_control_fw` | Implemented Benchmark | `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001354 | 5,635 | `2026-07-26 14:11:21` |
| `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` | `wave52b_offset_harmonic_guided` | 0.001392 | 22,593 | `2026-07-02 01:57:18` |
| `shape_objective_v3_periodic_gru_sequence_fw` | Implemented Benchmark | `te_shape_objective_v3_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.001400 | 157,953 | `2026-07-21 19:02:58` |
| `shape_first_distilled_periodic_mlp_harmonic_fw` | Implemented Benchmark | `te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints` | `periodic_mlp` | 0.001420 | 28,545 | `2026-07-22 14:48:11` |
| `stage4_h08_r5_deep` | Implemented Benchmark | `te_stage4_h08_r5_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001455 | 7,187 | `2026-07-28 11:04:19` |
| `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw` | Implemented Benchmark | `te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.001463 | 157,953 | `2026-07-21 13:08:39` |
| `shape_objective_curve_aware_residual_fw` | Implemented Benchmark | `te_shape_objective_curve_aware_residual_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.001463 | 85,747 | `2026-07-21 19:20:11` |
| `phase3_pinn_c1_linear_compliance_soft_fw_seed_314159` | Implemented Benchmark | `te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001472 | 7,212 | `2026-07-26 20:00:21` |
| `phase3_pinn_c1_linear_compliance_soft_fw` | Implemented Benchmark | `te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001495 | 7,212 | `2026-07-26 18:21:36` |
| `shape_first_distilled_periodic_gru_sequence_fw` | Implemented Benchmark | `te_shape_first_distilled_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.001523 | 157,953 | `2026-07-22 14:43:06` |
| `periodic_lstm_sequence_fw` | Implemented Benchmark | `te_periodic_lstm_sequence_fw` | `periodic_lstm_sequence` | 0.001547 | 210,049 | `2026-07-09 05:16:31` |
| `phase3_pinn_c2_temperature_compliance_soft_fw` | Implemented Benchmark | `te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001551 | 7,212 | `2026-07-26 18:37:03` |
| `stage4_c04_r1_deep` | Implemented Benchmark | `te_stage4_c04_r1_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001609 | 6,901 | `2026-07-28 10:17:21` |
| `phase3_pinn_c0_learned_mean_control_fw` | Implemented Benchmark | `te_phase3_pinn_c0_learned_mean_control_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001611 | 7,212 | `2026-07-26 17:53:30` |
| `stage4_h02_r2_deep` | Implemented Benchmark | `te_stage4_h02_r2_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001617 | 7,745 | `2026-07-28 10:36:11` |
| `stage4_c03_r1_compact` | Implemented Benchmark | `te_stage4_c03_r1_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001620 | 1,485 | `2026-07-28 10:12:46` |
| `stage4_c01_r1_compact` | Implemented Benchmark | `te_stage4_c01_r1_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001624 | 1,825 | `2026-07-28 10:06:00` |
| `stage4_c05_r1_compact` | Implemented Benchmark | `te_stage4_c05_r1_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001624 | 1,825 | `2026-07-28 10:21:37` |
| `stage4_c06_r1_deep` | Implemented Benchmark | `te_stage4_c06_r1_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001665 | 7,139 | `2026-07-28 10:25:52` |
| `wave4_3_mixture_density_k3_fw` | Implemented Benchmark | `te_wave4_3_mixture_density_k3_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001671 | 86,976 | `2026-07-15 15:39:35` |
| `wave4_3_mixture_density_k2_fw` | Implemented Benchmark | `te_wave4_3_mixture_density_k2_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001698 | 86,400 | `2026-07-15 06:02:16` |
| `tree_fw` | Implemented Benchmark | `te_tree_fw__polished_setpoints` | `hist_gradient_boosting` | 0.001699 | 5 | `2026-07-07 10:07:54` |
| `stage4_h07_r5_compact` | Implemented Benchmark | `te_stage4_h07_r5_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001725 | 1,843 | `2026-07-28 10:59:18` |
| `feedforward_fw` | Implemented Benchmark | `te_feedforward_fw` | `feedforward` | 0.001726 | 109,697 | `2026-07-07 19:17:09` |
| `periodic_mlp_fw` | Implemented Benchmark | `te_periodic_mlp_fw` | `periodic_mlp` | 0.001742 | 27,137 | `2026-07-07 22:12:18` |
| `phase3_pinn_c3_nonlinear_compliance_soft_fw` | Implemented Benchmark | `te_phase3_pinn_c3_nonlinear_compliance_soft_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001745 | 7,212 | `2026-07-26 18:52:22` |
| `residual_harmonic_mlp_fw` | Implemented Benchmark | `te_residual_harmonic_mlp_fw__polished_setpoints` | `residual_harmonic_mlp` | 0.001759 | 26,266 | `2026-07-07 14:15:24` |
| `stage4_c02_r1_deep` | Implemented Benchmark | `te_stage4_c02_r1_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001760 | 7,745 | `2026-07-28 10:08:58` |
| `phase2_pinn_h2_oscillator_periodic_closure_fw` | Implemented Benchmark | `te_phase2_pinn_h2_oscillator_periodic_closure_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001784 | 16,570 | `2026-07-26 15:35:48` |
| `stage4_a01_r2_compact` | Implemented Benchmark | `te_stage4_a01_r2_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001878 | 1,825 | `2026-07-28 11:09:21` |
| `phase3_pinn_c1_linear_compliance_soft_fw_seed_271828` | Implemented Benchmark | `te_phase3_pinn_c1_linear_compliance_soft_fw_seed_271828__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001898 | 7,212 | `2026-07-26 20:07:49` |
| `wave4_2_gaussian_nll_fw` | Implemented Benchmark | `te_wave4_2_gaussian_nll_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001914 | 85,632 | `2026-07-14 21:40:47` |
| `wave4_2_quantile_p10_p50_p90_fw` | Implemented Benchmark | `te_wave4_2_quantile_p10_p50_p90_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001914 | 85,824 | `2026-07-14 17:11:13` |
| `wave3_3_raw_centered_shape_curve_aware_fw` | Implemented Benchmark | `te_wave3_3_raw_centered_shape_curve_aware_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001917 | 85,440 | `2026-07-11 20:41:54` |
| `wave3_3_curve_aware_pointwise_control_fw` | Implemented Benchmark | `te_wave3_3_curve_aware_pointwise_control_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001919 | 85,440 | `2026-07-11 14:43:50` |
| `wave4_1_log_cosh_robust_loss_fw` | Implemented Benchmark | `te_wave4_1_log_cosh_robust_loss_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001921 | 85,440 | `2026-07-01 07:40:32` |
| `stage4_a03_r5_compact` | Implemented Benchmark | `te_stage4_a03_r5_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001926 | 2,033 | `2026-07-28 11:16:11` |
| `wave52b_offset_harmonic_guided_offset_centered_shape_fw` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_offset_centered_shape_fw` | `wave52b_offset_harmonic_guided` | 0.001931 | 22,593 | `2026-07-02 00:02:31` |
| `stage4_h01_r2_compact` | Implemented Benchmark | `te_stage4_h01_r2_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001940 | 1,825 | `2026-07-28 10:31:03` |
| `wave3_2_harmonic_residual_offset_fw` | Implemented Benchmark | `te_wave3_2_harmonic_residual_offset_fw` | `harmonic_residual_offset_probe` | 0.001948 | 85,440 | `2026-07-11 06:13:40` |
| `wave52b_offset_harmonic_guided_offset_head_fw` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_offset_head_fw` | `wave52b_offset_harmonic_guided` | 0.001948 | 22,593 | `2026-07-01 22:04:27` |
| `phase2_pinn_h1_oscillator_residual_fw` | Implemented Benchmark | `te_phase2_pinn_h1_oscillator_residual_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001951 | 16,570 | `2026-07-26 14:33:28` |
| `wave3_3_raw_offset_curve_aware_fw` | Implemented Benchmark | `te_wave3_3_raw_offset_curve_aware_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001953 | 85,440 | `2026-07-12 02:57:47` |
| `wave4_1_smooth_l1_robust_loss_fw` | Implemented Benchmark | `te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001956 | 85,747 | `2026-07-13 01:50:39` |
| `wave4_1_mae_robust_loss_fw` | Implemented Benchmark | `te_wave4_1_mae_robust_loss_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001961 | 85,440 | `2026-07-12 19:08:24` |
| `stage4_h06_r4_deep` | Implemented Benchmark | `te_stage4_h06_r4_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001965 | 6,857 | `2026-07-28 10:54:15` |
| `wave3_3_full_curve_composite_fw` | Implemented Benchmark | `te_wave3_3_full_curve_composite_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.002038 | 85,440 | `2026-07-12 13:09:19` |
| `wave52b_offset_harmonic_guided_pointwise_control_fw` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_pointwise_control_fw` | `wave52b_offset_harmonic_guided` | 0.002054 | 22,593 | `2026-07-01 20:13:10` |
| `residual_harmonic_gru_sequence_sparse_rcim_fw` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_sparse_rcim_fw` | `residual_harmonic_gru_sequence` | 0.002056 | 150,676 | `2026-07-09 08:55:01` |
| `harmonic_regression_fw` | Implemented Benchmark | `te_harmonic_regression_fw__polished_actual_values` | `harmonic_regression` | 0.002066 | 150 | `2026-07-08 00:32:21` |
| `residual_harmonic_lstm_sequence_sparse_rcim_fw` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.002067 | 201,364 | `2026-07-09 22:37:02` |
| `residual_harmonic_gru_sequence_dense360_fw` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002074 | 151,762 | `2026-07-09 17:49:07` |
| `periodic_temporal_convolution_fw` | Implemented Benchmark | `te_periodic_temporal_convolution_fw__polished_actual_values` | `periodic_temporal_convolution` | 0.002077 | 158,529 | `2026-07-08 21:27:59` |
| `phase3_pinn_c4_hard_elastic_offset_fw` | Implemented Benchmark | `te_phase3_pinn_c4_hard_elastic_offset_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002087 | 5,611 | `2026-07-26 19:06:07` |
| `causal_offset_mean_gru_sequence_fw` | Implemented Benchmark | `te_causal_offset_mean_gru_sequence_fw__polished_setpoints` | `sequential_residual_offset_probe` | 0.002100 | 92,802 | `2026-07-22 18:23:32` |
| `residual_harmonic_gru_sequence_dense240_fw` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_dense240_fw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002101 | 151,522 | `2026-07-09 12:19:38` |
| `stage4_h05_r4_compact` | Implemented Benchmark | `te_stage4_h05_r4_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.002111 | 1,513 | `2026-07-28 10:49:33` |
| `residual_harmonic_lstm_sequence_dense240_fw` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_dense240_fw` | `residual_harmonic_lstm_sequence` | 0.002147 | 201,314 | `2026-07-10 02:54:22` |
| `wave5_1_harmonic_prior_smooth_l1_structured_fw` | Implemented Benchmark | `te_wave5_1_harmonic_prior_smooth_l1_structured_fw` | `wave3_harmonic_prior_residual` | 0.002151 | 7,168 | `2026-07-16 06:57:05` |
| `wave5_1_harmonic_prior_pointwise_control_fw` | Implemented Benchmark | `te_wave5_1_harmonic_prior_pointwise_control_fw` | `wave3_harmonic_prior_residual` | 0.002185 | 7,168 | `2026-07-16 03:08:07` |
| `residual_harmonic_lstm_sequence_dense360_fw` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_dense360_fw` | `residual_harmonic_lstm_sequence` | 0.002219 | 201,554 | `2026-07-10 07:24:50` |
| `lstm_sequence_fw` | Implemented Benchmark | `te_lstm_sequence_fw__polished_actual_values` | `lstm_sequence` | 0.002239 | 201,345 | `2026-07-08 18:02:26` |
| `wave3_1_sequential_residual_offset_probe_fw` | Implemented Benchmark | `te_wave3_1_sequential_residual_offset_probe_fw` | `sequential_residual_offset_probe` | 0.002246 | 92,418 | `2026-07-10 11:35:18` |
| `gru_sequence_fw` | Implemented Benchmark | `te_gru_sequence_fw` | `gru_sequence` | 0.002247 | 150,657 | `2026-07-08 14:10:34` |
| `wave3_2_clean_sequential_residual_offset_fw` | Implemented Benchmark | `te_wave3_2_clean_sequential_residual_offset_fw` | `sequential_residual_offset_probe` | 0.002258 | 92,418 | `2026-07-10 22:37:03` |
| `wave4_4_gru_latent_offset_residual_fw` | Implemented Benchmark | `te_wave4_4_gru_latent_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.002300 | 124,899 | `2026-07-15 19:13:13` |
| `wave4_4_causal_tcn_latent_offset_residual_fw` | Implemented Benchmark | `te_wave4_4_causal_tcn_latent_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.002316 | 97,155 | `2026-07-15 22:54:23` |
| `phase2_pinn_h3_oscillator_periodic_bauer_anchor_fw` | Implemented Benchmark | `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.002389 | 16,570 | `2026-07-26 16:16:46` |
| `temporal_convolution_fw` | Implemented Benchmark | `te_temporal_convolution_fw__polished_actual_values` | `temporal_convolution` | 0.002390 | 147,009 | `2026-07-08 10:34:09` |
| `shape_gate_loss_pilot_periodic_gru_sequence_fw` | Implemented Benchmark | `te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.002522 | 157,953 | `2026-07-20 20:07:19` |
| `stage4_a04_r5_compact` | Implemented Benchmark | `te_stage4_a04_r5_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.002846 | 2,033 | `2026-07-28 11:19:25` |
| `track2f_bis_harmonic_residual_offset_fw` | Implemented Benchmark | `te_track2f_bis_harmonic_residual_offset_fw` | `harmonic_residual_offset_probe` | 0.002862 | 85,747 | `2026-06-05 16:32:38` |
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
| `stage4_a02_r2_compact` | Implemented Benchmark | `te_stage4_a02_r2_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.005241 | 1,825 | `2026-07-28 11:13:26` |
| `stage4_h03_r3_compact` | Implemented Benchmark | `te_stage4_h03_r3_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.046115 | 1,825 | `2026-07-28 10:40:56` |
| `stage4_h04_r3_deep` | Implemented Benchmark | `te_stage4_h04_r3_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.046188 | 7,745 | `2026-07-28 10:44:28` |

#### Backward Models

| Family | Current Role | Best Run | Model Type | Test MAE [deg] | Params | Last Update |
| --- | --- | --- | --- | ---: | ---: | --- |
| `periodic_gru_sequence_bw` | Current Program Winner | `te_periodic_gru_sequence_bw` | `periodic_gru_sequence` | 0.001084 | 157,569 | `2026-07-09 01:51:59` |
| `periodic_lstm_sequence_bw` | Implemented Benchmark | `te_periodic_lstm_sequence_bw` | `periodic_lstm_sequence` | 0.001226 | 210,049 | `2026-07-09 05:28:43` |
| `periodic_mlp_harmonic_bw` | Implemented Benchmark | `te_periodic_mlp_harmonic_bw` | `periodic_mlp` | 0.001279 | 28,417 | `2026-07-08 03:56:01` |
| `phase2_pinn_h0_fourier_control_bw` | Implemented Benchmark | `te_phase2_pinn_h0_fourier_control_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001498 | 5,635 | `2026-07-26 14:16:04` |
| `phase3_pinn_c2_temperature_compliance_soft_bw` | Implemented Benchmark | `te_phase3_pinn_c2_temperature_compliance_soft_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001624 | 7,212 | `2026-07-26 18:44:42` |
| `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw` | `wave52b_offset_harmonic_guided` | 0.001677 | 22,593 | `2026-07-02 02:27:12` |
| `feedforward_bw` | Implemented Benchmark | `te_feedforward_bw` | `feedforward` | 0.001686 | 109,697 | `2026-07-07 19:39:50` |
| `tree_bw` | Implemented Benchmark | `te_tree_bw__polished_setpoints` | `hist_gradient_boosting` | 0.001699 | 5 | `2026-07-07 10:07:54` |
| `wave4_3_mixture_density_k3_bw` | Implemented Benchmark | `te_wave4_3_mixture_density_k3_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001704 | 86,976 | `2026-07-15 16:07:33` |
| `residual_harmonic_mlp_bw` | Implemented Benchmark | `te_residual_harmonic_mlp_bw` | `residual_harmonic_mlp` | 0.001712 | 26,138 | `2026-07-07 14:47:50` |
| `phase2_pinn_h1_oscillator_residual_bw` | Implemented Benchmark | `te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001723 | 16,570 | `2026-07-26 15:08:52` |
| `wave4_3_mixture_density_k2_bw` | Implemented Benchmark | `te_wave4_3_mixture_density_k2_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001725 | 86,400 | `2026-07-15 06:33:19` |
| `periodic_mlp_bw` | Implemented Benchmark | `te_periodic_mlp_bw` | `periodic_mlp` | 0.001740 | 27,137 | `2026-07-07 22:30:44` |
| `phase3_pinn_c0_learned_mean_control_bw` | Implemented Benchmark | `te_phase3_pinn_c0_learned_mean_control_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001825 | 7,212 | `2026-07-26 18:00:41` |
| `phase3_pinn_c1_linear_compliance_soft_bw` | Implemented Benchmark | `te_phase3_pinn_c1_linear_compliance_soft_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001877 | 7,212 | `2026-07-26 18:29:08` |
| `wave4_2_quantile_p10_p50_p90_bw` | Implemented Benchmark | `te_wave4_2_quantile_p10_p50_p90_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001888 | 85,824 | `2026-07-14 17:40:45` |
| `wave3_2_harmonic_residual_offset_bw` | Implemented Benchmark | `te_wave3_2_harmonic_residual_offset_bw` | `harmonic_residual_offset_probe` | 0.001894 | 85,440 | `2026-07-11 06:57:20` |
| `wave3_3_raw_offset_curve_aware_bw` | Implemented Benchmark | `te_wave3_3_raw_offset_curve_aware_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001898 | 85,440 | `2026-07-12 03:46:43` |
| `wave4_1_log_cosh_robust_loss_bw` | Implemented Benchmark | `te_wave4_1_log_cosh_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001899 | 85,440 | `2026-07-01 08:37:58` |
| `wave4_1_mae_robust_loss_bw` | Implemented Benchmark | `te_wave4_1_mae_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001907 | 85,440 | `2026-07-12 19:55:36` |
| `wave3_3_raw_centered_shape_curve_aware_bw` | Implemented Benchmark | `te_wave3_3_raw_centered_shape_curve_aware_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001916 | 85,440 | `2026-07-11 21:32:35` |
| `wave3_3_curve_aware_pointwise_control_bw` | Implemented Benchmark | `te_wave3_3_curve_aware_pointwise_control_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001925 | 85,440 | `2026-07-11 15:28:19` |
| `phase3_pinn_c3_nonlinear_compliance_soft_bw` | Implemented Benchmark | `te_phase3_pinn_c3_nonlinear_compliance_soft_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001926 | 7,212 | `2026-07-26 18:59:06` |
| `wave4_2_gaussian_nll_bw` | Implemented Benchmark | `te_wave4_2_gaussian_nll_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001927 | 85,632 | `2026-07-14 22:39:07` |
| `phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw` | Implemented Benchmark | `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001931 | 16,570 | `2026-07-26 16:38:48` |
| `phase2_pinn_h2_oscillator_periodic_closure_bw` | Implemented Benchmark | `te_phase2_pinn_h2_oscillator_periodic_closure_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001966 | 16,570 | `2026-07-26 15:56:14` |
| `wave4_1_smooth_l1_robust_loss_bw` | Implemented Benchmark | `te_wave4_1_smooth_l1_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001968 | 85,440 | `2026-07-13 02:22:43` |
| `wave52b_offset_harmonic_guided_pointwise_control_bw` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_pointwise_control_bw` | `wave52b_offset_harmonic_guided` | 0.001979 | 22,593 | `2026-07-01 20:42:26` |
| `periodic_temporal_convolution_bw` | Implemented Benchmark | `te_periodic_temporal_convolution_bw__polished_actual_values` | `periodic_temporal_convolution` | 0.002001 | 158,529 | `2026-07-08 21:50:44` |
| `wave52b_offset_harmonic_guided_offset_head_bw` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_offset_head_bw` | `wave52b_offset_harmonic_guided` | 0.002008 | 22,593 | `2026-07-01 22:36:30` |
| `wave52b_offset_harmonic_guided_offset_centered_shape_bw` | Implemented Benchmark | `te_wave52b_offset_harmonic_guided_offset_centered_shape_bw` | `wave52b_offset_harmonic_guided` | 0.002012 | 22,593 | `2026-07-02 00:38:22` |
| `residual_harmonic_gru_sequence_dense240_bw` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_dense240_bw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002049 | 151,522 | `2026-07-09 12:52:09` |
| `wave3_3_full_curve_composite_bw` | Implemented Benchmark | `te_wave3_3_full_curve_composite_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002067 | 85,440 | `2026-07-12 13:51:11` |
| `residual_harmonic_gru_sequence_dense360_bw` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002071 | 151,762 | `2026-07-09 18:18:10` |
| `harmonic_regression_bw` | Implemented Benchmark | `te_harmonic_regression_bw__polished_actual_values` | `harmonic_regression` | 0.002076 | 150 | `2026-07-08 00:46:14` |
| `residual_harmonic_gru_sequence_sparse_rcim_bw` | Implemented Benchmark | `te_residual_harmonic_gru_sequence_sparse_rcim_bw` | `residual_harmonic_gru_sequence` | 0.002083 | 150,676 | `2026-07-09 09:31:01` |
| `residual_harmonic_lstm_sequence_dense360_bw` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_dense360_bw` | `residual_harmonic_lstm_sequence` | 0.002097 | 201,554 | `2026-07-10 07:56:39` |
| `wave5_1_harmonic_prior_pointwise_control_bw` | Implemented Benchmark | `te_wave5_1_harmonic_prior_pointwise_control_bw` | `wave3_harmonic_prior_residual` | 0.002105 | 7,168 | `2026-07-16 03:36:03` |
| `residual_harmonic_lstm_sequence_sparse_rcim_bw` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_sparse_rcim_bw` | `residual_harmonic_lstm_sequence` | 0.002108 | 200,852 | `2026-07-09 22:49:53` |
| `residual_harmonic_lstm_sequence_dense240_bw` | Implemented Benchmark | `te_residual_harmonic_lstm_sequence_dense240_bw__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.002116 | 201,826 | `2026-07-10 03:27:02` |
| `wave5_1_harmonic_prior_smooth_l1_structured_bw` | Implemented Benchmark | `te_wave5_1_harmonic_prior_smooth_l1_structured_bw` | `wave3_harmonic_prior_residual` | 0.002178 | 7,168 | `2026-07-16 07:23:05` |
| `wave3_1_sequential_residual_offset_probe_bw` | Implemented Benchmark | `te_wave3_1_sequential_residual_offset_probe_bw` | `sequential_residual_offset_probe` | 0.002225 | 92,418 | `2026-07-10 12:18:02` |
| `gru_sequence_bw` | Implemented Benchmark | `te_gru_sequence_bw` | `gru_sequence` | 0.002230 | 150,657 | `2026-07-08 14:46:08` |
| `lstm_sequence_bw` | Implemented Benchmark | `te_lstm_sequence_bw` | `lstm_sequence` | 0.002240 | 200,833 | `2026-07-08 18:46:16` |
| `wave3_2_clean_sequential_residual_offset_bw` | Implemented Benchmark | `te_wave3_2_clean_sequential_residual_offset_bw` | `sequential_residual_offset_probe` | 0.002242 | 92,418 | `2026-07-10 23:01:43` |
| `wave4_4_gru_latent_offset_residual_bw` | Implemented Benchmark | `te_wave4_4_gru_latent_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.002260 | 124,899 | `2026-07-15 19:43:02` |
| `temporal_convolution_bw` | Implemented Benchmark | `te_temporal_convolution_bw__polished_actual_values` | `temporal_convolution` | 0.002303 | 147,009 | `2026-07-08 11:01:13` |
| `wave4_4_causal_tcn_latent_offset_residual_bw` | Implemented Benchmark | `te_wave4_4_causal_tcn_latent_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.002309 | 97,155 | `2026-07-15 23:09:39` |
| `phase3_pinn_c4_hard_elastic_offset_bw` | Implemented Benchmark | `te_phase3_pinn_c4_hard_elastic_offset_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002350 | 5,611 | `2026-07-26 19:10:25` |
| `track2h_mixture_density_heads_mdn_k2_bw` | Implemented Benchmark | `te_track2h_mdn_k2_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002658 | 86,802 | `2026-06-13 12:14:13` |
| `track2h_mixture_density_heads_mdn_k3_bw` | Implemented Benchmark | `te_track2h_mdn_k3_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002721 | 87,435 | `2026-06-13 13:10:07` |
| `track2h_quantile_probabilistic_quantile_p10_p50_p90_bw` | Implemented Benchmark | `te_track2h_quantile_p10_p50_p90_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002927 | 86,169 | `2026-06-12 12:10:23` |
| `track2h_quantile_probabilistic_gaussian_nll_bw` | Implemented Benchmark | `te_track2h_gaussian_nll_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002998 | 85,958 | `2026-06-12 13:53:26` |
| `track2h_dispersion_aware_smooth_l1_robust_bw` | Implemented Benchmark | `te_track2h_smooth_l1_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003074 | 85,747 | `2026-06-11 13:24:47` |
| `track2f_bis_harmonic_residual_offset_bw` | Implemented Benchmark | `te_track2f_bis_harmonic_residual_offset_bw` | `harmonic_residual_offset_probe` | 0.003336 | 85,747 | `2026-06-05 16:44:49` |
| `wave3_harmonic_prior_residual_pointwise_control_bw` | Implemented Benchmark | `te_wave3_harmonic_prior_residual_pointwise_control_bw` | `wave3_harmonic_prior_residual` | 0.003363 | 7,283 | `2026-06-15 14:49:19` |
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

- No campaign is currently in `prepared` or `running` state.
- The next active implementation branch should therefore be read from the live backlog focus and the next approved campaign plan.

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
| Wave 5.1. Hybrid Structured Models | status: first real campaign closed successfully as a scalar training; current scaffold:; model type: `wave3_harmonic_prior_residual`;; model class:; dry-run skeleton checker:; training-smoke-ready checker:; final one-batch validation artifact:; prepared package:; prepared launcher:; campaign closeout report:; scalar training winner:; scalar decision: no program-best promotion; the current program winner; official TE Curve Verification Pipeline launcher:; official TE curve-verification report:; strongest Wave 5.1 TE Curve Verification Pipeline candidate:; updated priority: use the completed Wave 5.1 curve, offset, collage, overlay,; mandatory rule: prepare or justify `global`, `forward`, and `backward`; paper-reproduction scope:; compare hybrid structured predictors against the paper-style harmonic stack;; test condition-conditioned residual structure and separate treatment of; prepare the repository-owned deployable predictor package after the; next implementation steps:; proceed to Wave 5.2 reference intake, equation audit, and formulation |

Low-priority exploratory families currently listed in the backlog:

- `low priority.`
- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- `optional Kernel Ridge / Gaussian Process benchmark`
| Wave 5.2. PINN Formulation And First PINN | status: Phases 0 through 15 complete; sixteen-phase roadmap closed;; canonical roadmap:; physics reference-intake register:; active general formulation families:; Polynomial-Fourier structured residual PINN;; harmonic-kinematic constraint PINN;; contact-regime or energy-consistency PINN where references and observable; additional reference-derived formulations, kept separate until their; full-PINN qualification rule:; training must contain an explicit differentiable physical residual,; harmonic features, Fourier heads, curve metrics, or ungrounded soft; active evidence base:; Waves 3.1 through 3.3 for offset, centered shape, slope, amplitude, phase,; Waves 4.1 through 4.4 for robustness, uncertainty, mixture behavior, and; Wave 5.1 for harmonic priors and structured residual learning;; periodic GRU and periodic harmonic MLP as time-windowed and non-windowed; the existing direction-specific Polynomial Fourier Series PLC; current scaffold:; diagnostic adapter:; diagnostic report builder:; parameter-inventory report builder:; generated diagnostic report:; generated parameter-inventory report:; companion artifacts:; parameter-inventory artifacts:; residual-explanatory diagnostic report:; leakage-safe residual-explanatory rerun:; completed Phase 4 evidence:; all `969` canonical raw files preserve one ordered `Fw`-to-`Bw`; no condition contains repeated reversal cycles or repeated major loops;; minor-loop, controlled warm-up, and deterministic reset labels are absent;; `PINN-Y1`, `PINN-Y2`, `PINN-Y3`, and `PINN-Y5` are; no Phase 4 training campaign or physical-residual promotion is authorized;; completed Phase 5 evidence:; all `969` common-split condition pairs and `37,805,294` simplified-source; median centered `Fw`/`Bw` correlation is `0.985-0.990`;; the median absolute directional mean gap is `3.79-4.78 arcmin`, but it is; `PINN-B1` remains an empirical real-data-trainable comparator but is not a; no Phase 5 training campaign or physical-residual promotion is authorized;; completed Phase 6 evidence:; all `969` raw conditions and `99,696,607` rows were audited with strictly; all directional validity windows pass the speed-stability check;; no transition passes the fourfold robust P95 acceleration-separation gate;; load inertia, commanded drive law, repeated dynamic trajectories, and; no Phase 6 training campaign or physical-residual promotion is authorized;; completed Phase 7 evidence:; six evidence files and eleven required quantities were verified;; angle, torque, and direction are causal, while stiffness, clearance,; `PINN-K1` through `PINN-K5` are synthetic-only and `PINN-K6` is blocked;; no Phase 7 training campaign or physical-residual promotion is authorized;; completed Phase 8 evidence:; five evidence files, eleven quantities, and five `PINN-E` candidates were; output power is reconstructable only as a one-sided proxy;; input power, internal force, friction loss, and efficiency are absent;; `PINN-E1/E2` are synthetic-only, `PINN-E5` is offline-only, and; no Phase 8 training campaign or physical-residual promotion is authorized;; completed Phase 9 evidence:; six evidence files, eight quantities, and five `PINN-G` candidates were; nominal geometry exists, while unit metrology, multi-instance identity,; `PINN-G1/G2/G3` are synthetic-only and `PINN-G4/G5` are blocked;; MMT remains deferred and no Phase 9 training or residual is authorized;; completed Phase 10 evidence:; three evidence files, eight quantities, and five `PINN-W` candidates were; operating inputs exist, but reducer identity, chronology, load cycles,; `PINN-W2/W3/W4` are synthetic-only and `PINN-W1/W5` are blocked;; no Phase 10 training campaign or physical residual is authorized;; completed Phase 11 evidence:; three evidence files, eight quantities, and four `PINN-M` candidates were; mechanical channels exist, but synchronized electrical, sideband, health,; `PINN-M2/M4` are synthetic-only and `PINN-M1/M3` are blocked;; no Phase 11 training campaign or physical residual is authorized;; completed Phase 12 evidence:; four evidence files, eight quantities, and six `PINN-R` candidates were; five hybrid architectures are empirically trainable but none is full-PINN; `PINN-R5` is blocked because no validated physical regime gate exists;; no Phase 12 full-PINN campaign or physical residual is authorized;; completed Phase 13 evidence:; all thirteen phase-evidence files and twelve formulation families were; zero isolated candidates are full-PINN eligible;; the tournament closed as no contest without training or a fabricated; completed Phase 14 evidence:; four evidence files, eight requirements, and eight planned integrations; zero promoted components are available against a minimum requirement of; no integrated campaign or combined residual is authorized;; completed Phase 15 evidence:; four final evidence files and all five Wave 6 entry prerequisites were; all five physics-integrated entry prerequisites fail;; no campaign, residual, or automatic phase advance is authorized;; updated priority: preserve reopening conditions and, if desired, prepare a; mandatory rule: prepare or justify `global`, `forward`, and `backward`; paper-reproduction scope:; prepare explicit PINN model and physics-loss formulations for later; test whether soft physics, periodicity, smoothness, harmonic-consistency,; keep online compensation execution out of Wave 5.2 unless Track 3 is; completed inventory conclusions:; known geometry constants are safe for diagnostics and feature generation;; operating metadata can be used for stratification and causal conditioning;; five equivalent-error groups are train-only calibratable;; contact geometry remains unavailable or ambiguous and blocks calibrated; measured TE remains target-only and must not become an inference input.; MMT-specific closed implementation conclusions:; exact-manifest replay preserves all archived model artifacts and split; 224 metadata, geometry, combined, and shuffled comparisons were fitted on; geometry-locked MMT signatures produced zero incremental held-out gain;; 56 calibrated equivalent-error arms were explicitly blocked because; no MMT feature, auxiliary-output, weak-loss, or paper-faithful MMT; MMT future TODO reopening gate:; obtain independent component-error measurements or a validated causal; prove that the resulting MMT inputs vary by operating condition without; create a new technical document and, if training is proposed, a new; until those conditions are met, the MMT-paper-faithful subbranch is not; general full-PINN evidence gates:; register and synthesize each supplied reference;; verify equations, units, assumptions, observability, identifiability,; test equations against measured curves and synthetic or analytical oracles; prepare a separate approved technical document and campaign plan for one; apply multi-index curve-first verification before accepting, combining, or; use validated findings to define the later Wave 6 architecture. |

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
| `wave52r_offline_leader_cross_surface_promotion_2026_07_30` | `2026-07-31 11:18:11` | 27 | 0 | `K01`, provisional scalar `Fw` winner | No registry promotion; official `Fw`/`Bw`/`global` curve-first verification pending |
| `wave52r_stage4_data_only_residual_capacity_2026_07_28` | `2026-07-28 11:19:25` | 18 | 0 | `te_stage4_h08_r5_deep__polished_setpoints_fw` | Updated stage4_h08_r5_deep family best |
| `wave52r_stage4_data_only_residual_capacity_2026_07_28` | `2026-07-28 10:00:02` | 0 | 1 | N/A | No winner artifact |
| `phase3_c1_fw_stability_repeat_2026_07_26` | `2026-07-26 20:07:49` | 2 | 0 | `te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints` | Updated phase3_pinn_c1_linear_compliance_soft_fw_seed_314159 family best |
| `phase3_quasi_static_compliance_pinn_2026_07_26` | `2026-07-26 19:23:35` | 12 | 0 | `te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints` | Updated phase3_pinn_c1_linear_compliance_soft_fw family best |
| `phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26` | `2026-07-26 16:38:48` | 8 | 0 | `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints` | No family-best change |

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
| `periodic_gru_sequence_global` | `te_periodic_gru_sequence_global` | `periodic_gru_sequence` | 0.001132 | 0.001159 | 0.001465 | 157,569 | N/A | Unknown | Implemented Benchmark |
| `periodic_lstm_sequence_global` | `te_periodic_lstm_sequence_global` | `periodic_lstm_sequence` | 0.001185 | 0.001187 | 0.001505 | 210,049 | N/A | Unknown | Implemented Benchmark |
| `periodic_mlp_harmonic_global` | `te_periodic_mlp_harmonic_global` | `periodic_mlp` | 0.001196 | 0.001264 | 0.001737 | 28,417 | N/A | Unknown | Implemented Benchmark |
| `periodic_gru_sequence` | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | 0.001274 | 0.001279 | 0.001638 | 157,569 | 1.82 MB | High | Implemented Benchmark |
| `wave4_3_mixture_density_k3_global` | `te_wave4_3_mixture_density_k3_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001407 | 0.001544 | 0.001992 | 86,976 | N/A | Unknown | Implemented Benchmark |
| `tree_global` | `te_tree_global__polished_setpoints` | `hist_gradient_boosting` | 0.001498 | 0.001699 | 0.002947 | 5 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_mlp_global` | `te_residual_harmonic_mlp_global` | `residual_harmonic_mlp` | 0.001621 | 0.001710 | 0.002307 | 26,138 | N/A | Unknown | Implemented Benchmark |
| `feedforward_global` | `te_feedforward_global` | `feedforward` | 0.001637 | 0.001734 | 0.002220 | 109,697 | N/A | Unknown | Implemented Benchmark |
| `periodic_mlp_global` | `te_periodic_mlp_global` | `periodic_mlp` | 0.001655 | 0.001741 | 0.002333 | 27,137 | N/A | Unknown | Implemented Benchmark |
| `wave4_3_mixture_density_k2_global` | `te_wave4_3_mixture_density_k2_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001550 | 0.001743 | 0.002245 | 86,400 | N/A | Unknown | Implemented Benchmark |
| `tree` | `te_hist_gbr_tabular_global` | `hist_gradient_boosting` | 0.001591 | 0.001753 | 0.002892 | 4 | 0.44 MB | Very Low | Implemented Benchmark |
| `wave4_2_quantile_p10_p50_p90_global` | `te_wave4_2_quantile_p10_p50_p90_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001728 | 0.001878 | 0.002428 | 85,824 | N/A | Unknown | Implemented Benchmark |
| `wave4_1_mae_robust_loss_global` | `te_wave4_1_mae_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001754 | 0.001890 | 0.002443 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave4_1_log_cosh_robust_loss_global` | `te_wave4_1_log_cosh_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001776 | 0.001913 | 0.002459 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave3_2_harmonic_residual_offset_global` | `te_wave3_2_harmonic_residual_offset_global` | `harmonic_residual_offset_probe` | 0.001783 | 0.001914 | 0.002470 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_raw_centered_shape_curve_aware_global` | `te_wave3_3_raw_centered_shape_curve_aware_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001797 | 0.001954 | 0.002494 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_curve_aware_pointwise_control_global` | `te_wave3_3_curve_aware_pointwise_control_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001837 | 0.001971 | 0.002514 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `periodic_temporal_convolution_global` | `te_periodic_temporal_convolution_global__polished_actual_values` | `periodic_temporal_convolution` | 0.001908 | 0.001999 | 0.002971 | 158,529 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_raw_offset_curve_aware_global` | `te_wave3_3_raw_offset_curve_aware_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001870 | 0.002001 | 0.003029 | 85,747 | N/A | Unknown | Implemented Benchmark |
| `wave4_2_gaussian_nll_global` | `te_wave4_2_gaussian_nll_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001825 | 0.002001 | 0.002576 | 85,632 | N/A | Unknown | Implemented Benchmark |
| `track2g_curve_aware_harmonic_residual_offset_full_curve_composite_global` | `te_track2g_curve_aware_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001872 | 0.002008 | 0.002581 | 85,440 | 1.00 MB | High | Implemented Benchmark |
| `wave4_1_smooth_l1_robust_loss_global` | `te_wave4_1_smooth_l1_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001866 | 0.002017 | 0.002559 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_full_curve_composite_global` | `te_wave3_3_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001894 | 0.002023 | 0.002587 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c0_learned_mean_control_global` | `te_phase3_pinn_c0_learned_mean_control_global__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001977 | 0.002050 | 0.002529 | 7,212 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | `te_residual_harmonic_lstm_sequence_sparse_rcim_global` | `residual_harmonic_lstm_sequence` | 0.001954 | 0.002062 | 0.002651 | 200,852 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | `te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.001938 | 0.002062 | 0.003120 | 151,060 | N/A | Unknown | Implemented Benchmark |
| `harmonic_regression_global` | `te_harmonic_regression_global__polished_actual_values` | `harmonic_regression` | 0.001823 | 0.002071 | 0.003143 | 150 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_gru_sequence_dense240_global` | `te_residual_harmonic_gru_sequence_dense240_global` | `residual_harmonic_gru_sequence` | 0.001967 | 0.002076 | 0.002660 | 151,138 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_gru_sequence_dense360_global` | `te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.001960 | 0.002088 | 0.003113 | 151,762 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c5_shared_stiffness_global` | `te_phase3_pinn_c5_shared_stiffness_global__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002448 | 0.002103 | 0.002550 | 5,611 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_gru_sequence_sparse_rcim` | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.001978 | 0.002112 | 0.002699 | 150,676 | 1.74 MB | Medium | Implemented Benchmark |
| `wave5_1_harmonic_prior_smooth_l1_structured_global` | `te_wave5_1_harmonic_prior_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | 0.001870 | 0.002119 | 0.002712 | 7,168 | N/A | Unknown | Implemented Benchmark |
| `wave5_1_harmonic_prior_pointwise_control_global` | `te_wave5_1_harmonic_prior_pointwise_control_global` | `wave3_harmonic_prior_residual` | 0.001894 | 0.002159 | 0.002754 | 7,168 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_dense240_global` | `te_residual_harmonic_lstm_sequence_dense240_global` | `residual_harmonic_lstm_sequence` | 0.002031 | 0.002161 | 0.002748 | 201,314 | N/A | Unknown | Implemented Benchmark |
| `wave3_harmonic_prior_residual_smooth_l1_structured_global` | `te_wave3_harmonic_prior_residual_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | 0.001889 | 0.002168 | 0.002763 | 7,168 | 0.10 MB | Medium | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global` | `wave52b_offset_harmonic_guided` | 0.001886 | 0.002215 | 0.002799 | 22,593 | 0.30 MB | High | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_dense360_global` | `te_residual_harmonic_lstm_sequence_dense360_global` | `residual_harmonic_lstm_sequence` | 0.002071 | 0.002223 | 0.002815 | 201,554 | N/A | Unknown | Implemented Benchmark |
| `gru_sequence_global` | `te_gru_sequence_global` | `gru_sequence` | 0.002126 | 0.002229 | 0.002872 | 150,657 | N/A | Unknown | Implemented Benchmark |
| `lstm_sequence_global` | `te_lstm_sequence_global` | `lstm_sequence` | 0.002151 | 0.002258 | 0.002894 | 200,833 | N/A | Unknown | Implemented Benchmark |
| `wave3_1_sequential_residual_offset_probe_global` | `te_wave3_1_sequential_residual_offset_probe_global` | `sequential_residual_offset_probe` | 0.002147 | 0.002261 | 0.002896 | 92,418 | N/A | Unknown | Implemented Benchmark |
| `wave4_4_gru_latent_offset_residual_global` | `te_wave4_4_gru_latent_offset_residual_global__polished_actual_values` | `latent_state_hysteresis_probe` | 0.002173 | 0.002271 | 0.003341 | 125,475 | N/A | Unknown | Implemented Benchmark |
| `wave3_2_clean_sequential_residual_offset_global` | `te_wave3_2_clean_sequential_residual_offset_global` | `sequential_residual_offset_probe` | 0.002158 | 0.002276 | 0.002910 | 92,418 | N/A | Unknown | Implemented Benchmark |
| `wave4_4_causal_tcn_latent_offset_residual_global` | `te_wave4_4_causal_tcn_latent_offset_residual_global` | `latent_state_hysteresis_probe` | 0.002217 | 0.002315 | 0.002986 | 97,155 | N/A | Unknown | Implemented Benchmark |
| `temporal_convolution_global` | `te_temporal_convolution_global__polished_actual_values` | `temporal_convolution` | 0.002191 | 0.002327 | 0.003391 | 147,009 | N/A | Unknown | Implemented Benchmark |
| `track2h_latent_state_hysteresis_gru_offset_residual_global` | `te_track2h_l_gru_offset_residual_global` | `latent_state_hysteresis_probe` | 0.002232 | 0.002339 | 0.002986 | 124,899 | 1.48 MB | Medium | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_pointwise_control_global` | `te_wave52b_offset_harmonic_guided_pointwise_control_global` | `wave52b_offset_harmonic_guided` | 0.002210 | 0.002461 | 0.003142 | 22,593 | 0.30 MB | High | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_offset_head_global` | `te_wave52b_offset_harmonic_guided_offset_head_global` | `wave52b_offset_harmonic_guided` | 0.002249 | 0.002483 | 0.003166 | 22,593 | 0.30 MB | High | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_offset_centered_shape_global` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_global` | `wave52b_offset_harmonic_guided` | 0.002271 | 0.002540 | 0.003229 | 22,593 | 0.30 MB | High | Implemented Benchmark |
| `periodic_lstm_sequence` | `te_periodic_lstm_sequence_remote_global` | `periodic_lstm_sequence` | 0.002526 | 0.002682 | 0.002969 | 210,561 | 2.43 MB | High | Implemented Benchmark |
| `feedforward` | `te_feedforward_trial` | `feedforward` | 0.002725 | 0.002877 | 0.003835 | 26,113 | 0.32 MB | Low | Current Plain MLP Anchor |
| `track2h_quantile_probabilistic_gaussian_nll_global` | `te_track2h_gaussian_nll_global` | `curve_aware_harmonic_residual_offset_probe` | 0.003267 | 0.003013 | 0.003388 | 85,958 | 1.00 MB | High | Implemented Benchmark |
| `residual_harmonic_mlp` | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.002895 | 0.003034 | 0.003550 | 26,266 | 0.32 MB | Unknown | Implemented Benchmark |
| `periodic_mlp` | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.002994 | 0.003186 | 0.003690 | 27,265 | 0.33 MB | Unknown | Implemented Benchmark |
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
| `harmonic_regression` | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.003904 | 0.003839 | 0.004555 | 125 | 0.01 MB | Low | Implemented Benchmark |
| `feedforward_recovery_micro` | `te_feedforward_optuna_recovery_micro_global_optuna_t0000` | `feedforward` | 0.004266 | 0.004164 | 0.005109 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |
| `feedforward_recovery_probe_dense` | `te_feedforward_optuna_recovery_probe_dense_global_optuna_t0000` | `feedforward` | 0.004257 | 0.004602 | 0.005262 | 109,953 | 1.28 MB | Unknown | Implemented Benchmark |

### Forward Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `periodic_gru_sequence_fw` | `te_periodic_gru_sequence_fw` | `periodic_gru_sequence` | 0.001099 | 0.001101 | 0.001409 | 157,569 | N/A | Unknown | Implemented Benchmark |
| `shape_objective_periodic_mlp_harmonic_fw` | `te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints` | `periodic_mlp` | 0.001429 | 0.001236 | 0.001672 | 28,545 | N/A | Unknown | Implemented Benchmark |
| `causal_offset_mean_periodic_mlp_harmonic_fw` | `te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints` | `periodic_mlp` | 0.001469 | 0.001277 | 0.001739 | 28,545 | N/A | Unknown | Implemented Benchmark |
| `periodic_mlp_harmonic_fw` | `te_periodic_mlp_harmonic_fw` | `periodic_mlp` | 0.001144 | 0.001326 | 0.001780 | 28,417 | N/A | Unknown | Implemented Benchmark |
| `phase2_pinn_h0_fourier_control_fw` | `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001418 | 0.001354 | 0.001620 | 5,635 | N/A | Unknown | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` | `wave52b_offset_harmonic_guided` | 0.001809 | 0.001392 | 0.001771 | 22,593 | 0.30 MB | Medium | Implemented Benchmark |
| `shape_objective_v3_periodic_gru_sequence_fw` | `te_shape_objective_v3_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.001820 | 0.001400 | 0.001756 | 157,953 | N/A | Unknown | Implemented Benchmark |
| `shape_first_distilled_periodic_mlp_harmonic_fw` | `te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints` | `periodic_mlp` | 0.001573 | 0.001420 | 0.001866 | 28,545 | N/A | Unknown | Implemented Benchmark |
| `stage4_h08_r5_deep` | `te_stage4_h08_r5_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001490 | 0.001455 | 0.001825 | 7,187 | N/A | Unknown | Implemented Benchmark |
| `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw` | `te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.001983 | 0.001463 | 0.001831 | 157,953 | N/A | Unknown | Implemented Benchmark |
| `shape_objective_curve_aware_residual_fw` | `te_shape_objective_curve_aware_residual_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.001972 | 0.001463 | 0.001854 | 85,747 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c1_linear_compliance_soft_fw_seed_314159` | `te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001676 | 0.001472 | 0.001864 | 7,212 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c1_linear_compliance_soft_fw` | `te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001702 | 0.001495 | 0.001887 | 7,212 | N/A | Unknown | Implemented Benchmark |
| `shape_first_distilled_periodic_gru_sequence_fw` | `te_shape_first_distilled_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.002004 | 0.001523 | 0.001920 | 157,953 | N/A | Unknown | Implemented Benchmark |
| `periodic_lstm_sequence_fw` | `te_periodic_lstm_sequence_fw` | `periodic_lstm_sequence` | 0.001495 | 0.001547 | 0.001976 | 210,049 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c2_temperature_compliance_soft_fw` | `te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001672 | 0.001551 | 0.001950 | 7,212 | N/A | Unknown | Implemented Benchmark |
| `stage4_c04_r1_deep` | `te_stage4_c04_r1_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001828 | 0.001609 | 0.002010 | 6,901 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c0_learned_mean_control_fw` | `te_phase3_pinn_c0_learned_mean_control_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001774 | 0.001611 | 0.002017 | 7,212 | N/A | Unknown | Implemented Benchmark |
| `stage4_h02_r2_deep` | `te_stage4_h02_r2_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001630 | 0.001617 | 0.002030 | 7,745 | N/A | Unknown | Implemented Benchmark |
| `stage4_c03_r1_compact` | `te_stage4_c03_r1_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001874 | 0.001620 | 0.002066 | 1,485 | N/A | Unknown | Implemented Benchmark |
| `stage4_c01_r1_compact` | `te_stage4_c01_r1_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001835 | 0.001624 | 0.002065 | 1,825 | N/A | Unknown | Implemented Benchmark |
| `stage4_c05_r1_compact` | `te_stage4_c05_r1_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001835 | 0.001624 | 0.002065 | 1,825 | N/A | Unknown | Implemented Benchmark |
| `stage4_c06_r1_deep` | `te_stage4_c06_r1_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001915 | 0.001665 | 0.002134 | 7,139 | N/A | Unknown | Implemented Benchmark |
| `wave4_3_mixture_density_k3_fw` | `te_wave4_3_mixture_density_k3_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001501 | 0.001671 | 0.002181 | 86,976 | N/A | Unknown | Implemented Benchmark |
| `wave4_3_mixture_density_k2_fw` | `te_wave4_3_mixture_density_k2_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001493 | 0.001698 | 0.002196 | 86,400 | N/A | Unknown | Implemented Benchmark |
| `tree_fw` | `te_tree_fw__polished_setpoints` | `hist_gradient_boosting` | 0.001498 | 0.001699 | 0.002947 | 5 | N/A | Unknown | Implemented Benchmark |
| `stage4_h07_r5_compact` | `te_stage4_h07_r5_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001765 | 0.001725 | 0.002119 | 1,843 | N/A | Unknown | Implemented Benchmark |
| `feedforward_fw` | `te_feedforward_fw` | `feedforward` | 0.001628 | 0.001726 | 0.002205 | 109,697 | N/A | Unknown | Implemented Benchmark |
| `periodic_mlp_fw` | `te_periodic_mlp_fw` | `periodic_mlp` | 0.001597 | 0.001742 | 0.002329 | 27,137 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c3_nonlinear_compliance_soft_fw` | `te_phase3_pinn_c3_nonlinear_compliance_soft_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001942 | 0.001745 | 0.002209 | 7,212 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_mlp_fw` | `te_residual_harmonic_mlp_fw__polished_setpoints` | `residual_harmonic_mlp` | 0.001599 | 0.001759 | 0.002336 | 26,266 | N/A | Unknown | Implemented Benchmark |
| `stage4_c02_r1_deep` | `te_stage4_c02_r1_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.002001 | 0.001760 | 0.002226 | 7,745 | N/A | Unknown | Implemented Benchmark |
| `phase2_pinn_h2_oscillator_periodic_closure_fw` | `te_phase2_pinn_h2_oscillator_periodic_closure_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.002074 | 0.001784 | 0.002245 | 16,570 | N/A | Unknown | Implemented Benchmark |
| `stage4_a01_r2_compact` | `te_stage4_a01_r2_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.002265 | 0.001878 | 0.002393 | 1,825 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c1_linear_compliance_soft_fw_seed_271828` | `te_phase3_pinn_c1_linear_compliance_soft_fw_seed_271828__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002123 | 0.001898 | 0.002340 | 7,212 | N/A | Unknown | Implemented Benchmark |
| `wave4_2_gaussian_nll_fw` | `te_wave4_2_gaussian_nll_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001739 | 0.001914 | 0.002482 | 85,632 | N/A | Unknown | Implemented Benchmark |
| `wave4_2_quantile_p10_p50_p90_fw` | `te_wave4_2_quantile_p10_p50_p90_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001731 | 0.001914 | 0.002457 | 85,824 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_raw_centered_shape_curve_aware_fw` | `te_wave3_3_raw_centered_shape_curve_aware_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001789 | 0.001917 | 0.002466 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_curve_aware_pointwise_control_fw` | `te_wave3_3_curve_aware_pointwise_control_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001792 | 0.001919 | 0.002463 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave4_1_log_cosh_robust_loss_fw` | `te_wave4_1_log_cosh_robust_loss_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001807 | 0.001921 | 0.002465 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `stage4_a03_r5_compact` | `te_stage4_a03_r5_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.002057 | 0.001926 | 0.002382 | 2,033 | N/A | Unknown | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_offset_centered_shape_fw` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_fw` | `wave52b_offset_harmonic_guided` | 0.002258 | 0.001931 | 0.002445 | 22,593 | 0.30 MB | Medium | Implemented Benchmark |
| `stage4_h01_r2_compact` | `te_stage4_h01_r2_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.002123 | 0.001940 | 0.002397 | 1,825 | N/A | Unknown | Implemented Benchmark |
| `wave3_2_harmonic_residual_offset_fw` | `te_wave3_2_harmonic_residual_offset_fw` | `harmonic_residual_offset_probe` | 0.001809 | 0.001948 | 0.002507 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_offset_head_fw` | `te_wave52b_offset_harmonic_guided_offset_head_fw` | `wave52b_offset_harmonic_guided` | 0.002256 | 0.001948 | 0.002454 | 22,593 | 0.30 MB | Medium | Implemented Benchmark |
| `phase2_pinn_h1_oscillator_residual_fw` | `te_phase2_pinn_h1_oscillator_residual_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.002127 | 0.001951 | 0.002401 | 16,570 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_raw_offset_curve_aware_fw` | `te_wave3_3_raw_offset_curve_aware_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001833 | 0.001953 | 0.002499 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave4_1_smooth_l1_robust_loss_fw` | `te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001835 | 0.001956 | 0.002999 | 85,747 | N/A | Unknown | Implemented Benchmark |
| `wave4_1_mae_robust_loss_fw` | `te_wave4_1_mae_robust_loss_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001806 | 0.001961 | 0.002502 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `stage4_h06_r4_deep` | `te_stage4_h06_r4_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.002177 | 0.001965 | 0.002572 | 6,857 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_full_curve_composite_fw` | `te_wave3_3_full_curve_composite_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001898 | 0.002038 | 0.002607 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_pointwise_control_fw` | `te_wave52b_offset_harmonic_guided_pointwise_control_fw` | `wave52b_offset_harmonic_guided` | 0.002344 | 0.002054 | 0.002564 | 22,593 | 0.30 MB | Medium | Implemented Benchmark |
| `residual_harmonic_gru_sequence_sparse_rcim_fw` | `te_residual_harmonic_gru_sequence_sparse_rcim_fw` | `residual_harmonic_gru_sequence` | 0.001942 | 0.002056 | 0.002645 | 150,676 | N/A | Unknown | Implemented Benchmark |
| `harmonic_regression_fw` | `te_harmonic_regression_fw__polished_actual_values` | `harmonic_regression` | 0.001823 | 0.002066 | 0.003135 | 150 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_sparse_rcim_fw` | `te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.001951 | 0.002067 | 0.003129 | 201,364 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_gru_sequence_dense360_fw` | `te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.001955 | 0.002074 | 0.003114 | 151,762 | N/A | Unknown | Implemented Benchmark |
| `periodic_temporal_convolution_fw` | `te_periodic_temporal_convolution_fw__polished_actual_values` | `periodic_temporal_convolution` | 0.001939 | 0.002077 | 0.003080 | 158,529 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c4_hard_elastic_offset_fw` | `te_phase3_pinn_c4_hard_elastic_offset_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002301 | 0.002087 | 0.002481 | 5,611 | N/A | Unknown | Implemented Benchmark |
| `causal_offset_mean_gru_sequence_fw` | `te_causal_offset_mean_gru_sequence_fw__polished_setpoints` | `sequential_residual_offset_probe` | 0.002428 | 0.002100 | 0.002610 | 92,802 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_gru_sequence_dense240_fw` | `te_residual_harmonic_gru_sequence_dense240_fw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.001969 | 0.002101 | 0.003138 | 151,522 | N/A | Unknown | Implemented Benchmark |
| `stage4_h05_r4_compact` | `te_stage4_h05_r4_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.002346 | 0.002111 | 0.002707 | 1,513 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_dense240_fw` | `te_residual_harmonic_lstm_sequence_dense240_fw` | `residual_harmonic_lstm_sequence` | 0.002044 | 0.002147 | 0.002745 | 201,314 | N/A | Unknown | Implemented Benchmark |
| `wave5_1_harmonic_prior_smooth_l1_structured_fw` | `te_wave5_1_harmonic_prior_smooth_l1_structured_fw` | `wave3_harmonic_prior_residual` | 0.001912 | 0.002151 | 0.002745 | 7,168 | N/A | Unknown | Implemented Benchmark |
| `wave5_1_harmonic_prior_pointwise_control_fw` | `te_wave5_1_harmonic_prior_pointwise_control_fw` | `wave3_harmonic_prior_residual` | 0.001913 | 0.002185 | 0.002776 | 7,168 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_dense360_fw` | `te_residual_harmonic_lstm_sequence_dense360_fw` | `residual_harmonic_lstm_sequence` | 0.002066 | 0.002219 | 0.002819 | 201,554 | N/A | Unknown | Implemented Benchmark |
| `lstm_sequence_fw` | `te_lstm_sequence_fw__polished_actual_values` | `lstm_sequence` | 0.002151 | 0.002239 | 0.003319 | 201,345 | N/A | Unknown | Implemented Benchmark |
| `wave3_1_sequential_residual_offset_probe_fw` | `te_wave3_1_sequential_residual_offset_probe_fw` | `sequential_residual_offset_probe` | 0.002154 | 0.002246 | 0.002893 | 92,418 | N/A | Unknown | Implemented Benchmark |
| `gru_sequence_fw` | `te_gru_sequence_fw` | `gru_sequence` | 0.002130 | 0.002247 | 0.002882 | 150,657 | N/A | Unknown | Implemented Benchmark |
| `wave3_2_clean_sequential_residual_offset_fw` | `te_wave3_2_clean_sequential_residual_offset_fw` | `sequential_residual_offset_probe` | 0.002159 | 0.002258 | 0.002897 | 92,418 | N/A | Unknown | Implemented Benchmark |
| `wave4_4_gru_latent_offset_residual_fw` | `te_wave4_4_gru_latent_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.002201 | 0.002300 | 0.002953 | 124,899 | N/A | Unknown | Implemented Benchmark |
| `wave4_4_causal_tcn_latent_offset_residual_fw` | `te_wave4_4_causal_tcn_latent_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.002224 | 0.002316 | 0.002980 | 97,155 | N/A | Unknown | Implemented Benchmark |
| `phase2_pinn_h3_oscillator_periodic_bauer_anchor_fw` | `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.002898 | 0.002389 | 0.003042 | 16,570 | N/A | Unknown | Implemented Benchmark |
| `temporal_convolution_fw` | `te_temporal_convolution_fw__polished_actual_values` | `temporal_convolution` | 0.002272 | 0.002390 | 0.003496 | 147,009 | N/A | Unknown | Implemented Benchmark |
| `shape_gate_loss_pilot_periodic_gru_sequence_fw` | `te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.002297 | 0.002522 | 0.003133 | 157,953 | N/A | Unknown | Implemented Benchmark |
| `stage4_a04_r5_compact` | `te_stage4_a04_r5_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.003065 | 0.002846 | 0.003546 | 2,033 | N/A | Unknown | Implemented Benchmark |
| `track2f_bis_harmonic_residual_offset_fw` | `te_track2f_bis_harmonic_residual_offset_fw` | `harmonic_residual_offset_probe` | 0.002941 | 0.002862 | 0.003334 | 85,747 | 1.00 MB | Very Low | Implemented Benchmark |
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
| `stage4_a02_r2_compact` | `te_stage4_a02_r2_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.006336 | 0.005241 | 0.006491 | 1,825 | N/A | Unknown | Implemented Benchmark |
| `stage4_h03_r3_compact` | `te_stage4_h03_r3_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.058291 | 0.046115 | 0.055988 | 1,825 | N/A | Unknown | Implemented Benchmark |
| `stage4_h04_r3_deep` | `te_stage4_h04_r3_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.058330 | 0.046188 | 0.055998 | 7,745 | N/A | Unknown | Implemented Benchmark |

### Backward Models

| Family | Best Run | Model Type | Val MAE [deg] | Test MAE [deg] | Test RMSE [deg] | Params | Artifact Size | Training Cost | Current Role |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| `periodic_gru_sequence_bw` | `te_periodic_gru_sequence_bw` | `periodic_gru_sequence` | 0.001088 | 0.001084 | 0.001393 | 157,569 | N/A | Unknown | Current Program Winner |
| `periodic_lstm_sequence_bw` | `te_periodic_lstm_sequence_bw` | `periodic_lstm_sequence` | 0.001230 | 0.001226 | 0.001558 | 210,049 | N/A | Unknown | Implemented Benchmark |
| `periodic_mlp_harmonic_bw` | `te_periodic_mlp_harmonic_bw` | `periodic_mlp` | 0.001103 | 0.001279 | 0.001719 | 28,417 | N/A | Unknown | Implemented Benchmark |
| `phase2_pinn_h0_fourier_control_bw` | `te_phase2_pinn_h0_fourier_control_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001624 | 0.001498 | 0.001809 | 5,635 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c2_temperature_compliance_soft_bw` | `te_phase3_pinn_c2_temperature_compliance_soft_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001727 | 0.001624 | 0.002068 | 7,212 | N/A | Unknown | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw` | `wave52b_offset_harmonic_guided` | 0.002320 | 0.001677 | 0.002151 | 22,593 | 0.30 MB | Medium | Implemented Benchmark |
| `feedforward_bw` | `te_feedforward_bw` | `feedforward` | 0.001630 | 0.001686 | 0.002175 | 109,697 | N/A | Unknown | Implemented Benchmark |
| `tree_bw` | `te_tree_bw__polished_setpoints` | `hist_gradient_boosting` | 0.001498 | 0.001699 | 0.002947 | 5 | N/A | Unknown | Implemented Benchmark |
| `wave4_3_mixture_density_k3_bw` | `te_wave4_3_mixture_density_k3_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001519 | 0.001704 | 0.002205 | 86,976 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_mlp_bw` | `te_residual_harmonic_mlp_bw` | `residual_harmonic_mlp` | 0.001609 | 0.001712 | 0.002294 | 26,138 | N/A | Unknown | Implemented Benchmark |
| `phase2_pinn_h1_oscillator_residual_bw` | `te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001856 | 0.001723 | 0.002210 | 16,570 | N/A | Unknown | Implemented Benchmark |
| `wave4_3_mixture_density_k2_bw` | `te_wave4_3_mixture_density_k2_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001528 | 0.001725 | 0.002226 | 86,400 | N/A | Unknown | Implemented Benchmark |
| `periodic_mlp_bw` | `te_periodic_mlp_bw` | `periodic_mlp` | 0.001658 | 0.001740 | 0.002328 | 27,137 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c0_learned_mean_control_bw` | `te_phase3_pinn_c0_learned_mean_control_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001927 | 0.001825 | 0.002313 | 7,212 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c1_linear_compliance_soft_bw` | `te_phase3_pinn_c1_linear_compliance_soft_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001970 | 0.001877 | 0.002386 | 7,212 | N/A | Unknown | Implemented Benchmark |
| `wave4_2_quantile_p10_p50_p90_bw` | `te_wave4_2_quantile_p10_p50_p90_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001741 | 0.001888 | 0.002435 | 85,824 | N/A | Unknown | Implemented Benchmark |
| `wave3_2_harmonic_residual_offset_bw` | `te_wave3_2_harmonic_residual_offset_bw` | `harmonic_residual_offset_probe` | 0.001791 | 0.001894 | 0.002440 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_raw_offset_curve_aware_bw` | `te_wave3_3_raw_offset_curve_aware_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001768 | 0.001898 | 0.002445 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave4_1_log_cosh_robust_loss_bw` | `te_wave4_1_log_cosh_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001766 | 0.001899 | 0.002442 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave4_1_mae_robust_loss_bw` | `te_wave4_1_mae_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001757 | 0.001907 | 0.002455 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_raw_centered_shape_curve_aware_bw` | `te_wave3_3_raw_centered_shape_curve_aware_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001804 | 0.001916 | 0.002460 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_curve_aware_pointwise_control_bw` | `te_wave3_3_curve_aware_pointwise_control_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001815 | 0.001925 | 0.002473 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c3_nonlinear_compliance_soft_bw` | `te_phase3_pinn_c3_nonlinear_compliance_soft_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002038 | 0.001926 | 0.002441 | 7,212 | N/A | Unknown | Implemented Benchmark |
| `wave4_2_gaussian_nll_bw` | `te_wave4_2_gaussian_nll_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001778 | 0.001927 | 0.002482 | 85,632 | N/A | Unknown | Implemented Benchmark |
| `phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw` | `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.002087 | 0.001931 | 0.002469 | 16,570 | N/A | Unknown | Implemented Benchmark |
| `phase2_pinn_h2_oscillator_periodic_closure_bw` | `te_phase2_pinn_h2_oscillator_periodic_closure_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.002018 | 0.001966 | 0.002545 | 16,570 | N/A | Unknown | Implemented Benchmark |
| `wave4_1_smooth_l1_robust_loss_bw` | `te_wave4_1_smooth_l1_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001851 | 0.001968 | 0.002515 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_pointwise_control_bw` | `te_wave52b_offset_harmonic_guided_pointwise_control_bw` | `wave52b_offset_harmonic_guided` | 0.002591 | 0.001979 | 0.002587 | 22,593 | 0.30 MB | Medium | Implemented Benchmark |
| `periodic_temporal_convolution_bw` | `te_periodic_temporal_convolution_bw__polished_actual_values` | `periodic_temporal_convolution` | 0.001866 | 0.002001 | 0.003009 | 158,529 | N/A | Unknown | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_offset_head_bw` | `te_wave52b_offset_harmonic_guided_offset_head_bw` | `wave52b_offset_harmonic_guided` | 0.002597 | 0.002008 | 0.002632 | 22,593 | 0.30 MB | Medium | Implemented Benchmark |
| `wave52b_offset_harmonic_guided_offset_centered_shape_bw` | `te_wave52b_offset_harmonic_guided_offset_centered_shape_bw` | `wave52b_offset_harmonic_guided` | 0.002604 | 0.002012 | 0.002626 | 22,593 | 0.30 MB | Medium | Implemented Benchmark |
| `residual_harmonic_gru_sequence_dense240_bw` | `te_residual_harmonic_gru_sequence_dense240_bw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.001942 | 0.002049 | 0.003081 | 151,522 | N/A | Unknown | Implemented Benchmark |
| `wave3_3_full_curve_composite_bw` | `te_wave3_3_full_curve_composite_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001920 | 0.002067 | 0.002638 | 85,440 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_gru_sequence_dense360_bw` | `te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.001960 | 0.002071 | 0.003106 | 151,762 | N/A | Unknown | Implemented Benchmark |
| `harmonic_regression_bw` | `te_harmonic_regression_bw__polished_actual_values` | `harmonic_regression` | 0.001826 | 0.002076 | 0.003150 | 150 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_gru_sequence_sparse_rcim_bw` | `te_residual_harmonic_gru_sequence_sparse_rcim_bw` | `residual_harmonic_gru_sequence` | 0.001955 | 0.002083 | 0.002664 | 150,676 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_dense360_bw` | `te_residual_harmonic_lstm_sequence_dense360_bw` | `residual_harmonic_lstm_sequence` | 0.002007 | 0.002097 | 0.002693 | 201,554 | N/A | Unknown | Implemented Benchmark |
| `wave5_1_harmonic_prior_pointwise_control_bw` | `te_wave5_1_harmonic_prior_pointwise_control_bw` | `wave3_harmonic_prior_residual` | 0.001893 | 0.002105 | 0.002680 | 7,168 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_sparse_rcim_bw` | `te_residual_harmonic_lstm_sequence_sparse_rcim_bw` | `residual_harmonic_lstm_sequence` | 0.001994 | 0.002108 | 0.002694 | 200,852 | N/A | Unknown | Implemented Benchmark |
| `residual_harmonic_lstm_sequence_dense240_bw` | `te_residual_harmonic_lstm_sequence_dense240_bw__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.001985 | 0.002116 | 0.003149 | 201,826 | N/A | Unknown | Implemented Benchmark |
| `wave5_1_harmonic_prior_smooth_l1_structured_bw` | `te_wave5_1_harmonic_prior_smooth_l1_structured_bw` | `wave3_harmonic_prior_residual` | 0.001921 | 0.002178 | 0.002776 | 7,168 | N/A | Unknown | Implemented Benchmark |
| `wave3_1_sequential_residual_offset_probe_bw` | `te_wave3_1_sequential_residual_offset_probe_bw` | `sequential_residual_offset_probe` | 0.002147 | 0.002225 | 0.002871 | 92,418 | N/A | Unknown | Implemented Benchmark |
| `gru_sequence_bw` | `te_gru_sequence_bw` | `gru_sequence` | 0.002119 | 0.002230 | 0.002860 | 150,657 | N/A | Unknown | Implemented Benchmark |
| `lstm_sequence_bw` | `te_lstm_sequence_bw` | `lstm_sequence` | 0.002151 | 0.002240 | 0.002892 | 200,833 | N/A | Unknown | Implemented Benchmark |
| `wave3_2_clean_sequential_residual_offset_bw` | `te_wave3_2_clean_sequential_residual_offset_bw` | `sequential_residual_offset_probe` | 0.002150 | 0.002242 | 0.002885 | 92,418 | N/A | Unknown | Implemented Benchmark |
| `wave4_4_gru_latent_offset_residual_bw` | `te_wave4_4_gru_latent_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.002191 | 0.002260 | 0.002915 | 124,899 | N/A | Unknown | Implemented Benchmark |
| `temporal_convolution_bw` | `te_temporal_convolution_bw__polished_actual_values` | `temporal_convolution` | 0.002198 | 0.002303 | 0.003366 | 147,009 | N/A | Unknown | Implemented Benchmark |
| `wave4_4_causal_tcn_latent_offset_residual_bw` | `te_wave4_4_causal_tcn_latent_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.002204 | 0.002309 | 0.002974 | 97,155 | N/A | Unknown | Implemented Benchmark |
| `phase3_pinn_c4_hard_elastic_offset_bw` | `te_phase3_pinn_c4_hard_elastic_offset_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002758 | 0.002350 | 0.002859 | 5,611 | N/A | Unknown | Implemented Benchmark |
| `track2h_mixture_density_heads_mdn_k2_bw` | `te_track2h_mdn_k2_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002914 | 0.002658 | 0.003198 | 86,802 | 1.01 MB | Medium | Implemented Benchmark |
| `track2h_mixture_density_heads_mdn_k3_bw` | `te_track2h_mdn_k3_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002775 | 0.002721 | 0.003250 | 87,435 | 1.02 MB | Medium | Implemented Benchmark |
| `track2h_quantile_probabilistic_quantile_p10_p50_p90_bw` | `te_track2h_quantile_p10_p50_p90_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003436 | 0.002927 | 0.003519 | 86,169 | 1.01 MB | Medium | Implemented Benchmark |
| `track2h_quantile_probabilistic_gaussian_nll_bw` | `te_track2h_gaussian_nll_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003298 | 0.002998 | 0.003608 | 85,958 | 1.00 MB | Medium | Implemented Benchmark |
| `track2h_dispersion_aware_smooth_l1_robust_bw` | `te_track2h_smooth_l1_robust_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.003372 | 0.003074 | 0.003662 | 85,747 | 1.00 MB | Medium | Implemented Benchmark |
| `track2f_bis_harmonic_residual_offset_bw` | `te_track2f_bis_harmonic_residual_offset_bw` | `harmonic_residual_offset_probe` | 0.003555 | 0.003336 | 0.003935 | 85,747 | 1.00 MB | Very Low | Implemented Benchmark |
| `wave3_harmonic_prior_residual_pointwise_control_bw` | `te_wave3_harmonic_prior_residual_pointwise_control_bw` | `wave3_harmonic_prior_residual` | 0.003634 | 0.003363 | 0.003902 | 7,283 | 0.11 MB | Low | Implemented Benchmark |
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

#### complex_harmonic_coefficient_residuals

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `22`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `2026-07-28-16-17-08__stage5_c01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 2 | `2026-07-28-16-17-08__stage5_c02` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 3 | `2026-07-28-16-17-09__stage5_c03` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 4 | `2026-07-28-16-17-09__stage5_c04` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 5 | `2026-07-28-16-17-10__stage5_c05` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 6 | `2026-07-28-16-17-10__stage5_c06` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 7 | `2026-07-28-16-17-11__stage5_c07` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 8 | `2026-07-28-16-17-11__stage5_c08` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 9 | `2026-07-28-16-17-11__stage5_h01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 10 | `2026-07-28-16-17-12__stage5_h02` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 11 | `2026-07-28-16-17-12__stage5_h03` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 12 | `2026-07-28-16-17-13__stage5_h04` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 13 | `2026-07-28-16-17-13__stage5_h05` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 14 | `2026-07-28-16-17-14__stage5_h06` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 15 | `2026-07-28-16-17-15__stage5_h07` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 16 | `2026-07-28-16-17-15__stage5_h08` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 17 | `2026-07-28-16-17-16__stage5_a01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 18 | `2026-07-28-16-17-16__stage5_a02` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 19 | `2026-07-28-16-19-55__stage5_c04__seed_271828` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 20 | `2026-07-28-16-19-56__stage5_c04__seed_161803` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 21 | `2026-07-28-16-19-56__stage5_h04__seed_161803` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 22 | `2026-07-28-16-19-56__stage5_h04__seed_271828` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |

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
- Completed tracked runs: `16`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_gru_sequence_global` | `gru_sequence` | 0.002229 | 0.002872 | 0.002126 | 150,657 | 56m 28s | 1.74 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_gru_sequence_bw` | `gru_sequence` | 0.002230 | 0.002860 | 0.002119 | 150,657 | 33m 29s | 1.74 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_gru_sequence_fw` | `gru_sequence` | 0.002247 | 0.002882 | 0.002130 | 150,657 | 29m 54s | 1.74 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_gru_sequence_bw__polished_actual_values` | `gru_sequence` | 0.002258 | 0.003322 | 0.002144 | 151,041 | 35m 34s | 1.74 MB | Very High | Medium | `dataset_input_mode_retraining__gru_sequence__polished_actual_values` |
| 5 | `te_gru_sequence_fw` | `gru_sequence` | 0.002260 | 0.002905 | 0.002156 | 150,657 | 35m 12s | 1.74 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_gru_sequence_bw` | `gru_sequence` | 0.002271 | 0.002908 | 0.002147 | 150,657 | 42m 04s | 1.74 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 7 | `te_gru_sequence_fw__polished_actual_values` | `gru_sequence` | 0.002274 | 0.003341 | 0.002165 | 151,041 | 26m 08s | 1.74 MB | Very High | Medium | `dataset_input_mode_retraining__gru_sequence__polished_actual_values` |
| 8 | `te_gru_sequence_global__polished_actual_values` | `gru_sequence` | 0.002292 | 0.003347 | 0.002172 | 151,041 | 27m 43s | 1.74 MB | Very High | Medium | `dataset_input_mode_retraining__gru_sequence__polished_actual_values` |
| 9 | `te_gru_sequence_global` | `gru_sequence` | 0.002311 | 0.002954 | 0.002205 | 150,657 | 15m 38s | 1.74 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 10 | `te_gru_sequence_fw__polished_setpoints` | `gru_sequence` | 0.002431 | 0.003811 | 0.002162 | 151,041 | 29m 18s | 1.74 MB | Very High | Medium | `dataset_input_mode_retraining__gru_sequence__polished_setpoints` |
| 11 | `te_gru_sequence_bw__polished_setpoints` | `gru_sequence` | 0.002467 | 0.003849 | 0.002183 | 151,041 | 16m 24s | 1.74 MB | Very High | Medium | `dataset_input_mode_retraining__gru_sequence__polished_setpoints` |
| 12 | `te_gru_sequence_global__polished_setpoints` | `gru_sequence` | 0.002474 | 0.003853 | 0.002174 | 151,041 | 20m 34s | 1.74 MB | Very High | Medium | `dataset_input_mode_retraining__gru_sequence__polished_setpoints` |
| 13 | `te_gru_sequence_bw__simplified_setpoints` | `gru_sequence` | 0.003510 | 0.004341 | 0.003661 | 151,041 | 15m 40s | 1.74 MB | Very High | Medium | `dataset_input_mode_retraining__gru_sequence__simplified_setpoints` |
| 14 | `te_gru_sequence_fw__simplified_setpoints` | `gru_sequence` | 0.003584 | 0.004393 | 0.003759 | 151,041 | 7m 50s | 1.74 MB | Very High | Low | `dataset_input_mode_retraining__gru_sequence__simplified_setpoints` |
| 15 | `te_gru_sequence_global__simplified_setpoints` | `gru_sequence` | 0.003590 | 0.004451 | 0.003777 | 151,041 | 6m 52s | 1.74 MB | Very High | Low | `dataset_input_mode_retraining__gru_sequence__simplified_setpoints` |
| 16 | `te_gru_sequence_remote_global` | `gru_sequence` | 0.003591 | 0.004110 | 0.003707 | 151,041 | 8m 44s | 1.74 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### mean_centered_shape_multi_head

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `7`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `2026-07-29-17-46-25__stage7_c01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 2 | `2026-07-29-17-46-26__stage7_p01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 3 | `2026-07-29-17-46-26__stage7_s01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 4 | `2026-07-29-17-46-27__stage7_i01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 5 | `2026-07-29-17-46-28__stage7_g01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 6 | `2026-07-29-17-46-29__stage7_a01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 7 | `2026-07-29-17-46-29__stage7_a02` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |

#### periodic_lstm_sequence

- Best run: `te_periodic_lstm_sequence_remote_global`
- Best test MAE: `0.002682`
- Completed tracked runs: `16`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_lstm_sequence_global` | `periodic_lstm_sequence` | 0.001187 | 0.001505 | 0.001185 | 210,049 | 1h 27m 51s | 2.42 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_periodic_lstm_sequence_bw` | `periodic_lstm_sequence` | 0.001226 | 0.001558 | 0.001230 | 210,049 | 46m 38s | 2.42 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_periodic_lstm_sequence_bw` | `periodic_lstm_sequence` | 0.001338 | 0.001719 | 0.001231 | 210,049 | 1h 14m 57s | 2.42 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_periodic_lstm_sequence_fw` | `periodic_lstm_sequence` | 0.001547 | 0.001976 | 0.001495 | 210,049 | 59m 17s | 2.42 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_periodic_lstm_sequence_fw` | `periodic_lstm_sequence` | 0.001555 | 0.001983 | 0.001513 | 210,049 | 29m 41s | 2.42 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_periodic_lstm_sequence_global__polished_setpoints` | `periodic_lstm_sequence` | 0.001561 | 0.002411 | 0.001371 | 210,561 | 39m 46s | 2.43 MB | Very High | Medium | `dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints` |
| 7 | `te_periodic_lstm_sequence_global` | `periodic_lstm_sequence` | 0.001601 | 0.002029 | 0.001536 | 210,049 | 30m 40s | 2.42 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 8 | `te_periodic_lstm_sequence_bw__polished_setpoints` | `periodic_lstm_sequence` | 0.001641 | 0.002567 | 0.001389 | 210,561 | 37m 47s | 2.43 MB | Very High | Medium | `dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints` |
| 9 | `te_periodic_lstm_sequence_global__polished_actual_values` | `periodic_lstm_sequence` | 0.002121 | 0.003300 | 0.001917 | 210,561 | 18m 34s | 2.43 MB | Very High | Medium | `dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values` |
| 10 | `te_periodic_lstm_sequence_fw__polished_setpoints` | `periodic_lstm_sequence` | 0.002176 | 0.003521 | 0.001867 | 210,561 | 13m 51s | 2.43 MB | Very High | Low | `dataset_input_mode_retraining__periodic_lstm_sequence__polished_setpoints` |
| 11 | `te_periodic_lstm_sequence_bw__polished_actual_values` | `periodic_lstm_sequence` | 0.002196 | 0.003476 | 0.001979 | 210,561 | 12m 12s | 2.43 MB | Very High | Low | `dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values` |
| 12 | `te_periodic_lstm_sequence_fw__polished_actual_values` | `periodic_lstm_sequence` | 0.002211 | 0.003527 | 0.001966 | 210,561 | 10m 24s | 2.43 MB | Very High | Low | `dataset_input_mode_retraining__periodic_lstm_sequence__polished_actual_values` |
| 13 | `te_periodic_lstm_sequence_remote_global` | `periodic_lstm_sequence` | 0.002682 | 0.002969 | 0.002526 | 210,561 | 1h 11m 12s | 2.43 MB | Very High | High | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |
| 14 | `te_periodic_lstm_sequence_bw__simplified_setpoints` | `periodic_lstm_sequence` | 0.003349 | 0.004076 | 0.003524 | 210,561 | 10m 59s | 2.43 MB | Very High | Low | `dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints` |
| 15 | `te_periodic_lstm_sequence_global__simplified_setpoints` | `periodic_lstm_sequence` | 0.003369 | 0.004027 | 0.003533 | 210,561 | 9m 05s | 2.43 MB | Very High | Low | `dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints` |
| 16 | `te_periodic_lstm_sequence_fw__simplified_setpoints` | `periodic_lstm_sequence` | 0.003390 | 0.004150 | 0.003483 | 210,561 | 12m 42s | 2.43 MB | Very High | Low | `dataset_input_mode_retraining__periodic_lstm_sequence__simplified_setpoints` |

#### periodic_mlp_harmonic

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `15`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_harmonic_global` | `periodic_mlp` | 0.001264 | 0.001737 | 0.001196 | 28,417 | 42m 19s | 0.35 MB | Medium | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_periodic_mlp_harmonic_global__polished_setpoints` | `periodic_mlp` | 0.001270 | 0.002217 | 0.001137 | 28,545 | 29m 32s | 0.35 MB | Medium | Medium | `dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints` |
| 3 | `te_periodic_mlp_harmonic_bw` | `periodic_mlp` | 0.001279 | 0.001719 | 0.001103 | 28,417 | 39m 46s | 0.35 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_periodic_mlp_harmonic_bw__polished_actual_values` | `periodic_mlp` | 0.001303 | 0.002220 | 0.001171 | 28,545 | 25m 00s | 0.35 MB | Medium | Medium | `dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values` |
| 5 | `te_periodic_mlp_harmonic_global` | `periodic_mlp` | 0.001309 | 0.001794 | 0.001265 | 28,417 | 15m 47s | 0.35 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_periodic_mlp_harmonic_fw` | `periodic_mlp` | 0.001326 | 0.001780 | 0.001144 | 28,417 | 38m 01s | 0.35 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 7 | `te_periodic_mlp_harmonic_bw` | `periodic_mlp` | 0.001342 | 0.001807 | 0.001188 | 28,417 | 20m 48s | 0.35 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 8 | `te_periodic_mlp_harmonic_fw` | `periodic_mlp` | 0.001360 | 0.001845 | 0.001209 | 28,417 | 17m 10s | 0.35 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 9 | `te_periodic_mlp_harmonic_fw__polished_setpoints` | `periodic_mlp` | 0.001442 | 0.002411 | 0.001208 | 28,545 | 13m 32s | 0.35 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints` |
| 10 | `te_periodic_mlp_harmonic_bw__polished_setpoints` | `periodic_mlp` | 0.001442 | 0.002380 | 0.001219 | 28,545 | 13m 51s | 0.35 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp_harmonic__polished_setpoints` |
| 11 | `te_periodic_mlp_harmonic_global__polished_actual_values` | `periodic_mlp` | 0.001445 | 0.002405 | 0.001238 | 28,545 | 18m 11s | 0.35 MB | Medium | Medium | `dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values` |
| 12 | `te_periodic_mlp_harmonic_fw__polished_actual_values` | `periodic_mlp` | 0.001590 | 0.002522 | 0.001311 | 28,545 | 13m 24s | 0.35 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp_harmonic__polished_actual_values` |
| 13 | `te_periodic_mlp_harmonic_fw__simplified_setpoints` | `periodic_mlp` | 0.003065 | 0.003709 | 0.002803 | 28,545 | 8m 09s | 0.35 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints` |
| 14 | `te_periodic_mlp_harmonic_global__simplified_setpoints` | `periodic_mlp` | 0.003293 | 0.003865 | 0.002847 | 28,545 | 8m 22s | 0.35 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints` |
| 15 | `te_periodic_mlp_harmonic_bw__simplified_setpoints` | `periodic_mlp` | 0.003377 | 0.004054 | 0.002803 | 28,545 | 7m 49s | 0.35 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp_harmonic__simplified_setpoints` |

#### periodic_temporal_convolution

- Best run: `te_periodic_temporal_convolution_sequence_remote_global`
- Best test MAE: `0.003508`
- Completed tracked runs: `16`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_temporal_convolution_global__polished_actual_values` | `periodic_temporal_convolution` | 0.001999 | 0.002971 | 0.001908 | 158,529 | 25m 34s | 1.83 MB | Very High | Medium | `dataset_input_mode_retraining__periodic_temporal_convolution__polished_actual_values` |
| 2 | `te_periodic_temporal_convolution_bw__polished_actual_values` | `periodic_temporal_convolution` | 0.002001 | 0.003009 | 0.001866 | 158,529 | 22m 45s | 1.83 MB | Very High | Medium | `dataset_input_mode_retraining__periodic_temporal_convolution__polished_actual_values` |
| 3 | `te_periodic_temporal_convolution_fw__polished_actual_values` | `periodic_temporal_convolution` | 0.002077 | 0.003080 | 0.001939 | 158,529 | 21m 42s | 1.83 MB | Very High | Medium | `dataset_input_mode_retraining__periodic_temporal_convolution__polished_actual_values` |
| 4 | `te_periodic_temporal_convolution_bw` | `periodic_temporal_convolution` | 0.002174 | 0.002734 | 0.002077 | 157,889 | 15m 34s | 1.82 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_periodic_temporal_convolution_fw` | `periodic_temporal_convolution` | 0.002178 | 0.002730 | 0.002065 | 157,889 | 31m 41s | 1.82 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_periodic_temporal_convolution_global__polished_setpoints` | `periodic_temporal_convolution` | 0.002236 | 0.003541 | 0.001961 | 158,529 | 14m 24s | 1.83 MB | Very High | Low | `dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints` |
| 7 | `te_periodic_temporal_convolution_bw` | `periodic_temporal_convolution` | 0.002238 | 0.002791 | 0.002161 | 157,889 | 27m 06s | 1.82 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 8 | `te_periodic_temporal_convolution_fw__polished_setpoints` | `periodic_temporal_convolution` | 0.002252 | 0.003578 | 0.001945 | 158,529 | 12m 56s | 1.83 MB | Very High | Low | `dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints` |
| 9 | `te_periodic_temporal_convolution_bw__polished_setpoints` | `periodic_temporal_convolution` | 0.002264 | 0.003555 | 0.001969 | 158,529 | 13m 01s | 1.83 MB | Very High | Low | `dataset_input_mode_retraining__periodic_temporal_convolution__polished_setpoints` |
| 10 | `te_periodic_temporal_convolution_fw` | `periodic_temporal_convolution` | 0.002280 | 0.002848 | 0.002209 | 157,889 | 15m 25s | 1.82 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 11 | `te_periodic_temporal_convolution_global` | `periodic_temporal_convolution` | 0.002302 | 0.002863 | 0.002160 | 157,889 | 14m 09s | 1.82 MB | Very High | Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 12 | `te_periodic_temporal_convolution_global` | `periodic_temporal_convolution` | 0.002319 | 0.002900 | 0.002202 | 157,889 | 22m 15s | 1.82 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 13 | `te_periodic_temporal_convolution_bw__simplified_setpoints` | `periodic_temporal_convolution` | 0.003388 | 0.004127 | 0.003553 | 158,529 | 9m 43s | 1.83 MB | Very High | Low | `dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints` |
| 14 | `te_periodic_temporal_convolution_global__simplified_setpoints` | `periodic_temporal_convolution` | 0.003436 | 0.004106 | 0.003600 | 158,529 | 9m 38s | 1.83 MB | Very High | Low | `dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints` |
| 15 | `te_periodic_temporal_convolution_fw__simplified_setpoints` | `periodic_temporal_convolution` | 0.003474 | 0.004188 | 0.003645 | 158,529 | 5m 56s | 1.83 MB | Very High | Low | `dataset_input_mode_retraining__periodic_temporal_convolution__simplified_setpoints` |
| 16 | `te_periodic_temporal_convolution_sequence_remote_global` | `periodic_temporal_convolution` | 0.003508 | 0.003929 | 0.003634 | 158,529 | 25m 37s | 1.83 MB | Very High | Medium | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### residual_harmonic_lstm_sequence_sparse_rcim

- Best run: `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim`
- Best test MAE: `0.003368`
- Completed tracked runs: `13`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_sparse_rcim_global` | `residual_harmonic_lstm_sequence` | 0.002062 | 0.002651 | 0.001954 | 200,852 | 32m 00s | 2.32 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.002067 | 0.003129 | 0.001951 | 201,364 | 50m 38s | 2.32 MB | Very High | High | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values` |
| 3 | `te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.002097 | 0.003168 | 0.001960 | 201,364 | 52m 27s | 2.32 MB | Very High | High | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values` |
| 4 | `te_residual_harmonic_lstm_sequence_sparse_rcim_bw` | `residual_harmonic_lstm_sequence` | 0.002108 | 0.002694 | 0.001994 | 200,852 | 20m 29s | 2.32 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_residual_harmonic_lstm_sequence_sparse_rcim_fw` | `residual_harmonic_lstm_sequence` | 0.002121 | 0.002711 | 0.001971 | 200,852 | 24m 30s | 2.32 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_setpoints` | `residual_harmonic_lstm_sequence` | 0.002325 | 0.003669 | 0.002045 | 201,364 | 22m 35s | 2.32 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_setpoints` |
| 7 | `te_residual_harmonic_lstm_sequence_sparse_rcim_global__polished_setpoints` | `residual_harmonic_lstm_sequence` | 0.002349 | 0.003726 | 0.002043 | 201,364 | 16m 24s | 2.32 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_setpoints` |
| 8 | `te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_setpoints` | `residual_harmonic_lstm_sequence` | 0.002361 | 0.003733 | 0.002023 | 201,364 | 24m 55s | 2.32 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_setpoints` |
| 9 | `te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.002413 | 0.003764 | 0.002154 | 201,364 | 12m 50s | 2.32 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__polished_actual_values` |
| 10 | `te_residual_harmonic_lstm_sequence_remote_global_sparse_rcim` | `residual_harmonic_lstm_sequence` | 0.003368 | 0.003808 | 0.003632 | 201,364 | 9m 32s | 2.32 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |
| 11 | `te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | 0.003372 | 0.004162 | 0.003678 | 201,364 | 14m 14s | 2.32 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints` |
| 12 | `te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints` | `residual_harmonic_lstm_sequence` | 0.003400 | 0.004178 | 0.003618 | 201,364 | 16m 39s | 2.32 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints` |
| 13 | `te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | 0.003449 | 0.004232 | 0.003654 | 201,364 | 13m 48s | 2.32 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_sparse_rcim__simplified_setpoints` |

#### residual_harmonic_mlp

- Best run: `te_residual_h12_deep_joint_wave1_global_optuna_t0006`
- Best test MAE: `0.003034`
- Completed tracked runs: `21`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_mlp_global` | `residual_harmonic_mlp` | 0.001710 | 0.002307 | 0.001621 | 26,138 | 22m 28s | 0.32 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_residual_harmonic_mlp_bw` | `residual_harmonic_mlp` | 0.001712 | 0.002294 | 0.001609 | 26,138 | 40m 41s | 0.32 MB | Medium | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_residual_harmonic_mlp_bw__polished_setpoints` | `residual_harmonic_mlp` | 0.001725 | 0.002305 | 0.001626 | 26,266 | 26m 08s | 0.32 MB | Medium | Medium | `dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints` |
| 4 | `te_residual_harmonic_mlp_global__polished_setpoints` | `residual_harmonic_mlp` | 0.001758 | 0.002348 | 0.001582 | 26,266 | 28m 05s | 0.32 MB | Medium | Medium | `dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints` |
| 5 | `te_residual_harmonic_mlp_fw__polished_setpoints` | `residual_harmonic_mlp` | 0.001759 | 0.002336 | 0.001599 | 26,266 | 34m 12s | 0.32 MB | Medium | Medium | `dataset_input_mode_retraining__residual_harmonic_mlp__polished_setpoints` |
| 6 | `te_residual_harmonic_mlp_bw__polished_actual_values` | `residual_harmonic_mlp` | 0.001771 | 0.002344 | 0.001606 | 26,266 | 32m 26s | 0.32 MB | Medium | Medium | `dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values` |
| 7 | `te_residual_harmonic_mlp_fw` | `residual_harmonic_mlp` | 0.001783 | 0.002349 | 0.001632 | 26,138 | 19m 27s | 0.32 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 8 | `te_residual_harmonic_mlp_global__polished_actual_values` | `residual_harmonic_mlp` | 0.001795 | 0.002375 | 0.001603 | 26,266 | 30m 13s | 0.32 MB | Medium | Medium | `dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values` |
| 9 | `te_residual_harmonic_mlp_bw` | `residual_harmonic_mlp` | 0.001799 | 0.002380 | 0.001637 | 26,138 | 16m 36s | 0.32 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 10 | `te_residual_harmonic_mlp_fw` | `residual_harmonic_mlp` | 0.001808 | 0.002420 | 0.001647 | 26,138 | 24m 31s | 0.32 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 11 | `te_residual_harmonic_mlp_fw__polished_actual_values` | `residual_harmonic_mlp` | 0.001816 | 0.002399 | 0.001639 | 26,266 | 25m 05s | 0.32 MB | Medium | Medium | `dataset_input_mode_retraining__residual_harmonic_mlp__polished_actual_values` |
| 12 | `te_residual_harmonic_mlp_global` | `residual_harmonic_mlp` | 0.001841 | 0.002433 | 0.001660 | 26,138 | 33m 07s | 0.32 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 13 | `te_residual_h12_deep_joint_wave1_global_optuna_t0006` | `residual_harmonic_mlp` | 0.003034 | 0.003550 | 0.002895 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 14 | `te_residual_h12_deep_joint_wave1_global_optuna_t0010` | `residual_harmonic_mlp` | 0.003067 | 0.003568 | 0.002903 | 26,258 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 15 | `te_residual_h12_deep_joint_wave1` | `residual_harmonic_mlp` | 0.003152 | 0.003640 | 0.003024 | 26,266 | N/A | 0.32 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_residual_harmonic_dense240_tracking_global` | `residual_harmonic_mlp` | 0.003162 | 0.003598 | 0.002976 | 26,722 | 11m 07s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 17 | `te_residual_harmonic_mlp_fw__simplified_setpoints` | `residual_harmonic_mlp` | 0.003218 | 0.003723 | 0.003064 | 26,266 | 15m 23s | 0.32 MB | Medium | Medium | `dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints` |
| 18 | `te_residual_harmonic_rcim_sparse_tracking_global` | `residual_harmonic_mlp` | 0.003378 | 0.003902 | 0.002969 | 26,260 | 8m 03s | 0.32 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 19 | `te_residual_harmonic_mlp_bw__simplified_setpoints` | `residual_harmonic_mlp` | 0.003380 | 0.003868 | 0.003065 | 26,266 | 11m 55s | 0.32 MB | Medium | Low | `dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints` |
| 20 | `te_residual_harmonic_dense360_tracking_global` | `residual_harmonic_mlp` | 0.003434 | 0.003957 | 0.002943 | 26,962 | 13m 52s | 0.33 MB | Medium | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 21 | `te_residual_harmonic_mlp_global__simplified_setpoints` | `residual_harmonic_mlp` | 0.003548 | 0.004086 | 0.003158 | 26,266 | 8m 18s | 0.32 MB | Medium | Low | `dataset_input_mode_retraining__residual_harmonic_mlp__simplified_setpoints` |

#### sequential_residual_offset_probe

- Best run: `te_sequential_residual_offset_probe_remote_global`
- Best test MAE: `0.003537`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_sequential_residual_offset_probe_remote_global` | `sequential_residual_offset_probe` | 0.003537 | 0.004005 | 0.003783 | 92,802 | 9m 22s | 1.09 MB | High | Low | `track2f_offset_aware_probe_campaign_2026_06_03` |

#### spectral_sobolev_guidance

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `15`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `2026-07-29-15-34-06__stage6_c01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 2 | `2026-07-29-15-34-07__stage6_c02` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 3 | `2026-07-29-15-34-08__stage6_c03` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 4 | `2026-07-29-15-34-08__stage6_c04` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 5 | `2026-07-29-15-34-09__stage6_d01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 6 | `2026-07-29-15-34-10__stage6_s02` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 7 | `2026-07-29-15-34-11__stage6_ds01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 8 | `2026-07-29-15-34-12__stage6_ds02` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 9 | `2026-07-29-15-34-13__stage6_cu01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 10 | `2026-07-29-15-34-13__stage6_fi01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 11 | `2026-07-29-15-34-14__stage6_ff00` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 12 | `2026-07-29-15-34-14__stage6_ff01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 13 | `2026-07-29-15-34-15__stage6_si00` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 14 | `2026-07-29-15-34-15__stage6_si01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 15 | `2026-07-29-15-34-16__stage6_w01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |

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
- Completed tracked runs: `19`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_tree_global__polished_setpoints` | `hist_gradient_boosting` | 0.001699 | 0.002947 | 0.001498 | 5 | 2m 51s | 0.47 MB | Light Artifact | Low | `dataset_input_mode_retraining__tree__polished_setpoints` |
| 2 | `te_tree_fw__polished_setpoints` | `hist_gradient_boosting` | 0.001699 | 0.002947 | 0.001498 | 5 | 2m 36s | 0.47 MB | Light Artifact | Low | `dataset_input_mode_retraining__tree__polished_setpoints` |
| 3 | `te_tree_bw__polished_setpoints` | `hist_gradient_boosting` | 0.001699 | 0.002947 | 0.001498 | 5 | 2m 31s | 0.47 MB | Light Artifact | Low | `dataset_input_mode_retraining__tree__polished_setpoints` |
| 4 | `te_tree_global__polished_actual_values` | `hist_gradient_boosting` | 0.001750 | 0.002892 | 0.001570 | 5 | 2m 41s | 0.44 MB | Light Artifact | Low | `dataset_input_mode_retraining__tree__polished_actual_values` |
| 5 | `te_tree_fw__polished_actual_values` | `hist_gradient_boosting` | 0.001750 | 0.002892 | 0.001570 | 5 | 2m 32s | 0.44 MB | Light Artifact | Low | `dataset_input_mode_retraining__tree__polished_actual_values` |
| 6 | `te_tree_bw__polished_actual_values` | `hist_gradient_boosting` | 0.001750 | 0.002892 | 0.001570 | 5 | 2m 29s | 0.44 MB | Light Artifact | Low | `dataset_input_mode_retraining__tree__polished_actual_values` |
| 7 | `te_hist_gbr_tabular_global` | `hist_gradient_boosting` | 0.001753 | 0.002892 | 0.001591 | 4 | 1m 53s | 0.44 MB | Light Artifact | Very Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 8 | `te_tree_global` | `hist_gradient_boosting` | 0.001753 | 0.002892 | 0.001591 | 4 | 3m 00s | 0.44 MB | Light Artifact | Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 9 | `te_tree_fw` | `hist_gradient_boosting` | 0.001753 | 0.002892 | 0.001591 | 4 | 2m 29s | 0.44 MB | Light Artifact | Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 10 | `te_tree_bw` | `hist_gradient_boosting` | 0.001753 | 0.002892 | 0.001591 | 4 | 2m 24s | 0.44 MB | Light Artifact | Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 11 | `te_tree_global` | `hist_gradient_boosting` | 0.001753 | 0.002892 | 0.001591 | 4 | 2m 16s | 0.44 MB | Light Artifact | Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 12 | `te_tree_fw` | `hist_gradient_boosting` | 0.001753 | 0.002892 | 0.001591 | 4 | 1m 53s | 0.44 MB | Light Artifact | Very Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 13 | `te_tree_bw` | `hist_gradient_boosting` | 0.001753 | 0.002892 | 0.001591 | 4 | 1m 53s | 0.44 MB | Light Artifact | Very Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 14 | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf10` | `hist_gradient_boosting` | 0.002782 | 0.003520 | 0.002655 | 5 | N/A | 0.48 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 15 | `te_hist_gbr_tabular_global_grid_depth10_lr008_leaf20` | `hist_gradient_boosting` | 0.002782 | 0.003520 | 0.002655 | 5 | N/A | 0.48 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 16 | `te_hist_gbr_tabular_global_grid_depth8_lr008_leaf10` | `hist_gradient_boosting` | 0.002830 | 0.003585 | 0.002677 | 5 | N/A | 0.50 MB | Light Artifact | Unknown | `standalone_or_unknown` |
| 17 | `te_tree_global__simplified_setpoints` | `hist_gradient_boosting` | 0.002885 | 0.003607 | 0.002719 | 5 | 2m 03s | 0.62 MB | Light Artifact | Low | `dataset_input_mode_retraining__tree__simplified_setpoints` |
| 18 | `te_tree_fw__simplified_setpoints` | `hist_gradient_boosting` | 0.002885 | 0.003607 | 0.002719 | 5 | 2m 04s | 0.62 MB | Light Artifact | Low | `dataset_input_mode_retraining__tree__simplified_setpoints` |
| 19 | `te_tree_bw__simplified_setpoints` | `hist_gradient_boosting` | 0.002885 | 0.003607 | 0.002719 | 5 | 1m 55s | 0.62 MB | Light Artifact | Very Low | `dataset_input_mode_retraining__tree__simplified_setpoints` |

#### wave3_3_full_curve_composite

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_3_full_curve_composite_global` | `curve_aware_harmonic_residual_offset_probe` | 0.002023 | 0.002587 | 0.001894 | 85,440 | 34m 43s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave3_3_full_curve_composite_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.002038 | 0.002607 | 0.001898 | 85,440 | 25m 54s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave3_3_full_curve_composite_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.002067 | 0.002638 | 0.001920 | 85,440 | 29m 10s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave3_3_full_curve_composite_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002070 | 0.003119 | 0.001944 | 85,747 | 41m 52s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values` |
| 5 | `te_wave3_3_full_curve_composite_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002113 | 0.003176 | 0.001980 | 85,747 | 55m 37s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values` |
| 6 | `te_wave3_3_full_curve_composite_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002169 | 0.003232 | 0.002008 | 85,747 | 38m 19s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_actual_values` |
| 7 | `te_wave3_3_full_curve_composite_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002353 | 0.003715 | 0.002030 | 85,747 | 32m 51s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints` |
| 8 | `te_wave3_3_full_curve_composite_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002353 | 0.003704 | 0.002058 | 85,747 | 40m 00s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints` |
| 9 | `te_wave3_3_full_curve_composite_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002360 | 0.003713 | 0.002037 | 85,747 | 26m 34s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_full_curve_composite__polished_setpoints` |
| 10 | `te_wave3_3_full_curve_composite_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003419 | 0.004198 | 0.003639 | 85,747 | 36m 52s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints` |
| 11 | `te_wave3_3_full_curve_composite_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003553 | 0.004307 | 0.003657 | 85,747 | 34m 10s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints` |
| 12 | `te_wave3_3_full_curve_composite_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003575 | 0.004322 | 0.003679 | 85,747 | 30m 41s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_full_curve_composite__simplified_setpoints` |

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

#### wave4_1_mae_robust_loss

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave4_1_mae_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001890 | 0.002443 | 0.001754 | 85,440 | 50m 21s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave4_1_mae_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001907 | 0.002455 | 0.001757 | 85,440 | 52m 16s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave4_1_mae_robust_loss_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001961 | 0.002502 | 0.001806 | 85,440 | 26m 51s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave4_1_mae_robust_loss_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002010 | 0.003415 | 0.001734 | 85,747 | 49m 15s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_actual_values` |
| 5 | `te_wave4_1_mae_robust_loss_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002013 | 0.003329 | 0.001787 | 85,747 | 47m 12s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_actual_values` |
| 6 | `te_wave4_1_mae_robust_loss_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002047 | 0.003417 | 0.001768 | 85,747 | 43m 48s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_actual_values` |
| 7 | `te_wave4_1_mae_robust_loss_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002109 | 0.003545 | 0.001792 | 85,747 | 31m 29s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints` |
| 8 | `te_wave4_1_mae_robust_loss_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002113 | 0.003548 | 0.001788 | 85,747 | 47m 04s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints` |
| 9 | `te_wave4_1_mae_robust_loss_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002150 | 0.003545 | 0.001832 | 85,747 | 27m 59s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_mae_robust_loss__polished_setpoints` |
| 10 | `te_wave4_1_mae_robust_loss_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003478 | 0.004271 | 0.003555 | 85,747 | 29m 25s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints` |
| 11 | `te_wave4_1_mae_robust_loss_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003512 | 0.004289 | 0.003586 | 85,747 | 22m 13s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints` |
| 12 | `te_wave4_1_mae_robust_loss_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003561 | 0.004316 | 0.003644 | 85,747 | 17m 35s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_mae_robust_loss__simplified_setpoints` |

#### wave4_2_quantile_p10_p50_p90

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `15`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave4_2_quantile_p10_p50_p90_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001878 | 0.002428 | 0.001728 | 85,824 | 59m 14s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave4_2_quantile_p10_p50_p90_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001888 | 0.002435 | 0.001741 | 85,824 | 45m 41s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave4_2_quantile_p10_p50_p90_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001914 | 0.002457 | 0.001731 | 85,824 | 59m 28s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave4_2_quantile_p10_p50_p90_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001918 | 0.003007 | 0.001768 | 86,169 | 56m 11s | 1.01 MB | High | High | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values` |
| 5 | `te_wave4_2_quantile_p10_p50_p90_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001934 | 0.003029 | 0.001774 | 86,169 | 42m 47s | 1.01 MB | High | High | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values` |
| 6 | `te_wave4_2_quantile_p10_p50_p90_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001952 | 0.003074 | 0.001788 | 86,169 | 29m 32s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_actual_values` |
| 7 | `te_wave4_2_quantile_p10_p50_p90_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002095 | 0.003519 | 0.001795 | 86,169 | 33m 37s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints` |
| 8 | `te_wave4_2_quantile_p10_p50_p90_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002133 | 0.003542 | 0.001817 | 86,169 | 24m 02s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints` |
| 9 | `te_wave4_2_quantile_p10_p50_p90_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002141 | 0.003552 | 0.001801 | 86,169 | 39m 27s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__polished_setpoints` |
| 10 | `te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003342 | 0.004121 | 0.003537 | 86,169 | 22m 07s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints` |
| 11 | `te_wave4_2_quantile_p10_p50_p90_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003378 | 0.004183 | 0.003516 | 86,169 | 25m 04s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints` |
| 12 | `te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003411 | 0.004192 | 0.003537 | 86,169 | 35m 11s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints` |
| 13 | `te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003443 | 0.004183 | 0.003558 | 86,169 | 27m 14s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints` |
| 14 | `te_wave4_2_quantile_p10_p50_p90_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003466 | 0.004275 | 0.003551 | 86,169 | 25m 51s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints` |
| 15 | `te_wave4_2_quantile_p10_p50_p90_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003496 | 0.004299 | 0.003497 | 86,169 | 27m 58s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_2_quantile_p10_p50_p90__simplified_setpoints` |

#### wave4_3_mixture_density_k3

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave4_3_mixture_density_k3_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001544 | 0.001992 | 0.001407 | 86,976 | 1h 03m 09s | 1.01 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave4_3_mixture_density_k3_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001671 | 0.002181 | 0.001501 | 86,976 | 1h 12m 00s | 1.01 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave4_3_mixture_density_k3_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001704 | 0.002205 | 0.001519 | 86,976 | 54m 20s | 1.01 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave4_3_mixture_density_k3_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001803 | 0.003007 | 0.001615 | 87,435 | 1h 00m 36s | 1.02 MB | High | High | `dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values` |
| 5 | `te_wave4_3_mixture_density_k3_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001980 | 0.003276 | 0.001787 | 87,435 | 40m 40s | 1.02 MB | High | High | `dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values` |
| 6 | `te_wave4_3_mixture_density_k3_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002095 | 0.003487 | 0.001814 | 87,435 | 27m 57s | 1.02 MB | High | Medium | `dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_actual_values` |
| 7 | `te_wave4_3_mixture_density_k3_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002151 | 0.003566 | 0.001846 | 87,435 | 33m 52s | 1.02 MB | High | Medium | `dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints` |
| 8 | `te_wave4_3_mixture_density_k3_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002163 | 0.003572 | 0.001838 | 87,435 | 40m 39s | 1.02 MB | High | High | `dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints` |
| 9 | `te_wave4_3_mixture_density_k3_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002176 | 0.003600 | 0.001834 | 87,435 | 46m 49s | 1.02 MB | High | High | `dataset_input_mode_retraining__wave4_3_mixture_density_k3__polished_setpoints` |
| 10 | `te_wave4_3_mixture_density_k3_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003333 | 0.004103 | 0.003574 | 87,435 | 22m 40s | 1.02 MB | High | Medium | `dataset_input_mode_retraining__wave4_3_mixture_density_k3__simplified_setpoints` |
| 11 | `te_wave4_3_mixture_density_k3_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003460 | 0.004301 | 0.003582 | 87,435 | 25m 04s | 1.02 MB | High | Medium | `dataset_input_mode_retraining__wave4_3_mixture_density_k3__simplified_setpoints` |
| 12 | `te_wave4_3_mixture_density_k3_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003521 | 0.004291 | 0.003613 | 87,435 | 24m 44s | 1.02 MB | High | Medium | `dataset_input_mode_retraining__wave4_3_mixture_density_k3__simplified_setpoints` |

#### wave52b_offset_harmonic_guided_offset_centered_shape_global

- Best run: `te_wave52b_offset_harmonic_guided_offset_centered_shape_global`
- Best test MAE: `0.002540`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_offset_centered_shape_global` | `wave52b_offset_harmonic_guided` | 0.002540 | 0.003229 | 0.002271 | 22,593 | 49m 14s | 0.30 MB | Medium | High | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

#### wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global

- Best run: `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global`
- Best test MAE: `0.002215`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_global` | `wave52b_offset_harmonic_guided` | 0.002215 | 0.002799 | 0.001886 | 22,593 | 46m 25s | 0.30 MB | Medium | High | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

#### wave52b_offset_harmonic_guided_offset_head_global

- Best run: `te_wave52b_offset_harmonic_guided_offset_head_global`
- Best test MAE: `0.002483`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_offset_head_global` | `wave52b_offset_harmonic_guided` | 0.002483 | 0.003166 | 0.002249 | 22,593 | 1h 00m 16s | 0.30 MB | Medium | High | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

#### wave52b_offset_harmonic_guided_pointwise_control_global

- Best run: `te_wave52b_offset_harmonic_guided_pointwise_control_global`
- Best test MAE: `0.002461`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_pointwise_control_global` | `wave52b_offset_harmonic_guided` | 0.002461 | 0.003142 | 0.002210 | 22,593 | 55m 18s | 0.30 MB | Medium | High | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

#### wave5_1_harmonic_prior_smooth_l1_structured

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave5_1_harmonic_prior_smooth_l1_structured_global` | `wave3_harmonic_prior_residual` | 0.002119 | 0.002712 | 0.001870 | 7,168 | 29m 36s | 0.10 MB | Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave5_1_harmonic_prior_smooth_l1_structured_fw` | `wave3_harmonic_prior_residual` | 0.002151 | 0.002745 | 0.001912 | 7,168 | 28m 24s | 0.10 MB | Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave5_1_harmonic_prior_smooth_l1_structured_bw` | `wave3_harmonic_prior_residual` | 0.002178 | 0.002776 | 0.001921 | 7,168 | 25m 05s | 0.10 MB | Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |

#### weak_forward_compliance_priors

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `9`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `2026-07-29-18-19-22__stage8_c00` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 2 | `2026-07-29-18-19-25__stage8_s01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 3 | `2026-07-29-18-19-26__stage8_b01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 4 | `2026-07-29-18-19-26__stage8_w01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 5 | `2026-07-29-18-19-27__stage8_t01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 6 | `2026-07-29-18-19-28__stage8_a01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 7 | `2026-07-29-18-19-29__stage8_r01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 8 | `2026-07-29-18-19-30__stage8_n01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |
| 9 | `2026-07-29-18-19-31__stage8_h01` | `unknown` | N/A | N/A | N/A | N/A | N/A | N/A | Unknown | Unknown | `standalone_or_unknown` |

### Forward Models

#### causal_offset_mean_calibration

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `2`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints` | `periodic_mlp` | 0.001277 | 0.001739 | 0.001469 | 28,545 | 7m 42s | 0.35 MB | Medium | Low | `causal_offset_mean_calibration_pilot_2026_07_22` |
| 2 | `te_causal_offset_mean_gru_sequence_fw__polished_setpoints` | `sequential_residual_offset_probe` | 0.002100 | 0.002610 | 0.002428 | 92,802 | 6m 23s | 1.09 MB | High | Low | `causal_offset_mean_calibration_pilot_2026_07_22` |

#### data_only_residual_capacity

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `18`
- Known failed campaign attempts: `1`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_stage4_h08_r5_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001455 | 0.001825 | 0.001490 | 7,187 | 5m 01s | 0.10 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 2 | `te_stage4_c04_r1_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001609 | 0.002010 | 0.001828 | 6,901 | 4m 35s | 0.10 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 3 | `te_stage4_h02_r2_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001617 | 0.002030 | 0.001630 | 7,745 | 5m 08s | 0.11 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 4 | `te_stage4_c03_r1_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001620 | 0.002066 | 0.001874 | 1,485 | 3m 48s | 0.04 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 5 | `te_stage4_c01_r1_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001624 | 0.002065 | 0.001835 | 1,825 | 4m 20s | 0.04 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 6 | `te_stage4_c05_r1_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001624 | 0.002065 | 0.001835 | 1,825 | 4m 16s | 0.04 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 7 | `te_stage4_c06_r1_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001665 | 0.002134 | 0.001915 | 7,139 | 4m 15s | 0.10 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 8 | `te_stage4_h07_r5_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001725 | 0.002119 | 0.001765 | 1,843 | 5m 03s | 0.04 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 9 | `te_stage4_c02_r1_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001760 | 0.002226 | 0.002001 | 7,745 | 2m 58s | 0.11 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 10 | `te_stage4_a01_r2_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001878 | 0.002393 | 0.002265 | 1,825 | 5m 02s | 0.04 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 11 | `te_stage4_a03_r5_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001926 | 0.002382 | 0.002057 | 2,033 | 2m 45s | 0.04 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 12 | `te_stage4_h01_r2_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001940 | 0.002397 | 0.002123 | 1,825 | 5m 11s | 0.04 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 13 | `te_stage4_h06_r4_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.001965 | 0.002572 | 0.002177 | 6,857 | 4m 42s | 0.10 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 14 | `te_stage4_h05_r4_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.002111 | 0.002707 | 0.002346 | 1,513 | 5m 05s | 0.04 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 15 | `te_stage4_a04_r5_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.002846 | 0.003546 | 0.003065 | 2,033 | 3m 13s | 0.04 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 16 | `te_stage4_a02_r2_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.005241 | 0.006491 | 0.006336 | 1,825 | 4m 04s | 0.04 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 17 | `te_stage4_h03_r3_compact__polished_setpoints_fw` | `data_only_residual_capacity` | 0.046115 | 0.055988 | 0.058291 | 1,825 | 4m 44s | 0.04 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |
| 18 | `te_stage4_h04_r3_deep__polished_setpoints_fw` | `data_only_residual_capacity` | 0.046188 | 0.055998 | 0.058330 | 7,745 | 3m 33s | 0.11 MB | Low | Low | `wave52r_stage4_data_only_residual_capacity_2026_07_28` |

Known failed campaign attempts for this family:

- `te_stage4_c01_r1_compact__polished_setpoints_fw` | campaign `wave52r_stage4_data_only_residual_capacity_2026_07_28` | model type `data_only_residual_capacity` | error `Unsupported Model Type for Campaign Runner | data_only_residual_capacity | Supported: ['curve_aware_harmonic_residual_offset_probe', 'feedforward', 'gru_sequence', 'harmonic_kinematic_pinn', 'harmonic_regression', 'harmonic_residual_offset_probe', 'hist_gradient_boosting', 'latent_state_hysteresis_probe', 'lstm_sequence', 'periodic_gru_sequence', 'periodic_lstm_sequence', 'periodic_mlp', 'periodic_temporal_convolution', 'quasi_static_compliance_pinn', 'random_forest', 'residual_harmonic_gru_sequence', 'residual_harmonic_lstm_sequence', 'residual_harmonic_mlp', 'sequential_residual_offset_probe', 'temporal_convolution', 'wave3_harmonic_prior_residual', 'wave52b_offset_harmonic_guided']`

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
- Best test MAE: `0.002247`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_gru_sequence_remote_Fw` | `gru_sequence` | 0.003333 | 0.003881 | 0.003409 | 151,041 | 6m 01s | 1.74 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### harmonic_kinematic_pinn

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `11`
- Known failed campaign attempts: `2`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001354 | 0.001620 | 0.001418 | 5,635 | 12m 34s | 0.08 MB | Low | Low | `phase2_harmonic_kinematic_pinn_common_split_restart_2026_07_26` |
| 2 | `te_phase2_pinn_h0_fourier_control_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001498 | 0.001809 | 0.001624 | 5,635 | 10m 04s | 0.08 MB | Low | Low | `phase2_harmonic_kinematic_pinn_common_split_restart_2026_07_26` |
| 3 | `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001646 | 0.002040 | 0.001852 | 5,635 | 7m 38s | 0.08 MB | Low | Low | `phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26` |
| 4 | `te_phase2_pinn_h0_fourier_control_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001703 | 0.002137 | 0.001847 | 5,635 | 6m 35s | 0.08 MB | Low | Low | `phase2_harmonic_kinematic_pinn_2026_07_26` |
| 5 | `te_phase2_pinn_h1_oscillator_residual_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001723 | 0.002210 | 0.001856 | 16,570 | 35m 24s | 0.27 MB | Medium | Medium | `phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26` |
| 6 | `te_phase2_pinn_h2_oscillator_periodic_closure_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001784 | 0.002245 | 0.002074 | 16,570 | 26m 56s | 0.27 MB | Medium | Medium | `phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26` |
| 7 | `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001931 | 0.002469 | 0.002087 | 16,570 | 22m 02s | 0.27 MB | Medium | Medium | `phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26` |
| 8 | `te_phase2_pinn_h1_oscillator_residual_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001951 | 0.002401 | 0.002127 | 16,570 | 17m 23s | 0.27 MB | Medium | Medium | `phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26` |
| 9 | `te_phase2_pinn_h2_oscillator_periodic_closure_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.001966 | 0.002545 | 0.002018 | 16,570 | 20m 26s | 0.27 MB | Medium | Medium | `phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26` |
| 10 | `te_phase2_pinn_h0_fourier_control_bw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.002066 | 0.002643 | 0.002077 | 5,635 | 4m 43s | 0.08 MB | Low | Low | `phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26` |
| 11 | `te_phase2_pinn_h3_oscillator_periodic_bauer_anchor_fw__polished_setpoints` | `harmonic_kinematic_pinn` | 0.002389 | 0.003042 | 0.002898 | 16,570 | 20m 32s | 0.27 MB | Medium | Medium | `phase2_harmonic_kinematic_pinn_runtime_bounded_restart_2026_07_26` |

Known failed campaign attempts for this family:

- `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints` | campaign `phase2_harmonic_kinematic_pinn_2026_07_26` | model type `harmonic_kinematic_pinn` | error `[Errno 22] Invalid argument`
- `te_phase2_pinn_h0_fourier_control_fw__polished_setpoints` | campaign `phase2_harmonic_kinematic_pinn_2026_07_26` | model type `harmonic_kinematic_pinn` | error `Unsupported Model Type for Campaign Runner | harmonic_kinematic_pinn | Supported: ['curve_aware_harmonic_residual_offset_probe', 'feedforward', 'gru_sequence', 'harmonic_regression', 'harmonic_residual_offset_probe', 'hist_gradient_boosting', 'latent_state_hysteresis_probe', 'lstm_sequence', 'periodic_gru_sequence', 'periodic_lstm_sequence', 'periodic_mlp', 'periodic_temporal_convolution', 'random_forest', 'residual_harmonic_gru_sequence', 'residual_harmonic_lstm_sequence', 'residual_harmonic_mlp', 'sequential_residual_offset_probe', 'temporal_convolution', 'wave3_harmonic_prior_residual', 'wave52b_offset_harmonic_guided']`

#### harmonic_regression

- Best run: `te_harmonic_order12_linear_conditioned_recovery_global`
- Best test MAE: `0.003839`
- Completed tracked runs: `22`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_harmonic_regression_fw__polished_actual_values` | `harmonic_regression` | 0.002066 | 0.003135 | 0.001823 | 150 | 17m 07s | 0.01 MB | Very Low | Medium | `dataset_input_mode_retraining__harmonic_regression__polished_actual_values` |
| 2 | `te_harmonic_regression_global__polished_actual_values` | `harmonic_regression` | 0.002071 | 0.003143 | 0.001823 | 150 | 13m 58s | 0.01 MB | Very Low | Low | `dataset_input_mode_retraining__harmonic_regression__polished_actual_values` |
| 3 | `te_harmonic_regression_bw__polished_actual_values` | `harmonic_regression` | 0.002076 | 0.003150 | 0.001826 | 150 | 13m 53s | 0.01 MB | Very Low | Low | `dataset_input_mode_retraining__harmonic_regression__polished_actual_values` |
| 4 | `te_harmonic_regression_global` | `harmonic_regression` | 0.003795 | 0.004515 | 0.003879 | 125 | 23m 12s | 0.01 MB | Very Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_harmonic_regression_fw` | `harmonic_regression` | 0.003806 | 0.004524 | 0.003887 | 125 | 15m 42s | 0.01 MB | Very Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_harmonic_regression_bw` | `harmonic_regression` | 0.003808 | 0.004519 | 0.003892 | 125 | 11m 29s | 0.01 MB | Very Low | Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 7 | `te_harmonic_regression_bw` | `harmonic_regression` | 0.003811 | 0.004529 | 0.003888 | 125 | 19m 57s | 0.01 MB | Very Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 8 | `te_harmonic_regression_fw` | `harmonic_regression` | 0.003819 | 0.004525 | 0.003900 | 125 | 10m 07s | 0.01 MB | Very Low | Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 9 | `te_harmonic_regression_global` | `harmonic_regression` | 0.003828 | 0.004545 | 0.003899 | 125 | 10m 24s | 0.01 MB | Very Low | Low | `polished_dataset_full_wave_retraining_2026_06_22` |
| 10 | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.003839 | 0.004555 | 0.003904 | 125 | 11m 27s | 0.01 MB | Very Low | Low | `wave1_directional_retraining_campaign_2026_05_06_16_07_16` |
| 11 | `te_harmonic_regression_fw__polished_setpoints` | `harmonic_regression` | 0.018003 | 0.021015 | 0.017150 | 150 | 10m 33s | 0.01 MB | Very Low | Low | `dataset_input_mode_retraining__harmonic_regression__polished_setpoints` |
| 12 | `te_harmonic_regression_bw__polished_setpoints` | `harmonic_regression` | 0.018022 | 0.021014 | 0.017151 | 150 | 10m 14s | 0.01 MB | Very Low | Low | `dataset_input_mode_retraining__harmonic_regression__polished_setpoints` |
| 13 | `te_harmonic_regression_global__polished_setpoints` | `harmonic_regression` | 0.018032 | 0.021021 | 0.017141 | 150 | 10m 51s | 0.01 MB | Very Low | Low | `dataset_input_mode_retraining__harmonic_regression__polished_setpoints` |
| 14 | `te_harmonic_rcim_sparse_tracking_global` | `harmonic_regression` | 0.020767 | 0.022376 | 0.016995 | 114 | 6m 17s | 0.01 MB | Very Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 15 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr00005_stride5` | `harmonic_regression` | 0.020774 | 0.022412 | 0.017025 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 16 | `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr0001_stride1` | `harmonic_regression` | 0.020775 | 0.022417 | 0.017013 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 17 | `te_harmonic_order12_linear_conditioned_recovery_global` | `harmonic_regression` | 0.020779 | 0.022403 | 0.017017 | 150 | N/A | 0.01 MB | Very Low | Unknown | `standalone_or_unknown` |
| 18 | `te_harmonic_dense360_tracking_global` | `harmonic_regression` | 0.020780 | 0.022399 | 0.016991 | 4,326 | 8m 57s | 0.06 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 19 | `te_harmonic_regression_fw__simplified_setpoints` | `harmonic_regression` | 0.020784 | 0.022910 | 0.016996 | 150 | 6m 09s | 0.01 MB | Very Low | Low | `dataset_input_mode_retraining__harmonic_regression__simplified_setpoints` |
| 20 | `te_harmonic_regression_global__simplified_setpoints` | `harmonic_regression` | 0.020784 | 0.022917 | 0.016993 | 150 | 6m 29s | 0.01 MB | Very Low | Low | `dataset_input_mode_retraining__harmonic_regression__simplified_setpoints` |
| 21 | `te_harmonic_dense240_tracking_global` | `harmonic_regression` | 0.020787 | 0.022388 | 0.016989 | 2,886 | 6m 02s | 0.04 MB | Low | Low | `wave1_high_order_harmonic_tracking_campaign_2026_05_19_17_40_01` |
| 22 | `te_harmonic_regression_bw__simplified_setpoints` | `harmonic_regression` | 0.020789 | 0.022914 | 0.016989 | 150 | 6m 28s | 0.01 MB | Very Low | Low | `dataset_input_mode_retraining__harmonic_regression__simplified_setpoints` |

#### harmonic_regression_fw

- Best run: `te_harmonic_regression_fw__polished_actual_values`
- Best test MAE: `0.002066`
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

#### lstm_sequence

- Best run: `te_lstm_sequence_remote_global`
- Best test MAE: `0.003482`
- Completed tracked runs: `16`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_lstm_sequence_fw__polished_actual_values` | `lstm_sequence` | 0.002239 | 0.003319 | 0.002151 | 201,345 | 42m 07s | 2.32 MB | Very High | High | `dataset_input_mode_retraining__lstm_sequence__polished_actual_values` |
| 2 | `te_lstm_sequence_bw` | `lstm_sequence` | 0.002240 | 0.002892 | 0.002151 | 200,833 | 50m 56s | 2.31 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_lstm_sequence_bw__polished_actual_values` | `lstm_sequence` | 0.002253 | 0.003321 | 0.002145 | 201,345 | 43m 50s | 2.32 MB | Very High | High | `dataset_input_mode_retraining__lstm_sequence__polished_actual_values` |
| 4 | `te_lstm_sequence_global` | `lstm_sequence` | 0.002258 | 0.002894 | 0.002151 | 200,833 | 52m 04s | 2.31 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_lstm_sequence_bw` | `lstm_sequence` | 0.002259 | 0.002907 | 0.002147 | 200,833 | 27m 12s | 2.31 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_lstm_sequence_global` | `lstm_sequence` | 0.002265 | 0.002905 | 0.002138 | 200,833 | 29m 43s | 2.31 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 7 | `te_lstm_sequence_fw` | `lstm_sequence` | 0.002266 | 0.002915 | 0.002151 | 200,833 | 47m 50s | 2.31 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 8 | `te_lstm_sequence_global__polished_actual_values` | `lstm_sequence` | 0.002281 | 0.003346 | 0.002189 | 201,345 | 29m 05s | 2.32 MB | Very High | Medium | `dataset_input_mode_retraining__lstm_sequence__polished_actual_values` |
| 9 | `te_lstm_sequence_fw` | `lstm_sequence` | 0.002282 | 0.002920 | 0.002169 | 200,833 | 22m 50s | 2.31 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 10 | `te_lstm_sequence_fw__polished_setpoints` | `lstm_sequence` | 0.002464 | 0.003859 | 0.002191 | 201,345 | 15m 04s | 2.32 MB | Very High | Medium | `dataset_input_mode_retraining__lstm_sequence__polished_setpoints` |
| 11 | `te_lstm_sequence_bw__polished_setpoints` | `lstm_sequence` | 0.002469 | 0.003842 | 0.002200 | 201,345 | 17m 36s | 2.32 MB | Very High | Medium | `dataset_input_mode_retraining__lstm_sequence__polished_setpoints` |
| 12 | `te_lstm_sequence_global__polished_setpoints` | `lstm_sequence` | 0.002470 | 0.003855 | 0.002186 | 201,345 | 20m 05s | 2.32 MB | Very High | Medium | `dataset_input_mode_retraining__lstm_sequence__polished_setpoints` |
| 13 | `te_lstm_sequence_global__simplified_setpoints` | `lstm_sequence` | 0.003446 | 0.004293 | 0.003692 | 201,345 | 14m 41s | 2.32 MB | Very High | Low | `dataset_input_mode_retraining__lstm_sequence__simplified_setpoints` |
| 14 | `te_lstm_sequence_bw__simplified_setpoints` | `lstm_sequence` | 0.003463 | 0.004340 | 0.003677 | 201,345 | 12m 12s | 2.32 MB | Very High | Low | `dataset_input_mode_retraining__lstm_sequence__simplified_setpoints` |
| 15 | `te_lstm_sequence_remote_global` | `lstm_sequence` | 0.003482 | 0.003948 | 0.003681 | 201,345 | 9m 56s | 2.32 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |
| 16 | `te_lstm_sequence_fw__simplified_setpoints` | `lstm_sequence` | 0.003519 | 0.004378 | 0.003702 | 201,345 | 9m 50s | 2.32 MB | Very High | Low | `dataset_input_mode_retraining__lstm_sequence__simplified_setpoints` |

#### lstm_sequence_fw

- Best run: `te_lstm_sequence_fw__polished_actual_values`
- Best test MAE: `0.002239`
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

#### periodic_temporal_convolution_fw

- Best run: `te_periodic_temporal_convolution_fw__polished_actual_values`
- Best test MAE: `0.002077`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_temporal_convolution_sequence_remote_Fw` | `periodic_temporal_convolution` | 0.003337 | 0.003830 | 0.003321 | 158,529 | 8m 15s | 1.83 MB | Very High | Low | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### quasi_static_compliance_pinn

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `14`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_phase3_pinn_c1_linear_compliance_soft_fw_seed_314159__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001472 | 0.001864 | 0.001676 | 7,212 | 7m 36s | 0.11 MB | Low | Low | `phase3_c1_fw_stability_repeat_2026_07_26` |
| 2 | `te_phase3_pinn_c1_linear_compliance_soft_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001495 | 0.001887 | 0.001702 | 7,212 | 7m 36s | 0.11 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |
| 3 | `te_phase3_pinn_c2_temperature_compliance_soft_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001551 | 0.001950 | 0.001672 | 7,212 | 7m 54s | 0.11 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |
| 4 | `te_phase3_pinn_c0_learned_mean_control_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001611 | 0.002017 | 0.001774 | 7,212 | 7m 12s | 0.11 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |
| 5 | `te_phase3_pinn_c2_temperature_compliance_soft_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001624 | 0.002068 | 0.001727 | 7,212 | 7m 39s | 0.11 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |
| 6 | `te_phase3_pinn_c3_nonlinear_compliance_soft_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001745 | 0.002209 | 0.001942 | 7,212 | 7m 40s | 0.11 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |
| 7 | `te_phase3_pinn_c0_learned_mean_control_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001825 | 0.002313 | 0.001927 | 7,212 | 7m 10s | 0.11 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |
| 8 | `te_phase3_pinn_c1_linear_compliance_soft_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001877 | 0.002386 | 0.001970 | 7,212 | 7m 32s | 0.11 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |
| 9 | `te_phase3_pinn_c1_linear_compliance_soft_fw_seed_271828__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001898 | 0.002340 | 0.002123 | 7,212 | 7m 28s | 0.11 MB | Low | Low | `phase3_c1_fw_stability_repeat_2026_07_26` |
| 10 | `te_phase3_pinn_c3_nonlinear_compliance_soft_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.001926 | 0.002441 | 0.002038 | 7,212 | 6m 44s | 0.11 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |
| 11 | `te_phase3_pinn_c0_learned_mean_control_global__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002050 | 0.002529 | 0.001977 | 7,212 | 13m 20s | 0.11 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |
| 12 | `te_phase3_pinn_c4_hard_elastic_offset_fw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002087 | 0.002481 | 0.002301 | 5,611 | 7m 01s | 0.09 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |
| 13 | `te_phase3_pinn_c5_shared_stiffness_global__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002103 | 0.002550 | 0.002448 | 5,611 | 13m 10s | 0.09 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |
| 14 | `te_phase3_pinn_c4_hard_elastic_offset_bw__polished_setpoints` | `quasi_static_compliance_pinn` | 0.002350 | 0.002859 | 0.002758 | 5,611 | 4m 18s | 0.09 MB | Low | Low | `phase3_quasi_static_compliance_pinn_2026_07_26` |

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

#### residual_harmonic_gru_sequence_sparse_rcim

- Best run: `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim`
- Best test MAE: `0.002112`
- Completed tracked runs: `14`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_sparse_rcim_fw` | `residual_harmonic_gru_sequence` | 0.002056 | 0.002645 | 0.001942 | 150,676 | 31m 46s | 1.74 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002062 | 0.003120 | 0.001938 | 151,060 | 39m 39s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values` |
| 3 | `te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002082 | 0.003139 | 0.001951 | 151,060 | 35m 40s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values` |
| 4 | `te_residual_harmonic_gru_sequence_sparse_rcim_bw` | `residual_harmonic_gru_sequence` | 0.002083 | 0.002664 | 0.001955 | 150,676 | 25m 11s | 1.74 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002083 | 0.003142 | 0.001953 | 151,060 | 36m 01s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_actual_values` |
| 6 | `te_residual_harmonic_gru_sequence_sparse_rcim_global` | `residual_harmonic_gru_sequence` | 0.002104 | 0.002690 | 0.001973 | 150,676 | 22m 42s | 1.74 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 7 | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.002112 | 0.002699 | 0.001978 | 150,676 | 24m 21s | 1.74 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |
| 8 | `te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_setpoints` | `residual_harmonic_gru_sequence` | 0.002279 | 0.003659 | 0.001985 | 151,060 | 24m 13s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_setpoints` |
| 9 | `te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_setpoints` | `residual_harmonic_gru_sequence` | 0.002357 | 0.003734 | 0.002032 | 151,060 | 13m 14s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_setpoints` |
| 10 | `te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_setpoints` | `residual_harmonic_gru_sequence` | 0.002369 | 0.003732 | 0.002059 | 151,060 | 10m 38s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__polished_setpoints` |
| 11 | `te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints` | `residual_harmonic_gru_sequence` | 0.003418 | 0.004220 | 0.003602 | 151,060 | 10m 51s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints` |
| 12 | `te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints` | `residual_harmonic_gru_sequence` | 0.003435 | 0.004261 | 0.003598 | 151,060 | 9m 46s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints` |
| 13 | `te_residual_harmonic_gru_sequence_remote_global_sparse_rcim` | `residual_harmonic_gru_sequence` | 0.003440 | 0.003848 | 0.003607 | 151,060 | 11m 44s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |
| 14 | `te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints` | `residual_harmonic_gru_sequence` | 0.003456 | 0.004304 | 0.003581 | 151,060 | 10m 22s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_sparse_rcim__simplified_setpoints` |

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

- Best run: `te_residual_harmonic_mlp_fw__polished_setpoints`
- Best test MAE: `0.001759`
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

#### shape_first_training_rule_distillation

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `2`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints` | `periodic_mlp` | 0.001420 | 0.001866 | 0.001573 | 28,545 | 5m 06s | 0.35 MB | Medium | Low | `shape_first_training_rule_distillation_pilot_2026_07_22` |
| 2 | `te_shape_first_distilled_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.001523 | 0.001920 | 0.002004 | 157,953 | 4m 15s | 1.82 MB | Very High | Low | `shape_first_training_rule_distillation_pilot_2026_07_22` |

#### shape_gate_loss_pilot_periodic_gru_sequence

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.002522 | 0.003133 | 0.002297 | 157,953 | 8m 05s | 1.82 MB | Very High | Low | `shape_gate_loss_pilot_2026_07_20` |

#### shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.001463 | 0.001831 | 0.001983 | 157,953 | 4m 43s | 1.82 MB | Very High | Low | `shape_gate_loss_v2_checkpoint_selection_pilot_2026_07_21` |

#### shape_objective_followup

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_shape_objective_periodic_mlp_harmonic_fw__polished_setpoints` | `periodic_mlp` | 0.001236 | 0.001672 | 0.001429 | 28,545 | 9m 12s | 0.35 MB | Medium | Low | `parallel_shape_objective_followup_2026_07_21` |
| 2 | `te_shape_objective_v3_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.001400 | 0.001756 | 0.001820 | 157,953 | 10m 14s | 1.82 MB | Very High | Low | `parallel_shape_objective_followup_2026_07_21` |
| 3 | `te_shape_objective_curve_aware_residual_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.001463 | 0.001854 | 0.001972 | 85,747 | 8m 01s | 1.00 MB | High | Low | `parallel_shape_objective_followup_2026_07_21` |

#### temporal_convolution_fw

- Best run: `te_temporal_convolution_fw__polished_actual_values`
- Best test MAE: `0.002390`
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

- Best run: `te_tree_fw__polished_setpoints`
- Best test MAE: `0.001699`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002743 | 0.003409 | 0.002677 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 2 | `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf20` | `hist_gradient_boosting` | 0.002743 | 0.003409 | 0.002677 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 3 | `te_hist_gbr_tabular_Fw` | `hist_gradient_boosting` | 0.002845 | 0.003476 | 0.002666 | 5 | N/A | 0.50 MB | Very Low | Unknown | `standalone_or_unknown` |

#### wave3_3_curve_aware_pointwise_control

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_3_curve_aware_pointwise_control_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001919 | 0.002463 | 0.001792 | 85,440 | 40m 19s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave3_3_curve_aware_pointwise_control_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001925 | 0.002473 | 0.001815 | 85,440 | 36m 27s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001943 | 0.002977 | 0.001833 | 85,747 | 57m 11s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values` |
| 4 | `te_wave3_3_curve_aware_pointwise_control_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001971 | 0.002514 | 0.001837 | 85,440 | 27m 33s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_wave3_3_curve_aware_pointwise_control_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001984 | 0.003019 | 0.001850 | 85,747 | 44m 29s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values` |
| 6 | `te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001987 | 0.003027 | 0.001850 | 85,747 | 50m 15s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_actual_values` |
| 7 | `te_wave3_3_curve_aware_pointwise_control_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002239 | 0.003598 | 0.001915 | 85,747 | 30m 14s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_setpoints` |
| 8 | `te_wave3_3_curve_aware_pointwise_control_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002241 | 0.003595 | 0.001931 | 85,747 | 40m 18s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_setpoints` |
| 9 | `te_wave3_3_curve_aware_pointwise_control_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002254 | 0.003612 | 0.001954 | 85,747 | 29m 48s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__polished_setpoints` |
| 10 | `te_wave3_3_curve_aware_pointwise_control_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003400 | 0.004125 | 0.003618 | 85,747 | 26m 58s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints` |
| 11 | `te_wave3_3_curve_aware_pointwise_control_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003445 | 0.004177 | 0.003585 | 85,747 | 35m 06s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints` |
| 12 | `te_wave3_3_curve_aware_pointwise_control_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003495 | 0.004252 | 0.003630 | 85,747 | 27m 25s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_curve_aware_pointwise_control__simplified_setpoints` |

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

#### wave4_1_smooth_l1_robust_loss

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave4_1_smooth_l1_robust_loss_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001956 | 0.002999 | 0.001835 | 85,747 | 56m 18s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values` |
| 2 | `te_wave4_1_smooth_l1_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001968 | 0.002515 | 0.001851 | 85,440 | 24m 11s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave4_1_smooth_l1_robust_loss_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001986 | 0.002536 | 0.001841 | 85,440 | 23m 12s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave4_1_smooth_l1_robust_loss_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002011 | 0.003057 | 0.001894 | 85,747 | 32m 04s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values` |
| 5 | `te_wave4_1_smooth_l1_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | 0.002017 | 0.002559 | 0.001866 | 85,440 | 22m 21s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_wave4_1_smooth_l1_robust_loss_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002028 | 0.003067 | 0.001882 | 85,747 | 36m 44s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_actual_values` |
| 7 | `te_wave4_1_smooth_l1_robust_loss_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002182 | 0.003551 | 0.001902 | 85,747 | 39m 33s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints` |
| 8 | `te_wave4_1_smooth_l1_robust_loss_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002233 | 0.003602 | 0.001929 | 85,747 | 26m 00s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints` |
| 9 | `te_wave4_1_smooth_l1_robust_loss_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002256 | 0.003638 | 0.001938 | 85,747 | 33m 23s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__polished_setpoints` |
| 10 | `te_wave4_1_smooth_l1_robust_loss_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003373 | 0.004139 | 0.003640 | 85,747 | 24m 55s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints` |
| 11 | `te_wave4_1_smooth_l1_robust_loss_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003411 | 0.004234 | 0.003536 | 85,747 | 24m 34s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints` |
| 12 | `te_wave4_1_smooth_l1_robust_loss_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003462 | 0.004219 | 0.003578 | 85,747 | 28m 15s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_smooth_l1_robust_loss__simplified_setpoints` |

#### wave4_2_gaussian_nll

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave4_2_gaussian_nll_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001914 | 0.002482 | 0.001739 | 85,632 | 1h 02m 58s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave4_2_gaussian_nll_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001927 | 0.002482 | 0.001778 | 85,632 | 49m 15s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave4_2_gaussian_nll_global` | `curve_aware_harmonic_residual_offset_probe` | 0.002001 | 0.002576 | 0.001825 | 85,632 | 31m 45s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave4_2_gaussian_nll_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002032 | 0.003297 | 0.001806 | 85,958 | 58m 20s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values` |
| 5 | `te_wave4_2_gaussian_nll_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002113 | 0.003566 | 0.001816 | 85,958 | 57m 47s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values` |
| 6 | `te_wave4_2_gaussian_nll_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002210 | 0.003605 | 0.001882 | 85,958 | 56m 32s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints` |
| 7 | `te_wave4_2_gaussian_nll_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.084400 | 0.105673 | 0.084195 | 85,958 | 9m 58s | 1.00 MB | High | Low | `dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints` |
| 8 | `te_wave4_2_gaussian_nll_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.087134 | 0.109389 | 0.088198 | 85,958 | 9m 59s | 1.00 MB | High | Low | `dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_setpoints` |
| 9 | `te_wave4_2_gaussian_nll_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.092190 | 0.115726 | 0.091721 | 85,958 | 8m 34s | 1.00 MB | High | Low | `dataset_input_mode_retraining__wave4_2_gaussian_nll__simplified_setpoints` |
| 10 | `te_wave4_2_gaussian_nll_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.099431 | 0.123764 | 0.100961 | 85,958 | 8m 28s | 1.00 MB | High | Low | `dataset_input_mode_retraining__wave4_2_gaussian_nll__simplified_setpoints` |
| 11 | `te_wave4_2_gaussian_nll_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.101119 | 0.123836 | 0.101972 | 85,958 | 10m 10s | 1.00 MB | High | Low | `dataset_input_mode_retraining__wave4_2_gaussian_nll__polished_actual_values` |
| 12 | `te_wave4_2_gaussian_nll_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.109411 | 0.135984 | 0.110745 | 85,958 | 8m 22s | 1.00 MB | High | Low | `dataset_input_mode_retraining__wave4_2_gaussian_nll__simplified_setpoints` |

#### wave4_3_mixture_density_k2

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave4_3_mixture_density_k2_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001698 | 0.002196 | 0.001493 | 86,400 | 1h 13m 02s | 1.01 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave4_3_mixture_density_k2_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001725 | 0.002226 | 0.001528 | 86,400 | 49m 12s | 1.01 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave4_3_mixture_density_k2_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001743 | 0.002245 | 0.001550 | 86,400 | 51m 39s | 1.01 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave4_3_mixture_density_k2_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001936 | 0.003224 | 0.001725 | 86,802 | 1h 00m 26s | 1.01 MB | High | High | `dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_actual_values` |
| 5 | `te_wave4_3_mixture_density_k2_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001975 | 0.003299 | 0.001755 | 86,802 | 57m 21s | 1.01 MB | High | High | `dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_actual_values` |
| 6 | `te_wave4_3_mixture_density_k2_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002086 | 0.003379 | 0.001801 | 86,802 | 31m 03s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_actual_values` |
| 7 | `te_wave4_3_mixture_density_k2_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002155 | 0.003552 | 0.001850 | 86,802 | 32m 24s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints` |
| 8 | `te_wave4_3_mixture_density_k2_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002160 | 0.003580 | 0.001817 | 86,802 | 46m 56s | 1.01 MB | High | High | `dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints` |
| 9 | `te_wave4_3_mixture_density_k2_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002221 | 0.003626 | 0.001863 | 86,802 | 37m 16s | 1.01 MB | High | Medium | `dataset_input_mode_retraining__wave4_3_mixture_density_k2__polished_setpoints` |
| 10 | `te_wave4_3_mixture_density_k2_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003256 | 0.004035 | 0.003468 | 86,802 | 49m 25s | 1.01 MB | High | High | `dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints` |
| 11 | `te_wave4_3_mixture_density_k2_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003283 | 0.004147 | 0.003467 | 86,802 | 51m 03s | 1.01 MB | High | High | `dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints` |
| 12 | `te_wave4_3_mixture_density_k2_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003481 | 0.004230 | 0.003608 | 86,802 | 42m 44s | 1.01 MB | High | High | `dataset_input_mode_retraining__wave4_3_mixture_density_k2__simplified_setpoints` |

#### wave52b_offset_harmonic_guided_offset_centered_shape_fw

- Best run: `te_wave52b_offset_harmonic_guided_offset_centered_shape_fw`
- Best test MAE: `0.001931`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_offset_centered_shape_fw` | `wave52b_offset_harmonic_guided` | 0.001931 | 0.002445 | 0.002258 | 22,593 | 36m 47s | 0.30 MB | Medium | Medium | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

#### wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw

- Best run: `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw`
- Best test MAE: `0.001392`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` | `wave52b_offset_harmonic_guided` | 0.001392 | 0.001771 | 0.001809 | 22,593 | 32m 31s | 0.30 MB | Medium | Medium | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

#### wave52b_offset_harmonic_guided_offset_head_fw

- Best run: `te_wave52b_offset_harmonic_guided_offset_head_fw`
- Best test MAE: `0.001948`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_offset_head_fw` | `wave52b_offset_harmonic_guided` | 0.001948 | 0.002454 | 0.002256 | 22,593 | 21m 45s | 0.30 MB | Medium | Medium | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

#### wave52b_offset_harmonic_guided_pointwise_control_fw

- Best run: `te_wave52b_offset_harmonic_guided_pointwise_control_fw`
- Best test MAE: `0.002054`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_pointwise_control_fw` | `wave52b_offset_harmonic_guided` | 0.002054 | 0.002564 | 0.002344 | 22,593 | 18m 48s | 0.30 MB | Medium | Medium | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

### Backward Models

#### feedforward

- Best run: `te_feedforward_trial`
- Best test MAE: `0.002877`
- Completed tracked runs: `19`
- Known failed campaign attempts: `1`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_bw` | `feedforward` | 0.001686 | 0.002175 | 0.001630 | 109,697 | 1h 02m 27s | 1.28 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_feedforward_bw` | `feedforward` | 0.001719 | 0.002205 | 0.001606 | 109,697 | 3h 19m 34s | 1.28 MB | High | Very High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_feedforward_fw` | `feedforward` | 0.001726 | 0.002205 | 0.001628 | 109,697 | 1h 44m 25s | 1.28 MB | High | Very High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_feedforward_global` | `feedforward` | 0.001734 | 0.002220 | 0.001637 | 109,697 | 2h 35m 35s | 1.28 MB | High | Very High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_feedforward_fw__polished_actual_values` | `feedforward` | 0.001758 | 0.002736 | 0.001616 | 109,953 | 34m 06s | 1.28 MB | High | Medium | `dataset_input_mode_retraining__feedforward__polished_actual_values` |
| 6 | `te_feedforward_fw` | `feedforward` | 0.001766 | 0.002254 | 0.001654 | 109,697 | 45m 44s | 1.28 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 7 | `te_feedforward_global` | `feedforward` | 0.001790 | 0.002281 | 0.001672 | 109,697 | 40m 07s | 1.28 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 8 | `te_feedforward_global__polished_actual_values` | `feedforward` | 0.001809 | 0.002784 | 0.001608 | 109,953 | 30m 52s | 1.28 MB | High | Medium | `dataset_input_mode_retraining__feedforward__polished_actual_values` |
| 9 | `te_feedforward_bw__polished_actual_values` | `feedforward` | 0.001833 | 0.002792 | 0.001647 | 109,953 | 22m 41s | 1.28 MB | High | Medium | `dataset_input_mode_retraining__feedforward__polished_actual_values` |
| 10 | `te_feedforward_bw__polished_setpoints` | `feedforward` | 0.001853 | 0.002874 | 0.001641 | 109,953 | 18m 02s | 1.28 MB | High | Medium | `dataset_input_mode_retraining__feedforward__polished_setpoints` |
| 11 | `te_feedforward_fw__polished_setpoints` | `feedforward` | 0.001938 | 0.002950 | 0.001683 | 109,953 | 15m 36s | 1.28 MB | High | Medium | `dataset_input_mode_retraining__feedforward__polished_setpoints` |
| 12 | `te_feedforward_global__polished_setpoints` | `feedforward` | 0.001999 | 0.003006 | 0.001691 | 109,953 | 15m 04s | 1.28 MB | High | Medium | `dataset_input_mode_retraining__feedforward__polished_setpoints` |
| 13 | `te_feedforward_trial` | `feedforward` | 0.002877 | 0.003835 | 0.002725 | 26,113 | 3m 27s | 0.32 MB | Medium | Low | `polished_dataset_stage1_smoke_2026_06_21` |
| 14 | `te_feedforward_stride1_high_compute_long_remote_global` | `feedforward` | 0.003150 | 0.003603 | 0.003056 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 15 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0017` | `feedforward` | 0.003208 | 0.003810 | 0.002962 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0012` | `feedforward` | 0.003217 | 0.003847 | 0.003014 | 43,649 | N/A | 0.52 MB | Medium | Unknown | `standalone_or_unknown` |
| 17 | `te_feedforward_global__simplified_setpoints` | `feedforward` | 0.003243 | 0.003875 | 0.002968 | 109,953 | 18m 18s | 1.28 MB | High | Medium | `dataset_input_mode_retraining__feedforward__simplified_setpoints` |
| 18 | `te_feedforward_bw__simplified_setpoints` | `feedforward` | 0.003341 | 0.003986 | 0.002974 | 109,953 | 21m 55s | 1.28 MB | High | Medium | `dataset_input_mode_retraining__feedforward__simplified_setpoints` |
| 19 | `te_feedforward_fw__simplified_setpoints` | `feedforward` | 0.003423 | 0.004082 | 0.002999 | 109,953 | 13m 30s | 1.28 MB | High | Low | `dataset_input_mode_retraining__feedforward__simplified_setpoints` |

Known failed campaign attempts for this family:

- `te_feedforward_trial` | campaign `polished_dataset_stage1_smoke_2026_06_21` | model type `feedforward` | error `invalid literal for int() with base 10: 'auto'`

#### feedforward_bw

- Best run: `te_feedforward_bw`
- Best test MAE: `0.001686`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005` | `feedforward` | 0.003099 | 0.003630 | 0.003018 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |
| 2 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0013` | `feedforward` | 0.003106 | 0.003700 | 0.002989 | 109,953 | N/A | 1.28 MB | High | Unknown | `standalone_or_unknown` |
| 3 | `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0016` | `feedforward` | 0.003173 | 0.003818 | 0.002901 | 167,937 | N/A | 1.95 MB | Very High | Unknown | `standalone_or_unknown` |

#### gru_sequence_bw

- Best run: `te_gru_sequence_bw`
- Best test MAE: `0.002230`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_gru_sequence_remote_Bw` | `gru_sequence` | 0.003631 | 0.004297 | 0.003867 | 151,041 | 6m 29s | 1.74 MB | Very High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### harmonic_regression_bw

- Best run: `te_harmonic_regression_bw__polished_actual_values`
- Best test MAE: `0.002076`
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
- Completed tracked runs: `17`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_gru_sequence_bw` | `periodic_gru_sequence` | 0.001084 | 0.001393 | 0.001088 | 157,569 | 1h 21m 37s | 1.82 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_periodic_gru_sequence_fw` | `periodic_gru_sequence` | 0.001101 | 0.001409 | 0.001099 | 157,569 | 1h 20m 41s | 1.82 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_periodic_gru_sequence_fw` | `periodic_gru_sequence` | 0.001121 | 0.001444 | 0.001084 | 157,569 | 45m 23s | 1.82 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_periodic_gru_sequence_global` | `periodic_gru_sequence` | 0.001159 | 0.001465 | 0.001132 | 157,569 | 41m 27s | 1.82 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_periodic_gru_sequence_bw` | `periodic_gru_sequence` | 0.001166 | 0.001481 | 0.001158 | 157,569 | 45m 02s | 1.82 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_periodic_gru_sequence_global` | `periodic_gru_sequence` | 0.001257 | 0.001613 | 0.001252 | 157,569 | 1h 02m 53s | 1.82 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 7 | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | 0.001279 | 0.001638 | 0.001274 | 157,569 | 40m 03s | 1.82 MB | Very High | High | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |
| 8 | `te_periodic_gru_sequence_bw__polished_actual_values` | `periodic_gru_sequence` | 0.001343 | 0.001978 | 0.001279 | 157,953 | 42m 38s | 1.82 MB | Very High | High | `dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values` |
| 9 | `te_periodic_gru_sequence_global__polished_actual_values` | `periodic_gru_sequence` | 0.001390 | 0.002058 | 0.001322 | 157,953 | 43m 44s | 1.82 MB | Very High | High | `dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values` |
| 10 | `te_periodic_gru_sequence_fw__polished_actual_values` | `periodic_gru_sequence` | 0.001561 | 0.002360 | 0.001501 | 157,953 | 40m 09s | 1.82 MB | Very High | High | `dataset_input_mode_retraining__periodic_gru_sequence__polished_actual_values` |
| 11 | `te_periodic_gru_sequence_fw__polished_setpoints` | `periodic_gru_sequence` | 0.002108 | 0.003430 | 0.001832 | 157,953 | 20m 46s | 1.82 MB | Very High | Medium | `dataset_input_mode_retraining__periodic_gru_sequence__polished_setpoints` |
| 12 | `te_periodic_gru_sequence_global__polished_setpoints` | `periodic_gru_sequence` | 0.002143 | 0.003467 | 0.001867 | 157,953 | 13m 48s | 1.82 MB | Very High | Low | `dataset_input_mode_retraining__periodic_gru_sequence__polished_setpoints` |
| 13 | `te_periodic_gru_sequence_bw__polished_setpoints` | `periodic_gru_sequence` | 0.002168 | 0.003506 | 0.001898 | 157,953 | 11m 27s | 1.82 MB | Very High | Low | `dataset_input_mode_retraining__periodic_gru_sequence__polished_setpoints` |
| 14 | `te_periodic_gru_sequence_remote_global` | `periodic_gru_sequence` | 0.002681 | 0.002971 | 0.002507 | 157,953 | 1h 00m 14s | 1.82 MB | Very High | High | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |
| 15 | `te_periodic_gru_sequence_bw__simplified_setpoints` | `periodic_gru_sequence` | 0.003250 | 0.003969 | 0.003500 | 157,953 | 9m 58s | 1.82 MB | Very High | Low | `dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints` |
| 16 | `te_periodic_gru_sequence_global__simplified_setpoints` | `periodic_gru_sequence` | 0.003332 | 0.004068 | 0.003477 | 157,953 | 9m 35s | 1.82 MB | Very High | Low | `dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints` |
| 17 | `te_periodic_gru_sequence_fw__simplified_setpoints` | `periodic_gru_sequence` | 0.003368 | 0.004076 | 0.003532 | 157,953 | 9m 05s | 1.82 MB | Very High | Low | `dataset_input_mode_retraining__periodic_gru_sequence__simplified_setpoints` |

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
- Best test MAE: `0.001226`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_lstm_sequence_remote_Bw` | `periodic_lstm_sequence` | 0.002556 | 0.002953 | 0.002432 | 210,561 | 35m 21s | 2.43 MB | Very High | Medium | `wave2b_harmonic_temporal_hybrid_campaign_2026_05_25` |

#### periodic_mlp

- Best run: `te_periodic_mlp_h04_standard_global_optuna_t0010`
- Best test MAE: `0.003186`
- Completed tracked runs: `21`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_periodic_mlp_bw` | `periodic_mlp` | 0.001740 | 0.002328 | 0.001658 | 27,137 | 20m 08s | 0.33 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_periodic_mlp_global` | `periodic_mlp` | 0.001741 | 0.002333 | 0.001655 | 27,137 | 19m 36s | 0.33 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_periodic_mlp_fw` | `periodic_mlp` | 0.001742 | 0.002329 | 0.001597 | 27,137 | 43m 55s | 0.33 MB | Medium | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_periodic_mlp_fw` | `periodic_mlp` | 0.001747 | 0.002347 | 0.001670 | 27,137 | 15m 31s | 0.33 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_periodic_mlp_bw` | `periodic_mlp` | 0.001758 | 0.002334 | 0.001611 | 27,137 | 40m 10s | 0.33 MB | Medium | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_periodic_mlp_fw__polished_setpoints` | `periodic_mlp` | 0.001770 | 0.002770 | 0.001624 | 27,265 | 19m 06s | 0.33 MB | Medium | Medium | `dataset_input_mode_retraining__periodic_mlp__polished_setpoints` |
| 7 | `te_periodic_mlp_global` | `periodic_mlp` | 0.001774 | 0.002355 | 0.001634 | 27,137 | 29m 56s | 0.33 MB | Medium | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 8 | `te_periodic_mlp_global__polished_setpoints` | `periodic_mlp` | 0.001794 | 0.002792 | 0.001654 | 27,265 | 14m 06s | 0.33 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp__polished_setpoints` |
| 9 | `te_periodic_mlp_global__polished_actual_values` | `periodic_mlp` | 0.001813 | 0.002796 | 0.001654 | 27,265 | 20m 28s | 0.33 MB | Medium | Medium | `dataset_input_mode_retraining__periodic_mlp__polished_actual_values` |
| 10 | `te_periodic_mlp_bw__polished_setpoints` | `periodic_mlp` | 0.001853 | 0.002843 | 0.001655 | 27,265 | 14m 06s | 0.33 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp__polished_setpoints` |
| 11 | `te_periodic_mlp_bw__polished_actual_values` | `periodic_mlp` | 0.001869 | 0.002856 | 0.001676 | 27,265 | 18m 27s | 0.33 MB | Medium | Medium | `dataset_input_mode_retraining__periodic_mlp__polished_actual_values` |
| 12 | `te_periodic_mlp_fw__polished_actual_values` | `periodic_mlp` | 0.001877 | 0.002885 | 0.001689 | 27,265 | 14m 00s | 0.33 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp__polished_actual_values` |
| 13 | `te_periodic_mlp_h04_standard_global_optuna_t0010` | `periodic_mlp` | 0.003186 | 0.003690 | 0.002994 | 27,265 | N/A | 0.33 MB | Medium | Unknown | `standalone_or_unknown` |
| 14 | `te_periodic_mlp_h04_standard_global_optuna_t0008` | `periodic_mlp` | 0.003200 | 0.003798 | 0.003057 | 46,721 | N/A | 0.56 MB | Medium | Unknown | `standalone_or_unknown` |
| 15 | `te_periodic_mlp_h04_standard_global_optuna_t0006` | `periodic_mlp` | 0.003233 | 0.003733 | 0.002964 | 27,777 | N/A | 0.34 MB | Medium | Unknown | `standalone_or_unknown` |
| 16 | `te_periodic_mlp_rcim_sparse_tracking_global` | `periodic_mlp` | 0.003275 | 0.003726 | 0.002863 | 28,545 | 7h 47m 34s | 0.35 MB | Medium | Very High | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 17 | `te_periodic_mlp_global__simplified_setpoints` | `periodic_mlp` | 0.003346 | 0.004047 | 0.003013 | 27,265 | 11m 13s | 0.33 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp__simplified_setpoints` |
| 18 | `te_periodic_mlp_dense240_tracking_global` | `periodic_mlp` | 0.003348 | 0.003862 | 0.002962 | 87,681 | 20m 22s | 1.03 MB | High | Medium | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 19 | `te_periodic_mlp_dense360_tracking_global` | `periodic_mlp` | 0.003401 | 0.003831 | 0.002859 | 118,401 | 50m 45s | 1.38 MB | High | High | `wave1_periodic_mlp_explicit_harmonic_tracking_campaign_2026_05_20_22_42_49` |
| 20 | `te_periodic_mlp_fw__simplified_setpoints` | `periodic_mlp` | 0.003419 | 0.004131 | 0.003021 | 27,265 | 6m 39s | 0.33 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp__simplified_setpoints` |
| 21 | `te_periodic_mlp_bw__simplified_setpoints` | `periodic_mlp` | 0.003446 | 0.004162 | 0.003016 | 27,265 | 8m 51s | 0.33 MB | Medium | Low | `dataset_input_mode_retraining__periodic_mlp__simplified_setpoints` |

#### periodic_mlp_bw

- Best run: `te_periodic_mlp_bw`
- Best test MAE: `0.001740`
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

- Best run: `te_periodic_temporal_convolution_bw__polished_actual_values`
- Best test MAE: `0.002001`
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

#### residual_harmonic_gru_sequence_dense240

- Best run: `te_residual_harmonic_gru_sequence_remote_global_dense240`
- Best test MAE: `0.003511`
- Completed tracked runs: `13`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_dense240_bw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002049 | 0.003081 | 0.001942 | 151,522 | 32m 31s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_actual_values` |
| 2 | `te_residual_harmonic_gru_sequence_dense240_global` | `residual_harmonic_gru_sequence` | 0.002076 | 0.002660 | 0.001967 | 151,138 | 47m 26s | 1.75 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_residual_harmonic_gru_sequence_dense240_bw` | `residual_harmonic_gru_sequence` | 0.002101 | 0.002698 | 0.001984 | 151,138 | 43m 06s | 1.75 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_residual_harmonic_gru_sequence_dense240_fw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002101 | 0.003138 | 0.001969 | 151,522 | 21m 40s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_actual_values` |
| 5 | `te_residual_harmonic_gru_sequence_dense240_fw` | `residual_harmonic_gru_sequence` | 0.002143 | 0.002729 | 0.002025 | 151,138 | 25m 47s | 1.75 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_residual_harmonic_gru_sequence_dense240_global__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002213 | 0.003268 | 0.002046 | 151,522 | 11m 00s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_actual_values` |
| 7 | `te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints` | `residual_harmonic_gru_sequence` | 0.002256 | 0.003614 | 0.001988 | 151,522 | 19m 53s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints` |
| 8 | `te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints` | `residual_harmonic_gru_sequence` | 0.002262 | 0.003634 | 0.001961 | 151,522 | 17m 37s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints` |
| 9 | `te_residual_harmonic_gru_sequence_dense240_global__polished_setpoints` | `residual_harmonic_gru_sequence` | 0.002278 | 0.003633 | 0.001986 | 151,522 | 20m 12s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__polished_setpoints` |
| 10 | `te_residual_harmonic_gru_sequence_dense240_fw__simplified_setpoints` | `residual_harmonic_gru_sequence` | 0.003365 | 0.004129 | 0.003587 | 151,522 | 10m 32s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__simplified_setpoints` |
| 11 | `te_residual_harmonic_gru_sequence_dense240_global__simplified_setpoints` | `residual_harmonic_gru_sequence` | 0.003375 | 0.004181 | 0.003617 | 151,522 | 10m 54s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__simplified_setpoints` |
| 12 | `te_residual_harmonic_gru_sequence_dense240_bw__simplified_setpoints` | `residual_harmonic_gru_sequence` | 0.003429 | 0.004166 | 0.003595 | 151,522 | 10m 01s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense240__simplified_setpoints` |
| 13 | `te_residual_harmonic_gru_sequence_remote_global_dense240` | `residual_harmonic_gru_sequence` | 0.003511 | 0.003983 | 0.003600 | 151,522 | 13m 21s | 1.75 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_gru_sequence_dense360

- Best run: `te_residual_harmonic_gru_sequence_remote_global_dense360`
- Best test MAE: `0.003535`
- Completed tracked runs: `13`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002071 | 0.003106 | 0.001960 | 151,762 | 29m 02s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values` |
| 2 | `te_residual_harmonic_gru_sequence_dense360_fw__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002074 | 0.003114 | 0.001955 | 151,762 | 30m 31s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values` |
| 3 | `te_residual_harmonic_gru_sequence_dense360_fw` | `residual_harmonic_gru_sequence` | 0.002083 | 0.002673 | 0.001968 | 151,378 | 54m 52s | 1.75 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_residual_harmonic_gru_sequence_dense360_global__polished_actual_values` | `residual_harmonic_gru_sequence` | 0.002088 | 0.003113 | 0.001960 | 151,762 | 26m 15s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_actual_values` |
| 5 | `te_residual_harmonic_gru_sequence_dense360_bw` | `residual_harmonic_gru_sequence` | 0.002103 | 0.002701 | 0.001979 | 151,378 | 50m 34s | 1.75 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_residual_harmonic_gru_sequence_dense360_global` | `residual_harmonic_gru_sequence` | 0.002149 | 0.002741 | 0.002020 | 151,378 | 30m 11s | 1.75 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 7 | `te_residual_harmonic_gru_sequence_dense360_fw__polished_setpoints` | `residual_harmonic_gru_sequence` | 0.002283 | 0.003646 | 0.002002 | 151,762 | 25m 17s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints` |
| 8 | `te_residual_harmonic_gru_sequence_dense360_global__polished_setpoints` | `residual_harmonic_gru_sequence` | 0.002284 | 0.003660 | 0.001974 | 151,762 | 27m 26s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints` |
| 9 | `te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints` | `residual_harmonic_gru_sequence` | 0.002292 | 0.003649 | 0.002000 | 151,762 | 18m 35s | 1.75 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__polished_setpoints` |
| 10 | `te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints` | `residual_harmonic_gru_sequence` | 0.003395 | 0.004190 | 0.003588 | 151,762 | 11m 25s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints` |
| 11 | `te_residual_harmonic_gru_sequence_dense360_global__simplified_setpoints` | `residual_harmonic_gru_sequence` | 0.003404 | 0.004244 | 0.003607 | 151,762 | 10m 28s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints` |
| 12 | `te_residual_harmonic_gru_sequence_dense360_fw__simplified_setpoints` | `residual_harmonic_gru_sequence` | 0.003407 | 0.004178 | 0.003582 | 151,762 | 11m 42s | 1.75 MB | Very High | Low | `dataset_input_mode_retraining__residual_harmonic_gru_sequence_dense360__simplified_setpoints` |
| 13 | `te_residual_harmonic_gru_sequence_remote_global_dense360` | `residual_harmonic_gru_sequence` | 0.003535 | 0.003999 | 0.003628 | 151,762 | 21m 39s | 1.75 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

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

#### residual_harmonic_lstm_sequence_dense240

- Best run: `te_residual_harmonic_lstm_sequence_remote_global_dense240`
- Best test MAE: `0.003473`
- Completed tracked runs: `13`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_dense240_bw__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.002116 | 0.003149 | 0.001985 | 201,826 | 32m 41s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__polished_actual_values` |
| 2 | `te_residual_harmonic_lstm_sequence_dense240_fw` | `residual_harmonic_lstm_sequence` | 0.002147 | 0.002745 | 0.002044 | 201,314 | 21m 58s | 2.32 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_residual_harmonic_lstm_sequence_dense240_global` | `residual_harmonic_lstm_sequence` | 0.002161 | 0.002748 | 0.002031 | 201,314 | 30m 03s | 2.32 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_residual_harmonic_lstm_sequence_dense240_bw` | `residual_harmonic_lstm_sequence` | 0.002164 | 0.002757 | 0.002040 | 201,314 | 25m 51s | 2.32 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_residual_harmonic_lstm_sequence_dense240_fw__polished_setpoints` | `residual_harmonic_lstm_sequence` | 0.002275 | 0.003636 | 0.001995 | 201,826 | 25m 40s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__polished_setpoints` |
| 6 | `te_residual_harmonic_lstm_sequence_dense240_global__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.002297 | 0.003625 | 0.002027 | 201,826 | 23m 21s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__polished_actual_values` |
| 7 | `te_residual_harmonic_lstm_sequence_dense240_global__polished_setpoints` | `residual_harmonic_lstm_sequence` | 0.002297 | 0.003647 | 0.002004 | 201,826 | 20m 56s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__polished_setpoints` |
| 8 | `te_residual_harmonic_lstm_sequence_dense240_fw__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.002298 | 0.003638 | 0.002025 | 201,826 | 23m 15s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__polished_actual_values` |
| 9 | `te_residual_harmonic_lstm_sequence_dense240_bw__polished_setpoints` | `residual_harmonic_lstm_sequence` | 0.002316 | 0.003665 | 0.002005 | 201,826 | 26m 59s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__polished_setpoints` |
| 10 | `te_residual_harmonic_lstm_sequence_dense240_fw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | 0.003354 | 0.004116 | 0.003561 | 201,826 | 21m 52s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints` |
| 11 | `te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | 0.003367 | 0.004145 | 0.003586 | 201,826 | 27m 02s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints` |
| 12 | `te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints` | `residual_harmonic_lstm_sequence` | 0.003381 | 0.004182 | 0.003604 | 201,826 | 17m 53s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense240__simplified_setpoints` |
| 13 | `te_residual_harmonic_lstm_sequence_remote_global_dense240` | `residual_harmonic_lstm_sequence` | 0.003473 | 0.003925 | 0.003624 | 201,826 | 13m 54s | 2.33 MB | Very High | Low | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |

#### residual_harmonic_lstm_sequence_dense360

- Best run: `te_residual_harmonic_lstm_sequence_remote_global_dense360`
- Best test MAE: `0.003477`
- Completed tracked runs: `13`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_residual_harmonic_lstm_sequence_dense360_bw` | `residual_harmonic_lstm_sequence` | 0.002097 | 0.002693 | 0.002007 | 201,554 | 46m 45s | 2.32 MB | Very High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.002156 | 0.003201 | 0.001999 | 202,066 | 31m 48s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values` |
| 3 | `te_residual_harmonic_lstm_sequence_dense360_fw` | `residual_harmonic_lstm_sequence` | 0.002219 | 0.002819 | 0.002066 | 201,554 | 28m 00s | 2.32 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_residual_harmonic_lstm_sequence_dense360_global` | `residual_harmonic_lstm_sequence` | 0.002223 | 0.002815 | 0.002071 | 201,554 | 27m 27s | 2.32 MB | Very High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_residual_harmonic_lstm_sequence_dense360_global__polished_setpoints` | `residual_harmonic_lstm_sequence` | 0.002282 | 0.003645 | 0.001977 | 202,066 | 33m 55s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints` |
| 6 | `te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints` | `residual_harmonic_lstm_sequence` | 0.002282 | 0.003627 | 0.001991 | 202,066 | 33m 59s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints` |
| 7 | `te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.002295 | 0.003624 | 0.002032 | 202,066 | 25m 12s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values` |
| 8 | `te_residual_harmonic_lstm_sequence_dense360_fw__polished_setpoints` | `residual_harmonic_lstm_sequence` | 0.002303 | 0.003648 | 0.002013 | 202,066 | 23m 24s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_setpoints` |
| 9 | `te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values` | `residual_harmonic_lstm_sequence` | 0.002330 | 0.003667 | 0.002092 | 202,066 | 15m 32s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__polished_actual_values` |
| 10 | `te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | 0.003402 | 0.004177 | 0.003582 | 202,066 | 19m 05s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints` |
| 11 | `te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints` | `residual_harmonic_lstm_sequence` | 0.003443 | 0.004246 | 0.003600 | 202,066 | 21m 09s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints` |
| 12 | `te_residual_harmonic_lstm_sequence_remote_global_dense360` | `residual_harmonic_lstm_sequence` | 0.003477 | 0.003940 | 0.003648 | 202,066 | 28m 49s | 2.33 MB | Very High | Medium | `wave2c_residual_harmonic_temporal_hybrid_campaign_2026_05_27` |
| 13 | `te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints` | `residual_harmonic_lstm_sequence` | 0.003480 | 0.004221 | 0.003604 | 202,066 | 15m 25s | 2.33 MB | Very High | Medium | `dataset_input_mode_retraining__residual_harmonic_lstm_sequence_dense360__simplified_setpoints` |

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
- Completed tracked runs: `16`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_temporal_convolution_bw__polished_actual_values` | `temporal_convolution` | 0.002303 | 0.003366 | 0.002198 | 147,009 | 27m 04s | 1.70 MB | High | Medium | `dataset_input_mode_retraining__temporal_convolution__polished_actual_values` |
| 2 | `te_temporal_convolution_global__polished_actual_values` | `temporal_convolution` | 0.002327 | 0.003391 | 0.002191 | 147,009 | 24m 33s | 1.70 MB | High | Medium | `dataset_input_mode_retraining__temporal_convolution__polished_actual_values` |
| 3 | `te_temporal_convolution_bw` | `temporal_convolution` | 0.002348 | 0.002988 | 0.002236 | 146,369 | 25m 15s | 1.69 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_temporal_convolution_global` | `temporal_convolution` | 0.002385 | 0.003048 | 0.002296 | 146,369 | 22m 15s | 1.69 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_temporal_convolution_fw__polished_actual_values` | `temporal_convolution` | 0.002390 | 0.003496 | 0.002272 | 147,009 | 14m 07s | 1.70 MB | High | Low | `dataset_input_mode_retraining__temporal_convolution__polished_actual_values` |
| 6 | `te_temporal_convolution_bw` | `temporal_convolution` | 0.002391 | 0.003044 | 0.002303 | 146,369 | 33m 57s | 1.69 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 7 | `te_temporal_convolution_fw` | `temporal_convolution` | 0.002399 | 0.003061 | 0.002311 | 146,369 | 33m 25s | 1.69 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 8 | `te_temporal_convolution_global` | `temporal_convolution` | 0.002411 | 0.003063 | 0.002308 | 146,369 | 29m 33s | 1.69 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 9 | `te_temporal_convolution_fw` | `temporal_convolution` | 0.002470 | 0.003146 | 0.002339 | 146,369 | 15m 07s | 1.69 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 10 | `te_temporal_convolution_bw__polished_setpoints` | `temporal_convolution` | 0.002508 | 0.003884 | 0.002222 | 147,009 | 25m 06s | 1.70 MB | High | Medium | `dataset_input_mode_retraining__temporal_convolution__polished_setpoints` |
| 11 | `te_temporal_convolution_global__polished_setpoints` | `temporal_convolution` | 0.002538 | 0.003933 | 0.002250 | 147,009 | 13m 19s | 1.70 MB | High | Low | `dataset_input_mode_retraining__temporal_convolution__polished_setpoints` |
| 12 | `te_temporal_convolution_fw__polished_setpoints` | `temporal_convolution` | 0.002544 | 0.003914 | 0.002253 | 147,009 | 12m 51s | 1.70 MB | High | Low | `dataset_input_mode_retraining__temporal_convolution__polished_setpoints` |
| 13 | `te_temporal_convolution_fw__simplified_setpoints` | `temporal_convolution` | 0.003530 | 0.004341 | 0.003779 | 147,009 | 6m 34s | 1.70 MB | High | Low | `dataset_input_mode_retraining__temporal_convolution__simplified_setpoints` |
| 14 | `te_temporal_convolution_bw__simplified_setpoints` | `temporal_convolution` | 0.003547 | 0.004393 | 0.003813 | 147,009 | 8m 39s | 1.70 MB | High | Low | `dataset_input_mode_retraining__temporal_convolution__simplified_setpoints` |
| 15 | `te_temporal_convolution_global__simplified_setpoints` | `temporal_convolution` | 0.003624 | 0.004478 | 0.003805 | 147,009 | 5m 29s | 1.70 MB | High | Low | `dataset_input_mode_retraining__temporal_convolution__simplified_setpoints` |
| 16 | `te_temporal_convolution_sequence_remote_global` | `temporal_convolution` | 0.003754 | 0.004266 | 0.003935 | 147,009 | 9m 46s | 1.70 MB | High | Low | `wave2_temporal_model_entry_campaign_2026_05_24_11_01_15` |

#### temporal_convolution_bw

- Best run: `te_temporal_convolution_bw__polished_actual_values`
- Best test MAE: `0.002303`
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

- Best run: `te_tree_bw__polished_setpoints`
- Best test MAE: `0.001699`
- Completed tracked runs: `3`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf10` | `hist_gradient_boosting` | 0.002954 | 0.003749 | 0.002681 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 2 | `te_hist_gbr_tabular_Bw_grid_depth6_lr008_leaf20` | `hist_gradient_boosting` | 0.002954 | 0.003749 | 0.002681 | 5 | N/A | 0.45 MB | Very Low | Unknown | `standalone_or_unknown` |
| 3 | `te_hist_gbr_tabular_Bw_grid_depth8_lr008_leaf10` | `hist_gradient_boosting` | 0.003002 | 0.003809 | 0.002650 | 5 | N/A | 0.44 MB | Very Low | Unknown | `standalone_or_unknown` |

#### wave3_1_sequential_residual_offset_probe

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_1_sequential_residual_offset_probe_bw` | `sequential_residual_offset_probe` | 0.002225 | 0.002871 | 0.002147 | 92,418 | 29m 05s | 1.09 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave3_1_sequential_residual_offset_probe_fw` | `sequential_residual_offset_probe` | 0.002246 | 0.002893 | 0.002154 | 92,418 | 24m 13s | 1.09 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave3_1_sequential_residual_offset_probe_global` | `sequential_residual_offset_probe` | 0.002261 | 0.002896 | 0.002147 | 92,418 | 23m 01s | 1.09 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave3_1_sequential_residual_offset_probe_bw__polished_actual_values` | `sequential_residual_offset_probe` | 0.002262 | 0.003326 | 0.002154 | 92,802 | 42m 44s | 1.09 MB | High | High | `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values` |
| 5 | `te_wave3_1_sequential_residual_offset_probe_fw__polished_actual_values` | `sequential_residual_offset_probe` | 0.002349 | 0.003433 | 0.002190 | 92,802 | 25m 45s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values` |
| 6 | `te_wave3_1_sequential_residual_offset_probe_global__polished_actual_values` | `sequential_residual_offset_probe` | 0.002379 | 0.003463 | 0.002209 | 92,802 | 20m 52s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_actual_values` |
| 7 | `te_wave3_1_sequential_residual_offset_probe_bw__polished_setpoints` | `sequential_residual_offset_probe` | 0.002450 | 0.003838 | 0.002169 | 92,802 | 25m 12s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_setpoints` |
| 8 | `te_wave3_1_sequential_residual_offset_probe_fw__polished_setpoints` | `sequential_residual_offset_probe` | 0.002465 | 0.003849 | 0.002175 | 92,802 | 25m 53s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_setpoints` |
| 9 | `te_wave3_1_sequential_residual_offset_probe_global__polished_setpoints` | `sequential_residual_offset_probe` | 0.002475 | 0.003835 | 0.002184 | 92,802 | 27m 17s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__polished_setpoints` |
| 10 | `te_wave3_1_sequential_residual_offset_probe_fw__simplified_setpoints` | `sequential_residual_offset_probe` | 0.003472 | 0.004298 | 0.003655 | 92,802 | 21m 27s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints` |
| 11 | `te_wave3_1_sequential_residual_offset_probe_global__simplified_setpoints` | `sequential_residual_offset_probe` | 0.003534 | 0.004399 | 0.003727 | 92,802 | 13m 12s | 1.09 MB | High | Low | `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints` |
| 12 | `te_wave3_1_sequential_residual_offset_probe_bw__simplified_setpoints` | `sequential_residual_offset_probe` | 0.003601 | 0.004440 | 0.003728 | 92,802 | 12m 34s | 1.09 MB | High | Low | `dataset_input_mode_retraining__wave3_1_sequential_residual_offset_probe__simplified_setpoints` |

#### wave3_2_clean_sequential_residual_offset

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_2_clean_sequential_residual_offset_bw` | `sequential_residual_offset_probe` | 0.002242 | 0.002885 | 0.002150 | 92,418 | 30m 17s | 1.09 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave3_2_clean_sequential_residual_offset_fw` | `sequential_residual_offset_probe` | 0.002258 | 0.002897 | 0.002159 | 92,418 | 26m 01s | 1.09 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave3_2_clean_sequential_residual_offset_global` | `sequential_residual_offset_probe` | 0.002276 | 0.002910 | 0.002158 | 92,418 | 28m 06s | 1.09 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values` | `sequential_residual_offset_probe` | 0.002288 | 0.003346 | 0.002169 | 92,802 | 30m 55s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values` |
| 5 | `te_wave3_2_clean_sequential_residual_offset_global__polished_actual_values` | `sequential_residual_offset_probe` | 0.002302 | 0.003369 | 0.002164 | 92,802 | 31m 42s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values` |
| 6 | `te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values` | `sequential_residual_offset_probe` | 0.002312 | 0.003384 | 0.002195 | 92,802 | 24m 39s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_actual_values` |
| 7 | `te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints` | `sequential_residual_offset_probe` | 0.002454 | 0.003851 | 0.002174 | 92,802 | 25m 58s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints` |
| 8 | `te_wave3_2_clean_sequential_residual_offset_fw__polished_setpoints` | `sequential_residual_offset_probe` | 0.002484 | 0.003853 | 0.002198 | 92,802 | 22m 26s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints` |
| 9 | `te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints` | `sequential_residual_offset_probe` | 0.002499 | 0.003890 | 0.002182 | 92,802 | 22m 06s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__polished_setpoints` |
| 10 | `te_wave3_2_clean_sequential_residual_offset_bw__simplified_setpoints` | `sequential_residual_offset_probe` | 0.003486 | 0.004293 | 0.003648 | 92,802 | 23m 19s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__simplified_setpoints` |
| 11 | `te_wave3_2_clean_sequential_residual_offset_fw__simplified_setpoints` | `sequential_residual_offset_probe` | 0.003580 | 0.004407 | 0.003716 | 92,802 | 14m 08s | 1.09 MB | High | Low | `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__simplified_setpoints` |
| 12 | `te_wave3_2_clean_sequential_residual_offset_global__simplified_setpoints` | `sequential_residual_offset_probe` | 0.003636 | 0.004490 | 0.003707 | 92,802 | 16m 07s | 1.09 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_clean_sequential_residual_offset__simplified_setpoints` |

#### wave3_2_harmonic_residual_offset

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_2_harmonic_residual_offset_bw` | `harmonic_residual_offset_probe` | 0.001894 | 0.002440 | 0.001791 | 85,440 | 37m 24s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave3_2_harmonic_residual_offset_global` | `harmonic_residual_offset_probe` | 0.001914 | 0.002470 | 0.001783 | 85,440 | 31m 20s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave3_2_harmonic_residual_offset_fw` | `harmonic_residual_offset_probe` | 0.001948 | 0.002507 | 0.001809 | 85,440 | 21m 25s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave3_2_harmonic_residual_offset_global__polished_actual_values` | `harmonic_residual_offset_probe` | 0.001958 | 0.003010 | 0.001836 | 85,747 | 38m 50s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values` |
| 5 | `te_wave3_2_harmonic_residual_offset_fw__polished_actual_values` | `harmonic_residual_offset_probe` | 0.001961 | 0.003003 | 0.001850 | 85,747 | 43m 48s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values` |
| 6 | `te_wave3_2_harmonic_residual_offset_bw__polished_actual_values` | `harmonic_residual_offset_probe` | 0.001969 | 0.003011 | 0.001853 | 85,747 | 43m 40s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_actual_values` |
| 7 | `te_wave3_2_harmonic_residual_offset_global__polished_setpoints` | `harmonic_residual_offset_probe` | 0.002220 | 0.003587 | 0.001905 | 85,747 | 28m 26s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints` |
| 8 | `te_wave3_2_harmonic_residual_offset_fw__polished_setpoints` | `harmonic_residual_offset_probe` | 0.002222 | 0.003593 | 0.001886 | 85,747 | 21m 43s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints` |
| 9 | `te_wave3_2_harmonic_residual_offset_bw__polished_setpoints` | `harmonic_residual_offset_probe` | 0.002256 | 0.003593 | 0.001933 | 85,747 | 27m 23s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__polished_setpoints` |
| 10 | `te_wave3_2_harmonic_residual_offset_fw__simplified_setpoints` | `harmonic_residual_offset_probe` | 0.003391 | 0.004142 | 0.003623 | 85,747 | 15m 10s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints` |
| 11 | `te_wave3_2_harmonic_residual_offset_bw__simplified_setpoints` | `harmonic_residual_offset_probe` | 0.003398 | 0.004083 | 0.003612 | 85,747 | 16m 11s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints` |
| 12 | `te_wave3_2_harmonic_residual_offset_global__simplified_setpoints` | `harmonic_residual_offset_probe` | 0.003405 | 0.004128 | 0.003624 | 85,747 | 18m 23s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_2_harmonic_residual_offset__simplified_setpoints` |

#### wave3_3_raw_centered_shape_curve_aware

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_3_raw_centered_shape_curve_aware_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001916 | 0.002460 | 0.001804 | 85,440 | 39m 41s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave3_3_raw_centered_shape_curve_aware_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001917 | 0.002466 | 0.001789 | 85,440 | 34m 22s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave3_3_raw_centered_shape_curve_aware_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001954 | 0.002494 | 0.001797 | 85,440 | 33m 54s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001966 | 0.003011 | 0.001828 | 85,747 | 56m 16s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values` |
| 5 | `te_wave3_3_raw_centered_shape_curve_aware_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001987 | 0.003023 | 0.001855 | 85,747 | 50m 41s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values` |
| 6 | `te_wave3_3_raw_centered_shape_curve_aware_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002074 | 0.003111 | 0.001935 | 85,747 | 30m 54s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_actual_values` |
| 7 | `te_wave3_3_raw_centered_shape_curve_aware_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002271 | 0.003605 | 0.001951 | 85,747 | 34m 33s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints` |
| 8 | `te_wave3_3_raw_centered_shape_curve_aware_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002276 | 0.003645 | 0.001941 | 85,747 | 24m 21s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints` |
| 9 | `te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002285 | 0.003628 | 0.001939 | 85,747 | 36m 15s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__polished_setpoints` |
| 10 | `te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003398 | 0.004115 | 0.003578 | 85,747 | 31m 35s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints` |
| 11 | `te_wave3_3_raw_centered_shape_curve_aware_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003429 | 0.004190 | 0.003567 | 85,747 | 29m 49s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints` |
| 12 | `te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003524 | 0.004312 | 0.003570 | 85,747 | 29m 11s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_centered_shape_curve_aware__simplified_setpoints` |

#### wave3_3_raw_offset_curve_aware

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave3_3_raw_offset_curve_aware_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001898 | 0.002445 | 0.001768 | 85,440 | 49m 46s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave3_3_raw_offset_curve_aware_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001953 | 0.002499 | 0.001833 | 85,440 | 28m 03s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave3_3_raw_offset_curve_aware_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001975 | 0.003015 | 0.001850 | 85,747 | 48m 56s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__polished_actual_values` |
| 4 | `te_wave3_3_raw_offset_curve_aware_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002001 | 0.003029 | 0.001870 | 85,747 | 43m 39s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__polished_actual_values` |
| 5 | `te_wave3_3_raw_offset_curve_aware_global` | `curve_aware_harmonic_residual_offset_probe` | 0.002014 | 0.002561 | 0.001863 | 85,440 | 25m 59s | 1.00 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 6 | `te_wave3_3_raw_offset_curve_aware_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002096 | 0.003143 | 0.001928 | 85,747 | 33m 09s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__polished_actual_values` |
| 7 | `te_wave3_3_raw_offset_curve_aware_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002203 | 0.003560 | 0.001895 | 85,747 | 36m 49s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__polished_setpoints` |
| 8 | `te_wave3_3_raw_offset_curve_aware_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002280 | 0.003638 | 0.002011 | 85,747 | 28m 22s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__polished_setpoints` |
| 9 | `te_wave3_3_raw_offset_curve_aware_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002285 | 0.003630 | 0.001950 | 85,747 | 35m 32s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__polished_setpoints` |
| 10 | `te_wave3_3_raw_offset_curve_aware_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003400 | 0.004187 | 0.003571 | 85,747 | 35m 17s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints` |
| 11 | `te_wave3_3_raw_offset_curve_aware_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003464 | 0.004225 | 0.003581 | 85,747 | 33m 23s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints` |
| 12 | `te_wave3_3_raw_offset_curve_aware_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003501 | 0.004263 | 0.003544 | 85,747 | 38m 05s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave3_3_raw_offset_curve_aware__simplified_setpoints` |

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

#### wave4_1_log_cosh_robust_loss

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `1`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave4_1_log_cosh_robust_loss_bw` | `curve_aware_harmonic_residual_offset_probe` | 0.001899 | 0.002442 | 0.001766 | 85,440 | 57m 26s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave4_1_log_cosh_robust_loss_global` | `curve_aware_harmonic_residual_offset_probe` | 0.001913 | 0.002459 | 0.001776 | 85,440 | 41m 02s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave4_1_log_cosh_robust_loss_fw` | `curve_aware_harmonic_residual_offset_probe` | 0.001921 | 0.002465 | 0.001807 | 85,440 | 40m 58s | 1.00 MB | High | High | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave4_1_log_cosh_robust_loss_fw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001955 | 0.002994 | 0.001827 | 85,747 | 49m 06s | 1.00 MB | High | High | `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values` |
| 5 | `te_wave4_1_log_cosh_robust_loss_bw__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.001995 | 0.003057 | 0.001871 | 85,747 | 33m 18s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values` |
| 6 | `te_wave4_1_log_cosh_robust_loss_global__polished_actual_values` | `curve_aware_harmonic_residual_offset_probe` | 0.002046 | 0.003090 | 0.001899 | 85,747 | 32m 48s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_actual_values` |
| 7 | `te_wave4_1_log_cosh_robust_loss_global__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002200 | 0.003572 | 0.001912 | 85,747 | 39m 50s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints` |
| 8 | `te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002289 | 0.003641 | 0.001960 | 85,747 | 28m 41s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints` |
| 9 | `te_wave4_1_log_cosh_robust_loss_bw__polished_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.002290 | 0.003645 | 0.001966 | 85,747 | 19m 26s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints` |
| 10 | `te_wave4_1_log_cosh_robust_loss_global__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003339 | 0.004048 | 0.003573 | 85,747 | 30m 09s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__simplified_setpoints` |
| 11 | `te_wave4_1_log_cosh_robust_loss_fw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003398 | 0.004187 | 0.003542 | 85,747 | 27m 11s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__simplified_setpoints` |
| 12 | `te_wave4_1_log_cosh_robust_loss_bw__simplified_setpoints` | `curve_aware_harmonic_residual_offset_probe` | 0.003402 | 0.004189 | 0.003527 | 85,747 | 26m 29s | 1.00 MB | High | Medium | `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__simplified_setpoints` |

Known failed campaign attempts for this family:

- `te_wave4_1_log_cosh_robust_loss_fw__polished_setpoints` | campaign `dataset_input_mode_retraining__wave4_1_log_cosh_robust_loss__polished_setpoints` | model type `curve_aware_harmonic_residual_offset_probe` | error `[Errno 28] No space left on device`

#### wave4_4_causal_tcn_latent_offset_residual

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave4_4_causal_tcn_latent_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.002309 | 0.002974 | 0.002204 | 97,155 | 30m 27s | 1.16 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave4_4_causal_tcn_latent_offset_residual_global` | `latent_state_hysteresis_probe` | 0.002315 | 0.002986 | 0.002217 | 97,155 | 26m 42s | 1.16 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave4_4_causal_tcn_latent_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.002316 | 0.002980 | 0.002224 | 97,155 | 28m 28s | 1.16 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values` | `latent_state_hysteresis_probe` | 0.002344 | 0.003435 | 0.002227 | 97,923 | 15m 16s | 1.17 MB | High | Medium | `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values` |
| 5 | `te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values` | `latent_state_hysteresis_probe` | 0.002372 | 0.003458 | 0.002254 | 97,923 | 14m 07s | 1.17 MB | High | Low | `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values` |
| 6 | `te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values` | `latent_state_hysteresis_probe` | 0.002420 | 0.003542 | 0.002304 | 97,923 | 12m 34s | 1.17 MB | High | Low | `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_actual_values` |
| 7 | `te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_setpoints` | `latent_state_hysteresis_probe` | 0.002513 | 0.003854 | 0.002215 | 97,923 | 23m 35s | 1.17 MB | High | Medium | `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_setpoints` |
| 8 | `te_wave4_4_causal_tcn_latent_offset_residual_global__polished_setpoints` | `latent_state_hysteresis_probe` | 0.002515 | 0.003880 | 0.002228 | 97,923 | 16m 33s | 1.17 MB | High | Medium | `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_setpoints` |
| 9 | `te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_setpoints` | `latent_state_hysteresis_probe` | 0.002527 | 0.003882 | 0.002240 | 97,923 | 18m 42s | 1.17 MB | High | Medium | `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__polished_setpoints` |
| 10 | `te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints` | `latent_state_hysteresis_probe` | 0.003343 | 0.004238 | 0.003498 | 97,923 | 24m 24s | 1.17 MB | High | Medium | `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints` |
| 11 | `te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints` | `latent_state_hysteresis_probe` | 0.003548 | 0.004384 | 0.003766 | 97,923 | 7m 10s | 1.17 MB | High | Low | `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints` |
| 12 | `te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints` | `latent_state_hysteresis_probe` | 0.003555 | 0.004415 | 0.003709 | 97,923 | 13m 13s | 1.17 MB | High | Low | `dataset_input_mode_retraining__wave4_4_causal_tcn_latent_offset_residual__simplified_setpoints` |

#### wave4_4_gru_latent_offset_residual

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `12`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave4_4_gru_latent_offset_residual_bw` | `latent_state_hysteresis_probe` | 0.002260 | 0.002915 | 0.002191 | 124,899 | 38m 01s | 1.48 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave4_4_gru_latent_offset_residual_global__polished_actual_values` | `latent_state_hysteresis_probe` | 0.002271 | 0.003341 | 0.002173 | 125,475 | 46m 05s | 1.48 MB | High | High | `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values` |
| 3 | `te_wave4_4_gru_latent_offset_residual_global` | `latent_state_hysteresis_probe` | 0.002287 | 0.002934 | 0.002195 | 124,899 | 36m 39s | 1.48 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave4_4_gru_latent_offset_residual_fw` | `latent_state_hysteresis_probe` | 0.002300 | 0.002953 | 0.002201 | 124,899 | 28m 49s | 1.48 MB | High | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 5 | `te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values` | `latent_state_hysteresis_probe` | 0.002328 | 0.003372 | 0.002228 | 125,475 | 29m 49s | 1.48 MB | High | Medium | `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values` |
| 6 | `te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values` | `latent_state_hysteresis_probe` | 0.002363 | 0.003419 | 0.002247 | 125,475 | 21m 49s | 1.48 MB | High | Medium | `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_actual_values` |
| 7 | `te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints` | `latent_state_hysteresis_probe` | 0.002488 | 0.003826 | 0.002218 | 125,475 | 31m 06s | 1.48 MB | High | Medium | `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints` |
| 8 | `te_wave4_4_gru_latent_offset_residual_global__polished_setpoints` | `latent_state_hysteresis_probe` | 0.002534 | 0.003918 | 0.002223 | 125,475 | 24m 09s | 1.48 MB | High | Medium | `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints` |
| 9 | `te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints` | `latent_state_hysteresis_probe` | 0.002568 | 0.003925 | 0.002265 | 125,475 | 14m 07s | 1.48 MB | High | Low | `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__polished_setpoints` |
| 10 | `te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints` | `latent_state_hysteresis_probe` | 0.003510 | 0.004334 | 0.003772 | 125,475 | 12m 27s | 1.48 MB | High | Low | `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints` |
| 11 | `te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints` | `latent_state_hysteresis_probe` | 0.003535 | 0.004351 | 0.003757 | 125,475 | 12m 06s | 1.48 MB | High | Low | `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints` |
| 12 | `te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints` | `latent_state_hysteresis_probe` | 0.003563 | 0.004400 | 0.003719 | 125,475 | 14m 49s | 1.48 MB | High | Low | `dataset_input_mode_retraining__wave4_4_gru_latent_offset_residual__simplified_setpoints` |

#### wave52b_offset_harmonic_guided_offset_centered_shape_bw

- Best run: `te_wave52b_offset_harmonic_guided_offset_centered_shape_bw`
- Best test MAE: `0.002012`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_offset_centered_shape_bw` | `wave52b_offset_harmonic_guided` | 0.002012 | 0.002626 | 0.002604 | 22,593 | 35m 50s | 0.30 MB | Medium | Medium | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

#### wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw

- Best run: `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw`
- Best test MAE: `0.001677`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_bw` | `wave52b_offset_harmonic_guided` | 0.001677 | 0.002151 | 0.002320 | 22,593 | 29m 54s | 0.30 MB | Medium | Medium | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

#### wave52b_offset_harmonic_guided_offset_head_bw

- Best run: `te_wave52b_offset_harmonic_guided_offset_head_bw`
- Best test MAE: `0.002008`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_offset_head_bw` | `wave52b_offset_harmonic_guided` | 0.002008 | 0.002632 | 0.002597 | 22,593 | 32m 03s | 0.30 MB | Medium | Medium | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

#### wave52b_offset_harmonic_guided_pointwise_control_bw

- Best run: `te_wave52b_offset_harmonic_guided_pointwise_control_bw`
- Best test MAE: `0.001979`
- Completed tracked runs: `1`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave52b_offset_harmonic_guided_pointwise_control_bw` | `wave52b_offset_harmonic_guided` | 0.001979 | 0.002587 | 0.002591 | 22,593 | 29m 15s | 0.30 MB | Medium | Medium | `wave52b_offset_harmonic_guided_campaign_2026_07_01` |

#### wave5_1_harmonic_prior_pointwise_control

- Best run: `N/A`
- Best test MAE: `N/A`
- Completed tracked runs: `6`
- Known failed campaign attempts: `0`

| Rank | Run | Model Type | Test MAE [deg] | Test RMSE [deg] | Val MAE [deg] | Params | Duration | Artifact Size | Model Complexity | Training Heaviness | Campaign |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | `te_wave5_1_harmonic_prior_pointwise_control_bw` | `wave3_harmonic_prior_residual` | 0.002105 | 0.002680 | 0.001893 | 7,168 | 35m 57s | 0.10 MB | Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 2 | `te_wave5_1_harmonic_prior_pointwise_control_global` | `wave3_harmonic_prior_residual` | 0.002159 | 0.002754 | 0.001894 | 7,168 | 30m 00s | 0.10 MB | Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 3 | `te_wave5_1_harmonic_prior_pointwise_control_fw` | `wave3_harmonic_prior_residual` | 0.002185 | 0.002776 | 0.001913 | 7,168 | 19m 31s | 0.10 MB | Low | Medium | `polished_dataset_full_wave_retraining_2026_06_22` |
| 4 | `te_wave5_1_harmonic_prior_pointwise_control_fw__simplified_setpoints` | `wave3_harmonic_prior_residual` | 0.003386 | 0.004122 | 0.003563 | 7,283 | 26m 19s | 0.11 MB | Low | Medium | `dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__simplified_setpoints` |
| 5 | `te_wave5_1_harmonic_prior_pointwise_control_global__simplified_setpoints` | `wave3_harmonic_prior_residual` | 0.003417 | 0.004130 | 0.003597 | 7,283 | 18m 55s | 0.11 MB | Low | Medium | `dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__simplified_setpoints` |
| 6 | `te_wave5_1_harmonic_prior_pointwise_control_bw__simplified_setpoints` | `wave3_harmonic_prior_residual` | 0.003434 | 0.004181 | 0.003644 | 7,283 | 12m 11s | 0.11 MB | Low | Low | `dataset_input_mode_retraining__wave5_1_harmonic_prior_pointwise_control__simplified_setpoints` |

## Source Of Truth

- Live backlog: `doc/running/te_model_live_backlog.md`
- Active campaign state: `doc/running/active_training_campaign.yaml`
- Program registry: `output/registries/program/current_best_solution.yaml`
- Family registries root: `output/registries/families`
- Training campaign root: `output/training_campaigns`
- Training run root: `output/training_runs`
- Paper reference report: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

This document is repository-generated. Regenerate it after new campaign results so the cross-family snapshot stays aligned with the canonical registries and campaign artifacts.
