# TE Curve Verification Pipeline Mean-Centered Collage Diagnostics Report

## Overview

This report tests whether the persistent vertical offset observed in
the `TE Curve Verification Pipeline` best-model collage hides stronger waveform tracking.
For each candidate and curve, the measured `TE` curve is centered by
its own mean and the predicted curve is centered by its own mean before
`MAE` and `RMSE` are recomputed.

This is a diagnostic post-prediction view. It does not train models,
change the dataset, or make mean-centering a deployable runtime
correction.

## Method

- candidates and representative curves match the best-model collage
  report structure;
- aggregate metrics are computed on the same deterministic four-curve
  selection used by the source collage report;
- this keeps the diagnostic directly comparable with the visual offset
  observed in the original collage PDF;
- raw `MAE`/`RMSE` are compared against metrics after subtracting each
  curve's own mean from truth and prediction separately.

## Top Mean-Centering Improvements

| Rank | Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | `harmonic_regression_global` | global | 0.031130 | 0.000888 | 97.1% | 0.031130 |
| 2 | `periodic_lstm_sequence_global` | global | 0.004495 | 0.000658 | 80.3% | 0.004492 |
| 3 | `periodic_temporal_convolution_global` | global | 0.003830 | 0.000906 | 75.9% | 0.003826 |
| 4 | `periodic_gru_sequence_global` | global | 0.003392 | 0.000854 | 70.3% | 0.003373 |
| 5 | `tree_global` | global | 0.004153 | 0.001080 | 67.3% | 0.004092 |
| 6 | `track1_best_Bw` | Bw | 0.006783 | 0.000805 | 64.6% | 0.006569 |
| 7 | `lstm_sequence_global` | global | 0.003451 | 0.001241 | 64.4% | 0.003419 |
| 8 | `periodic_gru_sequence_fw` | Fw | 0.003352 | 0.000997 | 64.2% | 0.003101 |
| 9 | `residual_harmonic_gru_sequence_sparse_rcim_global` | global | 0.003183 | 0.001123 | 63.4% | 0.003146 |
| 10 | `track1_best_Fw` | Fw | 0.002376 | 0.000731 | 62.7% | 0.002203 |
| 11 | `gru_sequence_global` | global | 0.003848 | 0.001383 | 61.0% | 0.003807 |
| 12 | `residual_harmonic_gru_sequence_sparse_rcim_Bw` | Bw | 0.003608 | 0.001459 | 60.9% | 0.003487 |

## Diagnostic Reading

- The persistent vertical offset is a material part of the raw `TE Curve Verification Pipeline`
  collage error for many candidates.
- `harmonic_regression_global` is the strongest offset example: its four-curve
  average `MAE` drops from `0.031130` deg to `0.000888` deg after
  mean-centering.
- Several global temporal candidates also show strong shape tracking after
  offset removal, including `periodic_lstm_sequence_global`,
  `periodic_temporal_convolution_global`, and `periodic_gru_sequence_global`.
- Dense `Wave 2.3` residual-harmonic temporal candidates improve much less than
  sparse `RCIM` variants, which means their visible error is not explained only
  by a vertical offset.
- This report should be read as a diagnostic signal for future calibration or
  curve-aware training. It does not authorize a non-causal runtime correction
  or a change to the pointwise test-rig input contract.

## Group Metrics

### Forward Reference Best Models

| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| --- | --- | ---: | ---: | ---: | ---: |
| `paper_original_best_Fw` | Fw | 0.002042 | 0.000724 | 52.9% | 0.001899 |
| `paper_retuned_best_Fw` | Fw | 0.002193 | 0.000722 | 57.5% | 0.002004 |
| `track1_best_Fw` | Fw | 0.002376 | 0.000731 | 62.7% | 0.002203 |

### Forward Wave 1 Family Best Models

| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| --- | --- | ---: | ---: | ---: | ---: |
| `feedforward_fw` | Fw | 0.002770 | 0.001805 | 34.4% | 0.002174 |
| `harmonic_regression_fw` | Fw | 0.002586 | 0.001124 | 54.4% | 0.002122 |
| `periodic_mlp_fw` | Fw | 0.002627 | 0.001279 | 46.3% | 0.002120 |
| `residual_harmonic_mlp_fw` | Fw | 0.002570 | 0.001333 | 47.6% | 0.001909 |
| `tree_fw` | Fw | 0.003639 | 0.001425 | 55.4% | 0.003279 |
| `periodic_mlp_harmonic_fw` | Fw | 0.002627 | 0.001279 | 46.3% | 0.002120 |

