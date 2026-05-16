# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0004`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-16-27-52__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0004\checkpoints\feedforward-epoch=081-val_mae=0.00289434.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025545`
- val_mae: `0.002894`
- val_rmse: `0.003512`

## Test Metrics

- test_loss: `0.032380`
- test_mae: `0.003482`
- test_rmse: `0.004095`

## Interpretation

The held-out val error stayed finite with MAE=0.002894 deg and RMSE=0.003512 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003482 deg and RMSE=0.004095 deg, which indicates a numerically stable baseline run.
