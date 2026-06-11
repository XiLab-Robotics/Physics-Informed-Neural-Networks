# Track 2 Multi-Model Curve Comparison Report

## Overview

This report compares representative `Track 2` TE curves by overlaying
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
| `track1_best_Fw` | `rcim_track1` | Fw | 0.003014 | 0.003204 | 6.819 |

### Forward Wave 1 Family Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_fw` | `wave1_current_registry` | Fw | 0.003404 | 0.003855 | 7.551 |
| `harmonic_regression_fw` | `wave1_current_registry` | Fw | 0.003230 | 0.003494 | 7.185 |
| `periodic_mlp_fw` | `wave1_current_registry` | Fw | 0.003254 | 0.003553 | 7.232 |
| `residual_harmonic_mlp_fw` | `wave1_current_registry` | Fw | 0.003273 | 0.003563 | 7.266 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.003053 | 0.003395 | 6.731 |
| `periodic_mlp_harmonic_fw` | `wave1_periodic_mlp_harmonic_campaign` | Fw | 0.003254 | 0.003553 | 7.232 |

### Backward Reference Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.003675 | 0.004284 | 7.572 |
| `track1_best_Bw` | `rcim_track1` | Bw | 0.005027 | 0.005212 | 11.860 |

### Backward Wave 1 Family Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_bw` | `wave1_current_registry` | Bw | 0.003586 | 0.004023 | 7.832 |
| `harmonic_regression_bw` | `wave1_current_registry` | Bw | 0.003678 | 0.004012 | 8.058 |
| `periodic_mlp_bw` | `wave1_current_registry` | Bw | 0.003574 | 0.004006 | 7.807 |
| `residual_harmonic_mlp_bw` | `wave1_current_registry` | Bw | 0.003536 | 0.003874 | 7.728 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.003258 | 0.003651 | 7.051 |
| `periodic_mlp_harmonic_bw` | `wave1_periodic_mlp_harmonic_campaign` | Bw | 0.003583 | 0.003925 | 7.875 |

### Forward Wave 2 Temporal Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.003603 | 0.004031 | 8.028 |
| `gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003330 | 0.003762 | 7.378 |
| `lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003366 | 0.003800 | 7.450 |
| `periodic_temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.003335 | 0.003708 | 7.404 |
| `periodic_gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003186 | 0.003438 | 7.077 |
| `periodic_lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003266 | 0.003550 | 7.258 |

### Backward Wave 2 Temporal Model Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.003742 | 0.004166 | 8.184 |
| `gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.003626 | 0.004082 | 7.907 |
| `lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.003555 | 0.003985 | 7.767 |
| `periodic_temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.003628 | 0.003987 | 7.979 |
| `periodic_gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002392 | 0.002639 | 5.466 |
| `periodic_lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002625 | 0.002877 | 6.013 |

### Forward Wave 2C Residual Harmonic Temporal Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003194 | 0.003499 | 7.083 |
| `residual_harmonic_gru_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.006983 | 0.009275 | 15.722 |
| `residual_harmonic_gru_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007869 | 0.010574 | 17.740 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003229 | 0.003533 | 7.164 |
| `residual_harmonic_lstm_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007042 | 0.009370 | 15.868 |
| `residual_harmonic_lstm_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007731 | 0.010235 | 17.430 |

### Backward Wave 2C Residual Harmonic Temporal Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.003502 | 0.003857 | 7.654 |
| `residual_harmonic_gru_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.008984 | 0.012987 | 20.358 |
| `residual_harmonic_gru_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.009370 | 0.013165 | 21.267 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.003440 | 0.003793 | 7.510 |
| `residual_harmonic_lstm_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.007367 | 0.009945 | 16.660 |
| `residual_harmonic_lstm_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.010268 | 0.014769 | 23.355 |

### Forward Track 2F Offset-Aware Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `sequential_residual_offset_probe_Fw` | `track2f_offset_aware_probe_registry` | Fw | 0.003377 | 0.003799 | 7.487 |

### Backward Track 2F Offset-Aware Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `sequential_residual_offset_probe_Bw` | `track2f_offset_aware_probe_registry` | Bw | 0.003636 | 0.004065 | 7.952 |

### Forward Track 2F-Bis Harmonic-Offset Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `track2f_bis_clean_sequential_residual_offset_Fw` | `track2f_bis_harmonic_offset_probe_registry` | Fw | 0.003439 | 0.003870 | 7.632 |
| `track2f_bis_harmonic_residual_offset_Fw` | `track2f_bis_harmonic_offset_probe_registry` | Fw | 0.002850 | 0.003108 | 6.286 |

