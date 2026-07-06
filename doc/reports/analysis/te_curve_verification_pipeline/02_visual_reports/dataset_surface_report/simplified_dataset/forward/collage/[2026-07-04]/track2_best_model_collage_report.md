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
| `paper_original_best_fw` | `rcim_original` | Fw | 0.002769 | 0.002951 | 6.250 |
| `paper_retuned_best_fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `track1_best_fw` | `rcim_track1` | Fw | 0.003014 | 0.003204 | 6.819 |

### Forward Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_fw` | `wave1_current_registry` | Fw | 0.086931 | 0.087006 | 190.832 |
| `harmonic_regression_fw` | `wave1_current_registry` | Fw | 0.003230 | 0.003494 | 7.185 |
| `periodic_mlp_fw` | `wave1_current_registry` | Fw | 0.089150 | 0.089207 | 195.822 |
| `residual_harmonic_mlp_fw` | `wave1_current_registry` | Fw | 0.085646 | 0.085696 | 187.950 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.066315 | 0.066379 | 145.420 |
| `periodic_mlp_harmonic_fw` | `wave1_periodic_mlp_harmonic_campaign` | Fw | 0.003254 | 0.003553 | 7.232 |

### Forward Wave 2.1 Temporal Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.088705 | 0.088763 | 195.075 |
| `gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.087172 | 0.087229 | 191.682 |
| `lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.088000 | 0.088052 | 193.497 |
| `periodic_temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.085364 | 0.085443 | 187.236 |
| `periodic_gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.086270 | 0.086329 | 189.713 |
| `periodic_lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.087733 | 0.087808 | 192.894 |

### Forward Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003194 | 0.003499 | 7.083 |
| `residual_harmonic_gru_sequence_dense240_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.006983 | 0.009275 | 15.722 |
| `residual_harmonic_gru_sequence_dense360_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007869 | 0.010574 | 17.740 |
| `residual_harmonic_lstm_sequence_sparse_rcim_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003229 | 0.003533 | 7.164 |
| `residual_harmonic_lstm_sequence_dense240_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007042 | 0.009370 | 15.868 |
| `residual_harmonic_lstm_sequence_dense360_fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007731 | 0.010235 | 17.430 |

### Forward Wave 3.1 Offset-Aware Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_fw` | `wave3_1_offset_aware_probe_registry` | Fw | 0.003377 | 0.003799 | 7.487 |

### Forward Wave 3.2 Harmonic-Offset Probe Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_fw` | `wave3_2_harmonic_offset_probe_registry` | Fw | 0.003439 | 0.003870 | 7.632 |
| `wave3_2_harmonic_residual_offset_fw` | `wave3_2_harmonic_offset_probe_registry` | Fw | 0.002850 | 0.003108 | 6.286 |

### Forward Wave 3.3 Curve-Aware Training Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003362 | 0.003612 | 7.474 |
| `wave3_3_raw_centered_shape_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003174 | 0.003429 | 7.047 |
| `wave3_3_raw_offset_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003269 | 0.003588 | 7.268 |
| `wave3_3_full_curve_composite_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003251 | 0.003515 | 7.209 |

### Forward Wave 4.1 Robust-Loss Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.003134 | 0.003382 | 6.956 |
| `wave4_1_smooth_l1_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.003300 | 0.003545 | 7.342 |
| `wave4_1_log_cosh_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.003344 | 0.003595 | 7.427 |

### Forward Wave 4.2 Quantile Probabilistic Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_fw` | `wave4_2_probabilistic_registry` | Fw | 0.003276 | 0.003545 | 7.279 |
| `wave4_2_gaussian_nll_fw` | `wave4_2_probabilistic_registry` | Fw | 0.003156 | 0.003415 | 7.008 |

### Forward Wave 4.3 Mixture Density Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_fw` | `wave4_3_mixture_density_registry` | Fw | 0.003329 | 0.003593 | 7.388 |
| `wave4_3_mixture_density_k3_fw` | `wave4_3_mixture_density_registry` | Fw | 0.003226 | 0.003487 | 7.164 |

### Forward Wave 4.4 Latent State Hysteresis Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_fw` | `wave4_4_latent_state_hysteresis_registry` | Fw | 0.003549 | 0.003996 | 7.873 |
| `wave4_4_causal_tcn_latent_offset_residual_fw` | `wave4_4_latent_state_hysteresis_registry` | Fw | 0.003476 | 0.003939 | 7.717 |

