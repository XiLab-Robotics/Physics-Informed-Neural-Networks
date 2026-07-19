# Residual Harmonic Lstm Sequence Dense240 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_bw__polished_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense240_bw`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-10-01-19-43__te_residual_harmonic_lstm_sequence_dense240_bw__polished_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=073-val_mae=0.00200521.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005280`
- val_mae: `0.002005`
- val_rmse: `0.002784`
- val_pointwise_loss: `0.005280`
- val_centered_curve_shape_loss: `0.004864`
- val_curve_offset_loss: `0.000416`
- val_curve_amplitude_loss: `0.035863`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039578`
- val_structured_rmse: `0.044088`

## Test Metrics

- test_loss: `0.008616`
- test_mae: `0.002316`
- test_rmse: `0.003665`
- test_pointwise_loss: `0.008616`
- test_centered_curve_shape_loss: `0.005723`
- test_curve_offset_loss: `0.002893`
- test_curve_amplitude_loss: `0.045572`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037304`
- test_structured_rmse: `0.042198`

## Interpretation

The held-out val error stayed finite with MAE=0.002005 deg and RMSE=0.002784 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002316 deg and RMSE=0.003665 deg, which indicates a numerically stable baseline run.
