# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0017`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-21-49-29__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0017\checkpoints\feedforward-epoch=040-val_mae=0.00281528.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024502`
- val_mae: `0.002815`
- val_rmse: `0.003494`

## Test Metrics

- test_loss: `0.029712`
- test_mae: `0.003372`
- test_rmse: `0.004017`

## Interpretation

The held-out val error stayed finite with MAE=0.002815 deg and RMSE=0.003494 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003372 deg and RMSE=0.004017 deg, which indicates a numerically stable baseline run.
