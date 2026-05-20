# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_dense360_tracking_Fw`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression_fw\2026-05-20-10-43-22__te_harmonic_dense360_tracking_fw\checkpoints\harmonic_regression-epoch=053-val_mae=0.00261006.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.019248`
- val_mae: `0.002610`
- val_rmse: `0.003057`

## Test Metrics

- test_loss: `0.020546`
- test_mae: `0.002916`
- test_rmse: `0.003237`

## Interpretation

The held-out val error stayed finite with MAE=0.002610 deg and RMSE=0.003057 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002916 deg and RMSE=0.003237 deg, which indicates a numerically stable baseline run.
