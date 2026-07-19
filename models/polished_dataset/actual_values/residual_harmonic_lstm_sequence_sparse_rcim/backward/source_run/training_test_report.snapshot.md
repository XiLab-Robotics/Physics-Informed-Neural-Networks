# Residual Harmonic Lstm Sequence Sparse Rcim Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-22-37-02__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=010-val_mae=0.00215380.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005743`
- val_mae: `0.002154`
- val_rmse: `0.002977`
- val_pointwise_loss: `0.005743`
- val_centered_curve_shape_loss: `0.005108`
- val_curve_offset_loss: `0.000635`
- val_curve_amplitude_loss: `0.038170`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.040059`
- val_structured_rmse: `0.045366`

## Test Metrics

- test_loss: `0.009085`
- test_mae: `0.002413`
- test_rmse: `0.003764`
- test_pointwise_loss: `0.009085`
- test_centered_curve_shape_loss: `0.005995`
- test_curve_offset_loss: `0.003089`
- test_curve_amplitude_loss: `0.048924`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037775`
- test_structured_rmse: `0.043427`

## Interpretation

The held-out val error stayed finite with MAE=0.002154 deg and RMSE=0.002977 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002413 deg and RMSE=0.003764 deg, which indicates a numerically stable baseline run.
