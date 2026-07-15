# Wave4 4 Causal Tcn Latent Offset Residual Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-14-26__te_wave4_4_causal_tcn_latent_offset_residual_fw__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=236-val_mae=0.00349844.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.009919`
- val_mae: `0.003498`
- val_rmse: `0.004468`
- val_pointwise_loss: `0.005615`
- val_centered_curve_shape_loss: `0.007457`
- val_curve_offset_loss: `0.003783`
- val_curve_amplitude_loss: `0.041116`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.027792`
- val_base_rmse: `0.031413`
- val_residual_offset_mean_abs: `0.015822`

## Test Metrics

- test_loss: `0.007280`
- test_mae: `0.003343`
- test_rmse: `0.004238`
- test_pointwise_loss: `0.004324`
- test_centered_curve_shape_loss: `0.004124`
- test_curve_offset_loss: `0.004526`
- test_curve_amplitude_loss: `0.024517`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.029531`
- test_base_rmse: `0.033048`
- test_residual_offset_mean_abs: `0.016631`

## Interpretation

The held-out val error stayed finite with MAE=0.003498 deg and RMSE=0.004468 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003343 deg and RMSE=0.004238 deg, which indicates a numerically stable baseline run.
