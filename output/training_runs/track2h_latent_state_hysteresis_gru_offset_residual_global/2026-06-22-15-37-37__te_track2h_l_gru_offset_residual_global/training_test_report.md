# Track2H Latent State Hysteresis Gru Offset Residual Global Training And Testing Report

## Overview

- Run Name: `te_track2h_l_gru_offset_residual_global`
- Model Family: `track2h_latent_state_hysteresis_gru_offset_residual_global`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_gru_offset_residual_global\2026-06-22-15-37-37__te_track2h_l_gru_offset_residual_global\checkpoints\latent_state_hysteresis_probe-epoch=101-val_mae=0.00223219.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005360`
- val_mae: `0.002232`
- val_rmse: `0.002762`
- val_pointwise_loss: `0.002994`
- val_centered_curve_shape_loss: `0.005592`
- val_curve_offset_loss: `0.000401`
- val_curve_amplitude_loss: `0.023346`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.022519`
- val_base_rmse: `0.025935`
- val_residual_offset_mean_abs: `0.009264`

## Test Metrics

- test_loss: `0.006120`
- test_mae: `0.002339`
- test_rmse: `0.002986`
- test_pointwise_loss: `0.003369`
- test_centered_curve_shape_loss: `0.006287`
- test_curve_offset_loss: `0.000452`
- test_curve_amplitude_loss: `0.028058`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.021381`
- test_base_rmse: `0.024958`
- test_residual_offset_mean_abs: `0.008927`

## Interpretation

The held-out val error stayed finite with MAE=0.002232 deg and RMSE=0.002762 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002339 deg and RMSE=0.002986 deg, which indicates a numerically stable baseline run.
