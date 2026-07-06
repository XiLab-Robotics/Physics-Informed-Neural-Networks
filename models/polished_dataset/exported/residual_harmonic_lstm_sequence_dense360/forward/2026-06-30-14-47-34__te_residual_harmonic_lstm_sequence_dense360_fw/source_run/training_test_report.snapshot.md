# Residual Harmonic Lstm Sequence Dense360 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense360_fw`
- Model Family: `residual_harmonic_lstm_sequence_dense360_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-06-30-14-47-34__te_residual_harmonic_lstm_sequence_dense360_fw\checkpoints\residual_harmonic_lstm_sequence-epoch=065-val_mae=0.00206567.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005435`
- val_mae: `0.002066`
- val_rmse: `0.002561`
- val_pointwise_loss: `0.005435`
- val_centered_curve_shape_loss: `0.005048`
- val_curve_offset_loss: `0.000387`
- val_curve_amplitude_loss: `0.034031`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039639`
- val_structured_rmse: `0.041853`

## Test Metrics

- test_loss: `0.006419`
- test_mae: `0.002219`
- test_rmse: `0.002819`
- test_pointwise_loss: `0.006419`
- test_centered_curve_shape_loss: `0.005807`
- test_curve_offset_loss: `0.000612`
- test_curve_amplitude_loss: `0.038927`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037324`
- test_structured_rmse: `0.040250`

## Interpretation

The held-out val error stayed finite with MAE=0.002066 deg and RMSE=0.002561 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002219 deg and RMSE=0.002819 deg, which indicates a numerically stable baseline run.
