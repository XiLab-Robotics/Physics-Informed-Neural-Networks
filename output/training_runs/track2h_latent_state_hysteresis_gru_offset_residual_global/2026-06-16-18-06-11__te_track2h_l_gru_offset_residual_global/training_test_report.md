# Track2H Latent State Hysteresis Gru Offset Residual Global Training And Testing Report

## Overview

- Run Name: `te_track2h_l_gru_offset_residual_global`
- Model Family: `track2h_latent_state_hysteresis_gru_offset_residual_global`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_gru_offset_residual_global\2026-06-16-18-06-11__te_track2h_l_gru_offset_residual_global\checkpoints\latent_state_hysteresis_probe-epoch=064-val_mae=0.00371717.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010948`
- val_mae: `0.003717`
- val_rmse: `0.004313`
- val_pointwise_loss: `0.005833`
- val_centered_curve_shape_loss: `0.007329`
- val_curve_offset_loss: `0.004345`
- val_curve_amplitude_loss: `0.055604`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.022478`
- val_base_rmse: `0.024798`
- val_residual_offset_mean_abs: `0.006764`

## Test Metrics

- test_loss: `0.008155`
- test_mae: `0.003590`
- test_rmse: `0.004074`
- test_pointwise_loss: `0.004650`
- test_centered_curve_shape_loss: `0.004048`
- test_curve_offset_loss: `0.005253`
- test_curve_amplitude_loss: `0.032881`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.023524`
- test_base_rmse: `0.025652`
- test_residual_offset_mean_abs: `0.006914`

## Interpretation

The held-out val error stayed finite with MAE=0.003717 deg and RMSE=0.004313 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003590 deg and RMSE=0.004074 deg, which indicates a numerically stable baseline run.
