# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0013`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-05-14-07__te_residual_h12_deep_joint_wave1_fw_optuna_t0013\checkpoints\residual_harmonic_mlp-epoch=029-val_mae=0.00279168.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024154`
- val_mae: `0.002792`
- val_rmse: `0.003445`
- val_structured_mae: `0.018312`
- val_structured_rmse: `0.021678`

## Test Metrics

- test_loss: `0.029084`
- test_mae: `0.003373`
- test_rmse: `0.003941`
- test_structured_mae: `0.021256`
- test_structured_rmse: `0.024390`

## Interpretation

The held-out val error stayed finite with MAE=0.002792 deg and RMSE=0.003445 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003373 deg and RMSE=0.003941 deg, which indicates a numerically stable baseline run.
