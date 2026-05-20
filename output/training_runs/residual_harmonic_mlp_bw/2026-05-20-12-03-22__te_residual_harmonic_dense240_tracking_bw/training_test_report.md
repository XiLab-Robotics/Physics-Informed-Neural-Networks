# Residual Harmonic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_dense240_tracking_Bw`
- Model Family: `residual_harmonic_mlp_bw`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp_bw\2026-05-20-12-03-22__te_residual_harmonic_dense240_tracking_bw\checkpoints\residual_harmonic_mlp-epoch=077-val_mae=0.00286149.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.024901`
- val_mae: `0.002861`
- val_rmse: `0.003409`
- val_structured_mae: `0.017488`
- val_structured_rmse: `0.019716`

## Test Metrics

- test_loss: `0.024741`
- test_mae: `0.003188`
- test_rmse: `0.003717`
- test_structured_mae: `0.021539`
- test_structured_rmse: `0.023467`

## Interpretation

The held-out val error stayed finite with MAE=0.002861 deg and RMSE=0.003409 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003188 deg and RMSE=0.003717 deg, which indicates a numerically stable baseline run.
