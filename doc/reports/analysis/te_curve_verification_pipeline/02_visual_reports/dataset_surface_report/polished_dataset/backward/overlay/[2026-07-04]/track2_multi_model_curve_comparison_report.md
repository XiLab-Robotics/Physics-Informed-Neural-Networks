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

### Backward Reference Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |

### Backward Wave 1 Family Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_bw` | `wave1_current_registry` | Bw | 0.002655 | 0.003193 | 4.708 |
| `harmonic_regression_bw` | `wave1_current_registry` | Bw | 0.008041 | 0.008675 | 16.236 |
| `periodic_mlp_bw` | `wave1_current_registry` | Bw | 0.002769 | 0.003282 | 4.910 |
| `residual_harmonic_mlp_bw` | `wave1_current_registry` | Bw | 0.002713 | 0.003255 | 4.822 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `periodic_mlp_harmonic_bw` | `wave1_periodic_mlp_harmonic_campaign` | Bw | 0.013927 | 0.014623 | 28.984 |

### Backward Wave 2.1 Temporal Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002530 | 0.003060 | 4.674 |
| `gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002425 | 0.002937 | 4.438 |
| `lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002430 | 0.002973 | 4.452 |
| `periodic_temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002326 | 0.002803 | 4.277 |
| `periodic_gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001129 | 0.001412 | 2.228 |
| `periodic_lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001290 | 0.001613 | 2.539 |

### Backward Wave 2.3 Residual Harmonic Temporal Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.010936 | 0.011364 | 22.574 |
| `residual_harmonic_gru_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.020530 | 0.024251 | 43.464 |
| `residual_harmonic_gru_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.015162 | 0.018761 | 32.047 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.011676 | 0.012103 | 23.908 |
| `residual_harmonic_lstm_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.016792 | 0.019189 | 35.128 |
| `residual_harmonic_lstm_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.015864 | 0.020039 | 33.657 |

### Backward Wave 3.1 Offset-Aware Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_bw` | `wave3_1_offset_aware_probe_registry` | Bw | 0.008945 | 0.009670 | 18.730 |

### Backward Wave 3.2 Harmonic-Offset Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_bw` | `wave3_2_harmonic_offset_probe_registry` | Bw | 0.008376 | 0.009258 | 17.556 |
| `wave3_2_harmonic_residual_offset_bw` | `wave3_2_harmonic_offset_probe_registry` | Bw | 0.012996 | 0.013533 | 26.826 |

### Backward Wave 3.3 Curve-Aware Training Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.009939 | 0.010532 | 20.584 |
| `wave3_3_raw_centered_shape_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.010075 | 0.010673 | 20.657 |
| `wave3_3_raw_offset_curve_aware_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.011255 | 0.011824 | 23.166 |
| `wave3_3_full_curve_composite_bw` | `wave3_3_curve_aware_training_registry` | Bw | 0.012620 | 0.013521 | 25.713 |

### Backward Wave 4.1 Robust-Loss Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.014320 | 0.014747 | 30.084 |
| `wave4_1_smooth_l1_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.012012 | 0.012561 | 24.411 |
| `wave4_1_log_cosh_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.009813 | 0.010421 | 19.966 |

### Backward Wave 4.2 Quantile Probabilistic Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_bw` | `wave4_2_probabilistic_registry` | Bw | 0.011462 | 0.011942 | 23.503 |
| `wave4_2_gaussian_nll_bw` | `wave4_2_probabilistic_registry` | Bw | 0.009739 | 0.010201 | 20.349 |

### Backward Wave 4.3 Mixture Density Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_bw` | `wave4_3_mixture_density_registry` | Bw | 0.008282 | 0.010642 | 16.490 |
| `wave4_3_mixture_density_k3_bw` | `wave4_3_mixture_density_registry` | Bw | 0.011511 | 0.011910 | 23.777 |

### Backward Wave 4.4 Latent State Hysteresis Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_bw` | `wave4_4_latent_state_hysteresis_registry` | Bw | 0.016484 | 0.016958 | 34.591 |
| `wave4_4_causal_tcn_latent_offset_residual_bw` | `wave4_4_latent_state_hysteresis_registry` | Bw | 0.007773 | 0.008896 | 15.746 |

