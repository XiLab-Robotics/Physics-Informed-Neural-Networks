# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0001`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-13-00-52__te_residual_h12_deep_joint_wave1_global_optuna_t0001\checkpoints\residual_harmonic_mlp-epoch=051-val_mae=0.00305188.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007521`
- val_mae: `0.003052`
- val_rmse: `0.003743`
- val_structured_mae: `0.040521`
- val_structured_rmse: `0.044046`

## Test Metrics

- test_loss: `0.007652`
- test_mae: `0.003305`
- test_rmse: `0.003914`
- test_structured_mae: `0.039403`
- test_structured_rmse: `0.044776`

## Interpretation

The held-out val error stayed finite with MAE=0.003052 deg and RMSE=0.003743 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003305 deg and RMSE=0.003914 deg, which indicates a numerically stable baseline run.
