# Periodic Gru Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_bw__polished_setpoints`
- Model Family: `periodic_gru_sequence_bw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-08-23-18-30__te_periodic_gru_sequence_bw__polished_setpoints/checkpoints/periodic_gru_sequence-epoch=064-val_mae=0.00189811.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004922`
- val_mae: `0.001898`
- val_rmse: `0.002647`
- val_pointwise_loss: `0.004922`
- val_centered_curve_shape_loss: `0.004346`
- val_curve_offset_loss: `0.000575`
- val_curve_amplitude_loss: `0.022526`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007986`
- test_mae: `0.002168`
- test_rmse: `0.003506`
- test_pointwise_loss: `0.007986`
- test_centered_curve_shape_loss: `0.004887`
- test_curve_offset_loss: `0.003099`
- test_curve_amplitude_loss: `0.030726`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001898 deg and RMSE=0.002647 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002168 deg and RMSE=0.003506 deg, which indicates a numerically stable baseline run.
