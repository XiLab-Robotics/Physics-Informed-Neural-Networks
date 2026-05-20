# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_dense240_tracking_global`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-05-20-10-17-23__te_harmonic_dense240_tracking_global\checkpoints\harmonic_regression-epoch=020-val_mae=0.01698888.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.186153`
- val_mae: `0.016989`
- val_rmse: `0.018488`

## Test Metrics

- test_loss: `0.252754`
- test_mae: `0.020787`
- test_rmse: `0.022388`

## Interpretation

The held-out val error stayed finite with MAE=0.016989 deg and RMSE=0.018488 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020787 deg and RMSE=0.022388 deg, which indicates a numerically stable baseline run.
