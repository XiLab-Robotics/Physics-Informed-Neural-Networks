# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0003`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-10-14-37__te_periodic_mlp_h04_standard_fw_optuna_t0003\checkpoints\periodic_mlp-epoch=008-val_mae=0.00278554.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024724`
- val_mae: `0.002786`
- val_rmse: `0.003252`

## Test Metrics

- test_loss: `0.030810`
- test_mae: `0.003421`
- test_rmse: `0.003888`

## Interpretation

The held-out val error stayed finite with MAE=0.002786 deg and RMSE=0.003252 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003421 deg and RMSE=0.003888 deg, which indicates a numerically stable baseline run.
