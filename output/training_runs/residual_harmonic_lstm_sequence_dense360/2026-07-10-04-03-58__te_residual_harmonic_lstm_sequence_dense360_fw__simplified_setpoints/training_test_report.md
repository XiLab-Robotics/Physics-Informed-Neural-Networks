# Residual Harmonic Lstm Sequence Dense360 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense360_fw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-04-03-58__te_residual_harmonic_lstm_sequence_dense360_fw__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=047-val_mae=0.00358223.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010713`
- val_mae: `0.003582`
- val_rmse: `0.004430`
- val_pointwise_loss: `0.010713`
- val_centered_curve_shape_loss: `0.006600`
- val_curve_offset_loss: `0.004112`
- val_curve_amplitude_loss: `0.042028`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037842`
- val_structured_rmse: `0.042648`

## Test Metrics

- test_loss: `0.008373`
- test_mae: `0.003402`
- test_rmse: `0.004177`
- test_pointwise_loss: `0.008373`
- test_centered_curve_shape_loss: `0.003447`
- test_curve_offset_loss: `0.004926`
- test_curve_amplitude_loss: `0.018063`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040708`
- test_structured_rmse: `0.045401`

## Interpretation

The held-out val error stayed finite with MAE=0.003582 deg and RMSE=0.004430 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003402 deg and RMSE=0.004177 deg, which indicates a numerically stable baseline run.
