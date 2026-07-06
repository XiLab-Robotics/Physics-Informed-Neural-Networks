# Residual Harmonic Gru Sequence Dense360 Global Training And Testing Report

## Overview

- Run Name: `te_residual_harmonic_gru_sequence_dense360_global`
- Model Family: `residual_harmonic_gru_sequence_dense360_global`
- Model Type: `residual_harmonic_gru_sequence`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\residual_harmonic_gru_sequence_dense360\2026-06-30-09-29-35__te_residual_harmonic_gru_sequence_dense360_global\checkpoints\residual_harmonic_gru_sequence-epoch=050-val_mae=0.00202033.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005323`
- val_mae: `0.002020`
- val_rmse: `0.002506`
- val_pointwise_loss: `0.005323`
- val_centered_curve_shape_loss: `0.004988`
- val_curve_offset_loss: `0.000335`
- val_curve_amplitude_loss: `0.033694`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_structured_mae: `0.039778`
- val_structured_rmse: `0.041983`

## Test Metrics

- test_loss: `0.006132`
- test_mae: `0.002149`
- test_rmse: `0.002741`
- test_pointwise_loss: `0.006132`
- test_centered_curve_shape_loss: `0.005775`
- test_curve_offset_loss: `0.000357`
- test_curve_amplitude_loss: `0.038996`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_structured_mae: `0.037369`
- test_structured_rmse: `0.040313`

## Interpretation

The held-out val error stayed finite with MAE=0.002020 deg and RMSE=0.002506 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002149 deg and RMSE=0.002741 deg, which indicates a numerically stable baseline run.
