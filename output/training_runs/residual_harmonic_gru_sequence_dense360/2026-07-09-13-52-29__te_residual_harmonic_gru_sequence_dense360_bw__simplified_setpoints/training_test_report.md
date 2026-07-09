# Residual Harmonic Gru Sequence Dense360 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints`
- Model Family: `residual_harmonic_gru_sequence_dense360_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-13-52-29__te_residual_harmonic_gru_sequence_dense360_bw__simplified_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=077-val_mae=0.00358806.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010833`
- val_mae: `0.003588`
- val_rmse: `0.004446`
- val_pointwise_loss: `0.010833`
- val_centered_curve_shape_loss: `0.006618`
- val_curve_offset_loss: `0.004215`
- val_curve_amplitude_loss: `0.045859`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037826`
- val_structured_rmse: `0.042663`

## Test Metrics

- test_loss: `0.008365`
- test_mae: `0.003395`
- test_rmse: `0.004190`
- test_pointwise_loss: `0.008365`
- test_centered_curve_shape_loss: `0.003480`
- test_curve_offset_loss: `0.004884`
- test_curve_amplitude_loss: `0.021112`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040700`
- test_structured_rmse: `0.045409`

## Interpretation

The held-out val error stayed finite with MAE=0.003588 deg and RMSE=0.004446 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003395 deg and RMSE=0.004190 deg, which indicates a numerically stable baseline run.
