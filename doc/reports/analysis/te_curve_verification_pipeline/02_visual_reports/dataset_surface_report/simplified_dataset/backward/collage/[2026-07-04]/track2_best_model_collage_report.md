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
| `paper_retuned_best_bw` | `rcim_retuned` | Bw | 0.003675 | 0.004284 | 7.572 |
| `track1_best_bw` | `rcim_track1` | Bw | 0.005027 | 0.005212 | 11.860 |

### Backward Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_bw` | `wave1_current_registry` | Bw | 0.008079 | 0.008672 | 17.892 |
| `harmonic_regression_bw` | `wave1_current_registry` | Bw | 0.003678 | 0.004012 | 8.058 |
| `periodic_mlp_bw` | `wave1_current_registry` | Bw | 0.010754 | 0.011174 | 23.160 |
| `residual_harmonic_mlp_bw` | `wave1_current_registry` | Bw | 0.008619 | 0.009001 | 18.775 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.015215 | 0.015523 | 34.609 |
| `periodic_mlp_harmonic_bw` | `wave1_periodic_mlp_harmonic_campaign` | Bw | 0.003583 | 0.003925 | 7.875 |

### Backward Wave 2.1 Temporal Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.008956 | 0.009381 | 19.524 |
| `gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.007468 | 0.007885 | 16.367 |
| `lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.006945 | 0.007367 | 15.245 |
| `periodic_temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.007596 | 0.008027 | 16.602 |
| `periodic_gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.006320 | 0.006795 | 14.078 |
| `periodic_lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.010769 | 0.011111 | 23.306 |

### Backward Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.003502 | 0.003857 | 7.654 |
| `residual_harmonic_gru_sequence_dense240_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.008984 | 0.012987 | 20.358 |
| `residual_harmonic_gru_sequence_dense360_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.009370 | 0.013165 | 21.267 |
| `residual_harmonic_lstm_sequence_sparse_rcim_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.003440 | 0.003793 | 7.510 |
| `residual_harmonic_lstm_sequence_dense240_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.007367 | 0.009945 | 16.660 |
| `residual_harmonic_lstm_sequence_dense360_bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.010268 | 0.014769 | 23.355 |

### Backward Wave 3.1 Offset-Aware Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_bw` | `wave3_1_offset_aware_probe_registry` | Bw | 0.003636 | 0.004065 | 7.952 |

### Backward Wave 3.2 Harmonic-Offset Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_bw` | `wave3_2_harmonic_offset_probe_registry` | Bw | 0.003541 | 0.003971 | 7.732 |
| `wave3_2_harmonic_residual_offset_bw` | `wave3_2_harmonic_offset_probe_registry` | Bw | 0.003331 | 0.003671 | 7.261 |

### Backward Wave 3.3 Curve-Aware Training Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.003436 | 0.003761 | 7.538 |
| `wave3_3_raw_centered_shape_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.003465 | 0.003790 | 7.582 |
| `wave3_3_raw_offset_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.003469 | 0.003799 | 7.608 |
| `wave3_3_full_curve_composite_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.003510 | 0.003897 | 7.683 |

### Backward Wave 4.1 Robust-Loss Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.003433 | 0.003750 | 7.506 |
| `wave4_1_smooth_l1_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.003078 | 0.003403 | 6.676 |
| `wave4_1_log_cosh_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.003486 | 0.003811 | 7.628 |

### Backward Wave 4.2 Quantile Probabilistic Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_bw` | `wave4_2_probabilistic_registry` | Bw | 0.002935 | 0.003250 | 6.307 |
| `wave4_2_gaussian_nll_bw` | `wave4_2_probabilistic_registry` | Bw | 0.003001 | 0.003303 | 6.488 |

### Backward Wave 4.3 Mixture Density Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_bw` | `wave4_3_mixture_density_registry` | Bw | 0.002668 | 0.002947 | 5.880 |
| `wave4_3_mixture_density_k3_bw` | `wave4_3_mixture_density_registry` | Bw | 0.002730 | 0.003009 | 6.049 |

### Backward Wave 4.4 Latent State Hysteresis Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_bw` | `wave4_4_latent_state_hysteresis_registry` | Bw | 0.003542 | 0.003984 | 7.736 |
| `wave4_4_causal_tcn_latent_offset_residual_bw` | `wave4_4_latent_state_hysteresis_registry` | Bw | 0.003624 | 0.004098 | 7.903 |

### Backward Wave 5.1 Harmonic Prior Residual Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_bw` | `wave5_1_harmonic_prior_residual_registry` | Bw | 0.003360 | 0.003677 | 7.363 |
| `wave5_1_harmonic_prior_smooth_l1_structured_bw` | `wave5_1_harmonic_prior_residual_registry` | Bw | 0.003431 | 0.003739 | 7.523 |

