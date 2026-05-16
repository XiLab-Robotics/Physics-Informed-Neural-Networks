# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0013`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-20-15-34__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0013\checkpoints\feedforward-epoch=022-val_mae=0.00282402.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024419`
- val_mae: `0.002824`
- val_rmse: `0.003504`

## Test Metrics

- test_loss: `0.029975`
- test_mae: `0.003357`
- test_rmse: `0.004017`

## Interpretation

The held-out val error stayed finite with MAE=0.002824 deg and RMSE=0.003504 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003357 deg and RMSE=0.004017 deg, which indicates a numerically stable baseline run.
