# Residual Harmonic Gru Sequence Sparse Rcim Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_setpoints`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_global`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-06-26-33__te_residual_harmonic_gru_sequence_sparse_rcim_global__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=060-val_mae=0.00203207.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005387`
- val_mae: `0.002032`
- val_rmse: `0.002825`
- val_pointwise_loss: `0.005387`
- val_centered_curve_shape_loss: `0.004911`
- val_curve_offset_loss: `0.000476`
- val_curve_amplitude_loss: `0.039559`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039781`
- val_structured_rmse: `0.044436`

## Test Metrics

- test_loss: `0.008991`
- test_mae: `0.002357`
- test_rmse: `0.003734`
- test_pointwise_loss: `0.008991`
- test_centered_curve_shape_loss: `0.005821`
- test_curve_offset_loss: `0.003170`
- test_curve_amplitude_loss: `0.050291`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037406`
- test_structured_rmse: `0.042451`

## Interpretation

The held-out val error stayed finite with MAE=0.002032 deg and RMSE=0.002825 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002357 deg and RMSE=0.003734 deg, which indicates a numerically stable baseline run.
