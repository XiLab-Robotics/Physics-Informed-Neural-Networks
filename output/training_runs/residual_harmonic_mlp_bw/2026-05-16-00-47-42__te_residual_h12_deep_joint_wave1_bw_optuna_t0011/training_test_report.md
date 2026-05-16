# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0011`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-16-00-47-42__te_residual_h12_deep_joint_wave1_bw_optuna_t0011\checkpoints\residual_harmonic_mlp-epoch=096-val_mae=0.00299977.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027098`
- val_mae: `0.003000`
- val_rmse: `0.003483`
- val_structured_mae: `0.017504`
- val_structured_rmse: `0.018859`

## Test Metrics

- test_loss: `0.025929`
- test_mae: `0.003223`
- test_rmse: `0.003657`
- test_structured_mae: `0.021538`
- test_structured_rmse: `0.023002`

## Interpretation

The held-out val error stayed finite with MAE=0.003000 deg and RMSE=0.003483 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003223 deg and RMSE=0.003657 deg, which indicates a numerically stable baseline run.
