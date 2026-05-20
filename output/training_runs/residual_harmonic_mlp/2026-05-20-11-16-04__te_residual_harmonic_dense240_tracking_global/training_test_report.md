# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_dense240_tracking_global`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-20-11-16-04__te_residual_harmonic_dense240_tracking_global\checkpoints\residual_harmonic_mlp-epoch=070-val_mae=0.00297567.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007001`
- val_mae: `0.002976`
- val_rmse: `0.003448`
- val_structured_mae: `0.040521`
- val_structured_rmse: `0.042627`

## Test Metrics

- test_loss: `0.006932`
- test_mae: `0.003162`
- test_rmse: `0.003598`
- test_structured_mae: `0.039402`
- test_structured_rmse: `0.042809`

## Interpretation

The held-out val error stayed finite with MAE=0.002976 deg and RMSE=0.003448 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003162 deg and RMSE=0.003598 deg, which indicates a numerically stable baseline run.
