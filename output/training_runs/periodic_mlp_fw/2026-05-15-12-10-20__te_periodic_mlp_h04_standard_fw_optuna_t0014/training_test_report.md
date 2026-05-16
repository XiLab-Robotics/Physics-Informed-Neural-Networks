# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0014`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-12-10-20__te_periodic_mlp_h04_standard_fw_optuna_t0014\checkpoints\periodic_mlp-epoch=043-val_mae=0.00276782.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024228`
- val_mae: `0.002768`
- val_rmse: `0.003359`

## Test Metrics

- test_loss: `0.031116`
- test_mae: `0.003448`
- test_rmse: `0.004036`

## Interpretation

The held-out val error stayed finite with MAE=0.002768 deg and RMSE=0.003359 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003448 deg and RMSE=0.004036 deg, which indicates a numerically stable baseline run.
