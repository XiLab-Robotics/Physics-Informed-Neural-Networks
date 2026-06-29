# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_bw`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-06-26-04-00-06__te_harmonic_regression_bw\checkpoints\harmonic_regression-epoch=039-val_mae=0.00388820.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010285`
- val_mae: `0.003888`
- val_rmse: `0.004471`
- val_pointwise_loss: `0.010285`
- val_centered_curve_shape_loss: `0.003086`
- val_curve_offset_loss: `0.007641`
- val_curve_amplitude_loss: `0.044954`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.010961`
- test_mae: `0.003811`
- test_rmse: `0.004529`
- test_pointwise_loss: `0.010961`
- test_centered_curve_shape_loss: `0.003831`
- test_curve_offset_loss: `0.007774`
- test_curve_amplitude_loss: `0.057996`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003888 deg and RMSE=0.004471 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003811 deg and RMSE=0.004529 deg, which indicates a numerically stable baseline run.
