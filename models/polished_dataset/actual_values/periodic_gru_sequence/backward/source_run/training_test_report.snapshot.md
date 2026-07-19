# Periodic Gru Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_bw__polished_actual_values`
- Model Family: `periodic_gru_sequence_bw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-09-01-09-21__te_periodic_gru_sequence_bw__polished_actual_values/checkpoints/periodic_gru_sequence-epoch=257-val_mae=0.00127934.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001679`
- val_mae: `0.001279`
- val_rmse: `0.001735`
- val_pointwise_loss: `0.001679`
- val_centered_curve_shape_loss: `0.001334`
- val_curve_offset_loss: `0.000345`
- val_curve_amplitude_loss: `0.005208`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.002046`
- test_mae: `0.001343`
- test_rmse: `0.001978`
- test_pointwise_loss: `0.002046`
- test_centered_curve_shape_loss: `0.001694`
- test_curve_offset_loss: `0.000352`
- test_curve_amplitude_loss: `0.005570`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001279 deg and RMSE=0.001735 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001343 deg and RMSE=0.001978 deg, which indicates a numerically stable baseline run.
