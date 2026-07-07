# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_bw__polished_actual_values`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-08-00-32-21__te_harmonic_regression_bw__polished_actual_values/checkpoints/harmonic_regression-epoch=054-val_mae=0.00182643.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.003268`
- val_mae: `0.001826`
- val_rmse: `0.002437`
- val_pointwise_loss: `0.003268`
- val_centered_curve_shape_loss: `0.003314`
- val_curve_offset_loss: `0.000883`
- val_curve_amplitude_loss: `0.051998`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.005400`
- test_mae: `0.002076`
- test_rmse: `0.003150`
- test_pointwise_loss: `0.005400`
- test_centered_curve_shape_loss: `0.005524`
- test_curve_offset_loss: `0.004079`
- test_curve_amplitude_loss: `0.075268`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001826 deg and RMSE=0.002437 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002076 deg and RMSE=0.003150 deg, which indicates a numerically stable baseline run.
