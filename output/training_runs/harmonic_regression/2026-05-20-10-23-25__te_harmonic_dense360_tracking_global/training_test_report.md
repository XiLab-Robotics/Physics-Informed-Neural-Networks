# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_dense360_tracking_global`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-05-20-10-23-25__te_harmonic_dense360_tracking_global\checkpoints\harmonic_regression-epoch=030-val_mae=0.01699096.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.187657`
- val_mae: `0.016991`
- val_rmse: `0.018551`

## Test Metrics

- test_loss: `0.253045`
- test_mae: `0.020780`
- test_rmse: `0.022399`

## Interpretation

The held-out val error stayed finite with MAE=0.016991 deg and RMSE=0.018551 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020780 deg and RMSE=0.022399 deg, which indicates a numerically stable baseline run.
