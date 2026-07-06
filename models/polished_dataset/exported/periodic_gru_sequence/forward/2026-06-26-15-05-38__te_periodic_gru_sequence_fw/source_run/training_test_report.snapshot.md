# Periodic Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_gru_sequence_fw`
- Model Family: `periodic_gru_sequence_fw`
- Model Type: `periodic_gru_sequence`
- Best Checkpoint: `C:\Users\XiLabTRig\Documents\Physics-Informed Machine Learning\StandardML - Codex\output\training_runs\periodic_gru_sequence\2026-06-26-15-05-38__te_periodic_gru_sequence_fw\checkpoints\periodic_gru_sequence-epoch=249-val_mae=0.00109946.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001129`
- val_mae: `0.001099`
- val_rmse: `0.001358`
- val_pointwise_loss: `0.001129`
- val_centered_curve_shape_loss: `0.000780`
- val_curve_offset_loss: `0.000349`
- val_curve_amplitude_loss: `0.003099`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.001277`
- test_mae: `0.001101`
- test_rmse: `0.001409`
- test_pointwise_loss: `0.001277`
- test_centered_curve_shape_loss: `0.001005`
- test_curve_offset_loss: `0.000272`
- test_curve_amplitude_loss: `0.003548`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001099 deg and RMSE=0.001358 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001101 deg and RMSE=0.001409 deg, which indicates a numerically stable baseline run.
