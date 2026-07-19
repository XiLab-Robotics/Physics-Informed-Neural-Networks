# Lstm Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_bw__polished_setpoints`
- Model Family: `lstm_sequence_bw`
- Model Type: `lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-16-21-04__te_lstm_sequence_bw__polished_setpoints/checkpoints/lstm_sequence-epoch=070-val_mae=0.00219971.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005862`
- val_mae: `0.002200`
- val_rmse: `0.003022`
- val_pointwise_loss: `0.005862`
- val_centered_curve_shape_loss: `0.005384`
- val_curve_offset_loss: `0.000477`
- val_curve_amplitude_loss: `0.060413`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009217`
- test_mae: `0.002469`
- test_rmse: `0.003842`
- test_pointwise_loss: `0.009217`
- test_centered_curve_shape_loss: `0.006293`
- test_curve_offset_loss: `0.002923`
- test_curve_amplitude_loss: `0.072487`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002200 deg and RMSE=0.003022 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002469 deg and RMSE=0.003842 deg, which indicates a numerically stable baseline run.
