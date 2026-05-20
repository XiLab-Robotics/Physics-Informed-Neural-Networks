# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_rcim_sparse_tracking_Bw`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_bw\2026-05-20-10-50-22__te_harmonic_rcim_sparse_tracking_bw\checkpoints\harmonic_regression-epoch=055-val_mae=0.00357006.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.030442`
- val_mae: `0.003570`
- val_rmse: `0.004009`

## Test Metrics

- test_loss: `0.026433`
- test_mae: `0.003406`
- test_rmse: `0.003894`

## Interpretation

The held-out val error stayed finite with MAE=0.003570 deg and RMSE=0.004009 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003406 deg and RMSE=0.003894 deg, which indicates a numerically stable baseline run.
