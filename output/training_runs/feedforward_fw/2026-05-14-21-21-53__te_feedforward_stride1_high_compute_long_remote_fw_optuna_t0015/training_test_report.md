# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0015`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-21-21-53__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0015\checkpoints\feedforward-epoch=036-val_mae=0.00287092.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025035`
- val_mae: `0.002871`
- val_rmse: `0.003369`

## Test Metrics

- test_loss: `0.030905`
- test_mae: `0.003420`
- test_rmse: `0.003873`

## Interpretation

The held-out val error stayed finite with MAE=0.002871 deg and RMSE=0.003369 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003420 deg and RMSE=0.003873 deg, which indicates a numerically stable baseline run.
