# Wave3 1 Sequential Residual Offset Probe Global Training And Testing Report

## Overview

- Run Name: `te_wave3_1_sequential_residual_offset_probe_global`
- Model Family: `wave3_1_sequential_residual_offset_probe_global`
- Model Type: `sequential_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_1_sequential_residual_offset_probe\2026-06-30-16-02-20__te_wave3_1_sequential_residual_offset_probe_global\checkpoints\sequential_residual_offset_probe-epoch=101-val_mae=0.00214720.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005739`
- val_mae: `0.002147`
- val_rmse: `0.002669`
- val_pointwise_loss: `0.005739`
- val_centered_curve_shape_loss: `0.005393`
- val_curve_offset_loss: `0.000346`
- val_curve_amplitude_loss: `0.059854`
- val_sparse_harmonic_shape_loss: `0.000000e+00`
- val_base_mae: `0.021357`
- val_base_rmse: `0.024549`
- val_residual_offset_mean_abs: `0.021207`

## Test Metrics

- test_loss: `0.006566`
- test_mae: `0.002261`
- test_rmse: `0.002896`
- test_pointwise_loss: `0.006566`
- test_centered_curve_shape_loss: `0.006234`
- test_curve_offset_loss: `0.000332`
- test_curve_amplitude_loss: `0.065781`
- test_sparse_harmonic_shape_loss: `0.000000e+00`
- test_base_mae: `0.020289`
- test_base_rmse: `0.023863`
- test_residual_offset_mean_abs: `0.020130`

## Interpretation

The held-out val error stayed finite with MAE=0.002147 deg and RMSE=0.002669 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002261 deg and RMSE=0.002896 deg, which indicates a numerically stable baseline run.
