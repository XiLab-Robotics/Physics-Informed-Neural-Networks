# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0016`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-09-23-31__te_periodic_mlp_h04_standard_bw_optuna_t0016\checkpoints\periodic_mlp-epoch=071-val_mae=0.00322085.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.029374`
- val_mae: `0.003221`
- val_rmse: `0.003851`

## Test Metrics

- test_loss: `0.031710`
- test_mae: `0.003656`
- test_rmse: `0.004282`

## Interpretation

The held-out val error stayed finite with MAE=0.003221 deg and RMSE=0.003851 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003656 deg and RMSE=0.004282 deg, which indicates a numerically stable baseline run.
