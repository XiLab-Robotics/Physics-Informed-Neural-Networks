# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0015`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-05-35-44__te_residual_h12_deep_joint_wave1_fw_optuna_t0015\checkpoints\residual_harmonic_mlp-epoch=026-val_mae=0.00289046.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023775`
- val_mae: `0.002890`
- val_rmse: `0.003437`
- val_structured_mae: `0.016763`
- val_structured_rmse: `0.019063`

## Test Metrics

- test_loss: `0.026486`
- test_mae: `0.003252`
- test_rmse: `0.003737`
- test_structured_mae: `0.020139`
- test_structured_rmse: `0.022213`

## Interpretation

The held-out val error stayed finite with MAE=0.002890 deg and RMSE=0.003437 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003252 deg and RMSE=0.003737 deg, which indicates a numerically stable baseline run.
