# Harmonic Regression Global Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_global__polished_setpoints`
- Model Family: `harmonic_regression_global`
- Model Type: `harmonic_regression`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-07-23-18-16__te_harmonic_regression_global__polished_setpoints/checkpoints/harmonic_regression-epoch=038-val_mae=0.01714113.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.185709`
- val_mae: `0.017141`
- val_rmse: `0.019879`
- val_pointwise_loss: `0.185709`
- val_centered_curve_shape_loss: `0.003263`
- val_curve_offset_loss: `0.175878`
- val_curve_amplitude_loss: `0.059907`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.212194`
- test_mae: `0.018032`
- test_rmse: `0.021021`
- test_pointwise_loss: `0.212194`
- test_centered_curve_shape_loss: `0.005259`
- test_curve_offset_loss: `0.197340`
- test_curve_amplitude_loss: `0.085541`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.017141 deg and RMSE=0.019879 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.018032 deg and RMSE=0.021021 deg, which indicates a numerically stable baseline run.
