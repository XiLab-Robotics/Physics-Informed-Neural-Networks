# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0003`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-13-16-19-04__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0003\checkpoints\feedforward-epoch=112-val_mae=0.00297608.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027947`
- val_mae: `0.002976`
- val_rmse: `0.003702`

## Test Metrics

- test_loss: `0.028642`
- test_mae: `0.003388`
- test_rmse: `0.004143`

## Interpretation

The held-out val error stayed finite with MAE=0.002976 deg and RMSE=0.003702 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003388 deg and RMSE=0.004143 deg, which indicates a numerically stable baseline run.
