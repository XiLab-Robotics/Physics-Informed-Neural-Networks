# Periodic Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_fw__simplified_setpoints`
- Model Family: `periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-08-22-14-21__te_periodic_gru_sequence_fw__simplified_setpoints/checkpoints/periodic_gru_sequence-epoch=056-val_mae=0.00353205.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010109`
- val_mae: `0.003532`
- val_rmse: `0.004348`
- val_pointwise_loss: `0.010109`
- val_centered_curve_shape_loss: `0.005802`
- val_curve_offset_loss: `0.004308`
- val_curve_amplitude_loss: `0.039263`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007885`
- test_mae: `0.003368`
- test_rmse: `0.004076`
- test_pointwise_loss: `0.007885`
- test_centered_curve_shape_loss: `0.002859`
- test_curve_offset_loss: `0.005026`
- test_curve_amplitude_loss: `0.015875`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003532 deg and RMSE=0.004348 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003368 deg and RMSE=0.004076 deg, which indicates a numerically stable baseline run.
