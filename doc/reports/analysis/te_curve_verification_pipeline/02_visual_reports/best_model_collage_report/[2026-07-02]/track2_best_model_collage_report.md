# TE Curve Verification Pipeline Best Model Collage Report

## Overview

This report compares representative `TE Curve Verification Pipeline` TE-curve predictions for
the current best reference, RCIM Model-Bank Reproduction, Wave 1 directional, and Wave 1
global models. Each model is shown as one four-image collage so local
oscillation tracking can be inspected directly.

## Scope

- each collage contains four deterministic held-out test curves;
- forward models are shown on forward curves only;
- backward models are shown on backward curves only;
- global Wave 1 models are shown on two forward and two backward curves;
- `Measured TE` uses the same line width as predictions and a dark-gray
  color for balanced visual comparison.

## Metrics Summary

### Forward Reference Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_original_best_fw` | `rcim_original` | Fw | 0.013058 | 0.013324 | 27.997 |
| `paper_retuned_best_fw` | `rcim_retuned` | Fw | 0.029204 | 0.029350 | 62.562 |
| `track1_best_fw` | `rcim_track1` | Fw | 0.062756 | 0.062835 | 134.143 |

### Backward Reference Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `track1_best_bw` | `rcim_track1` | Bw | 0.006633 | 0.007119 | 13.713 |

### Forward Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_fw` | `wave1_current_registry` | Fw | 0.002130 | 0.002586 | 4.378 |
| `harmonic_regression_fw` | `wave1_current_registry` | Fw | 0.062598 | 0.062702 | 133.783 |
| `periodic_mlp_fw` | `wave1_current_registry` | Fw | 0.002118 | 0.002575 | 4.351 |
| `residual_harmonic_mlp_fw` | `wave1_current_registry` | Fw | 0.002234 | 0.002695 | 4.616 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.002125 | 0.002612 | 4.355 |
| `periodic_mlp_harmonic_fw` | `wave1_periodic_mlp_harmonic_campaign` | Fw | 0.038372 | 0.039223 | 82.451 |

### Backward Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_bw` | `wave1_current_registry` | Bw | 0.002680 | 0.003213 | 4.759 |
| `harmonic_regression_bw` | `wave1_current_registry` | Bw | 0.008041 | 0.008675 | 16.236 |
| `periodic_mlp_bw` | `wave1_current_registry` | Bw | 0.002700 | 0.003230 | 4.793 |
| `residual_harmonic_mlp_bw` | `wave1_current_registry` | Bw | 0.002713 | 0.003255 | 4.822 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `periodic_mlp_harmonic_bw` | `wave1_periodic_mlp_harmonic_campaign` | Bw | 0.013927 | 0.014623 | 28.984 |

### Global Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_global` | `wave1_current_registry` | global | 0.003242 | 0.003867 | 6.502 |
| `harmonic_regression_global` | `wave1_current_registry` | global | 0.003946 | 0.004463 | 8.097 |
| `periodic_mlp_global` | `wave1_current_registry` | global | 0.020015 | 0.020667 | 42.524 |
| `residual_harmonic_mlp_global` | `wave1_current_registry` | global | 0.021834 | 0.022135 | 45.955 |
| `tree_global` | `wave1_current_registry` | global | 0.002431 | 0.002939 | 4.635 |
| `periodic_mlp_harmonic_global` | `wave1_periodic_mlp_harmonic_campaign` | global | 0.019249 | 0.019792 | 40.938 |

### Forward Wave 2.1 Temporal Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.002210 | 0.002686 | 4.557 |
| `gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.002078 | 0.002536 | 4.254 |
| `lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.002083 | 0.002538 | 4.261 |
| `periodic_temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.002004 | 0.002385 | 4.123 |
| `periodic_gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.001195 | 0.001461 | 2.559 |
| `periodic_lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.001730 | 0.002084 | 3.517 |

### Backward Wave 2.1 Temporal Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002566 | 0.003101 | 4.747 |
| `gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002440 | 0.002971 | 4.477 |
| `lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002430 | 0.002973 | 4.452 |
| `periodic_temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002482 | 0.002972 | 4.647 |
| `periodic_gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001129 | 0.001412 | 2.228 |
| `periodic_lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001405 | 0.001757 | 2.700 |

### Global Wave 2.1 Temporal Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_global` | `wave2_temporal_entry_registry` | global | 0.015819 | 0.016489 | 33.689 |
| `gru_sequence_global` | `wave2_temporal_entry_registry` | global | 0.019324 | 0.020436 | 40.840 |
| `lstm_sequence_global` | `wave2_temporal_entry_registry` | global | 0.015469 | 0.016606 | 32.362 |
| `periodic_temporal_convolution_global` | `wave2_temporal_entry_registry` | global | 0.019806 | 0.020351 | 42.088 |
| `periodic_gru_sequence_global` | `wave2_temporal_entry_registry` | global | 0.001368 | 0.001689 | 2.783 |
| `periodic_lstm_sequence_global` | `wave2_temporal_entry_registry` | global | 0.021008 | 0.021669 | 44.372 |

### Forward Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.045021 | 0.045184 | 96.691 |
| `residual_harmonic_gru_sequence_dense240_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.037261 | 0.038590 | 80.109 |
| `residual_harmonic_gru_sequence_dense360_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.038030 | 0.039604 | 81.958 |
| `residual_harmonic_lstm_sequence_sparse_rcim_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.042694 | 0.042917 | 91.847 |
| `residual_harmonic_lstm_sequence_dense240_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.034610 | 0.035965 | 74.503 |
| `residual_harmonic_lstm_sequence_dense360_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.033574 | 0.035202 | 72.338 |

### Backward Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.010936 | 0.011364 | 22.574 |
| `residual_harmonic_gru_sequence_dense240_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.020530 | 0.024251 | 43.464 |
| `residual_harmonic_gru_sequence_dense360_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.015162 | 0.018761 | 32.047 |
| `residual_harmonic_lstm_sequence_sparse_rcim_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.011676 | 0.012103 | 23.908 |
| `residual_harmonic_lstm_sequence_dense240_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.016792 | 0.019189 | 35.128 |
| `residual_harmonic_lstm_sequence_dense360_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.015864 | 0.020039 | 33.657 |

