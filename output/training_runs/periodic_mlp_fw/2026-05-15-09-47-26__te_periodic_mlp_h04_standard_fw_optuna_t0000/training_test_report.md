# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0000`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-09-47-26__te_periodic_mlp_h04_standard_fw_optuna_t0000\checkpoints\periodic_mlp-epoch=022-val_mae=0.00286426.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025748`
- val_mae: `0.002864`
- val_rmse: `0.003358`

## Test Metrics

- test_loss: `0.034158`
- test_mae: `0.003574`
- test_rmse: `0.004022`

## Interpretation

The held-out val error stayed finite with MAE=0.002864 deg and RMSE=0.003358 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003574 deg and RMSE=0.004022 deg, which indicates a numerically stable baseline run.
