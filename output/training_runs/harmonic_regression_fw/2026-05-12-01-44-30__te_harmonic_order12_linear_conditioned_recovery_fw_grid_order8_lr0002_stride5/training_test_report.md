# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr0002_stride5`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_fw\2026-05-12-01-44-30__te_harmonic_order12_linear_conditioned_recovery_fw_grid_order8_lr0002_stride5\checkpoints\harmonic_regression-epoch=024-val_mae=0.00280047.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.022574`
- val_mae: `0.002800`
- val_rmse: `0.003345`

## Test Metrics

- test_loss: `0.023926`
- test_mae: `0.003118`
- test_rmse: `0.003549`

## Interpretation

The held-out val error stayed finite with MAE=0.002800 deg and RMSE=0.003345 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003118 deg and RMSE=0.003549 deg, which indicates a numerically stable baseline run.
