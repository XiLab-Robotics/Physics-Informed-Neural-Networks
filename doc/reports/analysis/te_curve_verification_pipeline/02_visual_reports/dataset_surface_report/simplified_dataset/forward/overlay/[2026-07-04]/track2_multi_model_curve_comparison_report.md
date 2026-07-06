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
| `paper_original_best_Fw` | `rcim_original` | Fw | 0.002769 | 0.002951 | 6.250 |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.003014 | 0.003204 | 6.819 |

### Forward Wave 1 Family Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_fw` | `wave1_current_registry` | Fw | 0.086931 | 0.087006 | 190.832 |
| `harmonic_regression_fw` | `wave1_current_registry` | Fw | 0.003230 | 0.003494 | 7.185 |
| `periodic_mlp_fw` | `wave1_current_registry` | Fw | 0.089150 | 0.089207 | 195.822 |
| `residual_harmonic_mlp_fw` | `wave1_current_registry` | Fw | 0.085646 | 0.085696 | 187.950 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.066315 | 0.066379 | 145.420 |
| `periodic_mlp_harmonic_fw` | `wave1_periodic_mlp_harmonic_campaign` | Fw | 0.003254 | 0.003553 | 7.232 |

### Forward Wave 2.1 Temporal Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.088705 | 0.088763 | 195.075 |
| `gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.087172 | 0.087229 | 191.682 |
| `lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.088000 | 0.088052 | 193.497 |
| `periodic_temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.085364 | 0.085443 | 187.236 |
| `periodic_gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.086270 | 0.086329 | 189.713 |
| `periodic_lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.087733 | 0.087808 | 192.894 |

### Forward Wave 2.3 Residual Harmonic Temporal Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003194 | 0.003499 | 7.083 |
| `residual_harmonic_gru_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.006983 | 0.009275 | 15.722 |
| `residual_harmonic_gru_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007869 | 0.010574 | 17.740 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003229 | 0.003533 | 7.164 |
| `residual_harmonic_lstm_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007042 | 0.009370 | 15.868 |
| `residual_harmonic_lstm_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007731 | 0.010235 | 17.430 |

### Forward Wave 3.1 Offset-Aware Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_1_sequential_residual_offset_probe_fw` | `wave3_1_offset_aware_probe_registry` | Fw | 0.003377 | 0.003799 | 7.487 |

### Forward Wave 3.2 Harmonic-Offset Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_2_clean_sequential_residual_offset_fw` | `wave3_2_harmonic_offset_probe_registry` | Fw | 0.003439 | 0.003870 | 7.632 |
| `wave3_2_harmonic_residual_offset_fw` | `wave3_2_harmonic_offset_probe_registry` | Fw | 0.002850 | 0.003108 | 6.286 |

### Forward Wave 3.3 Curve-Aware Training Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave3_3_curve_aware_pointwise_control_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003362 | 0.003612 | 7.474 |
| `wave3_3_raw_centered_shape_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003174 | 0.003429 | 7.047 |
| `wave3_3_raw_offset_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003269 | 0.003588 | 7.268 |
| `wave3_3_full_curve_composite_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003251 | 0.003515 | 7.209 |

### Forward Wave 4.1 Robust-Loss Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_1_mae_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.003134 | 0.003382 | 6.956 |
| `wave4_1_smooth_l1_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.003300 | 0.003545 | 7.342 |
| `wave4_1_log_cosh_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.003344 | 0.003595 | 7.427 |

### Forward Wave 4.2 Quantile Probabilistic Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_2_quantile_p10_p50_p90_fw` | `wave4_2_probabilistic_registry` | Fw | 0.003276 | 0.003545 | 7.279 |
| `wave4_2_gaussian_nll_fw` | `wave4_2_probabilistic_registry` | Fw | 0.003156 | 0.003415 | 7.008 |

### Forward Wave 4.3 Mixture Density Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_3_mixture_density_k2_fw` | `wave4_3_mixture_density_registry` | Fw | 0.003329 | 0.003593 | 7.388 |
| `wave4_3_mixture_density_k3_fw` | `wave4_3_mixture_density_registry` | Fw | 0.003226 | 0.003487 | 7.164 |

