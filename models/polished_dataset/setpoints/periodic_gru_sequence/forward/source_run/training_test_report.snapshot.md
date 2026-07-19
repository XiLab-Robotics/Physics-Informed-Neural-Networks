# Periodic Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_fw__polished_setpoints`
- Model Family: `periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-08-22-57-44__te_periodic_gru_sequence_fw__polished_setpoints/checkpoints/periodic_gru_sequence-epoch=091-val_mae=0.00183161.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004697`
- val_mae: `0.001832`
- val_rmse: `0.002570`
- val_pointwise_loss: `0.004697`
- val_centered_curve_shape_loss: `0.004252`
- val_curve_offset_loss: `0.000446`
- val_curve_amplitude_loss: `0.022413`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007731`
- test_mae: `0.002108`
- test_rmse: `0.003430`
- test_pointwise_loss: `0.007731`
- test_centered_curve_shape_loss: `0.004786`
- test_curve_offset_loss: `0.002945`
- test_curve_amplitude_loss: `0.031060`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001832 deg and RMSE=0.002570 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002108 deg and RMSE=0.003430 deg, which indicates a numerically stable baseline run.
