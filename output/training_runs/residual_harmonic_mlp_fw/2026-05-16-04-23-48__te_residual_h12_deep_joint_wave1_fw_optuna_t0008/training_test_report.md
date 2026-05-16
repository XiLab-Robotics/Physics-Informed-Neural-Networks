# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0008`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-04-23-48__te_residual_h12_deep_joint_wave1_fw_optuna_t0008\checkpoints\residual_harmonic_mlp-epoch=008-val_mae=0.00288346.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024850`
- val_mae: `0.002883`
- val_rmse: `0.003464`
- val_structured_mae: `0.016806`
- val_structured_rmse: `0.019128`

## Test Metrics

- test_loss: `0.029893`
- test_mae: `0.003376`
- test_rmse: `0.003960`
- test_structured_mae: `0.020169`
- test_structured_rmse: `0.022267`

## Interpretation

The held-out val error stayed finite with MAE=0.002883 deg and RMSE=0.003464 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003376 deg and RMSE=0.003960 deg, which indicates a numerically stable baseline run.
