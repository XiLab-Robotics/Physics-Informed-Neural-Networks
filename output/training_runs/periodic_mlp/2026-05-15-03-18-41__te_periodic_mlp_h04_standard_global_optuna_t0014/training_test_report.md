# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0014`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-03-18-41__te_periodic_mlp_h04_standard_global_optuna_t0014\checkpoints\periodic_mlp-epoch=038-val_mae=0.00299186.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007239`
- val_mae: `0.002992`
- val_rmse: `0.003518`

## Test Metrics

- test_loss: `0.008004`
- test_mae: `0.003402`
- test_rmse: `0.003880`

## Interpretation

The held-out val error stayed finite with MAE=0.002992 deg and RMSE=0.003518 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003402 deg and RMSE=0.003880 deg, which indicates a numerically stable baseline run.
