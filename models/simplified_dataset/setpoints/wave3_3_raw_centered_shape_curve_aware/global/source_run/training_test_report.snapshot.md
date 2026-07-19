# Wave3 3 Raw Centered Shape Curve Aware Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints`
- Model Family: `wave3_3_raw_centered_shape_curve_aware_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_centered_shape_curve_aware/2026-07-11-15-43-36__te_wave3_3_raw_centered_shape_curve_aware_global__simplified_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=114-val_mae=0.00357026.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.013132`
- val_mae: `0.003570`
- val_rmse: `0.004451`
- val_pointwise_loss: `0.010893`
- val_centered_curve_shape_loss: `0.006332`
- val_curve_offset_loss: `0.004562`
- val_curve_amplitude_loss: `0.045383`
- val_sparse_harmonic_shape_loss: `0.000150`
- val_structured_mae: `0.034304`
- val_structured_rmse: `0.039765`
- val_residual_offset_mean_abs: `0.034659`

## Test Metrics

- test_loss: `0.009966`
- test_mae: `0.003524`
- test_rmse: `0.004312`
- test_pointwise_loss: `0.008849`
- test_centered_curve_shape_loss: `0.003162`
- test_curve_offset_loss: `0.005687`
- test_curve_amplitude_loss: `0.019376`
- test_sparse_harmonic_shape_loss: `6.853860e-05`
- test_structured_mae: `0.036059`
- test_structured_rmse: `0.041412`
- test_residual_offset_mean_abs: `0.036674`

## Interpretation

The held-out val error stayed finite with MAE=0.003570 deg and RMSE=0.004451 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003524 deg and RMSE=0.004312 deg, which indicates a numerically stable baseline run.
