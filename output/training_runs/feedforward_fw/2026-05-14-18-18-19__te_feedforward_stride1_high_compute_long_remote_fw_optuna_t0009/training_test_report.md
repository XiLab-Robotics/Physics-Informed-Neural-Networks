# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_stride1_high_compute_long_remote_Fw_optuna_t0009`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\feedforward_fw\2026-05-14-18-18-19__te_feedforward_stride1_high_compute_long_remote_fw_optuna_t0009\checkpoints\feedforward-epoch=078-val_mae=0.00284968.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023758`
- val_mae: `0.002850`
- val_rmse: `0.003473`

## Test Metrics

- test_loss: `0.026670`
- test_mae: `0.003229`
- test_rmse: `0.003774`

## Interpretation

The held-out val error stayed finite with MAE=0.002850 deg and RMSE=0.003473 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003229 deg and RMSE=0.003774 deg, which indicates a numerically stable baseline run.
