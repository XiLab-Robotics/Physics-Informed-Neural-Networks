# Residual Harmonic Lstm Sequence Sparse Rcim Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-18-56-39__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=029-val_mae=0.00367824.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011239`
- val_mae: `0.003678`
- val_rmse: `0.004530`
- val_pointwise_loss: `0.011239`
- val_centered_curve_shape_loss: `0.006893`
- val_curve_offset_loss: `0.004346`
- val_curve_amplitude_loss: `0.057345`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.038111`
- val_structured_rmse: `0.043236`

## Test Metrics

- test_loss: `0.008319`
- test_mae: `0.003372`
- test_rmse: `0.004162`
- test_pointwise_loss: `0.008319`
- test_centered_curve_shape_loss: `0.003599`
- test_curve_offset_loss: `0.004720`
- test_curve_amplitude_loss: `0.027331`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040934`
- test_structured_rmse: `0.045973`

## Interpretation

The held-out val error stayed finite with MAE=0.003678 deg and RMSE=0.004530 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003372 deg and RMSE=0.004162 deg, which indicates a numerically stable baseline run.
