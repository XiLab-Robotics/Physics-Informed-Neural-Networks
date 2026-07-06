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

### Global Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_global` | `wave1_current_registry` | global | 0.042327 | 0.042769 | 93.113 |
| `harmonic_regression_global` | `wave1_current_registry` | global | 0.042876 | 0.043100 | 94.195 |
| `periodic_mlp_global` | `wave1_current_registry` | global | 0.003447 | 0.003872 | 7.582 |
| `residual_harmonic_mlp_global` | `wave1_current_registry` | global | 0.003407 | 0.003822 | 7.486 |
| `tree_global` | `wave1_current_registry` | global | 0.040765 | 0.040951 | 90.014 |
| `periodic_mlp_harmonic_global` | `wave1_periodic_mlp_harmonic_campaign` | global | 0.003516 | 0.003810 | 7.779 |

### Global Wave 2.1 Temporal Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_global` | `wave2_temporal_entry_registry` | global | 0.003751 | 0.004183 | 8.295 |
| `gru_sequence_global` | `wave2_temporal_entry_registry` | global | 0.003591 | 0.004028 | 7.907 |
| `lstm_sequence_global` | `wave2_temporal_entry_registry` | global | 0.003480 | 0.003903 | 7.654 |
| `periodic_temporal_convolution_global` | `wave2_temporal_entry_registry` | global | 0.003506 | 0.003836 | 7.758 |
| `periodic_gru_sequence_global` | `wave2_temporal_entry_registry` | global | 0.046729 | 0.046927 | 102.931 |
| `periodic_lstm_sequence_global` | `wave2_temporal_entry_registry` | global | 0.002707 | 0.002958 | 6.120 |

### Global Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.045661 | 0.045865 | 100.419 |
| `residual_harmonic_gru_sequence_dense240_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.006660 | 0.009090 | 15.007 |
| `residual_harmonic_gru_sequence_dense360_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.008012 | 0.011416 | 18.090 |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.003368 | 0.003719 | 7.409 |
| `residual_harmonic_lstm_sequence_dense240_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.006419 | 0.008765 | 14.460 |
| `residual_harmonic_lstm_sequence_dense360_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.008810 | 0.013026 | 19.916 |

### Global Wave 3.1 Offset-Aware Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_global` | `wave3_1_offset_aware_probe_registry` | global | 0.003536 | 0.003959 | 7.790 |

### Global Wave 3.2 Harmonic-Offset Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_global` | `wave3_2_harmonic_offset_probe_registry` | global | 0.003522 | 0.003950 | 7.754 |
| `wave3_2_harmonic_residual_offset_global` | `wave3_2_harmonic_offset_probe_registry` | global | 0.003530 | 0.003833 | 7.789 |

### Global Wave 3.3 Curve-Aware Training Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_global` | `wave3_3_curve_aware_training_registry` | global | 0.003578 | 0.003900 | 7.911 |
| `wave3_3_raw_centered_shape_curve_aware_global` | `wave3_3_curve_aware_training_registry` | global | 0.003348 | 0.003682 | 7.395 |
| `wave3_3_raw_offset_curve_aware_global` | `wave3_3_curve_aware_training_registry` | global | 0.003459 | 0.003755 | 7.630 |
| `wave3_3_full_curve_composite_global` | `wave3_3_curve_aware_training_registry` | global | 0.045753 | 0.045971 | 100.665 |

### Global Wave 4.1 Robust-Loss Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_global` | `wave4_1_robust_loss_registry` | global | 0.003401 | 0.003715 | 7.504 |
| `wave4_1_smooth_l1_robust_loss_global` | `wave4_1_robust_loss_registry` | global | 0.003417 | 0.003719 | 7.539 |
| `wave4_1_log_cosh_robust_loss_global` | `wave4_1_robust_loss_registry` | global | 0.003498 | 0.003819 | 7.697 |

### Global Wave 4.2 Quantile Probabilistic Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_global` | `wave4_2_probabilistic_registry` | global | 0.003375 | 0.003689 | 7.438 |
| `wave4_2_gaussian_nll_global` | `wave4_2_probabilistic_registry` | global | 0.003009 | 0.003309 | 6.576 |

### Global Wave 4.3 Mixture Density Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_global` | `wave4_3_mixture_density_registry` | global | 0.003499 | 0.003828 | 7.727 |
| `wave4_3_mixture_density_k3_global` | `wave4_3_mixture_density_registry` | global | 0.003558 | 0.003868 | 7.861 |

