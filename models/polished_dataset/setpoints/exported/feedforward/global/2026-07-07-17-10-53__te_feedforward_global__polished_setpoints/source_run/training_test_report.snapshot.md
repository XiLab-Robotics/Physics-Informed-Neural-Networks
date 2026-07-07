# Feedforward Global Training And Testing Report

## Overview

- Run Name: `te_feedforward_global__polished_setpoints`
- Model Family: `feedforward_global`
- Model Type: `feedforward`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-17-10-53__te_feedforward_global__polished_setpoints/checkpoints/feedforward-epoch=038-val_mae=0.00169107.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002902`
- val_mae: `0.001691`
- val_rmse: `0.002266`
- val_pointwise_loss: `0.002902`
- val_centered_curve_shape_loss: `0.003363`
- val_curve_offset_loss: `0.000472`
- val_curve_amplitude_loss: `0.056746`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004900`
- test_mae: `0.001999`
- test_rmse: `0.003006`
- test_pointwise_loss: `0.004900`
- test_centered_curve_shape_loss: `0.005368`
- test_curve_offset_loss: `0.003688`
- test_curve_amplitude_loss: `0.088565`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001691 deg and RMSE=0.002266 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001999 deg and RMSE=0.003006 deg, which indicates a numerically stable baseline run.
