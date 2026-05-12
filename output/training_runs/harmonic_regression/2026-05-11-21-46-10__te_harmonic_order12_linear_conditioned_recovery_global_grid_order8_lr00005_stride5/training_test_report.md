# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr00005_stride5`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-05-11-21-46-10__te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr00005_stride5\checkpoints\harmonic_regression-epoch=017-val_mae=0.01701921.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.187475`
- val_mae: `0.017019`
- val_rmse: `0.018543`

## Test Metrics

- test_loss: `0.253266`
- test_mae: `0.020785`
- test_rmse: `0.022420`

## Interpretation

The held-out val error stayed finite with MAE=0.017019 deg and RMSE=0.018543 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020785 deg and RMSE=0.022420 deg, which indicates a numerically stable baseline run.