### Global Wave 4.4 Latent State Hysteresis Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_global` | `wave4_4_latent_state_hysteresis_registry` | global | 0.048086 | 0.048340 | 105.632 |
| `wave4_4_causal_tcn_latent_offset_residual_global` | `wave4_4_latent_state_hysteresis_registry` | global | 0.003372 | 0.003827 | 7.398 |

### Global Wave 5.1 Harmonic Prior Residual Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_global` | `wave5_1_harmonic_prior_residual_registry` | global | 0.003442 | 0.003755 | 7.597 |
| `wave5_1_harmonic_prior_smooth_l1_structured_global` | `wave5_1_harmonic_prior_residual_registry` | global | 0.048177 | 0.048385 | 105.742 |

### Global Polished Model Development Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `polished_feedforward_global` | `polished_model_development_registry` | global | 0.047748 | 0.048071 | 104.692 |
| `polished_harmonic_regression_global` | `polished_model_development_registry` | global | 0.042960 | 0.043184 | 94.377 |
| `polished_periodic_mlp_global` | `polished_model_development_registry` | global | 0.049450 | 0.049698 | 108.355 |
| `polished_residual_harmonic_mlp_global` | `polished_model_development_registry` | global | 0.048350 | 0.048566 | 105.957 |
| `polished_tree_global` | `polished_model_development_registry` | global | 0.040765 | 0.040951 | 90.014 |
| `polished_periodic_mlp_harmonic_global` | `polished_model_development_registry` | global | 0.049322 | 0.049536 | 108.169 |
| `polished_temporal_convolution_global` | `polished_model_development_registry` | global | 0.046350 | 0.046608 | 101.934 |
| `polished_gru_sequence_global` | `polished_model_development_registry` | global | 0.046419 | 0.046684 | 101.977 |
| `polished_lstm_sequence_global` | `polished_model_development_registry` | global | 0.047313 | 0.047542 | 103.978 |
| `polished_periodic_temporal_convolution_global` | `polished_model_development_registry` | global | 0.046505 | 0.046760 | 102.052 |
| `polished_periodic_gru_sequence_global` | `polished_model_development_registry` | global | 0.046922 | 0.047140 | 103.217 |
| `polished_periodic_lstm_sequence_global` | `polished_model_development_registry` | global | 0.049236 | 0.049460 | 107.819 |
| `polished_residual_harmonic_gru_sequence_sparse_rcim_global` | `polished_model_development_registry` | global | 0.046773 | 0.046984 | 102.806 |
| `polished_residual_harmonic_gru_sequence_dense240_global` | `polished_model_development_registry` | global | 0.049174 | 0.049576 | 108.033 |
| `polished_residual_harmonic_gru_sequence_dense360_global` | `polished_model_development_registry` | global | 0.048014 | 0.049116 | 105.765 |
| `polished_residual_harmonic_lstm_sequence_sparse_rcim_global` | `polished_model_development_registry` | global | 0.047751 | 0.047952 | 104.964 |
| `polished_residual_harmonic_lstm_sequence_dense240_global` | `polished_model_development_registry` | global | 0.048546 | 0.048996 | 106.822 |
| `polished_residual_harmonic_lstm_sequence_dense360_global` | `polished_model_development_registry` | global | 0.047963 | 0.048989 | 105.603 |
| `polished_wave3_1_sequential_residual_offset_probe_global` | `polished_model_development_registry` | global | 0.048869 | 0.049139 | 107.379 |
| `polished_wave3_2_clean_sequential_residual_offset_global` | `polished_model_development_registry` | global | 0.048305 | 0.048545 | 106.249 |
| `polished_wave3_2_harmonic_residual_offset_global` | `polished_model_development_registry` | global | 0.045267 | 0.045471 | 99.688 |
| `polished_wave3_3_curve_aware_pointwise_control_global` | `polished_model_development_registry` | global | 0.045409 | 0.045607 | 99.868 |
| `polished_wave3_3_raw_centered_shape_curve_aware_global` | `polished_model_development_registry` | global | 0.045819 | 0.046013 | 100.896 |
| `polished_wave3_3_raw_offset_curve_aware_global` | `polished_model_development_registry` | global | 0.044570 | 0.044765 | 98.213 |
| `polished_wave3_3_full_curve_composite_global` | `polished_model_development_registry` | global | 0.045523 | 0.045729 | 100.120 |
| `polished_wave4_1_mae_robust_loss_global` | `polished_model_development_registry` | global | 0.044542 | 0.044734 | 98.007 |
| `polished_wave4_1_smooth_l1_robust_loss_global` | `polished_model_development_registry` | global | 0.045997 | 0.046194 | 101.141 |
| `polished_wave4_1_log_cosh_robust_loss_global` | `polished_model_development_registry` | global | 0.047088 | 0.047279 | 103.486 |
| `polished_wave4_2_quantile_p10_p50_p90_global` | `polished_model_development_registry` | global | 0.044542 | 0.044746 | 97.786 |
| `polished_wave4_2_gaussian_nll_global` | `polished_model_development_registry` | global | 0.043595 | 0.043792 | 95.875 |
| `polished_wave4_3_mixture_density_k2_global` | `polished_model_development_registry` | global | 0.043690 | 0.043875 | 96.173 |
| `polished_wave4_3_mixture_density_k3_global` | `polished_model_development_registry` | global | 0.048129 | 0.048314 | 105.661 |
| `polished_wave4_4_gru_latent_offset_residual_global` | `polished_model_development_registry` | global | 0.048329 | 0.048607 | 106.081 |
| `polished_wave4_4_causal_tcn_latent_offset_residual_global` | `polished_model_development_registry` | global | 0.048573 | 0.048822 | 106.472 |
| `polished_wave5_1_harmonic_prior_pointwise_control_global` | `polished_model_development_registry` | global | 0.045987 | 0.046189 | 100.924 |
| `polished_wave5_1_harmonic_prior_smooth_l1_structured_global` | `polished_model_development_registry` | global | 0.045839 | 0.046043 | 100.627 |

