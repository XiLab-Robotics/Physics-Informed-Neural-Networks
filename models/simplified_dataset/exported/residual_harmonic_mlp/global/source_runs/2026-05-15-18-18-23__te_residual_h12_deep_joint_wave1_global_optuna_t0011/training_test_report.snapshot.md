# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0011`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-18-18-23__te_residual_h12_deep_joint_wave1_global_optuna_t0011\checkpoints\residual_harmonic_mlp-epoch=200-val_mae=0.00286835.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006816`
- val_mae: `0.002868`
- val_rmse: `0.003382`
- val_structured_mae: `0.040583`
- val_structured_rmse: `0.042549`

## Test Metrics

- test_loss: `0.008211`
- test_mae: `0.003428`
- test_rmse: `0.003928`
- test_structured_mae: `0.039430`
- test_structured_rmse: `0.042839`

## Interpretation

The held-out val error stayed finite with MAE=0.002868 deg and RMSE=0.003382 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003428 deg and RMSE=0.003928 deg, which indicates a numerically stable baseline run.
