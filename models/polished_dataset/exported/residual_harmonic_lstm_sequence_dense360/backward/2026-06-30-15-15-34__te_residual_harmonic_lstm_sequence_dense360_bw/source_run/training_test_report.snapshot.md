# Residual Harmonic Lstm Sequence Dense360 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense360_bw`
- Model Family: `residual_harmonic_lstm_sequence_dense360_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense360\2026-06-30-15-15-34__te_residual_harmonic_lstm_sequence_dense360_bw\checkpoints\residual_harmonic_lstm_sequence-epoch=100-val_mae=0.00200719.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005366`
- val_mae: `0.002007`
- val_rmse: `0.002493`
- val_pointwise_loss: `0.005366`
- val_centered_curve_shape_loss: `0.005019`
- val_curve_offset_loss: `0.000347`
- val_curve_amplitude_loss: `0.038245`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039745`
- val_structured_rmse: `0.041950`

## Test Metrics

- test_loss: `0.006045`
- test_mae: `0.002097`
- test_rmse: `0.002693`
- test_pointwise_loss: `0.006045`
- test_centered_curve_shape_loss: `0.005764`
- test_curve_offset_loss: `0.000280`
- test_curve_amplitude_loss: `0.043314`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037350`
- test_structured_rmse: `0.040286`

## Interpretation

The held-out val error stayed finite with MAE=0.002007 deg and RMSE=0.002493 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002097 deg and RMSE=0.002693 deg, which indicates a numerically stable baseline run.
