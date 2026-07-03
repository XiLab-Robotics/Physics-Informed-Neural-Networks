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
| `paper_original_best_Fw` | `rcim_original` | Fw | 0.002769 | 0.002951 | 6.250 |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `track1_best_Fw` | `rcim_track1` | Fw | 0.003014 | 0.003204 | 6.819 |

### Forward Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_fw` | `wave1_current_registry` | Fw | 0.003404 | 0.003855 | 7.551 |
| `harmonic_regression_fw` | `wave1_current_registry` | Fw | 0.003230 | 0.003494 | 7.185 |
| `periodic_mlp_fw` | `wave1_current_registry` | Fw | 0.003254 | 0.003553 | 7.232 |
| `residual_harmonic_mlp_fw` | `wave1_current_registry` | Fw | 0.003273 | 0.003563 | 7.266 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.003053 | 0.003395 | 6.731 |
| `periodic_mlp_harmonic_fw` | `wave1_periodic_mlp_harmonic_campaign` | Fw | 0.003254 | 0.003553 | 7.232 |

### Backward Reference Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.003675 | 0.004284 | 7.572 |
| `track1_best_Bw` | `rcim_track1` | Bw | 0.005027 | 0.005212 | 11.860 |

### Backward Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_bw` | `wave1_current_registry` | Bw | 0.003586 | 0.004023 | 7.832 |
| `harmonic_regression_bw` | `wave1_current_registry` | Bw | 0.003678 | 0.004012 | 8.058 |
| `periodic_mlp_bw` | `wave1_current_registry` | Bw | 0.003574 | 0.004006 | 7.807 |
| `residual_harmonic_mlp_bw` | `wave1_current_registry` | Bw | 0.003536 | 0.003874 | 7.728 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.003258 | 0.003651 | 7.051 |
| `periodic_mlp_harmonic_bw` | `wave1_periodic_mlp_harmonic_campaign` | Bw | 0.003583 | 0.003925 | 7.875 |

### Forward Wave 2.1 Temporal Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.003603 | 0.004031 | 8.028 |
| `gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003330 | 0.003762 | 7.378 |
| `lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003366 | 0.003800 | 7.450 |
| `periodic_temporal_convolution_fw` | `wave2_temporal_entry_registry` | Fw | 0.003335 | 0.003708 | 7.404 |
| `periodic_gru_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003186 | 0.003438 | 7.077 |
| `periodic_lstm_sequence_fw` | `wave2_temporal_entry_registry` | Fw | 0.003266 | 0.003550 | 7.258 |

### Backward Wave 2.1 Temporal Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.003742 | 0.004166 | 8.184 |
| `gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.003626 | 0.004082 | 7.907 |
| `lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.003555 | 0.003985 | 7.767 |
| `periodic_temporal_convolution_bw` | `wave2_temporal_entry_registry` | Bw | 0.003628 | 0.003987 | 7.979 |
| `periodic_gru_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002392 | 0.002639 | 5.466 |
| `periodic_lstm_sequence_bw` | `wave2_temporal_entry_registry` | Bw | 0.002625 | 0.002877 | 6.013 |

### Forward Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003194 | 0.003499 | 7.083 |
| `residual_harmonic_gru_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.006983 | 0.009275 | 15.722 |
| `residual_harmonic_gru_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007869 | 0.010574 | 17.740 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.003229 | 0.003533 | 7.164 |
| `residual_harmonic_lstm_sequence_dense240_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007042 | 0.009370 | 15.868 |
| `residual_harmonic_lstm_sequence_dense360_Fw` | `wave2c_residual_harmonic_temporal_registry` | Fw | 0.007731 | 0.010235 | 17.430 |

### Backward Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.003502 | 0.003857 | 7.654 |
| `residual_harmonic_gru_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.008984 | 0.012987 | 20.358 |
| `residual_harmonic_gru_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.009370 | 0.013165 | 21.267 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.003440 | 0.003793 | 7.510 |
| `residual_harmonic_lstm_sequence_dense240_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.007367 | 0.009945 | 16.660 |
| `residual_harmonic_lstm_sequence_dense360_Bw` | `wave2c_residual_harmonic_temporal_registry` | Bw | 0.010268 | 0.014769 | 23.355 |

