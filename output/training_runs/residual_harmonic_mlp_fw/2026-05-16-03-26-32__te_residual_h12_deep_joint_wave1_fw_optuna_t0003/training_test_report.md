# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0003`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-03-26-32__te_residual_h12_deep_joint_wave1_fw_optuna_t0003\checkpoints\residual_harmonic_mlp-epoch=024-val_mae=0.00299798.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025607`
- val_mae: `0.002998`
- val_rmse: `0.003490`
- val_structured_mae: `0.016589`
- val_structured_rmse: `0.017937`

## Test Metrics

- test_loss: `0.029922`
- test_mae: `0.003402`
- test_rmse: `0.003838`
- test_structured_mae: `0.020019`
- test_structured_rmse: `0.021549`

## Interpretation

The held-out val error stayed finite with MAE=0.002998 deg and RMSE=0.003490 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003402 deg and RMSE=0.003838 deg, which indicates a numerically stable baseline run.
