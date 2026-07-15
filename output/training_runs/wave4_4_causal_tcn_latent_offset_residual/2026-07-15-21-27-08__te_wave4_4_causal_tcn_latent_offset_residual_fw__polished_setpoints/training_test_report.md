# Wave4 4 Causal Tcn Latent Offset Residual Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_setpoints`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-21-27-08__te_wave4_4_causal_tcn_latent_offset_residual_fw__polished_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=107-val_mae=0.00221473.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005933`
- val_mae: `0.002215`
- val_rmse: `0.003047`
- val_pointwise_loss: `0.002979`
- val_centered_curve_shape_loss: `0.005456`
- val_curve_offset_loss: `0.000506`
- val_curve_amplitude_loss: `0.035225`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.030894`
- val_base_rmse: `0.034586`
- val_residual_offset_mean_abs: `0.016433`

## Test Metrics

- test_loss: `0.008331`
- test_mae: `0.002513`
- test_rmse: `0.003854`
- test_pointwise_loss: `0.004471`
- test_centered_curve_shape_loss: `0.006313`
- test_curve_offset_loss: `0.002727`
- test_curve_amplitude_loss: `0.041046`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.029135`
- test_base_rmse: `0.033116`
- test_residual_offset_mean_abs: `0.015374`

## Interpretation

The held-out val error stayed finite with MAE=0.002215 deg and RMSE=0.003047 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002513 deg and RMSE=0.003854 deg, which indicates a numerically stable baseline run.
