# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr0001_stride5`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-05-12-00-07-41__te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr0001_stride5\checkpoints\harmonic_regression-epoch=038-val_mae=0.01700669.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.187059`
- val_mae: `0.017007`
- val_rmse: `0.018538`

## Test Metrics

- test_loss: `0.253278`
- test_mae: `0.020793`
- test_rmse: `0.022416`

## Interpretation

The held-out val error stayed finite with MAE=0.017007 deg and RMSE=0.018538 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020793 deg and RMSE=0.022416 deg, which indicates a numerically stable baseline run.
