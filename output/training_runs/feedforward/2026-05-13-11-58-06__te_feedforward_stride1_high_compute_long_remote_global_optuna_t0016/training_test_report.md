# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0016`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-05-13-11-58-06__te_feedforward_stride1_high_compute_long_remote_global_optuna_t0016\checkpoints\feedforward-epoch=072-val_mae=0.00299788.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007534`
- val_mae: `0.002998`
- val_rmse: `0.003646`

## Test Metrics

- test_loss: `0.008610`
- test_mae: `0.003465`
- test_rmse: `0.004147`

## Interpretation

The held-out val error stayed finite with MAE=0.002998 deg and RMSE=0.003646 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003465 deg and RMSE=0.004147 deg, which indicates a numerically stable baseline run.
