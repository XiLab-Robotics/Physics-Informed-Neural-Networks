# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0014`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-05-24-02__te_residual_h12_deep_joint_wave1_fw_optuna_t0014\checkpoints\residual_harmonic_mlp-epoch=042-val_mae=0.00283525.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025505`
- val_mae: `0.002835`
- val_rmse: `0.003519`
- val_structured_mae: `0.018056`
- val_structured_rmse: `0.021291`

## Test Metrics

- test_loss: `0.032646`
- test_mae: `0.003505`
- test_rmse: `0.004202`
- test_structured_mae: `0.021069`
- test_structured_rmse: `0.024047`

## Interpretation

The held-out val error stayed finite with MAE=0.002835 deg and RMSE=0.003519 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003505 deg and RMSE=0.004202 deg, which indicates a numerically stable baseline run.
