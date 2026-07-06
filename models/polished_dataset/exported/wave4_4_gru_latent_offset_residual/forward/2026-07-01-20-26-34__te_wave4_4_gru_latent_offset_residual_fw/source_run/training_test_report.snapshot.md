# Wave4 4 Gru Latent Offset Residual Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_fw`
- Model Family: `wave4_4_gru_latent_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave4_4_gru_latent_offset_residual\2026-07-01-20-26-34__te_wave4_4_gru_latent_offset_residual_fw\checkpoints\latent_state_hysteresis_probe-epoch=128-val_mae=0.00220084.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005309`
- val_mae: `0.002201`
- val_rmse: `0.002738`
- val_pointwise_loss: `0.002990`
- val_centered_curve_shape_loss: `0.005609`
- val_curve_offset_loss: `0.000376`
- val_curve_amplitude_loss: `0.022451`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.026849`
- val_base_rmse: `0.029212`
- val_residual_offset_mean_abs: `0.018429`

## Test Metrics

- test_loss: `0.006073`
- test_mae: `0.002300`
- test_rmse: `0.002953`
- test_pointwise_loss: `0.003356`
- test_centered_curve_shape_loss: `0.006307`
- test_curve_offset_loss: `0.000407`
- test_curve_amplitude_loss: `0.027464`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.025641`
- test_base_rmse: `0.028300`
- test_residual_offset_mean_abs: `0.018046`

## Interpretation

The held-out val error stayed finite with MAE=0.002201 deg and RMSE=0.002738 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002300 deg and RMSE=0.002953 deg, which indicates a numerically stable baseline run.
