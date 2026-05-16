# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0008`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-11-07-39__te_periodic_mlp_h04_standard_fw_optuna_t0008\checkpoints\periodic_mlp-epoch=038-val_mae=0.00280913.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023347`
- val_mae: `0.002809`
- val_rmse: `0.003372`

## Test Metrics

- test_loss: `0.027981`
- test_mae: `0.003287`
- test_rmse: `0.003833`

## Interpretation

The held-out val error stayed finite with MAE=0.002809 deg and RMSE=0.003372 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003287 deg and RMSE=0.003833 deg, which indicates a numerically stable baseline run.
