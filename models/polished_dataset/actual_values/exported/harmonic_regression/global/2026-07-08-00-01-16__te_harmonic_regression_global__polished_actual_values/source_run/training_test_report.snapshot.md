# Harmonic Regression Global Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_global__polished_actual_values`
- Model Family: `harmonic_regression_global`
- Model Type: `harmonic_regression`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-08-00-01-16__te_harmonic_regression_global__polished_actual_values/checkpoints/harmonic_regression-epoch=053-val_mae=0.00182331.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.003255`
- val_mae: `0.001823`
- val_rmse: `0.002432`
- val_pointwise_loss: `0.003255`
- val_centered_curve_shape_loss: `0.003315`
- val_curve_offset_loss: `0.000882`
- val_curve_amplitude_loss: `0.052687`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.005379`
- test_mae: `0.002071`
- test_rmse: `0.003143`
- test_pointwise_loss: `0.005379`
- test_centered_curve_shape_loss: `0.005521`
- test_curve_offset_loss: `0.004086`
- test_curve_amplitude_loss: `0.076228`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001823 deg and RMSE=0.002432 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002071 deg and RMSE=0.003143 deg, which indicates a numerically stable baseline run.
