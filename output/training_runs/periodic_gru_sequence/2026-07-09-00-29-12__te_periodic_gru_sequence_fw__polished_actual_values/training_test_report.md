# Periodic Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_fw__polished_actual_values`
- Model Family: `periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/periodic_gru_sequence/2026-07-09-00-29-12__te_periodic_gru_sequence_fw__polished_actual_values/checkpoints/periodic_gru_sequence-epoch=200-val_mae=0.00150079.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002777`
- val_mae: `0.001501`
- val_rmse: `0.002083`
- val_pointwise_loss: `0.002777`
- val_centered_curve_shape_loss: `0.002421`
- val_curve_offset_loss: `0.000356`
- val_curve_amplitude_loss: `0.011367`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003064`
- test_mae: `0.001561`
- test_rmse: `0.002360`
- test_pointwise_loss: `0.003064`
- test_centered_curve_shape_loss: `0.002680`
- test_curve_offset_loss: `0.000383`
- test_curve_amplitude_loss: `0.011508`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001501 deg and RMSE=0.002083 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001561 deg and RMSE=0.002360 deg, which indicates a numerically stable baseline run.
