# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_fw`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-06-26-03-44-24__te_harmonic_regression_fw\checkpoints\harmonic_regression-epoch=050-val_mae=0.00388663.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010270`
- val_mae: `0.003887`
- val_rmse: `0.004472`
- val_pointwise_loss: `0.010270`
- val_centered_curve_shape_loss: `0.003080`
- val_curve_offset_loss: `0.007603`
- val_curve_amplitude_loss: `0.046988`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.010894`
- test_mae: `0.003806`
- test_rmse: `0.004524`
- test_pointwise_loss: `0.010894`
- test_centered_curve_shape_loss: `0.003831`
- test_curve_offset_loss: `0.007719`
- test_curve_amplitude_loss: `0.060279`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003887 deg and RMSE=0.004472 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003806 deg and RMSE=0.004524 deg, which indicates a numerically stable baseline run.
