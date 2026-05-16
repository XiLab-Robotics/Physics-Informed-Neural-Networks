# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0015`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-12-22-29__te_periodic_mlp_h04_standard_fw_optuna_t0015\checkpoints\periodic_mlp-epoch=019-val_mae=0.00280160.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023819`
- val_mae: `0.002802`
- val_rmse: `0.003453`

## Test Metrics

- test_loss: `0.028289`
- test_mae: `0.003296`
- test_rmse: `0.003924`

## Interpretation

The held-out val error stayed finite with MAE=0.002802 deg and RMSE=0.003453 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003296 deg and RMSE=0.003924 deg, which indicates a numerically stable baseline run.
