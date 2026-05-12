# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr0002_stride1`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-05-11-22-39-27__te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr0002_stride1\checkpoints\harmonic_regression-epoch=007-val_mae=0.01697999.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.187449`
- val_mae: `0.016980`
- val_rmse: `0.018562`

## Test Metrics

- test_loss: `0.253539`
- test_mae: `0.020800`
- test_rmse: `0.022409`

## Interpretation

The held-out val error stayed finite with MAE=0.016980 deg and RMSE=0.018562 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020800 deg and RMSE=0.022409 deg, which indicates a numerically stable baseline run.
