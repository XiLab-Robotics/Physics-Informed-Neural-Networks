# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0000`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-13-49-58__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0000\checkpoints\feedforward-epoch=051-val_mae=0.00283834.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025549`
- val_mae: `0.002838`
- val_rmse: `0.003315`

## Test Metrics

- test_loss: `0.032722`
- test_mae: `0.003487`
- test_rmse: `0.003928`

## Interpretation

The held-out val error stayed finite with MAE=0.002838 deg and RMSE=0.003315 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003487 deg and RMSE=0.003928 deg, which indicates a numerically stable baseline run.
