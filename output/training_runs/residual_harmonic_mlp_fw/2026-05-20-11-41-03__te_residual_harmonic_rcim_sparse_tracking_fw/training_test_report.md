# Residual Harmonic Mlp Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_rcim_sparse_tracking_Fw`
- Model Family: `residual_harmonic_mlp_fw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_fw\2026-05-20-11-41-03__te_residual_harmonic_rcim_sparse_tracking_fw\checkpoints\residual_harmonic_mlp-epoch=029-val_mae=0.00270433.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.021776`
- val_mae: `0.002704`
- val_rmse: `0.003196`
- val_structured_mae: `0.016599`
- val_structured_rmse: `0.018768`

## Test Metrics

- test_loss: `0.023898`
- test_mae: `0.003089`
- test_rmse: `0.003498`
- test_structured_mae: `0.020026`
- test_structured_rmse: `0.021975`

## Interpretation

The held-out val error stayed finite with MAE=0.002704 deg and RMSE=0.003196 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003089 deg and RMSE=0.003498 deg, which indicates a numerically stable baseline run.
