# Periodic Lstm Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_fw`
- Model Family: `periodic_lstm_sequence_fw`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_lstm_sequence\2026-06-30-04-57-16__te_periodic_lstm_sequence_fw\checkpoints\periodic_lstm_sequence-epoch=118-val_mae=0.00151323.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002873`
- val_mae: `0.001513`
- val_rmse: `0.001879`
- val_pointwise_loss: `0.002873`
- val_centered_curve_shape_loss: `0.002477`
- val_curve_offset_loss: `0.000395`
- val_curve_amplitude_loss: `0.008564`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.002950`
- test_mae: `0.001555`
- test_rmse: `0.001983`
- test_pointwise_loss: `0.002950`
- test_centered_curve_shape_loss: `0.002562`
- test_curve_offset_loss: `0.000388`
- test_curve_amplitude_loss: `0.008148`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001513 deg and RMSE=0.001879 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001555 deg and RMSE=0.001983 deg, which indicates a numerically stable baseline run.