### Backward Track 2F-Bis Harmonic-Offset Probe Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `track2f_bis_clean_sequential_residual_offset_Bw` | `track2f_bis_harmonic_offset_probe_registry` | Bw | 0.003541 | 0.003971 | 7.732 |
| `track2f_bis_harmonic_residual_offset_Bw` | `track2f_bis_harmonic_offset_probe_registry` | Bw | 0.003331 | 0.003671 | 7.261 |

### Forward Track 2G Curve-Aware Training Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `track2g_curve_aware_pointwise_control_Fw` | `track2g_curve_aware_training_registry` | Fw | 0.003362 | 0.003612 | 7.474 |
| `track2g_curve_aware_raw_centered_shape_Fw` | `track2g_curve_aware_training_registry` | Fw | 0.003174 | 0.003429 | 7.047 |
| `track2g_curve_aware_raw_offset_Fw` | `track2g_curve_aware_training_registry` | Fw | 0.003269 | 0.003588 | 7.268 |
| `track2g_curve_aware_full_curve_composite_Fw` | `track2g_curve_aware_training_registry` | Fw | 0.003251 | 0.003515 | 7.209 |

### Backward Track 2G Curve-Aware Training Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `track2g_curve_aware_pointwise_control_Bw` | `track2g_curve_aware_training_registry` | Bw | 0.003436 | 0.003761 | 7.538 |
| `track2g_curve_aware_raw_centered_shape_Bw` | `track2g_curve_aware_training_registry` | Bw | 0.003465 | 0.003790 | 7.582 |
| `track2g_curve_aware_raw_offset_Bw` | `track2g_curve_aware_training_registry` | Bw | 0.003469 | 0.003799 | 7.608 |
| `track2g_curve_aware_full_curve_composite_Bw` | `track2g_curve_aware_training_registry` | Bw | 0.003510 | 0.003897 | 7.683 |

### Forward Track 2H Robust-Loss Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `track2h_mae_robust_Fw` | `track2h_dispersion_aware_modeling_registry` | Fw | 0.003134 | 0.003382 | 6.956 |
| `track2h_smooth_l1_robust_Fw` | `track2h_dispersion_aware_modeling_registry` | Fw | 0.003300 | 0.003545 | 7.342 |
| `track2h_log_cosh_robust_Fw` | `track2h_dispersion_aware_modeling_registry` | Fw | 0.003344 | 0.003595 | 7.427 |

### Backward Track 2H Robust-Loss Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `track2h_mae_robust_Bw` | `track2h_dispersion_aware_modeling_registry` | Bw | 0.003433 | 0.003750 | 7.506 |
| `track2h_smooth_l1_robust_Bw` | `track2h_dispersion_aware_modeling_registry` | Bw | 0.003078 | 0.003403 | 6.676 |
| `track2h_log_cosh_robust_Bw` | `track2h_dispersion_aware_modeling_registry` | Bw | 0.003486 | 0.003811 | 7.628 |

### Forward Track 1 And Screened Wave 1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `track1_best_Fw` | `rcim_track1` | Fw | 0.003014 | 0.003204 | 6.819 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.003053 | 0.003395 | 6.731 |
| `harmonic_regression_fw` | `wave1_current_registry` | Fw | 0.003230 | 0.003494 | 7.185 |
| `periodic_mlp_fw` | `wave1_current_registry` | Fw | 0.003254 | 0.003553 | 7.232 |

### Backward Track 1 And Screened Wave 1 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `track1_best_Bw` | `rcim_track1` | Bw | 0.005027 | 0.005212 | 11.860 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.003258 | 0.003651 | 7.051 |
| `residual_harmonic_mlp_bw` | `wave1_current_registry` | Bw | 0.003536 | 0.003874 | 7.728 |
| `periodic_mlp_bw` | `wave1_current_registry` | Bw | 0.003574 | 0.004006 | 7.807 |

### Forward Reference Tree And Wave 2 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `track1_best_Fw` | `rcim_track1` | Fw | 0.003014 | 0.003204 | 6.819 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.003053 | 0.003395 | 6.731 |
| `temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.003603 | 0.004031 | 8.028 |
| `gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003330 | 0.003762 | 7.378 |
| `lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003366 | 0.003800 | 7.450 |
| `periodic_temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.003335 | 0.003708 | 7.404 |
| `periodic_gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003186 | 0.003438 | 7.077 |
| `periodic_lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003266 | 0.003550 | 7.258 |

