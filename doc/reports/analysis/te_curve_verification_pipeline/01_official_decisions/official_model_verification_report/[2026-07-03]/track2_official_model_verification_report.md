# TE Curve Verification Pipeline Official Model Verification Report

## Executive Verdict

This automated official refresh report closes `polished-dataset RCIM and full model-development refresh`.

Decision:

- `polished-dataset RCIM and full model-development refresh` is accepted and
  closed as the official `2026-07-03` TE Curve Verification Pipeline refresh.
- The accepted polished model-development baseline is the
  `polished_periodic_gru_sequence` family: `polished_periodic_gru_sequence_Bw`
  is the strongest refreshed aggregate candidate and
  `polished_periodic_gru_sequence_global` is the strongest refreshed global
  candidate.
- The forward raw-error leader is
  `polished_rcim_model_bank_reproduction_ET19_Fw`. It is recorded as the
  polished RCIM reference-bank forward leader, while the full historical matrix
  forward leader remains `rcim_retuned_GBM19_Fw` and
  `polished_periodic_gru_sequence_Fw` remains the strongest polished
  model-development forward fallback.
- The accepted polished direction-parallel leaders are therefore:
  `polished_rcim_model_bank_reproduction_ET19_Fw` for forward reference-bank
  evidence, `polished_periodic_gru_sequence_Fw` for forward
  model-development evidence, `polished_periodic_gru_sequence_Bw` for
  backward, and `polished_periodic_gru_sequence_global` for global.
- The launcher-generated matrix, collage, overlay, and PDF exports were
  reviewed during Codex closure and the status documents were synchronized.

## Source Package

This official report consolidates these refreshed artifacts:

