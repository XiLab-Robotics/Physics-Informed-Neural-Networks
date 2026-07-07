# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_regression_bw__polished_setpoints`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/harmonic_regression/2026-07-07-23-39-40__te_harmonic_regression_bw__polished_setpoints/checkpoints/harmonic_regression-epoch=044-val_mae=0.01715066.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.186085`
- val_mae: `0.017151`
- val_rmse: `0.019898`
- val_pointwise_loss: `0.186085`
- val_centered_curve_shape_loss: `0.003263`
- val_curve_offset_loss: `0.176055`
- val_curve_amplitude_loss: `0.059730`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.211984`
- test_mae: `0.018022`
- test_rmse: `0.021014`
- test_pointwise_loss: `0.211984`
- test_centered_curve_shape_loss: `0.005260`
- test_curve_offset_loss: `0.197003`
- test_curve_amplitude_loss: `0.085506`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.017151 deg and RMSE=0.019898 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.018022 deg and RMSE=0.021014 deg, which indicates a numerically stable baseline run.
