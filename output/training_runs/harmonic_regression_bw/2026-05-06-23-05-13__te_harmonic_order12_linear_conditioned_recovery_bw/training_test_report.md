# Harmonic Regression Bw Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_Bw`
- Model Family: `harmonic_regression_bw`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression_bw\2026-05-06-23-05-13__te_harmonic_order12_linear_conditioned_recovery_bw\checkpoints\harmonic_regression-epoch=019-val_mae=0.00370070.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.033769`
- val_mae: `0.003701`
- val_rmse: `0.004253`

## Test Metrics

- test_loss: `0.028694`
- test_mae: `0.003524`
- test_rmse: `0.004080`

## Interpretation

The held-out val error stayed finite with MAE=0.003701 deg and RMSE=0.004253 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003524 deg and RMSE=0.004080 deg, which indicates a numerically stable baseline run.
