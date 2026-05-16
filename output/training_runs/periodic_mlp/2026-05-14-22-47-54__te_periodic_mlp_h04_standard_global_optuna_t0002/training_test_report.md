# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0002`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-14-22-47-54__te_periodic_mlp_h04_standard_global_optuna_t0002\checkpoints\periodic_mlp-epoch=060-val_mae=0.00308753.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007369`
- val_mae: `0.003088`
- val_rmse: `0.003525`

## Test Metrics

- test_loss: `0.007777`
- test_mae: `0.003348`
- test_rmse: `0.003779`

## Interpretation

The held-out val error stayed finite with MAE=0.003088 deg and RMSE=0.003525 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003348 deg and RMSE=0.003779 deg, which indicates a numerically stable baseline run.
