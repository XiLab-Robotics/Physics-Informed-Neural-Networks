# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0000`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-14-22-03-11__te_periodic_mlp_h04_standard_global_optuna_t0000\checkpoints\periodic_mlp-epoch=041-val_mae=0.00313128.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007535`
- val_mae: `0.003131`
- val_rmse: `0.003581`

## Test Metrics

- test_loss: `0.007669`
- test_mae: `0.003321`
- test_rmse: `0.003732`

## Interpretation

The held-out val error stayed finite with MAE=0.003131 deg and RMSE=0.003581 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003321 deg and RMSE=0.003732 deg, which indicates a numerically stable baseline run.
