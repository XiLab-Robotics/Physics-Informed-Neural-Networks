# Wave4 4 Gru Latent Offset Residual Global Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_global__polished_actual_values`
- Model Family: `wave4_4_gru_latent_offset_residual_global`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-05-18__te_wave4_4_gru_latent_offset_residual_global__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=208-val_mae=0.00217281.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005002`
- val_mae: `0.002173`
- val_rmse: `0.003019`
- val_pointwise_loss: `0.002957`
- val_centered_curve_shape_loss: `0.005595`
- val_curve_offset_loss: `0.000329`
- val_curve_amplitude_loss: `0.017218`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.025695`
- val_base_rmse: `0.030140`
- val_residual_offset_mean_abs: `0.015445`

## Test Metrics

- test_loss: `0.005771`
- test_mae: `0.002271`
- test_rmse: `0.003341`
- test_pointwise_loss: `0.003322`
- test_centered_curve_shape_loss: `0.006273`
- test_curve_offset_loss: `0.000377`
- test_curve_amplitude_loss: `0.022368`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.024107`
- test_base_rmse: `0.028781`
- test_residual_offset_mean_abs: `0.014283`

## Interpretation

The held-out val error stayed finite with MAE=0.002173 deg and RMSE=0.003019 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002271 deg and RMSE=0.003341 deg, which indicates a numerically stable baseline run.