### Global Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.002125 | 0.002564 | 4.063 |
| `residual_harmonic_gru_sequence_dense240_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.023609 | 0.025357 | 50.450 |
| `residual_harmonic_gru_sequence_dense360_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.025279 | 0.027755 | 54.017 |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.020851 | 0.021154 | 44.178 |
| `residual_harmonic_lstm_sequence_dense240_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.025395 | 0.026906 | 54.290 |
| `residual_harmonic_lstm_sequence_dense360_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.022205 | 0.025320 | 47.717 |

### Forward Wave 3.1 Offset-Aware Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_fw` | `wave3_1_offset_aware_probe_registry` | Fw | 0.036294 | 0.036467 | 77.932 |

### Backward Wave 3.1 Offset-Aware Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_bw` | `wave3_1_offset_aware_probe_registry` | Bw | 0.008945 | 0.009670 | 18.730 |

### Global Wave 3.1 Offset-Aware Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_global` | `wave3_1_offset_aware_probe_registry` | global | 0.010335 | 0.011447 | 21.780 |

### Forward Wave 3.2 Harmonic-Offset Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_fw` | `wave3_2_harmonic_offset_probe_registry` | Fw | 0.045185 | 0.045455 | 97.083 |
| `wave3_2_harmonic_residual_offset_fw` | `wave3_2_harmonic_offset_probe_registry` | Fw | 0.059869 | 0.059969 | 127.873 |

### Backward Wave 3.2 Harmonic-Offset Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_bw` | `wave3_2_harmonic_offset_probe_registry` | Bw | 0.008376 | 0.009258 | 17.556 |
| `wave3_2_harmonic_residual_offset_bw` | `wave3_2_harmonic_offset_probe_registry` | Bw | 0.012996 | 0.013533 | 26.826 |

### Global Wave 3.2 Harmonic-Offset Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_global` | `wave3_2_harmonic_offset_probe_registry` | global | 0.010931 | 0.011645 | 23.153 |
| `wave3_2_harmonic_residual_offset_global` | `wave3_2_harmonic_offset_probe_registry` | global | 0.024458 | 0.024780 | 52.055 |

### Forward Wave 3.3 Curve-Aware Training Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.044577 | 0.044713 | 95.253 |
| `wave3_3_raw_centered_shape_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.037030 | 0.037237 | 79.717 |
| `wave3_3_raw_offset_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.058349 | 0.058552 | 124.991 |
| `wave3_3_full_curve_composite_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.050091 | 0.050255 | 107.778 |

### Backward Wave 3.3 Curve-Aware Training Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.009939 | 0.010532 | 20.584 |
| `wave3_3_raw_centered_shape_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.010075 | 0.010673 | 20.657 |
| `wave3_3_raw_offset_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.011255 | 0.011824 | 23.166 |
| `wave3_3_full_curve_composite_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.012620 | 0.013521 | 25.713 |

### Global Wave 3.3 Curve-Aware Training Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_global` | `wave3_3_curve_aware_training_registry` | global | 0.014650 | 0.015045 | 31.212 |
| `wave3_3_raw_centered_shape_curve_aware_global` | `wave3_3_curve_aware_training_registry` | global | 0.009702 | 0.010170 | 20.917 |
| `wave3_3_raw_offset_curve_aware_global` | `wave3_3_curve_aware_training_registry` | global | 0.009712 | 0.010143 | 20.524 |
| `wave3_3_full_curve_composite_global` | `wave3_3_curve_aware_training_registry` | global | 0.002021 | 0.002448 | 3.824 |

### Forward Wave 4.1 Robust-Loss Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.049061 | 0.049181 | 105.141 |
| `wave4_1_smooth_l1_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.058171 | 0.058283 | 124.441 |
| `wave4_1_log_cosh_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.054964 | 0.055089 | 117.915 |

### Backward Wave 4.1 Robust-Loss Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.014320 | 0.014747 | 30.084 |
| `wave4_1_smooth_l1_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.012012 | 0.012561 | 24.411 |
| `wave4_1_log_cosh_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.009813 | 0.010421 | 19.966 |

### Global Wave 4.1 Robust-Loss Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_global` | `wave4_1_robust_loss_registry` | global | 0.009839 | 0.010272 | 20.969 |
| `wave4_1_smooth_l1_robust_loss_global` | `wave4_1_robust_loss_registry` | global | 0.024904 | 0.025183 | 52.984 |
| `wave4_1_log_cosh_robust_loss_global` | `wave4_1_robust_loss_registry` | global | 0.008761 | 0.009218 | 18.772 |

### Forward Wave 4.2 Quantile Probabilistic Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_fw` | `wave4_2_probabilistic_registry` | Fw | 0.050281 | 0.050425 | 107.720 |
| `wave4_2_gaussian_nll_fw` | `wave4_2_probabilistic_registry` | Fw | 0.054985 | 0.055109 | 117.675 |

### Backward Wave 4.2 Quantile Probabilistic Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_bw` | `wave4_2_probabilistic_registry` | Bw | 0.011462 | 0.011942 | 23.503 |
| `wave4_2_gaussian_nll_bw` | `wave4_2_probabilistic_registry` | Bw | 0.009739 | 0.010201 | 20.349 |

### Global Wave 4.2 Quantile Probabilistic Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_global` | `wave4_2_probabilistic_registry` | global | 0.023037 | 0.023327 | 48.983 |
| `wave4_2_gaussian_nll_global` | `wave4_2_probabilistic_registry` | global | 0.013087 | 0.013458 | 27.845 |

