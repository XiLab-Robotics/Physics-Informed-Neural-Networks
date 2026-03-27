# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_small_joint_medium_dense_large_batch_wave1`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-03-26-20-01-25__te_residual_h12_small_joint_medium_dense_large_batch_wave1\checkpoints\residual_harmonic_mlp-epoch=087-val_mae=0.00293487.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007143`
- val_mae: `0.002935`
- val_rmse: `0.003570`
- val_structured_mae: `0.040543`
- val_structured_rmse: `0.044002`

## Test Metrics

- test_loss: `0.007656`
- test_mae: `0.003302`
- test_rmse: `0.003909`
- test_structured_mae: `0.039411`
- test_structured_rmse: `0.044770`

## Interpretation

The held-out val error stayed finite with MAE=0.002935 deg and RMSE=0.003570 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003302 deg and RMSE=0.003909 deg, which indicates a numerically stable baseline run.

