# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_rcim_sparse_tracking_global`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\harmonic_regression\2026-05-20-10-11-06__te_harmonic_rcim_sparse_tracking_global\checkpoints\harmonic_regression-epoch=039-val_mae=0.01699512.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.187027`
- val_mae: `0.016995`
- val_rmse: `0.018512`

## Test Metrics

- test_loss: `0.252540`
- test_mae: `0.020767`
- test_rmse: `0.022376`

## Interpretation

The held-out val error stayed finite with MAE=0.016995 deg and RMSE=0.018512 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020767 deg and RMSE=0.022376 deg, which indicates a numerically stable baseline run.