### Forward Wave 4.3 Mixture Density Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_fw` | `wave4_3_mixture_density_registry` | Fw | 0.047438 | 0.047677 | 102.227 |
| `wave4_3_mixture_density_k3_fw` | `wave4_3_mixture_density_registry` | Fw | 0.057840 | 0.057965 | 124.009 |

### Backward Wave 4.3 Mixture Density Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_bw` | `wave4_3_mixture_density_registry` | Bw | 0.008282 | 0.010642 | 16.490 |
| `wave4_3_mixture_density_k3_bw` | `wave4_3_mixture_density_registry` | Bw | 0.011511 | 0.011910 | 23.777 |

### Global Wave 4.3 Mixture Density Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_global` | `wave4_3_mixture_density_registry` | global | 0.012978 | 0.013430 | 27.105 |
| `wave4_3_mixture_density_k3_global` | `wave4_3_mixture_density_registry` | global | 0.012184 | 0.012600 | 25.767 |

### Forward Wave 4.4 Latent State Hysteresis Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_fw` | `wave4_4_latent_state_hysteresis_registry` | Fw | 0.024419 | 0.025009 | 52.319 |
| `wave4_4_causal_tcn_latent_offset_residual_fw` | `wave4_4_latent_state_hysteresis_registry` | Fw | 0.028476 | 0.028960 | 61.107 |

### Backward Wave 4.4 Latent State Hysteresis Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_bw` | `wave4_4_latent_state_hysteresis_registry` | Bw | 0.016484 | 0.016958 | 34.591 |
| `wave4_4_causal_tcn_latent_offset_residual_bw` | `wave4_4_latent_state_hysteresis_registry` | Bw | 0.007773 | 0.008896 | 15.746 |

### Global Wave 4.4 Latent State Hysteresis Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_global` | `wave4_4_latent_state_hysteresis_registry` | global | 0.002346 | 0.002846 | 4.572 |
| `wave4_4_causal_tcn_latent_offset_residual_global` | `wave4_4_latent_state_hysteresis_registry` | global | 0.021583 | 0.022991 | 46.360 |

### Forward Wave 5.1 Harmonic Prior Residual Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_fw` | `wave5_1_harmonic_prior_residual_registry` | Fw | 0.046994 | 0.047257 | 100.353 |
| `wave5_1_harmonic_prior_smooth_l1_structured_fw` | `wave5_1_harmonic_prior_residual_registry` | Fw | 0.047938 | 0.048105 | 102.360 |

### Backward Wave 5.1 Harmonic Prior Residual Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_bw` | `wave5_1_harmonic_prior_residual_registry` | Bw | 0.009485 | 0.010128 | 19.928 |
| `wave5_1_harmonic_prior_smooth_l1_structured_bw` | `wave5_1_harmonic_prior_residual_registry` | Bw | 0.011508 | 0.012082 | 24.388 |

### Global Wave 5.1 Harmonic Prior Residual Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_global` | `wave5_1_harmonic_prior_residual_registry` | global | 0.007113 | 0.007629 | 14.995 |
| `wave5_1_harmonic_prior_smooth_l1_structured_global` | `wave5_1_harmonic_prior_residual_registry` | global | 0.002163 | 0.002571 | 4.046 |

### Forward Wave52b Offset Harmonic Guided Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_fw` | `wave52b_offset_harmonic_guided_registry` | Fw | 0.001695 | 0.002045 | 3.391 |

### Backward Wave52b Offset Harmonic Guided Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_bw` | `wave52b_offset_harmonic_guided_registry` | Bw | 0.002266 | 0.002708 | 3.986 |

### Global Wave52b Offset Harmonic Guided Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_global` | `wave52b_offset_harmonic_guided_registry` | global | 0.002221 | 0.002629 | 4.184 |

## Collage Gallery - Forward Reference Best Models

paper_original_best_fw:

![paper_original_best_fw TE Curve Verification Pipeline collage](assets/forward_reference/paper_original_best_fw.png)

paper_retuned_best_fw:

![paper_retuned_best_fw TE Curve Verification Pipeline collage](assets/forward_reference/paper_retuned_best_fw.png)

## Collage Gallery - Forward Reference Best Models Continued

track1_best_fw:

![track1_best_fw TE Curve Verification Pipeline collage](assets/forward_reference/track1_best_fw.png)

## Collage Gallery - Backward Reference Best Models

paper_retuned_best_bw:

![paper_retuned_best_bw TE Curve Verification Pipeline collage](assets/backward_reference/paper_retuned_best_bw.png)

track1_best_bw:

![track1_best_bw TE Curve Verification Pipeline collage](assets/backward_reference/track1_best_bw.png)

## Collage Gallery - Forward Wave 1 Family Best Models

feedforward_fw:

![feedforward_fw TE Curve Verification Pipeline collage](assets/forward_wave1/feedforward_fw.png)

harmonic_regression_fw:

![harmonic_regression_fw TE Curve Verification Pipeline collage](assets/forward_wave1/harmonic_regression_fw.png)

## Collage Gallery - Forward Wave 1 Family Best Models Continued

periodic_mlp_fw:

![periodic_mlp_fw TE Curve Verification Pipeline collage](assets/forward_wave1/periodic_mlp_fw.png)

residual_harmonic_mlp_fw:

![residual_harmonic_mlp_fw TE Curve Verification Pipeline collage](assets/forward_wave1/residual_harmonic_mlp_fw.png)

## Collage Gallery - Forward Wave 1 Family Best Models Continued 2

tree_fw:

![tree_fw TE Curve Verification Pipeline collage](assets/forward_wave1/tree_fw.png)

periodic_mlp_harmonic_fw:

![periodic_mlp_harmonic_fw TE Curve Verification Pipeline collage](assets/forward_wave1/periodic_mlp_harmonic_fw.png)

