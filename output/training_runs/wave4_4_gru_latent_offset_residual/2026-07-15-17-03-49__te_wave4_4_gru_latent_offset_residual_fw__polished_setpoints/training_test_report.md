# Wave4 4 Gru Latent Offset Residual Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints`
- Model Family: `wave4_4_gru_latent_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-03-49__te_wave4_4_gru_latent_offset_residual_fw__polished_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=164-val_mae=0.00221821.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005566`
- val_mae: `0.002218`
- val_rmse: `0.003040`
- val_pointwise_loss: `0.002992`
- val_centered_curve_shape_loss: `0.005531`
- val_curve_offset_loss: `0.000461`
- val_curve_amplitude_loss: `0.027510`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.027557`
- val_base_rmse: `0.031367`
- val_residual_offset_mean_abs: `0.015281`

## Test Metrics

- test_loss: `0.007817`
- test_mae: `0.002488`
- test_rmse: `0.003826`
- test_pointwise_loss: `0.004438`
- test_centered_curve_shape_loss: `0.006400`
- test_curve_offset_loss: `0.002589`
- test_curve_amplitude_loss: `0.031621`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.026085`
- test_base_rmse: `0.030144`
- test_residual_offset_mean_abs: `0.014358`

## Interpretation

The held-out val error stayed finite with MAE=0.002218 deg and RMSE=0.003040 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002488 deg and RMSE=0.003826 deg, which indicates a numerically stable baseline run.
