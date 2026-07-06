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

### Backward Reference Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `track1_best_bw` | `rcim_track1` | Bw | 0.006633 | 0.007119 | 13.713 |

### Backward Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_bw` | `wave1_current_registry` | Bw | 0.002655 | 0.003193 | 4.708 |
| `harmonic_regression_bw` | `wave1_current_registry` | Bw | 0.008041 | 0.008675 | 16.236 |
| `periodic_mlp_bw` | `wave1_current_registry` | Bw | 0.002769 | 0.003282 | 4.910 |
| `residual_harmonic_mlp_bw` | `wave1_current_registry` | Bw | 0.002713 | 0.003255 | 4.822 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `periodic_mlp_harmonic_bw` | `wave1_periodic_mlp_harmonic_campaign` | Bw | 0.013927 | 0.014623 | 28.984 |

### Backward Wave 2.1 Temporal Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002530 | 0.003060 | 4.674 |
| `gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002425 | 0.002937 | 4.438 |
| `lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002430 | 0.002973 | 4.452 |
| `periodic_temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002326 | 0.002803 | 4.277 |
| `periodic_gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001129 | 0.001412 | 2.228 |
| `periodic_lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001290 | 0.001613 | 2.539 |

### Backward Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.010936 | 0.011364 | 22.574 |
| `residual_harmonic_gru_sequence_dense240_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.020530 | 0.024251 | 43.464 |
| `residual_harmonic_gru_sequence_dense360_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.015162 | 0.018761 | 32.047 |
| `residual_harmonic_lstm_sequence_sparse_rcim_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.011676 | 0.012103 | 23.908 |
| `residual_harmonic_lstm_sequence_dense240_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.016792 | 0.019189 | 35.128 |
| `residual_harmonic_lstm_sequence_dense360_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.015864 | 0.020039 | 33.657 |

### Backward Wave 3.1 Offset-Aware Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_bw` | `wave3_1_offset_aware_probe_registry` | Bw | 0.008945 | 0.009670 | 18.730 |

### Backward Wave 3.2 Harmonic-Offset Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_bw` | `wave3_2_harmonic_offset_probe_registry` | Bw | 0.008376 | 0.009258 | 17.556 |
| `wave3_2_harmonic_residual_offset_bw` | `wave3_2_harmonic_offset_probe_registry` | Bw | 0.012996 | 0.013533 | 26.826 |

### Backward Wave 3.3 Curve-Aware Training Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.009939 | 0.010532 | 20.584 |
| `wave3_3_raw_centered_shape_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.010075 | 0.010673 | 20.657 |
| `wave3_3_raw_offset_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.011255 | 0.011824 | 23.166 |
| `wave3_3_full_curve_composite_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.012620 | 0.013521 | 25.713 |

### Backward Wave 4.1 Robust-Loss Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.014320 | 0.014747 | 30.084 |
| `wave4_1_smooth_l1_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.012012 | 0.012561 | 24.411 |
| `wave4_1_log_cosh_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.009813 | 0.010421 | 19.966 |

### Backward Wave 4.2 Quantile Probabilistic Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_bw` | `wave4_2_probabilistic_registry` | Bw | 0.011462 | 0.011942 | 23.503 |
| `wave4_2_gaussian_nll_bw` | `wave4_2_probabilistic_registry` | Bw | 0.009739 | 0.010201 | 20.349 |

### Backward Wave 4.3 Mixture Density Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_bw` | `wave4_3_mixture_density_registry` | Bw | 0.008282 | 0.010642 | 16.490 |
| `wave4_3_mixture_density_k3_bw` | `wave4_3_mixture_density_registry` | Bw | 0.011511 | 0.011910 | 23.777 |

### Backward Wave 4.4 Latent State Hysteresis Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_bw` | `wave4_4_latent_state_hysteresis_registry` | Bw | 0.016484 | 0.016958 | 34.591 |
| `wave4_4_causal_tcn_latent_offset_residual_bw` | `wave4_4_latent_state_hysteresis_registry` | Bw | 0.007773 | 0.008896 | 15.746 |

### Backward Wave 5.1 Harmonic Prior Residual Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_bw` | `wave5_1_harmonic_prior_residual_registry` | Bw | 0.009485 | 0.010128 | 19.928 |
| `wave5_1_harmonic_prior_smooth_l1_structured_bw` | `wave5_1_harmonic_prior_residual_registry` | Bw | 0.011508 | 0.012082 | 24.388 |

