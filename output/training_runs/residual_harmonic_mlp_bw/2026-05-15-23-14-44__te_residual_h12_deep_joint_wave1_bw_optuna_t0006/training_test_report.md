# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0006`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-15-23-14-44__te_residual_h12_deep_joint_wave1_bw_optuna_t0006\checkpoints\residual_harmonic_mlp-epoch=071-val_mae=0.00299287.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027009`
- val_mae: `0.002993`
- val_rmse: `0.003701`
- val_structured_mae: `0.017565`
- val_structured_rmse: `0.020083`

## Test Metrics

- test_loss: `0.027489`
- test_mae: `0.003358`
- test_rmse: `0.004051`
- test_structured_mae: `0.021507`
- test_structured_rmse: `0.023691`

## Interpretation

The held-out val error stayed finite with MAE=0.002993 deg and RMSE=0.003701 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003358 deg and RMSE=0.004051 deg, which indicates a numerically stable baseline run.
