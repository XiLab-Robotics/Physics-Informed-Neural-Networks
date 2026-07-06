# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0006`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-06-09-21__te_periodic_mlp_h04_standard_bw_optuna_t0006\checkpoints\periodic_mlp-epoch=112-val_mae=0.00290718.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.026098`
- val_mae: `0.002907`
- val_rmse: `0.003537`

## Test Metrics

- test_loss: `0.026038`
- test_mae: `0.003233`
- test_rmse: `0.003792`

## Interpretation

The held-out val error stayed finite with MAE=0.002907 deg and RMSE=0.003537 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003233 deg and RMSE=0.003792 deg, which indicates a numerically stable baseline run.
