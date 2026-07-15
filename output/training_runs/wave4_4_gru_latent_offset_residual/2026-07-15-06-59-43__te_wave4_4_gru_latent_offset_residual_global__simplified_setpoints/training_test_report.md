# Wave4 4 Gru Latent Offset Residual Global Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints`
- Model Family: `wave4_4_gru_latent_offset_residual_global`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-06-59-43__te_wave4_4_gru_latent_offset_residual_global__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=065-val_mae=0.00375664.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010314`
- val_mae: `0.003757`
- val_rmse: `0.004669`
- val_pointwise_loss: `0.005912`
- val_centered_curve_shape_loss: `0.007454`
- val_curve_offset_loss: `0.004379`
- val_curve_amplitude_loss: `0.040712`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.029187`
- val_base_rmse: `0.033588`
- val_residual_offset_mean_abs: `0.012161`

## Test Metrics

- test_loss: `0.007470`
- test_mae: `0.003535`
- test_rmse: `0.004351`
- test_pointwise_loss: `0.004523`
- test_centered_curve_shape_loss: `0.004120`
- test_curve_offset_loss: `0.004926`
- test_curve_amplitude_loss: `0.022753`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.031001`
- test_base_rmse: `0.035148`
- test_residual_offset_mean_abs: `0.012782`

## Interpretation

The held-out val error stayed finite with MAE=0.003757 deg and RMSE=0.004669 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003535 deg and RMSE=0.004351 deg, which indicates a numerically stable baseline run.
