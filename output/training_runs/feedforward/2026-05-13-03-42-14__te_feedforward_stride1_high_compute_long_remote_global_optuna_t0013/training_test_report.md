# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0013`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-05-13-03-42-14__te_feedforward_stride1_high_compute_long_remote_global_optuna_t0013\checkpoints\feedforward-epoch=061-val_mae=0.00300852.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007545`
- val_mae: `0.003009`
- val_rmse: `0.003572`

## Test Metrics

- test_loss: `0.008217`
- test_mae: `0.003409`
- test_rmse: `0.003947`

## Interpretation

The held-out val error stayed finite with MAE=0.003009 deg and RMSE=0.003572 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003409 deg and RMSE=0.003947 deg, which indicates a numerically stable baseline run.
