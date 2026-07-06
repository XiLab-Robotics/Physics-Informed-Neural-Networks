# Residual Harmonic Lstm Sequence Sparse Rcim Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_bw`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_sparse_rcim\2026-06-30-12-41-44__te_residual_harmonic_lstm_sequence_sparse_rcim_bw\checkpoints\residual_harmonic_lstm_sequence-epoch=091-val_mae=0.00199396.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005306`
- val_mae: `0.001994`
- val_rmse: `0.002467`
- val_pointwise_loss: `0.005306`
- val_centered_curve_shape_loss: `0.004958`
- val_curve_offset_loss: `0.000348`
- val_curve_amplitude_loss: `0.040150`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039781`
- val_structured_rmse: `0.041978`

## Test Metrics

- test_loss: `0.006119`
- test_mae: `0.002108`
- test_rmse: `0.002694`
- test_pointwise_loss: `0.006119`
- test_centered_curve_shape_loss: `0.005736`
- test_curve_offset_loss: `0.000383`
- test_curve_amplitude_loss: `0.045288`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037337`
- test_structured_rmse: `0.040263`

## Interpretation

The held-out val error stayed finite with MAE=0.001994 deg and RMSE=0.002467 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002108 deg and RMSE=0.002694 deg, which indicates a numerically stable baseline run.
