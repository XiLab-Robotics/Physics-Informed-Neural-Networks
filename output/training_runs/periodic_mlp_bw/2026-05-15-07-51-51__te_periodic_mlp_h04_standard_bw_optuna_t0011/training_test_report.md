# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0011`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-07-51-51__te_periodic_mlp_h04_standard_bw_optuna_t0011\checkpoints\periodic_mlp-epoch=103-val_mae=0.00305790.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.028187`
- val_mae: `0.003058`
- val_rmse: `0.003709`

## Test Metrics

- test_loss: `0.027302`
- test_mae: `0.003271`
- test_rmse: `0.003889`

## Interpretation

The held-out val error stayed finite with MAE=0.003058 deg and RMSE=0.003709 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003271 deg and RMSE=0.003889 deg, which indicates a numerically stable baseline run.
