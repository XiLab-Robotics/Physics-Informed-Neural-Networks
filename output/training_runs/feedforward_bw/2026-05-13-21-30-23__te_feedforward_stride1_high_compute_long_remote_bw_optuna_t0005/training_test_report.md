# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0005`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-13-21-30-23__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0005\checkpoints\feedforward-epoch=115-val_mae=0.00301752.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027221`
- val_mae: `0.003018`
- val_rmse: `0.003527`

## Test Metrics

- test_loss: `0.025229`
- test_mae: `0.003099`
- test_rmse: `0.003630`

## Interpretation

The held-out val error stayed finite with MAE=0.003018 deg and RMSE=0.003527 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003099 deg and RMSE=0.003630 deg, which indicates a numerically stable baseline run.