## Collage Gallery - Backward Wave 1 Family Best Models

feedforward_bw:

![feedforward_bw TE Curve Verification Pipeline collage](assets/backward_wave1/feedforward_bw.png)

harmonic_regression_bw:

![harmonic_regression_bw TE Curve Verification Pipeline collage](assets/backward_wave1/harmonic_regression_bw.png)

## Collage Gallery - Backward Wave 1 Family Best Models Continued

periodic_mlp_bw:

![periodic_mlp_bw TE Curve Verification Pipeline collage](assets/backward_wave1/periodic_mlp_bw.png)

residual_harmonic_mlp_bw:

![residual_harmonic_mlp_bw TE Curve Verification Pipeline collage](assets/backward_wave1/residual_harmonic_mlp_bw.png)

## Collage Gallery - Backward Wave 1 Family Best Models Continued 2

tree_bw:

![tree_bw TE Curve Verification Pipeline collage](assets/backward_wave1/tree_bw.png)

periodic_mlp_harmonic_bw:

![periodic_mlp_harmonic_bw TE Curve Verification Pipeline collage](assets/backward_wave1/periodic_mlp_harmonic_bw.png)

## Collage Gallery - Global Wave 1 Family Best Models

feedforward_global:

![feedforward_global TE Curve Verification Pipeline collage](assets/global_wave1/feedforward_global.png)

harmonic_regression_global:

![harmonic_regression_global TE Curve Verification Pipeline collage](assets/global_wave1/harmonic_regression_global.png)

## Collage Gallery - Global Wave 1 Family Best Models Continued

periodic_mlp_global:

![periodic_mlp_global TE Curve Verification Pipeline collage](assets/global_wave1/periodic_mlp_global.png)

residual_harmonic_mlp_global:

![residual_harmonic_mlp_global TE Curve Verification Pipeline collage](assets/global_wave1/residual_harmonic_mlp_global.png)

## Collage Gallery - Global Wave 1 Family Best Models Continued 2

tree_global:

![tree_global TE Curve Verification Pipeline collage](assets/global_wave1/tree_global.png)

periodic_mlp_harmonic_global:

![periodic_mlp_harmonic_global TE Curve Verification Pipeline collage](assets/global_wave1/periodic_mlp_harmonic_global.png)

## Collage Gallery - Forward Wave 2.1 Temporal Family Best Models

temporal_convolution_fw:

![temporal_convolution_fw TE Curve Verification Pipeline collage](assets/forward_wave2/temporal_convolution_fw.png)

gru_sequence_fw:

![gru_sequence_fw TE Curve Verification Pipeline collage](assets/forward_wave2/gru_sequence_fw.png)

## Collage Gallery - Forward Wave 2.1 Temporal Family Best Models Continued

lstm_sequence_fw:

![lstm_sequence_fw TE Curve Verification Pipeline collage](assets/forward_wave2/lstm_sequence_fw.png)

periodic_temporal_convolution_fw:

![periodic_temporal_convolution_fw TE Curve Verification Pipeline collage](assets/forward_wave2/periodic_temporal_convolution_fw.png)

## Collage Gallery - Forward Wave 2.1 Temporal Family Best Models Continued 2

periodic_gru_sequence_fw:

![periodic_gru_sequence_fw TE Curve Verification Pipeline collage](assets/forward_wave2/periodic_gru_sequence_fw.png)

periodic_lstm_sequence_fw:

![periodic_lstm_sequence_fw TE Curve Verification Pipeline collage](assets/forward_wave2/periodic_lstm_sequence_fw.png)

## Collage Gallery - Backward Wave 2.1 Temporal Family Best Models

temporal_convolution_bw:

![temporal_convolution_bw TE Curve Verification Pipeline collage](assets/backward_wave2/temporal_convolution_bw.png)

gru_sequence_bw:

![gru_sequence_bw TE Curve Verification Pipeline collage](assets/backward_wave2/gru_sequence_bw.png)

## Collage Gallery - Backward Wave 2.1 Temporal Family Best Models Continued

lstm_sequence_bw:

![lstm_sequence_bw TE Curve Verification Pipeline collage](assets/backward_wave2/lstm_sequence_bw.png)

periodic_temporal_convolution_bw:

![periodic_temporal_convolution_bw TE Curve Verification Pipeline collage](assets/backward_wave2/periodic_temporal_convolution_bw.png)

## Collage Gallery - Backward Wave 2.1 Temporal Family Best Models Continued 2

periodic_gru_sequence_bw:

![periodic_gru_sequence_bw TE Curve Verification Pipeline collage](assets/backward_wave2/periodic_gru_sequence_bw.png)

periodic_lstm_sequence_bw:

![periodic_lstm_sequence_bw TE Curve Verification Pipeline collage](assets/backward_wave2/periodic_lstm_sequence_bw.png)

## Collage Gallery - Global Wave 2.1 Temporal Family Best Models

temporal_convolution_global:

![temporal_convolution_global TE Curve Verification Pipeline collage](assets/global_wave2/temporal_convolution_global.png)

gru_sequence_global:

![gru_sequence_global TE Curve Verification Pipeline collage](assets/global_wave2/gru_sequence_global.png)

## Collage Gallery - Global Wave 2.1 Temporal Family Best Models Continued

lstm_sequence_global:

![lstm_sequence_global TE Curve Verification Pipeline collage](assets/global_wave2/lstm_sequence_global.png)

periodic_temporal_convolution_global:

![periodic_temporal_convolution_global TE Curve Verification Pipeline collage](assets/global_wave2/periodic_temporal_convolution_global.png)

## Collage Gallery - Global Wave 2.1 Temporal Family Best Models Continued 2

periodic_gru_sequence_global:

![periodic_gru_sequence_global TE Curve Verification Pipeline collage](assets/global_wave2/periodic_gru_sequence_global.png)

