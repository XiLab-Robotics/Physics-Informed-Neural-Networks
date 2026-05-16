# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0005`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-05-57-04__te_periodic_mlp_h04_standard_bw_optuna_t0005\checkpoints\periodic_mlp-epoch=042-val_mae=0.00315875.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028912`
- val_mae: `0.003159`
- val_rmse: `0.003770`

## Test Metrics

- test_loss: `0.031731`
- test_mae: `0.003599`
- test_rmse: `0.004241`

## Interpretation

The held-out val error stayed finite with MAE=0.003159 deg and RMSE=0.003770 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003599 deg and RMSE=0.004241 deg, which indicates a numerically stable baseline run.
