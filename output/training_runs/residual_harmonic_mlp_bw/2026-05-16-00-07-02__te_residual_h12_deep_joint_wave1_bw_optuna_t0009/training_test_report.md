# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0009`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-16-00-07-02__te_residual_h12_deep_joint_wave1_bw_optuna_t0009\checkpoints\residual_harmonic_mlp-epoch=077-val_mae=0.00299661.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027637`
- val_mae: `0.002997`
- val_rmse: `0.003492`
- val_structured_mae: `0.017568`
- val_structured_rmse: `0.018892`

## Test Metrics

- test_loss: `0.027593`
- test_mae: `0.003267`
- test_rmse: `0.003810`
- test_structured_mae: `0.021506`
- test_structured_rmse: `0.023015`

## Interpretation

The held-out val error stayed finite with MAE=0.002997 deg and RMSE=0.003492 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003267 deg and RMSE=0.003810 deg, which indicates a numerically stable baseline run.
