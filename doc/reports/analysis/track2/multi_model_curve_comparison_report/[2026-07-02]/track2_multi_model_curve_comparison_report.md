# TE Curve Verification Pipeline Multi-Model Curve Comparison Report

## Overview

This report compares representative `TE Curve Verification Pipeline` TE curves by overlaying
multiple model predictions on the same original measured curve. The
plots are intended to show whether each model tracks the local harmonic
oscillations rather than only the broad mean trend.

## Scope

- each comparison image contains four deterministic held-out test curves;
- forward comparisons are shown on forward curves only;
- backward comparisons are shown on backward curves only;
- Wave 1 screening keeps the three strongest family-best models by
  `Curve MAE [deg]` within each direction;
- `Original Curve` uses the same visual weight as predictions and a
  dark-gray color for balanced comparison.

## Metrics Summary

### Forward Reference Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_original_best_Fw` | `rcim_original` | Fw | 0.013058 | 0.013324 | 27.997 |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.029204 | 0.029350 | 62.562 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.062756 | 0.062835 | 134.143 |

### Forward Wave 1 Family Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_fw` | `wave1_current_registry` | Fw | 0.002130 | 0.002586 | 4.378 |
| `harmonic_regression_fw` | `wave1_current_registry` | Fw | 0.062598 | 0.062702 | 133.783 |
| `periodic_mlp_fw` | `wave1_current_registry` | Fw | 0.002118 | 0.002575 | 4.351 |
| `residual_harmonic_mlp_fw` | `wave1_current_registry` | Fw | 0.002234 | 0.002695 | 4.616 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.002125 | 0.002612 | 4.355 |
| `periodic_mlp_harmonic_fw` | `wave1_periodic_mlp_harmonic_campaign` | Fw | 0.038372 | 0.039223 | 82.451 |

### Backward Reference Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |

### Backward Wave 1 Family Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_bw` | `wave1_current_registry` | Bw | 0.002680 | 0.003213 | 4.759 |
| `harmonic_regression_bw` | `wave1_current_registry` | Bw | 0.008041 | 0.008675 | 16.236 |
| `periodic_mlp_bw` | `wave1_current_registry` | Bw | 0.002700 | 0.003230 | 4.793 |
| `residual_harmonic_mlp_bw` | `wave1_current_registry` | Bw | 0.002713 | 0.003255 | 4.822 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `periodic_mlp_harmonic_bw` | `wave1_periodic_mlp_harmonic_campaign` | Bw | 0.013927 | 0.014623 | 28.984 |

### Forward Wave 2.1 Temporal Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.002210 | 0.002686 | 4.557 |
| `gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.002078 | 0.002536 | 4.254 |
| `lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.002083 | 0.002538 | 4.261 |
| `periodic_temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.002004 | 0.002385 | 4.123 |
| `periodic_gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.001195 | 0.001461 | 2.559 |
| `periodic_lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.001730 | 0.002084 | 3.517 |

### Backward Wave 2.1 Temporal Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002566 | 0.003101 | 4.747 |
| `gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002440 | 0.002971 | 4.477 |
| `lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002430 | 0.002973 | 4.452 |
| `periodic_temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002482 | 0.002972 | 4.647 |
| `periodic_gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001129 | 0.001412 | 2.228 |
| `periodic_lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001405 | 0.001757 | 2.700 |

### Forward Wave 2.3 Residual Harmonic Temporal Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.045021 | 0.045184 | 96.691 |
| `residual_harmonic_gru_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.037261 | 0.038590 | 80.109 |
| `residual_harmonic_gru_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.038030 | 0.039604 | 81.958 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.042694 | 0.042917 | 91.847 |
| `residual_harmonic_lstm_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.034610 | 0.035965 | 74.503 |
| `residual_harmonic_lstm_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.033574 | 0.035202 | 72.338 |

### Backward Wave 2.3 Residual Harmonic Temporal Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.010936 | 0.011364 | 22.574 |
| `residual_harmonic_gru_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.020530 | 0.024251 | 43.464 |
| `residual_harmonic_gru_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.015162 | 0.018761 | 32.047 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.011676 | 0.012103 | 23.908 |
| `residual_harmonic_lstm_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.016792 | 0.019189 | 35.128 |
| `residual_harmonic_lstm_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.015864 | 0.020039 | 33.657 |

