# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_rcim_sparse_tracking_Fw`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_fw\2026-05-20-10-32-22__te_harmonic_rcim_sparse_tracking_fw\checkpoints\harmonic_regression-epoch=028-val_mae=0.00256613.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.019159`
- val_mae: `0.002566`
- val_rmse: `0.003008`

## Test Metrics

- test_loss: `0.020900`
- test_mae: `0.002943`
- test_rmse: `0.003254`

## Interpretation

The held-out val error stayed finite with MAE=0.002566 deg and RMSE=0.003008 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002943 deg and RMSE=0.003254 deg, which indicates a numerically stable baseline run.
