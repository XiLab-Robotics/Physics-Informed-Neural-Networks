# Wave4 4 Causal Tcn Latent Offset Residual Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_bw`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-01-22-28-39__te_wave4_4_causal_tcn_latent_offset_residual_bw\checkpoints\latent_state_hysteresis_probe-epoch=154-val_mae=0.00220405.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005554`
- val_mae: `0.002204`
- val_rmse: `0.002741`
- val_pointwise_loss: `0.002981`
- val_centered_curve_shape_loss: `0.005602`
- val_curve_offset_loss: `0.000364`
- val_curve_amplitude_loss: `0.027600`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.027200`
- val_base_rmse: `0.029262`
- val_residual_offset_mean_abs: `0.009845`

## Test Metrics

- test_loss: `0.006241`
- test_mae: `0.002309`
- test_rmse: `0.002974`
- test_pointwise_loss: `0.003406`
- test_centered_curve_shape_loss: `0.006404`
- test_curve_offset_loss: `0.000407`
- test_curve_amplitude_loss: `0.029461`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.025880`
- test_base_rmse: `0.028281`
- test_residual_offset_mean_abs: `0.009465`

## Interpretation

The held-out val error stayed finite with MAE=0.002204 deg and RMSE=0.002741 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002309 deg and RMSE=0.002974 deg, which indicates a numerically stable baseline run.
