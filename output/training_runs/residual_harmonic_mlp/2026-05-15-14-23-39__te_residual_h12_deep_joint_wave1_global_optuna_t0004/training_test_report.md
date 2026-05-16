# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0004`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-14-23-39__te_residual_h12_deep_joint_wave1_global_optuna_t0004\checkpoints\residual_harmonic_mlp-epoch=074-val_mae=0.00301037.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007252`
- val_mae: `0.003010`
- val_rmse: `0.003539`
- val_structured_mae: `0.040554`
- val_structured_rmse: `0.042551`

## Test Metrics

- test_loss: `0.007326`
- test_mae: `0.003226`
- test_rmse: `0.003744`
- test_structured_mae: `0.039416`
- test_structured_rmse: `0.042810`

## Interpretation

The held-out val error stayed finite with MAE=0.003010 deg and RMSE=0.003539 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003226 deg and RMSE=0.003744 deg, which indicates a numerically stable baseline run.