### Forward Wave 3.1 Offset-Aware Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_fw` | `wave3_1_offset_aware_probe_registry` | Fw | 0.036294 | 0.036467 | 77.932 |

### Backward Wave 3.1 Offset-Aware Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_bw` | `wave3_1_offset_aware_probe_registry` | Bw | 0.008945 | 0.009670 | 18.730 |

### Forward Wave 3.2 Harmonic-Offset Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_fw` | `wave3_2_harmonic_offset_probe_registry` | Fw | 0.045185 | 0.045455 | 97.083 |
| `wave3_2_harmonic_residual_offset_fw` | `wave3_2_harmonic_offset_probe_registry` | Fw | 0.059869 | 0.059969 | 127.873 |

### Backward Wave 3.2 Harmonic-Offset Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_bw` | `wave3_2_harmonic_offset_probe_registry` | Bw | 0.008376 | 0.009258 | 17.556 |
| `wave3_2_harmonic_residual_offset_bw` | `wave3_2_harmonic_offset_probe_registry` | Bw | 0.012996 | 0.013533 | 26.826 |

### Forward Wave 3.3 Curve-Aware Training Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.044577 | 0.044713 | 95.253 |
| `wave3_3_raw_centered_shape_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.037030 | 0.037237 | 79.717 |
| `wave3_3_raw_offset_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.058349 | 0.058552 | 124.991 |
| `wave3_3_full_curve_composite_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.050091 | 0.050255 | 107.778 |

### Backward Wave 3.3 Curve-Aware Training Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.009939 | 0.010532 | 20.584 |
| `wave3_3_raw_centered_shape_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.010075 | 0.010673 | 20.657 |
| `wave3_3_raw_offset_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.011255 | 0.011824 | 23.166 |
| `wave3_3_full_curve_composite_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.012620 | 0.013521 | 25.713 |

### Forward Wave 4.1 Robust-Loss Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.049061 | 0.049181 | 105.141 |
| `wave4_1_smooth_l1_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.058171 | 0.058283 | 124.441 |
| `wave4_1_log_cosh_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.054964 | 0.055089 | 117.915 |

### Backward Wave 4.1 Robust-Loss Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.014320 | 0.014747 | 30.084 |
| `wave4_1_smooth_l1_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.012012 | 0.012561 | 24.411 |
| `wave4_1_log_cosh_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.009813 | 0.010421 | 19.966 |

### Forward Wave 4.2 Quantile Probabilistic Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_fw` | `wave4_2_probabilistic_registry` | Fw | 0.050281 | 0.050425 | 107.720 |
| `wave4_2_gaussian_nll_fw` | `wave4_2_probabilistic_registry` | Fw | 0.054985 | 0.055109 | 117.675 |

### Backward Wave 4.2 Quantile Probabilistic Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_bw` | `wave4_2_probabilistic_registry` | Bw | 0.011462 | 0.011942 | 23.503 |
| `wave4_2_gaussian_nll_bw` | `wave4_2_probabilistic_registry` | Bw | 0.009739 | 0.010201 | 20.349 |

### Forward Wave 4.3 Mixture Density Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_fw` | `wave4_3_mixture_density_registry` | Fw | 0.047438 | 0.047677 | 102.227 |
| `wave4_3_mixture_density_k3_fw` | `wave4_3_mixture_density_registry` | Fw | 0.057840 | 0.057965 | 124.009 |

### Backward Wave 4.3 Mixture Density Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_bw` | `wave4_3_mixture_density_registry` | Bw | 0.008282 | 0.010642 | 16.490 |
| `wave4_3_mixture_density_k3_bw` | `wave4_3_mixture_density_registry` | Bw | 0.011511 | 0.011910 | 23.777 |

### Forward Wave 4.4 Latent State Hysteresis Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_fw` | `wave4_4_latent_state_hysteresis_registry` | Fw | 0.024419 | 0.025009 | 52.319 |
| `wave4_4_causal_tcn_latent_offset_residual_fw` | `wave4_4_latent_state_hysteresis_registry` | Fw | 0.028476 | 0.028960 | 61.107 |