### Global Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_global` | `wave1_current_registry` | global | 0.003465 | 0.003897 | 7.636 |
| `harmonic_regression_global` | `wave1_current_registry` | global | 0.018129 | 0.018330 | 41.458 |
| `periodic_mlp_global` | `wave1_current_registry` | global | 0.003447 | 0.003872 | 7.582 |
| `residual_harmonic_mlp_global` | `wave1_current_registry` | global | 0.003407 | 0.003822 | 7.486 |
| `tree_global` | `wave1_current_registry` | global | 0.003144 | 0.003533 | 6.854 |
| `periodic_mlp_harmonic_global` | `wave1_periodic_mlp_harmonic_campaign` | global | 0.003516 | 0.003810 | 7.779 |

### Global Wave 2.1 Temporal Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `temporal_convolution_global` | `wave2_temporal_entry_registry` | global | 0.003751 | 0.004183 | 8.295 |
| `gru_sequence_global` | `wave2_temporal_entry_registry` | global | 0.003591 | 0.004028 | 7.907 |
| `lstm_sequence_global` | `wave2_temporal_entry_registry` | global | 0.003480 | 0.003903 | 7.654 |
| `periodic_temporal_convolution_global` | `wave2_temporal_entry_registry` | global | 0.003506 | 0.003836 | 7.758 |
| `periodic_gru_sequence_global` | `wave2_temporal_entry_registry` | global | 0.002704 | 0.002949 | 6.139 |
| `periodic_lstm_sequence_global` | `wave2_temporal_entry_registry` | global | 0.002707 | 0.002958 | 6.120 |