### Forward Wave 4.4 Latent State Hysteresis Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave4_4_gru_latent_offset_residual_fw` | `wave4_4_latent_state_hysteresis_registry` | Fw | 0.003549 | 0.003996 | 7.873 |
| `wave4_4_causal_tcn_latent_offset_residual_fw` | `wave4_4_latent_state_hysteresis_registry` | Fw | 0.003476 | 0.003939 | 7.717 |

### Forward Wave 3 Harmonic Prior Residual Registry Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave5_1_harmonic_prior_pointwise_control_fw` | `wave5_1_harmonic_prior_residual_registry` | Fw | 0.003374 | 0.003655 | 7.501 |
| `wave5_1_harmonic_prior_smooth_l1_structured_fw` | `wave5_1_harmonic_prior_residual_registry` | Fw | 0.003514 | 0.003768 | 7.812 |

### Forward Wave52b Offset Harmonic Guided Registry Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52b_offset_centered_shape_harmonic_Fw` | `wave52b_offset_harmonic_guided_registry` | Fw | 0.058653 | 0.058748 | 128.839 |

### Forward Polished Model Development Registry Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `polished_feedforward_Fw` | `polished_model_development_registry` | Fw | 0.086931 | 0.087006 | 190.832 |
| `polished_harmonic_regression_Fw` | `polished_model_development_registry` | Fw | 0.003230 | 0.003494 | 7.185 |
| `polished_periodic_mlp_Fw` | `polished_model_development_registry` | Fw | 0.089150 | 0.089207 | 195.822 |
| `polished_residual_harmonic_mlp_Fw` | `polished_model_development_registry` | Fw | 0.085646 | 0.085696 | 187.950 |
| `polished_tree_Fw` | `polished_model_development_registry` | Fw | 0.066315 | 0.066379 | 145.420 |
| `polished_periodic_mlp_harmonic_Fw` | `polished_model_development_registry` | Fw | 0.085830 | 0.085880 | 188.420 |
| `polished_temporal_convolution_Fw` | `polished_model_development_registry` | Fw | 0.088705 | 0.088763 | 195.075 |
| `polished_gru_sequence_Fw` | `polished_model_development_registry` | Fw | 0.087172 | 0.087229 | 191.682 |
| `polished_lstm_sequence_Fw` | `polished_model_development_registry` | Fw | 0.088000 | 0.088052 | 193.497 |
| `polished_periodic_temporal_convolution_Fw` | `polished_model_development_registry` | Fw | 0.085364 | 0.085443 | 187.236 |
| `polished_periodic_gru_sequence_Fw` | `polished_model_development_registry` | Fw | 0.086270 | 0.086329 | 189.713 |
| `polished_periodic_lstm_sequence_Fw` | `polished_model_development_registry` | Fw | 0.087733 | 0.087808 | 192.894 |
| `polished_residual_harmonic_gru_sequence_sparse_rcim_Fw` | `polished_model_development_registry` | Fw | 0.088164 | 0.088204 | 193.895 |
| `polished_residual_harmonic_gru_sequence_dense240_Fw` | `polished_model_development_registry` | Fw | 0.087700 | 0.087819 | 192.937 |
| `polished_residual_harmonic_gru_sequence_dense360_Fw` | `polished_model_development_registry` | Fw | 0.088752 | 0.089230 | 195.144 |
| `polished_residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `polished_model_development_registry` | Fw | 0.087932 | 0.087972 | 193.422 |
| `polished_residual_harmonic_lstm_sequence_dense240_Fw` | `polished_model_development_registry` | Fw | 0.087313 | 0.087440 | 192.137 |
| `polished_residual_harmonic_lstm_sequence_dense360_Fw` | `polished_model_development_registry` | Fw | 0.088280 | 0.088701 | 194.256 |
| `polished_wave3_1_sequential_residual_offset_probe_Fw` | `polished_model_development_registry` | Fw | 0.088949 | 0.088999 | 195.544 |
| `polished_wave3_2_clean_sequential_residual_offset_Fw` | `polished_model_development_registry` | Fw | 0.087791 | 0.087843 | 193.000 |
| `polished_wave3_2_harmonic_residual_offset_Fw` | `polished_model_development_registry` | Fw | 0.087584 | 0.087638 | 192.572 |
| `polished_wave3_3_curve_aware_pointwise_control_Fw` | `polished_model_development_registry` | Fw | 0.087578 | 0.087631 | 192.719 |
| `polished_wave3_3_raw_centered_shape_curve_aware_Fw` | `polished_model_development_registry` | Fw | 0.084910 | 0.084970 | 186.769 |
| `polished_wave3_3_raw_offset_curve_aware_Fw` | `polished_model_development_registry` | Fw | 0.083671 | 0.083727 | 184.231 |
| `polished_wave3_3_full_curve_composite_Fw` | `polished_model_development_registry` | Fw | 0.085191 | 0.085256 | 187.347 |
| `polished_wave4_1_mae_robust_loss_Fw` | `polished_model_development_registry` | Fw | 0.084308 | 0.084363 | 185.612 |
| `polished_wave4_1_smooth_l1_robust_loss_Fw` | `polished_model_development_registry` | Fw | 0.085061 | 0.085122 | 187.116 |
| `polished_wave4_1_log_cosh_robust_loss_Fw` | `polished_model_development_registry` | Fw | 0.084634 | 0.084695 | 186.340 |
| `polished_wave4_2_quantile_p10_p50_p90_Fw` | `polished_model_development_registry` | Fw | 0.083077 | 0.083129 | 182.617 |
| `polished_wave4_2_gaussian_nll_Fw` | `polished_model_development_registry` | Fw | 0.083971 | 0.084023 | 184.509 |
| `polished_wave4_3_mixture_density_k2_Fw` | `polished_model_development_registry` | Fw | 0.085189 | 0.085240 | 187.358 |
| `polished_wave4_3_mixture_density_k3_Fw` | `polished_model_development_registry` | Fw | 0.083190 | 0.083242 | 182.913 |
| `polished_wave4_4_gru_latent_offset_residual_Fw` | `polished_model_development_registry` | Fw | 0.088796 | 0.088857 | 195.229 |
| `polished_wave4_4_causal_tcn_latent_offset_residual_Fw` | `polished_model_development_registry` | Fw | 0.087696 | 0.087760 | 192.689 |
| `polished_wave5_1_harmonic_prior_pointwise_control_Fw` | `polished_model_development_registry` | Fw | 0.082881 | 0.082943 | 181.809 |
| `polished_wave5_1_harmonic_prior_smooth_l1_structured_Fw` | `polished_model_development_registry` | Fw | 0.086190 | 0.086245 | 188.491 |

### Forward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.003014 | 0.003204 | 6.819 |
| `harmonic_regression_fw` | `wave1_current_registry` | Fw | 0.003230 | 0.003494 | 7.185 |
| `periodic_mlp_harmonic_fw` | `wave1_periodic_mlp_harmonic_campaign` | Fw | 0.003254 | 0.003553 | 7.232 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.066315 | 0.066379 | 145.420 |

### Forward Reference Tree And Wave 2.1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.003014 | 0.003204 | 6.819 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.066315 | 0.066379 | 145.420 |
| `temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.088705 | 0.088763 | 195.075 |
| `gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.087172 | 0.087229 | 191.682 |
| `lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.088000 | 0.088052 | 193.497 |
| `periodic_temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.085364 | 0.085443 | 187.236 |
| `periodic_gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.086270 | 0.086329 | 189.713 |
| `periodic_lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.087733 | 0.087808 | 192.894 |

### Forward Reference Tree And Wave 2.3 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.003014 | 0.003204 | 6.819 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.066315 | 0.066379 | 145.420 |
| `residual_harmonic_gru_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003194 | 0.003499 | 7.083 |
| `residual_harmonic_gru_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.006983 | 0.009275 | 15.722 |
| `residual_harmonic_gru_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007869 | 0.010574 | 17.740 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003229 | 0.003533 | 7.164 |
| `residual_harmonic_lstm_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007042 | 0.009370 | 15.868 |
| `residual_harmonic_lstm_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007731 | 0.010235 | 17.430 |

