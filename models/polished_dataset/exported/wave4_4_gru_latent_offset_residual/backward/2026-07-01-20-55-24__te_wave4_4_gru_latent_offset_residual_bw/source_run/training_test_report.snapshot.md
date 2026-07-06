# Wave4 4 Gru Latent Offset Residual Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_bw`
- Model Family: `wave4_4_gru_latent_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-01-20-55-24__te_wave4_4_gru_latent_offset_residual_bw\checkpoints\latent_state_hysteresis_probe-epoch=173-val_mae=0.00219051.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005246`
- val_mae: `0.002191`
- val_rmse: `0.002724`
- val_pointwise_loss: `0.002995`
- val_centered_curve_shape_loss: `0.005629`
- val_curve_offset_loss: `0.000370`
- val_curve_amplitude_loss: `0.021013`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.026715`
- val_base_rmse: `0.028861`
- val_residual_offset_mean_abs: `0.009720`

## Test Metrics

- test_loss: `0.005892`
- test_mae: `0.002260`
- test_rmse: `0.002915`
- test_pointwise_loss: `0.003305`
- test_centered_curve_shape_loss: `0.006317`
- test_curve_offset_loss: `0.000299`
- test_curve_amplitude_loss: `0.025279`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.025723`
- test_base_rmse: `0.028136`
- test_residual_offset_mean_abs: `0.009402`

## Interpretation

The held-out val error stayed finite with MAE=0.002191 deg and RMSE=0.002724 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002260 deg and RMSE=0.002915 deg, which indicates a numerically stable baseline run.
