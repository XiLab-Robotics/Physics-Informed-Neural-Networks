# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0006`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-10-42-11__te_periodic_mlp_h04_standard_fw_optuna_t0006\checkpoints\periodic_mlp-epoch=047-val_mae=0.00279185.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023916`
- val_mae: `0.002792`
- val_rmse: `0.003445`

## Test Metrics

- test_loss: `0.029027`
- test_mae: `0.003338`
- test_rmse: `0.003969`

## Interpretation

The held-out val error stayed finite with MAE=0.002792 deg and RMSE=0.003445 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003338 deg and RMSE=0.003969 deg, which indicates a numerically stable baseline run.
