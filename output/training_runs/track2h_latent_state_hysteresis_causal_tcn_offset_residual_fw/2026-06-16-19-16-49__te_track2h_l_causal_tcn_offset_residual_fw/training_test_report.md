# Track2H Latent State Hysteresis Causal Tcn Offset Residual Fw Training And Testing Report

## Overview

- Run Name: `te_track2h_l_causal_tcn_offset_residual_fw`
- Model Family: `track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_causal_tcn_offset_residual_fw\2026-06-16-19-16-49__te_track2h_l_causal_tcn_offset_residual_fw\checkpoints\latent_state_hysteresis_probe-epoch=037-val_mae=0.00356529.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.031434`
- val_mae: `0.003565`
- val_rmse: `0.004217`
- val_pointwise_loss: `0.019106`
- val_centered_curve_shape_loss: `0.020640`
- val_curve_offset_loss: `0.017650`
- val_curve_amplitude_loss: `0.093403`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.010456`
- val_base_rmse: `0.012699`
- val_residual_offset_mean_abs: `0.005745`

## Test Metrics

- test_loss: `0.025296`
- test_mae: `0.003470`
- test_rmse: `0.004068`
- test_pointwise_loss: `0.016221`
- test_centered_curve_shape_loss: `0.012906`
- test_curve_offset_loss: `0.019541`
- test_curve_amplitude_loss: `0.051712`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.010384`
- test_base_rmse: `0.012664`
- test_residual_offset_mean_abs: `0.005807`

## Interpretation

The held-out val error stayed finite with MAE=0.003565 deg and RMSE=0.004217 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003470 deg and RMSE=0.004068 deg, which indicates a numerically stable baseline run.
