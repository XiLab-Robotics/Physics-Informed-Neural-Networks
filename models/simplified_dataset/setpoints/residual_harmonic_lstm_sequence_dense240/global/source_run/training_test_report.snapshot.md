# Residual Harmonic Lstm Sequence Dense240 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense240_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-14-07__te_residual_harmonic_lstm_sequence_dense240_global__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=042-val_mae=0.00360357.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010982`
- val_mae: `0.003604`
- val_rmse: `0.004485`
- val_pointwise_loss: `0.010982`
- val_centered_curve_shape_loss: `0.006656`
- val_curve_offset_loss: `0.004326`
- val_curve_amplitude_loss: `0.047129`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037862`
- val_structured_rmse: `0.042644`

## Test Metrics

- test_loss: `0.008339`
- test_mae: `0.003381`
- test_rmse: `0.004182`
- test_pointwise_loss: `0.008339`
- test_centered_curve_shape_loss: `0.003475`
- test_curve_offset_loss: `0.004864`
- test_curve_amplitude_loss: `0.021113`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040719`
- test_structured_rmse: `0.045402`

## Interpretation

The held-out val error stayed finite with MAE=0.003604 deg and RMSE=0.004485 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003381 deg and RMSE=0.004182 deg, which indicates a numerically stable baseline run.
