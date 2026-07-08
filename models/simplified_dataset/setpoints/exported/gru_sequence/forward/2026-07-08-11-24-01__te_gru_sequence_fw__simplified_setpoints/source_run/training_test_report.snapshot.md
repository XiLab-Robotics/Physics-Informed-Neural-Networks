# Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_fw__simplified_setpoints`
- Model Family: `gru_sequence_fw`
- Model Type: `gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-11-24-01__te_gru_sequence_fw__simplified_setpoints/checkpoints/gru_sequence-epoch=043-val_mae=0.00375895.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011888`
- val_mae: `0.003759`
- val_rmse: `0.004674`
- val_pointwise_loss: `0.011888`
- val_centered_curve_shape_loss: `0.007467`
- val_curve_offset_loss: `0.004421`
- val_curve_amplitude_loss: `0.066231`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009259`
- test_mae: `0.003584`
- test_rmse: `0.004393`
- test_pointwise_loss: `0.009259`
- test_centered_curve_shape_loss: `0.004172`
- test_curve_offset_loss: `0.005087`
- test_curve_amplitude_loss: `0.032906`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003759 deg and RMSE=0.004674 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003584 deg and RMSE=0.004393 deg, which indicates a numerically stable baseline run.
