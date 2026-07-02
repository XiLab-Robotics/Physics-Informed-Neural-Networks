# Wave3 3 Raw Offset Curve Aware Fw Training And Testing Report

## Overview

- Run Name: `te_wave3_3_raw_offset_curve_aware_fw`
- Model Family: `wave3_3_raw_offset_curve_aware_fw`
- Model Type: `curve_aware_harmonic_residual_offset_probe`
- Best Checkpoint: `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks\output\training_runs\wave3_3_raw_offset_curve_aware\2026-07-01-00-11-36__te_wave3_3_raw_offset_curve_aware_fw\checkpoints\curve_aware_harmonic_residual_offset_probe-epoch=092-val_mae=0.00183328.ckpt`

## Dataset Split

- Train Curves: `1356`
- Validation Curves: `388`
- Test Curves: `194`

## Validation Metrics

- val_loss: `0.004975`
- val_mae: `0.001833`
- val_rmse: `0.002258`
- val_pointwise_loss: `0.004843`
- val_centered_curve_shape_loss: `0.004549`
- val_curve_offset_loss: `0.000294`
- val_curve_amplitude_loss: `0.035755`
- val_sparse_harmonic_shape_loss: `0.000101`
- val_structured_mae: `0.006619`
- val_structured_rmse: `0.007033`
- val_residual_offset_mean_abs: `0.006089`

## Test Metrics

- test_loss: `0.005797`
- test_mae: `0.001953`
- test_rmse: `0.002499`
- test_pointwise_loss: `0.005629`
- test_centered_curve_shape_loss: `0.005257`
- test_curve_offset_loss: `0.000372`
- test_curve_amplitude_loss: `0.040801`
- test_sparse_harmonic_shape_loss: `0.000109`
- test_structured_mae: `0.007119`
- test_structured_rmse: `0.007595`
- test_residual_offset_mean_abs: `0.006560`

## Interpretation

The held-out val error stayed finite with MAE=0.001833 deg and RMSE=0.002258 deg, which indicates a numerically stable baseline run.
The held-out test error stayed finite with MAE=0.001953 deg and RMSE=0.002499 deg, which indicates a numerically stable baseline run.
