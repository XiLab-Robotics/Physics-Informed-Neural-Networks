# Track2H Latent State Hysteresis Gru Offset Residual Bw Training And Testing Report

## Overview

- Run Name: `te_track2h_l_gru_offset_residual_bw`
- Model Family: `track2h_latent_state_hysteresis_gru_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\track2h_latent_state_hysteresis_gru_offset_residual_bw\2026-06-16-18-34-12__te_track2h_l_gru_offset_residual_bw\checkpoints\latent_state_hysteresis_probe-epoch=149-val_mae=0.00383662.ckpt`

## Dataset Split

- Train Curves: `678`
- Validation Curves: `194`
- Test Curves: `97`

## Validation Metrics

- val_loss: `0.044734`
- val_mae: `0.003837`
- val_rmse: `0.004516`
- val_pointwise_loss: `0.022715`
- val_centered_curve_shape_loss: `0.033084`
- val_curve_offset_loss: `0.013765`
- val_curve_amplitude_loss: `0.252966`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.012299`
- val_base_rmse: `0.014906`
- val_residual_offset_mean_abs: `0.005650`

## Test Metrics

- test_loss: `0.029507`
- test_mae: `0.003545`
- test_rmse: `0.004175`
- test_pointwise_loss: `0.016700`
- test_centered_curve_shape_loss: `0.017358`
- test_curve_offset_loss: `0.016253`
- test_curve_amplitude_loss: `0.121695`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.012547`
- test_base_rmse: `0.015114`
- test_residual_offset_mean_abs: `0.005791`

## Interpretation

The held-out val error stayed finite with MAE=0.003837 deg and RMSE=0.004516 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003545 deg and RMSE=0.004175 deg, which indicates a numerically stable baseline run.
