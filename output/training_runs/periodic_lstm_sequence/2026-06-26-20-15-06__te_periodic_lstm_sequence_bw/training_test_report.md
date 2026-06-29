# Periodic Lstm Sequence Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_bw`
- Model Family: `periodic_lstm_sequence_bw`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_lstm_sequence\2026-06-26-20-15-06__te_periodic_lstm_sequence_bw\checkpoints\periodic_lstm_sequence-epoch=182-val_mae=0.00123087.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001622`
- val_mae: `0.001231`
- val_rmse: `0.001528`
- val_pointwise_loss: `0.001622`
- val_centered_curve_shape_loss: `0.001322`
- val_curve_offset_loss: `0.000299`
- val_curve_amplitude_loss: `0.006831`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.002062`
- test_mae: `0.001338`
- test_rmse: `0.001719`
- test_pointwise_loss: `0.002062`
- test_centered_curve_shape_loss: `0.001705`
- test_curve_offset_loss: `0.000358`
- test_curve_amplitude_loss: `0.009177`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001231 deg and RMSE=0.001528 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001338 deg and RMSE=0.001719 deg, which indicates a numerically stable baseline run.
