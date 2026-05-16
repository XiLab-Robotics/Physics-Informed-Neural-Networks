# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0004`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-13-21-13-38__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0004\checkpoints\feedforward-epoch=056-val_mae=0.00300889.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027976`
- val_mae: `0.003009`
- val_rmse: `0.003658`

## Test Metrics

- test_loss: `0.028637`
- test_mae: `0.003383`
- test_rmse: `0.004006`

## Interpretation

The held-out val error stayed finite with MAE=0.003009 deg and RMSE=0.003658 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003383 deg and RMSE=0.004006 deg, which indicates a numerically stable baseline run.
