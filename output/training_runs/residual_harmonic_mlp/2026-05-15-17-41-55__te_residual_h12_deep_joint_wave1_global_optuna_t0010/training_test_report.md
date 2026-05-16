# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0010`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-17-41-55__te_residual_h12_deep_joint_wave1_global_optuna_t0010\checkpoints\residual_harmonic_mlp-epoch=126-val_mae=0.00290265.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006868`
- val_mae: `0.002903`
- val_rmse: `0.003427`
- val_structured_mae: `0.040534`
- val_structured_rmse: `0.042564`

## Test Metrics

- test_loss: `0.006594`
- test_mae: `0.003067`
- test_rmse: `0.003568`
- test_structured_mae: `0.039408`
- test_structured_rmse: `0.042798`

## Interpretation

The held-out val error stayed finite with MAE=0.002903 deg and RMSE=0.003427 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003067 deg and RMSE=0.003568 deg, which indicates a numerically stable baseline run.
