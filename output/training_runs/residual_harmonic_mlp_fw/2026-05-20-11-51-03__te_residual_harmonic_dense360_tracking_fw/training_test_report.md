# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_dense360_tracking_Fw`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-20-11-51-03__te_residual_harmonic_dense360_tracking_fw\checkpoints\residual_harmonic_mlp-epoch=022-val_mae=0.00259842.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023569`
- val_mae: `0.002598`
- val_rmse: `0.003136`
- val_structured_mae: `0.016625`
- val_structured_rmse: `0.018831`

## Test Metrics

- test_loss: `0.033479`
- test_mae: `0.003568`
- test_rmse: `0.004118`
- test_structured_mae: `0.020052`
- test_structured_rmse: `0.022022`

## Interpretation

The held-out val error stayed finite with MAE=0.002598 deg and RMSE=0.003136 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003568 deg and RMSE=0.004118 deg, which indicates a numerically stable baseline run.