### Forward Wave 5.1 Harmonic Prior Residual Models Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_fw` | `wave5_1_harmonic_prior_residual_registry` | Fw | 0.003374 | 0.003655 | 7.501 |
| `wave5_1_harmonic_prior_smooth_l1_structured_fw` | `wave5_1_harmonic_prior_residual_registry` | Fw | 0.003514 | 0.003768 | 7.812 |

### Forward Polished Model Development Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `polished_feedforward_fw` | `polished_model_development_registry` | Fw | 0.086931 | 0.087006 | 190.832 |
| `polished_harmonic_regression_fw` | `polished_model_development_registry` | Fw | 0.003230 | 0.003494 | 7.185 |
| `polished_periodic_mlp_fw` | `polished_model_development_registry` | Fw | 0.089150 | 0.089207 | 195.822 |
| `polished_residual_harmonic_mlp_fw` | `polished_model_development_registry` | Fw | 0.085646 | 0.085696 | 187.950 |
| `polished_tree_fw` | `polished_model_development_registry` | Fw | 0.066315 | 0.066379 | 145.420 |
| `polished_periodic_mlp_harmonic_fw` | `polished_model_development_registry` | Fw | 0.085830 | 0.085880 | 188.420 |
| `polished_temporal_convolution_fw` | `polished_model_development_registry` | Fw | 0.088705 | 0.088763 | 195.075 |
| `polished_gru_sequence_fw` | `polished_model_development_registry` | Fw | 0.087172 | 0.087229 | 191.682 |
| `polished_lstm_sequence_fw` | `polished_model_development_registry` | Fw | 0.088000 | 0.088052 | 193.497 |
| `polished_periodic_temporal_convolution_fw` | `polished_model_development_registry` | Fw | 0.085364 | 0.085443 | 187.236 |
| `polished_periodic_gru_sequence_fw` | `polished_model_development_registry` | Fw | 0.086270 | 0.086329 | 189.713 |
| `polished_periodic_lstm_sequence_fw` | `polished_model_development_registry` | Fw | 0.087733 | 0.087808 | 192.894 |
| `polished_residual_harmonic_gru_sequence_sparse_rcim_fw` | `polished_model_development_registry` | Fw | 0.088164 | 0.088204 | 193.895 |
| `polished_residual_harmonic_gru_sequence_dense240_fw` | `polished_model_development_registry` | Fw | 0.087700 | 0.087819 | 192.937 |
| `polished_residual_harmonic_gru_sequence_dense360_fw` | `polished_model_development_registry` | Fw | 0.088752 | 0.089230 | 195.144 |
| `polished_residual_harmonic_lstm_sequence_sparse_rcim_fw` | `polished_model_development_registry` | Fw | 0.087932 | 0.087972 | 193.422 |
| `polished_residual_harmonic_lstm_sequence_dense240_fw` | `polished_model_development_registry` | Fw | 0.087313 | 0.087440 | 192.137 |
| `polished_residual_harmonic_lstm_sequence_dense360_fw` | `polished_model_development_registry` | Fw | 0.088280 | 0.088701 | 194.256 |
| `polished_wave3_1_sequential_residual_offset_probe_fw` | `polished_model_development_registry` | Fw | 0.088949 | 0.088999 | 195.544 |
| `polished_wave3_2_clean_sequential_residual_offset_fw` | `polished_model_development_registry` | Fw | 0.087791 | 0.087843 | 193.000 |
| `polished_wave3_2_harmonic_residual_offset_fw` | `polished_model_development_registry` | Fw | 0.087584 | 0.087638 | 192.572 |
| `polished_wave3_3_curve_aware_pointwise_control_fw` | `polished_model_development_registry` | Fw | 0.087578 | 0.087631 | 192.719 |
| `polished_wave3_3_raw_centered_shape_curve_aware_fw` | `polished_model_development_registry` | Fw | 0.084910 | 0.084970 | 186.769 |
| `polished_wave3_3_raw_offset_curve_aware_fw` | `polished_model_development_registry` | Fw | 0.083671 | 0.083727 | 184.231 |
| `polished_wave3_3_full_curve_composite_fw` | `polished_model_development_registry` | Fw | 0.085191 | 0.085256 | 187.347 |
| `polished_wave4_1_mae_robust_loss_fw` | `polished_model_development_registry` | Fw | 0.084308 | 0.084363 | 185.612 |
| `polished_wave4_1_smooth_l1_robust_loss_fw` | `polished_model_development_registry` | Fw | 0.085061 | 0.085122 | 187.116 |
| `polished_wave4_1_log_cosh_robust_loss_fw` | `polished_model_development_registry` | Fw | 0.084634 | 0.084695 | 186.340 |
| `polished_wave4_2_quantile_p10_p50_p90_fw` | `polished_model_development_registry` | Fw | 0.083077 | 0.083129 | 182.617 |
| `polished_wave4_2_gaussian_nll_fw` | `polished_model_development_registry` | Fw | 0.083971 | 0.084023 | 184.509 |
| `polished_wave4_3_mixture_density_k2_fw` | `polished_model_development_registry` | Fw | 0.085189 | 0.085240 | 187.358 |
| `polished_wave4_3_mixture_density_k3_fw` | `polished_model_development_registry` | Fw | 0.083190 | 0.083242 | 182.913 |
| `polished_wave4_4_gru_latent_offset_residual_fw` | `polished_model_development_registry` | Fw | 0.088796 | 0.088857 | 195.229 |
| `polished_wave4_4_causal_tcn_latent_offset_residual_fw` | `polished_model_development_registry` | Fw | 0.087696 | 0.087760 | 192.689 |
| `polished_wave5_1_harmonic_prior_pointwise_control_fw` | `polished_model_development_registry` | Fw | 0.082881 | 0.082943 | 181.809 |
| `polished_wave5_1_harmonic_prior_smooth_l1_structured_fw` | `polished_model_development_registry` | Fw | 0.086190 | 0.086245 | 188.491 |

