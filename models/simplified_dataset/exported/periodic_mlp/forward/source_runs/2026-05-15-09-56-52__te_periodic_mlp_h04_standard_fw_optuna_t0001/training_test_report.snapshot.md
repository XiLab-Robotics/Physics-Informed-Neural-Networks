# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0001`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-09-56-52__te_periodic_mlp_h04_standard_fw_optuna_t0001\checkpoints\periodic_mlp-epoch=023-val_mae=0.00275063.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023330`
- val_mae: `0.002751`
- val_rmse: `0.003405`

## Test Metrics

- test_loss: `0.027948`
- test_mae: `0.003294`
- test_rmse: `0.003899`

## Interpretation

The held-out val error stayed finite with MAE=0.002751 deg and RMSE=0.003405 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003294 deg and RMSE=0.003899 deg, which indicates a numerically stable baseline run.
