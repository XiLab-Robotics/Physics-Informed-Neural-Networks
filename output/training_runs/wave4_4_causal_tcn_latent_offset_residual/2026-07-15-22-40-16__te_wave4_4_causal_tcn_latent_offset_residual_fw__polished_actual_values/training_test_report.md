# Wave4 4 Causal Tcn Latent Offset Residual Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-40-16__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=038-val_mae=0.00225416.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005912`
- val_mae: `0.002254`
- val_rmse: `0.003097`
- val_pointwise_loss: `0.003042`
- val_centered_curve_shape_loss: `0.005659`
- val_curve_offset_loss: `0.000430`
- val_curve_amplitude_loss: `0.033027`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.028455`
- val_base_rmse: `0.033375`
- val_residual_offset_mean_abs: `0.014403`

## Test Metrics

- test_loss: `0.006609`
- test_mae: `0.002372`
- test_rmse: `0.003458`
- test_pointwise_loss: `0.003500`
- test_centered_curve_shape_loss: `0.006544`
- test_curve_offset_loss: `0.000457`
- test_curve_amplitude_loss: `0.034166`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.026856`
- test_base_rmse: `0.031971`
- test_residual_offset_mean_abs: `0.013821`

## Interpretation

The held-out val error stayed finite with MAE=0.002254 deg and RMSE=0.003097 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002372 deg and RMSE=0.003458 deg, which indicates a numerically stable baseline run.
