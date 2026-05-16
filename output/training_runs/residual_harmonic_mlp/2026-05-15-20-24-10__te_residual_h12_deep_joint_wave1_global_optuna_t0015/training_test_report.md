# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0015`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-20-24-10__te_residual_h12_deep_joint_wave1_global_optuna_t0015\checkpoints\residual_harmonic_mlp-epoch=094-val_mae=0.00295785.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007214`
- val_mae: `0.002958`
- val_rmse: `0.003591`
- val_structured_mae: `0.040563`
- val_structured_rmse: `0.043998`

## Test Metrics

- test_loss: `0.007913`
- test_mae: `0.003382`
- test_rmse: `0.003983`
- test_structured_mae: `0.039421`
- test_structured_rmse: `0.044780`

## Interpretation

The held-out val error stayed finite with MAE=0.002958 deg and RMSE=0.003591 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003382 deg and RMSE=0.003983 deg, which indicates a numerically stable baseline run.
