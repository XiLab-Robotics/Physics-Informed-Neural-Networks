# Residual Harmonic Gru Sequence Dense360 Fw Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense360_fw`
- Model Family: `residual_harmonic_gru_sequence_dense360_fw`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense360\2026-06-30-09-59-47__te_residual_harmonic_gru_sequence_dense360_fw\checkpoints\residual_harmonic_gru_sequence-epoch=133-val_mae=0.00196756.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005215`
- val_mae: `0.001968`
- val_rmse: `0.002442`
- val_pointwise_loss: `0.005215`
- val_centered_curve_shape_loss: `0.004950`
- val_curve_offset_loss: `0.000265`
- val_curve_amplitude_loss: `0.036071`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039899`
- val_structured_rmse: `0.042093`

## Test Metrics

- test_loss: `0.005930`
- test_mae: `0.002083`
- test_rmse: `0.002673`
- test_pointwise_loss: `0.005930`
- test_centered_curve_shape_loss: `0.005657`
- test_curve_offset_loss: `0.000273`
- test_curve_amplitude_loss: `0.041150`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037404`
- test_structured_rmse: `0.040348`

## Interpretation

The held-out val error stayed finite with MAE=0.001968 deg and RMSE=0.002442 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002083 deg and RMSE=0.002673 deg, which indicates a numerically stable baseline run.
