# Periodic Lstm Sequence Global Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_global__simplified_setpoints`
- Model Family: `periodic_lstm_sequence_global`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-02-10-37__te_periodic_lstm_sequence_global__simplified_setpoints/checkpoints/periodic_lstm_sequence-epoch=088-val_mae=0.00353329.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010053`
- val_mae: `0.003533`
- val_rmse: `0.004312`
- val_pointwise_loss: `0.010053`
- val_centered_curve_shape_loss: `0.005764`
- val_curve_offset_loss: `0.004289`
- val_curve_amplitude_loss: `0.040540`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007716`
- test_mae: `0.003369`
- test_rmse: `0.004027`
- test_pointwise_loss: `0.007716`
- test_centered_curve_shape_loss: `0.002781`
- test_curve_offset_loss: `0.004935`
- test_curve_amplitude_loss: `0.017044`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003533 deg and RMSE=0.004312 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003369 deg and RMSE=0.004027 deg, which indicates a numerically stable baseline run.
