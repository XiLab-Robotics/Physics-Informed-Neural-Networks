# Wave4 4 Gru Latent Offset Residual Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints`
- Model Family: `wave4_4_gru_latent_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-07-26-38__te_wave4_4_gru_latent_offset_residual_bw__simplified_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=072-val_mae=0.00377245.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.010391`
- val_mae: `0.003772`
- val_rmse: `0.004677`
- val_pointwise_loss: `0.005916`
- val_centered_curve_shape_loss: `0.007638`
- val_curve_offset_loss: `0.004200`
- val_curve_amplitude_loss: `0.042140`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.028252`
- val_base_rmse: `0.032753`
- val_residual_offset_mean_abs: `0.016543`

## Test Metrics

- test_loss: `0.007532`
- test_mae: `0.003510`
- test_rmse: `0.004334`
- test_pointwise_loss: `0.004487`
- test_centered_curve_shape_loss: `0.004287`
- test_curve_offset_loss: `0.004688`
- test_curve_amplitude_loss: `0.024992`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.030086`
- test_base_rmse: `0.034366`
- test_residual_offset_mean_abs: `0.017673`

## Interpretation

The held-out val error stayed finite with MAE=0.003772 deg and RMSE=0.004677 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.003510 deg and RMSE=0.004334 deg, which indicates a numerically stable baseline run.
