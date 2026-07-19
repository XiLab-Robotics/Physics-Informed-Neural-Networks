# Periodic Gru Sequence Global Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_global__simplified_setpoints`
- Model Family: `periodic_gru_sequence_global`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-08-22-04-46__te_periodic_gru_sequence_global__simplified_setpoints/checkpoints/periodic_gru_sequence-epoch=060-val_mae=0.00347740.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010029`
- val_mae: `0.003477`
- val_rmse: `0.004273`
- val_pointwise_loss: `0.010029`
- val_centered_curve_shape_loss: `0.005827`
- val_curve_offset_loss: `0.004202`
- val_curve_amplitude_loss: `0.040777`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007874`
- test_mae: `0.003332`
- test_rmse: `0.004068`
- test_pointwise_loss: `0.007874`
- test_centered_curve_shape_loss: `0.002833`
- test_curve_offset_loss: `0.005041`
- test_curve_amplitude_loss: `0.016643`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003477 deg and RMSE=0.004273 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003332 deg and RMSE=0.004068 deg, which indicates a numerically stable baseline run.
