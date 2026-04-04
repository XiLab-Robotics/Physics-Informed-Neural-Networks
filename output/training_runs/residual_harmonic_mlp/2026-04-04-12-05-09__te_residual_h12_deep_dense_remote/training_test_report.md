# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_dense_remote`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-04-04-12-05-09__te_residual_h12_deep_dense_remote\checkpoints\residual_harmonic_mlp-epoch=069-val_mae=0.00301834.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007393`
- val_mae: `0.003018`
- val_rmse: `0.003549`
- val_structured_mae: `0.040518`
- val_structured_rmse: `0.042630`

## Test Metrics

- test_loss: `0.007883`
- test_mae: `0.003365`
- test_rmse: `0.003868`
- test_structured_mae: `0.039402`
- test_structured_rmse: `0.042814`

## Interpretation

The held-out val error stayed finite with MAE=0.003018 deg and RMSE=0.003549 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003365 deg and RMSE=0.003868 deg, which indicates a numerically stable baseline run.
