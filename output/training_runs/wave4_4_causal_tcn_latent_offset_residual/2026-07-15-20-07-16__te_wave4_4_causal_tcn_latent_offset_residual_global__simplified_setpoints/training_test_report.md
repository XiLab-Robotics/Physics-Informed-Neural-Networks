# Wave4 4 Causal Tcn Latent Offset Residual Global Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_global`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_causal_tcn_latent_offset_residual/2026-07-15-20-07-16__te_wave4_4_causal_tcn_latent_offset_residual_global__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=055-val_mae=0.00376625.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010780`
- val_mae: `0.003766`
- val_rmse: `0.004704`
- val_pointwise_loss: `0.006031`
- val_centered_curve_shape_loss: `0.007475`
- val_curve_offset_loss: `0.004595`
- val_curve_amplitude_loss: `0.046697`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.032746`
- val_base_rmse: `0.037307`
- val_residual_offset_mean_abs: `0.013190`

## Test Metrics

- test_loss: `0.007882`
- test_mae: `0.003548`
- test_rmse: `0.004384`
- test_pointwise_loss: `0.004598`
- test_centered_curve_shape_loss: `0.004152`
- test_curve_offset_loss: `0.005045`
- test_curve_amplitude_loss: `0.028890`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.034811`
- test_base_rmse: `0.039127`
- test_residual_offset_mean_abs: `0.014057`

## Interpretation

The held-out val error stayed finite with MAE=0.003766 deg and RMSE=0.004704 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003548 deg and RMSE=0.004384 deg, which indicates a numerically stable baseline run.
