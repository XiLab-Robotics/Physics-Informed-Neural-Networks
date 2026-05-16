# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0010`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-18-41-35__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0010\checkpoints\feedforward-epoch=062-val_mae=0.00281712.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023615`
- val_mae: `0.002817`
- val_rmse: `0.003396`

## Test Metrics

- test_loss: `0.027486`
- test_mae: `0.003232`
- test_rmse: `0.003798`

## Interpretation

The held-out val error stayed finite with MAE=0.002817 deg and RMSE=0.003396 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003232 deg and RMSE=0.003798 deg, which indicates a numerically stable baseline run.
