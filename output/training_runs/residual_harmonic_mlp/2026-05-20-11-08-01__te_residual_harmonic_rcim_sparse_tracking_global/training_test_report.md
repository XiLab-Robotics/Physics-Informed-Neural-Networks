# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_rcim_sparse_tracking_global`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-05-20-11-08-01__te_residual_harmonic_rcim_sparse_tracking_global\checkpoints\residual_harmonic_mlp-epoch=042-val_mae=0.00296875.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006964`
- val_mae: `0.002969`
- val_rmse: `0.003467`
- val_structured_mae: `0.040526`
- val_structured_rmse: `0.042578`

## Test Metrics

- test_loss: `0.007770`
- test_mae: `0.003378`
- test_rmse: `0.003902`
- test_structured_mae: `0.039405`
- test_structured_rmse: `0.042791`

## Interpretation

The held-out val error stayed finite with MAE=0.002969 deg and RMSE=0.003467 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003378 deg and RMSE=0.003902 deg, which indicates a numerically stable baseline run.
