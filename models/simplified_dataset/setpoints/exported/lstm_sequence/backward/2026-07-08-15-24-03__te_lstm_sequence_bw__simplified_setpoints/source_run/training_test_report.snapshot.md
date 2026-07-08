# Lstm Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_bw__simplified_setpoints`
- Model Family: `lstm_sequence_bw`
- Model Type: `lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/lstm_sequence/2026-07-08-15-24-03__te_lstm_sequence_bw__simplified_setpoints/checkpoints/lstm_sequence-epoch=091-val_mae=0.00367749.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.011566`
- val_mae: `0.003677`
- val_rmse: `0.004581`
- val_pointwise_loss: `0.011566`
- val_centered_curve_shape_loss: `0.007349`
- val_curve_offset_loss: `0.004217`
- val_curve_amplitude_loss: `0.083128`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.008987`
- test_mae: `0.003463`
- test_rmse: `0.004340`
- test_pointwise_loss: `0.008987`
- test_centered_curve_shape_loss: `0.004053`
- test_curve_offset_loss: `0.004934`
- test_curve_amplitude_loss: `0.047945`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.003677 deg and RMSE=0.004581 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003463 deg and RMSE=0.004340 deg, which indicates a numerically stable baseline run.
