# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\residual_harmonic_mlp\2026-05-06-17-03-18__te_residual_h12_deep_joint_wave1_global\checkpoints\residual_harmonic_mlp-epoch=038-val_mae=0.00311466.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007789`
- val_mae: `0.003115`
- val_rmse: `0.003685`
- val_structured_mae: `0.040519`
- val_structured_rmse: `0.042632`

## Test Metrics

- test_loss: `0.008266`
- test_mae: `0.003420`
- test_rmse: `0.003931`
- test_structured_mae: `0.039402`
- test_structured_rmse: `0.042814`

## Interpretation

The held-out val error stayed finite with MAE=0.003115 deg and RMSE=0.003685 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003420 deg and RMSE=0.003931 deg, which indicates a numerically stable baseline run.
