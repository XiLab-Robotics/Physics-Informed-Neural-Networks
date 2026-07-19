# Residual Harmonic Lstm Sequence Dense360 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values`
- Model Family: `residual_harmonic_lstm_sequence_dense360_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-06-44-07__te_residual_harmonic_lstm_sequence_dense360_global__polished_actual_values/checkpoints/residual_harmonic_lstm_sequence-epoch=018-val_mae=0.00209241.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005517`
- val_mae: `0.002092`
- val_rmse: `0.002887`
- val_pointwise_loss: `0.005517`
- val_centered_curve_shape_loss: `0.004994`
- val_curve_offset_loss: `0.000522`
- val_curve_amplitude_loss: `0.035244`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039871`
- val_structured_rmse: `0.044837`

## Test Metrics

- test_loss: `0.008764`
- test_mae: `0.002330`
- test_rmse: `0.003667`
- test_pointwise_loss: `0.008764`
- test_centered_curve_shape_loss: `0.005806`
- test_curve_offset_loss: `0.002958`
- test_curve_amplitude_loss: `0.045261`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037599`
- test_structured_rmse: `0.042916`

## Interpretation

The held-out val error stayed finite with MAE=0.002092 deg and RMSE=0.002887 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002330 deg and RMSE=0.003667 deg, which indicates a numerically stable baseline run.
