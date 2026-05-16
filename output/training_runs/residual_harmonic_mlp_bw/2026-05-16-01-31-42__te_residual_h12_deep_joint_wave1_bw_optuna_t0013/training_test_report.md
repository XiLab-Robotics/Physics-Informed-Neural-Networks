# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0013`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-16-01-31-42__te_residual_h12_deep_joint_wave1_bw_optuna_t0013\checkpoints\residual_harmonic_mlp-epoch=107-val_mae=0.00305075.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027896`
- val_mae: `0.003051`
- val_rmse: `0.003554`
- val_structured_mae: `0.017585`
- val_structured_rmse: `0.018901`

## Test Metrics

- test_loss: `0.025868`
- test_mae: `0.003195`
- test_rmse: `0.003636`
- test_structured_mae: `0.021500`
- test_structured_rmse: `0.023020`

## Interpretation

The held-out val error stayed finite with MAE=0.003051 deg and RMSE=0.003554 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003195 deg and RMSE=0.003636 deg, which indicates a numerically stable baseline run.
