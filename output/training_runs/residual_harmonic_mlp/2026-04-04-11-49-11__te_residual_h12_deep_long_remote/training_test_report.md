# Residual Harmonic Mlp Training And Testing Report

## Overview

- Run Name: `te_residual_h12_deep_long_remote`
- Model Family: `residual_harmonic_mlp`
- Model Type: `residual_harmonic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_mlp\2026-04-04-11-49-11__te_residual_h12_deep_long_remote\checkpoints\residual_harmonic_mlp-epoch=080-val_mae=0.00297334.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007657`
- val_mae: `0.002973`
- val_rmse: `0.003495`
- val_structured_mae: `0.040530`
- val_structured_rmse: `0.042570`

## Test Metrics

- test_loss: `0.008434`
- test_mae: `0.003384`
- test_rmse: `0.003908`
- test_structured_mae: `0.039406`
- test_structured_rmse: `0.042796`

## Interpretation

The held-out val error stayed finite with MAE=0.002973 deg and RMSE=0.003495 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003384 deg and RMSE=0.003908 deg, which indicates a numerically stable baseline run.
