# Lstm Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_bw`
- Model Family: `lstm_sequence_bw`
- Model Type: `lstm_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\lstm_sequence\2026-06-26-11-50-45__te_lstm_sequence_bw\checkpoints\lstm_sequence-epoch=142-val_mae=0.00215130.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005793`
- val_mae: `0.002151`
- val_rmse: `0.002684`
- val_pointwise_loss: `0.005793`
- val_centered_curve_shape_loss: `0.005398`
- val_curve_offset_loss: `0.000395`
- val_curve_amplitude_loss: `0.058807`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006521`
- test_mae: `0.002240`
- test_rmse: `0.002892`
- test_pointwise_loss: `0.006521`
- test_centered_curve_shape_loss: `0.006173`
- test_curve_offset_loss: `0.000348`
- test_curve_amplitude_loss: `0.064585`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002151 deg and RMSE=0.002684 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002240 deg and RMSE=0.002892 deg, which indicates a numerically stable baseline run.
