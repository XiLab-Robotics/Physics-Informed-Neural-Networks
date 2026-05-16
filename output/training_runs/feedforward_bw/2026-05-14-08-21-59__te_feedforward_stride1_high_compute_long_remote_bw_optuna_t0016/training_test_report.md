# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Bw_optuna_t0016`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_bw\2026-05-14-08-21-59__te_feedforward_stride1_high_compute_long_remote_bw_optuna_t0016\checkpoints\feedforward-epoch=197-val_mae=0.00290145.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025898`
- val_mae: `0.002901`
- val_rmse: `0.003557`

## Test Metrics

- test_loss: `0.025799`
- test_mae: `0.003173`
- test_rmse: `0.003818`

## Interpretation

The held-out val error stayed finite with MAE=0.002901 deg and RMSE=0.003557 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003173 deg and RMSE=0.003818 deg, which indicates a numerically stable baseline run.