### Backward Wave 3 Harmonic Prior Residual Registry Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_bw` | `wave5_1_harmonic_prior_residual_registry` | Bw | 0.009485 | 0.010128 | 19.928 |
| `wave5_1_harmonic_prior_smooth_l1_structured_bw` | `wave5_1_harmonic_prior_residual_registry` | Bw | 0.011508 | 0.012082 | 24.388 |

### Backward Wave52b Offset Harmonic Guided Registry Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_Bw` | `wave52b_offset_harmonic_guided_registry` | Bw | 0.002266 | 0.002708 | 3.986 |

### Backward Polished Model Development Registry Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `polished_feedforward_Bw` | `polished_model_development_registry` | Bw | 0.002655 | 0.003193 | 4.708 |
| `polished_harmonic_regression_Bw` | `polished_model_development_registry` | Bw | 0.008041 | 0.008675 | 16.236 |
| `polished_periodic_mlp_Bw` | `polished_model_development_registry` | Bw | 0.002769 | 0.003282 | 4.910 |
| `polished_residual_harmonic_mlp_Bw` | `polished_model_development_registry` | Bw | 0.002713 | 0.003255 | 4.822 |
| `polished_tree_Bw` | `polished_model_development_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `polished_periodic_mlp_harmonic_Bw` | `polished_model_development_registry` | Bw | 0.002396 | 0.002823 | 4.137 |
| `polished_temporal_convolution_Bw` | `polished_model_development_registry` | Bw | 0.002530 | 0.003060 | 4.674 |
| `polished_gru_sequence_Bw` | `polished_model_development_registry` | Bw | 0.002425 | 0.002937 | 4.438 |
| `polished_lstm_sequence_Bw` | `polished_model_development_registry` | Bw | 0.002430 | 0.002973 | 4.452 |
| `polished_periodic_temporal_convolution_Bw` | `polished_model_development_registry` | Bw | 0.002326 | 0.002803 | 4.277 |
| `polished_periodic_gru_sequence_Bw` | `polished_model_development_registry` | Bw | 0.001129 | 0.001412 | 2.228 |
| `polished_periodic_lstm_sequence_Bw` | `polished_model_development_registry` | Bw | 0.001290 | 0.001613 | 2.539 |
| `polished_residual_harmonic_gru_sequence_sparse_rcim_Bw` | `polished_model_development_registry` | Bw | 0.002331 | 0.002829 | 4.234 |
| `polished_residual_harmonic_gru_sequence_dense240_Bw` | `polished_model_development_registry` | Bw | 0.003416 | 0.004405 | 6.794 |
| `polished_residual_harmonic_gru_sequence_dense360_Bw` | `polished_model_development_registry` | Bw | 0.005031 | 0.008128 | 10.446 |
| `polished_residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `polished_model_development_registry` | Bw | 0.002343 | 0.002825 | 4.242 |
| `polished_residual_harmonic_lstm_sequence_dense240_Bw` | `polished_model_development_registry` | Bw | 0.003569 | 0.004639 | 7.137 |
| `polished_residual_harmonic_lstm_sequence_dense360_Bw` | `polished_model_development_registry` | Bw | 0.005029 | 0.007977 | 10.455 |
| `polished_wave3_1_sequential_residual_offset_probe_Bw` | `polished_model_development_registry` | Bw | 0.002411 | 0.002947 | 4.412 |
| `polished_wave3_2_clean_sequential_residual_offset_Bw` | `polished_model_development_registry` | Bw | 0.002439 | 0.002959 | 4.469 |
| `polished_wave3_2_harmonic_residual_offset_Bw` | `polished_model_development_registry` | Bw | 0.002142 | 0.002591 | 3.805 |
| `polished_wave3_3_curve_aware_pointwise_control_Bw` | `polished_model_development_registry` | Bw | 0.002172 | 0.002638 | 3.909 |
| `polished_wave3_3_raw_centered_shape_curve_aware_Bw` | `polished_model_development_registry` | Bw | 0.002133 | 0.002578 | 3.790 |
| `polished_wave3_3_raw_offset_curve_aware_Bw` | `polished_model_development_registry` | Bw | 0.002139 | 0.002591 | 3.806 |
| `polished_wave3_3_full_curve_composite_Bw` | `polished_model_development_registry` | Bw | 0.002333 | 0.002822 | 4.250 |
| `polished_wave4_1_mae_robust_loss_Bw` | `polished_model_development_registry` | Bw | 0.002133 | 0.002572 | 3.754 |
| `polished_wave4_1_smooth_l1_robust_loss_Bw` | `polished_model_development_registry` | Bw | 0.002236 | 0.002696 | 4.026 |
| `polished_wave4_1_log_cosh_robust_loss_Bw` | `polished_model_development_registry` | Bw | 0.002131 | 0.002576 | 3.787 |
| `polished_wave4_2_quantile_p10_p50_p90_Bw` | `polished_model_development_registry` | Bw | 0.002133 | 0.002585 | 3.778 |
| `polished_wave4_2_gaussian_nll_Bw` | `polished_model_development_registry` | Bw | 0.002133 | 0.002582 | 3.758 |
| `polished_wave4_3_mixture_density_k2_Bw` | `polished_model_development_registry` | Bw | 0.001995 | 0.002403 | 3.526 |
| `polished_wave4_3_mixture_density_k3_Bw` | `polished_model_development_registry` | Bw | 0.001930 | 0.002341 | 3.405 |
| `polished_wave4_4_gru_latent_offset_residual_Bw` | `polished_model_development_registry` | Bw | 0.002455 | 0.002998 | 4.512 |
| `polished_wave4_4_causal_tcn_latent_offset_residual_Bw` | `polished_model_development_registry` | Bw | 0.002485 | 0.003022 | 4.545 |
| `polished_wave5_1_harmonic_prior_pointwise_control_Bw` | `polished_model_development_registry` | Bw | 0.002418 | 0.002843 | 4.202 |
| `polished_wave5_1_harmonic_prior_smooth_l1_structured_Bw` | `polished_model_development_registry` | Bw | 0.002528 | 0.002976 | 4.377 |