### Global Wave52b Offset Harmonic Guided Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_global` | `wave52b_offset_harmonic_guided_registry` | global | 0.042544 | 0.042751 | 93.500 |

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

## Collage Gallery - Global Wave 3.1 Offset-Aware Probe Models

wave3_1_sequential_residual_offset_probe_global:

![wave3_1_sequential_residual_offset_probe_global TE Curve Verification Pipeline collage](assets/global_wave3_1/wave3_1_sequential_residual_offset_probe_global.png)

## Collage Gallery - Global Wave 3.2 Harmonic-Offset Probe Models

wave3_2_clean_sequential_residual_offset_global:

![wave3_2_clean_sequential_residual_offset_global TE Curve Verification Pipeline collage](assets/global_wave3_2/wave3_2_clean_sequential_residual_offset_global.png)

wave3_2_harmonic_residual_offset_global:

![wave3_2_harmonic_residual_offset_global TE Curve Verification Pipeline collage](assets/global_wave3_2/wave3_2_harmonic_residual_offset_global.png)

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

## Collage Gallery - Global Wave 4.1 Robust-Loss Models

wave4_1_mae_robust_loss_global:

![wave4_1_mae_robust_loss_global TE Curve Verification Pipeline collage](assets/global_wave4_1/wave4_1_mae_robust_loss_global.png)

wave4_1_smooth_l1_robust_loss_global:

![wave4_1_smooth_l1_robust_loss_global TE Curve Verification Pipeline collage](assets/global_wave4_1/wave4_1_smooth_l1_robust_loss_global.png)

## Collage Gallery - Global Wave 4.1 Robust-Loss Models Continued

wave4_1_log_cosh_robust_loss_global:

![wave4_1_log_cosh_robust_loss_global TE Curve Verification Pipeline collage](assets/global_wave4_1/wave4_1_log_cosh_robust_loss_global.png)

## Collage Gallery - Global Wave 4.2 Quantile Probabilistic Models

wave4_2_quantile_p10_p50_p90_global:

![wave4_2_quantile_p10_p50_p90_global TE Curve Verification Pipeline collage](assets/global_wave4_2/wave4_2_quantile_p10_p50_p90_global.png)

wave4_2_gaussian_nll_global:

![wave4_2_gaussian_nll_global TE Curve Verification Pipeline collage](assets/global_wave4_2/wave4_2_gaussian_nll_global.png)

## Collage Gallery - Global Wave 4.3 Mixture Density Models Models

wave4_3_mixture_density_k2_global:

