# Gru Sequence Fw Training And Testing Report

## Overview

- Run Name: `te_gru_sequence_fw__polished_setpoints`
- Model Family: `gru_sequence_fw`
- Model Type: `gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/gru_sequence/2026-07-08-12-18-02__te_gru_sequence_fw__polished_setpoints/checkpoints/gru_sequence-epoch=152-val_mae=0.00216223.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005768`
- val_mae: `0.002162`
- val_rmse: `0.002979`
- val_pointwise_loss: `0.005768`
- val_centered_curve_shape_loss: `0.005349`
- val_curve_offset_loss: `0.000419`
- val_curve_amplitude_loss: `0.061304`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.009185`
- test_mae: `0.002431`
- test_rmse: `0.003811`
- test_pointwise_loss: `0.009185`
- test_centered_curve_shape_loss: `0.006258`
- test_curve_offset_loss: `0.002927`
- test_curve_amplitude_loss: `0.073705`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.002162 deg and RMSE=0.002979 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002431 deg and RMSE=0.003811 deg, which indicates a numerically stable baseline run.
