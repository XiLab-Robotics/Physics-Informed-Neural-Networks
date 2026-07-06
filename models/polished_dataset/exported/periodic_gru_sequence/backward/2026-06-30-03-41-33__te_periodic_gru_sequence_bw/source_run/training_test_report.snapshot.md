# Periodic Gru Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_bw`
- Model Family: `periodic_gru_sequence_bw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_gru_sequence\2026-06-30-03-41-33__te_periodic_gru_sequence_bw\checkpoints\periodic_gru_sequence-epoch=242-val_mae=0.00115776.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001312`
- val_mae: `0.001158`
- val_rmse: `0.001434`
- val_pointwise_loss: `0.001312`
- val_centered_curve_shape_loss: `0.000843`
- val_curve_offset_loss: `0.000469`
- val_curve_amplitude_loss: `0.002053`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.001415`
- test_mae: `0.001166`
- test_rmse: `0.001481`
- test_pointwise_loss: `0.001415`
- test_centered_curve_shape_loss: `0.000997`
- test_curve_offset_loss: `0.000417`
- test_curve_amplitude_loss: `0.002756`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001158 deg and RMSE=0.001434 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001166 deg and RMSE=0.001481 deg, which indicates a numerically stable baseline run.
