# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0009`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-07-12-22__te_periodic_mlp_h04_standard_bw_optuna_t0009\checkpoints\periodic_mlp-epoch=132-val_mae=0.00313978.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028609`
- val_mae: `0.003140`
- val_rmse: `0.003763`

## Test Metrics

- test_loss: `0.028072`
- test_mae: `0.003318`
- test_rmse: `0.003889`

## Interpretation

The held-out val error stayed finite with MAE=0.003140 deg and RMSE=0.003763 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003318 deg and RMSE=0.003889 deg, which indicates a numerically stable baseline run.
