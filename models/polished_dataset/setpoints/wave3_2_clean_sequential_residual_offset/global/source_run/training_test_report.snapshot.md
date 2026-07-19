# Wave3 2 Clean Sequential Residual Offset Global Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints`
- Model Family: `wave3_2_clean_sequential_residual_offset_global`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-13-46-46__te_wave3_2_clean_sequential_residual_offset_global__polished_setpoints/checkpoints/sequential_residual_offset_probe-epoch=128-val_mae=0.00217355.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005838`
- val_mae: `0.002174`
- val_rmse: `0.003013`
- val_pointwise_loss: `0.005838`
- val_centered_curve_shape_loss: `0.005364`
- val_curve_offset_loss: `0.000473`
- val_curve_amplitude_loss: `0.063544`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.024005`
- val_base_rmse: `0.028408`
- val_residual_offset_mean_abs: `0.023769`

## Test Metrics

- test_loss: `0.009269`
- test_mae: `0.002454`
- test_rmse: `0.003851`
- test_pointwise_loss: `0.009269`
- test_centered_curve_shape_loss: `0.006277`
- test_curve_offset_loss: `0.002992`
- test_curve_amplitude_loss: `0.076547`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.022778`
- test_base_rmse: `0.027340`
- test_residual_offset_mean_abs: `0.022429`

## Interpretation

The held-out val error stayed finite with MAE=0.002174 deg and RMSE=0.003013 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002454 deg and RMSE=0.003851 deg, which indicates a numerically stable baseline run.
