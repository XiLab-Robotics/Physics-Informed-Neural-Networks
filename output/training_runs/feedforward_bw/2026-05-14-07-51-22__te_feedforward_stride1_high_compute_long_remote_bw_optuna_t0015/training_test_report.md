# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0015`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-14-07-51-22__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0015\checkpoints\feedforward-epoch=121-val_mae=0.00305623.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027152`
- val_mae: `0.003056`
- val_rmse: `0.003560`

## Test Metrics

- test_loss: `0.024619`
- test_mae: `0.003224`
- test_rmse: `0.003684`

## Interpretation

The held-out val error stayed finite with MAE=0.003056 deg and RMSE=0.003560 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003224 deg and RMSE=0.003684 deg, which indicates a numerically stable baseline run.