### Backward Polished Model Development Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `polished_feedforward_bw` | `polished_model_development_registry` | Bw | 0.002655 | 0.003193 | 4.708 |
| `polished_harmonic_regression_bw` | `polished_model_development_registry` | Bw | 0.008041 | 0.008675 | 16.236 |
| `polished_periodic_mlp_bw` | `polished_model_development_registry` | Bw | 0.002769 | 0.003282 | 4.910 |
| `polished_residual_harmonic_mlp_bw` | `polished_model_development_registry` | Bw | 0.002713 | 0.003255 | 4.822 |
| `polished_tree_bw` | `polished_model_development_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `polished_periodic_mlp_harmonic_bw` | `polished_model_development_registry` | Bw | 0.002396 | 0.002823 | 4.137 |
| `polished_temporal_convolution_bw` | `polished_model_development_registry` | Bw | 0.002530 | 0.003060 | 4.674 |
| `polished_gru_sequence_bw` | `polished_model_development_registry` | Bw | 0.002425 | 0.002937 | 4.438 |
| `polished_lstm_sequence_bw` | `polished_model_development_registry` | Bw | 0.002430 | 0.002973 | 4.452 |
| `polished_periodic_temporal_convolution_bw` | `polished_model_development_registry` | Bw | 0.002326 | 0.002803 | 4.277 |
| `polished_periodic_gru_sequence_bw` | `polished_model_development_registry` | Bw | 0.001129 | 0.001412 | 2.228 |
| `polished_periodic_lstm_sequence_bw` | `polished_model_development_registry` | Bw | 0.001290 | 0.001613 | 2.539 |
| `polished_residual_harmonic_gru_sequence_sparse_rcim_bw` | `polished_model_development_registry` | Bw | 0.002331 | 0.002829 | 4.234 |
| `polished_residual_harmonic_gru_sequence_dense240_bw` | `polished_model_development_registry` | Bw | 0.003416 | 0.004405 | 6.794 |
| `polished_residual_harmonic_gru_sequence_dense360_bw` | `polished_model_development_registry` | Bw | 0.005031 | 0.008128 | 10.446 |
| `polished_residual_harmonic_lstm_sequence_sparse_rcim_bw` | `polished_model_development_registry` | Bw | 0.002343 | 0.002825 | 4.242 |
| `polished_residual_harmonic_lstm_sequence_dense240_bw` | `polished_model_development_registry` | Bw | 0.003569 | 0.004639 | 7.137 |
| `polished_residual_harmonic_lstm_sequence_dense360_bw` | `polished_model_development_registry` | Bw | 0.005029 | 0.007977 | 10.455 |
| `polished_wave3_1_sequential_residual_offset_probe_bw` | `polished_model_development_registry` | Bw | 0.002411 | 0.002947 | 4.412 |
| `polished_wave3_2_clean_sequential_residual_offset_bw` | `polished_model_development_registry` | Bw | 0.002439 | 0.002959 | 4.469 |
| `polished_wave3_2_harmonic_residual_offset_bw` | `polished_model_development_registry` | Bw | 0.002142 | 0.002591 | 3.805 |
| `polished_wave3_3_curve_aware_pointwise_control_bw` | `polished_model_development_registry` | Bw | 0.002172 | 0.002638 | 3.909 |
| `polished_wave3_3_raw_centered_shape_curve_aware_bw` | `polished_model_development_registry` | Bw | 0.002133 | 0.002578 | 3.790 |
| `polished_wave3_3_raw_offset_curve_aware_bw` | `polished_model_development_registry` | Bw | 0.002139 | 0.002591 | 3.806 |
| `polished_wave3_3_full_curve_composite_bw` | `polished_model_development_registry` | Bw | 0.002333 | 0.002822 | 4.250 |
| `polished_wave4_1_mae_robust_loss_bw` | `polished_model_development_registry` | Bw | 0.002133 | 0.002572 | 3.754 |
| `polished_wave4_1_smooth_l1_robust_loss_bw` | `polished_model_development_registry` | Bw | 0.002236 | 0.002696 | 4.026 |
| `polished_wave4_1_log_cosh_robust_loss_bw` | `polished_model_development_registry` | Bw | 0.002131 | 0.002576 | 3.787 |
| `polished_wave4_2_quantile_p10_p50_p90_bw` | `polished_model_development_registry` | Bw | 0.002133 | 0.002585 | 3.778 |
| `polished_wave4_2_gaussian_nll_bw` | `polished_model_development_registry` | Bw | 0.002133 | 0.002582 | 3.758 |
| `polished_wave4_3_mixture_density_k2_bw` | `polished_model_development_registry` | Bw | 0.001995 | 0.002403 | 3.526 |
| `polished_wave4_3_mixture_density_k3_bw` | `polished_model_development_registry` | Bw | 0.001930 | 0.002341 | 3.405 |
| `polished_wave4_4_gru_latent_offset_residual_bw` | `polished_model_development_registry` | Bw | 0.002455 | 0.002998 | 4.512 |
| `polished_wave4_4_causal_tcn_latent_offset_residual_bw` | `polished_model_development_registry` | Bw | 0.002485 | 0.003022 | 4.545 |
| `polished_wave5_1_harmonic_prior_pointwise_control_bw` | `polished_model_development_registry` | Bw | 0.002418 | 0.002843 | 4.202 |
| `polished_wave5_1_harmonic_prior_smooth_l1_structured_bw` | `polished_model_development_registry` | Bw | 0.002528 | 0.002976 | 4.377 |

### Backward Wave52b Offset Harmonic Guided Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_bw` | `wave52b_offset_harmonic_guided_registry` | Bw | 0.002266 | 0.002708 | 3.986 |

