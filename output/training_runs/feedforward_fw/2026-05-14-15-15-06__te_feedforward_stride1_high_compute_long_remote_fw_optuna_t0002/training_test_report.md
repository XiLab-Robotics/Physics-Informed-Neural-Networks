# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0002`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-15-15-06__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0002\checkpoints\feedforward-epoch=059-val_mae=0.00290430.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024756`
- val_mae: `0.002904`
- val_rmse: `0.003539`

## Test Metrics

- test_loss: `0.029149`
- test_mae: `0.003301`
- test_rmse: `0.003958`

## Interpretation

The held-out val error stayed finite with MAE=0.002904 deg and RMSE=0.003539 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003301 deg and RMSE=0.003958 deg, which indicates a numerically stable baseline run.