### Forward Wave52b Offset Harmonic Guided Registry Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_fw` | `wave52b_offset_harmonic_guided_registry` | Fw | 0.058653 | 0.058748 | 128.839 |

## Collage Gallery - Forward Reference Best Models

paper_original_best_fw:

![paper_original_best_fw TE Curve Verification Pipeline collage](assets/forward_reference/paper_original_best_fw.png)

paper_retuned_best_fw:

![paper_retuned_best_fw TE Curve Verification Pipeline collage](assets/forward_reference/paper_retuned_best_fw.png)

## Collage Gallery - Forward Reference Best Models Continued

track1_best_fw:

![track1_best_fw TE Curve Verification Pipeline collage](assets/forward_reference/track1_best_fw.png)

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

## Collage Gallery - Forward Wave 3.1 Offset-Aware Probe Models

wave3_1_sequential_residual_offset_probe_fw:

![wave3_1_sequential_residual_offset_probe_fw TE Curve Verification Pipeline collage](assets/forward_wave3_1/wave3_1_sequential_residual_offset_probe_fw.png)

## Collage Gallery - Forward Wave 3.2 Harmonic-Offset Probe Models

wave3_2_clean_sequential_residual_offset_fw:

![wave3_2_clean_sequential_residual_offset_fw TE Curve Verification Pipeline collage](assets/forward_wave3_2/wave3_2_clean_sequential_residual_offset_fw.png)

wave3_2_harmonic_residual_offset_fw:

![wave3_2_harmonic_residual_offset_fw TE Curve Verification Pipeline collage](assets/forward_wave3_2/wave3_2_harmonic_residual_offset_fw.png)

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

## Collage Gallery - Forward Wave 4.1 Robust-Loss Models

wave4_1_mae_robust_loss_fw:

![wave4_1_mae_robust_loss_fw TE Curve Verification Pipeline collage](assets/forward_wave4_1/wave4_1_mae_robust_loss_fw.png)

wave4_1_smooth_l1_robust_loss_fw:

![wave4_1_smooth_l1_robust_loss_fw TE Curve Verification Pipeline collage](assets/forward_wave4_1/wave4_1_smooth_l1_robust_loss_fw.png)

## Collage Gallery - Forward Wave 4.1 Robust-Loss Models Continued

wave4_1_log_cosh_robust_loss_fw:

![wave4_1_log_cosh_robust_loss_fw TE Curve Verification Pipeline collage](assets/forward_wave4_1/wave4_1_log_cosh_robust_loss_fw.png)

## Collage Gallery - Forward Wave 4.2 Quantile Probabilistic Models

wave4_2_quantile_p10_p50_p90_fw:

![wave4_2_quantile_p10_p50_p90_fw TE Curve Verification Pipeline collage](assets/forward_wave4_2/wave4_2_quantile_p10_p50_p90_fw.png)

wave4_2_gaussian_nll_fw:

![wave4_2_gaussian_nll_fw TE Curve Verification Pipeline collage](assets/forward_wave4_2/wave4_2_gaussian_nll_fw.png)

## Collage Gallery - Forward Wave 4.3 Mixture Density Models Models

