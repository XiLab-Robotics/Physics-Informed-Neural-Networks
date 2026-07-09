# Residual Harmonic Lstm Sequence Sparse Rcim Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_sparse_rcim_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_sparse_rcim/2026-07-09-19-52-09__te_residual_harmonic_lstm_sequence_sparse_rcim_fw__polished_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=068-val_mae=0.00202292.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005361`
- val_mae: `0.002023`
- val_rmse: `0.002806`
- val_pointwise_loss: `0.005361`
- val_centered_curve_shape_loss: `0.004889`
- val_curve_offset_loss: `0.000471`
- val_curve_amplitude_loss: `0.039494`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039797`
- val_structured_rmse: `0.044362`

## Test Metrics

- test_loss: `0.008888`
- test_mae: `0.002361`
- test_rmse: `0.003733`
- test_pointwise_loss: `0.008888`
- test_centered_curve_shape_loss: `0.005817`
- test_curve_offset_loss: `0.003071`
- test_curve_amplitude_loss: `0.049969`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037382`
- test_structured_rmse: `0.042356`

## Interpretation

The held-out val error stayed finite with MAE=0.002023 deg and RMSE=0.002806 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002361 deg and RMSE=0.003733 deg, which indicates a numerically stable baseline run.
