# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0012`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-11-48-55__te_periodic_mlp_h04_standard_fw_optuna_t0012\checkpoints\periodic_mlp-epoch=026-val_mae=0.00283193.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023927`
- val_mae: `0.002832`
- val_rmse: `0.003430`

## Test Metrics

- test_loss: `0.028576`
- test_mae: `0.003299`
- test_rmse: `0.003876`

## Interpretation

The held-out val error stayed finite with MAE=0.002832 deg and RMSE=0.003430 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003299 deg and RMSE=0.003876 deg, which indicates a numerically stable baseline run.
