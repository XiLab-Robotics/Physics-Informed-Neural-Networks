# Residual Harmonic Gru Sequence Sparse Rcim Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_global`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-07-39-41__te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=226-val_mae=0.00193782.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005230`
- val_mae: `0.001938`
- val_rmse: `0.002735`
- val_pointwise_loss: `0.005230`
- val_centered_curve_shape_loss: `0.004935`
- val_curve_offset_loss: `0.000295`
- val_curve_amplitude_loss: `0.041700`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039848`
- val_structured_rmse: `0.044297`

## Test Metrics

- test_loss: `0.006018`
- test_mae: `0.002062`
- test_rmse: `0.003120`
- test_pointwise_loss: `0.006018`
- test_centered_curve_shape_loss: `0.005721`
- test_curve_offset_loss: `0.000297`
- test_curve_amplitude_loss: `0.046851`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037359`
- test_structured_rmse: `0.042255`

## Interpretation

The held-out val error stayed finite with MAE=0.001938 deg and RMSE=0.002735 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002062 deg and RMSE=0.003120 deg, which indicates a numerically stable baseline run.
