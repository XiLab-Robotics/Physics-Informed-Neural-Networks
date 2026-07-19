# Periodic Lstm Sequence Global Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_global__polished_setpoints`
- Model Family: `periodic_lstm_sequence_global`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-03-02-43__te_periodic_lstm_sequence_global__polished_setpoints/checkpoints/periodic_lstm_sequence-epoch=245-val_mae=0.00137071.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001969`
- val_mae: `0.001371`
- val_rmse: `0.001870`
- val_pointwise_loss: `0.001969`
- val_centered_curve_shape_loss: `0.001487`
- val_curve_offset_loss: `0.000482`
- val_curve_amplitude_loss: `0.005500`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003644`
- test_mae: `0.001561`
- test_rmse: `0.002411`
- test_pointwise_loss: `0.003644`
- test_centered_curve_shape_loss: `0.002091`
- test_curve_offset_loss: `0.001553`
- test_curve_amplitude_loss: `0.009535`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001371 deg and RMSE=0.001870 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001561 deg and RMSE=0.002411 deg, which indicates a numerically stable baseline run.
