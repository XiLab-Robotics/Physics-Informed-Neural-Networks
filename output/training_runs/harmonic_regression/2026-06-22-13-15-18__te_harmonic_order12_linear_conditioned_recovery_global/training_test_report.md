# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_global`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-06-22-13-15-18__te_harmonic_order12_linear_conditioned_recovery_global\checkpoints\harmonic_regression-epoch=030-val_mae=0.00390380.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010372`
- val_mae: `0.003904`
- val_rmse: `0.004480`
- val_pointwise_loss: `0.010372`
- val_centered_curve_shape_loss: `0.003079`
- val_curve_offset_loss: `0.007698`
- val_curve_amplitude_loss: `0.046224`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.011122`
- test_mae: `0.003839`
- test_rmse: `0.004555`
- test_pointwise_loss: `0.011122`
- test_centered_curve_shape_loss: `0.003825`
- test_curve_offset_loss: `0.007863`
- test_curve_amplitude_loss: `0.059061`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003904 deg and RMSE=0.004480 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003839 deg and RMSE=0.004555 deg, which indicates a numerically stable baseline run.
