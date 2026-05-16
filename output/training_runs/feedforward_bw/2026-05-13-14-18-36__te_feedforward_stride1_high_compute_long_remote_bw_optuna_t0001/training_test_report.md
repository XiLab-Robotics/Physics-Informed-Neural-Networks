# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0001`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-13-14-18-36__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0001\checkpoints\feedforward-epoch=080-val_mae=0.00299728.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027256`
- val_mae: `0.002997`
- val_rmse: `0.003729`

## Test Metrics

- test_loss: `0.027661`
- test_mae: `0.003286`
- test_rmse: `0.004043`

## Interpretation

The held-out val error stayed finite with MAE=0.002997 deg and RMSE=0.003729 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003286 deg and RMSE=0.004043 deg, which indicates a numerically stable baseline run.