### Backward Reference Best Models

| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| --- | --- | ---: | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | Bw | 0.004126 | 0.002324 | 40.4% | 0.003400 |
| `track1_best_Bw` | Bw | 0.006783 | 0.000805 | 64.6% | 0.006569 |

### Backward Wave 1 Family Best Models

| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| --- | --- | ---: | ---: | ---: | ---: |
| `feedforward_bw` | Bw | 0.002600 | 0.001738 | 28.5% | 0.002147 |
| `harmonic_regression_bw` | Bw | 0.004031 | 0.001483 | 53.1% | 0.003856 |
| `periodic_mlp_bw` | Bw | 0.002925 | 0.001676 | 39.7% | 0.002726 |
| `residual_harmonic_mlp_bw` | Bw | 0.003001 | 0.001457 | 42.4% | 0.002628 |
| `tree_bw` | Bw | 0.003341 | 0.001503 | 49.0% | 0.002985 |
| `periodic_mlp_harmonic_bw` | Bw | 0.003865 | 0.001628 | 59.9% | 0.003812 |

### Forward Wave 2.1 Temporal Family Best Models

| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| --- | --- | ---: | ---: | ---: | ---: |
| `temporal_convolution_fw` | Fw | 0.004003 | 0.001715 | 52.0% | 0.003650 |
| `gru_sequence_fw` | Fw | 0.003093 | 0.001763 | 39.7% | 0.002537 |
| `lstm_sequence_fw` | Fw | 0.003131 | 0.001817 | 38.3% | 0.002510 |
| `periodic_temporal_convolution_fw` | Fw | 0.003739 | 0.001385 | 59.3% | 0.003578 |
| `periodic_gru_sequence_fw` | Fw | 0.003352 | 0.000997 | 64.2% | 0.003101 |
| `periodic_lstm_sequence_fw` | Fw | 0.002999 | 0.001237 | 55.4% | 0.002690 |

### Backward Wave 2.1 Temporal Family Best Models

| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| --- | --- | ---: | ---: | ---: | ---: |
| `temporal_convolution_bw` | Bw | 0.003361 | 0.001677 | 44.5% | 0.002956 |
| `gru_sequence_bw` | Bw | 0.003402 | 0.001707 | 50.0% | 0.003161 |
| `lstm_sequence_bw` | Bw | 0.002850 | 0.001729 | 40.6% | 0.002491 |
| `periodic_temporal_convolution_bw` | Bw | 0.003276 | 0.001522 | 50.0% | 0.003094 |
| `periodic_gru_sequence_bw` | Bw | 0.003020 | 0.001004 | 45.7% | 0.002681 |
| `periodic_lstm_sequence_bw` | Bw | 0.002122 | 0.000935 | 45.9% | 0.001929 |

### Forward Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| --- | --- | ---: | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_Fw` | Fw | 0.002791 | 0.001330 | 43.0% | 0.002348 |
| `residual_harmonic_gru_sequence_dense240_Fw` | Fw | 0.006660 | 0.006259 | 5.9% | 0.001800 |
| `residual_harmonic_gru_sequence_dense360_Fw` | Fw | 0.007889 | 0.007254 | 7.9% | 0.002573 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Fw` | Fw | 0.002726 | 0.001301 | 40.3% | 0.002052 |
| `residual_harmonic_lstm_sequence_dense240_Fw` | Fw | 0.006996 | 0.006259 | 10.2% | 0.002699 |
| `residual_harmonic_lstm_sequence_dense360_Fw` | Fw | 0.007889 | 0.006987 | 11.2% | 0.003096 |

### Backward Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| --- | --- | ---: | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_Bw` | Bw | 0.003608 | 0.001459 | 60.9% | 0.003487 |
| `residual_harmonic_gru_sequence_dense240_Bw` | Bw | 0.009116 | 0.008347 | 8.0% | 0.005168 |
| `residual_harmonic_gru_sequence_dense360_Bw` | Bw | 0.008917 | 0.008601 | 3.1% | 0.002430 |
| `residual_harmonic_lstm_sequence_sparse_rcim_Bw` | Bw | 0.002943 | 0.001481 | 48.2% | 0.002685 |
| `residual_harmonic_lstm_sequence_dense240_Bw` | Bw | 0.007183 | 0.006446 | 10.2% | 0.003384 |
| `residual_harmonic_lstm_sequence_dense360_Bw` | Bw | 0.009855 | 0.009533 | 3.1% | 0.002784 |

