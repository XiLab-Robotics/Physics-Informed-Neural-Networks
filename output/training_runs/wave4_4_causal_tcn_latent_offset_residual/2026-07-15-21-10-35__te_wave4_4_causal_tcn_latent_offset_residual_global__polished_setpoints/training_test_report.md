# Wave4 4 Causal Tcn Latent Offset Residual Global Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_global__polished_setpoints`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_global`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-21-10-35__te_wave4_4_causal_tcn_latent_offset_residual_global__polished_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=060-val_mae=0.00222789.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006066`
- val_mae: `0.002228`
- val_rmse: `0.003083`
- val_pointwise_loss: `0.003003`
- val_centered_curve_shape_loss: `0.005480`
- val_curve_offset_loss: `0.000531`
- val_curve_amplitude_loss: `0.037206`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.032758`
- val_base_rmse: `0.037101`
- val_residual_offset_mean_abs: `0.013845`

## Test Metrics

- test_loss: `0.008427`
- test_mae: `0.002515`
- test_rmse: `0.003880`
- test_pointwise_loss: `0.004525`
- test_centered_curve_shape_loss: `0.006352`
- test_curve_offset_loss: `0.002825`
- test_curve_amplitude_loss: `0.041348`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.030868`
- test_base_rmse: `0.035471`
- test_residual_offset_mean_abs: `0.013195`

## Interpretation

The held-out val error stayed finite with MAE=0.002228 deg and RMSE=0.003083 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002515 deg and RMSE=0.003880 deg, which indicates a numerically stable baseline run.
