# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0013`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-19-39-19__te_residual_h12_deep_joint_wave1_global_optuna_t0013\checkpoints\residual_harmonic_mlp-epoch=050-val_mae=0.00297835.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007137`
- val_mae: `0.002978`
- val_rmse: `0.003517`
- val_structured_mae: `0.040568`
- val_structured_rmse: `0.042553`

## Test Metrics

- test_loss: `0.007791`
- test_mae: `0.003377`
- test_rmse: `0.003933`
- test_structured_mae: `0.039423`
- test_structured_rmse: `0.042824`

## Interpretation

The held-out val error stayed finite with MAE=0.002978 deg and RMSE=0.003517 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003377 deg and RMSE=0.003933 deg, which indicates a numerically stable baseline run.
