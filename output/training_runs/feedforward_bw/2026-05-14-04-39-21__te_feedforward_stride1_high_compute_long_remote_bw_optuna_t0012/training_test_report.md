# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0012`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-14-04-39-21__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0012\checkpoints\feedforward-epoch=074-val_mae=0.00296184.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026756`
- val_mae: `0.002962`
- val_rmse: `0.003605`

## Test Metrics

- test_loss: `0.026806`
- test_mae: `0.003263`
- test_rmse: `0.003822`

## Interpretation

The held-out val error stayed finite with MAE=0.002962 deg and RMSE=0.003605 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003263 deg and RMSE=0.003822 deg, which indicates a numerically stable baseline run.
