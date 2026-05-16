# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0010`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-11-29-13__te_periodic_mlp_h04_standard_fw_optuna_t0010\checkpoints\periodic_mlp-epoch=029-val_mae=0.00280340.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024461`
- val_mae: `0.002803`
- val_rmse: `0.003479`

## Test Metrics

- test_loss: `0.030130`
- test_mae: `0.003368`
- test_rmse: `0.004043`

## Interpretation

The held-out val error stayed finite with MAE=0.002803 deg and RMSE=0.003479 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003368 deg and RMSE=0.004043 deg, which indicates a numerically stable baseline run.