### Global Wave 1 Family Best Models

| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| --- | --- | ---: | ---: | ---: | ---: |
| `feedforward_global` | global | 0.002527 | 0.001264 | 37.1% | 0.002208 |
| `harmonic_regression_global` | global | 0.031130 | 0.000888 | 97.1% | 0.031130 |
| `periodic_mlp_global` | global | 0.002478 | 0.001246 | 43.2% | 0.002199 |
| `residual_harmonic_mlp_global` | global | 0.003028 | 0.001240 | 59.3% | 0.002963 |
| `tree_global` | global | 0.004153 | 0.001080 | 67.3% | 0.004092 |
| `periodic_mlp_harmonic_global` | global | 0.003384 | 0.000993 | 54.9% | 0.003252 |

### Global Wave 2.1 Temporal Family Best Models

| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| --- | --- | ---: | ---: | ---: | ---: |
| `temporal_convolution_global` | global | 0.002982 | 0.001473 | 43.5% | 0.002755 |
| `gru_sequence_global` | global | 0.003848 | 0.001383 | 61.0% | 0.003807 |
| `lstm_sequence_global` | global | 0.003451 | 0.001241 | 64.4% | 0.003419 |
| `periodic_temporal_convolution_global` | global | 0.003830 | 0.000906 | 75.9% | 0.003826 |
| `periodic_gru_sequence_global` | global | 0.003392 | 0.000854 | 70.3% | 0.003373 |
| `periodic_lstm_sequence_global` | global | 0.004495 | 0.000658 | 80.3% | 0.004492 |

### Global Wave 2.3 Residual Harmonic Temporal Models

| Candidate | Surface | Raw MAE | Centered MAE | Improvement | Offset |
| --- | --- | ---: | ---: | ---: | ---: |
| `residual_harmonic_gru_sequence_sparse_rcim_global` | global | 0.003183 | 0.001123 | 63.4% | 0.003146 |
| `residual_harmonic_gru_sequence_dense240_global` | global | 0.007160 | 0.005633 | 18.8% | 0.004367 |
| `residual_harmonic_gru_sequence_dense360_global` | global | 0.007630 | 0.007037 | 7.5% | 0.003301 |
| `residual_harmonic_lstm_sequence_sparse_rcim_global` | global | 0.002533 | 0.001097 | 44.7% | 0.002362 |
| `residual_harmonic_lstm_sequence_dense240_global` | global | 0.006656 | 0.005380 | 16.7% | 0.004190 |
| `residual_harmonic_lstm_sequence_dense360_global` | global | 0.008495 | 0.007968 | 6.1% | 0.002246 |

## Mean-Centered Collage Gallery - Forward Reference Best Models

paper_original_best_Fw:

![paper_original_best_Fw mean-centered curve-verification collage](assets/forward_reference/paper_original_best_fw.png)

paper_retuned_best_Fw:

![paper_retuned_best_Fw mean-centered curve-verification collage](assets/forward_reference/paper_retuned_best_fw.png)

## Mean-Centered Collage Gallery - Forward Reference Best Models Continued

track1_best_Fw:

![track1_best_Fw mean-centered curve-verification collage](assets/forward_reference/track1_best_fw.png)

## Mean-Centered Collage Gallery - Forward Wave 1 Family Best Models

feedforward_fw:

![feedforward_fw mean-centered curve-verification collage](assets/forward_wave1/feedforward_fw.png)

harmonic_regression_fw:

![harmonic_regression_fw mean-centered curve-verification collage](assets/forward_wave1/harmonic_regression_fw.png)

## Mean-Centered Collage Gallery - Forward Wave 1 Family Best Models Continued

periodic_mlp_fw:

![periodic_mlp_fw mean-centered curve-verification collage](assets/forward_wave1/periodic_mlp_fw.png)

residual_harmonic_mlp_fw:

![residual_harmonic_mlp_fw mean-centered curve-verification collage](assets/forward_wave1/residual_harmonic_mlp_fw.png)

## Mean-Centered Collage Gallery - Forward Wave 1 Family Best Models Continued 2

tree_fw:

![tree_fw mean-centered curve-verification collage](assets/forward_wave1/tree_fw.png)

