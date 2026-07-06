# Periodic Mlp Bw Training And Testing Report

## Overview

- Run Name: `te_periodic_mlp_bw`
- Model Family: `periodic_mlp_bw`
- Model Type: `periodic_mlp`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\periodic_mlp\2026-06-29-20-02-16__te_periodic_mlp_bw\checkpoints\periodic_mlp-epoch=094-val_mae=0.00165793.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.002807`
- val_mae: `0.001658`
- val_rmse: `0.002132`
- val_pointwise_loss: `0.002807`
- val_centered_curve_shape_loss: `0.003092`
- val_curve_offset_loss: `0.000406`
- val_curve_amplitude_loss: `0.046801`
- val_sparse_harmonic_shape_loss: `0.000000e+00`

## Test Metrics

- test_loss: `0.004076`
- test_mae: `0.001740`
- test_rmse: `0.002328`
- test_pointwise_loss: `0.004076`
- test_centered_curve_shape_loss: `0.003915`
- test_curve_offset_loss: `0.001239`
- test_curve_amplitude_loss: `0.060727`
- test_sparse_harmonic_shape_loss: `0.000000e+00`

## Interpretation

The held-out val error stayed finite with MAE=0.001658 deg and RMSE=0.002132 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001740 deg and RMSE=0.002328 deg, which indicates a numerically stable baseline run.
