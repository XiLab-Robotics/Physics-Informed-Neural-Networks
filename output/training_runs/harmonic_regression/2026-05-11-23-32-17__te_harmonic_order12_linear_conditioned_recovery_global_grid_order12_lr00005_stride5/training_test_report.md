# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr00005_stride5`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-05-11-23-32-17__te_harmonic_order12_linear_conditioned_recovery_global_grid_order12_lr00005_stride5\checkpoints\harmonic_regression-epoch=040-val_mae=0.01702522.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.188175`
- val_mae: `0.017025`
- val_rmse: `0.018580`

## Test Metrics

- test_loss: `0.253309`
- test_mae: `0.020774`
- test_rmse: `0.022412`

## Interpretation

The held-out val error stayed finite with MAE=0.017025 deg and RMSE=0.018580 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020774 deg and RMSE=0.022412 deg, which indicates a numerically stable baseline run.
