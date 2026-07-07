# Harmonic Regression Global Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_global__simplified_setpoints`
- Model Family: `harmonic_regression_global`
- Model Type: `harmonic_regression`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-07-22-48-30__te_harmonic_regression_global__simplified_setpoints/checkpoints/harmonic_regression-epoch=063-val_mae=0.01699328.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.186782`
- val_mae: `0.016993`
- val_rmse: `0.019524`
- val_pointwise_loss: `0.186782`
- val_centered_curve_shape_loss: `0.003545`
- val_curve_offset_loss: `0.197139`
- val_curve_amplitude_loss: `0.061895`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.253273`
- test_mae: `0.020784`
- test_rmse: `0.022917`
- test_pointwise_loss: `0.253273`
- test_centered_curve_shape_loss: `0.003282`
- test_curve_offset_loss: `0.223888`
- test_curve_amplitude_loss: `0.058197`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.016993 deg and RMSE=0.019524 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020784 deg and RMSE=0.022917 deg, which indicates a numerically stable baseline run.
