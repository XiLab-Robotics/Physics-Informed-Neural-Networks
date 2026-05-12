# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Fw_grid_order12_lr00005_stride1`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_fw\2026-05-12-01-53-37__te_harmonic_order12_linear_conditioned_recovery_fw_grid_order12_lr00005_stride1\checkpoints\harmonic_regression-epoch=061-val_mae=0.00283880.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.022740`
- val_mae: `0.002839`
- val_rmse: `0.003378`

## Test Metrics

- test_loss: `0.023627`
- test_mae: `0.003105`
- test_rmse: `0.003534`

## Interpretation

The held-out val error stayed finite with MAE=0.002839 deg and RMSE=0.003378 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003105 deg and RMSE=0.003534 deg, which indicates a numerically stable baseline run.