periodic_mlp_harmonic_fw:

![periodic_mlp_harmonic_fw mean-centered curve-verification collage](assets/forward_wave1/periodic_mlp_harmonic_fw.png)

## Mean-Centered Collage Gallery - Backward Reference Best Models

paper_retuned_best_Bw:

![paper_retuned_best_Bw mean-centered curve-verification collage](assets/backward_reference/paper_retuned_best_bw.png)

track1_best_Bw:

![track1_best_Bw mean-centered curve-verification collage](assets/backward_reference/track1_best_bw.png)

## Mean-Centered Collage Gallery - Backward Wave 1 Family Best Models

feedforward_bw:

![feedforward_bw mean-centered curve-verification collage](assets/backward_wave1/feedforward_bw.png)

harmonic_regression_bw:

![harmonic_regression_bw mean-centered curve-verification collage](assets/backward_wave1/harmonic_regression_bw.png)

## Mean-Centered Collage Gallery - Backward Wave 1 Family Best Models Continued

periodic_mlp_bw:

![periodic_mlp_bw mean-centered curve-verification collage](assets/backward_wave1/periodic_mlp_bw.png)

residual_harmonic_mlp_bw:

![residual_harmonic_mlp_bw mean-centered curve-verification collage](assets/backward_wave1/residual_harmonic_mlp_bw.png)

## Mean-Centered Collage Gallery - Backward Wave 1 Family Best Models Continued 2

tree_bw:

![tree_bw mean-centered curve-verification collage](assets/backward_wave1/tree_bw.png)

periodic_mlp_harmonic_bw:

![periodic_mlp_harmonic_bw mean-centered curve-verification collage](assets/backward_wave1/periodic_mlp_harmonic_bw.png)

## Mean-Centered Collage Gallery - Forward Wave 2.1 Temporal Family Best Models

temporal_convolution_fw:

![temporal_convolution_fw mean-centered curve-verification collage](assets/forward_wave2/temporal_convolution_fw.png)

gru_sequence_fw:

![gru_sequence_fw mean-centered curve-verification collage](assets/forward_wave2/gru_sequence_fw.png)

## Mean-Centered Collage Gallery - Forward Wave 2.1 Temporal Family Best Models Continued

lstm_sequence_fw:

![lstm_sequence_fw mean-centered curve-verification collage](assets/forward_wave2/lstm_sequence_fw.png)

periodic_temporal_convolution_fw:

![periodic_temporal_convolution_fw mean-centered curve-verification collage](assets/forward_wave2/periodic_temporal_convolution_fw.png)

## Mean-Centered Collage Gallery - Forward Wave 2.1 Temporal Family Best Models Continued 2

periodic_gru_sequence_fw:

![periodic_gru_sequence_fw mean-centered curve-verification collage](assets/forward_wave2/periodic_gru_sequence_fw.png)

periodic_lstm_sequence_fw:

![periodic_lstm_sequence_fw mean-centered curve-verification collage](assets/forward_wave2/periodic_lstm_sequence_fw.png)

## Mean-Centered Collage Gallery - Backward Wave 2.1 Temporal Family Best Models

temporal_convolution_bw:

![temporal_convolution_bw mean-centered curve-verification collage](assets/backward_wave2/temporal_convolution_bw.png)

gru_sequence_bw:

![gru_sequence_bw mean-centered curve-verification collage](assets/backward_wave2/gru_sequence_bw.png)

## Mean-Centered Collage Gallery - Backward Wave 2.1 Temporal Family Best Models Continued

lstm_sequence_bw:

![lstm_sequence_bw mean-centered curve-verification collage](assets/backward_wave2/lstm_sequence_bw.png)

periodic_temporal_convolution_bw:

![periodic_temporal_convolution_bw mean-centered curve-verification collage](assets/backward_wave2/periodic_temporal_convolution_bw.png)

## Mean-Centered Collage Gallery - Backward Wave 2.1 Temporal Family Best Models Continued 2

periodic_gru_sequence_bw:

![periodic_gru_sequence_bw mean-centered curve-verification collage](assets/backward_wave2/periodic_gru_sequence_bw.png)

periodic_lstm_sequence_bw:

![periodic_lstm_sequence_bw mean-centered curve-verification collage](assets/backward_wave2/periodic_lstm_sequence_bw.png)

## Mean-Centered Collage Gallery - Forward Wave 2.3 Residual Harmonic Temporal Models

