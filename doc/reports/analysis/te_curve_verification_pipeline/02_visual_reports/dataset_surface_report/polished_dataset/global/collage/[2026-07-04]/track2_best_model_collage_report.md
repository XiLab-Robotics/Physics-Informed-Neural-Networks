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
| `feedforward_global` | `wave1_current_registry` | global | 0.003242 | 0.003867 | 6.502 |
| `harmonic_regression_global` | `wave1_current_registry` | global | 0.003946 | 0.004463 | 8.097 |
| `periodic_mlp_global` | `wave1_current_registry` | global | 0.020015 | 0.020667 | 42.524 |
| `residual_harmonic_mlp_global` | `wave1_current_registry` | global | 0.021834 | 0.022135 | 45.955 |
| `tree_global` | `wave1_current_registry` | global | 0.002431 | 0.002939 | 4.635 |
| `periodic_mlp_harmonic_global` | `wave1_periodic_mlp_harmonic_campaign` | global | 0.019249 | 0.019792 | 40.938 |

### Global Wave 2.1 Temporal Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_global` | `wave2_temporal_entry_registry` | global | 0.015819 | 0.016489 | 33.689 |
| `gru_sequence_global` | `wave2_temporal_entry_registry` | global | 0.019324 | 0.020436 | 40.840 |
| `lstm_sequence_global` | `wave2_temporal_entry_registry` | global | 0.015469 | 0.016606 | 32.362 |
| `periodic_temporal_convolution_global` | `wave2_temporal_entry_registry` | global | 0.019806 | 0.020351 | 42.088 |
| `periodic_gru_sequence_global` | `wave2_temporal_entry_registry` | global | 0.001368 | 0.001689 | 2.783 |
| `periodic_lstm_sequence_global` | `wave2_temporal_entry_registry` | global | 0.021008 | 0.021669 | 44.372 |

### Global Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.002125 | 0.002564 | 4.063 |
| `residual_harmonic_gru_sequence_dense240_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.023609 | 0.025357 | 50.450 |
| `residual_harmonic_gru_sequence_dense360_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.025279 | 0.027755 | 54.017 |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.020851 | 0.021154 | 44.178 |
| `residual_harmonic_lstm_sequence_dense240_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.025395 | 0.026906 | 54.290 |
| `residual_harmonic_lstm_sequence_dense360_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.022205 | 0.025320 | 47.717 |

### Global Wave 3.1 Offset-Aware Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_global` | `wave3_1_offset_aware_probe_registry` | global | 0.010335 | 0.011447 | 21.780 |

### Global Wave 3.2 Harmonic-Offset Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_global` | `wave3_2_harmonic_offset_probe_registry` | global | 0.010931 | 0.011645 | 23.153 |
| `wave3_2_harmonic_residual_offset_global` | `wave3_2_harmonic_offset_probe_registry` | global | 0.024458 | 0.024780 | 52.055 |

### Global Wave 3.3 Curve-Aware Training Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_global` | `wave3_3_curve_aware_training_registry` | global | 0.014650 | 0.015045 | 31.212 |
| `wave3_3_raw_centered_shape_curve_aware_global` | `wave3_3_curve_aware_training_registry` | global | 0.009702 | 0.010170 | 20.917 |
| `wave3_3_raw_offset_curve_aware_global` | `wave3_3_curve_aware_training_registry` | global | 0.009712 | 0.010143 | 20.524 |
| `wave3_3_full_curve_composite_global` | `wave3_3_curve_aware_training_registry` | global | 0.002021 | 0.002448 | 3.824 |

### Global Wave 4.1 Robust-Loss Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_global` | `wave4_1_robust_loss_registry` | global | 0.009839 | 0.010272 | 20.969 |
| `wave4_1_smooth_l1_robust_loss_global` | `wave4_1_robust_loss_registry` | global | 0.024904 | 0.025183 | 52.984 |
| `wave4_1_log_cosh_robust_loss_global` | `wave4_1_robust_loss_registry` | global | 0.008761 | 0.009218 | 18.772 |

### Global Wave 4.2 Quantile Probabilistic Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_global` | `wave4_2_probabilistic_registry` | global | 0.023037 | 0.023327 | 48.983 |
| `wave4_2_gaussian_nll_global` | `wave4_2_probabilistic_registry` | global | 0.013087 | 0.013458 | 27.845 |

### Global Wave 4.3 Mixture Density Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_global` | `wave4_3_mixture_density_registry` | global | 0.012978 | 0.013430 | 27.105 |
| `wave4_3_mixture_density_k3_global` | `wave4_3_mixture_density_registry` | global | 0.012184 | 0.012600 | 25.767 |

### Global Wave 4.4 Latent State Hysteresis Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_global` | `wave4_4_latent_state_hysteresis_registry` | global | 0.002346 | 0.002846 | 4.572 |
| `wave4_4_causal_tcn_latent_offset_residual_global` | `wave4_4_latent_state_hysteresis_registry` | global | 0.021583 | 0.022991 | 46.360 |

### Global Wave 5.1 Harmonic Prior Residual Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_global` | `wave5_1_harmonic_prior_residual_registry` | global | 0.007113 | 0.007629 | 14.995 |
| `wave5_1_harmonic_prior_smooth_l1_structured_global` | `wave5_1_harmonic_prior_residual_registry` | global | 0.002163 | 0.002571 | 4.046 |

