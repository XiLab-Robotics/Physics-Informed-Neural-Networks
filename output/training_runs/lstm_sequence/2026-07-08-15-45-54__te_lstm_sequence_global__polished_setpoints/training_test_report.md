# Lstm Sequence Global Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_global__polished_setpoints`
- Model Family: `lstm_sequence_global`
- Model Type: `lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-15-45-54__te_lstm_sequence_global__polished_setpoints/checkpoints/lstm_sequence-epoch=118-val_mae=0.00218648.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005833`
- val_mae: `0.002186`
- val_rmse: `0.003020`
- val_pointwise_loss: `0.005833`
- val_centered_curve_shape_loss: `0.005384`
- val_curve_offset_loss: `0.000449`
- val_curve_amplitude_loss: `0.057821`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009363`
- test_mae: `0.002470`
- test_rmse: `0.003855`
- test_pointwise_loss: `0.009363`
- test_centered_curve_shape_loss: `0.006285`
- test_curve_offset_loss: `0.003078`
- test_curve_amplitude_loss: `0.070525`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002186 deg and RMSE=0.003020 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002470 deg and RMSE=0.003855 deg, which indicates a numerically stable baseline run.
