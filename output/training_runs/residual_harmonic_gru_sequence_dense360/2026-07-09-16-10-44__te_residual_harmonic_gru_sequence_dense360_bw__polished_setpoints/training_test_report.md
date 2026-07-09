# Residual Harmonic Gru Sequence Dense360 Bw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints`
- Model Family: `residual_harmonic_gru_sequence_dense360_bw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/residual_harmonic_gru_sequence_dense360/2026-07-09-16-10-44__te_residual_harmonic_gru_sequence_dense360_bw__polished_setpoints/checkpoints/residual_harmonic_gru_sequence-epoch=064-val_mae=0.00200024.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005305`
- val_mae: `0.002000`
- val_rmse: `0.002783`
- val_pointwise_loss: `0.005305`
- val_centered_curve_shape_loss: `0.004891`
- val_curve_offset_loss: `0.000414`
- val_curve_amplitude_loss: `0.035091`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039492`
- val_structured_rmse: `0.043997`

## Test Metrics

- test_loss: `0.008646`
- test_mae: `0.002292`
- test_rmse: `0.003649`
- test_pointwise_loss: `0.008646`
- test_centered_curve_shape_loss: `0.005754`
- test_curve_offset_loss: `0.002893`
- test_curve_amplitude_loss: `0.045554`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037269`
- test_structured_rmse: `0.042140`

## Interpretation

The held-out val error stayed finite with MAE=0.002000 deg and RMSE=0.002783 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002292 deg and RMSE=0.003649 deg, which indicates a numerically stable baseline run.
