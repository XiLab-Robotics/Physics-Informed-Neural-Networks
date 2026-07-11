# Wave3 3 Raw Offset Curve Aware Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_bw__polished_setpoints`
- Model Family: `wave3_3_raw_offset_curve_aware_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-12-00-59-31__te_wave3_3_raw_offset_curve_aware_bw__polished_setpoints/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=112-val_mae=0.00201121.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005517`
- val_mae: `0.002011`
- val_rmse: `0.002762`
- val_pointwise_loss: `0.005239`
- val_centered_curve_shape_loss: `0.004621`
- val_curve_offset_loss: `0.000618`
- val_curve_amplitude_loss: `0.032947`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.033557`
- val_structured_rmse: `0.038446`
- val_residual_offset_mean_abs: `0.033550`

## Test Metrics

- test_loss: `0.010058`
- test_mae: `0.002280`
- test_rmse: `0.003638`
- test_pointwise_loss: `0.008644`
- test_centered_curve_shape_loss: `0.005502`
- test_curve_offset_loss: `0.003142`
- test_curve_amplitude_loss: `0.043407`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.034290`
- test_structured_rmse: `0.039499`
- test_residual_offset_mean_abs: `0.034187`

## Interpretation

The held-out val error stayed finite with MAE=0.002011 deg and RMSE=0.002762 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002280 deg and RMSE=0.003638 deg, which indicates a numerically stable baseline run.