## Collage Gallery - Backward Reference Best Models

paper_retuned_best_bw:

![paper_retuned_best_bw TE Curve Verification Pipeline collage](assets/backward_reference/paper_retuned_best_bw.png)

track1_best_bw:

![track1_best_bw TE Curve Verification Pipeline collage](assets/backward_reference/track1_best_bw.png)

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

## Collage Gallery - Backward Wave 3.1 Offset-Aware Probe Models

wave3_1_sequential_residual_offset_probe_bw:

![wave3_1_sequential_residual_offset_probe_bw TE Curve Verification Pipeline collage](assets/backward_wave3_1/wave3_1_sequential_residual_offset_probe_bw.png)

## Collage Gallery - Backward Wave 3.2 Harmonic-Offset Probe Models

wave3_2_clean_sequential_residual_offset_bw:

![wave3_2_clean_sequential_residual_offset_bw TE Curve Verification Pipeline collage](assets/backward_wave3_2/wave3_2_clean_sequential_residual_offset_bw.png)

wave3_2_harmonic_residual_offset_bw:

![wave3_2_harmonic_residual_offset_bw TE Curve Verification Pipeline collage](assets/backward_wave3_2/wave3_2_harmonic_residual_offset_bw.png)

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

## Collage Gallery - Backward Wave 4.1 Robust-Loss Models

wave4_1_mae_robust_loss_bw:

![wave4_1_mae_robust_loss_bw TE Curve Verification Pipeline collage](assets/backward_wave4_1/wave4_1_mae_robust_loss_bw.png)

wave4_1_smooth_l1_robust_loss_bw:

![wave4_1_smooth_l1_robust_loss_bw TE Curve Verification Pipeline collage](assets/backward_wave4_1/wave4_1_smooth_l1_robust_loss_bw.png)

## Collage Gallery - Backward Wave 4.1 Robust-Loss Models Continued

wave4_1_log_cosh_robust_loss_bw:

![wave4_1_log_cosh_robust_loss_bw TE Curve Verification Pipeline collage](assets/backward_wave4_1/wave4_1_log_cosh_robust_loss_bw.png)

## Collage Gallery - Backward Wave 4.2 Quantile Probabilistic Models

wave4_2_quantile_p10_p50_p90_bw:

![wave4_2_quantile_p10_p50_p90_bw TE Curve Verification Pipeline collage](assets/backward_wave4_2/wave4_2_quantile_p10_p50_p90_bw.png)

wave4_2_gaussian_nll_bw:

![wave4_2_gaussian_nll_bw TE Curve Verification Pipeline collage](assets/backward_wave4_2/wave4_2_gaussian_nll_bw.png)

## Collage Gallery - Backward Wave 4.3 Mixture Density Models Models

wave4_3_mixture_density_k2_bw:

![wave4_3_mixture_density_k2_bw TE Curve Verification Pipeline collage](assets/auto_backward_wave4_3_mixture_density_registry/wave4_3_mixture_density_k2_bw.png)

