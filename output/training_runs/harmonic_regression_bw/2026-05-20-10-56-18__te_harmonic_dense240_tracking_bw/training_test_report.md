# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_dense240_tracking_Bw`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_bw\2026-05-20-10-56-18__te_harmonic_dense240_tracking_bw\checkpoints\harmonic_regression-epoch=023-val_mae=0.00358755.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.030138`
- val_mae: `0.003588`
- val_rmse: `0.004007`

## Test Metrics

- test_loss: `0.026240`
- test_mae: `0.003400`
- test_rmse: `0.003886`

## Interpretation

The held-out val error stayed finite with MAE=0.003588 deg and RMSE=0.004007 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003400 deg and RMSE=0.003886 deg, which indicates a numerically stable baseline run.
