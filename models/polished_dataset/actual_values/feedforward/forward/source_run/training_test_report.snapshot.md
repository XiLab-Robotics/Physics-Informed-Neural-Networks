# Feedforward Fw Training And Testing Report

## Overview

- Run Name: `te_feedforward_fw__polished_actual_values`
- Model Family: `feedforward_fw`
- Model Type: `feedforward`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-18-43-03__te_feedforward_fw__polished_actual_values/checkpoints/feedforward-epoch=181-val_mae=0.00161552.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002748`
- val_mae: `0.001616`
- val_rmse: `0.002193`
- val_pointwise_loss: `0.002748`
- val_centered_curve_shape_loss: `0.003346`
- val_curve_offset_loss: `0.000414`
- val_curve_amplitude_loss: `0.053967`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004129`
- test_mae: `0.001758`
- test_rmse: `0.002736`
- test_pointwise_loss: `0.004129`
- test_centered_curve_shape_loss: `0.006111`
- test_curve_offset_loss: `0.002660`
- test_curve_amplitude_loss: `0.078437`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001616 deg and RMSE=0.002193 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001758 deg and RMSE=0.002736 deg, which indicates a numerically stable baseline run.
