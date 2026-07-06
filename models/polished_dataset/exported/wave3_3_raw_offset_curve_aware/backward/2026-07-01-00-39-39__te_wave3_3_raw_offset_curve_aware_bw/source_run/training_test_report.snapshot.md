# Wave3 3 Raw Offset Curve Aware Bw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_bw`
- Model Family: `wave3_3_raw_offset_curve_aware_bw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-01-00-39-39__te_wave3_3_raw_offset_curve_aware_bw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=160-val_mae=0.00176783.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004966`
- val_mae: `0.001768`
- val_rmse: `0.002185`
- val_pointwise_loss: `0.004847`
- val_centered_curve_shape_loss: `0.004581`
- val_curve_offset_loss: `0.000266`
- val_curve_amplitude_loss: `0.036676`
- val_sparse_harmonic_shape_loss: `0.000102`
- val_structured_mae: `0.005165`
- val_structured_rmse: `0.005559`
- val_residual_offset_mean_abs: `0.004459`

## Test Metrics

- test_loss: `0.005738`
- test_mae: `0.001898`
- test_rmse: `0.002445`
- test_pointwise_loss: `0.005611`
- test_centered_curve_shape_loss: `0.005327`
- test_curve_offset_loss: `0.000283`
- test_curve_amplitude_loss: `0.042259`
- test_sparse_harmonic_shape_loss: `0.000111`
- test_structured_mae: `0.005374`
- test_structured_rmse: `0.005928`
- test_residual_offset_mean_abs: `0.004515`

## Interpretation

The held-out val error stayed finite with MAE=0.001768 deg and RMSE=0.002185 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001898 deg and RMSE=0.002445 deg, which indicates a numerically stable baseline run.
