# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0004`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-03-33-32__te_residual_h12_deep_joint_wave1_fw_optuna_t0004\checkpoints\residual_harmonic_mlp-epoch=036-val_mae=0.00280993.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025681`
- val_mae: `0.002810`
- val_rmse: `0.003413`
- val_structured_mae: `0.017113`
- val_structured_rmse: `0.019620`

## Test Metrics

- test_loss: `0.033080`
- test_mae: `0.003527`
- test_rmse: `0.004142`
- test_structured_mae: `0.020382`
- test_structured_rmse: `0.022680`

## Interpretation

The held-out val error stayed finite with MAE=0.002810 deg and RMSE=0.003413 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003527 deg and RMSE=0.004142 deg, which indicates a numerically stable baseline run.
