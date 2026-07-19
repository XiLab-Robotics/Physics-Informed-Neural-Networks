# Wave3 2 Clean Sequential Residual Offset Global Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_global__simplified_setpoints`
- Model Family: `wave3_2_clean_sequential_residual_offset_global`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-12-38-46__te_wave3_2_clean_sequential_residual_offset_global__simplified_setpoints/checkpoints/sequential_residual_offset_probe-epoch=110-val_mae=0.00370701.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011787`
- val_mae: `0.003707`
- val_rmse: `0.004638`
- val_pointwise_loss: `0.011787`
- val_centered_curve_shape_loss: `0.007291`
- val_curve_offset_loss: `0.004495`
- val_curve_amplitude_loss: `0.074831`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.026261`
- val_base_rmse: `0.031393`
- val_residual_offset_mean_abs: `0.025801`

## Test Metrics

- test_loss: `0.009565`
- test_mae: `0.003636`
- test_rmse: `0.004490`
- test_pointwise_loss: `0.009565`
- test_centered_curve_shape_loss: `0.003994`
- test_curve_offset_loss: `0.005571`
- test_curve_amplitude_loss: `0.041659`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.028284`
- test_base_rmse: `0.033119`
- test_residual_offset_mean_abs: `0.028071`

## Interpretation

The held-out val error stayed finite with MAE=0.003707 deg and RMSE=0.004638 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003636 deg and RMSE=0.004490 deg, which indicates a numerically stable baseline run.