### Backward Wave 4.4 Latent State Hysteresis Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_bw` | `wave4_4_latent_state_hysteresis_registry` | Bw | 0.016484 | 0.016958 | 34.591 |
| `wave4_4_causal_tcn_latent_offset_residual_bw` | `wave4_4_latent_state_hysteresis_registry` | Bw | 0.007773 | 0.008896 | 15.746 |

### Forward Wave 3 Harmonic Prior Residual Registry Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_fw` | `wave5_1_harmonic_prior_residual_registry` | Fw | 0.046994 | 0.047257 | 100.353 |
| `wave5_1_harmonic_prior_smooth_l1_structured_fw` | `wave5_1_harmonic_prior_residual_registry` | Fw | 0.047938 | 0.048105 | 102.360 |

### Backward Wave 3 Harmonic Prior Residual Registry Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_bw` | `wave5_1_harmonic_prior_residual_registry` | Bw | 0.009485 | 0.010128 | 19.928 |
| `wave5_1_harmonic_prior_smooth_l1_structured_bw` | `wave5_1_harmonic_prior_residual_registry` | Bw | 0.011508 | 0.012082 | 24.388 |

### Forward Wave52b Offset Harmonic Guided Registry Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_Fw` | `wave52b_offset_harmonic_guided_registry` | Fw | 0.001695 | 0.002045 | 3.391 |

### Backward Wave52b Offset Harmonic Guided Registry Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_Bw` | `wave52b_offset_harmonic_guided_registry` | Bw | 0.002266 | 0.002708 | 3.986 |

### Forward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.062756 | 0.062835 | 134.143 |
| `periodic_mlp_fw` | `wave1_current_registry` | Fw | 0.002118 | 0.002575 | 4.351 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.002125 | 0.002612 | 4.355 |
| `feedforward_fw` | `wave1_current_registry` | Fw | 0.002130 | 0.002586 | 4.378 |

### Backward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |
| `feedforward_bw` | `wave1_current_registry` | Bw | 0.002680 | 0.003213 | 4.759 |
| `periodic_mlp_bw` | `wave1_current_registry` | Bw | 0.002700 | 0.003230 | 4.793 |
| `residual_harmonic_mlp_bw` | `wave1_current_registry` | Bw | 0.002713 | 0.003255 | 4.822 |

### Forward Reference Tree And Wave 2.1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.029204 | 0.029350 | 62.562 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.062756 | 0.062835 | 134.143 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.002125 | 0.002612 | 4.355 |
| `temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.002210 | 0.002686 | 4.557 |
| `gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.002078 | 0.002536 | 4.254 |
| `lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.002083 | 0.002538 | 4.261 |
| `periodic_temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.002004 | 0.002385 | 4.123 |
| `periodic_gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.001195 | 0.001461 | 2.559 |
| `periodic_lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.001730 | 0.002084 | 3.517 |

### Backward Reference Tree And Wave 2.1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002566 | 0.003101 | 4.747 |
| `gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002440 | 0.002971 | 4.477 |
| `lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002430 | 0.002973 | 4.452 |
| `periodic_temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002482 | 0.002972 | 4.647 |
| `periodic_gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001129 | 0.001412 | 2.228 |
| `periodic_lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001405 | 0.001757 | 2.700 |

### Forward Reference Tree And Wave 2.3 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.029204 | 0.029350 | 62.562 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.062756 | 0.062835 | 134.143 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.002125 | 0.002612 | 4.355 |
| `residual_harmonic_gru_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.045021 | 0.045184 | 96.691 |
| `residual_harmonic_gru_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.037261 | 0.038590 | 80.109 |
| `residual_harmonic_gru_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.038030 | 0.039604 | 81.958 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.042694 | 0.042917 | 91.847 |
| `residual_harmonic_lstm_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.034610 | 0.035965 | 74.503 |
| `residual_harmonic_lstm_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.033574 | 0.035202 | 72.338 |

