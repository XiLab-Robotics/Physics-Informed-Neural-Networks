# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_global`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-05-06-22-40-20__te_harmonic_order12_linear_conditioned_recovery_global\checkpoints\harmonic_regression-epoch=018-val_mae=0.01701703.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.187696`
- val_mae: `0.017017`
- val_rmse: `0.018572`

## Test Metrics

- test_loss: `0.253200`
- test_mae: `0.020779`
- test_rmse: `0.022403`

## Interpretation

The held-out val error stayed finite with MAE=0.017017 deg and RMSE=0.018572 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020779 deg and RMSE=0.022403 deg, which indicates a numerically stable baseline run.
