# Residual Harmonic Lstm Sequence Dense240 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_global`
- Model Family: `residual_harmonic_lstm_sequence_dense240_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-06-30-13-02-13__te_residual_harmonic_lstm_sequence_dense240_global\checkpoints\residual_harmonic_lstm_sequence-epoch=061-val_mae=0.00203116.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005375`
- val_mae: `0.002031`
- val_rmse: `0.002516`
- val_pointwise_loss: `0.005375`
- val_centered_curve_shape_loss: `0.005011`
- val_curve_offset_loss: `0.000364`
- val_curve_amplitude_loss: `0.036026`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039749`
- val_structured_rmse: `0.041951`

## Test Metrics

- test_loss: `0.006164`
- test_mae: `0.002161`
- test_rmse: `0.002748`
- test_pointwise_loss: `0.006164`
- test_centered_curve_shape_loss: `0.005724`
- test_curve_offset_loss: `0.000441`
- test_curve_amplitude_loss: `0.040433`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037340`
- test_structured_rmse: `0.040276`

## Interpretation

The held-out val error stayed finite with MAE=0.002031 deg and RMSE=0.002516 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002161 deg and RMSE=0.002748 deg, which indicates a numerically stable baseline run.
