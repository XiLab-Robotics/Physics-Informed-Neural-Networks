# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0010`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-01-49-04__te_periodic_mlp_h04_standard_global_optuna_t0010\checkpoints\periodic_mlp-epoch=078-val_mae=0.00299353.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007115`
- val_mae: `0.002994`
- val_rmse: `0.003538`

## Test Metrics

- test_loss: `0.007166`
- test_mae: `0.003186`
- test_rmse: `0.003690`

## Interpretation

The held-out val error stayed finite with MAE=0.002994 deg and RMSE=0.003538 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003186 deg and RMSE=0.003690 deg, which indicates a numerically stable baseline run.
