# Wave4 4 Gru Latent Offset Residual Global Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_global`
- Model Family: `wave4_4_gru_latent_offset_residual_global`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-01-19-49-54__te_wave4_4_gru_latent_offset_residual_global\checkpoints\latent_state_hysteresis_probe-epoch=171-val_mae=0.00219533.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005551`
- val_mae: `0.002195`
- val_rmse: `0.002734`
- val_pointwise_loss: `0.002957`
- val_centered_curve_shape_loss: `0.005543`
- val_curve_offset_loss: `0.000376`
- val_curve_amplitude_loss: `0.028197`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.022562`
- val_base_rmse: `0.025994`
- val_residual_offset_mean_abs: `0.009945`

## Test Metrics

- test_loss: `0.006349`
- test_mae: `0.002287`
- test_rmse: `0.002934`
- test_pointwise_loss: `0.003297`
- test_centered_curve_shape_loss: `0.006188`
- test_curve_offset_loss: `0.000405`
- test_curve_amplitude_loss: `0.034671`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.021452`
- test_base_rmse: `0.025136`
- test_residual_offset_mean_abs: `0.009685`

## Interpretation

The held-out val error stayed finite with MAE=0.002195 deg and RMSE=0.002734 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002287 deg and RMSE=0.002934 deg, which indicates a numerically stable baseline run.
