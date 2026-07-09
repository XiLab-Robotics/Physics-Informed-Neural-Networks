# Residual Harmonic Lstm Sequence Sparse Rcim Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-20-17-04__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__polished_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=088-val_mae=0.00204480.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005481`
- val_mae: `0.002045`
- val_rmse: `0.002833`
- val_pointwise_loss: `0.005481`
- val_centered_curve_shape_loss: `0.004884`
- val_curve_offset_loss: `0.000597`
- val_curve_amplitude_loss: `0.041019`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039742`
- val_structured_rmse: `0.044223`

## Test Metrics

- test_loss: `0.008660`
- test_mae: `0.002325`
- test_rmse: `0.003669`
- test_pointwise_loss: `0.008660`
- test_centered_curve_shape_loss: `0.005809`
- test_curve_offset_loss: `0.002851`
- test_curve_amplitude_loss: `0.051837`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037336`
- test_structured_rmse: `0.042231`

## Interpretation

The held-out val error stayed finite with MAE=0.002045 deg and RMSE=0.002833 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002325 deg and RMSE=0.003669 deg, which indicates a numerically stable baseline run.
