# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0013`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-11-57-05__te_periodic_mlp_h04_standard_fw_optuna_t0013\checkpoints\periodic_mlp-epoch=051-val_mae=0.00279052.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024629`
- val_mae: `0.002791`
- val_rmse: `0.003376`

## Test Metrics

- test_loss: `0.030077`
- test_mae: `0.003372`
- test_rmse: `0.003950`

## Interpretation

The held-out val error stayed finite with MAE=0.002791 deg and RMSE=0.003376 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003372 deg and RMSE=0.003950 deg, which indicates a numerically stable baseline run.
