# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0000`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-12-47-30__te_residual_h12_deep_joint_wave1_global_optuna_t0000\checkpoints\residual_harmonic_mlp-epoch=010-val_mae=0.00317925.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.008166`
- val_mae: `0.003179`
- val_rmse: `0.003653`
- val_structured_mae: `0.040541`
- val_structured_rmse: `0.040820`

## Test Metrics

- test_loss: `0.008781`
- test_mae: `0.003569`
- test_rmse: `0.004019`
- test_structured_mae: `0.039411`
- test_structured_rmse: `0.039705`

## Interpretation

The held-out val error stayed finite with MAE=0.003179 deg and RMSE=0.003653 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003569 deg and RMSE=0.004019 deg, which indicates a numerically stable baseline run.
