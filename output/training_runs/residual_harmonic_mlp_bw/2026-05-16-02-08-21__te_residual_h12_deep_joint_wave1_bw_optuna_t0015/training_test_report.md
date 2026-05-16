# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0015`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-16-02-08-21__te_residual_h12_deep_joint_wave1_bw_optuna_t0015\checkpoints\residual_harmonic_mlp-epoch=084-val_mae=0.00300792.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027977`
- val_mae: `0.003008`
- val_rmse: `0.003766`
- val_structured_mae: `0.017496`
- val_structured_rmse: `0.020003`

## Test Metrics

- test_loss: `0.029046`
- test_mae: `0.003426`
- test_rmse: `0.004125`
- test_structured_mae: `0.021544`
- test_structured_rmse: `0.023723`

## Interpretation

The held-out val error stayed finite with MAE=0.003008 deg and RMSE=0.003766 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003426 deg and RMSE=0.004125 deg, which indicates a numerically stable baseline run.
