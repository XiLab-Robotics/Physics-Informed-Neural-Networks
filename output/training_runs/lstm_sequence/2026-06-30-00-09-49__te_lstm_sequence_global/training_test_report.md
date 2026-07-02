# Lstm Sequence Global Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_global`
- Model Family: `lstm_sequence_global`
- Model Type: `lstm_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\lstm_sequence\2026-06-30-00-09-49__te_lstm_sequence_global\checkpoints\lstm_sequence-epoch=145-val_mae=0.00213809.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005749`
- val_mae: `0.002138`
- val_rmse: `0.002666`
- val_pointwise_loss: `0.005749`
- val_centered_curve_shape_loss: `0.005394`
- val_curve_offset_loss: `0.000355`
- val_curve_amplitude_loss: `0.058617`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006607`
- test_mae: `0.002265`
- test_rmse: `0.002905`
- test_pointwise_loss: `0.006607`
- test_centered_curve_shape_loss: `0.006125`
- test_curve_offset_loss: `0.000482`
- test_curve_amplitude_loss: `0.064375`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002138 deg and RMSE=0.002666 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002265 deg and RMSE=0.002905 deg, which indicates a numerically stable baseline run.
