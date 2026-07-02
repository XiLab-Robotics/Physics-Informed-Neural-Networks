# Residual Harmonic Gru Sequence Dense240 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_fw`
- Model Family: `residual_harmonic_gru_sequence_dense240_fw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense240\2026-06-30-08-20-41__te_residual_harmonic_gru_sequence_dense240_fw\checkpoints\residual_harmonic_gru_sequence-epoch=068-val_mae=0.00202486.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005332`
- val_mae: `0.002025`
- val_rmse: `0.002503`
- val_pointwise_loss: `0.005332`
- val_centered_curve_shape_loss: `0.004965`
- val_curve_offset_loss: `0.000366`
- val_curve_amplitude_loss: `0.033996`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039708`
- val_structured_rmse: `0.041909`

## Test Metrics

- test_loss: `0.006053`
- test_mae: `0.002143`
- test_rmse: `0.002729`
- test_pointwise_loss: `0.006053`
- test_centered_curve_shape_loss: `0.005690`
- test_curve_offset_loss: `0.000364`
- test_curve_amplitude_loss: `0.038365`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037326`
- test_structured_rmse: `0.040254`

## Interpretation

The held-out val error stayed finite with MAE=0.002025 deg and RMSE=0.002503 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002143 deg and RMSE=0.002729 deg, which indicates a numerically stable baseline run.
