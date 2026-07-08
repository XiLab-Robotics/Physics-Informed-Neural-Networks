# Periodic Gru Sequence Global Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_global__polished_setpoints`
- Model Family: `periodic_gru_sequence_global`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-08-22-43-56__te_periodic_gru_sequence_global__polished_setpoints/checkpoints/periodic_gru_sequence-epoch=045-val_mae=0.00186736.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004757`
- val_mae: `0.001867`
- val_rmse: `0.002625`
- val_pointwise_loss: `0.004757`
- val_centered_curve_shape_loss: `0.004241`
- val_curve_offset_loss: `0.000516`
- val_curve_amplitude_loss: `0.025261`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.007958`
- test_mae: `0.002143`
- test_rmse: `0.003467`
- test_pointwise_loss: `0.007958`
- test_centered_curve_shape_loss: `0.004908`
- test_curve_offset_loss: `0.003051`
- test_curve_amplitude_loss: `0.035265`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001867 deg and RMSE=0.002625 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002143 deg and RMSE=0.003467 deg, which indicates a numerically stable baseline run.
