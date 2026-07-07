# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_bw__simplified_setpoints`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-07-23-01-08__te_harmonic_regression_bw__simplified_setpoints/checkpoints/harmonic_regression-epoch=060-val_mae=0.01698885.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.186833`
- val_mae: `0.016989`
- val_rmse: `0.019525`
- val_pointwise_loss: `0.186833`
- val_centered_curve_shape_loss: `0.003544`
- val_curve_offset_loss: `0.197149`
- val_curve_amplitude_loss: `0.062213`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.253253`
- test_mae: `0.020789`
- test_rmse: `0.022914`
- test_pointwise_loss: `0.253253`
- test_centered_curve_shape_loss: `0.003282`
- test_curve_offset_loss: `0.223892`
- test_curve_amplitude_loss: `0.058904`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.016989 deg and RMSE=0.019525 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020789 deg and RMSE=0.022914 deg, which indicates a numerically stable baseline run.
