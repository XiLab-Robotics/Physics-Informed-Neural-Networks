# Wave4 4 Causal Tcn Latent Offset Residual Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-38-50__te_wave4_4_causal_tcn_latent_offset_residual_bw__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=105-val_mae=0.00370934.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010990`
- val_mae: `0.003709`
- val_rmse: `0.004649`
- val_pointwise_loss: `0.005905`
- val_centered_curve_shape_loss: `0.007338`
- val_curve_offset_loss: `0.004479`
- val_curve_amplitude_loss: `0.054418`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.031471`
- val_base_rmse: `0.035653`
- val_residual_offset_mean_abs: `0.017812`

## Test Metrics

- test_loss: `0.007938`
- test_mae: `0.003555`
- test_rmse: `0.004415`
- test_pointwise_loss: `0.004664`
- test_centered_curve_shape_loss: `0.004086`
- test_curve_offset_loss: `0.005242`
- test_curve_amplitude_loss: `0.028184`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.033322`
- test_base_rmse: `0.037339`
- test_residual_offset_mean_abs: `0.018754`

## Interpretation

The held-out val error stayed finite with MAE=0.003709 deg and RMSE=0.004649 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003555 deg and RMSE=0.004415 deg, which indicates a numerically stable baseline run.
