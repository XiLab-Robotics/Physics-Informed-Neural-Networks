# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr0002_stride5`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-05-12-00-40-22__te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr0002_stride5\checkpoints\harmonic_regression-epoch=008-val_mae=0.01700294.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.186799`
- val_mae: `0.017003`
- val_rmse: `0.018542`

## Test Metrics

- test_loss: `0.253340`
- test_mae: `0.020783`
- test_rmse: `0.022411`

## Interpretation

The held-out val error stayed finite with MAE=0.017003 deg and RMSE=0.018542 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020783 deg and RMSE=0.022411 deg, which indicates a numerically stable baseline run.
