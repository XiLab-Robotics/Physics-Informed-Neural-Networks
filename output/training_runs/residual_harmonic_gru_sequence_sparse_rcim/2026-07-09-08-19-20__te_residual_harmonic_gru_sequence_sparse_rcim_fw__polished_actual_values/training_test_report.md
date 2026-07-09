# Residual Harmonic Gru Sequence Sparse Rcim Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_fw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-19-20__te_residual_harmonic_gru_sequence_sparse_rcim_fw__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=170-val_mae=0.00195142.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005269`
- val_mae: `0.001951`
- val_rmse: `0.002753`
- val_pointwise_loss: `0.005269`
- val_centered_curve_shape_loss: `0.004925`
- val_curve_offset_loss: `0.000343`
- val_curve_amplitude_loss: `0.040578`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039723`
- val_structured_rmse: `0.044182`

## Test Metrics

- test_loss: `0.006092`
- test_mae: `0.002082`
- test_rmse: `0.003139`
- test_pointwise_loss: `0.006092`
- test_centered_curve_shape_loss: `0.005729`
- test_curve_offset_loss: `0.000363`
- test_curve_amplitude_loss: `0.045681`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037324`
- test_structured_rmse: `0.042196`

## Interpretation

The held-out val error stayed finite with MAE=0.001951 deg and RMSE=0.002753 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002082 deg and RMSE=0.003139 deg, which indicates a numerically stable baseline run.
