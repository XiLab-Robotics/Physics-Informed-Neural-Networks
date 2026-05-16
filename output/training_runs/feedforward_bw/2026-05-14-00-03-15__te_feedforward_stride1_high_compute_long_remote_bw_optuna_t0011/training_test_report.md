# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0011`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-14-00-03-15__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0011\checkpoints\feedforward-epoch=190-val_mae=0.00294061.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026358`
- val_mae: `0.002941`
- val_rmse: `0.003581`

## Test Metrics

- test_loss: `0.025114`
- test_mae: `0.003234`
- test_rmse: `0.003775`

## Interpretation

The held-out val error stayed finite with MAE=0.002941 deg and RMSE=0.003581 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003234 deg and RMSE=0.003775 deg, which indicates a numerically stable baseline run.