### Backward Reference Tree And Wave 2.3 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `residual_harmonic_gru_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.010936 | 0.011364 | 22.574 |
| `residual_harmonic_gru_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.020530 | 0.024251 | 43.464 |
| `residual_harmonic_gru_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.015162 | 0.018761 | 32.047 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.011676 | 0.012103 | 23.908 |
| `residual_harmonic_lstm_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.016792 | 0.019189 | 35.128 |
| `residual_harmonic_lstm_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.015864 | 0.020039 | 33.657 |

### Forward Reference Tree And Wave 3.1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.029204 | 0.029350 | 62.562 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.062756 | 0.062835 | 134.143 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.002125 | 0.002612 | 4.355 |
| `wave3_1_sequential_residual_offset_probe_fw` | `wave3_1_offset_aware_probe_registry` | Fw | 0.036294 | 0.036467 | 77.932 |

### Backward Reference Tree And Wave 3.1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `wave3_1_sequential_residual_offset_probe_bw` | `wave3_1_offset_aware_probe_registry` | Bw | 0.008945 | 0.009670 | 18.730 |

### Forward Reference Tree And Wave 3.3 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.029204 | 0.029350 | 62.562 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.062756 | 0.062835 | 134.143 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.002125 | 0.002612 | 4.355 |
| `wave3_3_curve_aware_pointwise_control_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.044577 | 0.044713 | 95.253 |
| `wave3_3_raw_centered_shape_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.037030 | 0.037237 | 79.717 |
| `wave3_3_raw_offset_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.058349 | 0.058552 | 124.991 |
| `wave3_3_full_curve_composite_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.050091 | 0.050255 | 107.778 |

### Backward Reference Tree And Wave 3.3 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `wave3_3_curve_aware_pointwise_control_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.009939 | 0.010532 | 20.584 |
| `wave3_3_raw_centered_shape_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.010075 | 0.010673 | 20.657 |
| `wave3_3_raw_offset_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.011255 | 0.011824 | 23.166 |
| `wave3_3_full_curve_composite_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.012620 | 0.013521 | 25.713 |

### Forward Reference Tree And Wave 4 series Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.029204 | 0.029350 | 62.562 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.062756 | 0.062835 | 134.143 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.002125 | 0.002612 | 4.355 |
| `wave4_1_mae_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.049061 | 0.049181 | 105.141 |
| `wave4_1_smooth_l1_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.058171 | 0.058283 | 124.441 |
| `wave4_1_log_cosh_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.054964 | 0.055089 | 117.915 |

### Backward Reference Tree And Wave 4 series Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `wave4_1_mae_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.014320 | 0.014747 | 30.084 |
| `wave4_1_smooth_l1_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.012012 | 0.012561 | 24.411 |
| `wave4_1_log_cosh_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.009813 | 0.010421 | 19.966 |

## Comparison Gallery - Forward Reference Model Overlay

Included models: `paper_original_best_Fw`, `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`.

![Forward Reference Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference.png)

## Comparison Gallery - Forward Wave 1 Family Model Overlay

Included models: `feedforward_fw`, `harmonic_regression_fw`, `periodic_mlp_fw`, `residual_harmonic_mlp_fw`, `tree_fw`, `periodic_mlp_harmonic_fw`.

![Forward Wave 1 Family Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave1.png)

## Comparison Gallery - Backward Reference Model Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`.

![Backward Reference Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference.png)

## Comparison Gallery - Backward Wave 1 Family Model Overlay

Included models: `feedforward_bw`, `harmonic_regression_bw`, `periodic_mlp_bw`, `residual_harmonic_mlp_bw`, `tree_bw`, `periodic_mlp_harmonic_bw`.

![Backward Wave 1 Family Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave1.png)

## Comparison Gallery - Forward Wave 2.1 Temporal Model Overlay

Included models: `temporal_convolution_fw`, `gru_sequence_fw`, `lstm_sequence_fw`, `periodic_temporal_convolution_fw`, `periodic_gru_sequence_fw`, `periodic_lstm_sequence_fw`.

![Forward Wave 2.1 Temporal Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave2.png)

## Comparison Gallery - Backward Wave 2.1 Temporal Model Overlay

Included models: `temporal_convolution_bw`, `gru_sequence_bw`, `lstm_sequence_bw`, `periodic_temporal_convolution_bw`, `periodic_gru_sequence_bw`, `periodic_lstm_sequence_bw`.

