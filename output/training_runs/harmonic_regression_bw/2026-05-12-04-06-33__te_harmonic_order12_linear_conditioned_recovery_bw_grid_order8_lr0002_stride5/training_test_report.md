# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order8_lr0002_stride5`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_bw\2026-05-12-04-06-33__te_harmonic_order12_linear_conditioned_recovery_bw_grid_order8_lr0002_stride5\checkpoints\harmonic_regression-epoch=047-val_mae=0.00363757.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.033681`
- val_mae: `0.003638`
- val_rmse: `0.004219`

## Test Metrics

- test_loss: `0.028922`
- test_mae: `0.003494`
- test_rmse: `0.004081`

## Interpretation

The held-out val error stayed finite with MAE=0.003638 deg and RMSE=0.004219 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003494 deg and RMSE=0.004081 deg, which indicates a numerically stable baseline run.
