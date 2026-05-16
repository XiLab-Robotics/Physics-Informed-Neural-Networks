# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0006`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-00-16-09__te_periodic_mlp_h04_standard_global_optuna_t0006\checkpoints\periodic_mlp-epoch=075-val_mae=0.00296443.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007178`
- val_mae: `0.002964`
- val_rmse: `0.003495`

## Test Metrics

- test_loss: `0.007404`
- test_mae: `0.003233`
- test_rmse: `0.003733`

## Interpretation

The held-out val error stayed finite with MAE=0.002964 deg and RMSE=0.003495 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003233 deg and RMSE=0.003733 deg, which indicates a numerically stable baseline run.
