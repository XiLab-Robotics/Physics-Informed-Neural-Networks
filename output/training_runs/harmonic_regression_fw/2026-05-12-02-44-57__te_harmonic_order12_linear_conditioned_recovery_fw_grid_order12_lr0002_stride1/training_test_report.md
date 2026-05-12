# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr0002_stride1`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_fw\2026-05-12-02-44-57__te_harmonic_order12_linear_conditioned_recovery_fw_grid_order12_lr0002_stride1\checkpoints\harmonic_regression-epoch=024-val_mae=0.00279216.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.022888`
- val_mae: `0.002792`
- val_rmse: `0.003338`

## Test Metrics

- test_loss: `0.025330`
- test_mae: `0.003187`
- test_rmse: `0.003656`

## Interpretation

The held-out val error stayed finite with MAE=0.002792 deg and RMSE=0.003338 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003187 deg and RMSE=0.003656 deg, which indicates a numerically stable baseline run.
