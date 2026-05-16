# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0002`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-15-22-10-18__te_residual_h12_deep_joint_wave1_bw_optuna_t0002\checkpoints\residual_harmonic_mlp-epoch=058-val_mae=0.00308715.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027882`
- val_mae: `0.003087`
- val_rmse: `0.003590`
- val_structured_mae: `0.017495`
- val_structured_rmse: `0.018865`

## Test Metrics

- test_loss: `0.025372`
- test_mae: `0.003206`
- test_rmse: `0.003720`
- test_structured_mae: `0.021546`
- test_structured_rmse: `0.023010`

## Interpretation

The held-out val error stayed finite with MAE=0.003087 deg and RMSE=0.003590 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003206 deg and RMSE=0.003720 deg, which indicates a numerically stable baseline run.
