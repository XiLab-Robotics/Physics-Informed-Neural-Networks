# Harmonic Regression Fw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Fw`
- Model Family: `harmonic_regression_fw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_fw\2026-05-06-22-54-24__te_harmonic_order12_linear_conditioned_recovery_fw\checkpoints\harmonic_regression-epoch=068-val_mae=0.00281060.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.022662`
- val_mae: `0.002811`
- val_rmse: `0.003355`

## Test Metrics

- test_loss: `0.024079`
- test_mae: `0.003129`
- test_rmse: `0.003567`

## Interpretation

The held-out val error stayed finite with MAE=0.002811 deg and RMSE=0.003355 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003129 deg and RMSE=0.003567 deg, which indicates a numerically stable baseline run.