periodic_lstm_sequence_global:

![periodic_lstm_sequence_global TE Curve Verification Pipeline collage](assets/global_wave2/periodic_lstm_sequence_global.png)

## Collage Gallery - Forward Wave 2.3 Residual Harmonic Temporal Models

residual_harmonic_gru_sequence_sparse_rcim_fw:

![residual_harmonic_gru_sequence_sparse_rcim_fw TE Curve Verification Pipeline collage](assets/forward_wave2c/residual_harmonic_gru_sequence_sparse_rcim_fw.png)

residual_harmonic_gru_sequence_dense240_fw:

![residual_harmonic_gru_sequence_dense240_fw TE Curve Verification Pipeline collage](assets/forward_wave2c/residual_harmonic_gru_sequence_dense240_fw.png)

## Collage Gallery - Forward Wave 2.3 Residual Harmonic Temporal Models Continued

residual_harmonic_gru_sequence_dense360_fw:

![residual_harmonic_gru_sequence_dense360_fw TE Curve Verification Pipeline collage](assets/forward_wave2c/residual_harmonic_gru_sequence_dense360_fw.png)

residual_harmonic_lstm_sequence_sparse_rcim_fw:

![residual_harmonic_lstm_sequence_sparse_rcim_fw TE Curve Verification Pipeline collage](assets/forward_wave2c/residual_harmonic_lstm_sequence_sparse_rcim_fw.png)

## Collage Gallery - Forward Wave 2.3 Residual Harmonic Temporal Models Continued 2

residual_harmonic_lstm_sequence_dense240_fw:

![residual_harmonic_lstm_sequence_dense240_fw TE Curve Verification Pipeline collage](assets/forward_wave2c/residual_harmonic_lstm_sequence_dense240_fw.png)

residual_harmonic_lstm_sequence_dense360_fw:

![residual_harmonic_lstm_sequence_dense360_fw TE Curve Verification Pipeline collage](assets/forward_wave2c/residual_harmonic_lstm_sequence_dense360_fw.png)

## Collage Gallery - Backward Wave 2.3 Residual Harmonic Temporal Models

residual_harmonic_gru_sequence_sparse_rcim_bw:

![residual_harmonic_gru_sequence_sparse_rcim_bw TE Curve Verification Pipeline collage](assets/backward_wave2c/residual_harmonic_gru_sequence_sparse_rcim_bw.png)

residual_harmonic_gru_sequence_dense240_bw:

![residual_harmonic_gru_sequence_dense240_bw TE Curve Verification Pipeline collage](assets/backward_wave2c/residual_harmonic_gru_sequence_dense240_bw.png)

## Collage Gallery - Backward Wave 2.3 Residual Harmonic Temporal Models Continued

residual_harmonic_gru_sequence_dense360_bw:

![residual_harmonic_gru_sequence_dense360_bw TE Curve Verification Pipeline collage](assets/backward_wave2c/residual_harmonic_gru_sequence_dense360_bw.png)

residual_harmonic_lstm_sequence_sparse_rcim_bw:

![residual_harmonic_lstm_sequence_sparse_rcim_bw TE Curve Verification Pipeline collage](assets/backward_wave2c/residual_harmonic_lstm_sequence_sparse_rcim_bw.png)

## Collage Gallery - Backward Wave 2.3 Residual Harmonic Temporal Models Continued 2

residual_harmonic_lstm_sequence_dense240_bw:

![residual_harmonic_lstm_sequence_dense240_bw TE Curve Verification Pipeline collage](assets/backward_wave2c/residual_harmonic_lstm_sequence_dense240_bw.png)

residual_harmonic_lstm_sequence_dense360_bw:

![residual_harmonic_lstm_sequence_dense360_bw TE Curve Verification Pipeline collage](assets/backward_wave2c/residual_harmonic_lstm_sequence_dense360_bw.png)

## Collage Gallery - Global Wave 2.3 Residual Harmonic Temporal Models

residual_harmonic_gru_sequence_sparse_rcim_global:

![residual_harmonic_gru_sequence_sparse_rcim_global TE Curve Verification Pipeline collage](assets/global_wave2c/residual_harmonic_gru_sequence_sparse_rcim_global.png)

residual_harmonic_gru_sequence_dense240_global:

![residual_harmonic_gru_sequence_dense240_global TE Curve Verification Pipeline collage](assets/global_wave2c/residual_harmonic_gru_sequence_dense240_global.png)

## Collage Gallery - Global Wave 2.3 Residual Harmonic Temporal Models Continued

residual_harmonic_gru_sequence_dense360_global:

![residual_harmonic_gru_sequence_dense360_global TE Curve Verification Pipeline collage](assets/global_wave2c/residual_harmonic_gru_sequence_dense360_global.png)

residual_harmonic_lstm_sequence_sparse_rcim_global:

![residual_harmonic_lstm_sequence_sparse_rcim_global TE Curve Verification Pipeline collage](assets/global_wave2c/residual_harmonic_lstm_sequence_sparse_rcim_global.png)

## Collage Gallery - Global Wave 2.3 Residual Harmonic Temporal Models Continued 2

residual_harmonic_lstm_sequence_dense240_global:

![residual_harmonic_lstm_sequence_dense240_global TE Curve Verification Pipeline collage](assets/global_wave2c/residual_harmonic_lstm_sequence_dense240_global.png)

residual_harmonic_lstm_sequence_dense360_global:

![residual_harmonic_lstm_sequence_dense360_global TE Curve Verification Pipeline collage](assets/global_wave2c/residual_harmonic_lstm_sequence_dense360_global.png)

## Collage Gallery - Forward Wave 3.1 Offset-Aware Probe Models

wave3_1_sequential_residual_offset_probe_fw:

![wave3_1_sequential_residual_offset_probe_fw TE Curve Verification Pipeline collage](assets/forward_wave3_1/wave3_1_sequential_residual_offset_probe_fw.png)

