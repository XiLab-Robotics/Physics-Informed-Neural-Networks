# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_dense360_tracking_Bw`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_bw\2026-05-20-11-01-18__te_harmonic_dense360_tracking_bw\checkpoints\harmonic_regression-epoch=033-val_mae=0.00363716.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.030808`
- val_mae: `0.003637`
- val_rmse: `0.004053`

## Test Metrics

- test_loss: `0.025854`
- test_mae: `0.003403`
- test_rmse: `0.003866`

## Interpretation

The held-out val error stayed finite with MAE=0.003637 deg and RMSE=0.004053 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003403 deg and RMSE=0.003866 deg, which indicates a numerically stable baseline run.