### Backward Polished Model Development Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `polished_feedforward_bw` | `polished_model_development_registry` | Bw | 0.008079 | 0.008672 | 17.892 |
| `polished_harmonic_regression_bw` | `polished_model_development_registry` | Bw | 0.003678 | 0.004012 | 8.058 |
| `polished_periodic_mlp_bw` | `polished_model_development_registry` | Bw | 0.010754 | 0.011174 | 23.160 |
| `polished_residual_harmonic_mlp_bw` | `polished_model_development_registry` | Bw | 0.008619 | 0.009001 | 18.775 |
| `polished_tree_bw` | `polished_model_development_registry` | Bw | 0.015215 | 0.015523 | 34.609 |
| `polished_periodic_mlp_harmonic_bw` | `polished_model_development_registry` | Bw | 0.009393 | 0.009831 | 20.198 |
| `polished_temporal_convolution_bw` | `polished_model_development_registry` | Bw | 0.008956 | 0.009381 | 19.524 |
| `polished_gru_sequence_bw` | `polished_model_development_registry` | Bw | 0.007468 | 0.007885 | 16.367 |
| `polished_lstm_sequence_bw` | `polished_model_development_registry` | Bw | 0.006945 | 0.007367 | 15.245 |
| `polished_periodic_temporal_convolution_bw` | `polished_model_development_registry` | Bw | 0.007596 | 0.008027 | 16.602 |
| `polished_periodic_gru_sequence_bw` | `polished_model_development_registry` | Bw | 0.006320 | 0.006795 | 14.078 |
| `polished_periodic_lstm_sequence_bw` | `polished_model_development_registry` | Bw | 0.010769 | 0.011111 | 23.306 |
| `polished_residual_harmonic_gru_sequence_sparse_rcim_bw` | `polished_model_development_registry` | Bw | 0.007012 | 0.007383 | 15.369 |
| `polished_residual_harmonic_gru_sequence_dense240_bw` | `polished_model_development_registry` | Bw | 0.009235 | 0.009959 | 20.204 |
| `polished_residual_harmonic_gru_sequence_dense360_bw` | `polished_model_development_registry` | Bw | 0.010578 | 0.012666 | 23.297 |
| `polished_residual_harmonic_lstm_sequence_sparse_rcim_bw` | `polished_model_development_registry` | Bw | 0.007740 | 0.008099 | 16.813 |
| `polished_residual_harmonic_lstm_sequence_dense240_bw` | `polished_model_development_registry` | Bw | 0.006772 | 0.007632 | 14.902 |
| `polished_residual_harmonic_lstm_sequence_dense360_bw` | `polished_model_development_registry` | Bw | 0.009108 | 0.011272 | 20.181 |
| `polished_wave3_1_sequential_residual_offset_probe_bw` | `polished_model_development_registry` | Bw | 0.009712 | 0.010105 | 21.306 |
| `polished_wave3_2_clean_sequential_residual_offset_bw` | `polished_model_development_registry` | Bw | 0.008107 | 0.008493 | 17.879 |
| `polished_wave3_2_harmonic_residual_offset_bw` | `polished_model_development_registry` | Bw | 0.004950 | 0.005267 | 11.001 |
| `polished_wave3_3_curve_aware_pointwise_control_bw` | `polished_model_development_registry` | Bw | 0.007181 | 0.007525 | 15.776 |
| `polished_wave3_3_raw_centered_shape_curve_aware_bw` | `polished_model_development_registry` | Bw | 0.005377 | 0.005696 | 11.898 |
| `polished_wave3_3_raw_offset_curve_aware_bw` | `polished_model_development_registry` | Bw | 0.007815 | 0.008139 | 17.245 |
| `polished_wave3_3_full_curve_composite_bw` | `polished_model_development_registry` | Bw | 0.005651 | 0.006040 | 12.391 |
| `polished_wave4_1_mae_robust_loss_bw` | `polished_model_development_registry` | Bw | 0.008153 | 0.008484 | 17.810 |
| `polished_wave4_1_smooth_l1_robust_loss_bw` | `polished_model_development_registry` | Bw | 0.007174 | 0.007502 | 15.817 |
| `polished_wave4_1_log_cosh_robust_loss_bw` | `polished_model_development_registry` | Bw | 0.004849 | 0.005168 | 10.664 |
| `polished_wave4_2_quantile_p10_p50_p90_bw` | `polished_model_development_registry` | Bw | 0.003809 | 0.004175 | 8.347 |
| `polished_wave4_2_gaussian_nll_bw` | `polished_model_development_registry` | Bw | 0.005195 | 0.005557 | 11.506 |
| `polished_wave4_3_mixture_density_k2_bw` | `polished_model_development_registry` | Bw | 0.004718 | 0.005044 | 10.385 |
| `polished_wave4_3_mixture_density_k3_bw` | `polished_model_development_registry` | Bw | 0.005049 | 0.005359 | 11.212 |
| `polished_wave4_4_gru_latent_offset_residual_bw` | `polished_model_development_registry` | Bw | 0.008062 | 0.008539 | 17.742 |
| `polished_wave4_4_causal_tcn_latent_offset_residual_bw` | `polished_model_development_registry` | Bw | 0.007758 | 0.008220 | 17.080 |
| `polished_wave5_1_harmonic_prior_pointwise_control_bw` | `polished_model_development_registry` | Bw | 0.007570 | 0.007930 | 16.593 |
| `polished_wave5_1_harmonic_prior_smooth_l1_structured_bw` | `polished_model_development_registry` | Bw | 0.006945 | 0.007295 | 15.256 |

### Backward Wave52b Offset Harmonic Guided Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_bw` | `wave52b_offset_harmonic_guided_registry` | Bw | 0.020690 | 0.021139 | 48.162 |

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

- output directory: `output\validation_checks\track2_best_model_collage_report\2026-07-05-15-00-18__track2_best_model_collage_report`;
- summary YAML: `output\validation_checks\track2_best_model_collage_report\2026-07-05-15-00-18__track2_best_model_collage_report\track2_best_model_collage_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_best_model_collage_report\2026-07-05-15-00-18__track2_best_model_collage_report\track2_best_model_collage_metrics.csv`;
- report Markdown: `doc\reports\analysis\te_curve_verification_pipeline\02_visual_reports\dataset_surface_report\simplified_dataset\backward\collage\[2026-07-04]\track2_best_model_collage_report.md`.
