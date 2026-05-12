# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order12_lr00005_stride1`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_bw\2026-05-12-04-17-32__te_harmonic_order12_linear_conditioned_recovery_bw_grid_order12_lr00005_stride1\checkpoints\harmonic_regression-epoch=071-val_mae=0.00373203.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.034092`
- val_mae: `0.003732`
- val_rmse: `0.004279`

## Test Metrics

- test_loss: `0.028468`
- test_mae: `0.003514`
- test_rmse: `0.004067`

## Interpretation

The held-out val error stayed finite with MAE=0.003732 deg and RMSE=0.004279 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003514 deg and RMSE=0.004067 deg, which indicates a numerically stable baseline run.
