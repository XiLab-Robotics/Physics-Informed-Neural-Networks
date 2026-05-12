# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr0001_stride5`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_fw\2026-05-12-02-36-57__te_harmonic_order12_linear_conditioned_recovery_fw_grid_order12_lr0001_stride5\checkpoints\harmonic_regression-epoch=028-val_mae=0.00284170.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.022741`
- val_mae: `0.002842`
- val_rmse: `0.003378`

## Test Metrics

- test_loss: `0.023673`
- test_mae: `0.003111`
- test_rmse: `0.003538`

## Interpretation

The held-out val error stayed finite with MAE=0.002842 deg and RMSE=0.003378 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003111 deg and RMSE=0.003538 deg, which indicates a numerically stable baseline run.
