# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0000`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-04-43-35__te_periodic_mlp_h04_standard_bw_optuna_t0000\checkpoints\periodic_mlp-epoch=016-val_mae=0.00331322.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.029582`
- val_mae: `0.003313`
- val_rmse: `0.003775`

## Test Metrics

- test_loss: `0.028652`
- test_mae: `0.003479`
- test_rmse: `0.003912`

## Interpretation

The held-out val error stayed finite with MAE=0.003313 deg and RMSE=0.003775 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003479 deg and RMSE=0.003912 deg, which indicates a numerically stable baseline run.
