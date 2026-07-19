# Periodic Lstm Sequence Global Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_global__polished_actual_values`
- Model Family: `periodic_lstm_sequence_global`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-04-47-33__te_periodic_lstm_sequence_global__polished_actual_values/checkpoints/periodic_lstm_sequence-epoch=103-val_mae=0.00191666.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004840`
- val_mae: `0.001917`
- val_rmse: `0.002660`
- val_pointwise_loss: `0.004840`
- val_centered_curve_shape_loss: `0.004369`
- val_curve_offset_loss: `0.000471`
- val_curve_amplitude_loss: `0.020470`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007003`
- test_mae: `0.002121`
- test_rmse: `0.003300`
- test_pointwise_loss: `0.007003`
- test_centered_curve_shape_loss: `0.004634`
- test_curve_offset_loss: `0.002370`
- test_curve_amplitude_loss: `0.023943`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001917 deg and RMSE=0.002660 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002121 deg and RMSE=0.003300 deg, which indicates a numerically stable baseline run.
