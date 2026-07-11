# Wave3 3 Raw Centered Shape Curve Aware Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-18-25-23__te_wave3_3_raw_centered_shape_curve_aware_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=121-val_mae=0.00193931.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006741`
- val_mae: `0.001939`
- val_rmse: `0.002718`
- val_pointwise_loss: `0.005118`
- val_centered_curve_shape_loss: `0.004594`
- val_curve_offset_loss: `0.000524`
- val_curve_amplitude_loss: `0.032097`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.029097`
- val_structured_rmse: `0.034468`
- val_residual_offset_mean_abs: `0.029070`

## Test Metrics

- test_loss: `0.010487`
- test_mae: `0.002285`
- test_rmse: `0.003628`
- test_pointwise_loss: `0.008544`
- test_centered_curve_shape_loss: `0.005504`
- test_curve_offset_loss: `0.003040`
- test_curve_amplitude_loss: `0.042374`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.026420`
- test_structured_rmse: `0.032420`
- test_residual_offset_mean_abs: `0.026382`

## Interpretation

The held-out val error stayed finite with MAE=0.001939 deg and RMSE=0.002718 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002285 deg and RMSE=0.003628 deg, which indicates a numerically stable baseline run.