![Backward Wave 2.1 Temporal Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave2.png)

## Comparison Gallery - Forward Wave 2.3 Residual Harmonic Temporal Overlay

Included models: `residual_harmonic_gru_sequence_sparse_rcim_Fw`, `residual_harmonic_gru_sequence_dense240_Fw`, `residual_harmonic_gru_sequence_dense360_Fw`, `residual_harmonic_lstm_sequence_sparse_rcim_Fw`, `residual_harmonic_lstm_sequence_dense240_Fw`, `residual_harmonic_lstm_sequence_dense360_Fw`.

![Forward Wave 2.3 Residual Harmonic Temporal Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave2c.png)

## Comparison Gallery - Backward Wave 2.3 Residual Harmonic Temporal Overlay

Included models: `residual_harmonic_gru_sequence_sparse_rcim_Bw`, `residual_harmonic_gru_sequence_dense240_Bw`, `residual_harmonic_gru_sequence_dense360_Bw`, `residual_harmonic_lstm_sequence_sparse_rcim_Bw`, `residual_harmonic_lstm_sequence_dense240_Bw`, `residual_harmonic_lstm_sequence_dense360_Bw`.

![Backward Wave 2.3 Residual Harmonic Temporal Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave2c.png)

## Comparison Gallery - Forward Wave 3.1 Offset-Aware Probe Overlay

Included models: `wave3_1_sequential_residual_offset_probe_fw`.

![Forward Wave 3.1 Offset-Aware Probe Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave3_1.png)

## Comparison Gallery - Backward Wave 3.1 Offset-Aware Probe Overlay

Included models: `wave3_1_sequential_residual_offset_probe_bw`.

![Backward Wave 3.1 Offset-Aware Probe Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave3_1.png)

## Comparison Gallery - Forward Wave 3.2 Harmonic-Offset Probe Overlay

Included models: `wave3_2_clean_sequential_residual_offset_fw`, `wave3_2_harmonic_residual_offset_fw`.

![Forward Wave 3.2 Harmonic-Offset Probe Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave3_2.png)

## Comparison Gallery - Backward Wave 3.2 Harmonic-Offset Probe Overlay

Included models: `wave3_2_clean_sequential_residual_offset_bw`, `wave3_2_harmonic_residual_offset_bw`.

![Backward Wave 3.2 Harmonic-Offset Probe Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave3_2.png)

## Comparison Gallery - Forward Wave 3.3 Curve-Aware Training Overlay

Included models: `wave3_3_curve_aware_pointwise_control_fw`, `wave3_3_raw_centered_shape_curve_aware_fw`, `wave3_3_raw_offset_curve_aware_fw`, `wave3_3_full_curve_composite_fw`.

![Forward Wave 3.3 Curve-Aware Training Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave3_3.png)

## Comparison Gallery - Backward Wave 3.3 Curve-Aware Training Overlay

Included models: `wave3_3_curve_aware_pointwise_control_bw`, `wave3_3_raw_centered_shape_curve_aware_bw`, `wave3_3_raw_offset_curve_aware_bw`, `wave3_3_full_curve_composite_bw`.

![Backward Wave 3.3 Curve-Aware Training Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave3_3.png)

## Comparison Gallery - Forward Wave 4.1 Robust-Loss Overlay

Included models: `wave4_1_mae_robust_loss_fw`, `wave4_1_smooth_l1_robust_loss_fw`, `wave4_1_log_cosh_robust_loss_fw`.

![Forward Wave 4.1 Robust-Loss Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave4_1.png)

## Comparison Gallery - Backward Wave 4.1 Robust-Loss Overlay

Included models: `wave4_1_mae_robust_loss_bw`, `wave4_1_smooth_l1_robust_loss_bw`, `wave4_1_log_cosh_robust_loss_bw`.

![Backward Wave 4.1 Robust-Loss Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave4_1.png)

## Comparison Gallery - Forward Wave 4.2 Quantile Probabilistic Overlay

Included models: `wave4_2_quantile_p10_p50_p90_fw`, `wave4_2_gaussian_nll_fw`.

