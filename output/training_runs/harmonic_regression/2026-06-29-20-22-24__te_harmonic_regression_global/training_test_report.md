# Harmonic Regression Global Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_global`
- Model Family: `harmonic_regression_global`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-06-29-20-22-24__te_harmonic_regression_global\checkpoints\harmonic_regression-epoch=054-val_mae=0.00389853.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010308`
- val_mae: `0.003899`
- val_rmse: `0.004480`
- val_pointwise_loss: `0.010308`
- val_centered_curve_shape_loss: `0.003109`
- val_curve_offset_loss: `0.007599`
- val_curve_amplitude_loss: `0.044165`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.010993`
- test_mae: `0.003828`
- test_rmse: `0.004545`
- test_pointwise_loss: `0.010993`
- test_centered_curve_shape_loss: `0.003860`
- test_curve_offset_loss: `0.007728`
- test_curve_amplitude_loss: `0.057249`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003899 deg and RMSE=0.004480 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003828 deg and RMSE=0.004545 deg, which indicates a numerically stable baseline run.
