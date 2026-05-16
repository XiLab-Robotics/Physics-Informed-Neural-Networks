# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0008`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-13-22-45-29__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0008\checkpoints\feedforward-epoch=171-val_mae=0.00293628.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026815`
- val_mae: `0.002936`
- val_rmse: `0.003581`

## Test Metrics

- test_loss: `0.028652`
- test_mae: `0.003401`
- test_rmse: `0.004012`

## Interpretation

The held-out val error stayed finite with MAE=0.002936 deg and RMSE=0.003581 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003401 deg and RMSE=0.004012 deg, which indicates a numerically stable baseline run.