### Global Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.003435 | 0.003784 | 7.571 |
| `residual_harmonic_gru_sequence_dense240_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.006660 | 0.009090 | 15.007 |
| `residual_harmonic_gru_sequence_dense360_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.008012 | 0.011416 | 18.090 |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.003368 | 0.003719 | 7.409 |
| `residual_harmonic_lstm_sequence_dense240_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.006419 | 0.008765 | 14.460 |
| `residual_harmonic_lstm_sequence_dense360_global` | `wave2c_residual_harmonic_temporal_registry` | global | 0.008810 | 0.013026 | 19.916 |

## Collage Gallery - Forward Reference Best Models

paper_original_best_Fw:

![paper_original_best_Fw curve-verification collage](assets/forward_reference/paper_original_best_fw.png)

paper_retuned_best_Fw:

![paper_retuned_best_Fw curve-verification collage](assets/forward_reference/paper_retuned_best_fw.png)

## Collage Gallery - Forward Reference Best Models Continued

track1_best_Fw:

![track1_best_Fw curve-verification collage](assets/forward_reference/track1_best_fw.png)

## Collage Gallery - Forward Wave 1 Family Best Models

feedforward_fw:

![feedforward_fw curve-verification collage](assets/forward_wave1/feedforward_fw.png)

harmonic_regression_fw:

![harmonic_regression_fw curve-verification collage](assets/forward_wave1/harmonic_regression_fw.png)

## Collage Gallery - Forward Wave 1 Family Best Models Continued

periodic_mlp_fw:

![periodic_mlp_fw curve-verification collage](assets/forward_wave1/periodic_mlp_fw.png)

residual_harmonic_mlp_fw:

![residual_harmonic_mlp_fw curve-verification collage](assets/forward_wave1/residual_harmonic_mlp_fw.png)

## Collage Gallery - Forward Wave 1 Family Best Models Continued 2

tree_fw:

![tree_fw curve-verification collage](assets/forward_wave1/tree_fw.png)

periodic_mlp_harmonic_fw:

![periodic_mlp_harmonic_fw curve-verification collage](assets/forward_wave1/periodic_mlp_harmonic_fw.png)

## Collage Gallery - Backward Reference Best Models

paper_retuned_best_Bw:

![paper_retuned_best_Bw curve-verification collage](assets/backward_reference/paper_retuned_best_bw.png)

track1_best_Bw:

![track1_best_Bw curve-verification collage](assets/backward_reference/track1_best_bw.png)

## Collage Gallery - Backward Wave 1 Family Best Models

feedforward_bw:

![feedforward_bw curve-verification collage](assets/backward_wave1/feedforward_bw.png)

harmonic_regression_bw:

![harmonic_regression_bw curve-verification collage](assets/backward_wave1/harmonic_regression_bw.png)

## Collage Gallery - Backward Wave 1 Family Best Models Continued

periodic_mlp_bw:

![periodic_mlp_bw curve-verification collage](assets/backward_wave1/periodic_mlp_bw.png)

residual_harmonic_mlp_bw:

![residual_harmonic_mlp_bw curve-verification collage](assets/backward_wave1/residual_harmonic_mlp_bw.png)

## Collage Gallery - Backward Wave 1 Family Best Models Continued 2

tree_bw:

![tree_bw curve-verification collage](assets/backward_wave1/tree_bw.png)

periodic_mlp_harmonic_bw:

![periodic_mlp_harmonic_bw curve-verification collage](assets/backward_wave1/periodic_mlp_harmonic_bw.png)

## Collage Gallery - Forward Wave 2.1 Temporal Family Best Models

temporal_convolution_fw:

![temporal_convolution_fw curve-verification collage](assets/forward_wave2/temporal_convolution_fw.png)

gru_sequence_fw:

![gru_sequence_fw curve-verification collage](assets/forward_wave2/gru_sequence_fw.png)

## Collage Gallery - Forward Wave 2.1 Temporal Family Best Models Continued

lstm_sequence_fw:

![lstm_sequence_fw curve-verification collage](assets/forward_wave2/lstm_sequence_fw.png)

periodic_temporal_convolution_fw:

![periodic_temporal_convolution_fw curve-verification collage](assets/forward_wave2/periodic_temporal_convolution_fw.png)

## Collage Gallery - Forward Wave 2.1 Temporal Family Best Models Continued 2

periodic_gru_sequence_fw:

![periodic_gru_sequence_fw curve-verification collage](assets/forward_wave2/periodic_gru_sequence_fw.png)

periodic_lstm_sequence_fw:

![periodic_lstm_sequence_fw curve-verification collage](assets/forward_wave2/periodic_lstm_sequence_fw.png)

## Collage Gallery - Backward Wave 2.1 Temporal Family Best Models

temporal_convolution_bw:

![temporal_convolution_bw curve-verification collage](assets/backward_wave2/temporal_convolution_bw.png)

gru_sequence_bw:

![gru_sequence_bw curve-verification collage](assets/backward_wave2/gru_sequence_bw.png)

## Collage Gallery - Backward Wave 2.1 Temporal Family Best Models Continued

lstm_sequence_bw:

![lstm_sequence_bw curve-verification collage](assets/backward_wave2/lstm_sequence_bw.png)

periodic_temporal_convolution_bw:

![periodic_temporal_convolution_bw curve-verification collage](assets/backward_wave2/periodic_temporal_convolution_bw.png)

## Collage Gallery - Backward Wave 2.1 Temporal Family Best Models Continued 2

periodic_gru_sequence_bw:

![periodic_gru_sequence_bw curve-verification collage](assets/backward_wave2/periodic_gru_sequence_bw.png)

periodic_lstm_sequence_bw:

![periodic_lstm_sequence_bw curve-verification collage](assets/backward_wave2/periodic_lstm_sequence_bw.png)

## Collage Gallery - Forward Wave 2.3 Residual Harmonic Temporal Models

residual_harmonic_gru_sequence_sparse_rcim_Fw:

![residual_harmonic_gru_sequence_sparse_rcim_Fw curve-verification collage](assets/forward_wave2c/residual_harmonic_gru_sequence_sparse_rcim_fw.png)

residual_harmonic_gru_sequence_dense240_Fw:

![residual_harmonic_gru_sequence_dense240_Fw curve-verification collage](assets/forward_wave2c/residual_harmonic_gru_sequence_dense240_fw.png)

## Collage Gallery - Forward Wave 2.3 Residual Harmonic Temporal Models Continued

residual_harmonic_gru_sequence_dense360_Fw:

![residual_harmonic_gru_sequence_dense360_Fw curve-verification collage](assets/forward_wave2c/residual_harmonic_gru_sequence_dense360_fw.png)

residual_harmonic_lstm_sequence_sparse_rcim_Fw:

![residual_harmonic_lstm_sequence_sparse_rcim_Fw curve-verification collage](assets/forward_wave2c/residual_harmonic_lstm_sequence_sparse_rcim_fw.png)

## Collage Gallery - Forward Wave 2.3 Residual Harmonic Temporal Models Continued 2

residual_harmonic_lstm_sequence_dense240_Fw:

![residual_harmonic_lstm_sequence_dense240_Fw curve-verification collage](assets/forward_wave2c/residual_harmonic_lstm_sequence_dense240_fw.png)

residual_harmonic_lstm_sequence_dense360_Fw:

![residual_harmonic_lstm_sequence_dense360_Fw curve-verification collage](assets/forward_wave2c/residual_harmonic_lstm_sequence_dense360_fw.png)

## Collage Gallery - Backward Wave 2.3 Residual Harmonic Temporal Models

residual_harmonic_gru_sequence_sparse_rcim_Bw:

![residual_harmonic_gru_sequence_sparse_rcim_Bw curve-verification collage](assets/backward_wave2c/residual_harmonic_gru_sequence_sparse_rcim_bw.png)

residual_harmonic_gru_sequence_dense240_Bw:

![residual_harmonic_gru_sequence_dense240_Bw curve-verification collage](assets/backward_wave2c/residual_harmonic_gru_sequence_dense240_bw.png)

## Collage Gallery - Backward Wave 2.3 Residual Harmonic Temporal Models Continued

residual_harmonic_gru_sequence_dense360_Bw:

![residual_harmonic_gru_sequence_dense360_Bw curve-verification collage](assets/backward_wave2c/residual_harmonic_gru_sequence_dense360_bw.png)

residual_harmonic_lstm_sequence_sparse_rcim_Bw:

![residual_harmonic_lstm_sequence_sparse_rcim_Bw curve-verification collage](assets/backward_wave2c/residual_harmonic_lstm_sequence_sparse_rcim_bw.png)

## Collage Gallery - Backward Wave 2.3 Residual Harmonic Temporal Models Continued 2

residual_harmonic_lstm_sequence_dense240_Bw:

![residual_harmonic_lstm_sequence_dense240_Bw curve-verification collage](assets/backward_wave2c/residual_harmonic_lstm_sequence_dense240_bw.png)

residual_harmonic_lstm_sequence_dense360_Bw:

![residual_harmonic_lstm_sequence_dense360_Bw curve-verification collage](assets/backward_wave2c/residual_harmonic_lstm_sequence_dense360_bw.png)

## Collage Gallery - Global Wave 1 Family Best Models

feedforward_global:

![feedforward_global curve-verification collage](assets/global_wave1/feedforward_global.png)

harmonic_regression_global:

![harmonic_regression_global curve-verification collage](assets/global_wave1/harmonic_regression_global.png)

## Collage Gallery - Global Wave 1 Family Best Models Continued

periodic_mlp_global:

![periodic_mlp_global curve-verification collage](assets/global_wave1/periodic_mlp_global.png)

residual_harmonic_mlp_global:

![residual_harmonic_mlp_global curve-verification collage](assets/global_wave1/residual_harmonic_mlp_global.png)

## Collage Gallery - Global Wave 1 Family Best Models Continued 2

tree_global:

![tree_global curve-verification collage](assets/global_wave1/tree_global.png)

periodic_mlp_harmonic_global:

![periodic_mlp_harmonic_global curve-verification collage](assets/global_wave1/periodic_mlp_harmonic_global.png)

## Collage Gallery - Global Wave 2.1 Temporal Family Best Models

temporal_convolution_global:

![temporal_convolution_global curve-verification collage](assets/global_wave2/temporal_convolution_global.png)

gru_sequence_global:

![gru_sequence_global curve-verification collage](assets/global_wave2/gru_sequence_global.png)

## Collage Gallery - Global Wave 2.1 Temporal Family Best Models Continued

lstm_sequence_global:

![lstm_sequence_global curve-verification collage](assets/global_wave2/lstm_sequence_global.png)

periodic_temporal_convolution_global:

![periodic_temporal_convolution_global curve-verification collage](assets/global_wave2/periodic_temporal_convolution_global.png)

## Collage Gallery - Global Wave 2.1 Temporal Family Best Models Continued 2

periodic_gru_sequence_global:

![periodic_gru_sequence_global curve-verification collage](assets/global_wave2/periodic_gru_sequence_global.png)

periodic_lstm_sequence_global:

![periodic_lstm_sequence_global curve-verification collage](assets/global_wave2/periodic_lstm_sequence_global.png)

## Collage Gallery - Global Wave 2.3 Residual Harmonic Temporal Models

residual_harmonic_gru_sequence_sparse_rcim_global:

![residual_harmonic_gru_sequence_sparse_rcim_global curve-verification collage](assets/global_wave2c/residual_harmonic_gru_sequence_sparse_rcim_global.png)

residual_harmonic_gru_sequence_dense240_global:

![residual_harmonic_gru_sequence_dense240_global curve-verification collage](assets/global_wave2c/residual_harmonic_gru_sequence_dense240_global.png)

## Collage Gallery - Global Wave 2.3 Residual Harmonic Temporal Models Continued

residual_harmonic_gru_sequence_dense360_global:

![residual_harmonic_gru_sequence_dense360_global curve-verification collage](assets/global_wave2c/residual_harmonic_gru_sequence_dense360_global.png)

residual_harmonic_lstm_sequence_sparse_rcim_global:

![residual_harmonic_lstm_sequence_sparse_rcim_global curve-verification collage](assets/global_wave2c/residual_harmonic_lstm_sequence_sparse_rcim_global.png)

## Collage Gallery - Global Wave 2.3 Residual Harmonic Temporal Models Continued 2

residual_harmonic_lstm_sequence_dense240_global:

![residual_harmonic_lstm_sequence_dense240_global curve-verification collage](assets/global_wave2c/residual_harmonic_lstm_sequence_dense240_global.png)

residual_harmonic_lstm_sequence_dense360_global:

![residual_harmonic_lstm_sequence_dense360_global curve-verification collage](assets/global_wave2c/residual_harmonic_lstm_sequence_dense360_global.png)

## Output Artifacts

- output directory: `output\validation_checks\track2_best_model_collage_report\2026-05-28-13-37-39__track2_best_model_collage_report`;
- summary YAML: `output\validation_checks\track2_best_model_collage_report\2026-05-28-13-37-39__track2_best_model_collage_report\track2_best_model_collage_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_best_model_collage_report\2026-05-28-13-37-39__track2_best_model_collage_report\track2_best_model_collage_metrics.csv`;
- report Markdown: `doc\reports\analysis\track2\best_model_collage_report\[2026-05-28]\track2_best_model_collage_report.md`.
