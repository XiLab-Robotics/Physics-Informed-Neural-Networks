# Track2H Latent State Hysteresis Causal Tcn Offset Residual Bw Training And Testing Report

## Overview

- Run Name: `te_track2h_l_causal_tcn_offset_residual_bw`
- Model Family: `track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_causal_tcn_offset_residual_bw\2026-06-16-19-22-13__te_track2h_l_causal_tcn_offset_residual_bw\checkpoints\latent_state_hysteresis_probe-epoch=100-val_mae=0.00384011.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.040695`
- val_mae: `0.003840`
- val_rmse: `0.004554`
- val_pointwise_loss: `0.023292`
- val_centered_curve_shape_loss: `0.034494`
- val_curve_offset_loss: `0.013753`
- val_curve_amplitude_loss: `0.155068`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.007893`
- val_base_rmse: `0.009658`
- val_residual_offset_mean_abs: `0.002550`

## Test Metrics

- test_loss: `0.028079`
- test_mae: `0.003630`
- test_rmse: `0.004312`
- test_pointwise_loss: `0.017540`
- test_centered_curve_shape_loss: `0.018235`
- test_curve_offset_loss: `0.017228`
- test_curve_amplitude_loss: `0.068938`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.007786`
- test_base_rmse: `0.009468`
- test_residual_offset_mean_abs: `0.002552`

## Interpretation

The held-out val error stayed finite with MAE=0.003840 deg and RMSE=0.004554 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003630 deg and RMSE=0.004312 deg, which indicates a numerically stable baseline run.