wave4_3_mixture_density_k3_bw:

![wave4_3_mixture_density_k3_bw TE Curve Verification Pipeline collage](assets/auto_backward_wave4_3_mixture_density_registry/wave4_3_mixture_density_k3_bw.png)

## Collage Gallery - Backward Wave 4.4 Latent State Hysteresis Models Models

wave4_4_gru_latent_offset_residual_bw:

![wave4_4_gru_latent_offset_residual_bw TE Curve Verification Pipeline collage](assets/a_bw_w4_4_late_stat_hyst_reg_718dadc3dc/wave4_4_gru_latent_offset_residual_bw.png)

wave4_4_causal_tcn_latent_offset_residual_bw:

![wave4_4_causal_tcn_latent_offset_residual_bw TE Curve Verification Pipeline collage](assets/a_bw_w4_4_late_stat_hyst_reg_718dadc3dc/wave4_4_causal_tcn_latent_offset_residual_bw.png)

## Collage Gallery - Backward Wave 5.1 Harmonic Prior Residual Models Models

wave5_1_harmonic_prior_pointwise_control_bw:

![wave5_1_harmonic_prior_pointwise_control_bw TE Curve Verification Pipeline collage](assets/a_bw_w5_1_harm_pri_res_reg_be36d55bf2/wave5_1_harmonic_prior_pointwise_control_bw.png)

wave5_1_harmonic_prior_smooth_l1_structured_bw:

