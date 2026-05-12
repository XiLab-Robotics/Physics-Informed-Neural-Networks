# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr0002_stride5`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_fw\2026-05-12-02-56-48__te_harmonic_order12_linear_conditioned_recovery_fw_grid_order12_lr0002_stride5\checkpoints\harmonic_regression-epoch=033-val_mae=0.00277858.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.022520`
- val_mae: `0.002779`
- val_rmse: `0.003326`

## Test Metrics

- test_loss: `0.024356`
- test_mae: `0.003144`
- test_rmse: `0.003582`

## Interpretation

The held-out val error stayed finite with MAE=0.002779 deg and RMSE=0.003326 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003144 deg and RMSE=0.003582 deg, which indicates a numerically stable baseline run.
