# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Bw_optuna_t0003`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_bw\2026-05-15-05-26-38__te_periodic_mlp_h04_standard_bw_optuna_t0003\checkpoints\periodic_mlp-epoch=055-val_mae=0.00319438.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.030313`
- val_mae: `0.003194`
- val_rmse: `0.003692`

## Test Metrics

- test_loss: `0.033158`
- test_mae: `0.003669`
- test_rmse: `0.004130`

## Interpretation

The held-out val error stayed finite with MAE=0.003194 deg and RMSE=0.003692 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003669 deg and RMSE=0.004130 deg, which indicates a numerically stable baseline run.
