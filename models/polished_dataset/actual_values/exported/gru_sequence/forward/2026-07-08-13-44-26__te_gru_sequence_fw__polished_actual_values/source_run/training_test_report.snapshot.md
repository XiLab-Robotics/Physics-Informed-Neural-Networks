# Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_fw__polished_actual_values`
- Model Family: `gru_sequence_fw`
- Model Type: `gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-13-44-26__te_gru_sequence_fw__polished_actual_values/checkpoints/gru_sequence-epoch=149-val_mae=0.00216525.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005779`
- val_mae: `0.002165`
- val_rmse: `0.002996`
- val_pointwise_loss: `0.005779`
- val_centered_curve_shape_loss: `0.005386`
- val_curve_offset_loss: `0.000393`
- val_curve_amplitude_loss: `0.057630`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006592`
- test_mae: `0.002274`
- test_rmse: `0.003341`
- test_pointwise_loss: `0.006592`
- test_centered_curve_shape_loss: `0.006217`
- test_curve_offset_loss: `0.000375`
- test_curve_amplitude_loss: `0.063294`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002165 deg and RMSE=0.002996 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002274 deg and RMSE=0.003341 deg, which indicates a numerically stable baseline run.
