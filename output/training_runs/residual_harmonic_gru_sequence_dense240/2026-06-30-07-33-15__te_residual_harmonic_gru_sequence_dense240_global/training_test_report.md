# Residual Harmonic Gru Sequence Dense240 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_global`
- Model Family: `residual_harmonic_gru_sequence_dense240_global`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense240\2026-06-30-07-33-15__te_residual_harmonic_gru_sequence_dense240_global\checkpoints\residual_harmonic_gru_sequence-epoch=136-val_mae=0.00196656.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005228`
- val_mae: `0.001967`
- val_rmse: `0.002441`
- val_pointwise_loss: `0.005228`
- val_centered_curve_shape_loss: `0.004963`
- val_curve_offset_loss: `0.000264`
- val_curve_amplitude_loss: `0.038133`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039816`
- val_structured_rmse: `0.042015`

## Test Metrics

- test_loss: `0.005948`
- test_mae: `0.002076`
- test_rmse: `0.002660`
- test_pointwise_loss: `0.005948`
- test_centered_curve_shape_loss: `0.005650`
- test_curve_offset_loss: `0.000298`
- test_curve_amplitude_loss: `0.043105`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037371`
- test_structured_rmse: `0.040311`

## Interpretation

The held-out val error stayed finite with MAE=0.001967 deg and RMSE=0.002441 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002076 deg and RMSE=0.002660 deg, which indicates a numerically stable baseline run.
