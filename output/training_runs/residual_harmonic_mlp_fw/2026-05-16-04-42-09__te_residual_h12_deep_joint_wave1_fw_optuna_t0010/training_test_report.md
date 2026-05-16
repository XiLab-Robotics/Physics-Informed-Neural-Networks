# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0010`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-04-42-09__te_residual_h12_deep_joint_wave1_fw_optuna_t0010\checkpoints\residual_harmonic_mlp-epoch=034-val_mae=0.00281446.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023443`
- val_mae: `0.002814`
- val_rmse: `0.003441`
- val_structured_mae: `0.018087`
- val_structured_rmse: `0.021340`

## Test Metrics

- test_loss: `0.028055`
- test_mae: `0.003294`
- test_rmse: `0.003867`
- test_structured_mae: `0.021095`
- test_structured_rmse: `0.024090`

## Interpretation

The held-out val error stayed finite with MAE=0.002814 deg and RMSE=0.003441 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003294 deg and RMSE=0.003867 deg, which indicates a numerically stable baseline run.
