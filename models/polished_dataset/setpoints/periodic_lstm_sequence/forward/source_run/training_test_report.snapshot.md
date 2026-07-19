# Periodic Lstm Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_fw__polished_setpoints`
- Model Family: `periodic_lstm_sequence_fw`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_lstm_sequence/2026-07-09-03-42-29__te_periodic_lstm_sequence_fw__polished_setpoints/checkpoints/periodic_lstm_sequence-epoch=047-val_mae=0.00186699.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004753`
- val_mae: `0.001867`
- val_rmse: `0.002597`
- val_pointwise_loss: `0.004753`
- val_centered_curve_shape_loss: `0.004253`
- val_curve_offset_loss: `0.000500`
- val_curve_amplitude_loss: `0.023765`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008113`
- test_mae: `0.002176`
- test_rmse: `0.003521`
- test_pointwise_loss: `0.008113`
- test_centered_curve_shape_loss: `0.004933`
- test_curve_offset_loss: `0.003180`
- test_curve_amplitude_loss: `0.033215`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001867 deg and RMSE=0.002597 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002176 deg and RMSE=0.003521 deg, which indicates a numerically stable baseline run.