![Forward Wave 4.2 Quantile Probabilistic Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave4_2.png)

## Comparison Gallery - Backward Wave 4.2 Quantile Probabilistic Overlay

Included models: `wave4_2_quantile_p10_p50_p90_bw`, `wave4_2_gaussian_nll_bw`.

![Backward Wave 4.2 Quantile Probabilistic Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave4_2.png)

## Comparison Gallery - Forward Wave 4.3 Mixture Density Overlay

Included models: `wave4_3_mixture_density_k2_fw`, `wave4_3_mixture_density_k3_fw`.

![Forward Wave 4.3 Mixture Density Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave4_3_mixture_density.png)

## Comparison Gallery - Backward Wave 4.3 Mixture Density Overlay

Included models: `wave4_3_mixture_density_k2_bw`, `wave4_3_mixture_density_k3_bw`.

![Backward Wave 4.3 Mixture Density Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave4_3_mixture_density.png)

## Comparison Gallery - Forward Wave 4.4 Latent State Hysteresis Overlay

Included models: `wave4_4_gru_latent_offset_residual_fw`, `wave4_4_causal_tcn_latent_offset_residual_fw`.

![Forward Wave 4.4 Latent State Hysteresis Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave4_4_latent_state_hysteresis.png)

## Comparison Gallery - Backward Wave 4.4 Latent State Hysteresis Overlay

Included models: `wave4_4_gru_latent_offset_residual_bw`, `wave4_4_causal_tcn_latent_offset_residual_bw`.

![Backward Wave 4.4 Latent State Hysteresis Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave4_4_latent_state_hysteresis.png)

## Comparison Gallery - Forward Wave 3 Harmonic Prior Residual Registry Overlay

Included models: `wave5_1_harmonic_prior_pointwise_control_fw`, `wave5_1_harmonic_prior_smooth_l1_structured_fw`.

![Forward Wave 3 Harmonic Prior Residual Registry Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave5_1_harmonic_prior_residual.png)

## Comparison Gallery - Backward Wave 3 Harmonic Prior Residual Registry Overlay

Included models: `wave5_1_harmonic_prior_pointwise_control_bw`, `wave5_1_harmonic_prior_smooth_l1_structured_bw`.

![Backward Wave 3 Harmonic Prior Residual Registry Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave5_1_harmonic_prior_residual.png)

## Comparison Gallery - Forward Wave52b Offset Harmonic Guided Registry Overlay

Included models: `wave52b_offset_centered_shape_harmonic_Fw`.

![Forward Wave52b Offset Harmonic Guided Registry Overlay TE Curve Verification Pipeline comparison](assets/comparisons/a_fw_wave_offs_harm_guid_reg_bd35ddc75a.png)

## Comparison Gallery - Backward Wave52b Offset Harmonic Guided Registry Overlay

Included models: `wave52b_offset_centered_shape_harmonic_Bw`.

![Backward Wave52b Offset Harmonic Guided Registry Overlay TE Curve Verification Pipeline comparison](assets/comparisons/a_bw_wave_offs_harm_guid_reg_ad871b9734.png)

## Comparison Gallery - Forward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay

Included models: `rcim_model_bank_reproduction_best_fw`, `periodic_mlp_fw`, `tree_fw`, `feedforward_fw`.

![Forward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_track1_screened_wave1.png)

## Comparison Gallery - Backward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay

Included models: `rcim_model_bank_reproduction_best_bw`, `feedforward_bw`, `periodic_mlp_bw`, `residual_harmonic_mlp_bw`.

![Backward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_track1_screened_wave1.png)

## Comparison Gallery - Forward Reference Tree And Wave 2.1 Overlay

Included models: `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`, `tree_fw`, `temporal_convolution_fw`, `gru_sequence_fw`, `lstm_sequence_fw`, `periodic_temporal_convolution_fw`, `periodic_gru_sequence_fw`, `periodic_lstm_sequence_fw`.

![Forward Reference Tree And Wave 2.1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference_tree_wave2.png)

