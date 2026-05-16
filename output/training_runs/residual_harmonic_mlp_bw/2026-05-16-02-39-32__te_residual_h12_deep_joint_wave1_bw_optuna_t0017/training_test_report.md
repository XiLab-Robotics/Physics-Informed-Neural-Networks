# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0017`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-16-02-39-32__te_residual_h12_deep_joint_wave1_bw_optuna_t0017\checkpoints\residual_harmonic_mlp-epoch=061-val_mae=0.00307458.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027513`
- val_mae: `0.003075`
- val_rmse: `0.003577`
- val_structured_mae: `0.017491`
- val_structured_rmse: `0.018866`

## Test Metrics

- test_loss: `0.026182`
- test_mae: `0.003271`
- test_rmse: `0.003738`
- test_structured_mae: `0.021549`
- test_structured_rmse: `0.023012`

## Interpretation

The held-out val error stayed finite with MAE=0.003075 deg and RMSE=0.003577 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003271 deg and RMSE=0.003738 deg, which indicates a numerically stable baseline run.
