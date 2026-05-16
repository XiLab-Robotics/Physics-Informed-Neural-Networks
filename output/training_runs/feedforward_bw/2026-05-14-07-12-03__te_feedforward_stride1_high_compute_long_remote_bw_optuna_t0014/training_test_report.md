# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0014`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-14-07-12-03__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0014\checkpoints\feedforward-epoch=110-val_mae=0.00290484.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026119`
- val_mae: `0.002905`
- val_rmse: `0.003532`

## Test Metrics

- test_loss: `0.026413`
- test_mae: `0.003243`
- test_rmse: `0.003830`

## Interpretation

The held-out val error stayed finite with MAE=0.002905 deg and RMSE=0.003532 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003243 deg and RMSE=0.003830 deg, which indicates a numerically stable baseline run.
