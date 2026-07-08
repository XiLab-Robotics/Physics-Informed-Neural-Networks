# Lstm Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_fw__simplified_setpoints`
- Model Family: `lstm_sequence_fw`
- Model Type: `lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-15-14-13__te_lstm_sequence_fw__simplified_setpoints/checkpoints/lstm_sequence-epoch=092-val_mae=0.00370236.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011681`
- val_mae: `0.003702`
- val_rmse: `0.004615`
- val_pointwise_loss: `0.011681`
- val_centered_curve_shape_loss: `0.007311`
- val_curve_offset_loss: `0.004370`
- val_curve_amplitude_loss: `0.081563`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009133`
- test_mae: `0.003519`
- test_rmse: `0.004378`
- test_pointwise_loss: `0.009133`
- test_centered_curve_shape_loss: `0.004010`
- test_curve_offset_loss: `0.005123`
- test_curve_amplitude_loss: `0.047347`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003702 deg and RMSE=0.004615 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003519 deg and RMSE=0.004378 deg, which indicates a numerically stable baseline run.
