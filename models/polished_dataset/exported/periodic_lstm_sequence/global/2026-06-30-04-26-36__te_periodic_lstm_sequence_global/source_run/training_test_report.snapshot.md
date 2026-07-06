# Periodic Lstm Sequence Global Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_global`
- Model Family: `periodic_lstm_sequence_global`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_lstm_sequence\2026-06-30-04-26-36__te_periodic_lstm_sequence_global\checkpoints\periodic_lstm_sequence-epoch=124-val_mae=0.00153599.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002961`
- val_mae: `0.001536`
- val_rmse: `0.001907`
- val_pointwise_loss: `0.002961`
- val_centered_curve_shape_loss: `0.002451`
- val_curve_offset_loss: `0.000510`
- val_curve_amplitude_loss: `0.008621`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003009`
- test_mae: `0.001601`
- test_rmse: `0.002029`
- test_pointwise_loss: `0.003009`
- test_centered_curve_shape_loss: `0.002574`
- test_curve_offset_loss: `0.000435`
- test_curve_amplitude_loss: `0.009469`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001536 deg and RMSE=0.001907 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001601 deg and RMSE=0.002029 deg, which indicates a numerically stable baseline run.
