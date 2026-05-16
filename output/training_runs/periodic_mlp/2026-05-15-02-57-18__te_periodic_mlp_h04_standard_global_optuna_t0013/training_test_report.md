# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0013`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-02-57-18__te_periodic_mlp_h04_standard_global_optuna_t0013\checkpoints\periodic_mlp-epoch=048-val_mae=0.00298797.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007363`
- val_mae: `0.002988`
- val_rmse: `0.003499`

## Test Metrics

- test_loss: `0.008421`
- test_mae: `0.003441`
- test_rmse: `0.003949`

## Interpretation

The held-out val error stayed finite with MAE=0.002988 deg and RMSE=0.003499 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003441 deg and RMSE=0.003949 deg, which indicates a numerically stable baseline run.
