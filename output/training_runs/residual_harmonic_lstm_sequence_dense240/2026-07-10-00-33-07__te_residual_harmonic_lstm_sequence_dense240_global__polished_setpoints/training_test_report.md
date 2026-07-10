# Residual Harmonic Lstm Sequence Dense240 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense240_global__polished_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense240_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense240/2026-07-10-00-33-07__te_residual_harmonic_lstm_sequence_dense240_global__polished_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=045-val_mae=0.00200392.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005299`
- val_mae: `0.002004`
- val_rmse: `0.002779`
- val_pointwise_loss: `0.005299`
- val_centered_curve_shape_loss: `0.004912`
- val_curve_offset_loss: `0.000387`
- val_curve_amplitude_loss: `0.034918`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039622`
- val_structured_rmse: `0.044203`

## Test Metrics

- test_loss: `0.008647`
- test_mae: `0.002297`
- test_rmse: `0.003647`
- test_pointwise_loss: `0.008647`
- test_centered_curve_shape_loss: `0.005761`
- test_curve_offset_loss: `0.002886`
- test_curve_amplitude_loss: `0.044627`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037340`
- test_structured_rmse: `0.042301`

## Interpretation

The held-out val error stayed finite with MAE=0.002004 deg and RMSE=0.002779 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002297 deg and RMSE=0.003647 deg, which indicates a numerically stable baseline run.
