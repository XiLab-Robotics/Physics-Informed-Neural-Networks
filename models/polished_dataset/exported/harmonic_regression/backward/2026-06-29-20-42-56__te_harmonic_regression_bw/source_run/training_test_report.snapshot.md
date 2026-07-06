# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_bw`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-06-29-20-42-56__te_harmonic_regression_bw\checkpoints\harmonic_regression-epoch=029-val_mae=0.00389217.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010242`
- val_mae: `0.003892`
- val_rmse: `0.004476`
- val_pointwise_loss: `0.010242`
- val_centered_curve_shape_loss: `0.003088`
- val_curve_offset_loss: `0.007589`
- val_curve_amplitude_loss: `0.045553`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.010833`
- test_mae: `0.003808`
- test_rmse: `0.004519`
- test_pointwise_loss: `0.010833`
- test_centered_curve_shape_loss: `0.003836`
- test_curve_offset_loss: `0.007638`
- test_curve_amplitude_loss: `0.059078`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003892 deg and RMSE=0.004476 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003808 deg and RMSE=0.004519 deg, which indicates a numerically stable baseline run.
