# Periodic Lstm Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_bw__polished_actual_values`
- Model Family: `periodic_lstm_sequence_bw`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-05-16-31__te_periodic_lstm_sequence_bw__polished_actual_values/checkpoints/periodic_lstm_sequence-epoch=053-val_mae=0.00197877.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004899`
- val_mae: `0.001979`
- val_rmse: `0.002720`
- val_pointwise_loss: `0.004899`
- val_centered_curve_shape_loss: `0.004312`
- val_curve_offset_loss: `0.000587`
- val_curve_amplitude_loss: `0.025854`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008027`
- test_mae: `0.002196`
- test_rmse: `0.003476`
- test_pointwise_loss: `0.008027`
- test_centered_curve_shape_loss: `0.004934`
- test_curve_offset_loss: `0.003092`
- test_curve_amplitude_loss: `0.034939`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001979 deg and RMSE=0.002720 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002196 deg and RMSE=0.003476 deg, which indicates a numerically stable baseline run.
