# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_joint_wave1_global_optuna_t0016`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Davide\Desktop\PINNs\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-15-20-51-47__te_residual_h12_deep_joint_wave1_global_optuna_t0016\checkpoints\residual_harmonic_mlp-epoch=036-val_mae=0.00307465.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007775`
- val_mae: `0.003075`
- val_rmse: `0.003620`
- val_structured_mae: `0.040622`
- val_structured_rmse: `0.042566`

## Test Metrics

- test_loss: `0.008736`
- test_mae: `0.003559`
- test_rmse: `0.004077`
- test_structured_mae: `0.039449`
- test_structured_rmse: `0.042892`

## Interpretation

The held-out val error stayed finite with MAE=0.003075 deg and RMSE=0.003620 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003559 deg and RMSE=0.004077 deg, which indicates a numerically stable baseline run.
