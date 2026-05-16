# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0017`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-12-40-34__te_periodic_mlp_h04_standard_fw_optuna_t0017\checkpoints\periodic_mlp-epoch=006-val_mae=0.00280714.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023741`
- val_mae: `0.002807`
- val_rmse: `0.003382`

## Test Metrics

- test_loss: `0.027999`
- test_mae: `0.003308`
- test_rmse: `0.003834`

## Interpretation

The held-out val error stayed finite with MAE=0.002807 deg and RMSE=0.003382 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003308 deg and RMSE=0.003834 deg, which indicates a numerically stable baseline run.
