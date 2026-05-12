# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order12_lr0001_stride1`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_bw\2026-05-12-04-48-34__te_harmonic_order12_linear_conditioned_recovery_bw_grid_order12_lr0001_stride1\checkpoints\harmonic_regression-epoch=085-val_mae=0.00369148.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.033726`
- val_mae: `0.003691`
- val_rmse: `0.004248`

## Test Metrics

- test_loss: `0.028673`
- test_mae: `0.003513`
- test_rmse: `0.004076`

## Interpretation

The held-out val error stayed finite with MAE=0.003691 deg and RMSE=0.004248 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003513 deg and RMSE=0.004076 deg, which indicates a numerically stable baseline run.
