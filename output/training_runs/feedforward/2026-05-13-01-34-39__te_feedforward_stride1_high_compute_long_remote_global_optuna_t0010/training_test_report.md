# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0010`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-05-13-01-34-39__te_feedforward_stride1_high_compute_long_remote_global_optuna_t0010\checkpoints\feedforward-epoch=040-val_mae=0.00303766.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007389`
- val_mae: `0.003038`
- val_rmse: `0.003724`

## Test Metrics

- test_loss: `0.007732`
- test_mae: `0.003333`
- test_rmse: `0.003989`

## Interpretation

The held-out val error stayed finite with MAE=0.003038 deg and RMSE=0.003724 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003333 deg and RMSE=0.003989 deg, which indicates a numerically stable baseline run.
