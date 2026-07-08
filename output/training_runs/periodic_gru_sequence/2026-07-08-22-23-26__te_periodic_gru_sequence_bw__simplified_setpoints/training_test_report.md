# Periodic Gru Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_bw__simplified_setpoints`
- Model Family: `periodic_gru_sequence_bw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-08-22-23-26__te_periodic_gru_sequence_bw__simplified_setpoints/checkpoints/periodic_gru_sequence-epoch=081-val_mae=0.00349987.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.009971`
- val_mae: `0.003500`
- val_rmse: `0.004293`
- val_pointwise_loss: `0.009971`
- val_centered_curve_shape_loss: `0.005775`
- val_curve_offset_loss: `0.004196`
- val_curve_amplitude_loss: `0.041717`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007548`
- test_mae: `0.003250`
- test_rmse: `0.003969`
- test_pointwise_loss: `0.007548`
- test_centered_curve_shape_loss: `0.002807`
- test_curve_offset_loss: `0.004741`
- test_curve_amplitude_loss: `0.017082`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003500 deg and RMSE=0.004293 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003250 deg and RMSE=0.003969 deg, which indicates a numerically stable baseline run.
