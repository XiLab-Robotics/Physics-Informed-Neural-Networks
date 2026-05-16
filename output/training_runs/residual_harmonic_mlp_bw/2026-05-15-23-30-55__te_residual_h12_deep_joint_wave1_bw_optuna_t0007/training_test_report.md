# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0007`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-15-23-30-55__te_residual_h12_deep_joint_wave1_bw_optuna_t0007\checkpoints\residual_harmonic_mlp-epoch=092-val_mae=0.00294754.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026983`
- val_mae: `0.002948`
- val_rmse: `0.003626`
- val_structured_mae: `0.017557`
- val_structured_rmse: `0.019827`

## Test Metrics

- test_loss: `0.026000`
- test_mae: `0.003162`
- test_rmse: `0.003862`
- test_structured_mae: `0.021510`
- test_structured_rmse: `0.023487`

## Interpretation

The held-out val error stayed finite with MAE=0.002948 deg and RMSE=0.003626 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003162 deg and RMSE=0.003862 deg, which indicates a numerically stable baseline run.
