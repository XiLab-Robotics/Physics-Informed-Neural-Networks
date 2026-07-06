# Residual Harmonic Lstm Sequence Sparse Rcim Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_global`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-06-30-11-45-14__te_residual_harmonic_lstm_sequence_sparse_rcim_global\checkpoints\residual_harmonic_lstm_sequence-epoch=126-val_mae=0.00195406.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005281`
- val_mae: `0.001954`
- val_rmse: `0.002424`
- val_pointwise_loss: `0.005281`
- val_centered_curve_shape_loss: `0.004946`
- val_curve_offset_loss: `0.000335`
- val_curve_amplitude_loss: `0.039905`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039805`
- val_structured_rmse: `0.042002`

## Test Metrics

- test_loss: `0.006046`
- test_mae: `0.002062`
- test_rmse: `0.002651`
- test_pointwise_loss: `0.006046`
- test_centered_curve_shape_loss: `0.005745`
- test_curve_offset_loss: `0.000301`
- test_curve_amplitude_loss: `0.045082`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037344`
- test_structured_rmse: `0.040276`

## Interpretation

The held-out val error stayed finite with MAE=0.001954 deg and RMSE=0.002424 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002062 deg and RMSE=0.002651 deg, which indicates a numerically stable baseline run.
