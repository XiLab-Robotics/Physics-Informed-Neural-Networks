# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0011`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-18-58-47__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0011\checkpoints\feedforward-epoch=022-val_mae=0.00285474.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024951`
- val_mae: `0.002855`
- val_rmse: `0.003530`

## Test Metrics

- test_loss: `0.028108`
- test_mae: `0.003268`
- test_rmse: `0.003909`

## Interpretation

The held-out val error stayed finite with MAE=0.002855 deg and RMSE=0.003530 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003268 deg and RMSE=0.003909 deg, which indicates a numerically stable baseline run.
