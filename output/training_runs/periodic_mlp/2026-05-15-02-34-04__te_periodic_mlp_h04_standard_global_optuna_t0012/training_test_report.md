# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0012`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-02-34-04__te_periodic_mlp_h04_standard_global_optuna_t0012\checkpoints\periodic_mlp-epoch=084-val_mae=0.00301103.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007294`
- val_mae: `0.003011`
- val_rmse: `0.003562`

## Test Metrics

- test_loss: `0.007525`
- test_mae: `0.003290`
- test_rmse: `0.003786`

## Interpretation

The held-out val error stayed finite with MAE=0.003011 deg and RMSE=0.003562 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003290 deg and RMSE=0.003786 deg, which indicates a numerically stable baseline run.
