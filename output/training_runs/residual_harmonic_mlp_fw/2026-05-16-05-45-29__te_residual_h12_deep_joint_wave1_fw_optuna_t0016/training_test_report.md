# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_Fw_optuna_t0016`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-16-05-45-29__te_residual_h12_deep_joint_wave1_fw_optuna_t0016\checkpoints\residual_harmonic_mlp-epoch=028-val_mae=0.00285559.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.025696`
- val_mae: `0.002856`
- val_rmse: `0.003538`
- val_structured_mae: `0.018238`
- val_structured_rmse: `0.021571`

## Test Metrics

- test_loss: `0.034331`
- test_mae: `0.003620`
- test_rmse: `0.004317`
- test_structured_mae: `0.021202`
- test_structured_rmse: `0.024295`

## Interpretation

The held-out val error stayed finite with MAE=0.002856 deg and RMSE=0.003538 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003620 deg and RMSE=0.004317 deg, which indicates a numerically stable baseline run.