## Collage Gallery - Backward Wave 3.1 Offset-Aware Probe Models

wave3_1_sequential_residual_offset_probe_bw:

![wave3_1_sequential_residual_offset_probe_bw TE Curve Verification Pipeline collage](assets/backward_wave3_1/wave3_1_sequential_residual_offset_probe_bw.png)

## Collage Gallery - Global Wave 3.1 Offset-Aware Probe Models

wave3_1_sequential_residual_offset_probe_global:

![wave3_1_sequential_residual_offset_probe_global TE Curve Verification Pipeline collage](assets/global_wave3_1/wave3_1_sequential_residual_offset_probe_global.png)

## Collage Gallery - Forward Wave 3.2 Harmonic-Offset Probe Models

wave3_2_clean_sequential_residual_offset_fw:

![wave3_2_clean_sequential_residual_offset_fw TE Curve Verification Pipeline collage](assets/forward_wave3_2/wave3_2_clean_sequential_residual_offset_fw.png)

wave3_2_harmonic_residual_offset_fw:

![wave3_2_harmonic_residual_offset_fw TE Curve Verification Pipeline collage](assets/forward_wave3_2/wave3_2_harmonic_residual_offset_fw.png)

## Collage Gallery - Backward Wave 3.2 Harmonic-Offset Probe Models

wave3_2_clean_sequential_residual_offset_bw:

![wave3_2_clean_sequential_residual_offset_bw TE Curve Verification Pipeline collage](assets/backward_wave3_2/wave3_2_clean_sequential_residual_offset_bw.png)

wave3_2_harmonic_residual_offset_bw:

![wave3_2_harmonic_residual_offset_bw TE Curve Verification Pipeline collage](assets/backward_wave3_2/wave3_2_harmonic_residual_offset_bw.png)

## Collage Gallery - Global Wave 3.2 Harmonic-Offset Probe Models

wave3_2_clean_sequential_residual_offset_global:

![wave3_2_clean_sequential_residual_offset_global TE Curve Verification Pipeline collage](assets/global_wave3_2/wave3_2_clean_sequential_residual_offset_global.png)

wave3_2_harmonic_residual_offset_global:

![wave3_2_harmonic_residual_offset_global TE Curve Verification Pipeline collage](assets/global_wave3_2/wave3_2_harmonic_residual_offset_global.png)

## Collage Gallery - Forward Wave 3.3 Curve-Aware Training Models

wave3_3_curve_aware_pointwise_control_fw:

![wave3_3_curve_aware_pointwise_control_fw TE Curve Verification Pipeline collage](assets/forward_wave3_3/wave3_3_curve_aware_pointwise_control_fw.png)

wave3_3_raw_centered_shape_curve_aware_fw:

![wave3_3_raw_centered_shape_curve_aware_fw TE Curve Verification Pipeline collage](assets/forward_wave3_3/wave3_3_raw_centered_shape_curve_aware_fw.png)

## Collage Gallery - Forward Wave 3.3 Curve-Aware Training Models Continued

wave3_3_raw_offset_curve_aware_fw:

![wave3_3_raw_offset_curve_aware_fw TE Curve Verification Pipeline collage](assets/forward_wave3_3/wave3_3_raw_offset_curve_aware_fw.png)

wave3_3_full_curve_composite_fw:

![wave3_3_full_curve_composite_fw TE Curve Verification Pipeline collage](assets/forward_wave3_3/wave3_3_full_curve_composite_fw.png)

## Collage Gallery - Backward Wave 3.3 Curve-Aware Training Models

wave3_3_curve_aware_pointwise_control_bw:

![wave3_3_curve_aware_pointwise_control_bw TE Curve Verification Pipeline collage](assets/backward_wave3_3/wave3_3_curve_aware_pointwise_control_bw.png)

wave3_3_raw_centered_shape_curve_aware_bw:

![wave3_3_raw_centered_shape_curve_aware_bw TE Curve Verification Pipeline collage](assets/backward_wave3_3/wave3_3_raw_centered_shape_curve_aware_bw.png)

## Collage Gallery - Backward Wave 3.3 Curve-Aware Training Models Continued

wave3_3_raw_offset_curve_aware_bw:

![wave3_3_raw_offset_curve_aware_bw TE Curve Verification Pipeline collage](assets/backward_wave3_3/wave3_3_raw_offset_curve_aware_bw.png)

wave3_3_full_curve_composite_bw:

![wave3_3_full_curve_composite_bw TE Curve Verification Pipeline collage](assets/backward_wave3_3/wave3_3_full_curve_composite_bw.png)

## Collage Gallery - Global Wave 3.3 Curve-Aware Training Models

wave3_3_curve_aware_pointwise_control_global:

![wave3_3_curve_aware_pointwise_control_global TE Curve Verification Pipeline collage](assets/global_wave3_3/wave3_3_curve_aware_pointwise_control_global.png)

wave3_3_raw_centered_shape_curve_aware_global:

![wave3_3_raw_centered_shape_curve_aware_global TE Curve Verification Pipeline collage](assets/global_wave3_3/wave3_3_raw_centered_shape_curve_aware_global.png)

## Collage Gallery - Global Wave 3.3 Curve-Aware Training Models Continued

wave3_3_raw_offset_curve_aware_global:

![wave3_3_raw_offset_curve_aware_global TE Curve Verification Pipeline collage](assets/global_wave3_3/wave3_3_raw_offset_curve_aware_global.png)

wave3_3_full_curve_composite_global:

![wave3_3_full_curve_composite_global TE Curve Verification Pipeline collage](assets/global_wave3_3/wave3_3_full_curve_composite_global.png)

## Collage Gallery - Forward Wave 4.1 Robust-Loss Models

wave4_1_mae_robust_loss_fw:

