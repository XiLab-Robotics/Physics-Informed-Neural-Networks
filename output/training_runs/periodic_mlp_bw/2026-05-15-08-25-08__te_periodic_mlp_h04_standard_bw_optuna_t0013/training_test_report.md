# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0013`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-08-25-08__te_periodic_mlp_h04_standard_bw_optuna_t0013\checkpoints\periodic_mlp-epoch=130-val_mae=0.00292461.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026751`
- val_mae: `0.002925`
- val_rmse: `0.003548`

## Test Metrics

- test_loss: `0.027501`
- test_mae: `0.003329`
- test_rmse: `0.003896`

## Interpretation

The held-out val error stayed finite with MAE=0.002925 deg and RMSE=0.003548 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003329 deg and RMSE=0.003896 deg, which indicates a numerically stable baseline run.
