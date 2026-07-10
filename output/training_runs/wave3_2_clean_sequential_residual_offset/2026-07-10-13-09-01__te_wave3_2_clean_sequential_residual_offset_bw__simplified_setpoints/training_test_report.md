# Wave3 2 Clean Sequential Residual Offset Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_bw__simplified_setpoints`
- Model Family: `wave3_2_clean_sequential_residual_offset_bw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-13-09-01__te_wave3_2_clean_sequential_residual_offset_bw__simplified_setpoints/checkpoints/sequential_residual_offset_probe-epoch=151-val_mae=0.00364800.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011367`
- val_mae: `0.003648`
- val_rmse: `0.004547`
- val_pointwise_loss: `0.011367`
- val_centered_curve_shape_loss: `0.007268`
- val_curve_offset_loss: `0.004099`
- val_curve_amplitude_loss: `0.078945`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.023149`
- val_base_rmse: `0.027939`
- val_residual_offset_mean_abs: `0.022885`

## Test Metrics

- test_loss: `0.008812`
- test_mae: `0.003486`
- test_rmse: `0.004293`
- test_pointwise_loss: `0.008812`
- test_centered_curve_shape_loss: `0.003971`
- test_curve_offset_loss: `0.004841`
- test_curve_amplitude_loss: `0.044570`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.025294`
- test_base_rmse: `0.029785`
- test_residual_offset_mean_abs: `0.025195`

## Interpretation

The held-out val error stayed finite with MAE=0.003648 deg and RMSE=0.004547 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003486 deg and RMSE=0.004293 deg, which indicates a numerically stable baseline run.
