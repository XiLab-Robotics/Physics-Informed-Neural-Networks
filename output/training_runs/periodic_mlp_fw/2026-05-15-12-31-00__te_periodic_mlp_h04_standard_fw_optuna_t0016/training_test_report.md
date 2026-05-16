# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0016`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-12-31-00__te_periodic_mlp_h04_standard_fw_optuna_t0016\checkpoints\periodic_mlp-epoch=025-val_mae=0.00289682.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025211`
- val_mae: `0.002897`
- val_rmse: `0.003464`

## Test Metrics

- test_loss: `0.028923`
- test_mae: `0.003365`
- test_rmse: `0.003905`

## Interpretation

The held-out val error stayed finite with MAE=0.002897 deg and RMSE=0.003464 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003365 deg and RMSE=0.003905 deg, which indicates a numerically stable baseline run.
