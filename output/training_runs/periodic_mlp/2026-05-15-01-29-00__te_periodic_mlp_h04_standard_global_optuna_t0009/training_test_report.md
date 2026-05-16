# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0009`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-01-29-00__te_periodic_mlp_h04_standard_global_optuna_t0009\checkpoints\periodic_mlp-epoch=040-val_mae=0.00311959.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007294`
- val_mae: `0.003120`
- val_rmse: `0.003639`

## Test Metrics

- test_loss: `0.007424`
- test_mae: `0.003301`
- test_rmse: `0.003818`

## Interpretation

The held-out val error stayed finite with MAE=0.003120 deg and RMSE=0.003639 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003301 deg and RMSE=0.003818 deg, which indicates a numerically stable baseline run.