wave4_3_mixture_density_k2_fw:

![wave4_3_mixture_density_k2_fw TE Curve Verification Pipeline collage](assets/auto_forward_wave4_3_mixture_density_registry/wave4_3_mixture_density_k2_fw.png)

wave4_3_mixture_density_k3_fw:

![wave4_3_mixture_density_k3_fw TE Curve Verification Pipeline collage](assets/auto_forward_wave4_3_mixture_density_registry/wave4_3_mixture_density_k3_fw.png)

## Collage Gallery - Forward Wave 4.4 Latent State Hysteresis Models Models

wave4_4_gru_latent_offset_residual_fw:

![wave4_4_gru_latent_offset_residual_fw TE Curve Verification Pipeline collage](assets/a_fw_w4_4_late_stat_hyst_reg_87cb6f7756/wave4_4_gru_latent_offset_residual_fw.png)

wave4_4_causal_tcn_latent_offset_residual_fw:

![wave4_4_causal_tcn_latent_offset_residual_fw TE Curve Verification Pipeline collage](assets/a_fw_w4_4_late_stat_hyst_reg_87cb6f7756/wave4_4_causal_tcn_latent_offset_residual_fw.png)

## Collage Gallery - Forward Wave 5.1 Harmonic Prior Residual Models Models

wave5_1_harmonic_prior_pointwise_control_fw:

![wave5_1_harmonic_prior_pointwise_control_fw TE Curve Verification Pipeline collage](assets/a_fw_w5_1_harm_pri_res_reg_74c66fdb87/wave5_1_harmonic_prior_pointwise_control_fw.png)

wave5_1_harmonic_prior_smooth_l1_structured_fw:

