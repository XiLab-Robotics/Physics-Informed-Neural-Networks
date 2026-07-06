# Lstm Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_lstm_sequence_fw`
- Model Family: `lstm_sequence_fw`
- Model Type: `lstm_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\lstm_sequence\2026-06-26-11-02-55__te_lstm_sequence_fw\checkpoints\lstm_sequence-epoch=098-val_mae=0.00215097.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005749`
- val_mae: `0.002151`
- val_rmse: `0.002675`
- val_pointwise_loss: `0.005749`
- val_centered_curve_shape_loss: `0.005408`
- val_curve_offset_loss: `0.000341`
- val_curve_amplitude_loss: `0.055986`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.006590`
- test_mae: `0.002266`
- test_rmse: `0.002915`
- test_pointwise_loss: `0.006590`
- test_centered_curve_shape_loss: `0.006226`
- test_curve_offset_loss: `0.000364`
- test_curve_amplitude_loss: `0.061943`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002151 deg and RMSE=0.002675 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002266 deg and RMSE=0.002915 deg, which indicates a numerically stable baseline run.
