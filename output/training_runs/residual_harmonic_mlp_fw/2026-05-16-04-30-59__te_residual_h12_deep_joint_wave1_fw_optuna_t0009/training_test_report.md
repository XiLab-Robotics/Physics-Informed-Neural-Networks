# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0009`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-04-30-59__te_residual_h12_deep_joint_wave1_fw_optuna_t0009\checkpoints\residual_harmonic_mlp-epoch=038-val_mae=0.00279382.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023517`
- val_mae: `0.002794`
- val_rmse: `0.003443`
- val_structured_mae: `0.017895`
- val_structured_rmse: `0.021049`

## Test Metrics

- test_loss: `0.027483`
- test_mae: `0.003211`
- test_rmse: `0.003828`
- test_structured_mae: `0.020953`
- test_structured_rmse: `0.023833`

## Interpretation

The held-out val error stayed finite with MAE=0.002794 deg and RMSE=0.003443 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003211 deg and RMSE=0.003828 deg, which indicates a numerically stable baseline run.