![wave4_3_mixture_density_k2_global TE Curve Verification Pipeline collage](assets/auto_mixed_wave4_3_mixture_density_registry/wave4_3_mixture_density_k2_global.png)

wave4_3_mixture_density_k3_global:

![wave4_3_mixture_density_k3_global TE Curve Verification Pipeline collage](assets/auto_mixed_wave4_3_mixture_density_registry/wave4_3_mixture_density_k3_global.png)

## Collage Gallery - Global Wave 4.4 Latent State Hysteresis Models Models

wave4_4_gru_latent_offset_residual_global:

![wave4_4_gru_latent_offset_residual_global TE Curve Verification Pipeline collage](assets/a_mix_w4_4_late_stat_hyst_reg_2b5eb4e117/wave4_4_gru_latent_offset_residual_global.png)

wave4_4_causal_tcn_latent_offset_residual_global:

![wave4_4_causal_tcn_latent_offset_residual_global TE Curve Verification Pipeline collage](assets/a_mix_w4_4_late_stat_hyst_reg_2b5eb4e117/wave4_4_causal_tcn_latent_offset_residual_global.png)

## Collage Gallery - Global Wave 5.1 Harmonic Prior Residual Models Models

wave5_1_harmonic_prior_pointwise_control_global:

![wave5_1_harmonic_prior_pointwise_control_global TE Curve Verification Pipeline collage](assets/a_mix_w5_1_harm_pri_res_reg_4c723dd5e5/wave5_1_harmonic_prior_pointwise_control_global.png)

wave5_1_harmonic_prior_smooth_l1_structured_global:

![wave5_1_harmonic_prior_smooth_l1_structured_global TE Curve Verification Pipeline collage](assets/a_mix_w5_1_harm_pri_res_reg_4c723dd5e5/wave5_1_harmonic_prior_smooth_l1_structured_global.png)

## Collage Gallery - Global Polished Model Development Registry Models

polished_feedforward_global:

![polished_feedforward_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_feedforward_global.png)

polished_harmonic_regression_global:

