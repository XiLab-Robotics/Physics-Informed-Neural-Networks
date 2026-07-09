# Residual Harmonic Gru Sequence Sparse Rcim Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_fw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-56-34__te_residual_harmonic_gru_sequence_sparse_rcim_fw__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=070-val_mae=0.00360244.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011030`
- val_mae: `0.003602`
- val_rmse: `0.004458`
- val_pointwise_loss: `0.011030`
- val_centered_curve_shape_loss: `0.006809`
- val_curve_offset_loss: `0.004221`
- val_curve_amplitude_loss: `0.056932`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037924`
- val_structured_rmse: `0.042717`

## Test Metrics

- test_loss: `0.008525`
- test_mae: `0.003418`
- test_rmse: `0.004220`
- test_pointwise_loss: `0.008525`
- test_centered_curve_shape_loss: `0.003502`
- test_curve_offset_loss: `0.005023`
- test_curve_amplitude_loss: `0.026856`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040764`
- test_structured_rmse: `0.045483`

## Interpretation

The held-out val error stayed finite with MAE=0.003602 deg and RMSE=0.004458 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003418 deg and RMSE=0.004220 deg, which indicates a numerically stable baseline run.
