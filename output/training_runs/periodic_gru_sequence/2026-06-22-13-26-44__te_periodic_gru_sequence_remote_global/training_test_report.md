# Periodic Gru Sequence Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_remote_global`
- Model Family: `periodic_gru_sequence`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_gru_sequence\2026-06-22-13-26-44__te_periodic_gru_sequence_remote_global\checkpoints\periodic_gru_sequence-epoch=190-val_mae=0.00127364.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001610`
- val_mae: `0.001274`
- val_rmse: `0.001572`
- val_pointwise_loss: `0.001610`
- val_centered_curve_shape_loss: `0.001198`
- val_curve_offset_loss: `0.000412`
- val_curve_amplitude_loss: `0.004329`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.001741`
- test_mae: `0.001279`
- test_rmse: `0.001638`
- test_pointwise_loss: `0.001741`
- test_centered_curve_shape_loss: `0.001358`
- test_curve_offset_loss: `0.000382`
- test_curve_amplitude_loss: `0.004588`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001274 deg and RMSE=0.001572 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001279 deg and RMSE=0.001638 deg, which indicates a numerically stable baseline run.