### Backward Reference Tree And Wave 2 Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.003675 | 0.004284 | 7.572 |
| `track1_best_Bw` | `rcim_track1` | Bw | 0.005027 | 0.005212 | 11.860 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.003258 | 0.003651 | 7.051 |
| `temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.003742 | 0.004166 | 8.184 |
| `gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.003626 | 0.004082 | 7.907 |
| `lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.003555 | 0.003985 | 7.767 |
| `periodic_temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.003628 | 0.003987 | 7.979 |
| `periodic_gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002392 | 0.002639 | 5.466 |
| `periodic_lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002625 | 0.002877 | 6.013 |

### Forward Reference Tree And Wave 2C Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `track1_best_Fw` | `rcim_track1` | Fw | 0.003014 | 0.003204 | 6.819 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.003053 | 0.003395 | 6.731 |
| `residual_harmonic_gru_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003194 | 0.003499 | 7.083 |
| `residual_harmonic_gru_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.006983 | 0.009275 | 15.722 |
| `residual_harmonic_gru_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007869 | 0.010574 | 17.740 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003229 | 0.003533 | 7.164 |
| `residual_harmonic_lstm_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007042 | 0.009370 | 15.868 |
| `residual_harmonic_lstm_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007731 | 0.010235 | 17.430 |

### Backward Reference Tree And Wave 2C Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.003675 | 0.004284 | 7.572 |
| `track1_best_Bw` | `rcim_track1` | Bw | 0.005027 | 0.005212 | 11.860 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.003258 | 0.003651 | 7.051 |
| `residual_harmonic_gru_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.003502 | 0.003857 | 7.654 |
| `residual_harmonic_gru_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.008984 | 0.012987 | 20.358 |
| `residual_harmonic_gru_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.009370 | 0.013165 | 21.267 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.003440 | 0.003793 | 7.510 |
| `residual_harmonic_lstm_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.007367 | 0.009945 | 16.660 |
| `residual_harmonic_lstm_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.010268 | 0.014769 | 23.355 |

### Forward Reference Tree And Track 2F Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `track1_best_Fw` | `rcim_track1` | Fw | 0.003014 | 0.003204 | 6.819 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.003053 | 0.003395 | 6.731 |
| `sequential_residual_offset_probe_Fw` | `track2f_offset_aware_probe_registry` | Fw | 0.003377 | 0.003799 | 7.487 |

### Backward Reference Tree And Track 2F Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.003675 | 0.004284 | 7.572 |
| `track1_best_Bw` | `rcim_track1` | Bw | 0.005027 | 0.005212 | 11.860 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.003258 | 0.003651 | 7.051 |
| `sequential_residual_offset_probe_Bw` | `track2f_offset_aware_probe_registry` | Bw | 0.003636 | 0.004065 | 7.952 |

### Forward Reference Tree And Track 2G Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `track1_best_Fw` | `rcim_track1` | Fw | 0.003014 | 0.003204 | 6.819 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.003053 | 0.003395 | 6.731 |
| `track2g_curve_aware_pointwise_control_Fw` | `track2g_curve_aware_training_registry` | Fw | 0.003362 | 0.003612 | 7.474 |
| `track2g_curve_aware_raw_centered_shape_Fw` | `track2g_curve_aware_training_registry` | Fw | 0.003174 | 0.003429 | 7.047 |
| `track2g_curve_aware_raw_offset_Fw` | `track2g_curve_aware_training_registry` | Fw | 0.003269 | 0.003588 | 7.268 |
| `track2g_curve_aware_full_curve_composite_Fw` | `track2g_curve_aware_training_registry` | Fw | 0.003251 | 0.003515 | 7.209 |

### Backward Reference Tree And Track 2G Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.003675 | 0.004284 | 7.572 |
| `track1_best_Bw` | `rcim_track1` | Bw | 0.005027 | 0.005212 | 11.860 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.003258 | 0.003651 | 7.051 |
| `track2g_curve_aware_pointwise_control_Bw` | `track2g_curve_aware_training_registry` | Bw | 0.003436 | 0.003761 | 7.538 |
| `track2g_curve_aware_raw_centered_shape_Bw` | `track2g_curve_aware_training_registry` | Bw | 0.003465 | 0.003790 | 7.582 |
| `track2g_curve_aware_raw_offset_Bw` | `track2g_curve_aware_training_registry` | Bw | 0.003469 | 0.003799 | 7.608 |
| `track2g_curve_aware_full_curve_composite_Bw` | `track2g_curve_aware_training_registry` | Bw | 0.003510 | 0.003897 | 7.683 |

