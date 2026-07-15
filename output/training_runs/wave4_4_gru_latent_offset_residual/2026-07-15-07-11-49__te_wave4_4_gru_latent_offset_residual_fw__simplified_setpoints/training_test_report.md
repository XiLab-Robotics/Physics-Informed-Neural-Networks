# Wave4 4 Gru Latent Offset Residual Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints`
- Model Family: `wave4_4_gru_latent_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-11-49__te_wave4_4_gru_latent_offset_residual_fw__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=081-val_mae=0.00371922.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010691`
- val_mae: `0.003719`
- val_rmse: `0.004630`
- val_pointwise_loss: `0.005808`
- val_centered_curve_shape_loss: `0.007423`
- val_curve_offset_loss: `0.004198`
- val_curve_amplitude_loss: `0.051185`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.028955`
- val_base_rmse: `0.033602`
- val_residual_offset_mean_abs: `0.017020`

## Test Metrics

- test_loss: `0.007912`
- test_mae: `0.003563`
- test_rmse: `0.004400`
- test_pointwise_loss: `0.004608`
- test_centered_curve_shape_loss: `0.004134`
- test_curve_offset_loss: `0.005081`
- test_curve_amplitude_loss: `0.029237`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.031005`
- test_base_rmse: `0.035393`
- test_residual_offset_mean_abs: `0.018205`

## Interpretation

The held-out val error stayed finite with MAE=0.003719 deg and RMSE=0.004630 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003563 deg and RMSE=0.004400 deg, which indicates a numerically stable baseline run.
