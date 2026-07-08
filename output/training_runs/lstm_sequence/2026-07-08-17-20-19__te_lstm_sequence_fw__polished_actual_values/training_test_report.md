# Lstm Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_fw__polished_actual_values`
- Model Family: `lstm_sequence_fw`
- Model Type: `lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-17-20-19__te_lstm_sequence_fw__polished_actual_values/checkpoints/lstm_sequence-epoch=210-val_mae=0.00215124.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005749`
- val_mae: `0.002151`
- val_rmse: `0.002979`
- val_pointwise_loss: `0.005749`
- val_centered_curve_shape_loss: `0.005398`
- val_curve_offset_loss: `0.000351`
- val_curve_amplitude_loss: `0.058478`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006541`
- test_mae: `0.002239`
- test_rmse: `0.003319`
- test_pointwise_loss: `0.006541`
- test_centered_curve_shape_loss: `0.006239`
- test_curve_offset_loss: `0.000302`
- test_curve_amplitude_loss: `0.063865`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002151 deg and RMSE=0.002979 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002239 deg and RMSE=0.003319 deg, which indicates a numerically stable baseline run.
