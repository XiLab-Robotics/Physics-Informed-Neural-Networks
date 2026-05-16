# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0011`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-02-18-44__te_periodic_mlp_h04_standard_global_optuna_t0011\checkpoints\periodic_mlp-epoch=028-val_mae=0.00305594.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007859`
- val_mae: `0.003056`
- val_rmse: `0.003573`

## Test Metrics

- test_loss: `0.009533`
- test_mae: `0.003696`
- test_rmse: `0.004227`

## Interpretation

The held-out val error stayed finite with MAE=0.003056 deg and RMSE=0.003573 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003696 deg and RMSE=0.004227 deg, which indicates a numerically stable baseline run.
