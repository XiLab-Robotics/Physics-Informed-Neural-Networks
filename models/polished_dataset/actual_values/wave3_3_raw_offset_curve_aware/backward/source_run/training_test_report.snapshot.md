# Wave3 3 Raw Offset Curve Aware Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_bw__polished_actual_values`
- Model Family: `wave3_3_raw_offset_curve_aware_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-12-02-57-47__te_wave3_3_raw_offset_curve_aware_bw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=199-val_mae=0.00184997.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004989`
- val_mae: `0.001850`
- val_rmse: `0.002607`
- val_pointwise_loss: `0.004844`
- val_centered_curve_shape_loss: `0.004522`
- val_curve_offset_loss: `0.000323`
- val_curve_amplitude_loss: `0.034229`
- val_sparse_harmonic_shape_loss: `9.995131e-05`
- val_structured_mae: `0.008455`
- val_structured_rmse: `0.010200`
- val_residual_offset_mean_abs: `0.008075`

## Test Metrics

- test_loss: `0.005824`
- test_mae: `0.001975`
- test_rmse: `0.003015`
- test_pointwise_loss: `0.005675`
- test_centered_curve_shape_loss: `0.005345`
- test_curve_offset_loss: `0.000331`
- test_curve_amplitude_loss: `0.038672`
- test_sparse_harmonic_shape_loss: `0.000108`
- test_structured_mae: `0.008371`
- test_structured_rmse: `0.010368`
- test_residual_offset_mean_abs: `0.007868`

## Interpretation

The held-out val error stayed finite with MAE=0.001850 deg and RMSE=0.002607 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001975 deg and RMSE=0.003015 deg, which indicates a numerically stable baseline run.
