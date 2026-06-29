# Periodic Lstm Sequence Global Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_global`
- Model Family: `periodic_lstm_sequence_global`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_lstm_sequence\2026-06-26-17-47-56__te_periodic_lstm_sequence_global\checkpoints\periodic_lstm_sequence-epoch=256-val_mae=0.00118477.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001445`
- val_mae: `0.001185`
- val_rmse: `0.001466`
- val_pointwise_loss: `0.001445`
- val_centered_curve_shape_loss: `0.001056`
- val_curve_offset_loss: `0.000389`
- val_curve_amplitude_loss: `0.003368`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.001541`
- test_mae: `0.001187`
- test_rmse: `0.001505`
- test_pointwise_loss: `0.001541`
- test_centered_curve_shape_loss: `0.001135`
- test_curve_offset_loss: `0.000407`
- test_curve_amplitude_loss: `0.003438`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001185 deg and RMSE=0.001466 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001187 deg and RMSE=0.001505 deg, which indicates a numerically stable baseline run.