![wave4_1_mae_robust_loss_fw TE Curve Verification Pipeline collage](assets/forward_wave4_1/wave4_1_mae_robust_loss_fw.png)

wave4_1_smooth_l1_robust_loss_fw:

![wave4_1_smooth_l1_robust_loss_fw TE Curve Verification Pipeline collage](assets/forward_wave4_1/wave4_1_smooth_l1_robust_loss_fw.png)

## Collage Gallery - Forward Wave 4.1 Robust-Loss Models Continued

wave4_1_log_cosh_robust_loss_fw:

![wave4_1_log_cosh_robust_loss_fw TE Curve Verification Pipeline collage](assets/forward_wave4_1/wave4_1_log_cosh_robust_loss_fw.png)

## Collage Gallery - Backward Wave 4.1 Robust-Loss Models

wave4_1_mae_robust_loss_bw:

![wave4_1_mae_robust_loss_bw TE Curve Verification Pipeline collage](assets/backward_wave4_1/wave4_1_mae_robust_loss_bw.png)

wave4_1_smooth_l1_robust_loss_bw:

![wave4_1_smooth_l1_robust_loss_bw TE Curve Verification Pipeline collage](assets/backward_wave4_1/wave4_1_smooth_l1_robust_loss_bw.png)

## Collage Gallery - Backward Wave 4.1 Robust-Loss Models Continued

wave4_1_log_cosh_robust_loss_bw:

![wave4_1_log_cosh_robust_loss_bw TE Curve Verification Pipeline collage](assets/backward_wave4_1/wave4_1_log_cosh_robust_loss_bw.png)

## Collage Gallery - Global Wave 4.1 Robust-Loss Models

wave4_1_mae_robust_loss_global:

![wave4_1_mae_robust_loss_global TE Curve Verification Pipeline collage](assets/global_wave4_1/wave4_1_mae_robust_loss_global.png)

wave4_1_smooth_l1_robust_loss_global:

![wave4_1_smooth_l1_robust_loss_global TE Curve Verification Pipeline collage](assets/global_wave4_1/wave4_1_smooth_l1_robust_loss_global.png)

## Collage Gallery - Global Wave 4.1 Robust-Loss Models Continued

wave4_1_log_cosh_robust_loss_global:

![wave4_1_log_cosh_robust_loss_global TE Curve Verification Pipeline collage](assets/global_wave4_1/wave4_1_log_cosh_robust_loss_global.png)

## Collage Gallery - Forward Wave 4.2 Quantile Probabilistic Models

wave4_2_quantile_p10_p50_p90_fw:

![wave4_2_quantile_p10_p50_p90_fw TE Curve Verification Pipeline collage](assets/forward_wave4_2/wave4_2_quantile_p10_p50_p90_fw.png)

wave4_2_gaussian_nll_fw:

![wave4_2_gaussian_nll_fw TE Curve Verification Pipeline collage](assets/forward_wave4_2/wave4_2_gaussian_nll_fw.png)

## Collage Gallery - Backward Wave 4.2 Quantile Probabilistic Models

wave4_2_quantile_p10_p50_p90_bw:

![wave4_2_quantile_p10_p50_p90_bw TE Curve Verification Pipeline collage](assets/backward_wave4_2/wave4_2_quantile_p10_p50_p90_bw.png)

wave4_2_gaussian_nll_bw:

![wave4_2_gaussian_nll_bw TE Curve Verification Pipeline collage](assets/backward_wave4_2/wave4_2_gaussian_nll_bw.png)

## Collage Gallery - Global Wave 4.2 Quantile Probabilistic Models

wave4_2_quantile_p10_p50_p90_global:

![wave4_2_quantile_p10_p50_p90_global TE Curve Verification Pipeline collage](assets/global_wave4_2/wave4_2_quantile_p10_p50_p90_global.png)

wave4_2_gaussian_nll_global:

![wave4_2_gaussian_nll_global TE Curve Verification Pipeline collage](assets/global_wave4_2/wave4_2_gaussian_nll_global.png)

## Collage Gallery - Forward Wave 4.3 Mixture Density Models Models

wave4_3_mixture_density_k2_fw:

![wave4_3_mixture_density_k2_fw TE Curve Verification Pipeline collage](assets/auto_forward_wave4_3_mixture_density_registry/wave4_3_mixture_density_k2_fw.png)

wave4_3_mixture_density_k3_fw:

![wave4_3_mixture_density_k3_fw TE Curve Verification Pipeline collage](assets/auto_forward_wave4_3_mixture_density_registry/wave4_3_mixture_density_k3_fw.png)

## Collage Gallery - Backward Wave 4.3 Mixture Density Models Models

wave4_3_mixture_density_k2_bw:

![wave4_3_mixture_density_k2_bw TE Curve Verification Pipeline collage](assets/auto_backward_wave4_3_mixture_density_registry/wave4_3_mixture_density_k2_bw.png)

wave4_3_mixture_density_k3_bw:

![wave4_3_mixture_density_k3_bw TE Curve Verification Pipeline collage](assets/auto_backward_wave4_3_mixture_density_registry/wave4_3_mixture_density_k3_bw.png)

## Collage Gallery - Global Wave 4.3 Mixture Density Models Models

wave4_3_mixture_density_k2_global:

![wave4_3_mixture_density_k2_global TE Curve Verification Pipeline collage](assets/auto_mixed_wave4_3_mixture_density_registry/wave4_3_mixture_density_k2_global.png)

wave4_3_mixture_density_k3_global:

![wave4_3_mixture_density_k3_global TE Curve Verification Pipeline collage](assets/auto_mixed_wave4_3_mixture_density_registry/wave4_3_mixture_density_k3_global.png)

## Collage Gallery - Forward Wave 4.4 Latent State Hysteresis Models Models

wave4_4_gru_latent_offset_residual_fw:

