# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0007`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-13-22-25-09__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0007\checkpoints\feedforward-epoch=117-val_mae=0.00309500.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028699`
- val_mae: `0.003095`
- val_rmse: `0.003582`

## Test Metrics

- test_loss: `0.028641`
- test_mae: `0.003358`
- test_rmse: `0.003837`

## Interpretation

The held-out val error stayed finite with MAE=0.003095 deg and RMSE=0.003582 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003358 deg and RMSE=0.003837 deg, which indicates a numerically stable baseline run.
