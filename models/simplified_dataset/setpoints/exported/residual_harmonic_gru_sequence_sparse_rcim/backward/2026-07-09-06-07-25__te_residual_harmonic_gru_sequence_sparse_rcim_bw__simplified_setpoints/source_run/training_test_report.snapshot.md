# Residual Harmonic Gru Sequence Sparse Rcim Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints`
- Model Family: `residual_harmonic_gru_sequence_sparse_rcim_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_sparse_rcim/2026-07-09-06-07-25__te_residual_harmonic_gru_sequence_sparse_rcim_bw__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=061-val_mae=0.00359811.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011084`
- val_mae: `0.003598`
- val_rmse: `0.004469`
- val_pointwise_loss: `0.011084`
- val_centered_curve_shape_loss: `0.006809`
- val_curve_offset_loss: `0.004275`
- val_curve_amplitude_loss: `0.056127`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037974`
- val_structured_rmse: `0.042838`

## Test Metrics

- test_loss: `0.008692`
- test_mae: `0.003435`
- test_rmse: `0.004261`
- test_pointwise_loss: `0.008692`
- test_centered_curve_shape_loss: `0.003501`
- test_curve_offset_loss: `0.005191`
- test_curve_amplitude_loss: `0.026264`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040803`
- test_structured_rmse: `0.045600`

## Interpretation

The held-out val error stayed finite with MAE=0.003598 deg and RMSE=0.004469 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003435 deg and RMSE=0.004261 deg, which indicates a numerically stable baseline run.
