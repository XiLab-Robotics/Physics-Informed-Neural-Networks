# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0016`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-21-34-57__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0016\checkpoints\feedforward-epoch=033-val_mae=0.00287661.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024709`
- val_mae: `0.002877`
- val_rmse: `0.003529`

## Test Metrics

- test_loss: `0.031408`
- test_mae: `0.003449`
- test_rmse: `0.004134`

## Interpretation

The held-out val error stayed finite with MAE=0.002877 deg and RMSE=0.003529 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003449 deg and RMSE=0.004134 deg, which indicates a numerically stable baseline run.
