# Wave3 3 Curve Aware Pointwise Control Global Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values`
- Model Family: `wave3_3_curve_aware_pointwise_control_global`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-12-56-24__te_wave3_3_curve_aware_pointwise_control_global__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=199-val_mae=0.00185032.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004829`
- val_mae: `0.001850`
- val_rmse: `0.002613`
- val_pointwise_loss: `0.004829`
- val_centered_curve_shape_loss: `0.004486`
- val_curve_offset_loss: `0.000343`
- val_curve_amplitude_loss: `0.034386`
- val_sparse_harmonic_shape_loss: `9.911418e-05`
- val_structured_mae: `0.010523`
- val_structured_rmse: `0.012527`
- val_residual_offset_mean_abs: `0.010181`

## Test Metrics

- test_loss: `0.005674`
- test_mae: `0.001987`
- test_rmse: `0.003027`
- test_pointwise_loss: `0.005674`
- test_centered_curve_shape_loss: `0.005267`
- test_curve_offset_loss: `0.000407`
- test_curve_amplitude_loss: `0.038834`
- test_sparse_harmonic_shape_loss: `0.000108`
- test_structured_mae: `0.011006`
- test_structured_rmse: `0.013549`
- test_residual_offset_mean_abs: `0.010596`

## Interpretation

The held-out val error stayed finite with MAE=0.001850 deg and RMSE=0.002613 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001987 deg and RMSE=0.003027 deg, which indicates a numerically stable baseline run.
