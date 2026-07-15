# Wave4 4 Causal Tcn Latent Offset Residual Global Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_global`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-22-27-43__te_wave4_4_causal_tcn_latent_offset_residual_global__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=041-val_mae=0.00230429.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006129`
- val_mae: `0.002304`
- val_rmse: `0.003196`
- val_pointwise_loss: `0.003252`
- val_centered_curve_shape_loss: `0.005992`
- val_curve_offset_loss: `0.000531`
- val_curve_amplitude_loss: `0.031463`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.026747`
- val_base_rmse: `0.031537`
- val_residual_offset_mean_abs: `0.014569`

## Test Metrics

- test_loss: `0.006744`
- test_mae: `0.002420`
- test_rmse: `0.003542`
- test_pointwise_loss: `0.003666`
- test_centered_curve_shape_loss: `0.006759`
- test_curve_offset_loss: `0.000593`
- test_curve_amplitude_loss: `0.032160`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.025337`
- test_base_rmse: `0.030284`
- test_residual_offset_mean_abs: `0.013746`

## Interpretation

The held-out val error stayed finite with MAE=0.002304 deg and RMSE=0.003196 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002420 deg and RMSE=0.003542 deg, which indicates a numerically stable baseline run.
