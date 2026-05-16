# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0012`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-19-19-04__te_residual_h12_deep_joint_wave1_global_optuna_t0012\checkpoints\residual_harmonic_mlp-epoch=040-val_mae=0.00300216.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007396`
- val_mae: `0.003002`
- val_rmse: `0.003542`
- val_structured_mae: `0.040558`
- val_structured_rmse: `0.042554`

## Test Metrics

- test_loss: `0.008061`
- test_mae: `0.003389`
- test_rmse: `0.003870`
- test_structured_mae: `0.039419`
- test_structured_rmse: `0.042815`

## Interpretation

The held-out val error stayed finite with MAE=0.003002 deg and RMSE=0.003542 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003389 deg and RMSE=0.003870 deg, which indicates a numerically stable baseline run.
