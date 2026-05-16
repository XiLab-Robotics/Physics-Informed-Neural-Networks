# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0002`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-13-15-56-08__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0002\checkpoints\feedforward-epoch=089-val_mae=0.00303546.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027207`
- val_mae: `0.003035`
- val_rmse: `0.003726`

## Test Metrics

- test_loss: `0.026219`
- test_mae: `0.003243`
- test_rmse: `0.003964`

## Interpretation

The held-out val error stayed finite with MAE=0.003035 deg and RMSE=0.003726 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003243 deg and RMSE=0.003964 deg, which indicates a numerically stable baseline run.