### Backward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |
| `feedforward_bw` | `wave1_current_registry` | Bw | 0.002655 | 0.003193 | 4.708 |
| `residual_harmonic_mlp_bw` | `wave1_current_registry` | Bw | 0.002713 | 0.003255 | 4.822 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |

### Backward Reference Tree And Wave 2.1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002530 | 0.003060 | 4.674 |
| `gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002425 | 0.002937 | 4.438 |
| `lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002430 | 0.002973 | 4.452 |
| `periodic_temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.002326 | 0.002803 | 4.277 |
| `periodic_gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001129 | 0.001412 | 2.228 |
| `periodic_lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.001290 | 0.001613 | 2.539 |

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

### Backward Reference Tree And Wave 3.1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `wave3_1_sequential_residual_offset_probe_bw` | `wave3_1_offset_aware_probe_registry` | Bw | 0.008945 | 0.009670 | 18.730 |

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

### Backward Reference Tree And Wave 4 series Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.005363 | 0.006139 | 10.674 |
| `rcim_model_bank_reproduction_best_bw` | `rcim_model_bank_reproduction` | Bw | 0.006633 | 0.007119 | 13.713 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.002756 | 0.003287 | 4.934 |
| `wave4_1_mae_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.014320 | 0.014747 | 30.084 |
| `wave4_1_smooth_l1_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.012012 | 0.012561 | 24.411 |
| `wave4_1_log_cosh_robust_loss_bw` | `wave4_1_robust_loss_registry` | Bw | 0.009813 | 0.010421 | 19.966 |

## Comparison Gallery - Backward Reference Model Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`.

![Backward Reference Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference.png)

## Comparison Gallery - Backward Wave 1 Family Model Overlay

Included models: `feedforward_bw`, `harmonic_regression_bw`, `periodic_mlp_bw`, `residual_harmonic_mlp_bw`, `tree_bw`, `periodic_mlp_harmonic_bw`.

![Backward Wave 1 Family Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave1.png)

## Comparison Gallery - Backward Wave 2.1 Temporal Model Overlay

Included models: `temporal_convolution_bw`, `gru_sequence_bw`, `lstm_sequence_bw`, `periodic_temporal_convolution_bw`, `periodic_gru_sequence_bw`, `periodic_lstm_sequence_bw`.

![Backward Wave 2.1 Temporal Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave2.png)

## Comparison Gallery - Backward Wave 2.3 Residual Harmonic Temporal Overlay

Included models: `residual_harmonic_gru_sequence_sparse_rcim_Bw`, `residual_harmonic_gru_sequence_dense240_Bw`, `residual_harmonic_gru_sequence_dense360_Bw`, `residual_harmonic_lstm_sequence_sparse_rcim_Bw`, `residual_harmonic_lstm_sequence_dense240_Bw`, `residual_harmonic_lstm_sequence_dense360_Bw`.

