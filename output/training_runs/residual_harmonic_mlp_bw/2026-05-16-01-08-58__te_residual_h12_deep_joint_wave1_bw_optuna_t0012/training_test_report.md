# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0012`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-16-01-08-58__te_residual_h12_deep_joint_wave1_bw_optuna_t0012\checkpoints\residual_harmonic_mlp-epoch=107-val_mae=0.00297927.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027612`
- val_mae: `0.002979`
- val_rmse: `0.003479`
- val_structured_mae: `0.017523`
- val_structured_rmse: `0.018867`

## Test Metrics

- test_loss: `0.025837`
- test_mae: `0.003180`
- test_rmse: `0.003642`
- test_structured_mae: `0.021527`
- test_structured_rmse: `0.023003`

## Interpretation

The held-out val error stayed finite with MAE=0.002979 deg and RMSE=0.003479 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003180 deg and RMSE=0.003642 deg, which indicates a numerically stable baseline run.