- metric matrix:
  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`;
- matrix summary:
  `output/validation_checks/track2_reference_comparison/2026-07-03-17-46-19__track2_full_directional_family_matrix_polished_dataset_te_curve_verification_refresh_2026_07_03_fix3/validation_summary.yaml`;
- per-condition metrics:
  `output/validation_checks/track2_reference_comparison/2026-07-03-17-46-19__track2_full_directional_family_matrix_polished_dataset_te_curve_verification_refresh_2026_07_03_fix3/per_condition_metrics.csv`;
- best-model collage report:
  `doc/reports/analysis/track2/best_model_collage_report/[2026-07-03]/track2_best_model_collage_report.md`;
- multi-model curve comparison report:
  `doc/reports/analysis/track2/multi_model_curve_comparison_report/[2026-07-03]/track2_multi_model_curve_comparison_report.md`;
- operator launch logs:
  `output/validation_checks/track2_operator_launch_logs/2026-07-03-18-43-42_polished_dataset_te_curve_verification_refresh_2026_07_03_fix3`.

## Acceptance Checks

The accepted matrix is the `fix3` matrix generated on `2026-07-03`.

| Check | Result |
| --- | --- |
| Dataset root | `data\polished_dataset` |
| Refresh source contract | `data\polished_dataset` |
| Historical baseline source contract | `data/simplified_dataset` |
| Candidate count | `293` |
| Refreshed candidate count | `128` |
| Polished refreshed per-condition rows checked | `15,908` |
| Polished refreshed rows with a non-polished source path | `0` |

The remaining `data/simplified_dataset` reference in the matrix summary is the
explicit historical baseline contract for pre-polished candidates, not the
source used by the refreshed polished candidates.

## Candidate Refresh

The refresh added `128` candidates from `polished_model_development_registry`, `polished_rcim_model_bank_reproduction` into the official `293`-candidate matrix.

| Surface | Candidate | Family |
| --- | --- | --- |
| Fw | `polished_rcim_model_bank_reproduction_SVM19_Fw` | `SVM` |
| Fw | `polished_rcim_model_bank_reproduction_MLP19_Fw` | `MLP` |
| Fw | `polished_rcim_model_bank_reproduction_RF19_Fw` | `RF` |
| Fw | `polished_rcim_model_bank_reproduction_DT19_Fw` | `DT` |
| Fw | `polished_rcim_model_bank_reproduction_ET19_Fw` | `ET` |
| Fw | `polished_rcim_model_bank_reproduction_ERT19_Fw` | `ERT` |
| Fw | `polished_rcim_model_bank_reproduction_GBM19_Fw` | `GBM` |
| Fw | `polished_rcim_model_bank_reproduction_HGBM19_Fw` | `HGBM` |
| Fw | `polished_rcim_model_bank_reproduction_XGBM19_Fw` | `XGBM` |
| Fw | `polished_rcim_model_bank_reproduction_LGBM19_Fw` | `LGBM` |
| Bw | `polished_rcim_model_bank_reproduction_SVM19_Bw` | `SVM` |
| Bw | `polished_rcim_model_bank_reproduction_MLP19_Bw` | `MLP` |
| Bw | `polished_rcim_model_bank_reproduction_RF19_Bw` | `RF` |
| Bw | `polished_rcim_model_bank_reproduction_DT19_Bw` | `DT` |
| Bw | `polished_rcim_model_bank_reproduction_ET19_Bw` | `ET` |
| Bw | `polished_rcim_model_bank_reproduction_ERT19_Bw` | `ERT` |
| Bw | `polished_rcim_model_bank_reproduction_GBM19_Bw` | `GBM` |
| Bw | `polished_rcim_model_bank_reproduction_HGBM19_Bw` | `HGBM` |
| Bw | `polished_rcim_model_bank_reproduction_XGBM19_Bw` | `XGBM` |
| Bw | `polished_rcim_model_bank_reproduction_LGBM19_Bw` | `LGBM` |
| global | `polished_feedforward_global` | `feedforward` |
| Fw | `polished_feedforward_Fw` | `feedforward` |
| Bw | `polished_feedforward_Bw` | `feedforward` |
| global | `polished_harmonic_regression_global` | `harmonic_regression` |
| Fw | `polished_harmonic_regression_Fw` | `harmonic_regression` |
| Bw | `polished_harmonic_regression_Bw` | `harmonic_regression` |
| global | `polished_periodic_mlp_global` | `periodic_mlp` |
| Fw | `polished_periodic_mlp_Fw` | `periodic_mlp` |
| Bw | `polished_periodic_mlp_Bw` | `periodic_mlp` |
| global | `polished_residual_harmonic_mlp_global` | `residual_harmonic_mlp` |
| Fw | `polished_residual_harmonic_mlp_Fw` | `residual_harmonic_mlp` |
| Bw | `polished_residual_harmonic_mlp_Bw` | `residual_harmonic_mlp` |
| global | `polished_tree_global` | `tree` |
| Fw | `polished_tree_Fw` | `tree` |
| Bw | `polished_tree_Bw` | `tree` |
| global | `polished_periodic_mlp_harmonic_global` | `periodic_mlp_harmonic` |
| Fw | `polished_periodic_mlp_harmonic_Fw` | `periodic_mlp_harmonic` |
| Bw | `polished_periodic_mlp_harmonic_Bw` | `periodic_mlp_harmonic` |
| global | `polished_temporal_convolution_global` | `temporal_convolution` |
| Fw | `polished_temporal_convolution_Fw` | `temporal_convolution` |
| Bw | `polished_temporal_convolution_Bw` | `temporal_convolution` |
| global | `polished_gru_sequence_global` | `gru_sequence` |
| Fw | `polished_gru_sequence_Fw` | `gru_sequence` |
| Bw | `polished_gru_sequence_Bw` | `gru_sequence` |
| global | `polished_lstm_sequence_global` | `lstm_sequence` |
| Fw | `polished_lstm_sequence_Fw` | `lstm_sequence` |
| Bw | `polished_lstm_sequence_Bw` | `lstm_sequence` |
| global | `polished_periodic_temporal_convolution_global` | `periodic_temporal_convolution` |
| Fw | `polished_periodic_temporal_convolution_Fw` | `periodic_temporal_convolution` |
| Bw | `polished_periodic_temporal_convolution_Bw` | `periodic_temporal_convolution` |
| global | `polished_periodic_gru_sequence_global` | `periodic_gru_sequence` |
| Fw | `polished_periodic_gru_sequence_Fw` | `periodic_gru_sequence` |
| Bw | `polished_periodic_gru_sequence_Bw` | `periodic_gru_sequence` |
| global | `polished_periodic_lstm_sequence_global` | `periodic_lstm_sequence` |
| Fw | `polished_periodic_lstm_sequence_Fw` | `periodic_lstm_sequence` |
| Bw | `polished_periodic_lstm_sequence_Bw` | `periodic_lstm_sequence` |
| global | `polished_residual_harmonic_gru_sequence_sparse_rcim_global` | `residual_harmonic_gru_sequence_sparse_rcim` |
| Fw | `polished_residual_harmonic_gru_sequence_sparse_rcim_Fw` | `residual_harmonic_gru_sequence_sparse_rcim` |
| Bw | `polished_residual_harmonic_gru_sequence_sparse_rcim_Bw` | `residual_harmonic_gru_sequence_sparse_rcim` |
| global | `polished_residual_harmonic_gru_sequence_dense240_global` | `residual_harmonic_gru_sequence_dense240` |
| Fw | `polished_residual_harmonic_gru_sequence_dense240_Fw` | `residual_harmonic_gru_sequence_dense240` |
| Bw | `polished_residual_harmonic_gru_sequence_dense240_Bw` | `residual_harmonic_gru_sequence_dense240` |
| global | `polished_residual_harmonic_gru_sequence_dense360_global` | `residual_harmonic_gru_sequence_dense360` |
| Fw | `polished_residual_harmonic_gru_sequence_dense360_Fw` | `residual_harmonic_gru_sequence_dense360` |
| Bw | `polished_residual_harmonic_gru_sequence_dense360_Bw` | `residual_harmonic_gru_sequence_dense360` |
| global | `polished_residual_harmonic_lstm_sequence_sparse_rcim_global` | `residual_harmonic_lstm_sequence_sparse_rcim` |
| Fw | `polished_residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `residual_harmonic_lstm_sequence_sparse_rcim` |
| Bw | `polished_residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `residual_harmonic_lstm_sequence_sparse_rcim` |
| global | `polished_residual_harmonic_lstm_sequence_dense240_global` | `residual_harmonic_lstm_sequence_dense240` |
| Fw | `polished_residual_harmonic_lstm_sequence_dense240_Fw` | `residual_harmonic_lstm_sequence_dense240` |
| Bw | `polished_residual_harmonic_lstm_sequence_dense240_Bw` | `residual_harmonic_lstm_sequence_dense240` |
| global | `polished_residual_harmonic_lstm_sequence_dense360_global` | `residual_harmonic_lstm_sequence_dense360` |
| Fw | `polished_residual_harmonic_lstm_sequence_dense360_Fw` | `residual_harmonic_lstm_sequence_dense360` |
| Bw | `polished_residual_harmonic_lstm_sequence_dense360_Bw` | `residual_harmonic_lstm_sequence_dense360` |
| global | `polished_wave3_1_sequential_residual_offset_probe_global` | `wave3_1_sequential_residual_offset_probe` |
| Fw | `polished_wave3_1_sequential_residual_offset_probe_Fw` | `wave3_1_sequential_residual_offset_probe` |
| Bw | `polished_wave3_1_sequential_residual_offset_probe_Bw` | `wave3_1_sequential_residual_offset_probe` |
| global | `polished_wave3_2_clean_sequential_residual_offset_global` | `wave3_2_clean_sequential_residual_offset` |
| Fw | `polished_wave3_2_clean_sequential_residual_offset_Fw` | `wave3_2_clean_sequential_residual_offset` |
| Bw | `polished_wave3_2_clean_sequential_residual_offset_Bw` | `wave3_2_clean_sequential_residual_offset` |
| global | `polished_wave3_2_harmonic_residual_offset_global` | `wave3_2_harmonic_residual_offset` |
| Fw | `polished_wave3_2_harmonic_residual_offset_Fw` | `wave3_2_harmonic_residual_offset` |
| Bw | `polished_wave3_2_harmonic_residual_offset_Bw` | `wave3_2_harmonic_residual_offset` |
| global | `polished_wave3_3_curve_aware_pointwise_control_global` | `wave3_3_curve_aware_pointwise_control` |
| Fw | `polished_wave3_3_curve_aware_pointwise_control_Fw` | `wave3_3_curve_aware_pointwise_control` |
| Bw | `polished_wave3_3_curve_aware_pointwise_control_Bw` | `wave3_3_curve_aware_pointwise_control` |
| global | `polished_wave3_3_raw_centered_shape_curve_aware_global` | `wave3_3_raw_centered_shape_curve_aware` |
| Fw | `polished_wave3_3_raw_centered_shape_curve_aware_Fw` | `wave3_3_raw_centered_shape_curve_aware` |
| Bw | `polished_wave3_3_raw_centered_shape_curve_aware_Bw` | `wave3_3_raw_centered_shape_curve_aware` |
| global | `polished_wave3_3_raw_offset_curve_aware_global` | `wave3_3_raw_offset_curve_aware` |
| Fw | `polished_wave3_3_raw_offset_curve_aware_Fw` | `wave3_3_raw_offset_curve_aware` |
| Bw | `polished_wave3_3_raw_offset_curve_aware_Bw` | `wave3_3_raw_offset_curve_aware` |
| global | `polished_wave3_3_full_curve_composite_global` | `wave3_3_full_curve_composite` |
| Fw | `polished_wave3_3_full_curve_composite_Fw` | `wave3_3_full_curve_composite` |
| Bw | `polished_wave3_3_full_curve_composite_Bw` | `wave3_3_full_curve_composite` |
| global | `polished_wave4_1_mae_robust_loss_global` | `wave4_1_mae_robust_loss` |
| Fw | `polished_wave4_1_mae_robust_loss_Fw` | `wave4_1_mae_robust_loss` |
| Bw | `polished_wave4_1_mae_robust_loss_Bw` | `wave4_1_mae_robust_loss` |
| global | `polished_wave4_1_smooth_l1_robust_loss_global` | `wave4_1_smooth_l1_robust_loss` |
| Fw | `polished_wave4_1_smooth_l1_robust_loss_Fw` | `wave4_1_smooth_l1_robust_loss` |
| Bw | `polished_wave4_1_smooth_l1_robust_loss_Bw` | `wave4_1_smooth_l1_robust_loss` |
| global | `polished_wave4_1_log_cosh_robust_loss_global` | `wave4_1_log_cosh_robust_loss` |
| Fw | `polished_wave4_1_log_cosh_robust_loss_Fw` | `wave4_1_log_cosh_robust_loss` |
| Bw | `polished_wave4_1_log_cosh_robust_loss_Bw` | `wave4_1_log_cosh_robust_loss` |
| global | `polished_wave4_2_quantile_p10_p50_p90_global` | `wave4_2_quantile_p10_p50_p90` |
| Fw | `polished_wave4_2_quantile_p10_p50_p90_Fw` | `wave4_2_quantile_p10_p50_p90` |
| Bw | `polished_wave4_2_quantile_p10_p50_p90_Bw` | `wave4_2_quantile_p10_p50_p90` |
| global | `polished_wave4_2_gaussian_nll_global` | `wave4_2_gaussian_nll` |
| Fw | `polished_wave4_2_gaussian_nll_Fw` | `wave4_2_gaussian_nll` |
| Bw | `polished_wave4_2_gaussian_nll_Bw` | `wave4_2_gaussian_nll` |
| global | `polished_wave4_3_mixture_density_k2_global` | `wave4_3_mixture_density_k2` |
| Fw | `polished_wave4_3_mixture_density_k2_Fw` | `wave4_3_mixture_density_k2` |
| Bw | `polished_wave4_3_mixture_density_k2_Bw` | `wave4_3_mixture_density_k2` |
| global | `polished_wave4_3_mixture_density_k3_global` | `wave4_3_mixture_density_k3` |
| Fw | `polished_wave4_3_mixture_density_k3_Fw` | `wave4_3_mixture_density_k3` |
| Bw | `polished_wave4_3_mixture_density_k3_Bw` | `wave4_3_mixture_density_k3` |
| global | `polished_wave4_4_gru_latent_offset_residual_global` | `wave4_4_gru_latent_offset_residual` |
| Fw | `polished_wave4_4_gru_latent_offset_residual_Fw` | `wave4_4_gru_latent_offset_residual` |
| Bw | `polished_wave4_4_gru_latent_offset_residual_Bw` | `wave4_4_gru_latent_offset_residual` |
| global | `polished_wave4_4_causal_tcn_latent_offset_residual_global` | `wave4_4_causal_tcn_latent_offset_residual` |
| Fw | `polished_wave4_4_causal_tcn_latent_offset_residual_Fw` | `wave4_4_causal_tcn_latent_offset_residual` |
| Bw | `polished_wave4_4_causal_tcn_latent_offset_residual_Bw` | `wave4_4_causal_tcn_latent_offset_residual` |
| global | `polished_wave5_1_harmonic_prior_pointwise_control_global` | `wave5_1_harmonic_prior_pointwise_control` |
| Fw | `polished_wave5_1_harmonic_prior_pointwise_control_Fw` | `wave5_1_harmonic_prior_pointwise_control` |
| Bw | `polished_wave5_1_harmonic_prior_pointwise_control_Bw` | `wave5_1_harmonic_prior_pointwise_control` |
| global | `polished_wave5_1_harmonic_prior_smooth_l1_structured_global` | `wave5_1_harmonic_prior_smooth_l1_structured` |
| Fw | `polished_wave5_1_harmonic_prior_smooth_l1_structured_Fw` | `wave5_1_harmonic_prior_smooth_l1_structured` |
| Bw | `polished_wave5_1_harmonic_prior_smooth_l1_structured_Bw` | `wave5_1_harmonic_prior_smooth_l1_structured` |

## Refreshed Source Leaders

The table ranks the refreshed source by aggregate offline TE Curve Verification Pipeline metrics.

| Surface | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| Fw | `polished_rcim_model_bank_reproduction_ET19_Fw` | 0.001155 | 0.001394 | 2.401 | 4.928 |
| Bw | `polished_periodic_gru_sequence_Bw` | 0.001129 | 0.001412 | 2.228 | 4.688 |
| global | `polished_periodic_gru_sequence_global` | 0.001279 | 0.001568 | 2.636 | 5.690 |

## Refreshed Source Leaderboard

| Rank | Surface | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | Bw | `polished_periodic_gru_sequence_Bw` | 0.001129 | 0.001412 | 2.228 | 4.688 |
| 2 | Fw | `polished_rcim_model_bank_reproduction_ET19_Fw` | 0.001155 | 0.001394 | 2.401 | 4.928 |
| 3 | Fw | `polished_rcim_model_bank_reproduction_ERT19_Fw` | 0.001187 | 0.001438 | 2.457 | 5.438 |
| 4 | Fw | `polished_periodic_gru_sequence_Fw` | 0.001195 | 0.001461 | 2.559 | 5.193 |
| 5 | global | `polished_periodic_gru_sequence_global` | 0.001279 | 0.001568 | 2.636 | 5.690 |
| 6 | Bw | `polished_periodic_lstm_sequence_Bw` | 0.001290 | 0.001613 | 2.539 | 4.524 |
| 7 | global | `polished_periodic_lstm_sequence_global` | 0.001303 | 0.001600 | 2.642 | 5.314 |
| 8 | Fw | `polished_rcim_model_bank_reproduction_LGBM19_Fw` | 0.001368 | 0.001635 | 2.864 | 6.832 |
| 9 | Fw | `polished_wave4_3_mixture_density_k3_Fw` | 0.001528 | 0.001867 | 3.161 | 7.018 |
| 10 | Fw | `polished_wave4_3_mixture_density_k2_Fw` | 0.001545 | 0.001890 | 3.202 | 7.033 |
| 11 | global | `polished_wave4_3_mixture_density_k3_global` | 0.001585 | 0.001945 | 3.116 | 7.127 |
| 12 | Fw | `polished_rcim_model_bank_reproduction_GBM19_Fw` | 0.001644 | 0.001903 | 3.449 | 9.961 |
| 13 | Fw | `polished_wave3_3_curve_aware_pointwise_control_Fw` | 0.001701 | 0.002055 | 3.407 | 7.927 |
| 14 | Fw | `polished_wave4_2_gaussian_nll_Fw` | 0.001711 | 0.002056 | 3.424 | 8.122 |
| 15 | Fw | `polished_wave3_3_raw_centered_shape_curve_aware_Fw` | 0.001716 | 0.002078 | 3.450 | 8.345 |
| 16 | Fw | `polished_wave4_2_quantile_p10_p50_p90_Fw` | 0.001727 | 0.002081 | 3.466 | 7.927 |
| 17 | Fw | `polished_periodic_lstm_sequence_Fw` | 0.001730 | 0.002084 | 3.517 | 7.494 |
| 18 | Fw | `polished_wave3_3_raw_offset_curve_aware_Fw` | 0.001734 | 0.002099 | 3.495 | 8.291 |
| 19 | Fw | `polished_periodic_mlp_harmonic_Fw` | 0.001735 | 0.002062 | 3.511 | 7.554 |
| 20 | Fw | `polished_wave3_2_harmonic_residual_offset_Fw` | 0.001756 | 0.002127 | 3.526 | 8.417 |
| 21 | global | `polished_wave4_3_mixture_density_k2_global` | 0.001758 | 0.002131 | 3.354 | 8.461 |
| 22 | Fw | `polished_wave4_1_log_cosh_robust_loss_Fw` | 0.001764 | 0.002125 | 3.566 | 8.171 |
| 23 | Fw | `polished_wave4_1_mae_robust_loss_Fw` | 0.001775 | 0.002132 | 3.569 | 8.373 |
| 24 | Fw | `polished_wave3_3_full_curve_composite_Fw` | 0.001786 | 0.002167 | 3.606 | 8.311 |
| 25 | Fw | `polished_wave5_1_harmonic_prior_smooth_l1_structured_Fw` | 0.001795 | 0.002160 | 3.630 | 8.304 |
| 26 | Fw | `polished_rcim_model_bank_reproduction_SVM19_Fw` | 0.001797 | 0.002145 | 3.616 | 10.200 |
| 27 | Fw | `polished_wave4_1_smooth_l1_robust_loss_Fw` | 0.001799 | 0.002176 | 3.645 | 8.067 |
| 28 | Fw | `polished_residual_harmonic_gru_sequence_sparse_rcim_Fw` | 0.001832 | 0.002216 | 3.700 | 8.239 |
| 29 | Fw | `polished_wave5_1_harmonic_prior_pointwise_control_Fw` | 0.001881 | 0.002253 | 3.835 | 8.184 |
| 30 | Fw | `polished_residual_harmonic_lstm_sequence_sparse_rcim_Fw` | 0.001892 | 0.002286 | 3.839 | 8.161 |
| 31 | global | `polished_wave4_1_mae_robust_loss_global` | 0.001907 | 0.002311 | 3.588 | 9.258 |
| 32 | global | `polished_wave4_2_quantile_p10_p50_p90_global` | 0.001908 | 0.002311 | 3.589 | 9.208 |
| 33 | global | `polished_wave4_1_log_cosh_robust_loss_global` | 0.001923 | 0.002317 | 3.610 | 9.289 |
| 34 | Bw | `polished_wave4_3_mixture_density_k3_Bw` | 0.001930 | 0.002341 | 3.405 | 9.512 |
| 35 | global | `polished_wave3_2_harmonic_residual_offset_global` | 0.001936 | 0.002349 | 3.656 | 9.145 |
| 36 | global | `polished_wave3_3_curve_aware_pointwise_control_global` | 0.001967 | 0.002372 | 3.719 | 9.186 |
| 37 | global | `polished_wave3_3_raw_centered_shape_curve_aware_global` | 0.001977 | 0.002372 | 3.710 | 9.358 |
| 38 | Bw | `polished_wave4_3_mixture_density_k2_Bw` | 0.001995 | 0.002403 | 3.526 | 9.548 |
| 39 | Fw | `polished_rcim_model_bank_reproduction_RF19_Fw` | 0.001998 | 0.002293 | 4.243 | 10.816 |
| 40 | Fw | `polished_periodic_temporal_convolution_Fw` | 0.002004 | 0.002385 | 4.123 | 9.059 |
| 41 | global | `polished_wave4_2_gaussian_nll_global` | 0.002006 | 0.002417 | 3.776 | 9.403 |
| 42 | global | `polished_wave3_3_raw_offset_curve_aware_global` | 0.002009 | 0.002428 | 3.824 | 9.323 |
| 43 | global | `polished_wave4_1_smooth_l1_robust_loss_global` | 0.002018 | 0.002417 | 3.821 | 9.619 |
| 44 | global | `polished_wave3_3_full_curve_composite_global` | 0.002028 | 0.002464 | 3.869 | 9.205 |
| 45 | Fw | `polished_wave3_2_clean_sequential_residual_offset_Fw` | 0.002052 | 0.002494 | 4.192 | 8.319 |
| 46 | global | `polished_periodic_mlp_harmonic_global` | 0.002054 | 0.002457 | 3.832 | 9.502 |
| 47 | global | `polished_residual_harmonic_lstm_sequence_sparse_rcim_global` | 0.002069 | 0.002515 | 3.949 | 9.574 |
| 48 | Fw | `polished_wave3_1_sequential_residual_offset_probe_Fw` | 0.002071 | 0.002524 | 4.236 | 8.319 |
| 49 | Fw | `polished_lstm_sequence_Fw` | 0.002083 | 0.002538 | 4.261 | 8.262 |
| 50 | Fw | `polished_residual_harmonic_mlp_Fw` | 0.002093 | 0.002541 | 4.287 | 8.352 |
| 51 | Fw | `polished_gru_sequence_Fw` | 0.002102 | 0.002552 | 4.308 | 8.229 |
| 52 | global | `polished_residual_harmonic_gru_sequence_sparse_rcim_global` | 0.002107 | 0.002548 | 4.033 | 9.587 |
| 53 | Fw | `polished_periodic_mlp_Fw` | 0.002118 | 0.002575 | 4.351 | 8.283 |
| 54 | global | `polished_wave5_1_harmonic_prior_smooth_l1_structured_global` | 0.002121 | 0.002522 | 3.936 | 9.529 |
| 55 | Fw | `polished_tree_Fw` | 0.002125 | 0.002612 | 4.355 | 8.534 |
| 56 | Fw | `polished_feedforward_Fw` | 0.002130 | 0.002586 | 4.378 | 8.431 |
| 57 | Bw | `polished_wave4_1_log_cosh_robust_loss_Bw` | 0.002131 | 0.002576 | 3.787 | 9.666 |
| 58 | Bw | `polished_wave4_1_mae_robust_loss_Bw` | 0.002133 | 0.002572 | 3.754 | 9.697 |
| 59 | Bw | `polished_wave4_2_gaussian_nll_Bw` | 0.002133 | 0.002582 | 3.758 | 9.788 |
| 60 | Bw | `polished_wave3_3_raw_centered_shape_curve_aware_Bw` | 0.002133 | 0.002578 | 3.790 | 9.660 |
| 61 | Bw | `polished_wave4_2_quantile_p10_p50_p90_Bw` | 0.002133 | 0.002585 | 3.778 | 9.700 |
| 62 | Fw | `polished_wave4_4_gru_latent_offset_residual_Fw` | 0.002135 | 0.002611 | 4.373 | 8.386 |
| 63 | Bw | `polished_wave3_3_raw_offset_curve_aware_Bw` | 0.002139 | 0.002591 | 3.806 | 9.694 |
| 64 | Bw | `polished_wave3_2_harmonic_residual_offset_Bw` | 0.002142 | 0.002591 | 3.805 | 9.658 |
| 65 | Fw | `polished_wave4_4_causal_tcn_latent_offset_residual_Fw` | 0.002149 | 0.002620 | 4.408 | 8.453 |
| 66 | global | `polished_wave5_1_harmonic_prior_pointwise_control_global` | 0.002153 | 0.002556 | 4.001 | 9.336 |
| 67 | Bw | `polished_wave3_3_curve_aware_pointwise_control_Bw` | 0.002172 | 0.002638 | 3.909 | 9.815 |
| 68 | Fw | `polished_temporal_convolution_Fw` | 0.002210 | 0.002686 | 4.557 | 8.559 |
| 69 | global | `polished_gru_sequence_global` | 0.002235 | 0.002722 | 4.313 | 9.564 |
| 70 | Bw | `polished_wave4_1_smooth_l1_robust_loss_Bw` | 0.002236 | 0.002696 | 4.026 | 9.581 |
| 71 | global | `polished_wave3_1_sequential_residual_offset_probe_global` | 0.002252 | 0.002737 | 4.348 | 9.622 |
| 72 | global | `polished_lstm_sequence_global` | 0.002266 | 0.002753 | 4.390 | 9.554 |
| 73 | global | `polished_wave3_2_clean_sequential_residual_offset_global` | 0.002276 | 0.002760 | 4.397 | 9.579 |
| 74 | global | `polished_wave4_4_gru_latent_offset_residual_global` | 0.002306 | 0.002807 | 4.470 | 9.612 |
| 75 | global | `polished_periodic_temporal_convolution_global` | 0.002318 | 0.002743 | 4.527 | 9.986 |
| 76 | global | `polished_wave4_4_causal_tcn_latent_offset_residual_global` | 0.002321 | 0.002831 | 4.493 | 9.907 |
| 77 | Bw | `polished_periodic_temporal_convolution_Bw` | 0.002326 | 0.002803 | 4.277 | 9.862 |
| 78 | Bw | `polished_residual_harmonic_gru_sequence_sparse_rcim_Bw` | 0.002331 | 0.002829 | 4.234 | 9.948 |
| 79 | Bw | `polished_wave3_3_full_curve_composite_Bw` | 0.002333 | 0.002822 | 4.250 | 9.763 |
| 80 | Bw | `polished_residual_harmonic_lstm_sequence_sparse_rcim_Bw` | 0.002343 | 0.002825 | 4.242 | 9.919 |
| 81 | Fw | `polished_rcim_model_bank_reproduction_DT19_Fw` | 0.002373 | 0.002664 | 5.004 | 11.005 |
| 82 | Bw | `polished_periodic_mlp_harmonic_Bw` | 0.002396 | 0.002823 | 4.137 | 10.607 |
| 83 | global | `polished_temporal_convolution_global` | 0.002398 | 0.002909 | 4.702 | 9.713 |
| 84 | global | `polished_feedforward_global` | 0.002404 | 0.002907 | 4.575 | 10.056 |
| 85 | Bw | `polished_wave3_1_sequential_residual_offset_probe_Bw` | 0.002411 | 0.002947 | 4.412 | 10.138 |
| 86 | global | `polished_residual_harmonic_mlp_global` | 0.002411 | 0.002910 | 4.592 | 10.130 |
| 87 | Bw | `polished_wave5_1_harmonic_prior_pointwise_control_Bw` | 0.002418 | 0.002843 | 4.202 | 10.476 |
| 88 | global | `polished_periodic_mlp_global` | 0.002421 | 0.002922 | 4.606 | 9.853 |
| 89 | Bw | `polished_gru_sequence_Bw` | 0.002425 | 0.002937 | 4.438 | 10.148 |
| 90 | Bw | `polished_lstm_sequence_Bw` | 0.002430 | 0.002973 | 4.452 | 10.190 |
| 91 | global | `polished_tree_global` | 0.002431 | 0.002939 | 4.635 | 9.931 |
| 92 | Bw | `polished_wave3_2_clean_sequential_residual_offset_Bw` | 0.002439 | 0.002959 | 4.469 | 10.192 |
| 93 | Bw | `polished_wave4_4_gru_latent_offset_residual_Bw` | 0.002455 | 0.002998 | 4.512 | 10.190 |
| 94 | Bw | `polished_wave4_4_causal_tcn_latent_offset_residual_Bw` | 0.002485 | 0.003022 | 4.545 | 10.210 |
| 95 | Bw | `polished_wave5_1_harmonic_prior_smooth_l1_structured_Bw` | 0.002528 | 0.002976 | 4.377 | 10.763 |
| 96 | Bw | `polished_temporal_convolution_Bw` | 0.002530 | 0.003060 | 4.674 | 10.195 |
| 97 | Fw | `polished_rcim_model_bank_reproduction_HGBM19_Fw` | 0.002606 | 0.002910 | 5.628 | 12.844 |
| 98 | Bw | `polished_feedforward_Bw` | 0.002655 | 0.003193 | 4.708 | 10.602 |
| 99 | Bw | `polished_residual_harmonic_mlp_Bw` | 0.002713 | 0.003255 | 4.822 | 10.624 |
| 100 | Bw | `polished_tree_Bw` | 0.002756 | 0.003287 | 4.934 | 10.752 |
| 101 | Bw | `polished_periodic_mlp_Bw` | 0.002769 | 0.003282 | 4.910 | 10.607 |
| 102 | Fw | `polished_rcim_model_bank_reproduction_XGBM19_Fw` | 0.003028 | 0.003304 | 6.606 | 18.657 |
| 103 | global | `polished_residual_harmonic_gru_sequence_dense240_global` | 0.003121 | 0.003993 | 6.395 | 10.129 |
| 104 | Fw | `polished_residual_harmonic_gru_sequence_dense240_Fw` | 0.003186 | 0.004142 | 6.811 | 9.157 |
| 105 | Fw | `polished_residual_harmonic_lstm_sequence_dense240_Fw` | 0.003240 | 0.004196 | 6.948 | 9.142 |
| 106 | global | `polished_residual_harmonic_lstm_sequence_dense240_global` | 0.003329 | 0.004300 | 6.862 | 10.535 |
| 107 | Bw | `polished_residual_harmonic_gru_sequence_dense240_Bw` | 0.003416 | 0.004405 | 6.794 | 10.465 |
| 108 | Bw | `polished_residual_harmonic_lstm_sequence_dense240_Bw` | 0.003569 | 0.004639 | 7.137 | 10.677 |
| 109 | Bw | `polished_rcim_model_bank_reproduction_ERT19_Bw` | 0.003715 | 0.003957 | 7.516 | 43.149 |
| 110 | Bw | `polished_rcim_model_bank_reproduction_LGBM19_Bw` | 0.003765 | 0.004028 | 7.677 | 43.640 |
| 111 | global | `polished_harmonic_regression_global` | 0.003979 | 0.004503 | 8.163 | 14.763 |
| 112 | Bw | `polished_rcim_model_bank_reproduction_ET19_Bw` | 0.004034 | 0.004316 | 8.163 | 41.965 |
| 113 | Bw | `polished_rcim_model_bank_reproduction_DT19_Bw` | 0.004395 | 0.004659 | 9.372 | 39.764 |
| 114 | Bw | `polished_rcim_model_bank_reproduction_SVM19_Bw` | 0.004409 | 0.004851 | 8.793 | 38.822 |
| 115 | Bw | `polished_rcim_model_bank_reproduction_GBM19_Bw` | 0.004482 | 0.004755 | 9.169 | 43.941 |
| 116 | Fw | `polished_residual_harmonic_gru_sequence_dense360_Fw` | 0.004563 | 0.007628 | 9.896 | 11.402 |
| 117 | global | `polished_residual_harmonic_lstm_sequence_dense360_global` | 0.004618 | 0.006711 | 9.753 | 12.396 |
| 118 | global | `polished_residual_harmonic_gru_sequence_dense360_global` | 0.004631 | 0.006987 | 9.827 | 12.042 |
| 119 | Fw | `polished_residual_harmonic_lstm_sequence_dense360_Fw` | 0.004652 | 0.007237 | 10.094 | 11.605 |
| 120 | Bw | `polished_rcim_model_bank_reproduction_RF19_Bw` | 0.004852 | 0.005155 | 10.113 | 46.318 |
| 121 | Bw | `polished_rcim_model_bank_reproduction_HGBM19_Bw` | 0.004919 | 0.005254 | 10.239 | 44.526 |
| 122 | Bw | `polished_residual_harmonic_lstm_sequence_dense360_Bw` | 0.005029 | 0.007977 | 10.455 | 12.921 |
| 123 | Bw | `polished_residual_harmonic_gru_sequence_dense360_Bw` | 0.005031 | 0.008128 | 10.446 | 12.856 |
| 124 | Bw | `polished_rcim_model_bank_reproduction_XGBM19_Bw` | 0.005286 | 0.005591 | 11.237 | 48.248 |
| 125 | Bw | `polished_harmonic_regression_Bw` | 0.008041 | 0.008675 | 16.236 | 27.309 |
| 126 | Fw | `polished_rcim_model_bank_reproduction_MLP19_Fw` | 0.036479 | 0.044676 | 82.877 | 244.026 |
| 127 | Fw | `polished_harmonic_regression_Fw` | 0.062598 | 0.062702 | 133.783 | 271.628 |
| 128 | Bw | `polished_rcim_model_bank_reproduction_MLP19_Bw` | 0.062780 | 0.077368 | 139.565 | 338.222 |

## Current Direction Leaders

These leaders are read from the full matrix direction breakdown after the
refresh. This table includes historical comparison anchors as well as the new
polished candidates; therefore the forward all-matrix leader can differ from
the refreshed polished-source leader.

| Direction | Candidate | MAE [deg] | RMSE [deg] | Mean [%] | P95 [%] |
| --- | --- | ---: | ---: | ---: | ---: |
| backward | `polished_periodic_gru_sequence_Bw` | 0.001129 | 0.001412 | 2.228 | 4.688 |
| forward | `rcim_retuned_GBM19_Fw` | 0.001089 | 0.001299 | 2.372 | 4.912 |

## Visual Evidence

The same launcher run regenerated the visual companion reports and verified
that the refreshed source appears in the visual package.

| Source | Collage | Overlay Forward | Overlay Backward |
| --- | ---: | ---: | ---: |
| `polished_model_development_registry`, `polished_rcim_model_bank_reproduction` | 108 | 36 | 36 |

## Closeout Decision

`polished-dataset RCIM and full model-development refresh` is closed as:
accepted official TE Curve Verification Pipeline refresh on `2026-07-03`.

The polished refresh changes the accepted model-development baseline to the
`polished_periodic_gru_sequence` family. Direction-specific evidence remains
parallel rather than destructive: the historical full-matrix forward leader
remains `rcim_retuned_GBM19_Fw`, the polished RCIM model bank supplies the best
forward refreshed-source reference-bank curve candidate, and the polished
periodic GRU sequence family supplies the strongest backward, global, and
deployable model-development evidence.

No `paper original` or paper-retuned candidate was retrained by this refresh.
The pre-polished historical candidates remain in the matrix only as comparison
anchors.
