# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0003`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-16-10-36__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0003\checkpoints\feedforward-epoch=060-val_mae=0.00282053.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024147`
- val_mae: `0.002821`
- val_rmse: `0.003472`

## Test Metrics

- test_loss: `0.028197`
- test_mae: `0.003280`
- test_rmse: `0.003903`

## Interpretation

The held-out val error stayed finite with MAE=0.002821 deg and RMSE=0.003472 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003280 deg and RMSE=0.003903 deg, which indicates a numerically stable baseline run.
