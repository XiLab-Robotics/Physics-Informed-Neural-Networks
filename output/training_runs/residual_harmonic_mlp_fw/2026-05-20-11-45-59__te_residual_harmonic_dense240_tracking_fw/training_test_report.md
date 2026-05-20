# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_dense240_tracking_Fw`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-20-11-45-59__te_residual_harmonic_dense240_tracking_fw\checkpoints\residual_harmonic_mlp-epoch=019-val_mae=0.00264874.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.021462`
- val_mae: `0.002649`
- val_rmse: `0.003163`
- val_structured_mae: `0.016743`
- val_structured_rmse: `0.019016`

## Test Metrics

- test_loss: `0.027752`
- test_mae: `0.003304`
- test_rmse: `0.003773`
- test_structured_mae: `0.020117`
- test_structured_rmse: `0.022180`

## Interpretation

The held-out val error stayed finite with MAE=0.002649 deg and RMSE=0.003163 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003304 deg and RMSE=0.003773 deg, which indicates a numerically stable baseline run.
