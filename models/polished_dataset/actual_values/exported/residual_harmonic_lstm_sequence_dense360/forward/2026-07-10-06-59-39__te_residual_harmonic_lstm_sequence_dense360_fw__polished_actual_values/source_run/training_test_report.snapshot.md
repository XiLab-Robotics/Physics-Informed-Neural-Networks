# Residual Harmonic Lstm Sequence Dense360 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values`
- Model Family: `residual_harmonic_lstm_sequence_dense360_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-59-39__te_residual_harmonic_lstm_sequence_dense360_fw__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=062-val_mae=0.00203211.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005362`
- val_mae: `0.002032`
- val_rmse: `0.002816`
- val_pointwise_loss: `0.005362`
- val_centered_curve_shape_loss: `0.004908`
- val_curve_offset_loss: `0.000454`
- val_curve_amplitude_loss: `0.037707`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039702`
- val_structured_rmse: `0.044398`

## Test Metrics

- test_loss: `0.008651`
- test_mae: `0.002295`
- test_rmse: `0.003624`
- test_pointwise_loss: `0.008651`
- test_centered_curve_shape_loss: `0.005691`
- test_curve_offset_loss: `0.002959`
- test_curve_amplitude_loss: `0.047348`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037421`
- test_structured_rmse: `0.042493`

## Interpretation

The held-out val error stayed finite with MAE=0.002032 deg and RMSE=0.002816 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002295 deg and RMSE=0.003624 deg, which indicates a numerically stable baseline run.
