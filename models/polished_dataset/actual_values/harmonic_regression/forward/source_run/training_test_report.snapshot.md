# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_fw__polished_actual_values`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-08-00-15-14__te_harmonic_regression_fw__polished_actual_values/checkpoints/harmonic_regression-epoch=073-val_mae=0.00182314.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.003255`
- val_mae: `0.001823`
- val_rmse: `0.002430`
- val_pointwise_loss: `0.003255`
- val_centered_curve_shape_loss: `0.003316`
- val_curve_offset_loss: `0.000901`
- val_curve_amplitude_loss: `0.051444`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.005344`
- test_mae: `0.002066`
- test_rmse: `0.003135`
- test_pointwise_loss: `0.005344`
- test_centered_curve_shape_loss: `0.005524`
- test_curve_offset_loss: `0.004068`
- test_curve_amplitude_loss: `0.074520`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001823 deg and RMSE=0.002430 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002066 deg and RMSE=0.003135 deg, which indicates a numerically stable baseline run.
