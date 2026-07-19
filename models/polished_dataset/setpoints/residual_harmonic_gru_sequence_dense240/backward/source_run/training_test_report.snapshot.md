# Residual Harmonic Gru Sequence Dense240 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints`
- Model Family: `residual_harmonic_gru_sequence_dense240_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense240/2026-07-09-11-12-09__te_residual_harmonic_gru_sequence_dense240_bw__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=069-val_mae=0.00196095.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005222`
- val_mae: `0.001961`
- val_rmse: `0.002748`
- val_pointwise_loss: `0.005222`
- val_centered_curve_shape_loss: `0.004864`
- val_curve_offset_loss: `0.000359`
- val_curve_amplitude_loss: `0.035423`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039573`
- val_structured_rmse: `0.044084`

## Test Metrics

- test_loss: `0.008621`
- test_mae: `0.002262`
- test_rmse: `0.003634`
- test_pointwise_loss: `0.008621`
- test_centered_curve_shape_loss: `0.005727`
- test_curve_offset_loss: `0.002894`
- test_curve_amplitude_loss: `0.045536`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037298`
- test_structured_rmse: `0.042193`

## Interpretation

The held-out val error stayed finite with MAE=0.001961 deg and RMSE=0.002748 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002262 deg and RMSE=0.003634 deg, which indicates a numerically stable baseline run.
