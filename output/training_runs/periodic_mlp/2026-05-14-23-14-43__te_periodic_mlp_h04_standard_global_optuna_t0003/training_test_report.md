# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0003`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-14-23-14-43__te_periodic_mlp_h04_standard_global_optuna_t0003\checkpoints\periodic_mlp-epoch=048-val_mae=0.00316225.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007653`
- val_mae: `0.003162`
- val_rmse: `0.003601`

## Test Metrics

- test_loss: `0.007658`
- test_mae: `0.003344`
- test_rmse: `0.003713`

## Interpretation

The held-out val error stayed finite with MAE=0.003162 deg and RMSE=0.003601 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003344 deg and RMSE=0.003713 deg, which indicates a numerically stable baseline run.