### Forward Reference Tree And Track 2H Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `track1_best_Fw` | `rcim_track1` | Fw | 0.003014 | 0.003204 | 6.819 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.003053 | 0.003395 | 6.731 |
| `track2h_mae_robust_Fw` | `track2h_dispersion_aware_modeling_registry` | Fw | 0.003134 | 0.003382 | 6.956 |
| `track2h_smooth_l1_robust_Fw` | `track2h_dispersion_aware_modeling_registry` | Fw | 0.003300 | 0.003545 | 7.342 |
| `track2h_log_cosh_robust_Fw` | `track2h_dispersion_aware_modeling_registry` | Fw | 0.003344 | 0.003595 | 7.427 |

### Backward Reference Tree And Track 2H Overlay

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.003675 | 0.004284 | 7.572 |
| `track1_best_Bw` | `rcim_track1` | Bw | 0.005027 | 0.005212 | 11.860 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.003258 | 0.003651 | 7.051 |
| `track2h_mae_robust_Bw` | `track2h_dispersion_aware_modeling_registry` | Bw | 0.003433 | 0.003750 | 7.506 |
| `track2h_smooth_l1_robust_Bw` | `track2h_dispersion_aware_modeling_registry` | Bw | 0.003078 | 0.003403 | 6.676 |
| `track2h_log_cosh_robust_Bw` | `track2h_dispersion_aware_modeling_registry` | Bw | 0.003486 | 0.003811 | 7.628 |

## Comparison Gallery - Forward Reference Model Overlay

Included models: `paper_original_best_Fw`, `paper_retuned_best_Fw`, `track1_best_Fw`.

![Forward Reference Model Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_reference.png)

## Comparison Gallery - Forward Wave 1 Family Model Overlay

Included models: `feedforward_fw`, `harmonic_regression_fw`, `periodic_mlp_fw`, `residual_harmonic_mlp_fw`, `tree_fw`, `periodic_mlp_harmonic_fw`.

![Forward Wave 1 Family Model Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_wave1.png)

## Comparison Gallery - Backward Reference Model Overlay

Included models: `paper_retuned_best_Bw`, `track1_best_Bw`.

![Backward Reference Model Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_reference.png)

## Comparison Gallery - Backward Wave 1 Family Model Overlay

Included models: `feedforward_bw`, `harmonic_regression_bw`, `periodic_mlp_bw`, `residual_harmonic_mlp_bw`, `tree_bw`, `periodic_mlp_harmonic_bw`.

![Backward Wave 1 Family Model Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_wave1.png)

## Comparison Gallery - Forward Wave 2 Temporal Model Overlay

Included models: `temporal_convolution_fw`, `gru_sequence_fw`, `lstm_sequence_fw`, `periodic_temporal_convolution_fw`, `periodic_gru_sequence_fw`, `periodic_lstm_sequence_fw`.

![Forward Wave 2 Temporal Model Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_wave2.png)

## Comparison Gallery - Backward Wave 2 Temporal Model Overlay

Included models: `temporal_convolution_bw`, `gru_sequence_bw`, `lstm_sequence_bw`, `periodic_temporal_convolution_bw`, `periodic_gru_sequence_bw`, `periodic_lstm_sequence_bw`.

![Backward Wave 2 Temporal Model Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_wave2.png)

## Comparison Gallery - Forward Wave 2C Residual Harmonic Temporal Overlay

Included models: `residual_harmonic_gru_sequence_sparse_rcim_Fw`, `residual_harmonic_gru_sequence_dense240_Fw`, `residual_harmonic_gru_sequence_dense360_Fw`, `residual_harmonic_lstm_sequence_sparse_rcim_Fw`, `residual_harmonic_lstm_sequence_dense240_Fw`, `residual_harmonic_lstm_sequence_dense360_Fw`.

![Forward Wave 2C Residual Harmonic Temporal Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_wave2c.png)

## Comparison Gallery - Backward Wave 2C Residual Harmonic Temporal Overlay

