# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Bw_optuna_t0008`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-15-23-50-38__te_residual_h12_deep_joint_wave1_bw_optuna_t0008\checkpoints\residual_harmonic_mlp-epoch=065-val_mae=0.00296999.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.027431`
- val_mae: `0.002970`
- val_rmse: `0.003457`
- val_structured_mae: `0.017579`
- val_structured_rmse: `0.018898`

## Test Metrics

- test_loss: `0.033224`
- test_mae: `0.003641`
- test_rmse: `0.004137`
- test_structured_mae: `0.021502`
- test_structured_rmse: `0.023018`

## Interpretation

The held-out val error stayed finite with MAE=0.002970 deg and RMSE=0.003457 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003641 deg and RMSE=0.004137 deg, which indicates a numerically stable baseline run.
