# Periodic Mlp Harmonic Fw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_fw`
- Model Family: `periodic_mlp_harmonic_fw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_harmonic\2026-06-29-21-10-12__te_periodic_mlp_harmonic_fw\checkpoints\periodic_mlp-epoch=071-val_mae=0.00120864.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001899`
- val_mae: `0.001209`
- val_rmse: `0.001573`
- val_pointwise_loss: `0.001899`
- val_centered_curve_shape_loss: `0.002117`
- val_curve_offset_loss: `0.000425`
- val_curve_amplitude_loss: `0.022477`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003202`
- test_mae: `0.001360`
- test_rmse: `0.001845`
- test_pointwise_loss: `0.003202`
- test_centered_curve_shape_loss: `0.002944`
- test_curve_offset_loss: `0.001289`
- test_curve_amplitude_loss: `0.032772`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001209 deg and RMSE=0.001573 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001360 deg and RMSE=0.001845 deg, which indicates a numerically stable baseline run.
