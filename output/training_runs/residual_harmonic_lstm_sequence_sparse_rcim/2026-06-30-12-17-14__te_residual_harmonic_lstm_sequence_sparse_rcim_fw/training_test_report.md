# Residual Harmonic Lstm Sequence Sparse Rcim Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_fw`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-06-30-12-17-14__te_residual_harmonic_lstm_sequence_sparse_rcim_fw\checkpoints\residual_harmonic_lstm_sequence-epoch=082-val_mae=0.00197149.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005298`
- val_mae: `0.001971`
- val_rmse: `0.002445`
- val_pointwise_loss: `0.005298`
- val_centered_curve_shape_loss: `0.004934`
- val_curve_offset_loss: `0.000364`
- val_curve_amplitude_loss: `0.039719`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039741`
- val_structured_rmse: `0.041939`

## Test Metrics

- test_loss: `0.006228`
- test_mae: `0.002121`
- test_rmse: `0.002711`
- test_pointwise_loss: `0.006228`
- test_centered_curve_shape_loss: `0.005688`
- test_curve_offset_loss: `0.000541`
- test_curve_amplitude_loss: `0.044832`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037327`
- test_structured_rmse: `0.040246`

## Interpretation

The held-out val error stayed finite with MAE=0.001971 deg and RMSE=0.002445 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002121 deg and RMSE=0.002711 deg, which indicates a numerically stable baseline run.
