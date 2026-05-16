# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0007`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-16-02-29__te_residual_h12_deep_joint_wave1_global_optuna_t0007\checkpoints\residual_harmonic_mlp-epoch=113-val_mae=0.00293687.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007048`
- val_mae: `0.002937`
- val_rmse: `0.003480`
- val_structured_mae: `0.040557`
- val_structured_rmse: `0.042549`

## Test Metrics

- test_loss: `0.007518`
- test_mae: `0.003273`
- test_rmse: `0.003849`
- test_structured_mae: `0.039418`
- test_structured_rmse: `0.042813`

## Interpretation

The held-out val error stayed finite with MAE=0.002937 deg and RMSE=0.003480 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003273 deg and RMSE=0.003849 deg, which indicates a numerically stable baseline run.
