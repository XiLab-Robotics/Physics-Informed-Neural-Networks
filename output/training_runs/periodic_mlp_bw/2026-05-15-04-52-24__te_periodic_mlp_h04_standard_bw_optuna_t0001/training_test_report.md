# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0001`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-04-52-24__te_periodic_mlp_h04_standard_bw_optuna_t0001\checkpoints\periodic_mlp-epoch=115-val_mae=0.00308155.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027377`
- val_mae: `0.003082`
- val_rmse: `0.003743`

## Test Metrics

- test_loss: `0.028537`
- test_mae: `0.003386`
- test_rmse: `0.004135`

## Interpretation

The held-out val error stayed finite with MAE=0.003082 deg and RMSE=0.003743 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003386 deg and RMSE=0.004135 deg, which indicates a numerically stable baseline run.
