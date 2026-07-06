# Residual Harmonic Lstm Sequence Dense360 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense360_global`
- Model Family: `residual_harmonic_lstm_sequence_dense360_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-06-30-14-20-06__te_residual_harmonic_lstm_sequence_dense360_global\checkpoints\residual_harmonic_lstm_sequence-epoch=037-val_mae=0.00207083.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005490`
- val_mae: `0.002071`
- val_rmse: `0.002557`
- val_pointwise_loss: `0.005490`
- val_centered_curve_shape_loss: `0.005077`
- val_curve_offset_loss: `0.000413`
- val_curve_amplitude_loss: `0.032944`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039686`
- val_structured_rmse: `0.041896`

## Test Metrics

- test_loss: `0.006515`
- test_mae: `0.002223`
- test_rmse: `0.002815`
- test_pointwise_loss: `0.006515`
- test_centered_curve_shape_loss: `0.005752`
- test_curve_offset_loss: `0.000763`
- test_curve_amplitude_loss: `0.037974`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037334`
- test_structured_rmse: `0.040267`

## Interpretation

The held-out val error stayed finite with MAE=0.002071 deg and RMSE=0.002557 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002223 deg and RMSE=0.002815 deg, which indicates a numerically stable baseline run.
