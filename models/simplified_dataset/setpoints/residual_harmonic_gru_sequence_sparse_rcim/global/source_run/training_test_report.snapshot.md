# Residual Harmonic Gru Sequence Sparse Rcim Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_global`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-05-46-13__te_residual_harmonic_gru_sequence_sparse_rcim_global__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=106-val_mae=0.00358149.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011152`
- val_mae: `0.003581`
- val_rmse: `0.004482`
- val_pointwise_loss: `0.011152`
- val_centered_curve_shape_loss: `0.006786`
- val_curve_offset_loss: `0.004366`
- val_curve_amplitude_loss: `0.055980`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037851`
- val_structured_rmse: `0.042629`

## Test Metrics

- test_loss: `0.008854`
- test_mae: `0.003456`
- test_rmse: `0.004304`
- test_pointwise_loss: `0.008854`
- test_centered_curve_shape_loss: `0.003490`
- test_curve_offset_loss: `0.005364`
- test_curve_amplitude_loss: `0.026676`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040715`
- test_structured_rmse: `0.045390`

## Interpretation

The held-out val error stayed finite with MAE=0.003581 deg and RMSE=0.004482 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003456 deg and RMSE=0.004304 deg, which indicates a numerically stable baseline run.
