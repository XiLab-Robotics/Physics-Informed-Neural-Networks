# Residual Harmonic Lstm Sequence Dense360 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense360_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-23-03__te_residual_harmonic_lstm_sequence_dense360_bw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=030-val_mae=0.00360440.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010839`
- val_mae: `0.003604`
- val_rmse: `0.004462`
- val_pointwise_loss: `0.010839`
- val_centered_curve_shape_loss: `0.006641`
- val_curve_offset_loss: `0.004198`
- val_curve_amplitude_loss: `0.044542`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037877`
- val_structured_rmse: `0.042670`

## Test Metrics

- test_loss: `0.008554`
- test_mae: `0.003480`
- test_rmse: `0.004221`
- test_pointwise_loss: `0.008554`
- test_centered_curve_shape_loss: `0.003498`
- test_curve_offset_loss: `0.005056`
- test_curve_amplitude_loss: `0.019350`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040728`
- test_structured_rmse: `0.045429`

## Interpretation

The held-out val error stayed finite with MAE=0.003604 deg and RMSE=0.004462 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003480 deg and RMSE=0.004221 deg, which indicates a numerically stable baseline run.
