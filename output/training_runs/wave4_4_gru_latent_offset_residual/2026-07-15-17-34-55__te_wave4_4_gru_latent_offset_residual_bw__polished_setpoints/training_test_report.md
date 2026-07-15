# Wave4 4 Gru Latent Offset Residual Bw Training And Testing Report

## Overview

- Run Name: `te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints`
- Model Family: `wave4_4_gru_latent_offset_residual_bw`
- Model Type: `latent_state_hysteresis_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave4_4_gru_latent_offset_residual/2026-07-15-17-34-55__te_wave4_4_gru_latent_offset_residual_bw__polished_setpoints/checkpoints/latent_state_hysteresis_probe-epoch=036-val_mae=0.00226526.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.006024`
- val_mae: `0.002265`
- val_rmse: `0.003109`
- val_pointwise_loss: `0.003062`
- val_centered_curve_shape_loss: `0.005632`
- val_curve_offset_loss: `0.000498`
- val_curve_amplitude_loss: `0.034721`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.033006`
- val_base_rmse: `0.037913`
- val_residual_offset_mean_abs: `0.012548`

## Test Metrics

- test_loss: `0.008407`
- test_mae: `0.002568`
- test_rmse: `0.003925`
- test_pointwise_loss: `0.004608`
- test_centered_curve_shape_loss: `0.006458`
- test_curve_offset_loss: `0.002887`
- test_curve_amplitude_loss: `0.038604`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.031022`
- test_base_rmse: `0.036223`
- test_residual_offset_mean_abs: `0.012019`

## Interpretation

The held-out val error stayed finite with MAE=0.002265 deg and RMSE=0.003109 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002568 deg and RMSE=0.003925 deg, which indicates a numerically stable baseline run.
