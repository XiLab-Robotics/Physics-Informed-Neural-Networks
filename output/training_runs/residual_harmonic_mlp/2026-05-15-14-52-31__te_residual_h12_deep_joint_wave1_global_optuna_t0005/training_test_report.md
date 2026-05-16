# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0005`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-14-52-31__te_residual_h12_deep_joint_wave1_global_optuna_t0005\checkpoints\residual_harmonic_mlp-epoch=067-val_mae=0.00307521.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007538`
- val_mae: `0.003075`
- val_rmse: `0.003631`
- val_structured_mae: `0.040540`
- val_structured_rmse: `0.042558`

## Test Metrics

- test_loss: `0.007370`
- test_mae: `0.003257`
- test_rmse: `0.003790`
- test_structured_mae: `0.039410`
- test_structured_rmse: `0.042801`

## Interpretation

The held-out val error stayed finite with MAE=0.003075 deg and RMSE=0.003631 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003257 deg and RMSE=0.003790 deg, which indicates a numerically stable baseline run.
