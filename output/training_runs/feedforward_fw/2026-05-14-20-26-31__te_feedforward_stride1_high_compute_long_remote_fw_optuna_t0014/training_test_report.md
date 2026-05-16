# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0014`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-20-26-31__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0014\checkpoints\feedforward-epoch=049-val_mae=0.00284621.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024156`
- val_mae: `0.002846`
- val_rmse: `0.003498`

## Test Metrics

- test_loss: `0.027140`
- test_mae: `0.003232`
- test_rmse: `0.003812`

## Interpretation

The held-out val error stayed finite with MAE=0.002846 deg and RMSE=0.003498 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003232 deg and RMSE=0.003812 deg, which indicates a numerically stable baseline run.
