# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0009`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-17-10-34__te_residual_h12_deep_joint_wave1_global_optuna_t0009\checkpoints\residual_harmonic_mlp-epoch=084-val_mae=0.00301855.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007255`
- val_mae: `0.003019`
- val_rmse: `0.003557`
- val_structured_mae: `0.040548`
- val_structured_rmse: `0.042552`

## Test Metrics

- test_loss: `0.007352`
- test_mae: `0.003252`
- test_rmse: `0.003769`
- test_structured_mae: `0.039414`
- test_structured_rmse: `0.042806`

## Interpretation

The held-out val error stayed finite with MAE=0.003019 deg and RMSE=0.003557 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003252 deg and RMSE=0.003769 deg, which indicates a numerically stable baseline run.