![Backward Wave 2.3 Residual Harmonic Temporal Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave2c.png)

## Comparison Gallery - Backward Wave 3.1 Offset-Aware Probe Overlay

Included models: `wave3_1_sequential_residual_offset_probe_bw`.

![Backward Wave 3.1 Offset-Aware Probe Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave3_1.png)

## Comparison Gallery - Backward Wave 3.2 Harmonic-Offset Probe Overlay

Included models: `wave3_2_clean_sequential_residual_offset_bw`, `wave3_2_harmonic_residual_offset_bw`.

![Backward Wave 3.2 Harmonic-Offset Probe Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave3_2.png)

## Comparison Gallery - Backward Wave 3.3 Curve-Aware Training Overlay

Included models: `wave3_3_curve_aware_pointwise_control_bw`, `wave3_3_raw_centered_shape_curve_aware_bw`, `wave3_3_raw_offset_curve_aware_bw`, `wave3_3_full_curve_composite_bw`.

![Backward Wave 3.3 Curve-Aware Training Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave3_3.png)

## Comparison Gallery - Backward Wave 4.1 Robust-Loss Overlay

Included models: `wave4_1_mae_robust_loss_bw`, `wave4_1_smooth_l1_robust_loss_bw`, `wave4_1_log_cosh_robust_loss_bw`.

![Backward Wave 4.1 Robust-Loss Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave4_1.png)

## Comparison Gallery - Backward Wave 4.2 Quantile Probabilistic Overlay

Included models: `wave4_2_quantile_p10_p50_p90_bw`, `wave4_2_gaussian_nll_bw`.

![Backward Wave 4.2 Quantile Probabilistic Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave4_2.png)

## Comparison Gallery - Backward Wave 4.3 Mixture Density Overlay

Included models: `wave4_3_mixture_density_k2_bw`, `wave4_3_mixture_density_k3_bw`.

![Backward Wave 4.3 Mixture Density Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave4_3_mixture_density.png)

## Comparison Gallery - Backward Wave 4.4 Latent State Hysteresis Overlay

Included models: `wave4_4_gru_latent_offset_residual_bw`, `wave4_4_causal_tcn_latent_offset_residual_bw`.

![Backward Wave 4.4 Latent State Hysteresis Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave4_4_latent_state_hysteresis.png)

## Comparison Gallery - Backward Wave 3 Harmonic Prior Residual Registry Overlay

Included models: `wave5_1_harmonic_prior_pointwise_control_bw`, `wave5_1_harmonic_prior_smooth_l1_structured_bw`.

![Backward Wave 3 Harmonic Prior Residual Registry Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_wave5_1_harmonic_prior_residual.png)

## Comparison Gallery - Backward Wave52b Offset Harmonic Guided Registry Overlay

Included models: `wave52b_offset_centered_shape_harmonic_Bw`.

![Backward Wave52b Offset Harmonic Guided Registry Overlay TE Curve Verification Pipeline comparison](assets/comparisons/a_bw_wave_offs_harm_guid_reg_ad871b9734.png)

## Comparison Gallery - Backward Polished Model Development Registry Overlay

