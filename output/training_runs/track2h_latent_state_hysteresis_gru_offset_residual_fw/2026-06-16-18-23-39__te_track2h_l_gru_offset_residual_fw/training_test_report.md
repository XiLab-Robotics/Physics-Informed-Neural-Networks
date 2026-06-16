# Track2H Latent State Hysteresis Gru Offset Residual Fw Training And Testing Report

## Overview

- Run Name: `te_track2h_l_gru_offset_residual_fw`
- Model Family: `track2h_latent_state_hysteresis_gru_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_gru_offset_residual_fw\2026-06-16-18-23-39__te_track2h_l_gru_offset_residual_fw\checkpoints\latent_state_hysteresis_probe-epoch=109-val_mae=0.00346843.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.030553`
- val_mae: `0.003468`
- val_rmse: `0.004100`
- val_pointwise_loss: `0.018109`
- val_centered_curve_shape_loss: `0.020389`
- val_curve_offset_loss: `0.015945`
- val_curve_amplitude_loss: `0.103539`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.011322`
- val_base_rmse: `0.013785`
- val_residual_offset_mean_abs: `0.005727`

## Test Metrics

- test_loss: `0.026621`
- test_mae: `0.003537`
- test_rmse: `0.004110`
- test_pointwise_loss: `0.016699`
- test_centered_curve_shape_loss: `0.012421`
- test_curve_offset_loss: `0.020982`
- test_curve_amplitude_loss: `0.064840`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.011132`
- test_base_rmse: `0.013584`
- test_residual_offset_mean_abs: `0.006108`

## Interpretation

The held-out val error stayed finite with MAE=0.003468 deg and RMSE=0.004100 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003537 deg and RMSE=0.004110 deg, which indicates a numerically stable baseline run.
