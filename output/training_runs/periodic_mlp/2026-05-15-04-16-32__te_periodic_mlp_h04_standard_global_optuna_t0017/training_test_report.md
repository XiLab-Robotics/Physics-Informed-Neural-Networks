# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0017`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-04-16-32__te_periodic_mlp_h04_standard_global_optuna_t0017\checkpoints\periodic_mlp-epoch=067-val_mae=0.00299552.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007359`
- val_mae: `0.002996`
- val_rmse: `0.003502`

## Test Metrics

- test_loss: `0.007969`
- test_mae: `0.003344`
- test_rmse: `0.003830`

## Interpretation

The held-out val error stayed finite with MAE=0.002996 deg and RMSE=0.003502 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003344 deg and RMSE=0.003830 deg, which indicates a numerically stable baseline run.