![wave4_4_gru_latent_offset_residual_fw TE Curve Verification Pipeline collage](assets/a_fw_w4_4_late_stat_hyst_reg_87cb6f7756/wave4_4_gru_latent_offset_residual_fw.png)

wave4_4_causal_tcn_latent_offset_residual_fw:

![wave4_4_causal_tcn_latent_offset_residual_fw TE Curve Verification Pipeline collage](assets/a_fw_w4_4_late_stat_hyst_reg_87cb6f7756/wave4_4_causal_tcn_latent_offset_residual_fw.png)

## Collage Gallery - Backward Wave 4.4 Latent State Hysteresis Models Models

wave4_4_gru_latent_offset_residual_bw:

![wave4_4_gru_latent_offset_residual_bw TE Curve Verification Pipeline collage](assets/a_bw_w4_4_late_stat_hyst_reg_718dadc3dc/wave4_4_gru_latent_offset_residual_bw.png)

wave4_4_causal_tcn_latent_offset_residual_bw:

![wave4_4_causal_tcn_latent_offset_residual_bw TE Curve Verification Pipeline collage](assets/a_bw_w4_4_late_stat_hyst_reg_718dadc3dc/wave4_4_causal_tcn_latent_offset_residual_bw.png)

## Collage Gallery - Global Wave 4.4 Latent State Hysteresis Models Models

wave4_4_gru_latent_offset_residual_global:

![wave4_4_gru_latent_offset_residual_global TE Curve Verification Pipeline collage](assets/a_mix_w4_4_late_stat_hyst_reg_2b5eb4e117/wave4_4_gru_latent_offset_residual_global.png)

wave4_4_causal_tcn_latent_offset_residual_global:

![wave4_4_causal_tcn_latent_offset_residual_global TE Curve Verification Pipeline collage](assets/a_mix_w4_4_late_stat_hyst_reg_2b5eb4e117/wave4_4_causal_tcn_latent_offset_residual_global.png)

## Collage Gallery - Forward Wave 5.1 Harmonic Prior Residual Models Models

wave5_1_harmonic_prior_pointwise_control_fw:

![wave5_1_harmonic_prior_pointwise_control_fw TE Curve Verification Pipeline collage](assets/a_fw_w5_1_harm_pri_res_reg_74c66fdb87/wave5_1_harmonic_prior_pointwise_control_fw.png)

wave5_1_harmonic_prior_smooth_l1_structured_fw:

![wave5_1_harmonic_prior_smooth_l1_structured_fw TE Curve Verification Pipeline collage](assets/a_fw_w5_1_harm_pri_res_reg_74c66fdb87/wave5_1_harmonic_prior_smooth_l1_structured_fw.png)

## Collage Gallery - Backward Wave 5.1 Harmonic Prior Residual Models Models

wave5_1_harmonic_prior_pointwise_control_bw:

![wave5_1_harmonic_prior_pointwise_control_bw TE Curve Verification Pipeline collage](assets/a_bw_w5_1_harm_pri_res_reg_be36d55bf2/wave5_1_harmonic_prior_pointwise_control_bw.png)

wave5_1_harmonic_prior_smooth_l1_structured_bw:

![wave5_1_harmonic_prior_smooth_l1_structured_bw TE Curve Verification Pipeline collage](assets/a_bw_w5_1_harm_pri_res_reg_be36d55bf2/wave5_1_harmonic_prior_smooth_l1_structured_bw.png)

## Collage Gallery - Global Wave 5.1 Harmonic Prior Residual Models Models

wave5_1_harmonic_prior_pointwise_control_global:

![wave5_1_harmonic_prior_pointwise_control_global TE Curve Verification Pipeline collage](assets/a_mix_w5_1_harm_pri_res_reg_4c723dd5e5/wave5_1_harmonic_prior_pointwise_control_global.png)

wave5_1_harmonic_prior_smooth_l1_structured_global:

![wave5_1_harmonic_prior_smooth_l1_structured_global TE Curve Verification Pipeline collage](assets/a_mix_w5_1_harm_pri_res_reg_4c723dd5e5/wave5_1_harmonic_prior_smooth_l1_structured_global.png)

## Collage Gallery - Forward Wave52b Offset Harmonic Guided Registry Models

wave52b_offset_centered_shape_harmonic_fw:

![wave52b_offset_centered_shape_harmonic_fw TE Curve Verification Pipeline collage](assets/a_fw_wave_offs_harm_guid_reg_bd35ddc75a/wave52b_offset_centered_shape_harmonic_fw.png)

## Collage Gallery - Backward Wave52b Offset Harmonic Guided Registry Models

wave52b_offset_centered_shape_harmonic_bw:

![wave52b_offset_centered_shape_harmonic_bw TE Curve Verification Pipeline collage](assets/a_bw_wave_offs_harm_guid_reg_ad871b9734/wave52b_offset_centered_shape_harmonic_bw.png)

## Collage Gallery - Global Wave52b Offset Harmonic Guided Registry Models

wave52b_offset_centered_shape_harmonic_global:

![wave52b_offset_centered_shape_harmonic_global TE Curve Verification Pipeline collage](assets/a_mix_wave_offs_harm_guid_reg_6e1ba80501/wave52b_offset_centered_shape_harmonic_global.png)

## Output Artifacts

- output directory: `output\validation_checks\track2_best_model_collage_report\2026-07-02-13-16-02__track2_best_model_collage_report`;
- summary YAML: `output\validation_checks\track2_best_model_collage_report\2026-07-02-13-16-02__track2_best_model_collage_report\track2_best_model_collage_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_best_model_collage_report\2026-07-02-13-16-02__track2_best_model_collage_report\track2_best_model_collage_metrics.csv`;
- report Markdown: `doc\reports\analysis\track2\best_model_collage_report\[2026-07-02]\track2_best_model_collage_report.md`.
