# Gru Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_bw__polished_actual_values`
- Model Family: `gru_sequence_bw`
- Model Type: `gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-14-10-34__te_gru_sequence_bw__polished_actual_values/checkpoints/gru_sequence-epoch=172-val_mae=0.00214390.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005720`
- val_mae: `0.002144`
- val_rmse: `0.002970`
- val_pointwise_loss: `0.005720`
- val_centered_curve_shape_loss: `0.005383`
- val_curve_offset_loss: `0.000337`
- val_curve_amplitude_loss: `0.058538`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006571`
- test_mae: `0.002258`
- test_rmse: `0.003322`
- test_pointwise_loss: `0.006571`
- test_centered_curve_shape_loss: `0.006189`
- test_curve_offset_loss: `0.000382`
- test_curve_amplitude_loss: `0.064204`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002144 deg and RMSE=0.002970 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002258 deg and RMSE=0.003322 deg, which indicates a numerically stable baseline run.
