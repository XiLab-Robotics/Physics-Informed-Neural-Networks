# Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_fw`
- Model Family: `gru_sequence_fw`
- Model Type: `gru_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\gru_sequence\2026-06-26-08-53-33__te_gru_sequence_fw\checkpoints\gru_sequence-epoch=083-val_mae=0.00215611.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005773`
- val_mae: `0.002156`
- val_rmse: `0.002690`
- val_pointwise_loss: `0.005773`
- val_centered_curve_shape_loss: `0.005421`
- val_curve_offset_loss: `0.000352`
- val_curve_amplitude_loss: `0.060567`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006567`
- test_mae: `0.002260`
- test_rmse: `0.002905`
- test_pointwise_loss: `0.006567`
- test_centered_curve_shape_loss: `0.006229`
- test_curve_offset_loss: `0.000338`
- test_curve_amplitude_loss: `0.066200`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002156 deg and RMSE=0.002690 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002260 deg and RMSE=0.002905 deg, which indicates a numerically stable baseline run.
