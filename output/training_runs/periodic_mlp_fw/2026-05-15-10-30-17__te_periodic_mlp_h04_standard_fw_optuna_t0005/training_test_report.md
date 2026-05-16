# Periodic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_h04_standard_Fw_optuna_t0005`
- Model Family: `periodic_mlp_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_fw\2026-05-15-10-30-17__te_periodic_mlp_h04_standard_fw_optuna_t0005\checkpoints\periodic_mlp-epoch=059-val_mae=0.00285118.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025321`
- val_mae: `0.002851`
- val_rmse: `0.003517`

## Test Metrics

- test_loss: `0.030771`
- test_mae: `0.003428`
- test_rmse: `0.004078`

## Interpretation

The held-out val error stayed finite with MAE=0.002851 deg and RMSE=0.003517 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003428 deg and RMSE=0.004078 deg, which indicates a numerically stable baseline run.
