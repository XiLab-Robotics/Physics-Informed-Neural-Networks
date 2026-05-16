# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0008`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-16-41-15__te_residual_h12_deep_joint_wave1_global_optuna_t0008\checkpoints\residual_harmonic_mlp-epoch=095-val_mae=0.00296278.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007355`
- val_mae: `0.002963`
- val_rmse: `0.003624`
- val_structured_mae: `0.040535`
- val_structured_rmse: `0.044008`

## Test Metrics

- test_loss: `0.008387`
- test_mae: `0.003443`
- test_rmse: `0.004085`
- test_structured_mae: `0.039408`
- test_structured_rmse: `0.044768`

## Interpretation

The held-out val error stayed finite with MAE=0.002963 deg and RMSE=0.003624 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003443 deg and RMSE=0.004085 deg, which indicates a numerically stable baseline run.
