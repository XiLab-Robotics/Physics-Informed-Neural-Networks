# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0007`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-06-31-51__te_periodic_mlp_h04_standard_bw_optuna_t0007\checkpoints\periodic_mlp-epoch=153-val_mae=0.00293255.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026171`
- val_mae: `0.002933`
- val_rmse: `0.003546`

## Test Metrics

- test_loss: `0.026238`
- test_mae: `0.003239`
- test_rmse: `0.003820`

## Interpretation

The held-out val error stayed finite with MAE=0.002933 deg and RMSE=0.003546 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003239 deg and RMSE=0.003820 deg, which indicates a numerically stable baseline run.
