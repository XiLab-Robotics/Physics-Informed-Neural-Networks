# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order8_lr00005_stride1`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_fw\2026-05-12-00-51-53__te_harmonic_order12_linear_conditioned_recovery_fw_grid_order8_lr00005_stride1\checkpoints\harmonic_regression-epoch=013-val_mae=0.00283065.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023433`
- val_mae: `0.002831`
- val_rmse: `0.003408`

## Test Metrics

- test_loss: `0.024869`
- test_mae: `0.003155`
- test_rmse: `0.003626`

## Interpretation

The held-out val error stayed finite with MAE=0.002831 deg and RMSE=0.003408 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003155 deg and RMSE=0.003626 deg, which indicates a numerically stable baseline run.