![wave5_1_harmonic_prior_smooth_l1_structured_fw TE Curve Verification Pipeline collage](assets/a_fw_w5_1_harm_pri_res_reg_74c66fdb87/wave5_1_harmonic_prior_smooth_l1_structured_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models

polished_feedforward_fw:

![polished_feedforward_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_feedforward_fw.png)

polished_harmonic_regression_fw:

![polished_harmonic_regression_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_harmonic_regression_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued

polished_periodic_mlp_fw:

![polished_periodic_mlp_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_periodic_mlp_fw.png)

polished_residual_harmonic_mlp_fw:

![polished_residual_harmonic_mlp_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_residual_harmonic_mlp_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 2

polished_tree_fw:

![polished_tree_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_tree_fw.png)

polished_periodic_mlp_harmonic_fw:

![polished_periodic_mlp_harmonic_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_periodic_mlp_harmonic_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 3

polished_temporal_convolution_fw:

![polished_temporal_convolution_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_temporal_convolution_fw.png)

polished_gru_sequence_fw:

![polished_gru_sequence_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_gru_sequence_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 4

polished_lstm_sequence_fw:

![polished_lstm_sequence_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_lstm_sequence_fw.png)

polished_periodic_temporal_convolution_fw:

![polished_periodic_temporal_convolution_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_periodic_temporal_convolution_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 5

polished_periodic_gru_sequence_fw:

![polished_periodic_gru_sequence_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_periodic_gru_sequence_fw.png)

polished_periodic_lstm_sequence_fw:

![polished_periodic_lstm_sequence_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_periodic_lstm_sequence_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 6

polished_residual_harmonic_gru_sequence_sparse_rcim_fw:

![polished_residual_harmonic_gru_sequence_sparse_rcim_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_residual_harmonic_gru_sequence_sparse_rcim_fw.png)

polished_residual_harmonic_gru_sequence_dense240_fw:

![polished_residual_harmonic_gru_sequence_dense240_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_residual_harmonic_gru_sequence_dense240_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 7

polished_residual_harmonic_gru_sequence_dense360_fw:

![polished_residual_harmonic_gru_sequence_dense360_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_residual_harmonic_gru_sequence_dense360_fw.png)

polished_residual_harmonic_lstm_sequence_sparse_rcim_fw:

![polished_residual_harmonic_lstm_sequence_sparse_rcim_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_residual_harmonic_lstm_sequence_sparse_rcim_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 8

polished_residual_harmonic_lstm_sequence_dense240_fw:

![polished_residual_harmonic_lstm_sequence_dense240_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_residual_harmonic_lstm_sequence_dense240_fw.png)

polished_residual_harmonic_lstm_sequence_dense360_fw:

![polished_residual_harmonic_lstm_sequence_dense360_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_residual_harmonic_lstm_sequence_dense360_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 9

polished_wave3_1_sequential_residual_offset_probe_fw:

![polished_wave3_1_sequential_residual_offset_probe_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave3_1_sequential_residual_offset_probe_fw.png)

polished_wave3_2_clean_sequential_residual_offset_fw:

![polished_wave3_2_clean_sequential_residual_offset_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave3_2_clean_sequential_residual_offset_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 10

polished_wave3_2_harmonic_residual_offset_fw:

![polished_wave3_2_harmonic_residual_offset_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave3_2_harmonic_residual_offset_fw.png)

polished_wave3_3_curve_aware_pointwise_control_fw:

![polished_wave3_3_curve_aware_pointwise_control_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave3_3_curve_aware_pointwise_control_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 11

polished_wave3_3_raw_centered_shape_curve_aware_fw:

![polished_wave3_3_raw_centered_shape_curve_aware_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave3_3_raw_centered_shape_curve_aware_fw.png)

polished_wave3_3_raw_offset_curve_aware_fw:

![polished_wave3_3_raw_offset_curve_aware_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave3_3_raw_offset_curve_aware_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 12

polished_wave3_3_full_curve_composite_fw:

![polished_wave3_3_full_curve_composite_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave3_3_full_curve_composite_fw.png)

polished_wave4_1_mae_robust_loss_fw:

![polished_wave4_1_mae_robust_loss_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave4_1_mae_robust_loss_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 13

polished_wave4_1_smooth_l1_robust_loss_fw:

![polished_wave4_1_smooth_l1_robust_loss_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave4_1_smooth_l1_robust_loss_fw.png)

polished_wave4_1_log_cosh_robust_loss_fw:

![polished_wave4_1_log_cosh_robust_loss_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave4_1_log_cosh_robust_loss_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 14

polished_wave4_2_quantile_p10_p50_p90_fw:

![polished_wave4_2_quantile_p10_p50_p90_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave4_2_quantile_p10_p50_p90_fw.png)

polished_wave4_2_gaussian_nll_fw:

![polished_wave4_2_gaussian_nll_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave4_2_gaussian_nll_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 15

polished_wave4_3_mixture_density_k2_fw:

![polished_wave4_3_mixture_density_k2_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave4_3_mixture_density_k2_fw.png)

polished_wave4_3_mixture_density_k3_fw:

![polished_wave4_3_mixture_density_k3_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave4_3_mixture_density_k3_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 16

polished_wave4_4_gru_latent_offset_residual_fw:

![polished_wave4_4_gru_latent_offset_residual_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave4_4_gru_latent_offset_residual_fw.png)

polished_wave4_4_causal_tcn_latent_offset_residual_fw:

![polished_wave4_4_causal_tcn_latent_offset_residual_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave4_4_causal_tcn_latent_offset_residual_fw.png)

## Collage Gallery - Forward Polished Model Development Registry Models Continued 17

polished_wave5_1_harmonic_prior_pointwise_control_fw:

![polished_wave5_1_harmonic_prior_pointwise_control_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave5_1_harmonic_prior_pointwise_control_fw.png)

polished_wave5_1_harmonic_prior_smooth_l1_structured_fw:

![polished_wave5_1_harmonic_prior_smooth_l1_structured_fw TE Curve Verification Pipeline collage](assets/auto_forward_polished_model_development_registry/polished_wave5_1_harmonic_prior_smooth_l1_structured_fw.png)

## Collage Gallery - Forward Wave52b Offset Harmonic Guided Registry Models

wave52b_offset_centered_shape_harmonic_fw:

![wave52b_offset_centered_shape_harmonic_fw TE Curve Verification Pipeline collage](assets/a_fw_wave_offs_harm_guid_reg_bd35ddc75a/wave52b_offset_centered_shape_harmonic_fw.png)

## Output Artifacts

- output directory: `output\validation_checks\track2_best_model_collage_report\2026-07-05-09-24-32__track2_best_model_collage_report`;
- summary YAML: `output\validation_checks\track2_best_model_collage_report\2026-07-05-09-24-32__track2_best_model_collage_report\track2_best_model_collage_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_best_model_collage_report\2026-07-05-09-24-32__track2_best_model_collage_report\track2_best_model_collage_metrics.csv`;
- report Markdown: `doc\reports\analysis\te_curve_verification_pipeline\02_visual_reports\dataset_surface_report\simplified_dataset\forward\collage\[2026-07-04]\track2_best_model_collage_report.md`.
