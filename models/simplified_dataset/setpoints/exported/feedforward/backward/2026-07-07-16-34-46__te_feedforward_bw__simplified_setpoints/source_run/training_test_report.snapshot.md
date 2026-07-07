# Feedforward Bw Training And Testing Report

## Overview

- Run Name: `te_feedforward_bw__simplified_setpoints`
- Model Family: `feedforward_bw`
- Model Type: `feedforward`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/feedforward/2026-07-07-16-34-46__te_feedforward_bw__simplified_setpoints/checkpoints/feedforward-epoch=128-val_mae=0.00297364.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.007416`
- val_mae: `0.002974`
- val_rmse: `0.003654`
- val_pointwise_loss: `0.007416`
- val_centered_curve_shape_loss: `0.003584`
- val_curve_offset_loss: `0.004519`
- val_curve_amplitude_loss: `0.056279`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007953`
- test_mae: `0.003341`
- test_rmse: `0.003986`
- test_pointwise_loss: `0.007953`
- test_centered_curve_shape_loss: `0.002879`
- test_curve_offset_loss: `0.005513`
- test_curve_amplitude_loss: `0.047092`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002974 deg and RMSE=0.003654 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003341 deg and RMSE=0.003986 deg, which indicates a numerically stable baseline run.
