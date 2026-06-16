# Track2H Latent State Hysteresis Causal Tcn Offset Residual Global Training And Testing Report

## Overview

- Run Name: `te_track2h_l_causal_tcn_offset_residual_global`
- Model Family: `track2h_latent_state_hysteresis_causal_tcn_offset_residual_global`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_causal_tcn_offset_residual_global\2026-06-16-18-48-13__te_track2h_l_causal_tcn_offset_residual_global\checkpoints\latent_state_hysteresis_probe-epoch=152-val_mae=0.00354330.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010240`
- val_mae: `0.003543`
- val_rmse: `0.004146`
- val_pointwise_loss: `0.005744`
- val_centered_curve_shape_loss: `0.007424`
- val_curve_offset_loss: `0.004070`
- val_curve_amplitude_loss: `0.043937`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.026073`
- val_base_rmse: `0.027703`
- val_residual_offset_mean_abs: `0.016083`

## Test Metrics

- test_loss: `0.007345`
- test_mae: `0.003368`
- test_rmse: `0.003860`
- test_pointwise_loss: `0.004304`
- test_centered_curve_shape_loss: `0.004127`
- test_curve_offset_loss: `0.004480`
- test_curve_amplitude_loss: `0.026394`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.027244`
- test_base_rmse: `0.028768`
- test_residual_offset_mean_abs: `0.016717`

## Interpretation

The held-out val error stayed finite with MAE=0.003543 deg and RMSE=0.004146 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003368 deg and RMSE=0.003860 deg, which indicates a numerically stable baseline run.
