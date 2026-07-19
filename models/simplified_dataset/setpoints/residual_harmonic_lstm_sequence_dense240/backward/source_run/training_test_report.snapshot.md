# Residual Harmonic Lstm Sequence Dense240 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense240_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-09-23-53-53__te_residual_harmonic_lstm_sequence_dense240_bw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=087-val_mae=0.00358639.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010797`
- val_mae: `0.003586`
- val_rmse: `0.004434`
- val_pointwise_loss: `0.010797`
- val_centered_curve_shape_loss: `0.006601`
- val_curve_offset_loss: `0.004196`
- val_curve_amplitude_loss: `0.042989`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037829`
- val_structured_rmse: `0.042647`

## Test Metrics

- test_loss: `0.008192`
- test_mae: `0.003367`
- test_rmse: `0.004145`
- test_pointwise_loss: `0.008192`
- test_centered_curve_shape_loss: `0.003418`
- test_curve_offset_loss: `0.004774`
- test_curve_amplitude_loss: `0.019287`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040702`
- test_structured_rmse: `0.045396`

## Interpretation

The held-out val error stayed finite with MAE=0.003586 deg and RMSE=0.004434 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003367 deg and RMSE=0.004145 deg, which indicates a numerically stable baseline run.
