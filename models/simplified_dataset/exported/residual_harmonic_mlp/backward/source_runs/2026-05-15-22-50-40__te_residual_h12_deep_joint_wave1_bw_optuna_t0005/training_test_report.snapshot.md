# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0005`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-15-22-50-40__te_residual_h12_deep_joint_wave1_bw_optuna_t0005\checkpoints\residual_harmonic_mlp-epoch=115-val_mae=0.00292969.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026877`
- val_mae: `0.002930`
- val_rmse: `0.003413`
- val_structured_mae: `0.017547`
- val_structured_rmse: `0.018879`

## Test Metrics

- test_loss: `0.029218`
- test_mae: `0.003454`
- test_rmse: `0.003918`
- test_structured_mae: `0.021515`
- test_structured_rmse: `0.023008`

## Interpretation

The held-out val error stayed finite with MAE=0.002930 deg and RMSE=0.003413 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003454 deg and RMSE=0.003918 deg, which indicates a numerically stable baseline run.