![wave5_1_harmonic_prior_smooth_l1_structured_bw TE Curve Verification Pipeline collage](assets/a_bw_w5_1_harm_pri_res_reg_be36d55bf2/wave5_1_harmonic_prior_smooth_l1_structured_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models

polished_feedforward_bw:

![polished_feedforward_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_feedforward_bw.png)

polished_harmonic_regression_bw:

![polished_harmonic_regression_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_harmonic_regression_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued

polished_periodic_mlp_bw:

![polished_periodic_mlp_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_periodic_mlp_bw.png)

polished_residual_harmonic_mlp_bw:

![polished_residual_harmonic_mlp_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_residual_harmonic_mlp_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 2

polished_tree_bw:

![polished_tree_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_tree_bw.png)

polished_periodic_mlp_harmonic_bw:

![polished_periodic_mlp_harmonic_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_periodic_mlp_harmonic_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 3

polished_temporal_convolution_bw:

![polished_temporal_convolution_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_temporal_convolution_bw.png)

polished_gru_sequence_bw:

![polished_gru_sequence_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_gru_sequence_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 4

polished_lstm_sequence_bw:

![polished_lstm_sequence_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_lstm_sequence_bw.png)

polished_periodic_temporal_convolution_bw:

![polished_periodic_temporal_convolution_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_periodic_temporal_convolution_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 5

polished_periodic_gru_sequence_bw:

![polished_periodic_gru_sequence_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_periodic_gru_sequence_bw.png)

polished_periodic_lstm_sequence_bw:

![polished_periodic_lstm_sequence_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_periodic_lstm_sequence_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 6

polished_residual_harmonic_gru_sequence_sparse_rcim_bw:

![polished_residual_harmonic_gru_sequence_sparse_rcim_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_residual_harmonic_gru_sequence_sparse_rcim_bw.png)

polished_residual_harmonic_gru_sequence_dense240_bw:

![polished_residual_harmonic_gru_sequence_dense240_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_residual_harmonic_gru_sequence_dense240_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 7

polished_residual_harmonic_gru_sequence_dense360_bw:

![polished_residual_harmonic_gru_sequence_dense360_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_residual_harmonic_gru_sequence_dense360_bw.png)

polished_residual_harmonic_lstm_sequence_sparse_rcim_bw:

![polished_residual_harmonic_lstm_sequence_sparse_rcim_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_residual_harmonic_lstm_sequence_sparse_rcim_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 8

polished_residual_harmonic_lstm_sequence_dense240_bw:

![polished_residual_harmonic_lstm_sequence_dense240_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_residual_harmonic_lstm_sequence_dense240_bw.png)

polished_residual_harmonic_lstm_sequence_dense360_bw:

![polished_residual_harmonic_lstm_sequence_dense360_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_residual_harmonic_lstm_sequence_dense360_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 9

polished_wave3_1_sequential_residual_offset_probe_bw:

![polished_wave3_1_sequential_residual_offset_probe_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave3_1_sequential_residual_offset_probe_bw.png)

polished_wave3_2_clean_sequential_residual_offset_bw:

![polished_wave3_2_clean_sequential_residual_offset_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave3_2_clean_sequential_residual_offset_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 10

polished_wave3_2_harmonic_residual_offset_bw:

![polished_wave3_2_harmonic_residual_offset_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave3_2_harmonic_residual_offset_bw.png)

polished_wave3_3_curve_aware_pointwise_control_bw:

![polished_wave3_3_curve_aware_pointwise_control_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave3_3_curve_aware_pointwise_control_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 11

polished_wave3_3_raw_centered_shape_curve_aware_bw:

![polished_wave3_3_raw_centered_shape_curve_aware_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave3_3_raw_centered_shape_curve_aware_bw.png)

polished_wave3_3_raw_offset_curve_aware_bw:

![polished_wave3_3_raw_offset_curve_aware_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave3_3_raw_offset_curve_aware_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 12

polished_wave3_3_full_curve_composite_bw:

![polished_wave3_3_full_curve_composite_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave3_3_full_curve_composite_bw.png)

polished_wave4_1_mae_robust_loss_bw:

![polished_wave4_1_mae_robust_loss_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave4_1_mae_robust_loss_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 13

polished_wave4_1_smooth_l1_robust_loss_bw:

![polished_wave4_1_smooth_l1_robust_loss_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave4_1_smooth_l1_robust_loss_bw.png)

polished_wave4_1_log_cosh_robust_loss_bw:

![polished_wave4_1_log_cosh_robust_loss_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave4_1_log_cosh_robust_loss_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 14

polished_wave4_2_quantile_p10_p50_p90_bw:

![polished_wave4_2_quantile_p10_p50_p90_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave4_2_quantile_p10_p50_p90_bw.png)

polished_wave4_2_gaussian_nll_bw:

![polished_wave4_2_gaussian_nll_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave4_2_gaussian_nll_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 15

polished_wave4_3_mixture_density_k2_bw:

![polished_wave4_3_mixture_density_k2_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave4_3_mixture_density_k2_bw.png)

polished_wave4_3_mixture_density_k3_bw:

![polished_wave4_3_mixture_density_k3_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave4_3_mixture_density_k3_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 16

polished_wave4_4_gru_latent_offset_residual_bw:

![polished_wave4_4_gru_latent_offset_residual_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave4_4_gru_latent_offset_residual_bw.png)

polished_wave4_4_causal_tcn_latent_offset_residual_bw:

![polished_wave4_4_causal_tcn_latent_offset_residual_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave4_4_causal_tcn_latent_offset_residual_bw.png)

## Collage Gallery - Backward Polished Model Development Registry Models Continued 17

polished_wave5_1_harmonic_prior_pointwise_control_bw:

![polished_wave5_1_harmonic_prior_pointwise_control_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave5_1_harmonic_prior_pointwise_control_bw.png)

polished_wave5_1_harmonic_prior_smooth_l1_structured_bw:

![polished_wave5_1_harmonic_prior_smooth_l1_structured_bw TE Curve Verification Pipeline collage](assets/a_bw_poli_mode_deve_reg_c54d0bb56e/polished_wave5_1_harmonic_prior_smooth_l1_structured_bw.png)

## Collage Gallery - Backward Wave52b Offset Harmonic Guided Registry Models

wave52b_offset_centered_shape_harmonic_bw:

![wave52b_offset_centered_shape_harmonic_bw TE Curve Verification Pipeline collage](assets/a_bw_wave_offs_harm_guid_reg_ad871b9734/wave52b_offset_centered_shape_harmonic_bw.png)

## Output Artifacts

- output directory: `output\validation_checks\track2_best_model_collage_report\2026-07-04-14-13-56__track2_best_model_collage_report`;
- summary YAML: `output\validation_checks\track2_best_model_collage_report\2026-07-04-14-13-56__track2_best_model_collage_report\track2_best_model_collage_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_best_model_collage_report\2026-07-04-14-13-56__track2_best_model_collage_report\track2_best_model_collage_metrics.csv`;
- report Markdown: `doc\reports\analysis\te_curve_verification_pipeline\02_visual_reports\dataset_surface_report\polished_dataset\backward\collage\[2026-07-04]\track2_best_model_collage_report.md`.
