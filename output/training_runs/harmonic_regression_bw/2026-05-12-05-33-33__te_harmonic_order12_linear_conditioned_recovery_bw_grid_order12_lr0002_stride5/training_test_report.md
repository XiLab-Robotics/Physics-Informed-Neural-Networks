# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Bw_grid_order12_lr0002_stride5`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_bw\2026-05-12-05-33-33__te_harmonic_order12_linear_conditioned_recovery_bw_grid_order12_lr0002_stride5\checkpoints\harmonic_regression-epoch=045-val_mae=0.00360287.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.033213`
- val_mae: `0.003603`
- val_rmse: `0.004174`

## Test Metrics

- test_loss: `0.029052`
- test_mae: `0.003519`
- test_rmse: `0.004100`

## Interpretation

The held-out val error stayed finite with MAE=0.003603 deg and RMSE=0.004174 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003519 deg and RMSE=0.004100 deg, which indicates a numerically stable baseline run.
