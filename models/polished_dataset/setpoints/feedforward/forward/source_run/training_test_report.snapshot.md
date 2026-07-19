# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_fw__polished_setpoints`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-17-25-58__te_feedforward_fw__polished_setpoints/checkpoints/feedforward-epoch=042-val_mae=0.00168289.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002881`
- val_mae: `0.001683`
- val_rmse: `0.002255`
- val_pointwise_loss: `0.002881`
- val_centered_curve_shape_loss: `0.003364`
- val_curve_offset_loss: `0.000564`
- val_curve_amplitude_loss: `0.054037`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004669`
- test_mae: `0.001938`
- test_rmse: `0.002950`
- test_pointwise_loss: `0.004669`
- test_centered_curve_shape_loss: `0.005377`
- test_curve_offset_loss: `0.003892`
- test_curve_amplitude_loss: `0.084451`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001683 deg and RMSE=0.002255 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001938 deg and RMSE=0.002950 deg, which indicates a numerically stable baseline run.
