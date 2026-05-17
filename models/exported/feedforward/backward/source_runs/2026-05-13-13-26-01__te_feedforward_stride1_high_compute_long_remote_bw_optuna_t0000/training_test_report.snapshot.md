# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0000`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-13-13-26-01__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0000\checkpoints\feedforward-epoch=209-val_mae=0.00287506.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025324`
- val_mae: `0.002875`
- val_rmse: `0.003346`

## Test Metrics

- test_loss: `0.026413`
- test_mae: `0.003276`
- test_rmse: `0.003767`

## Interpretation

The held-out val error stayed finite with MAE=0.002875 deg and RMSE=0.003346 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003276 deg and RMSE=0.003767 deg, which indicates a numerically stable baseline run.
