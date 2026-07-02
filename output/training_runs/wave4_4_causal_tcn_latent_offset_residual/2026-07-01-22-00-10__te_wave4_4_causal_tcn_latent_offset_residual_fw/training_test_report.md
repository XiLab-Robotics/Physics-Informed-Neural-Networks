# Wave4 4 Causal Tcn Latent Offset Residual Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_causal_tcn_latent_offset_residual_fw`
- Model Family: `wave4_4_causal_tcn_latent_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_causal_tcn_latent_offset_residual\2026-07-01-22-00-10__te_wave4_4_causal_tcn_latent_offset_residual_fw\checkpoints\latent_state_hysteresis_probe-epoch=105-val_mae=0.00222384.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005581`
- val_mae: `0.002224`
- val_rmse: `0.002766`
- val_pointwise_loss: `0.003008`
- val_centered_curve_shape_loss: `0.005647`
- val_curve_offset_loss: `0.000374`
- val_curve_amplitude_loss: `0.027368`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.021251`
- val_base_rmse: `0.024418`
- val_residual_offset_mean_abs: `0.010708`

## Test Metrics

- test_loss: `0.006205`
- test_mae: `0.002316`
- test_rmse: `0.002980`
- test_pointwise_loss: `0.003433`
- test_centered_curve_shape_loss: `0.006524`
- test_curve_offset_loss: `0.000342`
- test_curve_amplitude_loss: `0.027972`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.020324`
- test_base_rmse: `0.023772`
- test_residual_offset_mean_abs: `0.010259`

## Interpretation

The held-out val error stayed finite with MAE=0.002224 deg and RMSE=0.002766 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002316 deg and RMSE=0.002980 deg, which indicates a numerically stable baseline run.
