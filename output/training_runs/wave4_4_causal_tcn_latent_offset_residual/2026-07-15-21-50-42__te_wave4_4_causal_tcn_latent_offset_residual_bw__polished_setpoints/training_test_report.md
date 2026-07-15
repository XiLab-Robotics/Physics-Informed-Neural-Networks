# Wave4 4 Causal Tcn Latent Offset Residual Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_setpoints`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-21-50-42__te_wave4_4_causal_tcn_latent_offset_residual_bw__polished_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=074-val_mae=0.00224017.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005904`
- val_mae: `0.002240`
- val_rmse: `0.003077`
- val_pointwise_loss: `0.003025`
- val_centered_curve_shape_loss: `0.005568`
- val_curve_offset_loss: `0.000486`
- val_curve_amplitude_loss: `0.033364`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.031514`
- val_base_rmse: `0.035802`
- val_residual_offset_mean_abs: `0.018691`

## Test Metrics

- test_loss: `0.008337`
- test_mae: `0.002527`
- test_rmse: `0.003882`
- test_pointwise_loss: `0.004567`
- test_centered_curve_shape_loss: `0.006425`
- test_curve_offset_loss: `0.002841`
- test_curve_amplitude_loss: `0.038332`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.029696`
- test_base_rmse: `0.034298`
- test_residual_offset_mean_abs: `0.017363`

## Interpretation

The held-out val error stayed finite with MAE=0.002240 deg and RMSE=0.003077 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002527 deg and RMSE=0.003882 deg, which indicates a numerically stable baseline run.
