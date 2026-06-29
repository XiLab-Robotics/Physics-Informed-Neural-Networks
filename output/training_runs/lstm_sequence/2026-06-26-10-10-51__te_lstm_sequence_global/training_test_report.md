# Lstm Sequence Global Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_global`
- Model Family: `lstm_sequence_global`
- Model Type: `lstm_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\lstm_sequence\2026-06-26-10-10-51__te_lstm_sequence_global\checkpoints\lstm_sequence-epoch=120-val_mae=0.00215068.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005760`
- val_mae: `0.002151`
- val_rmse: `0.002673`
- val_pointwise_loss: `0.005760`
- val_centered_curve_shape_loss: `0.005400`
- val_curve_offset_loss: `0.000361`
- val_curve_amplitude_loss: `0.057010`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006534`
- test_mae: `0.002258`
- test_rmse: `0.002894`
- test_pointwise_loss: `0.006534`
- test_centered_curve_shape_loss: `0.006208`
- test_curve_offset_loss: `0.000326`
- test_curve_amplitude_loss: `0.063140`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002151 deg and RMSE=0.002673 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002258 deg and RMSE=0.002894 deg, which indicates a numerically stable baseline run.
