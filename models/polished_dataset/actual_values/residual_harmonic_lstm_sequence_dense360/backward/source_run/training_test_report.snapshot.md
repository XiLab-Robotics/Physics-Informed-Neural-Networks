# Residual Harmonic Lstm Sequence Dense360 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values`
- Model Family: `residual_harmonic_lstm_sequence_dense360_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-07-24-50__te_residual_harmonic_lstm_sequence_dense360_bw__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=105-val_mae=0.00199856.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005261`
- val_mae: `0.001999`
- val_rmse: `0.002783`
- val_pointwise_loss: `0.005261`
- val_centered_curve_shape_loss: `0.004890`
- val_curve_offset_loss: `0.000371`
- val_curve_amplitude_loss: `0.034854`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039696`
- val_structured_rmse: `0.044233`

## Test Metrics

- test_loss: `0.006202`
- test_mae: `0.002156`
- test_rmse: `0.003201`
- test_pointwise_loss: `0.006202`
- test_centered_curve_shape_loss: `0.005780`
- test_curve_offset_loss: `0.000422`
- test_curve_amplitude_loss: `0.039573`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037359`
- test_structured_rmse: `0.042304`

## Interpretation

The held-out val error stayed finite with MAE=0.001999 deg and RMSE=0.002783 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002156 deg and RMSE=0.003201 deg, which indicates a numerically stable baseline run.
