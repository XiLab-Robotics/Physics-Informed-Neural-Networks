# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0004`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-05-39-16__te_periodic_mlp_h04_standard_bw_optuna_t0004\checkpoints\periodic_mlp-epoch=080-val_mae=0.00299454.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028044`
- val_mae: `0.002995`
- val_rmse: `0.003641`

## Test Metrics

- test_loss: `0.030874`
- test_mae: `0.003498`
- test_rmse: `0.004066`

## Interpretation

The held-out val error stayed finite with MAE=0.002995 deg and RMSE=0.003641 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003498 deg and RMSE=0.004066 deg, which indicates a numerically stable baseline run.