residual_harmonic_gru_sequence_sparse_rcim_Fw:

![residual_harmonic_gru_sequence_sparse_rcim_Fw mean-centered curve-verification collage](assets/forward_wave2c/residual_harmonic_gru_sequence_sparse_rcim_fw.png)

residual_harmonic_gru_sequence_dense240_Fw:

![residual_harmonic_gru_sequence_dense240_Fw mean-centered curve-verification collage](assets/forward_wave2c/residual_harmonic_gru_sequence_dense240_fw.png)

## Mean-Centered Collage Gallery - Forward Wave 2.3 Residual Harmonic Temporal Models Continued

residual_harmonic_gru_sequence_dense360_Fw:

![residual_harmonic_gru_sequence_dense360_Fw mean-centered curve-verification collage](assets/forward_wave2c/residual_harmonic_gru_sequence_dense360_fw.png)

residual_harmonic_lstm_sequence_sparse_rcim_Fw:

![residual_harmonic_lstm_sequence_sparse_rcim_Fw mean-centered curve-verification collage](assets/forward_wave2c/residual_harmonic_lstm_sequence_sparse_rcim_fw.png)

## Mean-Centered Collage Gallery - Forward Wave 2.3 Residual Harmonic Temporal Models Continued 2

residual_harmonic_lstm_sequence_dense240_Fw:

![residual_harmonic_lstm_sequence_dense240_Fw mean-centered curve-verification collage](assets/forward_wave2c/residual_harmonic_lstm_sequence_dense240_fw.png)

residual_harmonic_lstm_sequence_dense360_Fw:

![residual_harmonic_lstm_sequence_dense360_Fw mean-centered curve-verification collage](assets/forward_wave2c/residual_harmonic_lstm_sequence_dense360_fw.png)

## Mean-Centered Collage Gallery - Backward Wave 2.3 Residual Harmonic Temporal Models

residual_harmonic_gru_sequence_sparse_rcim_Bw:

![residual_harmonic_gru_sequence_sparse_rcim_Bw mean-centered curve-verification collage](assets/backward_wave2c/residual_harmonic_gru_sequence_sparse_rcim_bw.png)

residual_harmonic_gru_sequence_dense240_Bw:

![residual_harmonic_gru_sequence_dense240_Bw mean-centered curve-verification collage](assets/backward_wave2c/residual_harmonic_gru_sequence_dense240_bw.png)

## Mean-Centered Collage Gallery - Backward Wave 2.3 Residual Harmonic Temporal Models Continued

residual_harmonic_gru_sequence_dense360_Bw:

![residual_harmonic_gru_sequence_dense360_Bw mean-centered curve-verification collage](assets/backward_wave2c/residual_harmonic_gru_sequence_dense360_bw.png)

residual_harmonic_lstm_sequence_sparse_rcim_Bw:

![residual_harmonic_lstm_sequence_sparse_rcim_Bw mean-centered curve-verification collage](assets/backward_wave2c/residual_harmonic_lstm_sequence_sparse_rcim_bw.png)

## Mean-Centered Collage Gallery - Backward Wave 2.3 Residual Harmonic Temporal Models Continued 2

residual_harmonic_lstm_sequence_dense240_Bw:

![residual_harmonic_lstm_sequence_dense240_Bw mean-centered curve-verification collage](assets/backward_wave2c/residual_harmonic_lstm_sequence_dense240_bw.png)

residual_harmonic_lstm_sequence_dense360_Bw:

![residual_harmonic_lstm_sequence_dense360_Bw mean-centered curve-verification collage](assets/backward_wave2c/residual_harmonic_lstm_sequence_dense360_bw.png)

## Mean-Centered Collage Gallery - Global Wave 1 Family Best Models

feedforward_global:

![feedforward_global mean-centered curve-verification collage](assets/global_wave1/feedforward_global.png)

harmonic_regression_global:

![harmonic_regression_global mean-centered curve-verification collage](assets/global_wave1/harmonic_regression_global.png)

## Mean-Centered Collage Gallery - Global Wave 1 Family Best Models Continued

periodic_mlp_global:

![periodic_mlp_global mean-centered curve-verification collage](assets/global_wave1/periodic_mlp_global.png)

residual_harmonic_mlp_global:

![residual_harmonic_mlp_global mean-centered curve-verification collage](assets/global_wave1/residual_harmonic_mlp_global.png)