### Global Polished Model Development Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `polished_feedforward_global` | `polished_model_development_registry` | global | 0.002404 | 0.002907 | 4.575 |
| `polished_harmonic_regression_global` | `polished_model_development_registry` | global | 0.003979 | 0.004503 | 8.163 |
| `polished_periodic_mlp_global` | `polished_model_development_registry` | global | 0.002421 | 0.002922 | 4.606 |
| `polished_residual_harmonic_mlp_global` | `polished_model_development_registry` | global | 0.002411 | 0.002910 | 4.592 |
| `polished_tree_global` | `polished_model_development_registry` | global | 0.002431 | 0.002939 | 4.635 |
| `polished_periodic_mlp_harmonic_global` | `polished_model_development_registry` | global | 0.002054 | 0.002457 | 3.832 |
| `polished_temporal_convolution_global` | `polished_model_development_registry` | global | 0.002398 | 0.002909 | 4.702 |
| `polished_gru_sequence_global` | `polished_model_development_registry` | global | 0.002235 | 0.002722 | 4.313 |
| `polished_lstm_sequence_global` | `polished_model_development_registry` | global | 0.002266 | 0.002753 | 4.390 |
| `polished_periodic_temporal_convolution_global` | `polished_model_development_registry` | global | 0.002318 | 0.002743 | 4.527 |
| `polished_periodic_gru_sequence_global` | `polished_model_development_registry` | global | 0.001279 | 0.001568 | 2.636 |
| `polished_periodic_lstm_sequence_global` | `polished_model_development_registry` | global | 0.001303 | 0.001600 | 2.642 |
| `polished_residual_harmonic_gru_sequence_sparse_rcim_global` | `polished_model_development_registry` | global | 0.002107 | 0.002548 | 4.033 |
| `polished_residual_harmonic_gru_sequence_dense240_global` | `polished_model_development_registry` | global | 0.003121 | 0.003993 | 6.395 |
| `polished_residual_harmonic_gru_sequence_dense360_global` | `polished_model_development_registry` | global | 0.004631 | 0.006987 | 9.827 |
| `polished_residual_harmonic_lstm_sequence_sparse_rcim_global` | `polished_model_development_registry` | global | 0.002069 | 0.002515 | 3.949 |
| `polished_residual_harmonic_lstm_sequence_dense240_global` | `polished_model_development_registry` | global | 0.003329 | 0.004300 | 6.862 |
| `polished_residual_harmonic_lstm_sequence_dense360_global` | `polished_model_development_registry` | global | 0.004618 | 0.006711 | 9.753 |
| `polished_wave3_1_sequential_residual_offset_probe_global` | `polished_model_development_registry` | global | 0.002252 | 0.002737 | 4.348 |
| `polished_wave3_2_clean_sequential_residual_offset_global` | `polished_model_development_registry` | global | 0.002276 | 0.002760 | 4.397 |
| `polished_wave3_2_harmonic_residual_offset_global` | `polished_model_development_registry` | global | 0.001936 | 0.002349 | 3.656 |
| `polished_wave3_3_curve_aware_pointwise_control_global` | `polished_model_development_registry` | global | 0.001967 | 0.002372 | 3.719 |
| `polished_wave3_3_raw_centered_shape_curve_aware_global` | `polished_model_development_registry` | global | 0.001977 | 0.002372 | 3.710 |
| `polished_wave3_3_raw_offset_curve_aware_global` | `polished_model_development_registry` | global | 0.002009 | 0.002428 | 3.824 |
| `polished_wave3_3_full_curve_composite_global` | `polished_model_development_registry` | global | 0.002028 | 0.002464 | 3.869 |
| `polished_wave4_1_mae_robust_loss_global` | `polished_model_development_registry` | global | 0.001907 | 0.002311 | 3.588 |
| `polished_wave4_1_smooth_l1_robust_loss_global` | `polished_model_development_registry` | global | 0.002018 | 0.002417 | 3.821 |
| `polished_wave4_1_log_cosh_robust_loss_global` | `polished_model_development_registry` | global | 0.001923 | 0.002317 | 3.610 |
| `polished_wave4_2_quantile_p10_p50_p90_global` | `polished_model_development_registry` | global | 0.001908 | 0.002311 | 3.589 |
| `polished_wave4_2_gaussian_nll_global` | `polished_model_development_registry` | global | 0.002006 | 0.002417 | 3.776 |
| `polished_wave4_3_mixture_density_k2_global` | `polished_model_development_registry` | global | 0.001758 | 0.002131 | 3.354 |
| `polished_wave4_3_mixture_density_k3_global` | `polished_model_development_registry` | global | 0.001585 | 0.001945 | 3.116 |
| `polished_wave4_4_gru_latent_offset_residual_global` | `polished_model_development_registry` | global | 0.002306 | 0.002807 | 4.470 |
| `polished_wave4_4_causal_tcn_latent_offset_residual_global` | `polished_model_development_registry` | global | 0.002321 | 0.002831 | 4.493 |
| `polished_wave5_1_harmonic_prior_pointwise_control_global` | `polished_model_development_registry` | global | 0.002153 | 0.002556 | 4.001 |
| `polished_wave5_1_harmonic_prior_smooth_l1_structured_global` | `polished_model_development_registry` | global | 0.002121 | 0.002522 | 3.936 |

### Global Wave52b Offset Harmonic Guided Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_global` | `wave52b_offset_harmonic_guided_registry` | global | 0.002221 | 0.002629 | 4.184 |

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

- output directory: `output\validation_checks\track2_best_model_collage_report\2026-07-04-18-31-59__track2_best_model_collage_report`;
- summary YAML: `output\validation_checks\track2_best_model_collage_report\2026-07-04-18-31-59__track2_best_model_collage_report\track2_best_model_collage_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_best_model_collage_report\2026-07-04-18-31-59__track2_best_model_collage_report\track2_best_model_collage_metrics.csv`;
- report Markdown: `doc\reports\analysis\te_curve_verification_pipeline\02_visual_reports\dataset_surface_report\polished_dataset\global\collage\[2026-07-04]\track2_best_model_collage_report.md`.
