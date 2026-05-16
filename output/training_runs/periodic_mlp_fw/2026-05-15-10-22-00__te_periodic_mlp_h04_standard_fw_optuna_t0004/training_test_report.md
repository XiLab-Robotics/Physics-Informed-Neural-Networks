# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0004`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-10-22-00__te_periodic_mlp_h04_standard_fw_optuna_t0004\checkpoints\periodic_mlp-epoch=016-val_mae=0.00276034.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024494`
- val_mae: `0.002760`
- val_rmse: `0.003354`

## Test Metrics

- test_loss: `0.031132`
- test_mae: `0.003420`
- test_rmse: `0.004025`

## Interpretation

The held-out val error stayed finite with MAE=0.002760 deg and RMSE=0.003354 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003420 deg and RMSE=0.004025 deg, which indicates a numerically stable baseline run.