## Mean-Centered Collage Gallery - Global Wave 1 Family Best Models Continued 2

tree_global:

![tree_global mean-centered curve-verification collage](assets/global_wave1/tree_global.png)

periodic_mlp_harmonic_global:

![periodic_mlp_harmonic_global mean-centered curve-verification collage](assets/global_wave1/periodic_mlp_harmonic_global.png)

## Mean-Centered Collage Gallery - Global Wave 2.1 Temporal Family Best Models

temporal_convolution_global:

![temporal_convolution_global mean-centered curve-verification collage](assets/global_wave2/temporal_convolution_global.png)

gru_sequence_global:

![gru_sequence_global mean-centered curve-verification collage](assets/global_wave2/gru_sequence_global.png)

## Mean-Centered Collage Gallery - Global Wave 2.1 Temporal Family Best Models Continued

lstm_sequence_global:

![lstm_sequence_global mean-centered curve-verification collage](assets/global_wave2/lstm_sequence_global.png)

periodic_temporal_convolution_global:

![periodic_temporal_convolution_global mean-centered curve-verification collage](assets/global_wave2/periodic_temporal_convolution_global.png)

## Mean-Centered Collage Gallery - Global Wave 2.1 Temporal Family Best Models Continued 2

periodic_gru_sequence_global:

![periodic_gru_sequence_global mean-centered curve-verification collage](assets/global_wave2/periodic_gru_sequence_global.png)

periodic_lstm_sequence_global:

![periodic_lstm_sequence_global mean-centered curve-verification collage](assets/global_wave2/periodic_lstm_sequence_global.png)

## Mean-Centered Collage Gallery - Global Wave 2.3 Residual Harmonic Temporal Models

residual_harmonic_gru_sequence_sparse_rcim_global:

![residual_harmonic_gru_sequence_sparse_rcim_global mean-centered curve-verification collage](assets/global_wave2c/residual_harmonic_gru_sequence_sparse_rcim_global.png)

residual_harmonic_gru_sequence_dense240_global:

![residual_harmonic_gru_sequence_dense240_global mean-centered curve-verification collage](assets/global_wave2c/residual_harmonic_gru_sequence_dense240_global.png)

## Mean-Centered Collage Gallery - Global Wave 2.3 Residual Harmonic Temporal Models Continued

residual_harmonic_gru_sequence_dense360_global:

![residual_harmonic_gru_sequence_dense360_global mean-centered curve-verification collage](assets/global_wave2c/residual_harmonic_gru_sequence_dense360_global.png)

residual_harmonic_lstm_sequence_sparse_rcim_global:

![residual_harmonic_lstm_sequence_sparse_rcim_global mean-centered curve-verification collage](assets/global_wave2c/residual_harmonic_lstm_sequence_sparse_rcim_global.png)

## Mean-Centered Collage Gallery - Global Wave 2.3 Residual Harmonic Temporal Models Continued 2

residual_harmonic_lstm_sequence_dense240_global:

![residual_harmonic_lstm_sequence_dense240_global mean-centered curve-verification collage](assets/global_wave2c/residual_harmonic_lstm_sequence_dense240_global.png)

residual_harmonic_lstm_sequence_dense360_global:

![residual_harmonic_lstm_sequence_dense360_global mean-centered curve-verification collage](assets/global_wave2c/residual_harmonic_lstm_sequence_dense360_global.png)

## Output Artifacts

- output directory: `output\validation_checks\track2_mean_centered_collage_report\2026-06-02-13-33-14__track2_mean_centered_collage_report`;
- summary YAML: `output\validation_checks\track2_mean_centered_collage_report\2026-06-02-13-33-14__track2_mean_centered_collage_report\track2_mean_centered_collage_summary.yaml`;
- candidate metrics CSV: `output\validation_checks\track2_mean_centered_collage_report\2026-06-02-13-33-14__track2_mean_centered_collage_report\track2_mean_centered_candidate_metrics.csv`;
- per-curve metrics CSV: `output\validation_checks\track2_mean_centered_collage_report\2026-06-02-13-33-14__track2_mean_centered_collage_report\track2_mean_centered_per_curve_metrics.csv`;
- report Markdown: `doc\reports\analysis\track2\mean_centered_collage_report\[2026-06-02]\track2_mean_centered_collage_report.md`;
- styled PDF: generated from the Markdown report with
  `python -B scripts/reports/pdf/run_report_pipeline.py`.
