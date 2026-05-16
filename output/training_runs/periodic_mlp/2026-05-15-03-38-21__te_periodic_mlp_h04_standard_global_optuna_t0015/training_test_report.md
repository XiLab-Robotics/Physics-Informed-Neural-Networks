# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0015`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-03-38-21__te_periodic_mlp_h04_standard_global_optuna_t0015\checkpoints\periodic_mlp-epoch=072-val_mae=0.00306445.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007295`
- val_mae: `0.003064`
- val_rmse: `0.003684`

## Test Metrics

- test_loss: `0.007500`
- test_mae: `0.003280`
- test_rmse: `0.003873`

## Interpretation

The held-out val error stayed finite with MAE=0.003064 deg and RMSE=0.003684 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003280 deg and RMSE=0.003873 deg, which indicates a numerically stable baseline run.
