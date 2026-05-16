# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0017`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-21-10-56__te_residual_h12_deep_joint_wave1_global_optuna_t0017\checkpoints\residual_harmonic_mlp-epoch=032-val_mae=0.00309573.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007944`
- val_mae: `0.003096`
- val_rmse: `0.003639`
- val_structured_mae: `0.040540`
- val_structured_rmse: `0.042558`

## Test Metrics

- test_loss: `0.008666`
- test_mae: `0.003506`
- test_rmse: `0.004031`
- test_structured_mae: `0.039410`
- test_structured_rmse: `0.042800`

## Interpretation

The held-out val error stayed finite with MAE=0.003096 deg and RMSE=0.003639 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003506 deg and RMSE=0.004031 deg, which indicates a numerically stable baseline run.