### Forward Reference Tree And Wave 3.1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.003014 | 0.003204 | 6.819 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.066315 | 0.066379 | 145.420 |
| `wave3_1_sequential_residual_offset_probe_fw` | `wave3_1_offset_aware_probe_registry` | Fw | 0.003377 | 0.003799 | 7.487 |

### Forward Reference Tree And Wave 3.3 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.003014 | 0.003204 | 6.819 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.066315 | 0.066379 | 145.420 |
| `wave3_3_curve_aware_pointwise_control_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003362 | 0.003612 | 7.474 |
| `wave3_3_raw_centered_shape_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003174 | 0.003429 | 7.047 |
| `wave3_3_raw_offset_curve_aware_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003269 | 0.003588 | 7.268 |
| `wave3_3_full_curve_composite_fw` | `wave3_3_curve_aware_training_registry` | Fw | 0.003251 | 0.003515 | 7.209 |

### Forward Reference Tree And Wave 4 series Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `rcim_model_bank_reproduction_best_fw` | `rcim_model_bank_reproduction` | Fw | 0.003014 | 0.003204 | 6.819 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.066315 | 0.066379 | 145.420 |
| `wave4_1_mae_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.003134 | 0.003382 | 6.956 |
| `wave4_1_smooth_l1_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.003300 | 0.003545 | 7.342 |
| `wave4_1_log_cosh_robust_loss_fw` | `wave4_1_robust_loss_registry` | Fw | 0.003344 | 0.003595 | 7.427 |

## Comparison Gallery - Forward Reference Model Overlay

Included models: `paper_original_best_Fw`, `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`.

![Forward Reference Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference.png)

## Comparison Gallery - Forward Wave 1 Family Model Overlay

Included models: `feedforward_fw`, `harmonic_regression_fw`, `periodic_mlp_fw`, `residual_harmonic_mlp_fw`, `tree_fw`, `periodic_mlp_harmonic_fw`.

![Forward Wave 1 Family Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave1.png)

## Comparison Gallery - Forward Wave 2.1 Temporal Model Overlay

Included models: `temporal_convolution_fw`, `gru_sequence_fw`, `lstm_sequence_fw`, `periodic_temporal_convolution_fw`, `periodic_gru_sequence_fw`, `periodic_lstm_sequence_fw`.

![Forward Wave 2.1 Temporal Model Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave2.png)

## Comparison Gallery - Forward Wave 2.3 Residual Harmonic Temporal Overlay

Included models: `residual_harmonic_gru_sequence_sparse_rcim_Fw`, `residual_harmonic_gru_sequence_dense240_Fw`, `residual_harmonic_gru_sequence_dense360_Fw`, `residual_harmonic_lstm_sequence_sparse_rcim_Fw`, `residual_harmonic_lstm_sequence_dense240_Fw`, `residual_harmonic_lstm_sequence_dense360_Fw`.

![Forward Wave 2.3 Residual Harmonic Temporal Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave2c.png)

## Comparison Gallery - Forward Wave 3.1 Offset-Aware Probe Overlay

Included models: `wave3_1_sequential_residual_offset_probe_fw`.

![Forward Wave 3.1 Offset-Aware Probe Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave3_1.png)

## Comparison Gallery - Forward Wave 3.2 Harmonic-Offset Probe Overlay

Included models: `wave3_2_clean_sequential_residual_offset_fw`, `wave3_2_harmonic_residual_offset_fw`.

![Forward Wave 3.2 Harmonic-Offset Probe Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave3_2.png)

## Comparison Gallery - Forward Wave 3.3 Curve-Aware Training Overlay

Included models: `wave3_3_curve_aware_pointwise_control_fw`, `wave3_3_raw_centered_shape_curve_aware_fw`, `wave3_3_raw_offset_curve_aware_fw`, `wave3_3_full_curve_composite_fw`.

![Forward Wave 3.3 Curve-Aware Training Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave3_3.png)

## Comparison Gallery - Forward Wave 4.1 Robust-Loss Overlay

Included models: `wave4_1_mae_robust_loss_fw`, `wave4_1_smooth_l1_robust_loss_fw`, `wave4_1_log_cosh_robust_loss_fw`.

![Forward Wave 4.1 Robust-Loss Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave4_1.png)

## Comparison Gallery - Forward Wave 4.2 Quantile Probabilistic Overlay

Included models: `wave4_2_quantile_p10_p50_p90_fw`, `wave4_2_gaussian_nll_fw`.

![Forward Wave 4.2 Quantile Probabilistic Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave4_2.png)

## Comparison Gallery - Forward Wave 4.3 Mixture Density Overlay

Included models: `wave4_3_mixture_density_k2_fw`, `wave4_3_mixture_density_k3_fw`.

![Forward Wave 4.3 Mixture Density Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave4_3_mixture_density.png)

## Comparison Gallery - Forward Wave 4.4 Latent State Hysteresis Overlay

Included models: `wave4_4_gru_latent_offset_residual_fw`, `wave4_4_causal_tcn_latent_offset_residual_fw`.

![Forward Wave 4.4 Latent State Hysteresis Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave4_4_latent_state_hysteresis.png)

## Comparison Gallery - Forward Wave 3 Harmonic Prior Residual Registry Overlay

Included models: `wave5_1_harmonic_prior_pointwise_control_fw`, `wave5_1_harmonic_prior_smooth_l1_structured_fw`.

![Forward Wave 3 Harmonic Prior Residual Registry Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_wave5_1_harmonic_prior_residual.png)

## Comparison Gallery - Forward Wave52b Offset Harmonic Guided Registry Overlay

Included models: `wave52b_offset_centered_shape_harmonic_Fw`.

![Forward Wave52b Offset Harmonic Guided Registry Overlay TE Curve Verification Pipeline comparison](assets/comparisons/a_fw_wave_offs_harm_guid_reg_bd35ddc75a.png)

## Comparison Gallery - Forward Polished Model Development Registry Overlay

Included models: `polished_feedforward_Fw`, `polished_harmonic_regression_Fw`, `polished_periodic_mlp_Fw`, `polished_residual_harmonic_mlp_Fw`, `polished_tree_Fw`, `polished_periodic_mlp_harmonic_Fw`, `polished_temporal_convolution_Fw`, `polished_gru_sequence_Fw`, `polished_lstm_sequence_Fw`, `polished_periodic_temporal_convolution_Fw`, `polished_periodic_gru_sequence_Fw`, `polished_periodic_lstm_sequence_Fw`, `polished_residual_harmonic_gru_sequence_sparse_rcim_Fw`, `polished_residual_harmonic_gru_sequence_dense240_Fw`, `polished_residual_harmonic_gru_sequence_dense360_Fw`, `polished_residual_harmonic_lstm_sequence_sparse_rcim_Fw`, `polished_residual_harmonic_lstm_sequence_dense240_Fw`, `polished_residual_harmonic_lstm_sequence_dense360_Fw`, `polished_wave3_1_sequential_residual_offset_probe_Fw`, `polished_wave3_2_clean_sequential_residual_offset_Fw`, `polished_wave3_2_harmonic_residual_offset_Fw`, `polished_wave3_3_curve_aware_pointwise_control_Fw`, `polished_wave3_3_raw_centered_shape_curve_aware_Fw`, `polished_wave3_3_raw_offset_curve_aware_Fw`, `polished_wave3_3_full_curve_composite_Fw`, `polished_wave4_1_mae_robust_loss_Fw`, `polished_wave4_1_smooth_l1_robust_loss_Fw`, `polished_wave4_1_log_cosh_robust_loss_Fw`, `polished_wave4_2_quantile_p10_p50_p90_Fw`, `polished_wave4_2_gaussian_nll_Fw`, `polished_wave4_3_mixture_density_k2_Fw`, `polished_wave4_3_mixture_density_k3_Fw`, `polished_wave4_4_gru_latent_offset_residual_Fw`, `polished_wave4_4_causal_tcn_latent_offset_residual_Fw`, `polished_wave5_1_harmonic_prior_pointwise_control_Fw`, `polished_wave5_1_harmonic_prior_smooth_l1_structured_Fw`.

![Forward Polished Model Development Registry Overlay TE Curve Verification Pipeline comparison](assets/comparisons/auto_forward_polished_model_development_registry.png)

## Comparison Gallery - Forward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay

Included models: `rcim_model_bank_reproduction_best_fw`, `harmonic_regression_fw`, `periodic_mlp_harmonic_fw`, `tree_fw`.

![Forward RCIM Model-Bank Reproduction And Screened Wave 1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_track1_screened_wave1.png)

## Comparison Gallery - Forward Reference Tree And Wave 2.1 Overlay

Included models: `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`, `tree_fw`, `temporal_convolution_fw`, `gru_sequence_fw`, `lstm_sequence_fw`, `periodic_temporal_convolution_fw`, `periodic_gru_sequence_fw`, `periodic_lstm_sequence_fw`.

![Forward Reference Tree And Wave 2.1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference_tree_wave2.png)

## Comparison Gallery - Forward Reference Tree And Wave 2.3 Overlay

Included models: `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`, `tree_fw`, `residual_harmonic_gru_sequence_sparse_rcim_Fw`, `residual_harmonic_gru_sequence_dense240_Fw`, `residual_harmonic_gru_sequence_dense360_Fw`, `residual_harmonic_lstm_sequence_sparse_rcim_Fw`, `residual_harmonic_lstm_sequence_dense240_Fw`, `residual_harmonic_lstm_sequence_dense360_Fw`.

![Forward Reference Tree And Wave 2.3 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference_tree_wave2c.png)

## Comparison Gallery - Forward Reference Tree And Wave 3.1 Overlay

Included models: `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`, `tree_fw`, `wave3_1_sequential_residual_offset_probe_fw`.

![Forward Reference Tree And Wave 3.1 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference_tree_wave3_1.png)

## Comparison Gallery - Forward Reference Tree And Wave 3.3 Overlay

Included models: `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`, `tree_fw`, `wave3_3_curve_aware_pointwise_control_fw`, `wave3_3_raw_centered_shape_curve_aware_fw`, `wave3_3_raw_offset_curve_aware_fw`, `wave3_3_full_curve_composite_fw`.

![Forward Reference Tree And Wave 3.3 Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference_tree_wave3_3.png)

## Comparison Gallery - Forward Reference Tree And Wave 4 series Overlay

Included models: `paper_retuned_best_Fw`, `rcim_model_bank_reproduction_best_fw`, `tree_fw`, `wave4_1_mae_robust_loss_fw`, `wave4_1_smooth_l1_robust_loss_fw`, `wave4_1_log_cosh_robust_loss_fw`.

![Forward Reference Tree And Wave 4 series Overlay TE Curve Verification Pipeline comparison](assets/comparisons/forward_reference_tree_wave4_1.png)

## Output Artifacts

- output directory: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-07-05-11-32-46__track2_multi_model_curve_comparison_report`;
- summary YAML: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-07-05-11-32-46__track2_multi_model_curve_comparison_report\track2_multi_model_curve_comparison_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-07-05-11-32-46__track2_multi_model_curve_comparison_report\track2_multi_model_curve_comparison_metrics.csv`;
- report Markdown: `doc\reports\analysis\te_curve_verification_pipeline\02_visual_reports\dataset_surface_report\simplified_dataset\forward\overlay\[2026-07-04]\track2_multi_model_curve_comparison_report.md`.
