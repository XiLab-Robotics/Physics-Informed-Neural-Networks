# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0015`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-09-13-13__te_periodic_mlp_h04_standard_bw_optuna_t0015\checkpoints\periodic_mlp-epoch=064-val_mae=0.00310363.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027707`
- val_mae: `0.003104`
- val_rmse: `0.003774`

## Test Metrics

- test_loss: `0.027783`
- test_mae: `0.003363`
- test_rmse: `0.004052`

## Interpretation

The held-out val error stayed finite with MAE=0.003104 deg and RMSE=0.003774 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003363 deg and RMSE=0.004052 deg, which indicates a numerically stable baseline run.
