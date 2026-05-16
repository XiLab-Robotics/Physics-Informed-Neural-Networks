# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0001`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-14-22-24-48__te_periodic_mlp_h04_standard_global_optuna_t0001\checkpoints\periodic_mlp-epoch=054-val_mae=0.00306191.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007924`
- val_mae: `0.003062`
- val_rmse: `0.003717`

## Test Metrics

- test_loss: `0.008898`
- test_mae: `0.003531`
- test_rmse: `0.004168`

## Interpretation

The held-out val error stayed finite with MAE=0.003062 deg and RMSE=0.003717 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003531 deg and RMSE=0.004168 deg, which indicates a numerically stable baseline run.
