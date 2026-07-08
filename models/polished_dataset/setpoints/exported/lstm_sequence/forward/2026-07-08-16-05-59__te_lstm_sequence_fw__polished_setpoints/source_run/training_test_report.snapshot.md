# Lstm Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_fw__polished_setpoints`
- Model Family: `lstm_sequence_fw`
- Model Type: `lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-16-05-59__te_lstm_sequence_fw__polished_setpoints/checkpoints/lstm_sequence-epoch=078-val_mae=0.00219094.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005861`
- val_mae: `0.002191`
- val_rmse: `0.003024`
- val_pointwise_loss: `0.005861`
- val_centered_curve_shape_loss: `0.005371`
- val_curve_offset_loss: `0.000490`
- val_curve_amplitude_loss: `0.058320`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009286`
- test_mae: `0.002464`
- test_rmse: `0.003859`
- test_pointwise_loss: `0.009286`
- test_centered_curve_shape_loss: `0.006272`
- test_curve_offset_loss: `0.003014`
- test_curve_amplitude_loss: `0.070534`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002191 deg and RMSE=0.003024 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002464 deg and RMSE=0.003859 deg, which indicates a numerically stable baseline run.
