# Wave4 4 Gru Latent Offset Residual Fw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values`
- Model Family: `wave4_4_gru_latent_offset_residual_fw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-18-51-23__te_wave4_4_gru_latent_offset_residual_fw__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=113-val_mae=0.00224746.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005691`
- val_mae: `0.002247`
- val_rmse: `0.003099`
- val_pointwise_loss: `0.003043`
- val_centered_curve_shape_loss: `0.005703`
- val_curve_offset_loss: `0.000390`
- val_curve_amplitude_loss: `0.028593`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.024965`
- val_base_rmse: `0.029755`
- val_residual_offset_mean_abs: `0.015084`

## Test Metrics

- test_loss: `0.006339`
- test_mae: `0.002363`
- test_rmse: `0.003419`
- test_pointwise_loss: `0.003432`
- test_centered_curve_shape_loss: `0.006446`
- test_curve_offset_loss: `0.000422`
- test_curve_amplitude_loss: `0.030663`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.023697`
- test_base_rmse: `0.028590`
- test_residual_offset_mean_abs: `0.014166`

## Interpretation

The held-out val error stayed finite with MAE=0.002247 deg and RMSE=0.003099 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002363 deg and RMSE=0.003419 deg, which indicates a numerically stable baseline run.
