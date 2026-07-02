# Periodic Mlp Harmonic Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_harmonic_bw`
- Model Family: `periodic_mlp_harmonic_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp_harmonic\2026-06-29-21-27-22__te_periodic_mlp_harmonic_bw\checkpoints\periodic_mlp-epoch=126-val_mae=0.00118841.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.001845`
- val_mae: `0.001188`
- val_rmse: `0.001537`
- val_pointwise_loss: `0.001845`
- val_centered_curve_shape_loss: `0.002170`
- val_curve_offset_loss: `0.000359`
- val_curve_amplitude_loss: `0.016290`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.003023`
- test_mae: `0.001342`
- test_rmse: `0.001807`
- test_pointwise_loss: `0.003023`
- test_centered_curve_shape_loss: `0.002970`
- test_curve_offset_loss: `0.001115`
- test_curve_amplitude_loss: `0.024233`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001188 deg and RMSE=0.001537 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001342 deg and RMSE=0.001807 deg, which indicates a numerically stable baseline run.
