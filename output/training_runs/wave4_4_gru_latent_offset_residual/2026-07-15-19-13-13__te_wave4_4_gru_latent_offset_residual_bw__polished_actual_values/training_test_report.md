# Wave4 4 Gru Latent Offset Residual Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values`
- Model Family: `wave4_4_gru_latent_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-19-13-13__te_wave4_4_gru_latent_offset_residual_bw__polished_actual_values/checkpoints/latent_state_hysteresis_probe-epoch=140-val_mae=0.00222826.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005421`
- val_mae: `0.002228`
- val_rmse: `0.003068`
- val_pointwise_loss: `0.003006`
- val_centered_curve_shape_loss: `0.005613`
- val_curve_offset_loss: `0.000408`
- val_curve_amplitude_loss: `0.024203`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.024037`
- val_base_rmse: `0.028687`
- val_residual_offset_mean_abs: `0.010977`

## Test Metrics

- test_loss: `0.006064`
- test_mae: `0.002328`
- test_rmse: `0.003372`
- test_pointwise_loss: `0.003365`
- test_centered_curve_shape_loss: `0.006350`
- test_curve_offset_loss: `0.000385`
- test_curve_amplitude_loss: `0.027040`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.022779`
- test_base_rmse: `0.027577`
- test_residual_offset_mean_abs: `0.010478`

## Interpretation

The held-out val error stayed finite with MAE=0.002228 deg and RMSE=0.003068 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002328 deg and RMSE=0.003372 deg, which indicates a numerically stable baseline run.
