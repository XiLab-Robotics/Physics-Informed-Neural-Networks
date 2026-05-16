# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0017`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-14-13-21-56__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0017\checkpoints\feedforward-epoch=086-val_mae=0.00313629.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.029205`
- val_mae: `0.003136`
- val_rmse: `0.003782`

## Test Metrics

- test_loss: `0.029969`
- test_mae: `0.003499`
- test_rmse: `0.004114`

## Interpretation

The held-out val error stayed finite with MAE=0.003136 deg and RMSE=0.003782 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003499 deg and RMSE=0.004114 deg, which indicates a numerically stable baseline run.
