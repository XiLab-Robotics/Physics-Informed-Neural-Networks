# Wave3 2 Clean Sequential Residual Offset Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values`
- Model Family: `wave3_2_clean_sequential_residual_offset_bw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-22-37-04__te_wave3_2_clean_sequential_residual_offset_bw__polished_actual_values/checkpoints/sequential_residual_offset_probe-epoch=127-val_mae=0.00219453.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005873`
- val_mae: `0.002195`
- val_rmse: `0.003030`
- val_pointwise_loss: `0.005873`
- val_centered_curve_shape_loss: `0.005397`
- val_curve_offset_loss: `0.000475`
- val_curve_amplitude_loss: `0.059123`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.023037`
- val_base_rmse: `0.027988`
- val_residual_offset_mean_abs: `0.022714`

## Test Metrics

- test_loss: `0.006740`
- test_mae: `0.002312`
- test_rmse: `0.003384`
- test_pointwise_loss: `0.006740`
- test_centered_curve_shape_loss: `0.006286`
- test_curve_offset_loss: `0.000453`
- test_curve_amplitude_loss: `0.065486`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.021887`
- test_base_rmse: `0.026964`
- test_residual_offset_mean_abs: `0.021585`

## Interpretation

The held-out val error stayed finite with MAE=0.002195 deg and RMSE=0.003030 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002312 deg and RMSE=0.003384 deg, which indicates a numerically stable baseline run.
