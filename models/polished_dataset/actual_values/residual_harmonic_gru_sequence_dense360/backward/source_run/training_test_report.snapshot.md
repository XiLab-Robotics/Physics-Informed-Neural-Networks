# Residual Harmonic Gru Sequence Dense360 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values`
- Model Family: `residual_harmonic_gru_sequence_dense360_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-17-49-07__te_residual_harmonic_gru_sequence_dense360_bw__polished_actual_values/checkpoints/residual_harmonic_gru_sequence-epoch=116-val_mae=0.00195966.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005200`
- val_mae: `0.001960`
- val_rmse: `0.002740`
- val_pointwise_loss: `0.005200`
- val_centered_curve_shape_loss: `0.004870`
- val_curve_offset_loss: `0.000330`
- val_curve_amplitude_loss: `0.035024`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039617`
- val_structured_rmse: `0.044131`

## Test Metrics

- test_loss: `0.005948`
- test_mae: `0.002071`
- test_rmse: `0.003106`
- test_pointwise_loss: `0.005948`
- test_centered_curve_shape_loss: `0.005655`
- test_curve_offset_loss: `0.000293`
- test_curve_amplitude_loss: `0.039702`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037326`
- test_structured_rmse: `0.042236`

## Interpretation

The held-out val error stayed finite with MAE=0.001960 deg and RMSE=0.002740 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002071 deg and RMSE=0.003106 deg, which indicates a numerically stable baseline run.
