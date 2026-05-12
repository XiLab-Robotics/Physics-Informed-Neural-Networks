# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr00005_stride5`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_bw\2026-05-12-03-20-06__te_harmonic_order12_linear_conditioned_recovery_bw_grid_order8_lr00005_stride5\checkpoints\harmonic_regression-epoch=040-val_mae=0.00374673.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.034294`
- val_mae: `0.003747`
- val_rmse: `0.004292`

## Test Metrics

- test_loss: `0.028428`
- test_mae: `0.003517`
- test_rmse: `0.004063`

## Interpretation

The held-out val error stayed finite with MAE=0.003747 deg and RMSE=0.004292 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003517 deg and RMSE=0.004063 deg, which indicates a numerically stable baseline run.
