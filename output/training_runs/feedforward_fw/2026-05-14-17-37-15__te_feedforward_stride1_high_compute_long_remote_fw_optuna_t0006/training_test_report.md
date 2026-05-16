# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0006`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-17-37-15__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0006\checkpoints\feedforward-epoch=021-val_mae=0.00280685.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025446`
- val_mae: `0.002807`
- val_rmse: `0.003283`

## Test Metrics

- test_loss: `0.032815`
- test_mae: `0.003531`
- test_rmse: `0.003990`

## Interpretation

The held-out val error stayed finite with MAE=0.002807 deg and RMSE=0.003283 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003531 deg and RMSE=0.003990 deg, which indicates a numerically stable baseline run.
