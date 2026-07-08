# Gru Sequence Global Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_global__polished_actual_values`
- Model Family: `gru_sequence_global`
- Model Type: `gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-13-16-43__te_gru_sequence_global__polished_actual_values/checkpoints/gru_sequence-epoch=141-val_mae=0.00217238.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005766`
- val_mae: `0.002172`
- val_rmse: `0.002993`
- val_pointwise_loss: `0.005766`
- val_centered_curve_shape_loss: `0.005393`
- val_curve_offset_loss: `0.000373`
- val_curve_amplitude_loss: `0.057293`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006637`
- test_mae: `0.002292`
- test_rmse: `0.003347`
- test_pointwise_loss: `0.006637`
- test_centered_curve_shape_loss: `0.006223`
- test_curve_offset_loss: `0.000414`
- test_curve_amplitude_loss: `0.063033`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002172 deg and RMSE=0.002993 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002292 deg and RMSE=0.003347 deg, which indicates a numerically stable baseline run.
