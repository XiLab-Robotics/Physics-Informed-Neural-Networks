# Wave3 2 Clean Sequential Residual Offset Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values`
- Model Family: `wave3_2_clean_sequential_residual_offset_fw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-06-08__te_wave3_2_clean_sequential_residual_offset_fw__polished_actual_values/checkpoints/sequential_residual_offset_probe-epoch=153-val_mae=0.00216939.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005784`
- val_mae: `0.002169`
- val_rmse: `0.002998`
- val_pointwise_loss: `0.005784`
- val_centered_curve_shape_loss: `0.005396`
- val_curve_offset_loss: `0.000388`
- val_curve_amplitude_loss: `0.056716`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.022926`
- val_base_rmse: `0.027897`
- val_residual_offset_mean_abs: `0.022886`

## Test Metrics

- test_loss: `0.006647`
- test_mae: `0.002288`
- test_rmse: `0.003346`
- test_pointwise_loss: `0.006647`
- test_centered_curve_shape_loss: `0.006187`
- test_curve_offset_loss: `0.000460`
- test_curve_amplitude_loss: `0.062612`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.021776`
- test_base_rmse: `0.026928`
- test_residual_offset_mean_abs: `0.021688`

## Interpretation

The held-out val error stayed finite with MAE=0.002169 deg and RMSE=0.002998 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002288 deg and RMSE=0.003346 deg, which indicates a numerically stable baseline run.
