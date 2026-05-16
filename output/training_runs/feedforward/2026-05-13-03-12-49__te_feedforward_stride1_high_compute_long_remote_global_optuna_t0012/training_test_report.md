# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0012`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-05-13-03-12-49__te_feedforward_stride1_high_compute_long_remote_global_optuna_t0012\checkpoints\feedforward-epoch=060-val_mae=0.00301413.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007260`
- val_mae: `0.003014`
- val_rmse: `0.003666`

## Test Metrics

- test_loss: `0.007290`
- test_mae: `0.003217`
- test_rmse: `0.003847`

## Interpretation

The held-out val error stayed finite with MAE=0.003014 deg and RMSE=0.003666 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003217 deg and RMSE=0.003847 deg, which indicates a numerically stable baseline run.
