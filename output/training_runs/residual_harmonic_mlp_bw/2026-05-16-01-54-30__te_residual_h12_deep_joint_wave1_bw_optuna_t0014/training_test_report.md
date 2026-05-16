# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0014`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-16-01-54-30__te_residual_h12_deep_joint_wave1_bw_optuna_t0014\checkpoints\residual_harmonic_mlp-epoch=049-val_mae=0.00295421.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027073`
- val_mae: `0.002954`
- val_rmse: `0.003433`
- val_structured_mae: `0.017560`
- val_structured_rmse: `0.018886`

## Test Metrics

- test_loss: `0.029171`
- test_mae: `0.003467`
- test_rmse: `0.003952`
- test_structured_mae: `0.021509`
- test_structured_rmse: `0.023012`

## Interpretation

The held-out val error stayed finite with MAE=0.002954 deg and RMSE=0.003433 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003467 deg and RMSE=0.003952 deg, which indicates a numerically stable baseline run.
