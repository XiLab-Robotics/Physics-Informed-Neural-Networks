# Lstm Sequence Global Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_global__polished_actual_values`
- Model Family: `lstm_sequence_global`
- Model Type: `lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-16-51-13__te_lstm_sequence_global__polished_actual_values/checkpoints/lstm_sequence-epoch=160-val_mae=0.00218895.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005847`
- val_mae: `0.002189`
- val_rmse: `0.003024`
- val_pointwise_loss: `0.005847`
- val_centered_curve_shape_loss: `0.005399`
- val_curve_offset_loss: `0.000448`
- val_curve_amplitude_loss: `0.057304`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006622`
- test_mae: `0.002281`
- test_rmse: `0.003346`
- test_pointwise_loss: `0.006622`
- test_centered_curve_shape_loss: `0.006231`
- test_curve_offset_loss: `0.000391`
- test_curve_amplitude_loss: `0.062548`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002189 deg and RMSE=0.003024 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002281 deg and RMSE=0.003346 deg, which indicates a numerically stable baseline run.
