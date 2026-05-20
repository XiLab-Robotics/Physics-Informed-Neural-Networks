# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_dense240_tracking_Fw`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_fw\2026-05-20-10-37-26__te_harmonic_dense240_tracking_fw\checkpoints\harmonic_regression-epoch=040-val_mae=0.00259326.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.018919`
- val_mae: `0.002593`
- val_rmse: `0.003013`

## Test Metrics

- test_loss: `0.020625`
- test_mae: `0.002935`
- test_rmse: `0.003239`

## Interpretation

The held-out val error stayed finite with MAE=0.002593 deg and RMSE=0.003013 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002935 deg and RMSE=0.003239 deg, which indicates a numerically stable baseline run.
