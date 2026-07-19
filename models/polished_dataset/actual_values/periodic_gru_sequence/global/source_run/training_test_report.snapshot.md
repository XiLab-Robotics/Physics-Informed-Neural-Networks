# Periodic Gru Sequence Global Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_global__polished_actual_values`
- Model Family: `periodic_gru_sequence_global`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-08-23-45-29__te_periodic_gru_sequence_global__polished_actual_values/checkpoints/periodic_gru_sequence-epoch=259-val_mae=0.00132221.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001806`
- val_mae: `0.001322`
- val_rmse: `0.001796`
- val_pointwise_loss: `0.001806`
- val_centered_curve_shape_loss: `0.001417`
- val_curve_offset_loss: `0.000389`
- val_curve_amplitude_loss: `0.006180`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.002223`
- test_mae: `0.001390`
- test_rmse: `0.002058`
- test_pointwise_loss: `0.002223`
- test_centered_curve_shape_loss: `0.001867`
- test_curve_offset_loss: `0.000357`
- test_curve_amplitude_loss: `0.007473`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001322 deg and RMSE=0.001796 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001390 deg and RMSE=0.002058 deg, which indicates a numerically stable baseline run.
