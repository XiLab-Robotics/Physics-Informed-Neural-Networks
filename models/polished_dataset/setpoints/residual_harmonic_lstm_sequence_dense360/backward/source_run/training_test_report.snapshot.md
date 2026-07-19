# Residual Harmonic Lstm Sequence Dense360 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense360_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-05-51-16__te_residual_harmonic_lstm_sequence_dense360_bw__polished_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=102-val_mae=0.00199077.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005272`
- val_mae: `0.001991`
- val_rmse: `0.002762`
- val_pointwise_loss: `0.005272`
- val_centered_curve_shape_loss: `0.004860`
- val_curve_offset_loss: `0.000412`
- val_curve_amplitude_loss: `0.035140`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039637`
- val_structured_rmse: `0.044112`

## Test Metrics

- test_loss: `0.008533`
- test_mae: `0.002282`
- test_rmse: `0.003627`
- test_pointwise_loss: `0.008533`
- test_centered_curve_shape_loss: `0.005701`
- test_curve_offset_loss: `0.002832`
- test_curve_amplitude_loss: `0.045021`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037306`
- test_structured_rmse: `0.042184`

## Interpretation

The held-out val error stayed finite with MAE=0.001991 deg and RMSE=0.002762 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002282 deg and RMSE=0.003627 deg, which indicates a numerically stable baseline run.
