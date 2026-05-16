# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0007`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-04-11-14__te_residual_h12_deep_joint_wave1_fw_optuna_t0007\checkpoints\residual_harmonic_mlp-epoch=048-val_mae=0.00282934.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.023533`
- val_mae: `0.002829`
- val_rmse: `0.003468`
- val_structured_mae: `0.017014`
- val_structured_rmse: `0.019706`

## Test Metrics

- test_loss: `0.027126`
- test_mae: `0.003215`
- test_rmse: `0.003831`
- test_structured_mae: `0.020312`
- test_structured_rmse: `0.022659`

## Interpretation

The held-out val error stayed finite with MAE=0.002829 deg and RMSE=0.003468 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003215 deg and RMSE=0.003831 deg, which indicates a numerically stable baseline run.
