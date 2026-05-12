# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr0001_stride1`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_fw\2026-05-12-01-12-06__te_harmonic_order12_linear_conditioned_recovery_fw_grid_order8_lr0001_stride1\checkpoints\harmonic_regression-epoch=046-val_mae=0.00282731.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.022690`
- val_mae: `0.002827`
- val_rmse: `0.003365`

## Test Metrics

- test_loss: `0.023929`
- test_mae: `0.003127`
- test_rmse: `0.003558`

## Interpretation

The held-out val error stayed finite with MAE=0.002827 deg and RMSE=0.003365 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003127 deg and RMSE=0.003558 deg, which indicates a numerically stable baseline run.
