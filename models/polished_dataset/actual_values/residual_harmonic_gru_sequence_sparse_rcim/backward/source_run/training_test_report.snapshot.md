# Residual Harmonic Gru Sequence Sparse Rcim Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-08-55-01__te_residual_harmonic_gru_sequence_sparse_rcim_bw__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=200-val_mae=0.00195317.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005276`
- val_mae: `0.001953`
- val_rmse: `0.002754`
- val_pointwise_loss: `0.005276`
- val_centered_curve_shape_loss: `0.004929`
- val_curve_offset_loss: `0.000347`
- val_curve_amplitude_loss: `0.039952`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039807`
- val_structured_rmse: `0.044258`

## Test Metrics

- test_loss: `0.006095`
- test_mae: `0.002083`
- test_rmse: `0.003142`
- test_pointwise_loss: `0.006095`
- test_centered_curve_shape_loss: `0.005716`
- test_curve_offset_loss: `0.000379`
- test_curve_amplitude_loss: `0.045048`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037345`
- test_structured_rmse: `0.042234`

## Interpretation

The held-out val error stayed finite with MAE=0.001953 deg and RMSE=0.002754 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002083 deg and RMSE=0.003142 deg, which indicates a numerically stable baseline run.
