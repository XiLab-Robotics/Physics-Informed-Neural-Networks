# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0003`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-15-22-25-38__te_residual_h12_deep_joint_wave1_bw_optuna_t0003\checkpoints\residual_harmonic_mlp-epoch=040-val_mae=0.00304337.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028832`
- val_mae: `0.003043`
- val_rmse: `0.003539`
- val_structured_mae: `0.017560`
- val_structured_rmse: `0.018889`

## Test Metrics

- test_loss: `0.031649`
- test_mae: `0.003532`
- test_rmse: `0.004006`
- test_structured_mae: `0.021510`
- test_structured_rmse: `0.023014`

## Interpretation

The held-out val error stayed finite with MAE=0.003043 deg and RMSE=0.003539 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003532 deg and RMSE=0.004006 deg, which indicates a numerically stable baseline run.
