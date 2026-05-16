# Feedforward Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_global_optuna_t0017`
- Model Family: `feedforward`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward\2026-05-13-12-37-35__te_feedforward_stride1_high_compute_long_remote_global_optuna_t0017\checkpoints\feedforward-epoch=132-val_mae=0.00296250.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007182`
- val_mae: `0.002962`
- val_rmse: `0.003610`

## Test Metrics

- test_loss: `0.007221`
- test_mae: `0.003208`
- test_rmse: `0.003810`

## Interpretation

The held-out val error stayed finite with MAE=0.002962 deg and RMSE=0.003610 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003208 deg and RMSE=0.003810 deg, which indicates a numerically stable baseline run.
