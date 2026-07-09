# Residual Harmonic Lstm Sequence Sparse Rcim Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-39-59__te_residual_harmonic_lstm_sequence_sparse_rcim_global__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=050-val_mae=0.00361757.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011096`
- val_mae: `0.003618`
- val_rmse: `0.004474`
- val_pointwise_loss: `0.011096`
- val_centered_curve_shape_loss: `0.006804`
- val_curve_offset_loss: `0.004292`
- val_curve_amplitude_loss: `0.055025`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037981`
- val_structured_rmse: `0.042882`

## Test Metrics

- test_loss: `0.008363`
- test_mae: `0.003400`
- test_rmse: `0.004178`
- test_pointwise_loss: `0.008363`
- test_centered_curve_shape_loss: `0.003511`
- test_curve_offset_loss: `0.004852`
- test_curve_amplitude_loss: `0.025846`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040808`
- test_structured_rmse: `0.045638`

## Interpretation

The held-out val error stayed finite with MAE=0.003618 deg and RMSE=0.004474 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003400 deg and RMSE=0.004178 deg, which indicates a numerically stable baseline run.
