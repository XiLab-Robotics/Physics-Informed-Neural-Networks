# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0014`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-08-50-24__te_periodic_mlp_h04_standard_bw_optuna_t0014\checkpoints\periodic_mlp-epoch=114-val_mae=0.00303794.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028476`
- val_mae: `0.003038`
- val_rmse: `0.003679`

## Test Metrics

- test_loss: `0.030541`
- test_mae: `0.003466`
- test_rmse: `0.004092`

## Interpretation

The held-out val error stayed finite with MAE=0.003038 deg and RMSE=0.003679 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003466 deg and RMSE=0.004092 deg, which indicates a numerically stable baseline run.
