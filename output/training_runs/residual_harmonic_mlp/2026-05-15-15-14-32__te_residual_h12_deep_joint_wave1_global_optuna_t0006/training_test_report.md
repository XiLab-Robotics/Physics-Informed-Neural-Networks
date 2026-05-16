# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0006`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-15-14-32__te_residual_h12_deep_joint_wave1_global_optuna_t0006\checkpoints\residual_harmonic_mlp-epoch=175-val_mae=0.00289537.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006841`
- val_mae: `0.002895`
- val_rmse: `0.003432`
- val_structured_mae: `0.040567`
- val_structured_rmse: `0.042548`

## Test Metrics

- test_loss: `0.006415`
- test_mae: `0.003034`
- test_rmse: `0.003550`
- test_structured_mae: `0.039423`
- test_structured_rmse: `0.042822`

## Interpretation

The held-out val error stayed finite with MAE=0.002895 deg and RMSE=0.003432 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003034 deg and RMSE=0.003550 deg, which indicates a numerically stable baseline run.
