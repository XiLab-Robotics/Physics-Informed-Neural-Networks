# Wave4 4 Gru Latent Offset Residual Global Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_global__polished_setpoints`
- Model Family: `wave4_4_gru_latent_offset_residual_global`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-16-39-39__te_wave4_4_gru_latent_offset_residual_global__polished_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=100-val_mae=0.00222289.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005896`
- val_mae: `0.002223`
- val_rmse: `0.003070`
- val_pointwise_loss: `0.003010`
- val_centered_curve_shape_loss: `0.005584`
- val_curve_offset_loss: `0.000442`
- val_curve_amplitude_loss: `0.033613`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.029076`
- val_base_rmse: `0.033062`
- val_residual_offset_mean_abs: `0.014143`

## Test Metrics

- test_loss: `0.008416`
- test_mae: `0.002534`
- test_rmse: `0.003918`
- test_pointwise_loss: `0.004625`
- test_centered_curve_shape_loss: `0.006428`
- test_curve_offset_loss: `0.002962`
- test_curve_amplitude_loss: `0.038260`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.027409`
- test_base_rmse: `0.031696`
- test_residual_offset_mean_abs: `0.013383`

## Interpretation

The held-out val error stayed finite with MAE=0.002223 deg and RMSE=0.003070 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002534 deg and RMSE=0.003918 deg, which indicates a numerically stable baseline run.
