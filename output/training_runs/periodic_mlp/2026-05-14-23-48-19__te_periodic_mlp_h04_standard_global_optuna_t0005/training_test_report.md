# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0005`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-14-23-48-19__te_periodic_mlp_h04_standard_global_optuna_t0005\checkpoints\periodic_mlp-epoch=070-val_mae=0.00309759.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007968`
- val_mae: `0.003098`
- val_rmse: `0.003638`

## Test Metrics

- test_loss: `0.009620`
- test_mae: `0.003685`
- test_rmse: `0.004266`

## Interpretation

The held-out val error stayed finite with MAE=0.003098 deg and RMSE=0.003638 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003685 deg and RMSE=0.004266 deg, which indicates a numerically stable baseline run.
