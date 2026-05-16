# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0013`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-14-06-44-15__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0013\checkpoints\feedforward-epoch=121-val_mae=0.00298927.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027240`
- val_mae: `0.002989`
- val_rmse: `0.003656`

## Test Metrics

- test_loss: `0.024767`
- test_mae: `0.003106`
- test_rmse: `0.003700`

## Interpretation

The held-out val error stayed finite with MAE=0.002989 deg and RMSE=0.003656 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003106 deg and RMSE=0.003700 deg, which indicates a numerically stable baseline run.
