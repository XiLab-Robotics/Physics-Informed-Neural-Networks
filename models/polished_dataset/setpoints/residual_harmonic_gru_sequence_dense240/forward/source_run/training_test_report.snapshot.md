# Residual Harmonic Gru Sequence Dense240 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints`
- Model Family: `residual_harmonic_gru_sequence_dense240_fw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-52-16__te_residual_harmonic_gru_sequence_dense240_fw__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=110-val_mae=0.00198772.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005299`
- val_mae: `0.001988`
- val_rmse: `0.002769`
- val_pointwise_loss: `0.005299`
- val_centered_curve_shape_loss: `0.004878`
- val_curve_offset_loss: `0.000421`
- val_curve_amplitude_loss: `0.035113`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039634`
- val_structured_rmse: `0.044116`

## Test Metrics

- test_loss: `0.008535`
- test_mae: `0.002256`
- test_rmse: `0.003614`
- test_pointwise_loss: `0.008535`
- test_centered_curve_shape_loss: `0.005724`
- test_curve_offset_loss: `0.002811`
- test_curve_amplitude_loss: `0.045221`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037316`
- test_structured_rmse: `0.042199`

## Interpretation

The held-out val error stayed finite with MAE=0.001988 deg and RMSE=0.002769 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002256 deg and RMSE=0.003614 deg, which indicates a numerically stable baseline run.
