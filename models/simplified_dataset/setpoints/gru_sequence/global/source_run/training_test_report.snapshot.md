# Gru Sequence Global Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_global__simplified_setpoints`
- Model Family: `gru_sequence_global`
- Model Type: `gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-11-17-09__te_gru_sequence_global__simplified_setpoints/checkpoints/gru_sequence-epoch=036-val_mae=0.00377716.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011950`
- val_mae: `0.003777`
- val_rmse: `0.004703`
- val_pointwise_loss: `0.011950`
- val_centered_curve_shape_loss: `0.007494`
- val_curve_offset_loss: `0.004456`
- val_curve_amplitude_loss: `0.060509`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009433`
- test_mae: `0.003590`
- test_rmse: `0.004451`
- test_pointwise_loss: `0.009433`
- test_centered_curve_shape_loss: `0.004208`
- test_curve_offset_loss: `0.005225`
- test_curve_amplitude_loss: `0.029079`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003777 deg and RMSE=0.004703 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003590 deg and RMSE=0.004451 deg, which indicates a numerically stable baseline run.
