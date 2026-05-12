# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr0002_stride5`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-05-11-22-54-21__te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr0002_stride5\checkpoints\harmonic_regression-epoch=003-val_mae=0.01699265.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.187705`
- val_mae: `0.016993`
- val_rmse: `0.018558`

## Test Metrics

- test_loss: `0.253627`
- test_mae: `0.020794`
- test_rmse: `0.022423`

## Interpretation

The held-out val error stayed finite with MAE=0.016993 deg and RMSE=0.018558 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020794 deg and RMSE=0.022423 deg, which indicates a numerically stable baseline run.
