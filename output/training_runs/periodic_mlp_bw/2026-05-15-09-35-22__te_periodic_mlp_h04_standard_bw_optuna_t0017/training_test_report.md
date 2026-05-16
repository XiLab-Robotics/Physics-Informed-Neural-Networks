# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0017`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-09-35-22__te_periodic_mlp_h04_standard_bw_optuna_t0017\checkpoints\periodic_mlp-epoch=040-val_mae=0.00321092.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.029557`
- val_mae: `0.003211`
- val_rmse: `0.003893`

## Test Metrics

- test_loss: `0.030274`
- test_mae: `0.003532`
- test_rmse: `0.004158`

## Interpretation

The held-out val error stayed finite with MAE=0.003211 deg and RMSE=0.003893 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003532 deg and RMSE=0.004158 deg, which indicates a numerically stable baseline run.