Included models: `residual_harmonic_gru_sequence_sparse_rcim_Bw`, `residual_harmonic_gru_sequence_dense240_Bw`, `residual_harmonic_gru_sequence_dense360_Bw`, `residual_harmonic_lstm_sequence_sparse_rcim_Bw`, `residual_harmonic_lstm_sequence_dense240_Bw`, `residual_harmonic_lstm_sequence_dense360_Bw`.

![Backward Wave 2C Residual Harmonic Temporal Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_wave2c.png)

## Comparison Gallery - Forward Track 2F Offset-Aware Probe Overlay

Included models: `sequential_residual_offset_probe_Fw`.

![Forward Track 2F Offset-Aware Probe Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_track2f.png)

## Comparison Gallery - Backward Track 2F Offset-Aware Probe Overlay

Included models: `sequential_residual_offset_probe_Bw`.

![Backward Track 2F Offset-Aware Probe Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_track2f.png)

## Comparison Gallery - Forward Track 2F-Bis Harmonic-Offset Probe Overlay

Included models: `track2f_bis_clean_sequential_residual_offset_Fw`, `track2f_bis_harmonic_residual_offset_Fw`.

![Forward Track 2F-Bis Harmonic-Offset Probe Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_track2f_bis.png)

## Comparison Gallery - Backward Track 2F-Bis Harmonic-Offset Probe Overlay

Included models: `track2f_bis_clean_sequential_residual_offset_Bw`, `track2f_bis_harmonic_residual_offset_Bw`.

![Backward Track 2F-Bis Harmonic-Offset Probe Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_track2f_bis.png)

## Comparison Gallery - Forward Track 2G Curve-Aware Training Overlay

Included models: `track2g_curve_aware_pointwise_control_Fw`, `track2g_curve_aware_raw_centered_shape_Fw`, `track2g_curve_aware_raw_offset_Fw`, `track2g_curve_aware_full_curve_composite_Fw`.

![Forward Track 2G Curve-Aware Training Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_track2g.png)

## Comparison Gallery - Backward Track 2G Curve-Aware Training Overlay

Included models: `track2g_curve_aware_pointwise_control_Bw`, `track2g_curve_aware_raw_centered_shape_Bw`, `track2g_curve_aware_raw_offset_Bw`, `track2g_curve_aware_full_curve_composite_Bw`.

![Backward Track 2G Curve-Aware Training Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_track2g.png)

## Comparison Gallery - Forward Track 2H Robust-Loss Overlay

Included models: `track2h_mae_robust_Fw`, `track2h_smooth_l1_robust_Fw`, `track2h_log_cosh_robust_Fw`.

![Forward Track 2H Robust-Loss Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_track2h.png)

## Comparison Gallery - Backward Track 2H Robust-Loss Overlay

Included models: `track2h_mae_robust_Bw`, `track2h_smooth_l1_robust_Bw`, `track2h_log_cosh_robust_Bw`.

![Backward Track 2H Robust-Loss Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_track2h.png)

## Comparison Gallery - Forward Track 1 And Screened Wave 1 Overlay

Included models: `track1_best_Fw`, `tree_fw`, `harmonic_regression_fw`, `periodic_mlp_fw`.

![Forward Track 1 And Screened Wave 1 Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_track1_screened_wave1.png)

## Comparison Gallery - Backward Track 1 And Screened Wave 1 Overlay

Included models: `track1_best_Bw`, `tree_bw`, `residual_harmonic_mlp_bw`, `periodic_mlp_bw`.

![Backward Track 1 And Screened Wave 1 Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_track1_screened_wave1.png)

## Comparison Gallery - Forward Reference Tree And Wave 2 Overlay

Included models: `paper_retuned_best_Fw`, `track1_best_Fw`, `tree_fw`, `temporal_convolution_fw`, `gru_sequence_fw`, `lstm_sequence_fw`, `periodic_temporal_convolution_fw`, `periodic_gru_sequence_fw`, `periodic_lstm_sequence_fw`.

![Forward Reference Tree And Wave 2 Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_reference_tree_wave2.png)

## Comparison Gallery - Backward Reference Tree And Wave 2 Overlay

Included models: `paper_retuned_best_Bw`, `track1_best_Bw`, `tree_bw`, `temporal_convolution_bw`, `gru_sequence_bw`, `lstm_sequence_bw`, `periodic_temporal_convolution_bw`, `periodic_gru_sequence_bw`, `periodic_lstm_sequence_bw`.

![Backward Reference Tree And Wave 2 Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_reference_tree_wave2.png)

## Comparison Gallery - Forward Reference Tree And Wave 2C Overlay

