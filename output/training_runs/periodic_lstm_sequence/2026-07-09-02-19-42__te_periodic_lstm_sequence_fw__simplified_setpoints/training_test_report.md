# Periodic Lstm Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_fw__simplified_setpoints`
- Model Family: `periodic_lstm_sequence_fw`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-02-19-42__te_periodic_lstm_sequence_fw__simplified_setpoints/checkpoints/periodic_lstm_sequence-epoch=095-val_mae=0.00348296.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010217`
- val_mae: `0.003483`
- val_rmse: `0.004299`
- val_pointwise_loss: `0.010217`
- val_centered_curve_shape_loss: `0.005737`
- val_curve_offset_loss: `0.004480`
- val_curve_amplitude_loss: `0.035437`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008205`
- test_mae: `0.003390`
- test_rmse: `0.004150`
- test_pointwise_loss: `0.008205`
- test_centered_curve_shape_loss: `0.002760`
- test_curve_offset_loss: `0.005445`
- test_curve_amplitude_loss: `0.014064`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003483 deg and RMSE=0.004299 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003390 deg and RMSE=0.004150 deg, which indicates a numerically stable baseline run.
