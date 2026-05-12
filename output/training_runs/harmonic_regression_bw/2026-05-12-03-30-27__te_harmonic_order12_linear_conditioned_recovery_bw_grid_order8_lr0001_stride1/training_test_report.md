# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0001_stride1`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_bw\2026-05-12-03-30-27__te_harmonic_order12_linear_conditioned_recovery_bw_grid_order8_lr0001_stride1\checkpoints\harmonic_regression-epoch=043-val_mae=0.00371026.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.033882`
- val_mae: `0.003710`
- val_rmse: `0.004261`

## Test Metrics

- test_loss: `0.028619`
- test_mae: `0.003524`
- test_rmse: `0.004077`

## Interpretation

The held-out val error stayed finite with MAE=0.003710 deg and RMSE=0.004261 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003524 deg and RMSE=0.004077 deg, which indicates a numerically stable baseline run.
