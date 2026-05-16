# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0005`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-16-48-01__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0005\checkpoints\feedforward-epoch=086-val_mae=0.00274640.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.022728`
- val_mae: `0.002746`
- val_rmse: `0.003373`

## Test Metrics

- test_loss: `0.027919`
- test_mae: `0.003287`
- test_rmse: `0.003911`

## Interpretation

The held-out val error stayed finite with MAE=0.002746 deg and RMSE=0.003373 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003287 deg and RMSE=0.003911 deg, which indicates a numerically stable baseline run.
