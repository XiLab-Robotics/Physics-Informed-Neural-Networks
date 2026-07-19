# Wave3 3 Raw Centered Shape Curve Aware Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-19-14-45__te_wave3_3_raw_centered_shape_curve_aware_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=210-val_mae=0.00182815.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006372`
- val_mae: `0.001828`
- val_rmse: `0.002582`
- val_pointwise_loss: `0.004789`
- val_centered_curve_shape_loss: `0.004481`
- val_curve_offset_loss: `0.000308`
- val_curve_amplitude_loss: `0.032691`
- val_sparse_harmonic_shape_loss: `9.892472e-05`
- val_structured_mae: `0.004656`
- val_structured_rmse: `0.005734`
- val_residual_offset_mean_abs: `0.003944`

## Test Metrics

- test_loss: `0.007478`
- test_mae: `0.001966`
- test_rmse: `0.003011`
- test_pointwise_loss: `0.005637`
- test_centered_curve_shape_loss: `0.005215`
- test_curve_offset_loss: `0.000421`
- test_curve_amplitude_loss: `0.037040`
- test_sparse_harmonic_shape_loss: `0.000107`
- test_structured_mae: `0.005003`
- test_structured_rmse: `0.006452`
- test_residual_offset_mean_abs: `0.004132`

## Interpretation

The held-out val error stayed finite with MAE=0.001828 deg and RMSE=0.002582 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001966 deg and RMSE=0.003011 deg, which indicates a numerically stable baseline run.
