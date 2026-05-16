# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0000`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-02-55-21__te_residual_h12_deep_joint_wave1_fw_optuna_t0000\checkpoints\residual_harmonic_mlp-epoch=022-val_mae=0.00290055.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026471`
- val_mae: `0.002901`
- val_rmse: `0.003365`
- val_structured_mae: `0.016567`
- val_structured_rmse: `0.017930`

## Test Metrics

- test_loss: `0.032011`
- test_mae: `0.003529`
- test_rmse: `0.003975`
- test_structured_mae: `0.020018`
- test_structured_rmse: `0.021539`

## Interpretation

The held-out val error stayed finite with MAE=0.002901 deg and RMSE=0.003365 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003529 deg and RMSE=0.003975 deg, which indicates a numerically stable baseline run.
