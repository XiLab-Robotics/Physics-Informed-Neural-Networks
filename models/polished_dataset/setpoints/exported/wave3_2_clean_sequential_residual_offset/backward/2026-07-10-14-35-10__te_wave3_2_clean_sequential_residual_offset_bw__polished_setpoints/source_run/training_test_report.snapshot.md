# Wave3 2 Clean Sequential Residual Offset Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints`
- Model Family: `wave3_2_clean_sequential_residual_offset_bw`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_2_clean_sequential_residual_offset/2026-07-10-14-35-10__te_wave3_2_clean_sequential_residual_offset_bw__polished_setpoints/checkpoints/sequential_residual_offset_probe-epoch=089-val_mae=0.00218161.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005839`
- val_mae: `0.002182`
- val_rmse: `0.003011`
- val_pointwise_loss: `0.005839`
- val_centered_curve_shape_loss: `0.005385`
- val_curve_offset_loss: `0.000455`
- val_curve_amplitude_loss: `0.058336`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.026199`
- val_base_rmse: `0.030888`
- val_residual_offset_mean_abs: `0.026122`

## Test Metrics

- test_loss: `0.009424`
- test_mae: `0.002499`
- test_rmse: `0.003890`
- test_pointwise_loss: `0.009424`
- test_centered_curve_shape_loss: `0.006301`
- test_curve_offset_loss: `0.003123`
- test_curve_amplitude_loss: `0.070674`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.024747`
- test_base_rmse: `0.029579`
- test_residual_offset_mean_abs: `0.024490`

## Interpretation

The held-out val error stayed finite with MAE=0.002182 deg and RMSE=0.003011 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002499 deg and RMSE=0.003890 deg, which indicates a numerically stable baseline run.
