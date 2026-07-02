# Residual Harmonic Lstm Sequence Dense240 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_bw`
- Model Family: `residual_harmonic_lstm_sequence_dense240_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_lstm_sequence_dense240\2026-06-30-13-54-15__te_residual_harmonic_lstm_sequence_dense240_bw\checkpoints\residual_harmonic_lstm_sequence-epoch=047-val_mae=0.00204037.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005387`
- val_mae: `0.002040`
- val_rmse: `0.002521`
- val_pointwise_loss: `0.005387`
- val_centered_curve_shape_loss: `0.005002`
- val_curve_offset_loss: `0.000385`
- val_curve_amplitude_loss: `0.037172`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039668`
- val_structured_rmse: `0.041875`

## Test Metrics

- test_loss: `0.006199`
- test_mae: `0.002164`
- test_rmse: `0.002757`
- test_pointwise_loss: `0.006199`
- test_centered_curve_shape_loss: `0.005813`
- test_curve_offset_loss: `0.000386`
- test_curve_amplitude_loss: `0.041777`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037320`
- test_structured_rmse: `0.040244`

## Interpretation

The held-out val error stayed finite with MAE=0.002040 deg and RMSE=0.002521 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002164 deg and RMSE=0.002757 deg, which indicates a numerically stable baseline run.