![polished_harmonic_regression_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_harmonic_regression_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued

polished_periodic_mlp_global:

![polished_periodic_mlp_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_periodic_mlp_global.png)

polished_residual_harmonic_mlp_global:

![polished_residual_harmonic_mlp_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_residual_harmonic_mlp_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 2

polished_tree_global:

![polished_tree_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_tree_global.png)

polished_periodic_mlp_harmonic_global:

![polished_periodic_mlp_harmonic_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_periodic_mlp_harmonic_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 3

polished_temporal_convolution_global:

![polished_temporal_convolution_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_temporal_convolution_global.png)

polished_gru_sequence_global:

![polished_gru_sequence_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_gru_sequence_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 4

polished_lstm_sequence_global:

![polished_lstm_sequence_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_lstm_sequence_global.png)

polished_periodic_temporal_convolution_global:

![polished_periodic_temporal_convolution_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_periodic_temporal_convolution_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 5

polished_periodic_gru_sequence_global:

![polished_periodic_gru_sequence_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_periodic_gru_sequence_global.png)

polished_periodic_lstm_sequence_global:

![polished_periodic_lstm_sequence_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_periodic_lstm_sequence_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 6

polished_residual_harmonic_gru_sequence_sparse_rcim_global:

![polished_residual_harmonic_gru_sequence_sparse_rcim_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_residual_harmonic_gru_sequence_sparse_rcim_global.png)

polished_residual_harmonic_gru_sequence_dense240_global:

![polished_residual_harmonic_gru_sequence_dense240_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_residual_harmonic_gru_sequence_dense240_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 7

polished_residual_harmonic_gru_sequence_dense360_global:

![polished_residual_harmonic_gru_sequence_dense360_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_residual_harmonic_gru_sequence_dense360_global.png)

polished_residual_harmonic_lstm_sequence_sparse_rcim_global:

![polished_residual_harmonic_lstm_sequence_sparse_rcim_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_residual_harmonic_lstm_sequence_sparse_rcim_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 8

polished_residual_harmonic_lstm_sequence_dense240_global:

![polished_residual_harmonic_lstm_sequence_dense240_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_residual_harmonic_lstm_sequence_dense240_global.png)

polished_residual_harmonic_lstm_sequence_dense360_global:

![polished_residual_harmonic_lstm_sequence_dense360_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_residual_harmonic_lstm_sequence_dense360_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 9

polished_wave3_1_sequential_residual_offset_probe_global:

![polished_wave3_1_sequential_residual_offset_probe_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave3_1_sequential_residual_offset_probe_global.png)

polished_wave3_2_clean_sequential_residual_offset_global:

![polished_wave3_2_clean_sequential_residual_offset_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave3_2_clean_sequential_residual_offset_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 10

polished_wave3_2_harmonic_residual_offset_global:

![polished_wave3_2_harmonic_residual_offset_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave3_2_harmonic_residual_offset_global.png)

polished_wave3_3_curve_aware_pointwise_control_global:

![polished_wave3_3_curve_aware_pointwise_control_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave3_3_curve_aware_pointwise_control_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 11

polished_wave3_3_raw_centered_shape_curve_aware_global:

![polished_wave3_3_raw_centered_shape_curve_aware_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave3_3_raw_centered_shape_curve_aware_global.png)

polished_wave3_3_raw_offset_curve_aware_global:

![polished_wave3_3_raw_offset_curve_aware_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave3_3_raw_offset_curve_aware_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 12

polished_wave3_3_full_curve_composite_global:

![polished_wave3_3_full_curve_composite_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave3_3_full_curve_composite_global.png)

polished_wave4_1_mae_robust_loss_global:

![polished_wave4_1_mae_robust_loss_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave4_1_mae_robust_loss_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 13

polished_wave4_1_smooth_l1_robust_loss_global:

![polished_wave4_1_smooth_l1_robust_loss_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave4_1_smooth_l1_robust_loss_global.png)

polished_wave4_1_log_cosh_robust_loss_global:

![polished_wave4_1_log_cosh_robust_loss_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave4_1_log_cosh_robust_loss_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 14

polished_wave4_2_quantile_p10_p50_p90_global:

![polished_wave4_2_quantile_p10_p50_p90_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave4_2_quantile_p10_p50_p90_global.png)

polished_wave4_2_gaussian_nll_global:

![polished_wave4_2_gaussian_nll_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave4_2_gaussian_nll_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 15

polished_wave4_3_mixture_density_k2_global:

![polished_wave4_3_mixture_density_k2_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave4_3_mixture_density_k2_global.png)

polished_wave4_3_mixture_density_k3_global:

![polished_wave4_3_mixture_density_k3_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave4_3_mixture_density_k3_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 16

polished_wave4_4_gru_latent_offset_residual_global:

![polished_wave4_4_gru_latent_offset_residual_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave4_4_gru_latent_offset_residual_global.png)

polished_wave4_4_causal_tcn_latent_offset_residual_global:

![polished_wave4_4_causal_tcn_latent_offset_residual_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave4_4_causal_tcn_latent_offset_residual_global.png)

## Collage Gallery - Global Polished Model Development Registry Models Continued 17

polished_wave5_1_harmonic_prior_pointwise_control_global:

![polished_wave5_1_harmonic_prior_pointwise_control_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave5_1_harmonic_prior_pointwise_control_global.png)

polished_wave5_1_harmonic_prior_smooth_l1_structured_global:

![polished_wave5_1_harmonic_prior_smooth_l1_structured_global TE Curve Verification Pipeline collage](assets/auto_mixed_polished_model_development_registry/polished_wave5_1_harmonic_prior_smooth_l1_structured_global.png)

## Collage Gallery - Global Wave52b Offset Harmonic Guided Registry Models

wave52b_offset_centered_shape_harmonic_global:

![wave52b_offset_centered_shape_harmonic_global TE Curve Verification Pipeline collage](assets/a_mix_wave_offs_harm_guid_reg_6e1ba80501/wave52b_offset_centered_shape_harmonic_global.png)

## Output Artifacts

- output directory: `output\validation_checks\track2_best_model_collage_report\2026-07-05-20-22-02__track2_best_model_collage_report`;
- summary YAML: `output\validation_checks\track2_best_model_collage_report\2026-07-05-20-22-02__track2_best_model_collage_report\track2_best_model_collage_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_best_model_collage_report\2026-07-05-20-22-02__track2_best_model_collage_report\track2_best_model_collage_metrics.csv`;
- report Markdown: `doc\reports\analysis\te_curve_verification_pipeline\02_visual_reports\dataset_surface_report\simplified_dataset\global\collage\[2026-07-04]\track2_best_model_collage_report.md`.
