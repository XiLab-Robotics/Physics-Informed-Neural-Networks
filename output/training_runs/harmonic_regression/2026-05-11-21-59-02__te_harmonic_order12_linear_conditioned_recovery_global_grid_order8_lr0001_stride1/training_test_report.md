# Harmonic Regression Training And Testing Report

## Overview

- Run Name: `te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr0001_stride1`
- Model Family: `harmonic_regression`
- Model Type: `harmonic_regression`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\harmonic_regression\2026-05-11-21-59-02__te_harmonic_order12_linear_conditioned_recovery_global_grid_order8_lr0001_stride1\checkpoints\harmonic_regression-epoch=051-val_mae=0.01700146.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.187611`
- val_mae: `0.017001`
- val_rmse: `0.018551`

## Test Metrics

- test_loss: `0.253314`
- test_mae: `0.020791`
- test_rmse: `0.022416`

## Interpretation

The held-out val error stayed finite with MAE=0.017001 deg and RMSE=0.018551 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.020791 deg and RMSE=0.022416 deg, which indicates a numerically stable baseline run.
