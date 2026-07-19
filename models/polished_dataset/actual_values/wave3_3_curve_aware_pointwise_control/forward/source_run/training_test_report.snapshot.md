# Wave3 3 Curve Aware Pointwise Control Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values`
- Model Family: `wave3_3_curve_aware_pointwise_control_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_curve_aware_pointwise_control/2026-07-11-13-46-39__te_wave3_3_curve_aware_pointwise_control_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=256-val_mae=0.00183289.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004808`
- val_mae: `0.001833`
- val_rmse: `0.002587`
- val_pointwise_loss: `0.004808`
- val_centered_curve_shape_loss: `0.004492`
- val_curve_offset_loss: `0.000317`
- val_curve_amplitude_loss: `0.033855`
- val_sparse_harmonic_shape_loss: `9.925534e-05`
- val_structured_mae: `0.004897`
- val_structured_rmse: `0.005976`
- val_residual_offset_mean_abs: `0.004357`

## Test Metrics

- test_loss: `0.005547`
- test_mae: `0.001943`
- test_rmse: `0.002977`
- test_pointwise_loss: `0.005547`
- test_centered_curve_shape_loss: `0.005224`
- test_curve_offset_loss: `0.000324`
- test_curve_amplitude_loss: `0.038770`
- test_sparse_harmonic_shape_loss: `0.000107`
- test_structured_mae: `0.005175`
- test_structured_rmse: `0.006601`
- test_residual_offset_mean_abs: `0.004557`

## Interpretation

The held-out val error stayed finite with MAE=0.001833 deg and RMSE=0.002587 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001943 deg and RMSE=0.002977 deg, which indicates a numerically stable baseline run.
