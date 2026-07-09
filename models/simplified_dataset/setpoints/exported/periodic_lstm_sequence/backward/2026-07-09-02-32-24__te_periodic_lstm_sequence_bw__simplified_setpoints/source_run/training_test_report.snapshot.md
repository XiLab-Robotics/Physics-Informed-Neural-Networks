# Periodic Lstm Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_bw__simplified_setpoints`
- Model Family: `periodic_lstm_sequence_bw`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-02-32-24__te_periodic_lstm_sequence_bw__simplified_setpoints/checkpoints/periodic_lstm_sequence-epoch=074-val_mae=0.00352408.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010167`
- val_mae: `0.003524`
- val_rmse: `0.004321`
- val_pointwise_loss: `0.010167`
- val_centered_curve_shape_loss: `0.005813`
- val_curve_offset_loss: `0.004354`
- val_curve_amplitude_loss: `0.043842`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007919`
- test_mae: `0.003349`
- test_rmse: `0.004076`
- test_pointwise_loss: `0.007919`
- test_centered_curve_shape_loss: `0.002779`
- test_curve_offset_loss: `0.005140`
- test_curve_amplitude_loss: `0.018486`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003524 deg and RMSE=0.004321 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003349 deg and RMSE=0.004076 deg, which indicates a numerically stable baseline run.