Included models: `polished_feedforward_Bw`, `polished_harmonic_regression_Bw`, `polished_periodic_mlp_Bw`, `polished_residual_harmonic_mlp_Bw`, `polished_tree_Bw`, `polished_periodic_mlp_harmonic_Bw`, `polished_temporal_convolution_Bw`, `polished_gru_sequence_Bw`, `polished_lstm_sequence_Bw`, `polished_periodic_temporal_convolution_Bw`, `polished_periodic_gru_sequence_Bw`, `polished_periodic_lstm_sequence_Bw`, `polished_residual_harmonic_gru_sequence_sparse_rcim_Bw`, `polished_residual_harmonic_gru_sequence_dense240_Bw`, `polished_residual_harmonic_gru_sequence_dense360_Bw`, `polished_residual_harmonic_lstm_sequence_sparse_rcim_Bw`, `polished_residual_harmonic_lstm_sequence_dense240_Bw`, `polished_residual_harmonic_lstm_sequence_dense360_Bw`, `polished_wave3_1_sequential_residual_offset_probe_Bw`, `polished_wave3_2_clean_sequential_residual_offset_Bw`, `polished_wave3_2_harmonic_residual_offset_Bw`, `polished_wave3_3_curve_aware_pointwise_control_Bw`, `polished_wave3_3_raw_centered_shape_curve_aware_Bw`, `polished_wave3_3_raw_offset_curve_aware_Bw`, `polished_wave3_3_full_curve_composite_Bw`, `polished_wave4_1_mae_robust_loss_Bw`, `polished_wave4_1_smooth_l1_robust_loss_Bw`, `polished_wave4_1_log_cosh_robust_loss_Bw`, `polished_wave4_2_quantile_p10_p50_p90_Bw`, `polished_wave4_2_gaussian_nll_Bw`, `polished_wave4_3_mixture_density_k2_Bw`, `polished_wave4_3_mixture_density_k3_Bw`, `polished_wave4_4_gru_latent_offset_residual_Bw`, `polished_wave4_4_causal_tcn_latent_offset_residual_Bw`, `polished_wave5_1_harmonic_prior_pointwise_control_Bw`, `polished_wave5_1_harmonic_prior_smooth_l1_structured_Bw`.

![Backward Polished Model Development Registry Overlay TE Curve Verification Pipeline comparison](assets/comparisons/a_bw_poli_mode_deve_reg_c54d0bb56e.png)

## Comparison Gallery - Backward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay

Included models: `rcim_model_bank_reproduction_best_bw`, `feedforward_bw`, `residual_harmonic_mlp_bw`, `tree_bw`.

![Backward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_track1_screened_wave1.png)

## Comparison Gallery - Backward Reference Tree And Wave 2.1 Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`, `tree_bw`, `temporal_convolution_bw`, `gru_sequence_bw`, `lstm_sequence_bw`, `periodic_temporal_convolution_bw`, `periodic_gru_sequence_bw`, `periodic_lstm_sequence_bw`.

![Backward Reference Tree And Wave 2.1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference_tree_wave2.png)

## Comparison Gallery - Backward Reference Tree And Wave 2.3 Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`, `tree_bw`, `residual_harmonic_gru_sequence_sparse_rcim_Bw`, `residual_harmonic_gru_sequence_dense240_Bw`, `residual_harmonic_gru_sequence_dense360_Bw`, `residual_harmonic_lstm_sequence_sparse_rcim_Bw`, `residual_harmonic_lstm_sequence_dense240_Bw`, `residual_harmonic_lstm_sequence_dense360_Bw`.

![Backward Reference Tree And Wave 2.3 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference_tree_wave2c.png)

## Comparison Gallery - Backward Reference Tree And Wave 3.1 Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`, `tree_bw`, `wave3_1_sequential_residual_offset_probe_bw`.

![Backward Reference Tree And Wave 3.1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference_tree_wave3_1.png)

## Comparison Gallery - Backward Reference Tree And Wave 3.3 Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`, `tree_bw`, `wave3_3_curve_aware_pointwise_control_bw`, `wave3_3_raw_centered_shape_curve_aware_bw`, `wave3_3_raw_offset_curve_aware_bw`, `wave3_3_full_curve_composite_bw`.

![Backward Reference Tree And Wave 3.3 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference_tree_wave3_3.png)

## Comparison Gallery - Backward Reference Tree And Wave 4 series Overlay

Included models: `paper_retuned_best_Bw`, `rcim_model_bank_reproduction_best_bw`, `tree_bw`, `wave4_1_mae_robust_loss_bw`, `wave4_1_smooth_l1_robust_loss_bw`, `wave4_1_log_cosh_robust_loss_bw`.

![Backward Reference Tree And Wave 4 series Overlay TE Curve Verification Pipeline comparison](assets/comparisons/backward_reference_tree_wave4_1.png)

## Output Artifacts

- output directory: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-07-04-15-48-18__track2_multi_model_curve_comparison_report`;
- summary YAML: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-07-04-15-48-18__track2_multi_model_curve_comparison_report\track2_multi_model_curve_comparison_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-07-04-15-48-18__track2_multi_model_curve_comparison_report\track2_multi_model_curve_comparison_metrics.csv`;
- report Markdown: `doc\reports\analysis\te_curve_verification_pipeline\02_visual_reports\dataset_surface_report\polished_dataset\backward\overlay\[2026-07-04]\track2_multi_model_curve_comparison_report.md`.
