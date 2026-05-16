# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0009`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-13-23-16-02__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0009\checkpoints\feedforward-epoch=089-val_mae=0.00306058.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027380`
- val_mae: `0.003061`
- val_rmse: `0.003557`

## Test Metrics

- test_loss: `0.029194`
- test_mae: `0.003486`
- test_rmse: `0.003963`

## Interpretation

The held-out val error stayed finite with MAE=0.003061 deg and RMSE=0.003557 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003486 deg and RMSE=0.003963 deg, which indicates a numerically stable baseline run.
