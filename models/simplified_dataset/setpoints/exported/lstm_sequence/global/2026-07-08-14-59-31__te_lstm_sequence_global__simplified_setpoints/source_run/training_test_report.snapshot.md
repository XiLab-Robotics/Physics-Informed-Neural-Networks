# Lstm Sequence Global Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_global__simplified_setpoints`
- Model Family: `lstm_sequence_global`
- Model Type: `lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-14-59-31__te_lstm_sequence_global__simplified_setpoints/checkpoints/lstm_sequence-epoch=115-val_mae=0.00369210.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011541`
- val_mae: `0.003692`
- val_rmse: `0.004582`
- val_pointwise_loss: `0.011541`
- val_centered_curve_shape_loss: `0.007275`
- val_curve_offset_loss: `0.004266`
- val_curve_amplitude_loss: `0.077916`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008804`
- test_mae: `0.003446`
- test_rmse: `0.004293`
- test_pointwise_loss: `0.008804`
- test_centered_curve_shape_loss: `0.003971`
- test_curve_offset_loss: `0.004833`
- test_curve_amplitude_loss: `0.043118`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003692 deg and RMSE=0.004582 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003446 deg and RMSE=0.004293 deg, which indicates a numerically stable baseline run.
