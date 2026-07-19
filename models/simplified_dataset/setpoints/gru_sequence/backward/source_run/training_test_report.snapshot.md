# Gru Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_bw__simplified_setpoints`
- Model Family: `gru_sequence_bw`
- Model Type: `gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-11-31-51__te_gru_sequence_bw__simplified_setpoints/checkpoints/gru_sequence-epoch=132-val_mae=0.00366119.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011387`
- val_mae: `0.003661`
- val_rmse: `0.004557`
- val_pointwise_loss: `0.011387`
- val_centered_curve_shape_loss: `0.007282`
- val_curve_offset_loss: `0.004105`
- val_curve_amplitude_loss: `0.079943`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008987`
- test_mae: `0.003510`
- test_rmse: `0.004341`
- test_pointwise_loss: `0.008987`
- test_centered_curve_shape_loss: `0.003988`
- test_curve_offset_loss: `0.005000`
- test_curve_amplitude_loss: `0.044572`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003661 deg and RMSE=0.004557 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003510 deg and RMSE=0.004341 deg, which indicates a numerically stable baseline run.
