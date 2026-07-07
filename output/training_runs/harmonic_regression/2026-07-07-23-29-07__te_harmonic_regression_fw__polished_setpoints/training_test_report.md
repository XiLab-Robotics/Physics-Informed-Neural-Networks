# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_fw__polished_setpoints`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-07-23-29-07__te_harmonic_regression_fw__polished_setpoints/checkpoints/harmonic_regression-epoch=032-val_mae=0.01714993.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.186218`
- val_mae: `0.017150`
- val_rmse: `0.019904`
- val_pointwise_loss: `0.186218`
- val_centered_curve_shape_loss: `0.003263`
- val_curve_offset_loss: `0.176089`
- val_curve_amplitude_loss: `0.059968`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.212090`
- test_mae: `0.018003`
- test_rmse: `0.021015`
- test_pointwise_loss: `0.212090`
- test_centered_curve_shape_loss: `0.005259`
- test_curve_offset_loss: `0.196211`
- test_curve_amplitude_loss: `0.085630`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.017150 deg and RMSE=0.019904 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.018003 deg and RMSE=0.021015 deg, which indicates a numerically stable baseline run.
