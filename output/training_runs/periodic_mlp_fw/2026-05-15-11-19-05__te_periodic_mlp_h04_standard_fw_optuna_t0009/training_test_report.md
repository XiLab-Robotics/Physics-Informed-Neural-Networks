# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0009`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-11-19-05__te_periodic_mlp_h04_standard_fw_optuna_t0009\checkpoints\periodic_mlp-epoch=031-val_mae=0.00283370.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024612`
- val_mae: `0.002834`
- val_rmse: `0.003497`

## Test Metrics

- test_loss: `0.028688`
- test_mae: `0.003320`
- test_rmse: `0.003934`

## Interpretation

The held-out val error stayed finite with MAE=0.002834 deg and RMSE=0.003497 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003320 deg and RMSE=0.003934 deg, which indicates a numerically stable baseline run.
