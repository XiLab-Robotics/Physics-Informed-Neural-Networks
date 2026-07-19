# Residual Harmonic Lstm Sequence Dense360 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints`
- Model Family: `residual_harmonic_lstm_sequence_dense360_global`
- Model Type: `residual_harmonic_lstm_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_lstm_sequence_dense360/2026-07-10-03-42-49__te_residual_harmonic_lstm_sequence_dense360_global__simplified_setpoints/checkpoints/residual_harmonic_lstm_sequence-epoch=055-val_mae=0.00360012.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010959`
- val_mae: `0.003600`
- val_rmse: `0.004473`
- val_pointwise_loss: `0.010959`
- val_centered_curve_shape_loss: `0.006597`
- val_curve_offset_loss: `0.004362`
- val_curve_amplitude_loss: `0.045079`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.037837`
- val_structured_rmse: `0.042648`

## Test Metrics

- test_loss: `0.008568`
- test_mae: `0.003443`
- test_rmse: `0.004246`
- test_pointwise_loss: `0.008568`
- test_centered_curve_shape_loss: `0.003444`
- test_curve_offset_loss: `0.005124`
- test_curve_amplitude_loss: `0.020584`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.040706`
- test_structured_rmse: `0.045400`

## Interpretation

The held-out val error stayed finite with MAE=0.003600 deg and RMSE=0.004473 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003443 deg and RMSE=0.004246 deg, which indicates a numerically stable baseline run.
