# Residual Harmonic Lstm Sequence Sparse Rcim Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-19-10-53__te_residual_harmonic_lstm_sequence_sparse_rcim_bw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=027-val_mae=0.00365442.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011139`
- val_mae: `0.003654`
- val_rmse: `0.004496`
- val_pointwise_loss: `0.011139`
- val_centered_curve_shape_loss: `0.006918`
- val_curve_offset_loss: `0.004222`
- val_curve_amplitude_loss: `0.057222`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.038171`
- val_structured_rmse: `0.043384`

## Test Metrics

- test_loss: `0.008550`
- test_mae: `0.003449`
- test_rmse: `0.004232`
- test_pointwise_loss: `0.008550`
- test_centered_curve_shape_loss: `0.003611`
- test_curve_offset_loss: `0.004939`
- test_curve_amplitude_loss: `0.026721`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040991`
- test_structured_rmse: `0.046112`

## Interpretation

The held-out val error stayed finite with MAE=0.003654 deg and RMSE=0.004496 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003449 deg and RMSE=0.004232 deg, which indicates a numerically stable baseline run.
