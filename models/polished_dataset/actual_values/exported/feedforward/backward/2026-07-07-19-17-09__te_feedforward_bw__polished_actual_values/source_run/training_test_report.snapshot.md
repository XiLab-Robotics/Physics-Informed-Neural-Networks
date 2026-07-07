# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_bw__polished_actual_values`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-19-17-09__te_feedforward_bw__polished_actual_values/checkpoints/feedforward-epoch=074-val_mae=0.00164741.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002831`
- val_mae: `0.001647`
- val_rmse: `0.002239`
- val_pointwise_loss: `0.002831`
- val_centered_curve_shape_loss: `0.003417`
- val_curve_offset_loss: `0.000452`
- val_curve_amplitude_loss: `0.056122`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004274`
- test_mae: `0.001833`
- test_rmse: `0.002792`
- test_pointwise_loss: `0.004274`
- test_centered_curve_shape_loss: `0.005632`
- test_curve_offset_loss: `0.003306`
- test_curve_amplitude_loss: `0.082018`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001647 deg and RMSE=0.002239 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001833 deg and RMSE=0.002792 deg, which indicates a numerically stable baseline run.