## Comparison Gallery - Backward Reference Tree And Wave 2.1 Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`, `tree_bw`, `temporal_convolution_bw`, `gru_sequence_bw`, `lstm_sequence_bw`, `periodic_temporal_convolution_bw`, `periodic_gru_sequence_bw`, `periodic_lstm_sequence_bw`.

![Backward Reference Tree And Wave 2.1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference_tree_wave2.png)

## Comparison Gallery - Forward Reference Tree And Wave 2.3 Overlay

Included models: `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`, `tree_fw`, `residual_harmonic_gru_sequence_sparse_rcim_Fw`, `residual_harmonic_gru_sequence_dense240_Fw`, `residual_harmonic_gru_sequence_dense360_Fw`, `residual_harmonic_lstm_sequence_sparse_rcim_Fw`, `residual_harmonic_lstm_sequence_dense240_Fw`, `residual_harmonic_lstm_sequence_dense360_Fw`.

![Forward Reference Tree And Wave 2.3 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference_tree_wave2c.png)

## Comparison Gallery - Backward Reference Tree And Wave 2.3 Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`, `tree_bw`, `residual_harmonic_gru_sequence_sparse_rcim_Bw`, `residual_harmonic_gru_sequence_dense240_Bw`, `residual_harmonic_gru_sequence_dense360_Bw`, `residual_harmonic_lstm_sequence_sparse_rcim_Bw`, `residual_harmonic_lstm_sequence_dense240_Bw`, `residual_harmonic_lstm_sequence_dense360_Bw`.

![Backward Reference Tree And Wave 2.3 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference_tree_wave2c.png)

## Comparison Gallery - Forward Reference Tree And Wave 3.1 Overlay

Included models: `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`, `tree_fw`, `wave3_1_sequential_residual_offset_probe_fw`.

![Forward Reference Tree And Wave 3.1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference_tree_wave3_1.png)

## Comparison Gallery - Backward Reference Tree And Wave 3.1 Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`, `tree_bw`, `wave3_1_sequential_residual_offset_probe_bw`.

![Backward Reference Tree And Wave 3.1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference_tree_wave3_1.png)

## Comparison Gallery - Forward Reference Tree And Wave 3.3 Overlay

Included models: `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`, `tree_fw`, `wave3_3_curve_aware_pointwise_control_fw`, `wave3_3_raw_centered_shape_curve_aware_fw`, `wave3_3_raw_offset_curve_aware_fw`, `wave3_3_full_curve_composite_fw`.

![Forward Reference Tree And Wave 3.3 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference_tree_wave3_3.png)

## Comparison Gallery - Backward Reference Tree And Wave 3.3 Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`, `tree_bw`, `wave3_3_curve_aware_pointwise_control_bw`, `wave3_3_raw_centered_shape_curve_aware_bw`, `wave3_3_raw_offset_curve_aware_bw`, `wave3_3_full_curve_composite_bw`.

![Backward Reference Tree And Wave 3.3 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference_tree_wave3_3.png)

## Comparison Gallery - Forward Reference Tree And Wave 4 series Overlay

Included models: `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`, `tree_fw`, `wave4_1_mae_robust_loss_fw`, `wave4_1_smooth_l1_robust_loss_fw`, `wave4_1_log_cosh_robust_loss_fw`.

![Forward Reference Tree And Wave 4 series Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference_tree_wave4_1.png)

## Comparison Gallery - Backward Reference Tree And Wave 4 series Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`, `tree_bw`, `wave4_1_mae_robust_loss_bw`, `wave4_1_smooth_l1_robust_loss_bw`, `wave4_1_log_cosh_robust_loss_bw`.

![Backward Reference Tree And Wave 4 series Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference_tree_wave4_1.png)

## Output Artifacts

- output directory: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-07-02-14-44-11__track2_multi_model_curve_comparison_report`;
- summary YAML: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-07-02-14-44-11__track2_multi_model_curve_comparison_report\track2_multi_model_curve_comparison_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-07-02-14-44-11__track2_multi_model_curve_comparison_report\track2_multi_model_curve_comparison_metrics.csv`;
- report Markdown: `doc\reports\analysis\track2\multi_model_curve_comparison_report\[2026-07-02]\track2_multi_model_curve_comparison_report.md`.