Included models: `paper_retuned_best_Fw`, `track1_best_Fw`, `tree_fw`, `residual_harmonic_gru_sequence_sparse_rcim_Fw`, `residual_harmonic_gru_sequence_dense240_Fw`, `residual_harmonic_gru_sequence_dense360_Fw`, `residual_harmonic_lstm_sequence_sparse_rcim_Fw`, `residual_harmonic_lstm_sequence_dense240_Fw`, `residual_harmonic_lstm_sequence_dense360_Fw`.

![Forward Reference Tree And Wave 2C Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_reference_tree_wave2c.png)

## Comparison Gallery - Backward Reference Tree And Wave 2C Overlay

Included models: `paper_retuned_best_Bw`, `track1_best_Bw`, `tree_bw`, `residual_harmonic_gru_sequence_sparse_rcim_Bw`, `residual_harmonic_gru_sequence_dense240_Bw`, `residual_harmonic_gru_sequence_dense360_Bw`, `residual_harmonic_lstm_sequence_sparse_rcim_Bw`, `residual_harmonic_lstm_sequence_dense240_Bw`, `residual_harmonic_lstm_sequence_dense360_Bw`.

![Backward Reference Tree And Wave 2C Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_reference_tree_wave2c.png)

## Comparison Gallery - Forward Reference Tree And Track 2F Overlay

Included models: `paper_retuned_best_Fw`, `track1_best_Fw`, `tree_fw`, `sequential_residual_offset_probe_Fw`.

![Forward Reference Tree And Track 2F Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_reference_tree_track2f.png)

## Comparison Gallery - Backward Reference Tree And Track 2F Overlay

Included models: `paper_retuned_best_Bw`, `track1_best_Bw`, `tree_bw`, `sequential_residual_offset_probe_Bw`.

![Backward Reference Tree And Track 2F Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_reference_tree_track2f.png)

## Comparison Gallery - Forward Reference Tree And Track 2G Overlay

Included models: `paper_retuned_best_Fw`, `track1_best_Fw`, `tree_fw`, `track2g_curve_aware_pointwise_control_Fw`, `track2g_curve_aware_raw_centered_shape_Fw`, `track2g_curve_aware_raw_offset_Fw`, `track2g_curve_aware_full_curve_composite_Fw`.

![Forward Reference Tree And Track 2G Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_reference_tree_track2g.png)

## Comparison Gallery - Backward Reference Tree And Track 2G Overlay

Included models: `paper_retuned_best_Bw`, `track1_best_Bw`, `tree_bw`, `track2g_curve_aware_pointwise_control_Bw`, `track2g_curve_aware_raw_centered_shape_Bw`, `track2g_curve_aware_raw_offset_Bw`, `track2g_curve_aware_full_curve_composite_Bw`.

![Backward Reference Tree And Track 2G Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_reference_tree_track2g.png)

## Comparison Gallery - Forward Reference Tree And Track 2H Overlay

Included models: `paper_retuned_best_Fw`, `track1_best_Fw`, `tree_fw`, `track2h_mae_robust_Fw`, `track2h_smooth_l1_robust_Fw`, `track2h_log_cosh_robust_Fw`.

![Forward Reference Tree And Track 2H Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/forward_reference_tree_track2h.png)

## Comparison Gallery - Backward Reference Tree And Track 2H Overlay

Included models: `paper_retuned_best_Bw`, `track1_best_Bw`, `tree_bw`, `track2h_mae_robust_Bw`, `track2h_smooth_l1_robust_Bw`, `track2h_log_cosh_robust_Bw`.

![Backward Reference Tree And Track 2H Overlay Track 2 comparison](../../../../../../output/validation_checks/track2_multi_model_curve_comparison_report/2026-06-11-20-39-59__track2_multi_model_curve_comparison_report/comparisons/backward_reference_tree_track2h.png)

## Output Artifacts

- output directory: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-06-11-20-39-59__track2_multi_model_curve_comparison_report`;
- summary YAML: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-06-11-20-39-59__track2_multi_model_curve_comparison_report\track2_multi_model_curve_comparison_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_multi_model_curve_comparison_report\2026-06-11-20-39-59__track2_multi_model_curve_comparison_report\track2_multi_model_curve_comparison_metrics.csv`;
- report Markdown: `doc\reports\analysis\track2\multi_model_curve_comparison_report\[2026-06-11]\track2_multi_model_curve_comparison_report.md`.
