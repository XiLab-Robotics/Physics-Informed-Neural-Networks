# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0007`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-17-48-29__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0007\checkpoints\feedforward-epoch=041-val_mae=0.00285624.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024898`
- val_mae: `0.002856`
- val_rmse: `0.003433`

## Test Metrics

- test_loss: `0.029131`
- test_mae: `0.003364`
- test_rmse: `0.003893`

## Interpretation

The held-out val error stayed finite with MAE=0.002856 deg and RMSE=0.003433 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003364 deg and RMSE=0.003893 deg, which indicates a numerically stable baseline run.
