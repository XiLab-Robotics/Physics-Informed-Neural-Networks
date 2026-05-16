# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0011`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-05-13-02-11-16__te_feedforward_stride1_high_compute_long_remote_global_optuna_t0011\checkpoints\feedforward-epoch=178-val_mae=0.00302833.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007417`
- val_mae: `0.003028`
- val_rmse: `0.003547`

## Test Metrics

- test_loss: `0.007430`
- test_mae: `0.003238`
- test_rmse: `0.003725`

## Interpretation

The held-out val error stayed finite with MAE=0.003028 deg and RMSE=0.003547 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003238 deg and RMSE=0.003725 deg, which indicates a numerically stable baseline run.
