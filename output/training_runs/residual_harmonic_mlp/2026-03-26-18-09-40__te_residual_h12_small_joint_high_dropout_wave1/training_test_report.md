# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_small_joint_high_dropout_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-18-09-40__te_residual_h12_small_joint_high_dropout_wave1\checkpoints\residual_harmonic_mlp-epoch=094-val_mae=0.00300110.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007080`
- val_mae: `0.003001`
- val_rmse: `0.003519`
- val_structured_mae: `0.040524`
- val_structured_rmse: `0.042585`

## Test Metrics

- test_loss: `0.007078`
- test_mae: `0.003230`
- test_rmse: `0.003704`
- test_structured_mae: `0.039404`
- test_structured_rmse: `0.042797`

## Interpretation

The held-out val error stayed finite with MAE=0.003001 deg and RMSE=0.003519 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003230 deg and RMSE=0.003704 deg, which indicates a numerically stable baseline run.

