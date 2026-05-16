# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0012`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-08-09-59__te_periodic_mlp_h04_standard_bw_optuna_t0012\checkpoints\periodic_mlp-epoch=061-val_mae=0.00306124.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028761`
- val_mae: `0.003061`
- val_rmse: `0.003697`

## Test Metrics

- test_loss: `0.032564`
- test_mae: `0.003589`
- test_rmse: `0.004257`

## Interpretation

The held-out val error stayed finite with MAE=0.003061 deg and RMSE=0.003697 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003589 deg and RMSE=0.004257 deg, which indicates a numerically stable baseline run.
