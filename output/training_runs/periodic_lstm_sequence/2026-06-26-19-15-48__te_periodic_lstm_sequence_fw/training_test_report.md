# Periodic Lstm Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_lstm_sequence_fw`
- Model Family: `periodic_lstm_sequence_fw`
- Model Type: `periodic_lstm_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_lstm_sequence\2026-06-26-19-15-48__te_periodic_lstm_sequence_fw\checkpoints\periodic_lstm_sequence-epoch=167-val_mae=0.00149466.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002532`
- val_mae: `0.001495`
- val_rmse: `0.001848`
- val_pointwise_loss: `0.002532`
- val_centered_curve_shape_loss: `0.002116`
- val_curve_offset_loss: `0.000417`
- val_curve_amplitude_loss: `0.008304`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.002860`
- test_mae: `0.001547`
- test_rmse: `0.001976`
- test_pointwise_loss: `0.002860`
- test_centered_curve_shape_loss: `0.002461`
- test_curve_offset_loss: `0.000399`
- test_curve_amplitude_loss: `0.009958`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001495 deg and RMSE=0.001848 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001547 deg and RMSE=0.001976 deg, which indicates a numerically stable baseline run.
