# Wave4 4 Causal Tcn Latent Offset Residual Global Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_global`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_global`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-01-21-33-27__te_wave4_4_causal_tcn_latent_offset_residual_global\checkpoints\latent_state_hysteresis_probe-epoch=135-val_mae=0.00221664.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005642`
- val_mae: `0.002217`
- val_rmse: `0.002758`
- val_pointwise_loss: `0.003022`
- val_centered_curve_shape_loss: `0.005615`
- val_curve_offset_loss: `0.000434`
- val_curve_amplitude_loss: `0.028186`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.026389`
- val_base_rmse: `0.028727`
- val_residual_offset_mean_abs: `0.017743`

## Test Metrics

- test_loss: `0.006372`
- test_mae: `0.002315`
- test_rmse: `0.002986`
- test_pointwise_loss: `0.003448`
- test_centered_curve_shape_loss: `0.006453`
- test_curve_offset_loss: `0.000445`
- test_curve_amplitude_loss: `0.030888`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.025578`
- test_base_rmse: `0.028088`
- test_residual_offset_mean_abs: `0.017283`

## Interpretation

The held-out val error stayed finite with MAE=0.002217 deg and RMSE=0.002758 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002315 deg and RMSE=0.002986 deg, which indicates a numerically stable baseline run.
