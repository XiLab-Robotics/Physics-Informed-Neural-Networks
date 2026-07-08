# Lstm Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_bw__polished_actual_values`
- Model Family: `lstm_sequence_bw`
- Model Type: `lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-18-02-26__te_lstm_sequence_bw__polished_actual_values/checkpoints/lstm_sequence-epoch=240-val_mae=0.00214547.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005741`
- val_mae: `0.002145`
- val_rmse: `0.002976`
- val_pointwise_loss: `0.005741`
- val_centered_curve_shape_loss: `0.005400`
- val_curve_offset_loss: `0.000341`
- val_curve_amplitude_loss: `0.059582`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006564`
- test_mae: `0.002253`
- test_rmse: `0.003321`
- test_pointwise_loss: `0.006564`
- test_centered_curve_shape_loss: `0.006238`
- test_curve_offset_loss: `0.000326`
- test_curve_amplitude_loss: `0.065124`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002145 deg and RMSE=0.002976 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002253 deg and RMSE=0.003321 deg, which indicates a numerically stable baseline run.
