# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0017`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-05-53-29__te_residual_h12_deep_joint_wave1_fw_optuna_t0017\checkpoints\residual_harmonic_mlp-epoch=027-val_mae=0.00282862.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023631`
- val_mae: `0.002829`
- val_rmse: `0.003446`
- val_structured_mae: `0.017905`
- val_structured_rmse: `0.021058`

## Test Metrics

- test_loss: `0.030692`
- test_mae: `0.003389`
- test_rmse: `0.004062`
- test_structured_mae: `0.020959`
- test_structured_rmse: `0.023841`

## Interpretation

The held-out val error stayed finite with MAE=0.002829 deg and RMSE=0.003446 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003389 deg and RMSE=0.004062 deg, which indicates a numerically stable baseline run.
