# Wave3 3 Raw Offset Curve Aware Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_fw__polished_actual_values`
- Model Family: `wave3_3_raw_offset_curve_aware_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `/scratch1/dferrari/Physics-Informed-Neural-Networks/output/training_runs/wave3_3_raw_offset_curve_aware/2026-07-12-02-24-38__te_wave3_3_raw_offset_curve_aware_fw__polished_actual_values/checkpoints/curve_aware_harmonic_residual_offset_probe-epoch=103-val_mae=0.00192801.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.005192`
- val_mae: `0.001928`
- val_rmse: `0.002692`
- val_pointwise_loss: `0.004988`
- val_centered_curve_shape_loss: `0.004534`
- val_curve_offset_loss: `0.000454`
- val_curve_amplitude_loss: `0.034120`
- val_sparse_harmonic_shape_loss: `9.988406e-05`
- val_structured_mae: `0.038239`
- val_structured_rmse: `0.044726`
- val_residual_offset_mean_abs: `0.038185`

## Test Metrics

- test_loss: `0.006287`
- test_mae: `0.002096`
- test_rmse: `0.003143`
- test_pointwise_loss: `0.006040`
- test_centered_curve_shape_loss: `0.005493`
- test_curve_offset_loss: `0.000548`
- test_curve_amplitude_loss: `0.038826`
- test_sparse_harmonic_shape_loss: `0.000109`
- test_structured_mae: `0.035191`
- test_structured_rmse: `0.042252`
- test_residual_offset_mean_abs: `0.035141`

## Interpretation

The held-out val error stayed finite with MAE=0.001928 deg and RMSE=0.002692 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.002096 deg and RMSE=0.003143 deg, which indicates a numerically stable baseline run.
