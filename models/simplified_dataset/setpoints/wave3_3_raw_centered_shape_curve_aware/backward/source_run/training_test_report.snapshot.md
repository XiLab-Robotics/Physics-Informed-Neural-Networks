# Wave3 3 Raw Centered Shape Curve Aware Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-16-42-36__te_wave3_3_raw_centered_shape_curve_aware_bw__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=122-val_mae=0.00357800.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.012859`
- val_mae: `0.003578`
- val_rmse: `0.004403`
- val_pointwise_loss: `0.010617`
- val_centered_curve_shape_loss: `0.006342`
- val_curve_offset_loss: `0.004275`
- val_curve_amplitude_loss: `0.042509`
- val_sparse_harmonic_shape_loss: `0.000150`
- val_structured_mae: `0.030866`
- val_structured_rmse: `0.036158`
- val_residual_offset_mean_abs: `0.030435`

## Test Metrics

- test_loss: `0.009271`
- test_mae: `0.003398`
- test_rmse: `0.004115`
- test_pointwise_loss: `0.008139`
- test_centered_curve_shape_loss: `0.003204`
- test_curve_offset_loss: `0.004936`
- test_curve_amplitude_loss: `0.017711`
- test_sparse_harmonic_shape_loss: `6.927560e-05`
- test_structured_mae: `0.033876`
- test_structured_rmse: `0.038758`
- test_residual_offset_mean_abs: `0.033393`

## Interpretation

The held-out val error stayed finite with MAE=0.003578 deg and RMSE=0.004403 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003398 deg and RMSE=0.004115 deg, which indicates a numerically stable baseline run.
