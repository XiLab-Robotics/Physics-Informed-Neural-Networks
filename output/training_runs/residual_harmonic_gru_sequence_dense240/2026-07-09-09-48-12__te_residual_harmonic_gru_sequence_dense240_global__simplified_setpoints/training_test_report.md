# Residual Harmonic Gru Sequence Dense240 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_global__simplified_setpoints`
- Model Family: `residual_harmonic_gru_sequence_dense240_global`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-09-48-12__te_residual_harmonic_gru_sequence_dense240_global__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=102-val_mae=0.00361734.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010968`
- val_mae: `0.003617`
- val_rmse: `0.004466`
- val_pointwise_loss: `0.010968`
- val_centered_curve_shape_loss: `0.006582`
- val_curve_offset_loss: `0.004386`
- val_curve_amplitude_loss: `0.045419`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037826`
- val_structured_rmse: `0.042751`

## Test Metrics

- test_loss: `0.008340`
- test_mae: `0.003375`
- test_rmse: `0.004181`
- test_pointwise_loss: `0.008340`
- test_centered_curve_shape_loss: `0.003397`
- test_curve_offset_loss: `0.004943`
- test_curve_amplitude_loss: `0.020867`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040702`
- test_structured_rmse: `0.045477`

## Interpretation

The held-out val error stayed finite with MAE=0.003617 deg and RMSE=0.004466 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003375 deg and RMSE=0.004181 deg, which indicates a numerically stable baseline run.
