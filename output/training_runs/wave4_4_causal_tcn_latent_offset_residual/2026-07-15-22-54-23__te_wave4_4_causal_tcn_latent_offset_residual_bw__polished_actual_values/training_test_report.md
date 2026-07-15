# Wave4 4 Causal Tcn Latent Offset Residual Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-54-23__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=078-val_mae=0.00222665.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005754`
- val_mae: `0.002227`
- val_rmse: `0.003064`
- val_pointwise_loss: `0.002993`
- val_centered_curve_shape_loss: `0.005629`
- val_curve_offset_loss: `0.000360`
- val_curve_amplitude_loss: `0.031278`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.024712`
- val_base_rmse: `0.029248`
- val_residual_offset_mean_abs: `0.016449`

## Test Metrics

- test_loss: `0.006453`
- test_mae: `0.002344`
- test_rmse: `0.003435`
- test_pointwise_loss: `0.003435`
- test_centered_curve_shape_loss: `0.006509`
- test_curve_offset_loss: `0.000361`
- test_curve_amplitude_loss: `0.032889`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.023445`
- test_base_rmse: `0.028187`
- test_residual_offset_mean_abs: `0.015388`

## Interpretation

The held-out val error stayed finite with MAE=0.002227 deg and RMSE=0.003064 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002344 deg and RMSE=0.003435 deg, which indicates a numerically stable baseline run.
