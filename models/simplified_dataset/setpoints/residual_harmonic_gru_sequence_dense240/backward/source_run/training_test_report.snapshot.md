# Residual Harmonic Gru Sequence Dense240 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_bw__simplified_setpoints`
- Model Family: `residual_harmonic_gru_sequence_dense240_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-10-09-38__te_residual_harmonic_gru_sequence_dense240_bw__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=057-val_mae=0.00359522.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010787`
- val_mae: `0.003595`
- val_rmse: `0.004433`
- val_pointwise_loss: `0.010787`
- val_centered_curve_shape_loss: `0.006650`
- val_curve_offset_loss: `0.004137`
- val_curve_amplitude_loss: `0.047870`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037826`
- val_structured_rmse: `0.042728`

## Test Metrics

- test_loss: `0.008295`
- test_mae: `0.003429`
- test_rmse: `0.004166`
- test_pointwise_loss: `0.008295`
- test_centered_curve_shape_loss: `0.003453`
- test_curve_offset_loss: `0.004842`
- test_curve_amplitude_loss: `0.022176`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040701`
- test_structured_rmse: `0.045455`

## Interpretation

The held-out val error stayed finite with MAE=0.003595 deg and RMSE=0.004433 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003429 deg and RMSE=0.004166 deg, which indicates a numerically stable baseline run.
