# Residual Harmonic Lstm Sequence Dense240 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_fw`
- Model Family: `residual_harmonic_lstm_sequence_dense240_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-06-30-13-32-17__te_residual_harmonic_lstm_sequence_dense240_fw\checkpoints\residual_harmonic_lstm_sequence-epoch=032-val_mae=0.00204432.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005404`
- val_mae: `0.002044`
- val_rmse: `0.002532`
- val_pointwise_loss: `0.005404`
- val_centered_curve_shape_loss: `0.004977`
- val_curve_offset_loss: `0.000426`
- val_curve_amplitude_loss: `0.036569`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039733`
- val_structured_rmse: `0.041935`

## Test Metrics

- test_loss: `0.006179`
- test_mae: `0.002147`
- test_rmse: `0.002745`
- test_pointwise_loss: `0.006179`
- test_centered_curve_shape_loss: `0.005736`
- test_curve_offset_loss: `0.000443`
- test_curve_amplitude_loss: `0.041237`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037336`
- test_structured_rmse: `0.040269`

## Interpretation

The held-out val error stayed finite with MAE=0.002044 deg and RMSE=0.002532 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002147 deg and RMSE=0.002745 deg, which indicates a numerically stable baseline run.
