# Periodic Mlp Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_global_optuna_t0008`
- Model Family: `periodic_mlp`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-05-15-01-05-40__te_periodic_mlp_h04_standard_global_optuna_t0008\checkpoints\periodic_mlp-epoch=079-val_mae=0.00305702.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007220`
- val_mae: `0.003057`
- val_rmse: `0.003678`

## Test Metrics

- test_loss: `0.007147`
- test_mae: `0.003200`
- test_rmse: `0.003798`

## Interpretation

The held-out val error stayed finite with MAE=0.003057 deg and RMSE=0.003678 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003200 deg and RMSE=0.003798 deg, which indicates a numerically stable baseline run.
