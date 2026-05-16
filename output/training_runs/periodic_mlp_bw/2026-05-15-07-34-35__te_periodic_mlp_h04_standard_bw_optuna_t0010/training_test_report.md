# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0010`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-07-34-35__te_periodic_mlp_h04_standard_bw_optuna_t0010\checkpoints\periodic_mlp-epoch=076-val_mae=0.00296267.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027134`
- val_mae: `0.002963`
- val_rmse: `0.003641`

## Test Metrics

- test_loss: `0.025995`
- test_mae: `0.003248`
- test_rmse: `0.003817`

## Interpretation

The held-out val error stayed finite with MAE=0.002963 deg and RMSE=0.003641 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003248 deg and RMSE=0.003817 deg, which indicates a numerically stable baseline run.
